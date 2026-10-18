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

# Verification

The accompanying `verify_maximal_dissociation.py` is self-contained (Python standard library). Run `python verify_maximal_dissociation.py`; its captured expected output is included as `verification_output.txt`.

A direct graph test computes every vertex's induced degree on each selected-cell subset of each tested rook board. For each feasible subset it adds each omitted vertex in turn, rejecting a set as non-maximal whenever any addition keeps all induced degrees at most one. This is independent of the component formulas used by the second routine. The two methods agreed on 21 board dimensions and 1,501,518 subsets. The second routine also tested 325 dimension pairs through side lengths 25, including the wide-board exact coefficients and one-row limits. The recorded output ends `ALL_CHECKS_PASSED`.

The combinatorial proof, not finite computation, handles all integers \(m,n\ge1\). Bibliographic priority and an independent review are not certified here.
