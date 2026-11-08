---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

PASS: Gaussian E[gg^T]=I and E[(gg^T)^2]=(d+2)I reconstruct the exact 3x3 map on (E||x_k||^2,E<x_k,x_{k-1}>,E||x_{k-1}||^2). The induced positive-semidefinite Gram map satisfies det Gnext=omega^2 det G+(d+1)alpha^2 G11^2; for omega>0, 1–2 updates move nonzero PSD to its interior, ensuring primitive-cone Perron growth and a nonzero leading coefficient for any nonzero zero-momentum initialization. For omega=0 direct scalar factor applies. P(1)=alpha[2(1-omega^2)-alpha(d(1+omega)+2)] and det M=omega^3 yield iff strict stability (omega<1, alpha below ceiling). Completing the square for P((d+1)/(d+2)) makes its sign strictly negative except at omega=0, alpha=1/(d+2), proving unique global optimal rate. Independently recomputed polynomials and 64 rational spectral boundary checks, not extrapolated as proof.

## originality

PASS

Compared exact statements and logical implications against primary full text where accessible, plus published mathematical record searches. The specified result is not established by the inspected prior statements; explicit inaccessible-primary and historical-priority residual risks are retained.

## value

PASS

PASS: Gaussian rank-one sketches are a canonical randomized linear-system solver model and exact true mean-square behavior is practically different from norm-of-mean acceleration. The full-dimension necessary-and-sufficient stability frontier and unique sharp no-positive-momentum optimizer refine general sufficient bounds and illustrate a significant stochastic-momentum limitation; the original algorithm and known qualitative no-acceleration examples are credited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
