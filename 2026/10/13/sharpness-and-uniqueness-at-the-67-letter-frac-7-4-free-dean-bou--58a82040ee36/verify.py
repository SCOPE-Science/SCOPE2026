#!/usr/bin/env python3
import json, pathlib, subprocess, tempfile
root=pathlib.Path(__file__).resolve().parent
cert=json.loads((root/'certificate.json').read_text(encoding='utf-8'))
expected=cert['expected_stdout']
with tempfile.TemporaryDirectory() as td:
    exe=pathlib.Path(td)/'verify'
    subprocess.run(['g++','-O3','-std=c++17',str(root/'verify.cpp'),'-o',str(exe)],check=True)
    p=subprocess.run([str(exe)],check=True,text=True,capture_output=True)
    out=p.stdout.strip()
    assert out==expected,(out,expected)
print(out)
