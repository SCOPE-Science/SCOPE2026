---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The two embedded Python 3 programs require only the standard library. From their parent directory run:

```
python code/orbit_types.py 33 > /tmp/orbit_types.txt
python code/direct_types.py 15 > /tmp/direct_types.txt
```

The first uses only known cyclic and reflection automorphisms to normalise the first selected vertex and enumerate exact rank-four type signatures for both graph families at all widths three through thirty-two. All ordered tuples with repeated selections are represented. Its output agrees with `data/orbit_types.txt`; the root identifiers are 0 through 11 separately at widths three through eight, then shared identifier 12 for every width from nine through thirty-two.

The second implementation independently constructs edge sets, enumerates every ordered tuple without orbit reduction, and recursively interns the full atomic-extension type for both families at widths three through fourteen. Its output agrees with `data/direct_types.txt`; it reproduces the different twist types below nine and the common type at nine and above throughout the overlapping range. The identifiers agree because all type signatures are interned globally within each program.

The mathematical cyclic-gap lemma in `RESULT.md` supplies all widths at least thirty-two. Neither program has been misrepresented as an exhaustive calculation over infinitely many widths. Exact recursive type equality certifies finite equivalence and exact inequality certifies finite distinguishability. No formal proof-assistant or external expert certification was performed.
