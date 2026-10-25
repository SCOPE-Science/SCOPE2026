---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For Y uniform in full-dimensional centered K, polar gauge decomposition Y=RZ has independent R density d r^(d−1) and cone-boundary Z, E Z=0 and E R²=d/(d+2). With Σ=E ZZᵀ positive definite, the affine kernels are Kν(x,z)=1+xᵀΣ^(−1)z and Kμ(x,rz)=1+(d+2)r/d*xᵀΣ^(−1)z. Since each kernel has mean 1, its L1 norm equals 1+2 its negative mass. The independent radial positive-part integral Gd(s) produces Λμ−Λν=2 E[Gd((-u)_+)−((-u)_+−1)_+]. For s>d/(d+2), this difference is strictly positive; otherwise zero. Supporting functionals/Cauchy–Schwarz give u_x(−x)≤−1 for every symmetric-body boundary x; full support of cone measure then forces strict boundary gap. Convexity ensures boundary maximizers and strict operator norm difference. Verified the interval constants 5/3 versus 1 and independently integrated disk kernels against the correct coordinate/angle densities, reproducing both exact constants numerically.

## originality

PASS

Best-of-knowledge PASS for the complete all-centered-body pointwise measure comparison with equality criterion and symmetric-body strict norm gap. Cone-volume laws, radial disintegration and affine reproducing kernels are classical. Relevant projection literature and a published simplex norm result do not make this particular comparison.

## value

PASS

Interior-volume and cone-boundary sampling are canonical competing measures on a convex body. A universal pointwise Lebesgue-function ordering, exact equality threshold, and strict operator-norm separation for every centrally symmetric body are natural, reusable stability facts; interval/disk constants quantify accompanying positivity-loss gap. The value is not contingent on a downstream general theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
