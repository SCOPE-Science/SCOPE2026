#!/usr/bin/env python3
"""Exact finite-graph checks for run-bounded binary shift endomorphisms."""
from collections import Counter, deque
from itertools import product
import csv
import io
from pathlib import Path

CRITICAL_SETS = [
    (0,), (1,2,4), (2,5), (1,3,4,6), (3,5,6),
    (1,3,4,7), (1,3,6,7), (1,4,6,7), (3,4,6,7),
]


def local(r, a, b, c):
    return (r >> ((a << 2) | (b << 1) | c)) & 1


def preservation(k,r):
    for bits in product((0,1), repeat=k+2):
        if any(all(bits[j:j+k]) for j in range(3)):
            continue
        if all(local(r,*bits[i:i+3]) for i in range(k)):
            return False
    return True


def forbid_mask(k,bits):
    s=set()
    for i in range(k):
        s.add((bits[i]<<2)|(bits[i+1]<<1)|bits[i+2])
    return tuple(sorted(s))


def antichain(k):
    possible=set()
    for b in product((0,1),repeat=k+2):
        if any(all(b[j:j+k]) for j in range(3)): continue
        possible.add(frozenset(forbid_mask(k,b)))
    return set(tuple(sorted(z)) for z in possible if not any(t<z for t in possible))


def graph_structural_check(r):
    # Remove the 111 self-loop; there must be no remaining cycles.
    out={s:[] for s in range(4)}
    for t in range(7):
        if r>>t&1:out[t>>1].append((t&3,t&1))
    paths=[]
    for start in range(4):
        def visit(v,w,used):
            paths.append(w)
            for nxt,bit in out[v]:
                assert nxt not in used, ('unexpected cycle',r,w,nxt)
                visit(nxt,w+str(bit),used|{nxt})
        visit(start,f'{start:02b}',{start})
    if r&128:
        for w in paths:
            # Any path touching 11 admits loops at that vertex.
            if '11' in w:
                c=max(len(seg) for seg in w.split('0'))
                e=len(w)-2
                assert e<=c,(r,w,e,c)


def subset_min_missing(k,r):
    m=max(2,k-1)
    ns=1<<m
    state_mask=ns-1
    nextstates=[[set(),set()] for _ in range(ns)]
    for s in range(ns):
        for b in (0,1):
            if (((s<<1)|b)&((1<<k)-1))==((1<<k)-1):
                continue
            t=((s<<1)|b)&state_mask
            a=local(r,(s>>1)&1,s&1,b)
            nextstates[s][a].add(t)
    # full predecessor-set closure with legal-output trailing-run state
    trans_cache={}
    def step(v,a):
        key=(v,a)
        if key not in trans_cache:
            u=0
            for s in range(ns):
                if v>>s&1:
                    for t in nextstates[s][a]:u|=1<<t
            trans_cache[key]=u
        return trans_cache[key]
    initial=(1<<ns)-1
    q=deque([(initial,0,'')])
    visited={(initial,0)}
    while q:
        v,ones,w=q.popleft()
        for a in (0,1):
            if a and ones==k-1:continue
            t=step(v,a)
            if t==0:return w+str(a),len(visited)
            z=(t,ones+1 if a else 0)
            if z not in visited:
                visited.add(z)
                q.append((t,z[1],w+str(a)))
    return None,len(visited)


def direct_words(k,r,n):
    found=set()
    for b in product((0,1),repeat=n+2):
        if any(all(b[j:j+k]) for j in range(n+3-k)):continue
        found.add(''.join(str(local(r,*b[i:i+3])) for i in range(n)))
    return found


def legal_words(k,n):
    return {''.join(map(str,w)) for w in product((0,1),repeat=n) if not any(all(w[i:i+k]) for i in range(n+1-k))}


def full_shift_min_missing(r):
    for n in range(1,7):
        if len(direct_words(100,r,n))<2**n:
            return sorted(legal_words(100,n)-direct_words(100,r,n))[0]
    return None


def periodic(prefix, n):
    return tuple(int(prefix[i%len(prefix)]) for i in range(n))


