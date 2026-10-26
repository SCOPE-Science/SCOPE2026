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

The standalone Python 3 verifier `loewy_rank_verify.py` uses only the standard library. It enumerates every individual matrix over the indicated field, filters square-zero matrices, checks every pairwise ordered product among tuple entries, and directly computes the two independent ranks. It then compares the resulting full rank-pair histogram with the Gaussian–Möbius formula.

Successful tests: \((n,\ell,q)=(2,1,2),(3,1,3),(3,2,2),(3,2,3),(3,3,2),(3,3,3),(3,2,4),(4,2,2)\). For \(q=4\) arithmetic uses the explicitly represented field \(\mathbb F_2[z]/(z^2+z+1)\), not residue arithmetic modulo four. Terminal success marker: `VERIFY_OK_LOEWY_RANK_STRATA_ALL_CASES`.

These checks are finite, not a proof for all dimensions, field orders, or generator counts. The characteristic-independent argument and the rationality of rank strata rest on the flag-bundle construction and subspace-lattice inversion given in RESULT.md. No independent audit has been performed.
