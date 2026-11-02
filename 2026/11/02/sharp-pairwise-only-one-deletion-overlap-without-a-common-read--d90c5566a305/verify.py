"""Finite checks for a sharp pairwise-only one-deletion overlap theorem.
All algorithms use the literal channel definition. Run with Python 3.9+.
"""
from itertools import combinations, product

def delete_one(w):
    return {w[:i]+w[i+1:] for i in range(len(w))}

def insert_one(u):
    return {u[:i]+a+u[i:] for i in range(len(u)+1) for a in '01'}

def family(n):
    if n == 3:
        return {'001','010','100','101'}
    if n == 4:
        return {'0001','0010','0100','1000','1001'}
    if n < 3: raise ValueError('n must be at least 3')
    u='0010'; v='01001'; x='00110'; t='0'
    for m in range(5,n):
        u,v,x=u+t,v+t,x+t
        t='1' if t=='0' else '0'
    return (insert_one(u)-{x})|{v}

def check_family(n):
    C=family(n)
    assert len(C)==n+1, (n,len(C))
    D={w:delete_one(w) for w in C}
    assert all(D[a]&D[b] for a,b in combinations(C,2)),n
    assert not set.intersection(*D.values()),n
    return C

def check_syndromes(n):
    read_to_words={}
    for bits in product('01',repeat=n):
        w=''.join(bits)
        syndrome=sum((i+1)*int(bit) for i,bit in enumerate(w))%(n+1)
        for r in delete_one(w):
            prev=read_to_words.setdefault(r,{})
            assert syndrome not in prev or prev[syndrome]==w, (n,r,syndrome,w)
            prev[syndrome]=w
    return len(read_to_words)

def check_common_supersequence(m):
    sets={''.join(z):insert_one(''.join(z)) for z in product('01', repeat=m)}
    assert all(len(sets[a]&sets[b])<=2 for a,b in combinations(sets,2))

if __name__=='__main__':
    for m in range(1,9): check_common_supersequence(m)
    for n in range(1,14): check_syndromes(n)
    for n in range(3,251): check_family(n)
    for n in range(3,12):
        C=check_family(n)
        print('n=',n,'size=',len(C),'family=',','.join(sorted(C)) if n<=6 else 'verified')
    print('VERIFY_OK: all 3..250 sharp construction cases; all 1..13 VT color consistency; superstring two-bound 1..8')
