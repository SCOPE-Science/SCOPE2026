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

# Reproducibility of the 47-vertex certificate

Save `verify.py` and `witness.json` in the same directory. Run `python3 verify.py` using Python 3.9 or later. No third-party dependencies or downloaded data are required.

The program independently verifies vertex/edge counts, one incoming edge per nonroot vertex, connectivity, acyclicity, all bottom-up modal codes at depths zero through three, and complete coverage of types zero through fifteen. It recomputes the reduction from depth three to two, all sixteen weighted potentials, their 44-unit total, the root's 3-unit contribution, and the validity of local child-demand inequalities. The analytic proof in `RESULT.md` demonstrates the lower bound for every finite tree, not merely for trees enumerated by the program.

The witness has root code 4 and 47 vertices. The independently computed depth-three type multiplicities are: 19 of code 0, 11 of code 1, three of code 2, two of code 3, and one each of codes 4 through 15. The program's successful terminal line is `PASS: 47 vertices, 46 child edges, 16 types, weighted lower bound 47`.

The code does not check published-paper priority, prove generalisations to other modal depths, or supply an independent audit. No separate mathematical assertions rest on runtime search failures or on incomplete enumeration.
