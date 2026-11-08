---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For Brownian diffusion D>0 and nonzero deterministic |a|=c<1 Poisson proportional resets rate r>0, stationary X=sum_{j>=0}a^j Z_j with independent Laplace variables of scale ell=sqrt(D/r). Characteristic function product∏(1+ell² c^{2j}u²)^-1 decays faster than every inverse polynomial (select arbitrarily many fixed factors), yielding C^infinity via Fourier inversion. Stationary adjoint pantograph equation at x=0 gives f^(2n)(0)=(-1)^n f(0)ell^(-2n)c^(-n²)∏_{j<n}(1-c^(2j+1)), with all odd derivatives zero; independent exact-rational recurrence checks passed 48 cases. Derivative growth exp(Ln²+O(n)) for L=-log c prohibits every finite Gevrey order and gives zero Taylor radius. Known exponential-density series converges holomorphically in Re z>0 (reflected on negative line), so zero is the sole nonanalytic point. Cosine Taylor remainder bounded by absolute 2n moment, taking n=floor(log(ell/|x|)/L) yields f(0)exp(L-t²/L). The stationary single-time density claim does not extend to |a|=0 or >=1.

## originality

PASS

Biroli et al. 2024, Section II, already derive the same stationary density, exponential series and Gaussian-like small-x behavior; page 4 explicitly says the linear-term cancellation identity was numerically checked but not proved. Grzywny et al. 2024 Proposition 2.22 proves C-infinity in a much broader stable partial-resetting family, so smoothness alone is covered. The assessed addition is exact complete origin jet, rigorous non-Gevrey/nonanalyticity and explicit logarithmic-order Taylor approximation error; classical q-binomial cancellation alone is not claimed new.

## value

PASS

Distinguishing global C-infinity regularity from extreme nonanalyticity at the stationary peak is a mathematically meaningful regularity phase change. The exact jet and explicit super-algebraic approximation by logarithmically many Taylor terms quantify this counterintuitive structure, which a researcher analyzing local reset distributions can use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
