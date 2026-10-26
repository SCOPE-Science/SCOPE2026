"""Finite cyclic analogues of bounded-degree preferred-extension construction.
Run with Python 3; the infinite theorem is proved independently."""
from itertools import combinations

def build(rows, period):
    vertices=[]; attack=set(); core=[]
    for n in range(rows):
        for k in range(period):
            a=('a',n,k); up=('u',n,k); dn=('d',n,k)
            vertices.extend((a,up,dn)); core.append(a)
            attack.update(((up,up),(dn,dn),(up,a),(dn,a),
                           (('a',n,(k+1)%period),up),
                           (('a',n,(k-1)%period),dn)))
    for n in range(rows):
        for m in range(n+1,rows):
            kn=m if m<n else m-1
            km=n if n<m else n-1
            assert kn<period and km<period
            x=('a',n,kn);y=('a',m,km)
            attack.add((x,y));attack.add((y,x))
    incoming={v:set() for v in vertices};outgoing={v:set() for v in vertices}
    for x,y in attack:
        incoming[y].add(x);outgoing[x].add(y)
    assert max(map(len,incoming.values()))<=3
    assert max(map(len,outgoing.values()))<=3
    return vertices,core,incoming,outgoing

def run(rows,period):
    vertices,core,inc,out=build(rows,period)
    expected=[frozenset()]+[frozenset(('a',n,k) for k in range(period)) for n in range(rows)]
    actual=[]
    for mask in range(1<<len(core)):
        selected=frozenset(v for i,v in enumerate(core) if mask>>i&1)
        defended=True
        for v in selected:
            if any(w in selected for w in out[v]):
                defended=False;break
            if any(not (inc[attacker] & selected) for attacker in inc[v]):
                defended=False;break
        if defended: actual.append(selected)
    assert set(actual)==set(expected),(rows,period,len(actual),len(expected))
    maximal={s for s in actual if not any(s<t for t in actual)}
    assert maximal==set(expected[1:])
    print(f'OK rows={rows}, cycle_period={period}, core_subsets={1<<len(core)}, admissible={len(actual)}, preferred={len(maximal)}')

if __name__=='__main__':
    for n,p in ((2,2),(3,3),(4,4)):
        run(n,p)
    print('FINITE_ANALOGUES_OK')
