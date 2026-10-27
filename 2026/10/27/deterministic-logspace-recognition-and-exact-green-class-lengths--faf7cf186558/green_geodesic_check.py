"""Independent small-instance Green-geodesic checker for free inverse monoids.

Enumerates words and Munn-tree profiles directly. Standard-library only.
Run: python3 green_geodesic_check.py
"""
from itertools import product

LETTERS = 'aAbB'
INV = {'a':'A','A':'a','b':'B','B':'b'}

def reduced(word):
    stack=[]
    for ch in word:
        if stack and stack[-1] == INV[ch]:
            stack.pop()
        else:
            stack.append(ch)
    return ''.join(stack)

def inverse(u):
    return ''.join(INV[t] for t in reversed(u))

def profiles(word):
    p=['']
    for a in word:
        p.append(reduced(p[-1]+a))
    S=set(p)
    e=len(S)-1
    def dist(x,y): return len(reduced(inverse(x)+y))
    diameter=max(dist(x,y) for x in S for y in S)
    ecc_start=max(dist('',x) for x in S)
    ecc_end=max(dist(p[-1],x) for x in S)
    hdist=dist('',p[-1])
    h=(tuple(sorted(S)),p[-1])
    r=tuple(sorted(S))
    l=tuple(sorted(reduced(inverse(p[-1])+x) for x in S))
    d=min(tuple(sorted(reduced(inverse(v)+x) for x in S)) for v in S)
    geom={'H':2*e-hdist,'R':2*e-ecc_start,
          'L':2*e-ecc_end,'D':2*e-diameter}
    return dict(H=h,R=r,L=l,D=d),geom

def main():
    mins={t:{} for t in 'HRLD'}
    tested=0
    # first pass: global minima among all words <= 6
    for size in range(7):
        for tup in product(LETTERS, repeat=size):
            word=''.join(tup)
            keys,values=profiles(word)
            tested+=1
            for typ in 'HRLD':
                k=keys[typ]
                mins[typ][k]=min(size,mins[typ].get(k, size))
    # second pass: compare exact brute-force shortest lengths with tree formulas
    for size in range(7):
        for tup in product(LETTERS, repeat=size):
            word=''.join(tup)
            keys,values=profiles(word)
            for typ in 'HRLD':
                target=mins[typ][keys[typ]]
                assert values[typ]==target, (
                    'MISMATCH',word,typ,values[typ],target)
    assert tested == sum(4**n for n in range(7))
    print('VERIFY_OK words='+str(tested)+' rank=2 lengths=0..6 types=H,R,L,D')
    print('distinct-class-profiles ' + ' '.join(t+':'+str(len(mins[t])) for t in 'HRLD'))

if __name__=='__main__':
    main()
