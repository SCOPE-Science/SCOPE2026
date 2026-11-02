"""Build explicit comparison trees for separable permutations (offline proof artifacts)."""
import itertools, json, functools
from pathlib import Path

BAD={(1,3,0,2),(2,0,3,1)}  # rank-zero encodings 2413,3142

def avoids(p):
    for sub in itertools.combinations(p,4):
        order={x:i for i,x in enumerate(sorted(sub))}
        if tuple(order[x] for x in sub) in BAD:return False
    return True

def build(n):
    perms=[p for p in itertools.permutations(range(n)) if avoids(p)]
    m=len(perms); qs=list(itertools.combinations(range(n),2))
    masks=[sum(1<<i for i,p in enumerate(perms) if p[a]<p[b]) for a,b in qs]
    full=(1<<m)-1; d=m.bit_length()-1
    @functools.lru_cache(None)
    def yes(s,depth):
        if depth==0:return True
        if s.bit_count() < (1<<depth):return False
        for q,ms in enumerate(masks):
            pos=s&ms;neg=s^pos
            if pos.bit_count()<(1<<(depth-1)) or neg.bit_count()<(1<<(depth-1)):continue
            if yes(neg,depth-1) and yes(pos,depth-1):return True
        return False
    assert yes(full,d), (n,m,d)
    def tree(s,depth):
        if depth==0:
            j=(s&-s).bit_length()-1
            return {'w': list(perms[j])}
        for q,ms in enumerate(masks):
            pos=s&ms;neg=s^pos
            if pos.bit_count()<(1<<(depth-1)) or neg.bit_count()<(1<<(depth-1)):continue
            if yes(neg,depth-1) and yes(pos,depth-1):
                return {'q':q,'zero':tree(neg,depth-1),'one':tree(pos,depth-1)}
        raise AssertionError
    return {'n':n,'count':m,'depth':d,'queries':[list(q) for q in qs],'tree':tree(full,d)}

cert={'description':'Explicit complete comparison-query trees; zero-based permutation values and query indices. A one-edge answer means value at the first queried position is smaller.','cases':[build(n) for n in range(1,8)]}
out=Path(__file__).with_name('certificates.json')
out.write_text(json.dumps(cert,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
print('CERTIFICATES_BUILT',out.stat().st_size,[(c['n'],c['count'],c['depth']) for c in cert['cases']])
