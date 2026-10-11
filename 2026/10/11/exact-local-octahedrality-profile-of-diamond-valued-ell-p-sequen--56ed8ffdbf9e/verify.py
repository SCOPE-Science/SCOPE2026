from fractions import Fraction as F

def l1(v):
    return sum(abs(x) for x in v)

def fibre(alpha,a):
    # alpha and a use mesh 1/24; boundary vectors use mesh 1/48
    E=48
    best=F(-1)
    n=int(a*E)
    for k in range(n+1):
        q=F(k,E)
        r=a-q
        for s1 in (-1,1):
            for s2 in (-1,1):
                u=(s1*q,s2*r)
                z=(alpha,1-alpha)
                m=min(l1((z[0]+u[0],z[1]+u[1])),
                      l1((z[0]-u[0],z[1]-u[1])))
                if m>best:
                    best=m
    return best

D=24
fibre_checks=0
for ia in range(D//2+1):
    alpha=F(ia,D)
    for ja in range(D+1):
        a=F(ja,D)
        got=fibre(alpha,a)
        want=1+max(F(0),a-2*alpha)
        assert got==want,(alpha,a,got,want)
        fibre_checks+=1

profile_checks=0
for p in (1,2,3,4,6,8):
    for ia in range(D//2+1):
        alpha=F(ia,D)
        vals=[]
        for ja in range(D+1):
            a=F(ja,D)
            m=1+max(F(0),a-2*alpha)
            vals.append(1-a**p+m**p)
        got=max(vals)
        want=max(F(2),(2*(1-alpha))**p)
        assert got==want,(p,alpha,got,want)
        profile_checks+=1

for p in (1,2,3,4,6,8):
    assert max(F(2),(2*(1-F(1,2)))**p)==2
    assert max(F(2),(2*(1-F(0)))**p)==2**p

print(
    "VERIFY_OK "
    f"fibre_checks={fibre_checks} profile_checks={profile_checks} "
    "outer_mesh=1/24 fibre_mesh=1/48"
)
