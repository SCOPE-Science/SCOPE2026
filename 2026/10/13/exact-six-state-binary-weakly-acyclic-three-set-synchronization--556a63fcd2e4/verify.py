#!/usr/bin/env python3
import json, pathlib, subprocess, tempfile
root=pathlib.Path(__file__).resolve().parent
cert=json.loads((root/'certificate.json').read_text(encoding='utf-8'))
with tempfile.TemporaryDirectory() as td:
    exe=pathlib.Path(td)/'verify'
    subprocess.run(['g++','-O3','-std=c++17',str(root/'verify.cpp'),'-o',str(exe)],check=True)
    p=subprocess.run([str(exe)],check=True,text=True,capture_output=True,timeout=180)
out=p.stdout.strip()
for token in ['VERIFY_OK','maps=720','automata=518400','three_subsets_per_automaton=20','max=7','natural_extremal_presentations=4','isomorphism_classes=1','labeled_extremizers=1440','witness=aaabaaa']:
    assert token in out, token
assert cert['maximum_shortest_synchronizing_length']==7
assert cert['isomorphism_classes']==1
assert cert['labeled_extremizers']==1440
print(out)
