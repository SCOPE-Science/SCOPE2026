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

# Mathematical verification

The defining algebraic identity is \(\partial_{\bar z}\overline{P^k}=k\overline{P^{k-1}P'}\). Stokes' theorem on polynomial levels transforms each forbidden inner product into a contour integral of \(f/P^k\); its residue sum vanishes for \(\deg f\le dk-2\). The unnormalized holomorphic area formula counts \(d\) preimages almost everywhere, yielding precisely \(\pi(R^{2k}-r^{2k})/(dk)\).

`CHECK.py` runs using Python's standard library and checks exact polynomial coefficients, degree/monicity, positive squared norms and capacity ratios for nonrotational sample polynomials and several integer exponents. These checks are finite, not a proof of universal orthogonality or a substitute for the residue argument. The sharp capacity normalization follows from the exterior Green function of the outer filled polynomial lemniscate.

Scope exclusions: general holes and degrees outside the divisibility subsequence. Independent validation has not been performed. Full-text inspection of Simanek's closely related polynomial-lemniscate research was unavailable, so its possible implications remain a literature risk.
