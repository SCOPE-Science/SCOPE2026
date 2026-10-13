#!/usr/bin/env python3
import json
import pathlib
import subprocess
import tempfile

root=pathlib.Path(__file__).resolve().parent
cert=json.loads((root/"certificate.json").read_text(encoding="utf-8"))
with tempfile.TemporaryDirectory() as td:
    exe=pathlib.Path(td)/"verify"
    subprocess.run(["g++","-O3","-std=c++17",str(root/"verify.cpp"),"-o",str(exe)],check=True)
    p=subprocess.run([str(exe)],check=True,text=True,capture_output=True)
out=p.stdout.strip()
required=[
    "VERIFY_OK",
    "binary_max=4",
    "split_maxima=0,3,4,3",
    "ternary_witness_shortest=5",
    "unrestricted_published_max=5",
    "minimum_extremal_alphabet=3"
]
for token in required:
    assert token in out, token
assert cert["binary_exact_maximum_shortest_accepted_length"]==4
assert cert["unrestricted_published_maximum_shortest_accepted_length"]==5
assert cert["ternary_witness"]["shortest_accepted_word"]=="abbac"
print(out)
