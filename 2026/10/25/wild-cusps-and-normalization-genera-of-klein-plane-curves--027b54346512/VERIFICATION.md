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

The exact proof reduces the torus chart to \(1+s+s^m u^{-N}=0\), uses the valuation at \(s=0\) to prove geometric integrality, and resolves singular germs by the étale parameter \(w=u^{-h}\) when \(N=p^a h\). The local equation is then exactly a formal square plus a Frobenius power. This proves cusp type, delta invariant, Tjurina length, and normalization genus for every integer \(m\ge2\); it does not depend on finite sampling.

The included `verify_klein_reduction.py` was run under Python using standard-library integer arithmetic. It returned `VERIFY_OK instances=73 m_range=2..45`, including cases with \(p\mid(m+1)\) and with \(p^a=49\). Direct finite-field point checks establish the expected geometric equations only for the enumerated small cases, not for arbitrary algebraically closed fields.

Independent audit: not performed. The theorem concerns singularities of the specific plane model, not a stable arithmetic model.
