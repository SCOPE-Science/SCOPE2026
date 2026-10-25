"""Independent finite checks for synchronous binary majority dynamics on K_(p,q,r)."""
from itertools import product
from math import comb

def predict(ns):
    p1=2
    if all(n%2==0 for n in ns):
        p1+=comb(ns[0],ns[0]//2)*comb(ns[1],ns[1]//2)*comb(ns[2],ns[2]//2)
    p2 = int(max(ns)>sorted(ns)[-2])
    for i in range(3):
        for j in range(i+1,3):
            k=3-i-j
            if ns[i]==ns[j]:
                p2+=sum(comb(ns[k],b) for b in range(ns[k]+1) if abs(2*b-ns[k])<ns[i])
    return p1,p2

def successor_macro(ns,a):
    total=sum(a);N=sum(ns)
    return tuple(ns[i] if 2*(total-a[i])>N-ns[i] else 0 if 2*(total-a[i])<N-ns[i] else a[i] for i in range(3))

def check_macro():
    checks=0
    for ns in product(range(1,13),repeat=3):
        fixed=0; twice=0
        C=[[comb(n,k) for k in range(n+1)] for n in ns]
        for a in product(*(range(n+1) for n in ns)):
            b=successor_macro(ns,a)
            if successor_macro(ns,b)==a:
                w=C[0][a[0]]*C[1][a[1]]*C[2][a[2]]
                twice+=w
                if b==a: fixed+=w
        predicted=predict(ns)
        assert (fixed,(twice-fixed)//2)==predicted,(ns, fixed, (twice-fixed)//2, predicted)
        checks+=1
    return checks

def successor_bits(ns,bits):
    # All vertices updated independently from the original state, not macro states.
    n=sum(ns);new=0
    for i in range(n):
        if i<ns[0]: lo,hi=0,ns[0]
        elif i<ns[0]+ns[1]:lo,hi=ns[0],ns[0]+ns[1]
        else:lo,hi=ns[0]+ns[1],n
        neighbors=n-(hi-lo)
        ones=sum((bits>>j)&1 for j in range(n) if not (lo<=j<hi))
        v=(1 if 2*ones>neighbors else 0 if 2*ones<neighbors else ((bits>>i)&1))
        new|=v<<i
    return new

def check_micro():
    cases=0;states=0
    for ns in product(range(1,12),repeat=3):
        n=sum(ns)
        if n>12: continue
        c1=c2=0
        for bits in range(1<<n):
            nxt=successor_bits(ns,bits)
            if nxt==bits:c1+=1
            elif successor_bits(ns,nxt)==bits:c2+=1
            states+=1
        assert c2%2==0
        assert (c1,c2//2)==predict(ns),(ns,c1,c2//2,predict(ns))
        cases+=1
    return cases,states

if __name__=='__main__':
    a=check_macro()
    b,c=check_micro()
    print(f'VERIFY_OK macro_part_triples={a} micro_part_triples={b} micro_configurations={c}')
