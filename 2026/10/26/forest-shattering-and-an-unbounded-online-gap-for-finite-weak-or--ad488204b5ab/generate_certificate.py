"""Generate independent explicit adaptive comparison trees for finite total preorders."""
import itertools,json
from functools import lru_cache
from pathlib import Path

def all_orders(n):
    ranks=[]
    for k in range(1,n+1):
        for t in itertools.product(range(k),repeat=n):
            if set(t)==set(range(k)):
                ranks.append(t)
    return ranks

def make(n,depth):
    hyp=all_orders(n)
    Q=[(i,j) for i in range(n) for j in range(n) if i!=j]
    masks={q:sum((1<<h) for h,p in enumerate(hyp) if p[q[0]]<p[q[1]]) for q in Q}
    ALL=(1<<len(hyp))-1
    @lru_cache(None)
    def feasible(s,d):
        if d==0:return bool(s)
        if s.bit_count()<(1<<d):return False
        for q in Q:
            one=s & masks[q]
            zero=s & (ALL ^ masks[q])
            if one and zero and feasible(zero,d-1) and feasible(one,d-1):return True
        return False
    if not feasible(ALL,depth):raise ValueError('certificate impossible')
    def tree(s,d):
        if d==0:
            idx=(s&-s).bit_length()-1
            return {'ranks':list(hyp[idx])}
        for q in Q:
            one=s & masks[q]
            zero=s & (ALL ^ masks[q])
            if one and zero and feasible(zero,d-1) and feasible(one,d-1):
                return {'query':list(q),'zero':tree(zero,d-1),'one':tree(one,d-1)}
        raise AssertionError('missing branch')
    result={'n':n,'depth':depth,'tree':tree(ALL,depth)}
    print('n',n,'hyp',len(hyp),'depth',depth,'states',feasible.cache_info().currsize)
    return result

out={'certificates':[make(3,3),make(4,5)]}
Path(__file__).with_name('adaptive_preorder_trees.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n',encoding='utf-8')
