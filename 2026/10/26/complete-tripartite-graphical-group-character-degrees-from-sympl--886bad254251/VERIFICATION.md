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

# Reproducibility

Extract `artifacts/verify_tripartite.py` from the same finding record and execute `python3 artifacts/verify_tripartite.py` using standard Python 3 only. A successful run prints `VERIFY_OK_TRIPARTITE_RANK_DISTRIBUTION`.

The verifier independently enumerates complete tripartite matrix blocks and their actual alternating ranks over prime fields for the 12 tuples `(a,b,c,q)` equal to `(1,1,1,2)`, `(1,1,2,2)`, `(1,1,3,2)`, `(1,2,2,2)`, `(1,2,3,2)`, `(2,2,2,2)`, `(1,1,1,3)`, `(1,1,2,3)`, `(1,2,2,3)`, `(2,2,2,3)`, `(1,1,1,5)`, and `(1,1,2,5)`. In addition, it verifies `(1,1,1)`, `(1,1,2)`, and `(1,2,2)` over the extension field \(\mathbb F_4=\mathbb F_2[T]/(T^2+T+1)\), and enumerates small symplectic pullback maps for comparison with the formula \(H_q\). It asserts total cardinalities as well as every rank fiber.

The separate integer-only computation of \(K_{3,3,3}\) over \(\mathbb F_3\) gives rank coefficients \(1,44954,322403328,344675474208,7280599562496\). Their sum is \(3^{27}\); character multiplicities obtained from them have squared-degree sum \(3^{36}\). This is a symbolic finite-sum computation, not an exhaustive enumeration of \(3^{27}\) matrices.

These tests do not independently prove the theorem for unbounded \(a,b,c\). The general proof relies on rank-normal forms, symplectic quotient counts, and the known class-two character formula. No independent mathematical audit has been performed.
