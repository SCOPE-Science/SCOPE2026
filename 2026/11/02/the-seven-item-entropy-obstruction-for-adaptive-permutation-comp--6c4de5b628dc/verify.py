"""Independent certificate replay for permutation comparison-shattering trees.
Requires only Python 3 standard library and permutation_witnesses.json.
"""
import itertools,json,math,os
p=os.path.join(os.path.dirname(__file__),'permutation_witnesses.json')
with open(p,encoding='utf-8') as f: data=json.load(f)['certificates']
expected={2:1,3:2,4:4,5:6,6:9,7:11}
for n,depth in expected.items():
    cert=data[str(n)]; assert cert['depth']==depth
    perms=list(itertools.permutations(range(n)))
    assert len(perms)==math.factorial(n)
    signature=[]
    for perm in perms:
        where={x:i for i,x in enumerate(perm)}
        signature.append(where)
    used=[];internals=0;leaves=0
    def check(tree,levels,consistent):
        global internals,leaves
        if levels==0:
            assert set(tree)=={'permutation'}
            perm=tuple(tree['permutation'])
            assert sorted(perm)==list(range(n))
            assert perm in {perms[i] for i in consistent}
            used.append(perm);leaves+=1
            return
        assert set(tree)=={'query','zero','one'}
        a,b=tree['query'];assert 0<=a<b<n
        true=[i for i in consistent if signature[i][a]<signature[i][b]]
        false=[i for i in consistent if signature[i][a]>signature[i][b]]
        assert true and false
        internals+=1
        check(tree['zero'],levels-1,false)
        check(tree['one'],levels-1,true)
    check(cert['tree'],depth,list(range(len(perms))))
    assert len(used)==len(set(used))==2**depth
    assert internals==2**depth-1
    assert leaves==2**depth
    if n<=6:
        assert 2**(depth+1)>math.factorial(n), 'cardinality upper bound failed'
    print(f'CERTIFICATE_PASS n={n} d={depth} leaves={leaves} internal={internals} hypotheses={len(perms)}')
print('ALL_PERMUTATION_COMPARISON_WITNESSES_PASS')
