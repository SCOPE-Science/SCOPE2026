#!/usr/bin/env python3
"""Reproduce the finite symbolic transition certificate for a ternary digit-difference word."""
from itertools import product

ALPHABET = (0, 1, 2)
T8 = (0, 1, 1, 0, 1, 0, 0, 1)
TRIPLES = ((0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0))

def digit_parity(n):
    assert n >= 0
    return n.bit_count() & 1

def word_symbol(n):
    return 1 + digit_parity(n) - digit_parity(n + 1)

def block(a, b):
    t8 = tuple(v ^ a for v in T8) + (b,)
    return tuple(y for j in range(8) for y in (2*t8[j], 2-t8[j]-t8[j+1]))

def step(mask, symbol):
    mask |= (1 << symbol)
    return (1, 0) if mask == 7 else (0, mask)

def scan(word, initial_mask=0):
    m=initial_mask
    count=0
    counts=[0]
    for letter in word:
        more,m=step(m,letter)
        count += more
        counts.append(count)
    return counts,m

def certify():
    # Four 16-letter templates, determined solely by two adjacent binary digits.
    words = [block(a,b) for a,b in product((0,1), repeat=2)]
    assert len(set(words)) == 4
    assert all(len(w) == 16 and set(w) == set(ALPHABET) for w in words)
    # Exhaust all 8 potential masks, not merely reachable masks.
    for w in words:
        for mask in range(8):
            cnt,final=scan(w,mask)
            assert cnt[-1] == 5,(w,mask,cnt[-1])
        for letter in ALPHABET:
            cnt,final=scan(w,1<<letter)
            assert final == (1 << w[-1]),(w,letter,final)
    # All admissible triples: no triple 000 or 111 in Thue Morse.
    for a,b,c in TRIPLES:
        w=block(b,c)
        incoming=1 << (1+a-b)
        counts,last=scan(w,incoming)
        expected=[r//3 + int(r == 2 and a != b) for r in range(17)]
        assert counts == expected,(a,b,c,counts,expected)
        assert last == (1 << w[-1])
    init,fin=scan(block(0,1))
    assert init == [r//3 for r in range(17)]
    assert fin == 1
    # Independent recurrence construction of the square-free morphic word.
    subst=((0,1,2),(0,2),(1,))
    x=[0]
    for _ in range(14):
        x=[letter for z in x for letter in subst[z]]
    assert all(word_symbol(i)==z for i,z in enumerate(x)), 'difference-vs-morphism mismatch'
    # Symbol scan and closed formula for all explicit positions.
    mask=count=0
    discrepancies=set()
    for n,z in enumerate(x,1):
        more,mask=step(mask,z)
        count += more
        k,r=divmod(n,16)
        rhs=5*k + r//3 + int(k>0 and r==2 and digit_parity(k-1)!=digit_parity(k))
        assert count==rhs,(n,count,rhs)
        discrepancies.add(16*count-5*n)
    assert min(discrepancies)==-10 and max(discrepancies)==6
    # Independent subsequence enumeration for short prefixes; monotone embedding.
    for n in range(0,23):
        word=x[:n]
        k,r=divmod(n,16)
        u=5*k+r//3+int(k>0 and r==2 and digit_parity(k-1)!=digit_parity(k))
        for length in range(u+2):
            exists_all = True
            for test in product(ALPHABET,repeat=length):
                cursor=0
                for z in word:
                    if cursor<len(test) and z==test[cursor]:cursor+=1
                if cursor<len(test):
                    exists_all=False
                    break
            assert exists_all == (length<=u),(n,length,u,exists_all)
    print('VERIFY_OK templates=4 masks=8 triples=6 prefix_count='+str(len(x))+' brute_prefixes=0..22 discrepancy_min=-10 discrepancy_max=6')

if __name__=='__main__':certify()
