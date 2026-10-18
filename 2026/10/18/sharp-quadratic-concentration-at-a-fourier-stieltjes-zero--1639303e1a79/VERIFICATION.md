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

# Verification and reproduction

Execute `python3 verify.py` in the directory containing the result and the checker. It imports only `math` and performs three classes of tests: the scalar certificate contact/derivative identities, 100,000 positive evaluation points, and exact cancellation plus asymptotic ratio checks for five symmetric three-atom Fourier-zero measures.

The checker output is reproducibility evidence, not an exhaustive verification of the continuum. The proof's critical global assertion is the sign pattern of the derivatives of \(F\) on \([0,\pi/2]\), \([\pi/2,\pi]\), and \([\pi,\infty)\). The infinite-measure conclusion is obtained by integration, not numerical quadrature. Exact uniqueness also uses both the cosine and sine portions of the Fourier zero. The optimal coefficient is approached, not attained away from equality.

Neither a formal proof assistant nor independent validation was used. Scientific applicability is limited to exact Fourier zeros and laws of finite variance.
