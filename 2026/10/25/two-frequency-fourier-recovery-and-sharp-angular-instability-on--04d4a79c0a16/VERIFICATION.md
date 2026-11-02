---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Funk–Hecke with normalized sphere measure gives each harmonic-channel 2x2 multiplier M_l with phi_l(z)=2^nu Gamma(nu+1) z^{-nu} J_{l+nu}(z). On 0<bv<j_{nu,1}, the positive Bessel product and monotonicity of its first zero make ratio phi_l(at)/phi_l(bt) strictly increasing in t; det M_l<0 for u<v. Single observation sphere always has a nontrivial 1x2 null vector. The Bessel series cancels determinant leading terms and gives -kappa_l^2(abuv)^l (b²-a²)(v²-u²)/[4(l+nu+1)](1+O(1/l)). Bottom-right entry asymptotically dominates, and sigma_min=abs(det)/sigma_max gives stated sharp ill-conditioning. Independent 90-digit Bessel evaluations for d=2,3,5 and degrees 0,1,5,40 checked determinant sign and determinant/leading-term ratios 0.9966, 0.9931, 0.9896 at degree 40. All-l uniqueness rests on the proof, not finite samples.

## originality

PASS

Best-of-knowledge original surviving claim: Combining two copies of a one-shell uniqueness theorem does NOT separate two summands measured only through their sum; the 2x2 determinant proof is needed. Prior work and access risks as in structured comparisons.

## value

PASS

A natural two-shell inverse-source geometry is separated exactly by the minimal number of full measurement spheres and its ill-conditioning is quantified at the singular-value level. This is substantively stronger than bare uniqueness of a single-shell inverse problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
