"""Generate explicit comparison-query shattered trees; not required for verification."""
import itertools,functools,math,json,os
path=os.path.join(os.path.dirname(__file__),'permutation_witnesses.json')
out={}
for n in range(2,8):
    perms=list(itertools.permutations(range(n)))
    questions=list(itertools.combinations(range(n),2))
    universe=(1<<len(perms))-1
    positives=[]
    for a,b in questions:
        positives.append(sum(1<<i for i,p in enumerate(perms) if p.index(a)<p.index(b)))
    cap=math.factorial(n).bit_length()-1
    @functools.lru_cache(maxsize=None)
    def shatter(s,d):
        if d==0:return True
        if s.bit_count()<1<<d:return False
        for j,q in enumerate(positives):
            p=s&q;m=s&~q
            if p.bit_count()>=1<<(d-1) and m.bit_count()>=1<<(d-1):
                if shatter(p,d-1) and shatter(m,d-1):return True
        return False
    while not shatter(universe,cap): cap-=1
    def witness(s,d):
        if d==0:
            i=(s&-s).bit_length()-1
            return {'permutation':list(perms[i])}
        for j,q in enumerate(positives):
            p=s&q;m=s&~q
            if p.bit_count()>=1<<(d-1) and m.bit_count()>=1<<(d-1) and shatter(p,d-1) and shatter(m,d-1):
                return {'query':list(questions[j]),'zero':witness(m,d-1),'one':witness(p,d-1)}
        raise AssertionError('missing splitter')
    tree=witness(universe,cap)
    out[str(n)]={'depth':cap,'tree':tree}
    print('n',n,'d',cap,'hypotheses',len(perms),'cache',shatter.cache_info(),flush=True)
with open(path,'w',encoding='utf8') as f:json.dump({'description':'Explicit complete comparison-shattering trees for all linear orders of n labeled items. Query [a,b] returns one iff a precedes b.','certificates':out},f,separators=(',',':'));f.write('\n')
print('bytes',os.path.getsize(path))
