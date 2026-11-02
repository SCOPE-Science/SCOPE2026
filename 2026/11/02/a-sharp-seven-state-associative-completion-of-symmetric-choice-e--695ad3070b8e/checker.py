"""Independent, exact finite check for the seven-state error-operation theorem.
Run with Python 3; no third-party packages are needed.
"""
from itertools import product

OLD = '01uek'
V = '01uekrx'
OLD_ROWS = ('01uek', '1111k', 'u1uek', 'eeeek', 'kkkkk')
ROWS = ('01uekrx', '1111krr', 'u1uekrx', 'eeeekxx',
        'kkkkkkk', 'r1rkkrk', 'xexkkxk')
assert all(len(row) == len(V) for row in ROWS)
f = {(a,b): ROWS[i][j] for i,a in enumerate(V) for j,b in enumerate(V)}
original = {(a,b): OLD_ROWS[i][j] for i,a in enumerate(OLD) for j,b in enumerate(OLD)}
assert all(f[a,b] == z for (a,b),z in original.items()), 'Original five-state algebra changed'
assert all(f['0',a] == a and f[a,'0'] == a for a in V)
assert all(f['k',a] == 'k' and f[a,'k'] == 'k' for a in V)

# Check associativity on the entire seven-element carrier, not just examples.
triples = list(product(V,repeat=3))
for a,b,c in triples:
    assert f[f[a,b],c] == f[a,f[b,c]], (a,b,c)

pi = {x: ('k' if x in 'uekrx' else x) for x in V}
N = {
('0','0'):{'0'}, ('0','1'):{'1'}, ('0','k'):{'k'},
('1','0'):{'1'}, ('1','1'):{'1'}, ('1','k'):{'1','k'},
('k','0'):{'k'}, ('k','1'):{'1','k'}, ('k','k'):{'k'},
}
for a,b in product(V, repeat=2):
    assert pi[f[a,b]] in N[pi[a],pi[b]], (a,b)
neg = {'0':'1','1':'0',**{a:a for a in 'uekrx'}}
for a in V:
    assert neg[neg[a]] == a and pi[neg[a]] == ({'0':'1','1':'0','k':'k'}[pi[a]])

profiles = {(pi[f['1',a]], pi[f[a,'1']]): a for a in 'uerk'}
assert set(profiles) == {('1','1'),('1','k'),('k','1'),('k','k')}
assert f['e','r'] == 'x'
# The algebra is generated from the original five values plus the reverse error r.
closure = set('01uekr')
while True:
    nxt = closure | {f[a,b] for a,b in product(closure, repeat=2)}
    if nxt == closure: break
    closure = nxt
assert closure == set(V)

# Structural 6-point obstruction: e*r must be a value y with y*1=e
# and 1*y=1*r. In the original 5-point subalgebra, the only y with
# y*1=e is e; the same is false for new r since r*1=1.
R1 = {a: original[a,'1'] for a in OLD}
R1['r'] = '1'
L1 = {a: original['1',a] for a in OLD}
assert [a for a in R1 if R1[a] == 'e'] == ['e']
# Since pi(1*r)=k and associativity 1*(1*r)=1*r, it can only be k or r.
for possible_1r in ('k','r'):
    L1['r'] = possible_1r
    assert not any(R1[y] == 'e' and L1[y] == possible_1r for y in OLD+'r')
print('ALL_CHECKS_OK', len(triples), 'associativity triples', len(V)**2, 'projection pairs')
