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
need=[
    'VERIFY_OK','n2=0','n3=0','n4=0',
    f"n5_labeled={cert['primitive_nonsynchronizing_nonpermutation_counts']['5']}",
    f"classes={cert['five_state_isomorphism_classes']}",
    'orbit_sizes=240x12','rank33_classes=8','rank35_classes=4',
    'rank33_labeled=1920','rank35_labeled=960'
]
for token in need:
    assert token in out, token
assert cert['canonical_codes_base5']==[int(x) for x in out.split('canonical_codes=')[1].split(',')]
print(out)
