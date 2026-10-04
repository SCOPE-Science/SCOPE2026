from math import gcd

def cross(u,v):
    return (u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])

def reps(n,m):
    a=n*n-1; b=n*n+1; c=2*n**3
    out=[]
    for z in range(m//c+1):
        rem=m-c*z
        for x in range(rem//a+1):
            r=rem-a*x
            if r>=0 and r%b==0:
                out.append((x,r//b,z))
    return out

def noncollinear(rs):
    if len(rs)<3: return False
    p=rs[0]
    ds=[tuple(q[i]-p[i] for i in range(3)) for q in rs[1:]]
    for i in range(len(ds)):
        for j in range(i+1,len(ds)):
            if cross(ds[i],ds[j])!=(0,0,0):
                return True
    return False

for n in range(2,101,2):
    a=n*n-1; b=n*n+1; c=2*n**3
    M=(n+1)*(n**3-1)
    assert M==n**4+n**3-n-1
    assert gcd(gcd(a,b),c)==1
    u=(b,-a,0); v=(-n,-n,1)
    assert cross(u,v)==(-a,-b,-c)
    D=-n*n+n+1
    f=lambda t:n*n*abs(t)-t
    assert max(f(D)+c,f(D+2*n*n))==M
    D2=-n*n-n+1
    assert max(f(D2),f(D2+2*n*n)+c)==(n*n+1)*(n*n+n-1)
    assert (n*n+1)*(n*n+n-1)>M
    assert 2*(n**4-1)>M
    s0=(n,n*n-1,0); s1=(n*n+n+1,0,0); s2=(0,n*n-n-1,1)
    for s in (s0,s1,s2):
        assert a*s[0]+b*s[1]+c*s[2]==M
    assert tuple(s1[i]-s0[i] for i in range(3))==u
    assert tuple(s2[i]-s0[i] for i in range(3))==v

for n in (2,4,6,8,10,12):
    M=(n+1)*(n**3-1)
    first=None
    for m in range(1,M+1):
        if noncollinear(reps(n,m)):
            first=m
            break
    assert first==M,(n,first,M)

print("symbolic_identity_samples=50")
print("exhaustive_even_n=2,4,6,8,10,12")
print("first_noncollinear_degree_matches_formula=yes")
print("VERIFY_OK")
