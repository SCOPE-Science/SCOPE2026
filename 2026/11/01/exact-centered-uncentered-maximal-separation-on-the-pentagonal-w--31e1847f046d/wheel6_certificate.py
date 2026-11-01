"""Self-contained exact-integer certificate for graph-ball maximal averages on W_6.

Run: python3 wheel6_certificate.py
All linearization and Sylvester tests use only exact Python integers.
"""
from itertools import product
from fractions import Fraction

N=6
V=tuple(range(N))

def adjacent(i,j):
    if i==j:return False
    if i==0 or j==0:return True
    return (i-j)%5 in (1,4)

def balls():
    out=[]
    for c in V:
        out.append((c,))
        out.append(tuple(i for i in V if i==c or adjacent(i,c)))
        out.append(V)
    return list(dict.fromkeys(out))

ALL_BALLS=balls()
assert len(ALL_BALLS)==12 # 6 singletons, 5 four-vertex rim balls, 1 full ball

def choices(centered):
    arr=[]
    for v in V:
        eligible=[]
        for b in ALL_BALLS:
            if v not in b:continue
            if centered and not (b==(v,) or b==tuple(i for i in V if i==v or adjacent(i,v)) or b==V):continue
            if b not in eligible:eligible.append(b)
        eligible.sort(key=lambda b:(len(b),b))
        arr.append(eligible)
    return arr

