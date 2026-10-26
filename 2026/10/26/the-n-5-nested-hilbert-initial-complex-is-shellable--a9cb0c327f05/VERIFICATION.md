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

The verification program `verify.py` was run twice from the artifact directory. Both runs reconstructed the same 130-element shelling order and reported:

- 30 vertices and 14 generator supports;
- all 27,405 four-subsets examined;
- exactly 130 minimal hitting sets, all of size four;
- agreement between the full minimal-transversal recursion and the four-subset enumeration;
- 130 facets of size 26;
- direct facet-level shelling check: PASS.

The program uses only the Python standard library. These are reproducible self-review of the finite claim. They are not an independent audit and do not establish a result for any parameter other than \(n=5\).
