"""Finite corroboration of a rectangular forbidden-line Morse construction.

Only standard-library arithmetic and finite combinatorics are used; the general
homotopy classification rests on the accompanying mathematical proof.
"""
from itertools import product


def valid(mask, a, b):
    for i in range(a):
        row = sum(1 << (i*b+j) for j in range(b))
        if mask & row == row:
            return False
    for j in range(b):
        col = sum(1 << (i*b+j) for i in range(a))
        if mask & col == col:
            return False
    return True


def match(a,b):
    faces={q for q in range(1<<(a*b)) if valid(q,a,b)}
    num=len(faces)
    matches=[]
    for i in range(a-1):
        for j in range(b):
            bit=1<<(i*b+j)
            pairs=[(q,q|bit) for q in faces if not q&bit and q|bit in faces]
            affected={u for pair in pairs for u in pair}
            assert len(affected)==2*len(pairs)
            faces.difference_update(affected)
            matches.extend(pairs)
    expected=sum(1 << (i*b+j) for i in range(a-1) for j in range(1,b))
    assert faces=={expected},(a,b,faces,expected)
    return num,len(matches)


def orbit_partition(perm):
    unseen=set(range(len(perm)))
    blocks=[]
    while unseen:
        x=min(unseen); block=[]
        while x in unseen:
            unseen.remove(x);block.append(x);x=perm[x]
        blocks.append(block)
    return blocks


def check_orbit_map(n, left, right):
    aa=orbit_partition(left);bb=orbit_partition(right)
    a,b=len(aa),len(bb)
    cells=[]
    for rows in aa:
        for cols in bb:
            cells.append(sum(1 << (i*n+j) for i in rows for j in cols))
    for mask in range(1<<(a*b)):
        expanded=0
        for z,t in enumerate(cells):
            if mask>>z&1:
                expanded|=t
        assert valid(mask,a,b)==valid(expanded,n,n),(n,left,right,mask)
    return a,b


def main():
    total=0
    for a in range(2,5):
        for b in range(2,5):
            faces,pairs=match(a,b)
            assert faces==2*pairs+1
            print('RECTANGLE',a,b,'faces',faces,'pairs',pairs,'critical_size',(a-1)*(b-1))
            total+=1
    permutations={
        3:[(0,1,2),(1,0,2),(1,2,0)],
        4:[(0,1,2,3),(1,0,2,3),(1,0,3,2),(1,2,3,0),(1,2,0,3)]
    }
    count=0
    for n,perms in permutations.items():
        for left,right in product(perms,repeat=2):
            a,b=check_orbit_map(n,left,right)
            if a==1 or b==1:
                assert all(not valid(1<<i,a,b) for i in range(a*b))
            count+=1
    print('RECTANGULAR_FIXED_ORBIT_CHECKS_OK',total,count)

if __name__=='__main__':main()
