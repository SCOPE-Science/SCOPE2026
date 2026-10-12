#!/usr/bin/env python3
import json
import pathlib
import subprocess
import tempfile
root=pathlib.Path(__file__).resolve().parent
cert=json.loads((root/'certificate.json').read_text(encoding='utf-8'))
with tempfile.TemporaryDirectory() as td:
    exe=pathlib.Path(td)/'verify'
    subprocess.run(['g++','-O3','-std=c++17',str(root/'verify.cpp'),'-o',str(exe)],check=True)
    p=subprocess.run([str(exe)],check=True,text=True,capture_output=True)
out=p.stdout.strip()
required=[
 'VERIFY_OK','states=3','alphabet=2','labeled_pairs=262144','unambiguous=12502','mortal=7699',
 'max=6','extremizers=12','isomorphism_classes=1','canonical=10,98','witness=abaaba','engines=2'
]
for x in required: assert x in out,x
assert cert['maximum_shortest_killing_length']==6
assert cert['labeled_extremizers']==12
assert cert['isomorphism_classes']==1
assert cert['canonical_representative']['shortest_killing_word']=='abaaba'
print(out)
