"""Direct reproducible checks for optimal identifying codes of cycles.

Run: python3 verify.py. Uses only Python's standard library.
Finite tests corroborate, and do not replace, the symbolic proof.
"""
from collections import Counter, deque
from itertools import combinations


def is_identifying(n, mask):
    seen = set()
    for i in range(n):
        s = mask & ((1 << ((i - 1) % n)) | (1 << i) | (1 << ((i + 1) % n)))
        if not s or s in seen:
            return False
        seen.add(s)
    return True


def local_criterion(n, mask):
    for i in range(n):
        if not any(mask & (1 << ((i + j) % n)) for j in range(3)):
            return False
        if not ((mask >> i) & 1 or (mask >> ((i+3) % n)) & 1):
            return False
    return True


def orbit(n, word):
    assert len(word) == n
    mask = sum((int(ch) << i) for i, ch in enumerate(word))
    return [((mask << j) | (mask >> (n-j))) & ((1 << n) - 1) for j in range(n)]


def exchange_edges(codes):
    by_mask = set(codes)
    edges = set()
    for m in codes:
        ones = [i for i in range(m.bit_length()) if m & (1 << i)]
        all_n = max(codes).bit_length()
        for i in ones:
            gone = m ^ (1 << i)
            for j in range(all_n):
                if not (m & (1 << j)):
                    other = gone | (1 << j)
                    if other in by_mask:
                        edges.add(tuple(sorted((m, other))))
    return edges


def components(codes, edges):
    a = {m: set() for m in codes}
    for x, y in edges:
        a[x].add(y)
        a[y].add(x)
    result=[]
    while a:
        root=next(iter(a)); queue=[root]; seen={root}
        while queue:
            x=queue.pop()
            for y in a[x]:
                if y not in seen:
                    seen.add(y); queue.append(y)
        result.append(len(seen))
        for x in seen: del a[x]
    return sorted(result,reverse=True)


def canonical(n):
    assert n % 2 == 1 and n >= 13
    h = '1111' + '01' * ((n - 5)//2) + '0'
    l = '111' + '01' * ((n - 7)//2) + '1100'
    H, L = orbit(n,h), orbit(n,l)
    assert len(set(H)) == n and len(set(L)) == n and not (set(H) & set(L))
    E = orbit(15,'00111'*3) if n == 15 else []
    if E: E = list(set(E)); assert len(E) == 5
    return H, L, E


def predicted_edges(n,H,L):
    e=set()
    def connect(x,y):e.add(tuple(sorted((x,y))))
    for i in range(n):
        connect(H[i],H[(i+2)%n]);connect(H[i],H[(i-2)%n])
        connect(H[i],L[(i+1)%n]);connect(H[i],L[(i+5)%n])
    assert len(e)==3*n
    return e


def trace_poly(n):
    # Independent seven-state transfer-matrix trace, with weight t for appended 1.
    states=[s for s in range(1,8)]
    transitions={s:[] for s in states}
    for s in states:
        for d in (0,1):
            to=((s<<1)&7)|d
            if to and (((s>>2)&1)|d):
                transitions[s].append((to,d))
    count=Counter()
    for init in states:
        d={(init,0):1}
        for _ in range(n):
            nxt=Counter()
            for (state,weight),multiplicity in d.items():
                for to,bit in transitions[state]:nxt[(to,weight+bit)]+=multiplicity
            d=nxt
        for (state,weight),multiplicity in d.items():
            if state==init:count[weight]+=multiplicity
    return count


def main():
    for n in range(7,19):
        by_size=Counter()
        min_k=n+1
        winners=[]
        for mask in range(1<<n):
            ok=is_identifying(n,mask)
            assert ok == local_criterion(n,mask),(n,mask)
            if ok:
                k=mask.bit_count();by_size[k]+=1
                if k<min_k:min_k=k;winners=[mask]
                elif k==min_k:winners.append(mask)
        assert by_size==trace_poly(n),(n,by_size,trace_poly(n))
        es=exchange_edges(winners)
        if n%2==0:
            assert min_k==n//2 and len(winners)==2 and len(es)==0
            expected_components=[1,1]
        elif n>=13:
            assert min_k==(n+3)//2
            H,L,E=canonical(n)
            assert set(winners)==set(H+L+E),(n,len(winners),len(H+L+E))
            assert es==predicted_edges(n,H,L)
            expected_components=[2*n]+[1]*len(E)
        else:
            expected_components=components(winners,es)
        assert components(winners,es)==expected_components
        print(f'EXHAUSTIVE n={n} minimum={min_k} count={len(winners)} edges={len(es)} components={expected_components} CHECK_OK')
    for n in (19,21,23,25,31,41,51,99):
        H,L,E=canonical(n)
        allc=H+L+E
        assert len(set(allc))==2*n+len(E)
        assert all(is_identifying(n,m) for m in allc)
        real_edges=exchange_edges(allc)
        expected=predicted_edges(n,H,L)
        assert real_edges==expected
        assert components(allc,real_edges)==[2*n]+[1]*len(E)
        d=Counter()
        for a,b in real_edges:d[a]+=1;d[b]+=1
        assert sorted(Counter(d.values()).items())==[(2,n),(4,n)]
        print(f'PARAMETRIC n={n} count={len(allc)} edges={len(real_edges)} connected={len(E)==0} CHECK_OK')
    print('VERIFY_OK')

if __name__=='__main__':main()
