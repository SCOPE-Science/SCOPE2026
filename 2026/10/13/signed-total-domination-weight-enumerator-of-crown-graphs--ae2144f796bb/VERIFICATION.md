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

The proof is symbolic and valid for every integer \(n\ge3\). The bundled `verify.py` supplies finite regression evidence only. It enumerates all \(2^{2n}\) sign labelings for \(3\le n\le8\), tests the signed-total condition directly from open neighborhoods, checks equivalence with the side-sum criterion, compares every bivariate positive-label coefficient with \(\binom{n}{i}\binom{n}{j}\) on the predicted support, and checks the minimum weight and minimum-layer multiplicity.

No finite computation is used to infer the infinite theorem. The literature comparison establishes absence of located coverage, not proof of global novelty. The exact day in `first_public_date` is the date field exposed by an institutional repository record for the 2001 primary article.
