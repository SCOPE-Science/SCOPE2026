"""Independently tests finite threshold-graph open-neighborhood rank-three obstructions."""
from collections import defaultdict

def rows_of(word):
    n=len(word)+1
    rows=[0]*n
    for v,ch in enumerate(word,1):
        if ch=='1':
            for u in range(v):
                rows[u]|=1<<v
                rows[v]|=1<<u
    return tuple(rows)

def rank_ge_three(rows):
    n=len(rows)
    # Enumerate all different concepts, not multiple copies of twins.
    C=tuple(dict.fromkeys(rows))
    if len(C)<8:return False
    def rank2(C):
        if len(C)<4:return False
        for x in range(n):
            pos=[c for c in C if c & (1<<x)]
            if len(pos)>=2 and len(C)-len(pos)>=2:
                return True
        return False
    for x in range(n):
        yes=tuple(c for c in C if c & (1<<x))
        no=tuple(c for c in C if not c & (1<<x))
        if rank2(yes) and rank2(no):return True
    return False

def delete(rows,j):
    n=len(rows)
    return tuple(sum(((rows[i]>>k)&1)<<m for m,k in enumerate(t for t in range(n) if t!=j)) for i in range(n) if i!=j)

def degree_key(rows):return tuple(sorted(x.bit_count() for x in rows))

if __name__=='__main__':
    all_counts={}; mins={}
    for n in range(1,16):
        count=0;minimal=[]
        for code in range(1<<(n-1)):
            word=''.join('1' if code>>j&1 else '0' for j in range(n-1))
            rows=rows_of(word)
            if rank_ge_three(rows):
                count+=1
                if all(not rank_ge_three(delete(rows,v)) for v in range(n)):
                    minimal.append((word,degree_key(rows)))
        all_counts[n]=count
        mins[n]=minimal
        print('n=',n,'rank3=',count,'minimal=',minimal,flush=True)
    assert all_counts == {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:3,9:23,10:101,11:337,12:954,13:2426,14:5734,15:12878}
    assert mins[8]==[('1101010',(0,1,2,4,4,4,5,6)),('1010110',(0,2,3,4,4,5,6,6)),('1010101',(1,2,3,4,4,5,6,7))]
    assert mins[9]==[('11011011',(2,4,6,6,6,7,7,8,8))]
    assert all(not mins[n] for n in list(range(1,8))+list(range(10,16)))
    print('ALL_INDEPENDENT_CLASSIFICATION_CHECKS_PASS')
