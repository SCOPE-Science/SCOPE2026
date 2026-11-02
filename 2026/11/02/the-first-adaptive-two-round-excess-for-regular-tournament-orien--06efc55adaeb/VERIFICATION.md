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

# Reproducibility and scope

Extract `depth11_tree.json`, `verify.py`, `census.cpp`, and `make_witness.py` into a single directory. Execute:

```sh
python3 verify.py
g++ -O3 -std=c++17 census.cpp -o census
./census
```

`verify.py` enumerates all 2640 labeled regular tournaments on seven vertices, validates 2047 binary query nodes and 2048 distinct terminal tournament bit masks, and proves the upper bound through the 2640-vs-4096 cardinality obstruction. It checks cut-feasibility against direct trace enumeration on every query support at orders three and five and directly checks all 35 maximum supports at order seven. `census.cpp` exhausts all 2097152 edge supports for order seven using the cut criterion, with exact integer comparisons. `make_witness.py` reproduces the complete tree by finite recursion and can overwrite the included tree with an equivalent certificate.

The mathematical implication from cut inequalities to all-orientations shattering is established in `RESULT.md` using integer orientation feasibility. A finite experiment does not establish that implication; the independent code verifies its applications, not the infinite theorem in place of proof. The package verifies this finite claim only and does not assert a general all-odd-order Littlestone formula.
