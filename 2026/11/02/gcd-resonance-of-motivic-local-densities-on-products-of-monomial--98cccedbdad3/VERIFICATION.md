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

The parameterization \(z\mapsto(z^a,z^A)\) and its canonical one-form give exact \(m\)-ball volume \((1-\mathbb L^{-1})(1-\mathbb L^{-a})^{-1}\mathbb L^{-a\lceil m/a\rceil}\). For the product, the four coordinate derivative rows split into two pairs, and the minimum two-by-two minor valuation equals the sum of the minima; this verifies product measure at fixed radius. The residue-class sum is over \(\operatorname{lcm}(a,b)\) time steps and the CRT reduction is over \(\operatorname{gcd}(a,b)\) residue classes; all factors of \(a\), \(b\), and \(d\) are explicit in the proof.

The embedded `verify_density.py` uses exact rational arithmetic at \(\mathbb L=2,3,5,11\). It tests all \(a,b\in\{2,\dots,14\}\) (676 paired tests), the 52 individual period means and four cusp-pair defects. This only checks specializations and finite exponents. The infinite theorem is justified by finite geometric-series identities and the normalization calculation.

The claim concerns the embedded definable-set density, not a nonisolated intrinsic invariant. Earlier papers establish the one-factor cusp value, so only the new gcd-dependent product law is assessed. Independent mathematical audit was not performed.
