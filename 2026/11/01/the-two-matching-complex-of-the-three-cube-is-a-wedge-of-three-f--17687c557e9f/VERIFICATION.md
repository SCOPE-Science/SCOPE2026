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

# Reproducible finite proof

Run `python3 verify.py` with Python 3 (standard library only). This enumerates all \(4096\) subsets of the displayed cube edge set, compares two independent face predicates, produces an acyclic discrete-Morse matching, topologically sorts its entire directed gradient transition graph, reduces the signed cellular differential, and computes the original simplicial mod-two chain ranks separately.

Expected values, independently asserted in code: \(1698\) nonempty simplices; face counts \((12,66,212,423,516,352,108,9)\); \(846\) acyclic matched pairs; critical cells of dimensions \((0,4,5,5,5,5)\); complete nonempty Hasse incidence count \(7980\); integer degree row \((-1,1,-1,-1)\); reduced mod-two Betti numbers only \(\beta_5=3\). The row contains unit entries and hence defines a primitive attachment; this is the decisive integral step needed for the claimed wedge decomposition.

`verify_output.txt` is a record of actual execution. The essential logical checks are the executable enumeration and exact integer algebra, not an assumed correctness property of that log. The proof covers the entire specified finite complex; no extrapolation to larger hypercube dimensions is made.
