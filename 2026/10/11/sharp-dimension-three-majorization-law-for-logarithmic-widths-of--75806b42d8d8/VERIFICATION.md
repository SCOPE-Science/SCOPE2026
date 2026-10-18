---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS: Uniform spherical directions U are Gaussian directions Z/||Z||; this removes a w-independent radial log term and reduces the geometric-mean width to E log max_i sqrt(w_i)|Z_i|. For d=3 the probability that coordinate i wins is (2/π) arctan(w_i/q) with q=sqrt(w1w2+w1w3+w2w3), obtained by the two opposite rectangular-cone solid angles. Its derivative is arctan(w_i/q)/(πw_i), strictly decreasing in w_i at fixed q, proving Schur concavity via pair balancing and continuity to the closed simplex; the planar edge case follows likewise. The d≥4 violation uses a=(1/3,1/3,1/3,0...), b=(8/25,8/25,8/25,1/25,0...); a majorizes b but F(b)-F(a)≤0.5 log(24/25)+1/(6√2π²)=-0.008470181254903494...<0. The bound follows from an exact t³ small-ball estimate and E|Z|³; mixing both weights with uniform positive weights preserves the strict reversal. This is not inferred from finite quadrature or the packaged VERIFY_OK claim.

## originality

PASS

PASS (best knowledge): Ambrus's primary theorems optimize the ordinary arithmetic mean of Gaussian maxima and orthogonal crosspolytope widths. The logarithmic/geometric mean reverses the extremality direction in d=3, and the explicit d=4 obstruction plus d=2,3 strict Schur law is not a corollary of those ordinary-mean statements. Related regular-polytope moment results do not handle all arbitrary-axis weight vectors in this logarithmic functional.

## value

PASS

PASS: The geometric mean of widths is a canonical multiplicative/lower-tail-sensitive width functional. The complete strict dimension-two/three majorization law and exact dimension-four obstruction expose a genuine structural cutoff, with exact signed gap and stability under full-dimensional perturbation. This is a motivated geometry/probability theorem, not a table computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
