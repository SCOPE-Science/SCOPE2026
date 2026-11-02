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

# Reproducibility and boundaries

Run `python3 verify_random_evolution.py` using only a standard Python installation. Expected final output: `VERIFY_OK 10 exhaustive invertible-matrix cases and 16 scalar partition checks`.

The verifier independently enumerates every invertible structure matrix in the prime-field cases \((q,n)=(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(5,1),(5,2)\), and in the extension-field case \((q,n)=(4,2)\). The first four binary configurations are regression tests only. In each case it checks all scaled permutation automorphisms and independently constructs the monomial group orbits. It additionally checks exact transposition centralizer counts and sixteen finite scalar-restriction partition sums.

Important selected checks: over \(\mathbb F_3\) with \(n=3\), there are \(11232\) invertible structure matrices, \(576\) nonrigid matrices, and \(249\) isomorphism classes. Over \(\mathbb F_4\) with \(n=2\), the corresponding figures are \(180\), \(36\), and \(13\). These computations are exhaustive for their finite domains, but do not certify the asymptotic estimates. The latter follow from the algebraic and combinatorial proof in `RESULT.md`.

Scientific limits: fixed finite field of order at least three, perfect evolution algebras, ordinary rational automorphisms. No independent audit has been performed.
