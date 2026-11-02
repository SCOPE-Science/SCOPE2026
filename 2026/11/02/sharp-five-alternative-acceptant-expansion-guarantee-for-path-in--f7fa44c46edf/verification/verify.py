"""Finite exact tests for acceptant expansions. Requires only Python standard library."""
from itertools import permutations
from collections import Counter


def choice_of_order(perm,n):
    pos=[0]*n
    for j,a in enumerate(perm):pos[a]=j
    out=[0]*(1<<n)
    for subset in range(1,1<<n):
        a=min((i for i in range(n) if subset>>i&1),key=lambda i:pos[i])
        out[subset]=1<<a
    return out


def all_choices(n):
    """Closure under pointwise union of total-order maximum rules."""
    m=(1<<n)-1
    generators=[]
    for p in permutations(range(n)):
        C=choice_of_order(p,n)
        generators.append(sum(v<<(n*S) for S,v in enumerate(C)))
    Z={0}
    for gen in generators:
        # snapshot is essential: every generator used no more than once
        Z.update({z|gen for z in Z})
    Z.discard(0)
    return Z


def decode(z,n):
    m=(1<<n)-1
    return [(z>>(n*S))&m for S in range(1<<n)]


def pi(C):
    size=len(C)
    return all(C[A|B]==C[C[A]|B] for A in range(size) for B in range(size))


def qaccepted(C,q):
    return all(C[S].bit_count()==min(q,S.bit_count()) for S in range(1,len(C)))


def extension(C,T):
    return all(c&~t==0 for c,t in zip(C,T))


def six_witness():
    priorities=[(2,0,1,3,4,5),(2,1,0,3,4,5),
                (4,0,1,3,2,5),(4,3,0,1,2,5),
                (5,1,0,3,2,4),(5,3,1,0,2,4)]
    C=[0]*64
    for p in priorities:
        G=choice_of_order(p,6)
        C=[a|b for a,b in zip(C,G)]
    assert C[63]==sum(1<<v for v in (2,4,5))
    assert C[63^(1<<2)]==sum(1<<v for v in (0,1,4,5))
    assert C[63^(1<<4)]==sum(1<<v for v in (0,2,3,5))
    assert C[63^(1<<5)]==sum(1<<v for v in (1,2,3,4))
    assert max(c.bit_count() for c in C)==4
    assert all(C[S]&~S==0 and C[S]!=0 for S in range(1,64))
    assert pi(C)
    # A 4-acceptant expansion must fix those 5-element choices,
    # and substitutability prohibits 0,1,3 at the full set.
    for t in (0,1,3):
        S=63^(1<<{0:5,1:4,3:2}[t])
        assert t in range(6) and not(C[S]>>t&1)
    # Exhaustively independently enumerate every 4-acceptant
    # possible set-valued rule, and check there is no PI superset.
    # For every 4-acceptant T, all sets <=4 are fixed; on each
    # 5-set the only freedom is the rejected item; full chooses 4.
    candidates=0
    for full_reject in __import__('itertools').combinations(range(6),2):
        full=63^sum(1<<i for i in full_reject)
        for code in range(6**6):
            k=code
            T=[0]*64
            T[63]=full
            for S in range(1,63):
                if S.bit_count()<=4:T[S]=S
                else:
                    # 5-element choice excludes one of five
                    options=[i for i in range(6) if S>>i&1]
                    T[S]=S^(1<<options[k%5]);k//=5
            # Not all codes unique, but all possible 5set choices
            if not extension(C,T):continue
            if pi(T):candidates+=1
        # Some codes intentionally redundant, still exhaustive
    assert candidates==0
    print('SIX_WITNESS_NO_EXPANSION',max(c.bit_count() for c in C))


def main():
    for n in range(1,6):
        Z=all_choices(n)
        D=[decode(z,n) for z in Z]
        assert all(pi(C) for C in D)  # independent path-independence test
        print('GROUND_SIZE',n,'PATH_INDEPENDENT',len(Z))
        for q in range(1,n+1):
            source=[C for C in D if max(c.bit_count() for c in C)<=q]
            accept=[C for C in source if qaccepted(C,q)]
            assert accept
            uncovered=0
            dist=Counter()
            for C in source:
                num=sum(extension(C,T) for T in accept)
                dist[num]+=1
                if num==0:uncovered+=1
            assert uncovered==0
            print('QUOTA',q,'SOURCE',len(source),'ACCEPTANT',len(accept),
                  'UNCOVERED',uncovered)
            if n==5 and q==3:
                print('FIVE_THREE_DISTRIBUTION',sorted(dist.items()))
    six_witness()
    print('VERIFICATION_OK')

if __name__=='__main__':main()
