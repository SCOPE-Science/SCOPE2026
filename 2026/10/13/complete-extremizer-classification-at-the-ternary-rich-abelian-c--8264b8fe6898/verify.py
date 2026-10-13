#!/usr/bin/env python3
import json, subprocess, tempfile
from pathlib import Path

root=Path(__file__).resolve().parent
cert=json.loads((root/"certificate.json").read_text(encoding="utf-8"))
assert cert["canonical_count_length_180"]==4
assert cert["canonical_count_length_181"]==0
assert cert["labeled_extremizer_count"]==24
assert cert["alphabet_permutation_orbits"]==4
assert cert["permutation_plus_reversal_orbits"]==2
assert len(cert["canonical_extremizers"])==4
assert all(len(w)==180 and set(w)==set("012") for w in cert["canonical_extremizers"])

with tempfile.TemporaryDirectory() as td:
    exe=Path(td)/"verify"
    subprocess.run(["cc","-O3","-std=c11",str(root/"verify.c"),"-o",str(exe)],check=True)
    r=subprocess.run([str(exe)],check=True,text=True,capture_output=True)
    expected=("VERIFY_OK canonical180=4 canonical181=0 labeled180=24 "
              "perm_orbits=4 perm_reversal_orbits=2 reverse_pairs=1-3,2-4 direct_checks=4")
    assert r.stdout.strip()==expected, r.stdout
    print(r.stdout.strip())
