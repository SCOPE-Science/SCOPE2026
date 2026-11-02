#!/usr/bin/env python3
"""Builds complete online trees, independently checked by verify.py."""
from verify import concepts,matrix,littlestone
import json
from pathlib import Path

def build(n):
    C=concepts(n);q,masks=matrix(C);L,d=littlestone(masks,len(C))
    def tree(S,k):
        if k==0:
            return {'witness':(S & -S).bit_length()-1}
        for t,M in enumerate(masks):
            A=S&M;B=S^A
            if A and B and min(A.bit_count(),B.bit_count()) >= (1<<(k-1)) and L(A)>=k-1 and L(B)>=k-1:
                return {'query':t,'zero':tree(B,k-1),'one':tree(A,k-1)}
        raise AssertionError(('no tree',n,k,S.bit_count()))
    return {'n':n,'depth':d,'tree':tree((1<<len(C))-1,d)}

if __name__=='__main__':
    out={str(n):build(n) for n in (11,12)}
    Path(__file__).with_name('tree_certificate.json').write_text(json.dumps(out,separators=(',',':'),sort_keys=True)+'\n',encoding='utf8')
    print('CERTIFICATES_CREATED',[(k,v['depth']) for k,v in out.items()])
