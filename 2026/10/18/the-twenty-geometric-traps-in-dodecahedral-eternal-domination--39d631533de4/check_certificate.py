"""Crosscheck a finite safety-game certificate against a second exact enumeration."""
import json
import sys
from functools import lru_cache

cert_path = sys.argv[1] if len(sys.argv)>1 else 'certificate.json'
text_path = sys.argv[2] if len(sys.argv)>2 else 'matching_recompute_output.txt'
with open(cert_path,encoding='utf-8') as file:
    c=json.load(file)
with open(text_path,encoding='utf-8') as file:
    lines=[ln.strip().split() for ln in file if ln.strip()]
N=20
assert c['format']=='dodecahedral-eternal-domination-v1'
expected_edges=set()
for i in range(10):
    for a,b in [(i,(i+1)%10),(i,i+10),(i+10,10+(i+2)%10)]:
        expected_edges.add(tuple(sorted((a,b))))
assert set(tuple(x) for x in c['edges'])==expected_edges
assert c['vertices']==list(range(N))
adj=[1<<i for i in range(N)]
for u,v in expected_edges:
    adj[u] |= 1<<v
    adj[v] |= 1<<u


def members(s):
    return [i for i in range(N) if (s>>i)&1]


def dominating(s):
    cover=0
    for x in members(s):cover|=adj[x]
    return cover==(1<<N)-1


def move(s,t):
    a=members(s);b=members(t)
    if len(a)!=len(b):return False
    allowable=[sum(1<<j for j,v in enumerate(b) if (adj[u]>>v)&1) for u in a]
    @lru_cache(None)
    def rec(i,used):
        if i==len(a):return True
        z=allowable[i] & ~used
        while z:
            bit=z & -z;z-=bit
            if rec(i+1,used|bit):return True
        return False
    return rec(0,0)

results={}
fatal6={};fatal7={};masks7=set()
for items in lines:
    tag=items[0]
    if tag.startswith('D') and tag.endswith('_COUNT'):
        assert len(items)==2
        results[tag]=int(items[1])
    elif tag=='F6':
        assert len(items)==4
        fatal6[int(items[1])]=list(map(int,items[2:]))
    elif tag=='D7':
        assert len(items)==2
        masks7.add(int(items[1]))
    elif tag=='F7':
        assert len(items)==3
        fatal7[int(items[1])]=int(items[2])
    elif tag=='RESULT':
        results['RESULT']=' '.join(items[1:])
    else:raise AssertionError(items)

assert all(results[f'D{i}_COUNT']==0 for i in range(1,6))
assert c['dominating_counts_1_through_5']=={str(i):0 for i in range(1,6)}
assert len(c['dominating_six'])==10
assert len(c['dominating_seven'])==780
assert set(c['dominating_seven'])==masks7
assert fatal6=={s:list(v) for s,v in c['fatal_attacks_six']}
assert fatal7=={s:v for s,v in c['bad_seven']}
assert len(fatal7)==20
assert results['RESULT']=='D6=10 D7=780 BAD7=20 GOOD7=760 MINGOOD=26'
assert all(int(s).bit_count()==6 and dominating(int(s)) for s in c['dominating_six'])
assert all(s.bit_count()==7 and dominating(s) for s in masks7)

# The certificate's non-losing states are exactly all dominating seven-sets
# outside the explicitly enumerated, single-fatal-attack family.
good=masks7-set(fatal7)
seen=set()
for s,entries in c['good_seven_winning_response_table']:
    assert s in good and s not in seen
    seen.add(s)
    assert {a for a,t in entries}==set(range(N))-set(members(s))
    for a,t in entries:
        assert t in good and ((t>>a)&1)==1
        assert move(s,t)
assert seen==good

# Radius spheres independently from the graph edge list.
for attack in range(N):
    queue=[attack];distance={attack:0}
    for u in queue:
        for v in members(adj[u] & ~(1<<u)):
            if v not in distance:
                distance[v]=distance[u]+1
                queue.append(v)
    assert sorted(distance.values()).count(0)==1
    bad=sum(1<<v for v in range(N) if distance[v] in (1,4,5))
    assert fatal7[bad]==attack

print('certificate_crosscheck=PASS')
print('all_9880_witnessed_attacks_admit_simultaneous_injective_guard_moves=PASS')
print('all_20_distance_shell_traps_agree_with_second_enumeration=PASS')
print('all_six_guard_fatal_attacks_agree_with_second_enumeration=PASS')
