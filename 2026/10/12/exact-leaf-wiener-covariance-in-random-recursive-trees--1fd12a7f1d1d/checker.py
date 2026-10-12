from fractions import Fraction
from itertools import product

def harmonic_table(N):
    h=[Fraction(0)]*(N+1)
    for n in range(1,N+1):
        h[n]=h[n-1]+Fraction(1,n)
    return h

def means(n,h):
    a=n*(n+1)*h[n]-2*n*n
    s=n*(n+1)*h[n-1]-Fraction((n-1)*(7*n+6),4)
    b=n*h[n]-Fraction(n*(n+5),4)+Fraction(1,2)
    return a,s,b

def stats(parent):
    n=len(parent)-1
    children=[0]*(n+1)
    adj=[[] for _ in range(n+1)]
    sub=[1]*(n+1)
    for j in range(2,n+1):
        p=parent[j]
        children[p]+=1
        adj[p].append(j)
        adj[j].append(p)
    for j in range(n,1,-1):
        sub[parent[j]]+=sub[j]
    W=sum(sub[j]*(n-sub[j]) for j in range(2,n+1))
    leaves=[u for u in range(1,n+1) if children[u]==0]
    S=0
    for u in leaves:
        dist=[-1]*(n+1)
        dist[u]=0
        q=[u]
        for x in q:
            for y in adj[x]:
                if dist[y] < 0:
                    dist[y]=dist[x]+1
                    q.append(y)
        S += sum(dist[1:])
    return len(leaves),W,S

def run():
    h=harmonic_table(2000)
    trees=0
    enumeration_checks=0
    for n in range(2,10):
        vals=[]
        for choices in product(*[range(1,j) for j in range(2,n+1)]):
            parent=[0]*(n+1)
            for j,p in enumerate(choices,start=2):
                parent[j]=p
            vals.append(stats(parent))
        trees += len(vals)
        N=len(vals)
        EL=sum((Fraction(L,N) for L,W,S in vals),Fraction(0))
        EW=sum((Fraction(W,N) for L,W,S in vals),Fraction(0))
        ES=sum((Fraction(S,N) for L,W,S in vals),Fraction(0))
        ELW=sum((Fraction(L*W,N) for L,W,S in vals),Fraction(0))
        a,s,b=means(n,h)
        assert EL == Fraction(n,2)
        assert EW == a
        assert ES == s
        assert ELW-EL*EW == b
        enumeration_checks += 4

    recurrence_checks=0
    sign_checks=0
    for n in range(2,2000):
        a,s,b=means(n,h)
        an,sn,bn=means(n+1,h)
        assert an == (1+Fraction(2,n))*a+n
        assert sn == s+(1-Fraction(1,n))*Fraction(n,2)+n+Fraction(2,n)*a
        assert bn == Fraction(n+1,n)*b-Fraction((n-1)*(n-2),4*n)
        recurrence_checks += 3
        if n >= 4:
            assert b < 0
            sign_checks += 1

    print("VERIFY_OK")
    print(f"trees_enumerated={trees}")
    print(f"enumeration_moment_checks={enumeration_checks}")
    print(f"recurrence_checks={recurrence_checks}")
    print(f"sign_checks={sign_checks}")
    print("max_recurrence_n=2000")

if __name__=="__main__":
    run()
