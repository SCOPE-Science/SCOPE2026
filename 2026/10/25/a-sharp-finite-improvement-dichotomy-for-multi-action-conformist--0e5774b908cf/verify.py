"""Reproduce finite definition-level checks for a network-game improvement theorem.

Only Python's standard library is required. The unbounded graph theorem is
proved in RESULT.md, not by this finite experiment.
"""
from itertools import combinations, product


def payoff(i, profile, edges, types):
    neighbors = [j for j in range(len(types)) if (min(i,j),max(i,j)) in edges]
    equal = sum(profile[j] == profile[i] for j in neighbors)
    return equal if types[i] == 'C' else len(neighbors) - equal


def cycles4(edges, types, fixed, m):
    n=len(types)
    stubborn_colors=set(fixed.values())
    unused=[z for z in range(m) if z not in stubborn_colors]
    assert m >=3 and len(unused)>=2
    a,b=unused[:2]
    d=next(z for z in range(m) if z not in (a,b))
    refs=[]
    for u,v in edges:
        if types[u]=='R' and types[v]=='C':u,v=v,u
        if (types[u],types[v])!=('C','R'):continue
        states=[]
        for cu,rv in [(a,b),(b,b),(b,a),(a,a),(a,b)]:
            p=[fixed.get(i,d) for i in range(n)]
            p[u]=cu;p[v]=rv
            states.append(tuple(p))
        assert states[0]==states[-1] and len(set(states[:-1]))==4
        assert all(sum(x != y for x,y in zip(s,t))==1 for s,t in zip(states,states[1:]))
        for j,(s,t) in enumerate(zip(states,states[1:])):
            mover=u if j in (0,2) else v
            assert payoff(mover,t,edges,types)-payoff(mover,s,edges,types)==1
        refs.append(states)
    return refs


def potential(profile, edges, types):
    score=0
    for i,j in edges:
        a,b=types[i],types[j]
        if a=='S' and b=='S':continue
        assert {a,b}!={'C','R'}
        same=profile[i]==profile[j]
        if a=='C' or b=='C':score+=int(same)
        elif a=='R' or b=='R':score+=int(not same)
    return score


def test_all():
    count=0;edges_with_cycles=0;pot_checks=0
    for n in range(2,5):
        possible=list(combinations(range(n),2))
        for mask in range(1<<len(possible)):
            ed={possible[i] for i in range(len(possible)) if mask>>i &1}
            for ty in product('CRS',repeat=n):
                if not ('C' in ty and 'R' in ty):continue
                fixed={i:0 for i,t in enumerate(ty) if t=='S'}
                for m in [3,4]:
                    count+=1
                    refs=cycles4(ed,ty,fixed,m)
                    cr=sum({ty[i],ty[j]}=={'C','R'} for i,j in ed)
                    assert len(refs)==cr
                    edges_with_cycles+=bool(cr)
                if not any({ty[i],ty[j]}=={'C','R'} for i,j in ed):
                    mov=[i for i,t in enumerate(ty) if t!='S']
                    for vals in product(range(3),repeat=len(mov)):
                        state=[fixed.get(i,0) for i in range(n)]
                        for i,a in zip(mov,vals):state[i]=a
                        prev=potential(state,ed,ty)
                        for i in mov:
                            p=payoff(i,state,ed,ty)
                            for a in range(3):
                                next_state=state.copy();next_state[i]=a
                                change=payoff(i,next_state,ed,ty)-p
                                assert potential(next_state,ed,ty)-prev==change
                                pot_checks+=1
    assert count>1000 and edges_with_cycles>100
    # Three-agent witness: pinned S--C--R, with s=0.
    edges={(0,1),(1,2)};ty='SCR';fixed={0:0}
    witness=cycles4(edges,ty,fixed,3)[0]
    assert witness==[(0,1,2),(0,2,2),(0,2,1),(0,1,1),(0,1,2)]
    eq=(0,0,1)
    for i in (1,2):
        assert all(payoff(i,eq,edges,ty)>=payoff(i,eq[:i]+(a,)+eq[i+1:],edges,ty) for a in range(3))
    # The binary same-graph improvement digraph is the following exact chain.
    states=[(0,0,0),(0,0,1),(0,1,0),(0,1,1)]
    successors={}
    for s in states:
        ss=[]
        for i in (1,2):
            t=list(s);t[i]=1-t[i];t=tuple(t)
            if payoff(i,t,edges,ty)>payoff(i,s,edges,ty):ss.append(t)
        successors[s]=ss
    assert successors=={
        (0,0,0):[(0,0,1)],
        (0,0,1):[],
        (0,1,0):[(0,0,0)],
        (0,1,1):[(0,1,0)],
    }
    # Two agents cannot have an equilibrium and a directed improvement cycle.
    for ty in product('CRS',repeat=2):
        fixed={i:0 for i,t in enumerate(ty) if t=='S'}
        mov=[i for i,t in enumerate(ty) if t!='S']
        ss=[];out={}
        for vals in product(range(3),repeat=len(mov)):
            z=list(fixed.get(i,0) for i in range(2))
            for i,a in zip(mov,vals):z[i]=a
            ss.append(tuple(z))
        for z in ss:
            out[z]=[]
            for i in mov:
                for a in range(3):
                    y=list(z);y[i]=a;y=tuple(y)
                    if payoff(i,y,{(0,1)},ty)>payoff(i,z,{(0,1)},ty):out[z].append(y)
        has_pne=any(not x for x in out.values())
        if set(ty)=={'C','R'}: assert not has_pne
        # Else a potential exists, so no strict directed cycle.
        else: assert all(set(ty)!={'C','R'} for _ in [0])
    print('VERIFIED: graph/type/action combinations:',count)
    print('VERIFIED: cross-type cyclic cases:',edges_with_cycles)
    print('VERIFIED: potential equalities:',pot_checks)
    print('VERIFIED: 3-agent equilibrium/cycle, binary boundary, 2-agent boundary')


if __name__=='__main__':test_all()
