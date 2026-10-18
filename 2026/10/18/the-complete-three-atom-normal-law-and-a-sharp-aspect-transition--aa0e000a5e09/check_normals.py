"""Exact rational verification of the Euclidean-normal law for parallelograms.

All arithmetic uses fractions. Each of sixteen sign chambers is clipped from
[0,1]^2 and given the side/vertex normal count from geometric dot products.
"""
from fractions import Fraction as F
from itertools import product


def halfplane_clip(poly, aa, bb, cc):
    """Keep aa*x+bb*y+cc >= 0, with exact rational intersections."""
    if not poly:
        return []
    out=[]
    for i, Q in enumerate(poly):
        P=poly[i-1]
        vp=aa*P[0]+bb*P[1]+cc
        vq=aa*Q[0]+bb*Q[1]+cc
        if (vp < 0) != (vq < 0):
            d=vp-vq
            if d:
                t=vp/d
                out.append((P[0]+t*(Q[0]-P[0]),P[1]+t*(Q[1]-P[1])))
        if vq >= 0:
            out.append(Q)
    return out


def area(poly):
    return abs(sum(poly[i-1][0]*poly[i][1]-poly[i-1][1]*poly[i][0]
                   for i in range(len(poly)))/2) if len(poly)>=3 else F(0)


def exact_distribution(r,c):
    """r=long side/short side >=1, c=cos acute angle in [0,1)."""
    k=c/r
    ell=c*r
    planes=[(-F(1),-k,F(1)), (F(1),k,-k),
            (-ell,-F(1),F(1)), (ell,F(1),-ell)]
    distribution={4:F(0),6:F(0),8:F(0)}
    for mask in product((False,True),repeat=4):
        poly=[(F(0),F(0)),(F(1),F(0)),(F(1),F(1)),(F(0),F(1))]
        for is_true,(aa,bb,cc) in zip(mask,planes):
            if not is_true:
                aa,bb,cc=-aa,-bb,-cc
            poly=halfplane_clip(poly,aa,bb,cc)
            if not poly:
                break
        mass=area(poly)
        if mass==0:
            continue
        a1,a2,b1,b2=mask
        normals=2+sum(map(int,mask))+int(a1 and b2)+int(a2 and b1)
        assert normals in distribution,(r,c,mask,normals)
        distribution[normals]+=mass
    assert sum(distribution.values())==1,(r,c,distribution)
    return distribution


def predicted(r,c):
    k=c/r
    ell=c*r
    if ell<=1:
        p8=(1-k)*(1-ell)/(1-c*c)
        p4=c*c*(2-k-ell)/(1-c*c)
        p6=1-p4-p8
    else:
        p8=F(0)
        p6=(1-c*c)/ell
        p4=1-p6
    return {4:p4,6:p6,8:p8}


def main():
    qvals=list(map(F,['1','6/5','3/2','2','5/2','4','7','10']))
    cvals=list(map(F,['0','1/8','1/5','1/3','2/5','1/2','3/5','3/4','4/5','9/10']))
    count=0
    for r in qvals:
        for c in cvals:
            found=exact_distribution(r,c)
            theory=predicted(r,c)
            assert found==theory,(r,c,found,theory)
            count+=1
        c=1/r
        if c<1:
            assert exact_distribution(r,c)==predicted(r,c)
            count+=1
    # Check derivative and equality regimes symbolically at representative rationals.
    for c in [F(1,5),F(2,5),F(3,5),F(4,5)]:
        q=1/c
        before=predicted(F(1),c)
        critical=predicted(q,c)
        after=predicted(2*q,c)
        assert before[8]==(1-c)/(1+c)
        assert critical[8]==0 and critical[4]==c*c and critical[6]==1-c*c
        assert before[6]<critical[6] and after[6]<critical[6]
        assert before[4]>critical[4] and after[4]>critical[4]
    print(f'PARALLELOGRAM_NORMAL_EXACT_OK rational_chambers={count} phase_extrema=4')

if __name__=='__main__':
    main()

# This check deliberately uses physical Euclidean coordinates rather than the
# transformed chamber inequalities used in the exact polygon-area calculation.
def geometric_pointwise_check():
    import math, random
    rng=random.Random(2718281)
    matches=0
    for q,c in [(1.0,0.0),(1.0,0.6),(1.3,0.2),(2.0,0.6),(4.0,0.8)]:
        U=(q,0.0)
        V=(c,math.sqrt(1-c*c))
        verts=[(0.,0.), U,(U[0]+V[0],V[1]),V]
        def sub(x,y):return (x[0]-y[0],x[1]-y[1])
        def dot(x,y):return x[0]*y[0]+x[1]*y[1]
        for _ in range(250):
            x,y=rng.random(),rng.random()
            p=(x*U[0]+y*V[0],x*U[1]+y*V[1])
            n=0
            for i,a in enumerate(verts):
                b=verts[(i+1)%4];e=sub(b,a)
                t=dot(sub(p,a),e)/dot(e,e)
                if 1e-10<t<1-1e-10:n+=1
            for i,a in enumerate(verts):
                d_prev=sub(verts[(i-1)%4],a)
                d_next=sub(verts[(i+1)%4],a)
                w=sub(p,a)
                if dot(w,d_prev)>1e-10 and dot(w,d_next)>1e-10:n+=1
            k=c/q;ell=c*q
            aa=(x+k*y<1);bb=(x>k*(1-y))
            cc=(y+ell*x<1);dd=(y>ell*(1-x))
            predicted_n=2+sum(map(int,(aa,bb,cc,dd)))+int(aa and dd)+int(bb and cc)
            assert n==predicted_n,(q,c,x,y,n,predicted_n)
            matches+=1
    print(f'EUCLIDEAN_NORMAL_POINTWISE_OK cases={matches}')

if __name__=='__main__':
    geometric_pointwise_check()
