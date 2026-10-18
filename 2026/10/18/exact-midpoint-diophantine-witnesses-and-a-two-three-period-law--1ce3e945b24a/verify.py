"""Standalone integer checks for midpoint Diophantine solutions along a recurrence."""
from math import gcd


def midpoint_direct(a, b):
    """Find the equation index by modular enumeration (small a,b only)."""
    assert gcd(a,b) == 1 and a < b
    m = (a-1)*(b-1)//2
    options = []
    for delta in (0,1):
        target=m-delta
        cand=[]
        for x in range(target//a + 1):
            if (target-a*x)%b == 0:
                cand.append((x,(target-a*x)//b))
        if cand:
            options.append((delta,cand))
    assert len(options)==1 and len(options[0][1])==1
    return options[0][0],options[0][1][0]


def alpha_beta_independent(a,b):
    t=pow(a,-1,b)
    s=(a*b+1-a*t)//b
    return t,s


def predict(k, a, b, length):
    assert k>=2 and 1<=a<b and gcd(a,b)==1
    alpha,beta=alpha_beta_independent(a,b)
    results=[]
    for i in range(length):
        assert 1<=alpha<b and 1<=beta<=a
        assert a*alpha+b*beta==a*b+1
        delta=0 if alpha%2==beta%2==1 else 1
        if not delta:
            x,y=(alpha-1)//2,(beta-1)//2
        else:
            x,y=(b-alpha-1)//2,(a-beta-1)//2
        assert x>=0 and y>=0
        assert a*x+b*y+delta == (a-1)*(b-1)//2
        results.append((a,b,alpha,beta,delta,x,y))
        c=k*b-a
        alpha,beta=k*alpha+beta-a,b-alpha
        a,b=b,c
    return results


def check():
    full=0;direct=0;period=0;indep=0
    for k in range(2,15):
        for a in range(1,25):
            for b in range(a+1,32):
                if gcd(a,b)>1:continue
                records=predict(k,a,b,18)
                full+=len(records)
                for i,(x,y,alpha,beta,delta,u,v) in enumerate(records):
                    assert alpha_beta_independent(x,y)==(alpha,beta)
                    indep+=1
                    if i+ (2 if k%2==0 else 3)<len(records):
                        period+=1
                        assert delta==records[i+(2 if k%2==0 else 3)][4]
                    if i<3 and y<=900:
                        d,xy=midpoint_direct(x,y)
                        assert d==delta and xy==(u,v)
                        direct+=1
                vals=[r[4] for r in records]
                if k%2==0:
                    assert all(vals[i]!=vals[i+1] for i in range(len(vals)-1))
                else:
                    assert all(sum(vals[i:i+3]) in (1,2) for i in range(len(vals)-2))
    # Normalize common factors; the gcd of successive recurrence terms persists.
    scaled_cases=0
    for k in range(2,13):
        for a,b in ((1,2),(2,3),(4,9),(5,7),(8,11)):
            canonical=predict(k,a,b,12)
            for d in (2,3,5,12):
                U,V=d*a,d*b
                for j in range(12):
                    assert gcd(U,V)==d
                    assert (U//d,V//d)==canonical[j][:2]
                    U,V=V,k*V-U
                    scaled_cases+=1
    print('PASS: normalized noncoprime-seed indices:',scaled_cases)
    print('PASS: state and witness checks:',full)
    print('PASS: independently recomputed modular inverses:',indep)
    print('PASS: parity-period comparisons:',period)
    print('PASS: exhaustive small Diophantine searches:',direct)

if __name__=='__main__':
    check()