def row(b):
    assert 12%len(b)==0
    return tuple(12//len(b) if i in b else 0 for i in V)

def gram(selected):
    g=[[0]*N for i in V]
    for b in selected:
        a=row(b)
        for i in V:
            for j in V:
                g[i][j]+=a[i]*a[j]
    return g

def is_posdef_exact(Q):
    # Fraction-free leading-principal-minor elimination (Bareiss), no pivoting.
    a=[r.copy() for r in Q]
    prev=1
    for k in V:
        pivot=a[k][k]
        if pivot<=0:return False
        if k<N-1:
            for i in range(k+1,N):
                for j in range(k+1,N):
                    p=pivot*a[i][j]-a[i][k]*a[k][j]
                    assert p%prev==0
                    a[i][j]=p//prev
        prev=pivot
    return True

def check_enum(centered):
    options=choices(centered)
    expected=(2,3,3,3,3,3) if centered else (7,5,5,5,5,5)
    assert tuple(map(len,options))==expected
    bad=[]
    total=0
    for sel in product(*options):
        total+=1
        g=gram(sel)
        if centered:
            q=[[ (216 if i==j else 0)-g[i][j] for j in V] for i in V]
        else:
            # 144*(81/50)=5832/25
            q=[[ (5832 if i==j else 0)-25*g[i][j] for j in V] for i in V]
        if not is_posdef_exact(q):bad.append(sel)
    assert total==(486 if centered else 21875)
    if centered:
        expect=( (0,),)+tuple(tuple(i for i in V if i==v or adjacent(i,v)) for v in range(1,6))
        assert bad==[expect],(bad,expect)
    else:
        assert len(bad)==5
        assert all(s[0]==(0,) for s in bad)
        for s in bad:
            peaks=[i for i in range(1,6) if s[i]==(i,)]
            assert len(peaks)==1
            p=peaks[0]
            for v in range(1,6):
                if v==p:continue
                possible=[]
                for c in range(1,6):
                    b=tuple(i for i in V if i==c or adjacent(i,c))
                    if p in b and v in b:possible.append((c,b))
                # Among these centered balls, the unique selected ball has
                # the one closest rim center to p among centers covering v.
                assert s[v] in [z for c,z in possible]
            assert p in range(1,6)
        assert len(set(next(i for i in range(1,6) if s[i]==(i,)) for s in bad))==5
        def rotated(s,p):
            out=[None]*N
            def move(v):return (v-p)%5+1 if v else 0
            for v,b in enumerate(s):out[move(v)]=tuple(sorted(move(x) for x in b))
            return tuple(out)
        template=((0,),(1,),(0,1,2,5),(0,1,2,3),(0,1,4,5),(0,1,2,5))
        assert {rotated(s,next(i for i in range(1,6) if s[i]==(i,))) for s in bad}=={template}
        g=gram(template)
        expected_16=[[20,4,3,1,1,3],
                     [4,20,3,1,1,3],
                     [3,3,3,1,0,2],
                     [1,1,1,1,0,0],
                     [1,1,0,0,1,1],
                     [3,3,2,0,1,3]]
        assert all(g[i][j]==9*expected_16[i][j] for i in V for j in V)
    return total,len(bad),bad

def check_symbolic():
    # p(z)=64*z^3-120*z^2+27*z-1; bracket the Perron root.
    p=lambda z:64*z**3-120*z**2+27*z-1
    lo=Fraction(81,50);hi=Fraction(1621,1000)
    assert p(lo)<0<p(hi)
    assert 192*lo*lo-240*lo+27>0 and 384*lo-240>0
    d=lambda z:64*z*z-24*z+1
    assert d(lo)>0 and d(hi)>0
    # Exact eigenvector v=(1,1,y,z,z,y), y=(24z-1)/d, z=(8z-1)/d.
    # The three reduced eigen-equations, multiplied by d, are:
    # 16*lambda*d-24*d-6*(24lambda-1)-2*(8lambda-1)=16*p(lambda)
    # 16*lambda*(24lambda-1)-6*d-5*(24lambda-1)-(8lambda-1)=0
    # 16*lambda*(8lambda-1)-2*d-(24lambda-1)-(8lambda-1)=0.
    for k in [lo,hi,Fraction(5,3),Fraction(3,2)]:
        D=d(k)
        assert 16*k*D-24*D-6*(24*k-1)-2*(8*k-1)==16*p(k)
        assert 16*k*(24*k-1)-6*D-5*(24*k-1)-(8*k-1)==0
        assert 16*k*(8*k-1)-2*D-(24*k-1)-(8*k-1)==0
    # Check at interval endpoints that 0<z<y<1 throughout the root bracket.
    for k in (lo,hi):
        y=(24*k-1)/d(k)
        z=(8*k-1)/d(k)
        assert 0<z<y<1
    # Certified interval bounds for every selected ball at the positive
    # uncentered maximizing vector (1,1,y,z,z,y), without floating point.
    yl=(24*lo-1)/d(hi); yu=(24*hi-1)/d(lo)
    zl=(8*lo-1)/d(hi); zu=(8*hi-1)/d(lo)
    low=(Fraction(1),Fraction(1),yl,zl,zl,yl)
    high=(Fraction(1),Fraction(1),yu,zu,zu,yu)
    assert 0<zl<=zu<yl<=yu<1
    selected=((0,),(1,),(0,1,2,5),(0,1,2,3),(0,1,4,5),(0,1,2,5))
    for v,q in enumerate(choices(False)):
        b=selected[v]
        assert b in q
        selected_lower=sum(low[j] for j in b)/len(b)
        assert all(selected_lower>sum(high[j] for j in other)/len(other)
                   for other in q if other!=b)
    # Centered winner: at input (5,1,1,1,1,1), its output is (5,2,...,2),
    # so squared quotient is (25+5*4)/(25+5)=3/2 and all choices are strict.
    c=choices(True)
    vec=(5,1,1,1,1,1)
    assert max(Fraction(sum(vec[j] for j in b),len(b)) for b in c[0])==5
    for v in range(1,6):
        b=tuple(i for i in V if i==v or adjacent(i,v))
        assert Fraction(sum(vec[j] for j in b),len(b))==2
        assert all(Fraction(sum(vec[j] for j in other),len(other))<2 for other in c[v] if other!=b)
    assert Fraction(25+5*4,25+5)==Fraction(3,2)

if __name__=='__main__':
    c=check_enum(True)
    u=check_enum(False)
    check_symbolic()
    print('CERTIFICATE_OK centered_selections=%d centered_exceptions=%d uncentered_selections=%d uncentered_exceptions=%d'% (c[0],c[1],u[0],u[1]))
    print('CERTIFICATE_OK thresholds_centered=3/2 uncentered=81/50 cubic=64z^3-120z^2+27z-1 interval=(81/50,1621/1000)')
