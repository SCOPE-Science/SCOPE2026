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

# Verification and scientific limitations

Run the accompanying `verify_genus10.py` with a standard Python interpreter. It uses only the standard library. The script reconstructs the \(13\) nonzero character pairs and exactly \(10\) holomorphic eigenlines using local branch valuations. For each eigenline, two independent exact expansions agree on its full polynomial Cartier coefficient. It then verifies pairwise coprimality, irreducibility over \(\mathbb F_7\), roots in \(\mathbb F_{49}\), the cross-ratio polynomial identity, and the factorized Hasse–Witt determinant.

The asserted curve statements are proven from the local valuation and polynomial identities, valid throughout the algebraic closure; a finite-field point census is not used as proof. The geometric \(7\)-rank equals stable Cartier rank because \(7\equiv1\pmod3\) preserves each one-dimensional character eigenspace. No claim is made about other generalized Fermat parameters, positive characteristics, or geometric isomorphisms that do not respect the specified covering structure. Older literature may imply special cases, and independent audit remains unperformed.
