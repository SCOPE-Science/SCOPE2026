"""Rotation-normalized palindrome-span and complement/reversal orbit census.
No third-party packages; exhaustive for binary order-five de Bruijn cycles.
"""
from collections import Counter

N=32

def canonical(s):
    return min(s[k:]+s[:k] for k in range(N))

def span(s):
    d=s+s+s
    for l in range(N,0,-1):
        if any(d[k:k+l]==d[k:k+l][::-1] for k in range(N)):
            return l
    raise AssertionError

def all_cycles():
    result=set()
    for f in range(1<<16):
        state=0
        seen=set()
        chars=[]
        for _ in range(N):
            if state in seen: break
            seen.add(state)
            chars.append(str(state>>4))
            t=state&15
            state=((state<<1)&31)|((state>>4)^((f>>t)&1))
        if len(chars)==N and state==0:
            result.add(canonical(''.join(chars)))
    assert len(result)==2048
    return result

def main():
    words=all_cycles()
    unvisited=set(words)
    table=Counter()
    while unvisited:
        s=min(unvisited)
        comp=''.join('1' if a=='0' else '0' for a in s)
        orbit={canonical(s),canonical(comp),canonical(s[::-1]),canonical(comp[::-1])}
        assert orbit.issubset(words)
        assert len(orbit) in (2,4)
        spans={span(t) for t in orbit}
        assert len(spans)==1
        table[(spans.pop(),len(orbit))]+=1
        unvisited-=orbit
    expectation={(7,2):14,(7,4):43,(8,2):4,(8,4):46,
        (9,2):6,(9,4):211,(10,4):32,(11,2):6,(11,4):95,
        (12,4):8,(13,2):2,(13,4):49,(15,4):12}
    assert dict(table)==expectation
    assert sum(v*size for (_,size),v in table.items())==2048
    for length in sorted({k[0] for k in table}):
        print(f'ORBIT length={length} size2={table[(length,2)]} size4={table[(length,4)]}')
    print('ORBIT_VERIFY_OK')

if __name__=='__main__': main()