def explicit_witness(k,j):
    a=k-1
    patterns=[
        periodic('0',k+2),periodic('001',k+2),periodic('01',k+2),
        periodic('0011',k+2),periodic('011',k+2),
        tuple(map(int,'100'+'1'*a)),tuple(map(int,'00'+'1'*a+'0')),
        tuple(map(int,'1'*a+'001')),tuple(map(int,'0'+'1'*a+'00')),
    ]
    return patterns[j]


def run():
    assert antichain(4)==set(CRITICAL_SETS)
    for k in range(4,13):
        for i,S in enumerate(CRITICAL_SETS):
            w=explicit_witness(k,i)
            assert len(w)==k+2 and not any(all(w[j:j+k]) for j in range(3))
            assert set(forbid_mask(k,w))<=set(S),(k,i,w,S)
    preserving={k:{r for r in range(256) if preservation(k,r)} for k in range(3,9)}
    assert len(preserving[3])==62
    for k in range(4,9):
        assert len(preserving[k])==70
        assert preserving[k]==preserving[4]
    for r in preserving[4]: graph_structural_check(r)
    # Exact equivalence with the nine masks, including every k>=4 by the graph lemma.
    for r in range(256):
        bad=any(all(r>>t&1 for t in S) for S in CRITICAL_SETS)
        assert bad == (r not in preserving[4])
    expected={
        3:{0:6,1:2,2:24,3:6,4:8,5:6,6:8,7:2},
        4:{0:3,1:1,2:19,3:33,4:6,5:4,6:2,8:2},
        5:{0:3,1:1,2:12,3:34,4:18,5:2},
        6:{0:3,1:1,2:12,3:24,4:24,5:6},
        7:{0:3,1:1,2:12,3:24,4:19,5:9,6:2},
        8:{0:3,1:1,2:12,3:24,4:19,5:8,6:3},
    }
    rows=[]
    maxstates=0
    for k in range(3,9):
        dist=Counter()
        for r in sorted(preserving[k]):
            w,nstates=subset_min_missing(k,r)
            maxstates=max(maxstates,nstates)
            d=len(w) if w else 0
            dist[d]+=1
            rows.append([str(k),str(r),str(d),w or '',str(nstates)])
            if w:
                assert w in legal_words(k,len(w))
            # Independent direct input enumeration through the predicted threshold.
            for n in range(1,max(d,1)+1):
                absent=legal_words(k,n)-direct_words(k,r,n)
                assert bool(absent)==(w is not None and n>=d),(k,r,n)
                if n==d:assert w in absent
        assert dict(dist)==expected[k],(k,dist,expected[k])
    # k >= 9: any eight-symbol input word is legal, hence every output
    # word through length 6 has full-shift preimages exactly as in the full shift.
    for r in sorted(preserving[4]):
        w=full_shift_min_missing(r)
        w8,_=subset_min_missing(8,r)
        assert w8 is None if w is None else (len(w8)==len(w))
        assert (w is None)==(r in {170,204,240})
        rows.append(['9+',str(r),str(len(w) if w else 0),w or '', 'full-shift length <=6'])
    # Directly verify exact agreement between the k=8 and full-shift first missing word lengths.
    for r in preserving[4]:
        w8,_=subset_min_missing(8,r)
        w=full_shift_min_missing(r)
        assert (len(w8) if w8 else 0)==(len(w) if w else 0)
    buf=io.StringIO(newline='')
    writer=csv.writer(buf,lineterminator='\n')
    writer.writerow(['k','wolfram_rule','shortest_missing_length','witness','reachable_pair_states'])
    writer.writerows(rows)
    output=buf.getvalue()
    target=Path(__file__).with_name('classification.csv')
    if target.exists():
        assert target.read_text(encoding='utf-8')==output
    else:
        target.write_text(output,encoding='utf-8')
    print('VERIFY_OK: 62/70/70/70/70/70 preserving rule codes k=3..8; only shifts onto;')
    print('first missing maxima k=3..8: 7,8,5,5,6,6; exact k>=9 full-shift reduction;')
    print('nine all-k violation masks and loop-free graph proof certificate;')
    print('independent direct finite-preimage enumeration and classification CSV;')
    print('maximum reachable pair-subsets:',maxstates)

if __name__=='__main__':run()
