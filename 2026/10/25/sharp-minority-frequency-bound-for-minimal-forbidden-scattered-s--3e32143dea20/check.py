from itertools import product
from collections import Counter

def minimal_absent(w):
    seq={''}
    for c in w:
        seq |= {u+c for u in seq}
    return {v for u in seq for c in '01' if (v:=u+c) not in seq and all(v[:i]+v[i+1:] in seq for i in range(len(v)))}

def info(m):
    return {z:sum(t.endswith(z) for t in m) for z in ('0','1','00','11')}

seen=0
for n in range(0,15):
    for bits in product('01',repeat=n):
        w=''.join(bits)
        m=minimal_absent(w); k=w.count('1')
        a=info(m)
        assert len(m)<=2**(k+1),(w,len(m),k)
        assert a['0']<=2**k and a['1']<=2**k,(w,a,k)
        if w.endswith('1'):
            assert a['1']<=2**(k-1) and a['00']<=2**(k-1),(w,a,k)
        if w:
            p=w[:-1];prev=minimal_absent(p);b=info(prev)
            if w[-1]=='1' and '1' in p:
                assert a['1']==b['1'] and a['00']==b['00'],(w,a,b)
            if w[-1]=='0' and '0' in p:
                assert a['0']==b['0'],(w,a,b)
                if p.endswith('1'):
                    extra=b['00'] if len(p)-len(p.rstrip('1'))==1 else b['0']
                    assert a['1']==b['1']+extra,(w,a,b,extra)
        seen+=1
    print('checked length',n, flush=True)
for k in range(0,8):
    w='010'*k
    mm=minimal_absent(w)
    assert len(mm)==2**(k+1),(k,len(mm))
    print('witness k',k,'size',len(mm), flush=True)
print('VERIFY_OK',seen)
