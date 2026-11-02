#!/usr/bin/env python3
"""Optional symbolic evaluation of the finite transfer matrices; requires SymPy."""
import sympy as S
z=S.symbols('z')

def eval_d(d):
    states=[(h,s) for h in range(d+1) for s in range(3)]
    ix={s:i for i,s in enumerate(states)}
    P=S.zeros(len(states)); Q=S.zeros(len(states))
    for h,st in states:
        for pair,change in [('00',1),('01',0),('10',0),('11',-1)]:
            if h==0 and pair=='10':continue
            if not(0<=h+change<=d):continue
            seen = {0:None,1:'0',2:'1'}[st]
            completions=0
            for x in pair:
                if seen is None:seen=x
                elif x!=seen:seen=None;completions+=1
            assert completions in (0,1)
            new_state={None:0,'0':1,'1':2}[seen]
            matrix=P if completions else Q
            matrix[ix[(h,st)],ix[(h+change,new_state)]]+=1
    R=(S.eye(len(states))-z*P).inv()
    e=S.zeros(1,len(states));e[0,ix[(0,0)]]=1
    f=S.zeros(len(states),1)
    for s in range(3): f[ix[(0,s)],0]=1
    v=R*f
    for k in range(d):v=R*z*Q*v
    return S.factor((e*v)[0])

expected=[1/(1-z),z*z/((1-z)*(1-2*z)),z**3*(1-z)/(1-2*z)**3,z**4*(1-z)*(1-2*z+2*z*z)/(1-2*z)**5]
for d in range(4):
    a=eval_d(d)
    assert S.cancel(a-expected[d])==0,(d,a)
    print('SYMBOLIC_OK',d,str(a))
