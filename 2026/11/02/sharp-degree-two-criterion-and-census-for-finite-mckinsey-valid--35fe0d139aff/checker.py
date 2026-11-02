from itertools import combinations,product
from math import comb

def frame_valid(rows):
    n=len(rows)
    for vbits in range(1<<n):
        P={i for i in range(n) if (vbits>>i)&1}
        for w in range(n):
            box_diamond=all(any(x in P for x in rows[u]) for u in rows[w])
            diamond_box=any(all(x in P for x in rows[u]) for u in rows[w])
            if box_diamond and not diamond_box: return False
    return True

def criterion(rows):
    return all(any(len(rows[v])==1 for v in rows[w]) for w in range(len(rows)))

def formula(n):
    return sum(comb(n,k)*k**k*(comb(n,2)-comb(n-k,2))**(n-k) for k in range(1,n+1))

def test(n):
    rowopts=[set(s) for m in range(3) for s in combinations(range(n),m)]
    result=0
    for rows in product(rowopts,repeat=n):
        x=frame_valid(rows);y=criterion(rows)
        assert x==y, (n,rows,x,y)
        result+=x
    assert result==formula(n),(n,result,formula(n))
    print('n=',n,'frames=',len(rowopts)**n,'accepted=',result,'formula=',formula(n))
for n in range(1,5):test(n)
# bound 3 counterexample. 0 root, 1/2/3 two-outdegree intermediates, 4/5 singleton sinks
rows=[{1,2,3},{0,4},{4,5},{5,0},{4},{5}]
assert frame_valid(rows)
assert not criterion(rows)
print('sharp max outdegree 3 example n=6: all valid, fails degree2 local criterion')
