from itertools import combinations

def partitions(n, hi):
    if n==0:
        yield ()
    else:
        for first in range(min(n,hi),0,-1):
            for tail in partitions(n-first,first):
                yield (first,)+tail

def eligible():
    ans=[]
    for p in partitions(16,7):
        if len(p)<2 or p[0]+p[1]>7:continue
        possible={0}
        for d in p:possible|={x+d for x in possible}
        if 8 not in possible:ans.append(p)
    return ans
P=(4,3,3,3,3); Q=(3,3,3,3,3,1)
assert eligible()==[P,Q],eligible()

def has_eight(rows,width):
    for r in range(1,1<<len(rows)):
        degrees=[sum((rows[i]>>j)&1 for i in range(len(rows)) if (r>>i)&1) for j in range(width)]
        possible={0}
        for d in degrees: possible|={v+d for v in possible}
        if 8 in possible:return True
    return False

def count(R,C):
    w=len(C)
    opts=[]
    for d in R:
        opts.append([sum(1<<j for j in ix) for ix in combinations(range(w),d)])
    seen=0
    def rec(i,remain,rows):
        nonlocal seen
        if i==len(R):
            if any(remain):return
            seen+=1
            assert has_eight(rows,w),(R,C,rows)
            return
        nr=len(R)-i-1
        for mask in opts[i]:
            after=tuple(x-((mask>>j)&1) for j,x in enumerate(remain))
            if all(0<=z<=nr for z in after):rec(i+1,after,rows+(mask,))
    rec(0,C,())
    return seen

if __name__=='__main__':
    print('admissible_row_degrees',eligible())
    total=0
    for a,b in [(P,P),(P,Q),(Q,P),(Q,Q)]:
        x=count(a,b)
        total+=x
        print('pair',a,b,'count',x)
    assert total==57786,total
    print('EXHAUSTIVE_BIPARTITE_16_HALF_EIGHT_PASS',total)
