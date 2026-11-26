---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For each q>0, work on the complexified scalar-plus-L² state space with scalar weight f_q/b_q. The cross-terms of the negative-generator form are conjugate pairs with coefficient -f_q. The trace is bounded relative to bulk gradient energy (with arbitrarily small relative bound for the cross terms), so the form is closed, semibounded, and compactly embedded. Integration by parts yields the stated signs and Robin condition. For an independent threshold check, take R to be the static Robin solution with unit boundary forcing. Its boundary value is R(0)=1/[κ+D_c q coth(Hq)]. Completing the form square in C-f_q w R leaves the scalar coefficient (f_q/b_q)a_q-f_q²R(0). The chemical energy is positive definite, so below threshold all eigenvalues of the generator are negative, at threshold the kernel is one-dimensional, and above threshold it has exactly one positive simple eigenvalue. At s>0 the surface response is strictly smaller than at zero since x coth(x) is increasing and m=sqrt(q²+s/D_c)>q; the dispersion equation therefore gives strict slowing relative to the static prediction. For minimization, with y=Hq and t=y coth y, the stationary-point map has denominator M=2+U(2t-yt'), which is greater than Ut. Since t''>0 and 0<t'/t<1/y, M'/M<t'/t and the logarithmic derivative of B_U exceeds 2/y. B_U ranges from zero to infinity, and the derivative of F has the sign of B_U-β. The small-y expansion is B_U=Uy⁴/[3(1+U)]·(1+O(y²)); it yields q_*²=sqrt(D_r A/(D_t K))+O(D_r) with A=κ+D_c/H and K=D_cH/3, and hence the claimed threshold correction with O(D_r) remainder. Bounded replay `python3 /workspace/branches/independent_checks.py 1` gives q*=1.7214210415 and G_c=3.7918904277 for unit parameters. The printed q approximation in RESULT.md differs by about 1.4e-7, immaterial to the theorem; the gain agrees at the displayed precision. Inspected the supplied finite-volume checker but did not execute it.

## originality

PASS

The prior quasistatic equations imply the stationary per-q gain and the quasistatic growth rate; neither is new. The supported distinct result is the positive-feedback dynamic slab classification (all-real spectrum, no oscillatory onset, strict growth suppression), its combination with all-parameter single-band geometry, and the exact slab-dependent low-rotation coefficients. The quarter-root exponent, chemical memory, and polar feedback in isolation are not novelty claims.

## value

PASS

The question of when a quasistatic approximation misses an oscillatory onset is substantive in this source model. The result distinguishes exactly what finite diffusion changes (growth rates) from what it does not (threshold and stationary onset), and specifies a unique predicted mode, band, and crossover scale useful in comparing slab parameter regimes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
