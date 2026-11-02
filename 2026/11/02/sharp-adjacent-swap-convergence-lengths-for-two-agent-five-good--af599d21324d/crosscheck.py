"""Finite independent enumeration for 2-agent, 5-good RR adjacent swaps."""
from itertools import permutations
from collections import deque

M=5
orders=list(permutations(range(M)))
index={p:i for i,p in enumerate(orders)}
S=len(orders)
adj=[]
for p in orders:
    adj.append([index[p[:k]+(p[k+1],p[k])+p[k+2:]] for k in range(M-1)])

def rr(p,q):
    remaining=set(range(M))
    a=0
    for step in range(M):
        order=(p,q)[step%2]
        good=next(x for x in order if x in remaining)
        if step%2==0:a|=1<<good
        remaining.remove(good)
    return a

alloc=[[rr(p,q) for q in orders] for p in orders]
base_edges=[]
for i in range(S):
    for j in range(S):
        frm=i*S+j; out=[]; old=alloc[i][j]
        for who in (0,1):
            for dest in adj[i if who==0 else j]:
                ni,nj=(dest,j) if who==0 else (i,dest)
                new=alloc[ni][nj]
                if new==old:continue
                old_owned=old if who==0 else ((1<<M)-1)^old
                new_owned=new if who==0 else ((1<<M)-1)^new
                gain=new_owned&~old_owned
                loss=old_owned&~new_owned
                assert gain.bit_count()==loss.bit_count()==1
                out.append((ni*S+nj,who,gain.bit_length()-1,loss.bit_length()-1))
        base_edges.append(out)

def analyze(q):
    r2={good:k for k,good in enumerate(orders[q])}
    outgoing=[];degrees=[0]*(S*S)
    for frm,edges in enumerate(base_edges):
        chosen=[]
        for to,who,gain,loss in edges:
            improve=(gain<loss) if who==0 else (r2[gain]<r2[loss])
            if improve:
                chosen.append(to)
                degrees[to]+=1
        outgoing.append(chosen)
    todo=deque(i for i,d in enumerate(degrees) if not d)
    dist=[0]*(S*S)
    nseen=0
    while todo:
        frm=todo.popleft();nseen+=1
        for to in outgoing[frm]:
            dist[to]=max(dist[to],dist[frm]+1)
            degrees[to]-=1
            if not degrees[to]:todo.append(to)
    assert nseen==S*S
    # Longest path beginning from each state via reverse topological DP: recompute only if needed.
    memo={}
    def d(src):
        if src in memo:return memo[src]
        # Visit all descendants in acyclic graph, using explicit stack.
        stack=[(src,0)]
        while stack:
            node,pos=stack[-1]
            out=outgoing[node]
            if pos<len(out):
                stack[-1]=(node,pos+1)
                dst=out[pos]
                if dst not in memo:stack.append((dst,0))
            else:
                memo[node]=max((1+memo[t] for t in out),default=0)
                stack.pop()
        return memo[src]
    return max(dist),d(q),sum(map(len,outgoing))

max_all=max_truth=0
all_edges=0
for q in range(S):
    a,t,e=analyze(q)
    max_all=max(max_all,a);max_truth=max(max_truth,t);all_edges+=e
print('VERIFY_INDEPENDENT',len(base_edges),len(orders),max_all,max_truth,all_edges)
assert max_all==18 and max_truth==6 and all_edges==1_584_000

# Verify the independently supplied extremal improvement paths.
import json
from pathlib import Path
witness_file=Path(__file__).with_name('WITNESSES.json')
witnesses=json.loads(witness_file.read_text(encoding='utf-8'))
for name,rec in witnesses.items():
    states=rec['states']
    assert len(states)-1==rec['length']
    if name=='truth':
        assert states[0]['report_1']==rec['true_order_1']
        assert states[0]['report_2']==rec['true_order_2']
    for s in states:
        b1=tuple(int(z) for z in s['report_1'])
        b2=tuple(int(z) for z in s['report_2'])
        assert rr(b1,b2)==s['agent_1_bundle_mask']
    for before,after in zip(states,states[1:]):
        reports_b=(before['report_1'],before['report_2'])
        reports_a=(after['report_1'],after['report_2'])
        changed=[i for i in (0,1) if reports_b[i]!=reports_a[i]]
        assert len(changed)==1
        who=changed[0]
        positions=[k for k in range(M) if reports_b[who][k]!=reports_a[who][k]]
        assert len(positions)==2 and positions[1]==positions[0]+1
        old=before['agent_1_bundle_mask'];new=after['agent_1_bundle_mask']
        if who==1:old^=31;new^=31
        gain=new&~old;loss=old&~new
        assert gain.bit_count()==loss.bit_count()==1
        r=rec['true_order_1'] if who==0 else rec['true_order_2']
        assert r.index(str(gain.bit_length()-1))<r.index(str(loss.bit_length()-1))
print('WITNESSES_OK',len(witnesses['global']['states'])-1,len(witnesses['truth']['states'])-1)
