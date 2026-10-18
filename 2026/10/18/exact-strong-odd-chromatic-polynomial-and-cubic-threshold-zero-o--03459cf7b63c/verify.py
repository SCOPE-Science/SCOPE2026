"""Direct finite checks for strong-odd sunlet coloring counts."""
from itertools import product

def directly_strong_odd(colors,n):
    # order: cycle vertices 0..n-1; their private leaves n..2n-1
    for i in range(n):
        if colors[i] == colors[(i+1) % n] or colors[i] == colors[n+i]:
            return False
    for i in range(n):
        nbrs=(colors[(i-1)%n],colors[(i+1)%n],colors[n+i])
        for c in set(nbrs):
            if nbrs.count(c)%2 != 1:return False
    return True

def brute(n,k):
    return sum(directly_strong_odd(colors,n) for colors in product(range(k),repeat=2*n))

def exact_formula(n,k):
    q=k-3; r=4-k; L=1+q*(k-2)
    s0,s1=2,-q
    if n==0:s=s0
    elif n==1:s=s1
    else:
        for _ in range(2,n+1):
            s0,s1=s1,-q*s1+r*L*s0
        s=s1
    return (2*L**n+2*(k-1)*s+k*(k-3)*r**n+(k-1)*(k-2)*(-r)**n)//2

def transfer(n,k):
    if k<=1:return 0
    arcs=[(a,b) for a in range(k) for b in range(k) if a!=b]
    ix={a:i for i,a in enumerate(arcs)}
    total=0
    for x,start in enumerate(arcs):
        states={x:1}
        for _ in range(n):
            nxt={}
            for i,v in states.items():
                a,b=arcs[i]
                for c in range(k):
                    if c==b:continue
                    y=ix[(b,c)]; w=1 if a==c else k-3
                    nxt[y]=nxt.get(y,0)+v*w
            states=nxt
        total+=states.get(x,0)
    return total

def three_defect_count(n):
    ct=0
    for core in product(range(3),repeat=n):
        if any(core[i]==core[(i+1)%n] for i in range(n)):continue
        defects=sum(core[i-1]!=core[(i+1)%n] for i in range(n))
        if defects==3:ct+=1
    return ct

def main():
    raw=0
    for n in range(3,6):
        for k in range(1,5):
            b=brute(n,k); f=exact_formula(n,k)
            assert b==f,(n,k,b,f)
            raw+=k**(2*n)
    spectral=0
    for n in range(3,31):
        for k in range(1,9):
            t=transfer(n,k);f=exact_formula(n,k)
            assert t==f,(n,k,t,f)
            spectral+=1
    odd=0
    for n in range(3,14,2):
        observed=three_defect_count(n)
        expected=n*(n*n-1)//4
        assert observed==expected,(n,observed,expected)
        odd+=1
    for n in range(3,65):
        if n%2:assert exact_formula(n,3)==0 and exact_formula(n,4)==3**n-3
        else:assert exact_formula(n,2)==2 and exact_formula(n,3)==6
    print(f'VERIFICATION_OK raw_assignments={raw} transfer_cases={spectral} odd_defect_orders={odd} parity_orders=62')
if __name__=='__main__':main()
