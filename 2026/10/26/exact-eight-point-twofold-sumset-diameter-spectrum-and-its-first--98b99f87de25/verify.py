#!/usr/bin/env python3
"""Exhaustive independent replay of the finite twofold-sumset diameter classification."""
import json
import math
import pathlib
import re
import subprocess
import tempfile

base=pathlib.Path(__file__).resolve().parent
spec=json.loads((base/'spectrum.json').read_text(encoding='utf-8'))
assert len(spec['ranges'])==7
assert [z['k'] for z in spec['ranges']]==list(range(2,9))
with tempfile.TemporaryDirectory() as directory:
    for name in ('enumerate','independent'):
        subprocess.run(['g++','-O3','-std=c++17',str(base/(name+'.cpp')),'-o',str(pathlib.Path(directory)/name)],check=True)
    for dat in spec['ranges']:
        k,limit=dat['k'],dat['limit']
        run=subprocess.run([str(pathlib.Path(directory)/'enumerate'),str(k),str(limit)],capture_output=True,text=True,check=True)
        lines=run.stdout.splitlines()
        match=re.fullmatch(r'K=(\d+) MAX=(\d+) enumerated=(\d+)',lines[0])
        assert match and tuple(map(int,match.groups()))==(k,limit,math.comb(limit,k-1))
        parsed=[]
        for line in lines[1:]:
            match=re.fullmatch(r'size=(\d+) min_d=(\d+) count=(\d+) witness=([\d,]+)',line)
            assert match,line
            t,d,count,w=match.groups()
            parsed.append({'t':int(t),'d':int(d),'count_upto_limit':int(count),'witness':[int(x) for x in w.split(',') if x]})
        assert parsed==dat['rows'],('primary',k)
        assert sum(r['count_upto_limit'] for r in parsed)==dat['examined']
        separate=subprocess.run([str(pathlib.Path(directory)/'independent'),str(k),str(limit)],capture_output=True,text=True,check=True)
        ll=separate.stdout.splitlines()
        assert ll[0]==f'sets {dat["examined"]}'
        got=[tuple(map(int,s.split())) for s in ll[1:]]
        assert got==[(r['t'],r['d']) for r in parsed],('independent',k)
        for r in parsed:
            w=r['witness']
            assert len(w)==k and w[0]==0 and sorted(set(w))==w and w[-1]==r['d']
            assert len({w[i]+w[j] for i in range(k) for j in range(i,k)})==r['t']
        assert [r['t'] for r in parsed]==list(range(2*k-1,k*(k+1)//2+1))
profiles={dat['k']:[r['d'] for r in dat['rows']] for dat in spec['ranges']}
assert all(all(a<=b for a,b in zip(v,v[1:])) for k,v in profiles.items() if k<8)
v=profiles[8]
assert [(15+i,15+i+1,a,b) for i,(a,b) in enumerate(zip(v,v[1:])) if a>b]==[(32,33,20,19)]
assert [r['t'] for r in spec['ranges'][-1]['rows']]==list(range(15,37))
assert profiles[8][-1]==34
print('VERIFY_OK independent_enumerations=2 total_scanned='+str(sum(z['examined'] for z in spec['ranges']))+' first_drop=k8_at_32_to_33 universal_N_2_8=34')
