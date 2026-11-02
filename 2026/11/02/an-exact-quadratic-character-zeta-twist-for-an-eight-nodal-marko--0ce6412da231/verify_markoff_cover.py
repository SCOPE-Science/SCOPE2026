#!/usr/bin/env python3
"""Independent finite-field checks of the double-cover point-count identity.

No external libraries; enumerates all projective triples over each chosen prime field.
"""
from itertools import product

def inspect(p):
    assert p % 8 == 1
    ii = next(a for a in range(1, p) if a*a % p == p-1)
    pts = [(1,a) for a in range(p)] + [(0,1)]
    squares = {a*a % p for a in range(p)}
    mons=[]
    for X0,X1 in pts:
        mons.append((X0*X0 % p, X1*X1%p, X0*X1%p))
    ds=[[0]*(p+1) for _ in range(p+1)]
    ds2=[[0]*(p+1) for _ in range(p+1)]
    for a,(a0,a1,a01) in enumerate(mons):
        for b,(b0,b1,b01) in enumerate(mons):
            ds[a][b]=(a01*(b0-b1)+ii*b01*(a0-a1))%p
            ds2[a][b]=(a01*(b0-b1)-ii*b01*(a0-a1))%p
    N=U=nodes=0
    contradictions=[]
    for x,(x0,x1,x01) in enumerate(mons):
        for y,(y0,y1,y01) in enumerate(mons):
            for z,(z0,z1,z01) in enumerate(mons):
                f=(x1*y0*z0+x0*y1*z0+x0*y0*z1+x1*y1*z1-4*x01*y01*z01)%p
                if f:continue
                N+=1
                values=(ds[x][y],ds[x][z],ds[y][x],ds[y][z],ds[z][x],ds[z][y])
                nonzero=[v for v in values if v]
                if not nonzero:
                    nodes+=1
                    U+=1
                elif nonzero[0] in squares:
                    U+=1
                if nonzero and any((v in squares)!=(nonzero[0] in squares) for v in nonzero):
                    contradictions.append((x,y,z))
    X=2*U-nodes
    assert nodes==8,(p,nodes)
    assert not contradictions,(p,contradictions[:3])
    sigma=1 if (1+ii)%p in squares else -1
    assert X-N==8*p*sigma,(p,X,N,sigma)
    assert abs(X-(p*p+1))<=22*p
    assert abs(N-(p*p+1-8*p))<=22*p
    return dict(p=p,base_points=N,cover_image_points=U,ramification_points=nodes,cover_points=X,k3_trace=X-p*p-1,base_resolution_trace=N+8*p-p*p-1)

def main():
    for p in [17,41,73,89,97,113]:
        print(inspect(p),flush=True)
    print('MARKOFF_EIGHT_NODE_COVER_FINITE_FIELD_CHECKS_PASS')


# The following routine deliberately uses a distinct extension-field arithmetic path.
# It is called explicitly from a test harness, not from main(), to keep prime checks fast.
def inspect_quadratic_field(p, nonsquare):
    q=p*p
    def add(a,b):
        return (a%p+b%p)%p + p*((a//p+b//p)%p)
    def neg(a):return (-a%p)+p*((-(a//p))%p)
    # Multiplication in F_p[t]/(t^2-nonsquare)
    def mul(a,b):
        a0,a1=a%p,a//p; b0,b1=b%p,b//p
        return ((a0*b0+nonsquare*a1*b1)%p) + p*((a0*b1+a1*b0)%p)
    def sub(a,b):return add(a,neg(b))
    zero,one=0,1
    minusone=p-1
    ii=next(x for x in range(q) if mul(x,x)==minusone)
    squares={mul(x,x) for x in range(q)}
    points=[(one,x) for x in range(q)]+[(zero,one)]
    sq=[(mul(a,a),mul(b,b),mul(a,b)) for a,b in points]
    Ds=[[0]*(q+1) for _ in range(q+1)]
    for j,(A0,A1,A01) in enumerate(sq):
        for k,(B0,B1,B01) in enumerate(sq):
            Ds[j][k]=add(mul(A01,sub(B0,B1)),mul(ii,mul(B01,sub(A0,A1))))
    total=split=nodes=0
    for a,(a0,a1,aa) in enumerate(sq):
        for b,(b0,b1,bb) in enumerate(sq):
            for c,(c0,c1,cc) in enumerate(sq):
                f=add(add(add(mul(a1,mul(b0,c0)),mul(a0,mul(b1,c0))),mul(a0,mul(b0,c1))),mul(a1,mul(b1,c1)))
                f=sub(f,mul(4%p,mul(aa,mul(bb,cc))))
                if f!=0:continue
                total+=1
                values=[Ds[a][b],Ds[a][c],Ds[b][a],Ds[b][c],Ds[c][a],Ds[c][b]]
                nonzero=[v for v in values if v]
                if not nonzero:nodes+=1;split+=1
                else:
                    assert all((v in squares)==(nonzero[0] in squares) for v in nonzero)
                    if nonzero[0] in squares:split+=1
    assert nodes==8
    cover=2*split-8
    sigma=1 if add(one,ii) in squares else -1
    assert cover-total==8*q*sigma,(q,cover,total,sigma)
    assert abs(cover-q*q-1)<=22*q
    return {'q':q,'p':p,'nonsquare':nonsquare,'base_points':total,'cover_image_points':split,'cover_points':cover,'nodes':nodes}

if __name__=='__main__':
    main()
    for p,d in ((3,2),(5,2),(7,3)):
        print(inspect_quadratic_field(p,d),flush=True)
    print('MARKOFF_EIGHT_NODE_COVER_EXACT_DISCREPANCY_PASS')
