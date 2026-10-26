"""Exact periodic-point spectrum check for elementary cellular-automaton images.

Run: python verify.py  (requires class_recurrences.csv, rule_catalog.csv).
Python standard library only. Finite-state Cayley-Hamilton certificates apply
for all positive periods, not merely the enumerated periods.
"""
import csv
from collections import defaultdict
from pathlib import Path

DIR=Path(__file__).resolve().parent

def edge_relations(rule):
    relations=[0,0]
    for triplet in range(8):
        source=triplet>>1
        target=triplet&3
        label=(rule>>triplet)&1
        relations[label] |= 1 << (4*source+target)
    return relations

def compose(left,right):
    out=0
    for source in range(4):
        intermediate=(left>>(source*4))&15
        targets=0
        for mid in range(4):
            if (intermediate>>mid)&1:
                targets |= (right>>(4*mid))&15
        out |= targets<<(4*source)
    return out

def has_cycle(rel):
    """Graph cycle test by explicit transitive-closure reachability."""
    reachable=[[(rel>>(4*i+j))&1 for j in range(4)] for i in range(4)]
    for mid in range(4):
        for i in range(4):
            if reachable[i][mid]:
                for j in range(4):
                    reachable[i][j] |= reachable[mid][j]
    return any(reachable[i][i] for i in range(4))

def graph(rule):
    lab=edge_relations(rule)
    identity=sum(1<<(5*i) for i in range(4))
    states=[identity]
    lookup={identity:0}
    edges=[]
    for state in states:
        next_ids=[]
        for label in range(2):
            other=compose(state,lab[label])
            if other not in lookup:
                lookup[other]=len(states)
                states.append(other)
            next_ids.append(lookup[other])
        edges.append(tuple(next_ids))
    return states,edges

def counts_and_certificate(rule, coeffs, first8):
    states,edges=graph(rule)
    length=len(states)
    degree=len(coeffs)-1
    accept=[int(has_cycle(s)) for s in states]
    vec=[0]*length
    vec[0]=1
    counts=[]
    # N consecutive equalities for a linear combination of p(n):
    # Cayley-Hamilton on the N-state transition operator proves all others.
    for n in range(max(length+degree,9)):
        counts.append(sum(vec[i] for i in range(length) if accept[i]))
        nxt=[0]*length
        for index,value in enumerate(vec):
            if value:
                a,b=edges[index]
                nxt[a]+=value
                nxt[b]+=value
        vec=nxt
    assert counts[0]==1, (rule,'empty word')
    assert counts[1:9]==first8, (rule,'initial counts',counts[1:9],first8)
    for n in range(degree, length+degree):
        assert sum(coeffs[j]*counts[n-j] for j in range(degree+1))==0, (rule,n)
    return length,counts[:degree],counts[1:9]

def independent_periodic_check(rule,n):
    """Independent expanded-phase graph cycle test: no Boolean product."""
    lab=edge_relations(rule)
    total=0
    for word in range(1<<n):
        adj=[[] for _ in range(n*4)]
        for phase in range(n):
            label=(word>>phase)&1
            for u in range(4):
                for v in range(4):
                    if lab[label]&(1<<(4*u+v)):
                        adj[4*phase+u].append(4*((phase+1)%n)+v)
        color=[0]*(n*4)
        def visit(u):
            color[u]=1
            for v in adj[u]:
                if color[v]==1:return True
                if color[v]==0 and visit(v):return True
            color[u]=2
            return False
        if any(color[v]==0 and visit(v) for v in range(n*4)):
            total+=1
    return total

def main():
    with (DIR/'class_recurrences.csv').open(newline='',encoding='utf-8') as fh:
        classes=list(csv.DictReader(fh))
    with (DIR/'rule_catalog.csv').open(newline='',encoding='utf-8') as fh:
        rules=list(csv.DictReader(fh))
    assert len(classes)==31 and len(rules)==256
    by_class={int(c['class_id']):c for c in classes}
    assert len(by_class)==31 and len({int(x['rule']) for x in rules})==256
    signatures={}
    graph_sizes=[]
    first_terms={}
    for row in rules:
        r=int(row['rule']);cid=int(row['class_id'])
        c=by_class[cid]
        coeffs=[int(x) for x in c['coefficients'].split(';')]
        certified_initial=[int(x) for x in c['initial_values'].split(';')]
        initial=[int(row[f'p{i}']) for i in range(1,9)]
        n,prefix,first8=counts_and_certificate(r,coeffs,initial)
        assert n==int(row['relation_states']), r
        assert prefix==certified_initial, (r,'recurrence initial values')
        assert len(coeffs)-1==int(c['degree'])
        if cid not in signatures:signatures[cid]=(tuple(prefix),tuple(coeffs),tuple(first8))
        assert signatures[cid]==(tuple(prefix),tuple(coeffs),tuple(first8)),r
        graph_sizes.append(n)
        first_terms[r]=first8
    groups=defaultdict(list)
    for row in rules:groups[int(row['class_id'])].append(int(row['rule']))
    assert len(groups)==31
    for cid,c in by_class.items():
        members=[int(z) for z in c['rules'].split(';')]
        assert members==groups[cid]
    assert len({x[2] for x in signatures.values()})==31
    assert all(first_terms[7][i]==first_terms[25][i] for i in range(7))
    assert (first_terms[7][7],first_terms[25][7])==(148,156)
    # Cross-check each output word using a different n-phase directed graph.
    tests=0
    for r in range(256):
        for n in range(1,9):
            assert independent_periodic_check(r,n)==first_terms[r][n-1],(r,n)
            tests+=1
    print('VERIFY_OK: 256 exact complete-state recurrence certificates;')
    print('31 pairwise distinct all-period spectra separated by periods <=8;')
    print('sharp period-8 witness: Rule 7 versus Rule 25 (P8=148 versus 156);')
    print('max relation states=%d; max recurrence degree=%d;'%(max(graph_sizes),max(int(x['degree']) for x in classes)))
    print('%d independent expanded-phase periodic-word checks (periods 1..8)'%tests)

if __name__=='__main__':main()
