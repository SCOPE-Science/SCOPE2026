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
The statements below describe direct mathematical and computational checks, not an external certification.

The classical Bloch radial upper bound is attained on positive radii by \(\operatorname{arctanh}z\); \(\beta(\operatorname{arctanh})=1\). The derivative of the rational weighted composition separates into two positive terms at a positive real argument. The constant-vector branch cannot exceed \(\int t^{-1}d\mu\), while the hyperbolic-arctangent branch has radial limit exactly that value. Fatou's lemma and the explicitly shown bound \(K_t(r)\le3/t\) close the argument for general positive measures, not just finite sums of atoms.

Symbolic algebra checked \(r=y/[t+(1-t)y]\), the two coefficient substitutions and the maximum \(\max_r A_t(r)=(1-t)/[t(2-t)]\). The scalar boundary expansion gives a positive \(\varepsilon\log(1/\varepsilon)\) excess at each \(0<t<1\); the semigroup calculation gives \(r(\mathcal H_{\delta_t})=1/t\). Uniform convergence of the continuous scalar profile proves the small-parameter limit without an extrapolation from finitely many samples.

Independent numerical optimizations of the exact one-variable expression, for illustration only, produced \(N(1/2)\approx2.1223931485\), \(N(1/10)\approx11.0673957791\), and \(C_*\approx1.1176848412\). Those decimals are not certified interval bounds and do not support the infinite-dimensional theorem by themselves.

No assertion is made about signed measures, alternate norm conventions, a strict spectral gap for arbitrary positive mixtures or independent bibliographic certification.
