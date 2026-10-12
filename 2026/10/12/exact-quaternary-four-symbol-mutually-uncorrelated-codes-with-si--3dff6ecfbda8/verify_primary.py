"""Exact enumeration of cross-bifix-free, distance-two quaternary 4-codes.
Run: python3 verify_primary.py (Python 3, standard library only).
"""
from itertools import combinations, permutations, product

ALPHABET = range(4)

def eligible_words(A, B):
    return [w for w in product(ALPHABET, repeat=4)
            if w[0] in A and w[-1] in B
            and all(w[:r] != w[-r:] for r in (1,2,3))]

def compatible(u,v):
    return (sum(x != y for x,y in zip(u,v)) >= 2
            and all(u[:r] != v[-r:] and v[:r] != u[-r:]
                    for r in (1,2,3)))

def maximal_cliques(words):
    m=len(words)
    neighbors=[0]*m
    for i in range(m):
        for j in range(i):
            if compatible(words[i],words[j]):
                neighbors[i] |= 1 << j
                neighbors[j] |= 1 << i
    # Bron--Kerbosch with pivot: every maximal clique appears exactly once.
    def search(R,P,X):
        if P==0 and X==0:
            yield R
            return
        union=P|X
        pivot=-1
        max_n=-1
        while union:
            bit=union & -union; union-=bit
            j=bit.bit_length()-1
            score=(P & neighbors[j]).bit_count()
            if score>max_n: pivot,max_n=j,score
        todo=P & ~neighbors[pivot] if pivot>=0 else P
        while todo:
            bit=todo & -todo;todo-=bit
            j=bit.bit_length()-1
            yield from search(R|bit,P&neighbors[j],X&neighbors[j])
            P ^= bit
            X |= bit
    yield from search(0,(1<<m)-1,0)

def decode(mask, words):
    return frozenset(w for i,w in enumerate(words) if mask>>i & 1)

def main():
    all_optima=set()
    report=[]
    for r in (1,2,3):
        for A_t in combinations(ALPHABET,r):
            A=set(A_t);B=set(ALPHABET)-A
            words=eligible_words(A,B)
            maxsize=0; maxima=[]
            for mask in maximal_cliques(words):
                size=mask.bit_count()
                if size>maxsize:
                    maxsize=size;maxima=[]
                if size==maxsize:
                    maxima.append(decode(mask,words))
            report.append((tuple(sorted(A)),len(words),maxsize,len(maxima)))
            if maxsize==12: all_optima.update(maxima)
    assert len(report)==14
    assert sorted(x[2] for x in report)==[9]*8+[12]*6, report
    assert len(all_optima)==24, len(all_optima)
    # Classification under all symbol relabelings (not reversal of positions).
    def orbit(code):
        return {frozenset(tuple(p[c] for c in w) for w in code)
                for p in permutations(ALPHABET)}
    left=set(all_optima);orbits=[];reps=[]
    while left:
        code=min(left,key=lambda z:tuple(sorted(z)))
        o=orbit(code)
        assert o <= all_optima
        orbits.append(len(o))
        reps.append([''.join(map(str,w)) for w in sorted(code)])
        left-=o
    assert sorted(orbits)==[12,12],orbits
    print('PARTITION_REPORT',report)
    print('MAX_SIZE',12,'LABELED_MAXIMA',len(all_optima))
    print('SYMBOL_ORBIT_SIZES',sorted(orbits))
    for k,rep in enumerate(reps):print('ORBIT_REP',k+1,' '.join(rep))
    print('VERIFY_OK')
if __name__=='__main__': main()
