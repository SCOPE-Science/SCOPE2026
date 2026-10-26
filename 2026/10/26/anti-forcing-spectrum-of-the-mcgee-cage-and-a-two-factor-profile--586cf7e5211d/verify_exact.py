"""Exact anti-forcing census for the 24-vertex McGee (3,7)-cage.
Pure Python 3.10+. Every lower bound is an exhaustive finite check.
Run: python verify_exact.py [certificate.json]
"""
import hashlib
import itertools
import json
import sys
from collections import Counter

N = 24
OFFSETS = (12, 7, -7)


def graph_edges():
    e = {(min(i, (i+1) % N), max(i, (i+1) % N)) for i in range(N)}
    for i in range(N):
        j = (i + OFFSETS[i % 3]) % N
        e.add((min(i,j), max(i,j)))
    return tuple(sorted(e))


def all_matchings(E):
    neighbors = [set() for _ in range(N)]
    for a,b in E:
        neighbors[a].add(b); neighbors[b].add(a)
    full = (1 << N)-1
    def dfs(free, acc):
        if not free:
            yield tuple(sorted(acc))
            return
        a = (free & -free).bit_length()-1
        for b in sorted(neighbors[a]):
            if (free >> b) & 1:
                yield from dfs(free ^ (1 << a) ^ (1 << b), acc + ((min(a,b), max(a,b)),))
    return tuple(sorted(dfs(full, ())))


def factor_cycles(E, M):
    adj=[[] for _ in range(N)]
    for a,b in E:
        if (a,b) not in M:
            adj[a].append(b); adj[b].append(a)
    assert all(len(row)==2 for row in adj)
    seen=set(); lengths=[]
    for s in range(N):
        if s in seen: continue
        todo=[s]; seen.add(s); k=0
        for v in todo:
            k+=1
            for w in adj[v]:
                if w not in seen:
                    seen.add(w); todo.append(w)
        lengths.append(k)
    return sorted(lengths)


def evaluate(E, allM):
    rows=[]
    for i,match in enumerate(allM):
        matched=set(match)
        avail=[e for e in E if e not in matched]
        rivals=[set(m) for j,m in enumerate(allM) if j!=i]
        full=(1 << len(rivals))-1
        cover=[sum(1 << j for j,r in enumerate(rivals) if edge in r) for edge in avail]
        opt_count=0; opt_example=None; optimum=None
        # A candidate set anti-forces match iff it intersects every alternative
        # perfect matching. Every k-subset is tested; no MILP/heuristic is used.
        for k in range(0,7):
            count=0; witness=None
            for comb in itertools.combinations(range(len(avail)),k):
                mask=0
                for j in comb:
                    mask |= cover[j]
                if mask == full:
                    count+=1
                    if witness is None: witness=[list(avail[j]) for j in comb]
            if count:
                optimum=k; opt_count=count; opt_example=witness
                break
        if optimum is None:
            raise AssertionError('Unresolved anti-forcing number: '+str(i))
        rows.append({'matching_index':i,'matching':[list(e) for e in match],
                     'anti_forcing_number':optimum,'minimum_deletion_sets':opt_count,
                     'witness_deleted_edges':opt_example,
                     'complement_two_factor_lengths':factor_cycles(E,matched)})
    return rows


def main():
    E=graph_edges(); M=all_matchings(E)
    assert len(E)==36 and len(M)==60
    data={'graph':'McGee graph: LCF [12,7,-7]^8',
          'vertex_count':N,'edges':[list(e) for e in E],
          'perfect_matching_count':len(M), 'rows':evaluate(E,M)}
    spectrum=dict(sorted(Counter(row['anti_forcing_number'] for row in data['rows']).items()))
    refined=Counter((tuple(r['complement_two_factor_lengths']),r['anti_forcing_number']) for r in data['rows'])
    assert spectrum=={5:40,6:20},spectrum
    assert refined=={((8,8,8),5):8,((8,8,8),6):4,
                    ((12,12),6):6,((24,),5):32,((24,),6):10},refined
    data['summary']={'spectrum':spectrum,'refined_two_factor_spectrum':[
        {'complement_cycles':list(cs),'anti_forcing_number':af,'count':n}
        for (cs,af),n in sorted(refined.items())],
        'total_minimum_deletion_sets':sum(row['minimum_deletion_sets'] for row in data['rows'])}
    assert data['summary']['total_minimum_deletion_sets']==18200
    payload=(json.dumps(data,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode('utf-8')
    if len(sys.argv)>1:
        p=sys.argv[1]
        with open(p,'wb') as f:f.write(payload)
        assert open(p,'rb').read()==payload
    print('MATCHINGS',len(M),'ANTI_FORCING',spectrum,'TWO_FACTOR',dict(sorted(refined.items())),
          'MIN_CERTIFICATES',data['summary']['total_minimum_deletion_sets'])
    print('CERTIFICATE_SHA256',hashlib.sha256(payload).hexdigest())
    print('EXACT_ENUMERATION_OK')

if __name__=='__main__':main()
