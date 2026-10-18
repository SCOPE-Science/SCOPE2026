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

# Reproducible checks

Run `python3 verify_fan_matching.py` with standard Python 3 and no third-party packages. The verifier enumerates all matching faces of \(K_1\vee P_n\) for each \(2\le n\le15\); computes augmented simplicial boundary ranks by exact bitset elimination over \(\mathbf F_2\); compares all reduced Betti numbers with the claimed piecewise formulas; and independently computes the full face polynomial through the path-matching recurrence and the apex-cone decomposition. It checks the alternating Euler value as an additional consistency condition.

All assertions pass, as recorded in `verification_output.txt`. The computed sequence of unique nonzero reduced Betti multiplicities for \(n=2,\ldots,15\) is \((2,2,1,4,3,2,6,4,3,8,5,4,10,6)\). The program does not compute integer Smith forms or establish a universal homotopy equivalence. Those infinite/integral claims are supported instead by the explicit cofiber proof in `RESULT.md`; field computations cannot substitute for that proof.
