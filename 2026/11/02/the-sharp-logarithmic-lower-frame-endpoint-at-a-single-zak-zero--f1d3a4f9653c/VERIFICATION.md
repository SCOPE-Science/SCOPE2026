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

The lattice shift reduces deletion to index zero, and Zak unitarity turns synthesis into multiplication of a mean-zero polynomial by φ. The weighted negative Fourier norm dualizes to a point remainder: any representing function h satisfies φ̄h=ψ−d, and square integrability forces d=ψ(p) by the nonintegrable two-dimensional r^−2 singularity. Conversely subtract that constant and apply Cauchy–Schwarz to recover the synthesis inequality. In a spatial annulus of radius 2^−i the contribution of shell j is at most min(2^(j−i),1) times a_j=2^j‖ψ_j‖_2. The low-frequency part is bounded by convolution with a summable kernel; the high-frequency tail is the adjoint discrete Hardy inequality, giving the square cost Σ(1+j)^2 a_j^2. Monotonicity yields all β≥1. For β<1 the disjoint normalized frequency blocks all equal one at p, have real point remainders of the same sign, and lie in modulus below 1/2 on the relevant outer annuli once j≥i+K. Their weighted norm squared is o(N^3) while the annular remainder norm squared is bounded below by a constant times N^3, excluding the inequality. Completeness after deletion follows since an annihilator multiplied by φ̄ must be constant and 1/φ is not square integrable. The displayed point remainders divided by φ̄ give biorthogonals. For this complete minimal family, Riesz–Fischer is equivalent to Besselness of the biorthogonals; that Bessel bound gives the lower analysis bound by synthesis and completeness, and conversely the lower analysis bound applied to finite sums of biorthogonals gives their Bessel bound. The Gaussian expansion also checks directly by the Jacobi product: with q=e^−π and z=πξ−iπx only 1+q exp(2iz) vanishes in the cell; its derivative factor at p is −2π(u+iv), and the remaining prefactor is q^(1/4) times ∏_(ℓ≥1)(1−q^(2ℓ))^3, yielding the frozen coefficient.

## originality

PASS

Credit exactness and the simple-zero geometry, the existence of some positive weights, and sufficiency for β>1 in the Gaussian case to the verified antecedents and their combination. The distinctive result is the endpoint β=1 and matching necessity below it, with the sharp threshold extending to all windows with a quantitatively simple single Zak zero. The strongest inspected statements do not entail this distinction; overlap with equivalent critical logarithmic inequalities or uninspected portions of the Nyquist summability paper remains a qualified risk.

## value

PASS

This is a sharp endpoint left undecided by the available individual-biorthogonal summability criterion. It distinguishes the harmonic divergence of that sufficient test from failure of a lower semi-frame, settles the converse with an explicit counterfamily, and identifies a transferable mechanism for every window with a single quantitatively simple Zak zero.

The dated certificate retains the supplied scientific assessment, sources and limitations.
