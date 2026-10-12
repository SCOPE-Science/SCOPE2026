from itertools import combinations

def sums4(bs):
    return [bs[i]+bs[j] for i in range(4) for j in range(i+1,4)]

def has_witness(n, E):
    A=set(range(1,2*n,2))|set(E)
    # Every pair sum is at most 2n, so no witness needs an entry >=2n.
    for bs in combinations(range(1,2*n),4):
        if all(s in A for s in sums4(bs)):
            return True
    return False

brute=0
for n in range(6,13):
    safe=[]
    evens=list(range(2,2*n+1,2))
    for E in combinations(evens,3):
        if not has_witness(n,E):
            safe.append(E)
        brute+=1
    expected=(2,2*n-2,2*n)
    assert safe==[expected], (n,safe)

constructive=0
for n in range(6,201):
    odds=set(range(1,2*n,2))
    for a in range(6,2*n-3,2):
        if a<=n+1:
            bs=(1,2,a-2,a-1)
        else:
            bs=(a-n,n,a-n+1,n-1)
        assert len(set(bs))==4 and min(bs)>0
        ss=sums4(bs)
        assert all((s==a or s in odds) for s in ss), (n,a,bs,ss)
        assert all(1<=s<=2*n for s in ss)
        constructive+=1
    for E,bs in [
        ((4,2*n-2,2*n),(1,2,3,2*n-4)),
        ((2,4,2*n-2),(1,2,3,2*n-4)),
        ((2,4,2*n),(1,3,4,2*n-4)),
    ]:
        A=odds|set(E)
        assert len(set(bs))==4 and min(bs)>0
        assert all(s in A for s in sums4(bs)), (n,E,bs,sums4(bs))
        constructive+=1

print(f'VERIFY_OK brute_triples={brute} constructive_cases={constructive} n_bruteforce=6..12 n_formula=6..200')
