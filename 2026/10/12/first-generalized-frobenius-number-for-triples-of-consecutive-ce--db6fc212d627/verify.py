"""Finite cross-check of 1-Frobenius values for centered-square triples.
Uses a weighted priority enumeration of coefficient pairs, separate from the proof.
Finite computational checks do not establish the unrestricted theorem.
"""
import heapq

def c(n):
    return 2*n*n+2*n+1

def second_apery_by_enumeration(a,b,cval):
    queue=[(0,0,0)]
    seen={(0,0)}
    reps=[[] for _ in range(a)]
    unfinished=a
    while unfinished:
        value,u,v=heapq.heappop(queue)
        r=value%a
        if len(reps[r])<2:
            reps[r].append(value)
            if len(reps[r])==2:
                unfinished-=1
        for uu,vv,g in ((u+1,v,b),(u,v+1,cval)):
            if (uu,vv) not in seen:
                seen.add((uu,vv))
                heapq.heappush(queue,(value+g,uu,vv))
    return [pair[1] for pair in reps]

def theorem_value(n):
    if n==3:
        return 506
    if n<=5:
        return 6*n**3+26*n*n+43*n+22
    return 8*n**3+20*n*n+16*n-2

def run():
    total=0
    for n in range(3,81):
        a,b,cval=[c(n+i) for i in range(3)]
        actual=second_apery_by_enumeration(a,b,cval)
        predicted=[None]*a
        for u in range(2*n+3):
            w=u*b
            delta=n+1 if u>=5 else 2*n+3
            assert predicted[w%a] is None
            predicted[w%a]=w+delta*a
        for v in range(1,n+2):
            for u in range(2*n-2):
                w=u*b+v*cval
                delta=n+1 if u>=5 else (n+2 if v==n+1 else 2*n+3)
                assert predicted[w%a] is None
                predicted[w%a]=w+delta*a
        assert all(x is not None for x in predicted)
        assert actual==predicted,(n,'apery_mismatch')
        assert max(actual)-a==theorem_value(n),(n,'formula_mismatch')
        total+=a
    print('VERIFY_OK')
    print('parameter_range_n_3_to_80=78')
    print('second_apery_residue_values_checked=',total)
    print('formula_branches_checked= n3,n4_n5,n6_to80')
    print('finite_check_not_infinite_proof=True')

if __name__=='__main__':
    run()
