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

Circulant discrete Fourier diagonalization of the positive definite kernel G yields each nonzero frequency of optimal w equal to that of the tent density masses q_j via the csc-square aliasing identity. Their difference is a common scalar fixed by the zero Fourier mode: w_j=q_j-gamma(B-A)/[n(1+gamma B)]. The folded half-period convolution has its minimum at the density zero j=0 by symmetry, unimodality and circular layer-cake rearrangement; q0=1/2−n sin(2pi/n)/(4pi). Consequently positivity cuts off sharply at Gamma_pos=n q0/(B−A−n q0 B), with exact equality zero; sum w=(1+gamma A)/(1+gamma B) switches at Gamma_mass=−1/A. A<0 follows explicit summands. The n=2 equality and strict n>=3 ordering follow algebra, and Taylor expansions give order-n versus order-n^4 thresholds. Independent high-precision, separately integrated kernel-mean/Gram solves for n=2,3,4,5,7 and gamma in {0.1,3.7} reproduced formulas; analytic proof is required for all n.

## originality

PASS

Classical periodic Sobolev cardinal functions and Bayesian kernel quadrature weight positivity supply the framework. The candidate novelty is an exact two-parameter sign threshold for the specified nonsmooth Chebyshev density including parity-dependent constant-mass transition. Bartel–Gilbert–Griebel–Kuo–Sloan 2026 is highly relevant but full text was unavailable: only accessible abstract/general description reviewed, so no whole-document noncoverage assertion. The best-of-knowledge originality pass retains explicit significant equivalent spline-identity priority risk.

## value

PASS

Optimal unconstrained RKHS quadrature weights can become negative even when kernel and target density are positive; determining the exact smallest-weight transition and the later constant-response sign transition is a meaningful design boundary. The 16-fold parity effect in the latter and exact n- and n^4-scales are independently useful diagnostics, not merely routine inversion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
