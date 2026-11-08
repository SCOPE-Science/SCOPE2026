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

For all stable real 2×2 B and SPD D, S solves Lyapunov BS+SBᵀ=2D and is SPD; whitened G_t=e^{-S^-1/2 B S^1/2 t} has SPD innovation I−GGᵀ for t>0. The two-time stationary zero-mean Gaussian joint covariance and its swapped version have equal determinants; direct inversion yields I(t)=(G12−G21)^2(1−det G)/det(I−GGᵀ). Cayley–Hamilton B−μI squared=(μ²−detB)I gives G_t=a_t I+b_t K with b_t proportional to hyperbolic sinh, t, or sin(Ωt). For irreversible Δ=K12−K21≠0 this gives no positive zeros with real spectrum and *exactly* t=kπ/Ω for complex spectrum, where the full discrete-time Gaussian autoregressive chain is reversible. Taylor expansion gives q Δ²/(1−q)h²+O(h³) at each zero. The isotropic rotational case yields explicit 4e^{-2αt}sin²(ωt)/(1−e^{-2αt}); physical EPR remains 2ω²/α. Motivating Dey branch A~(a+b)τ,C~−aτ gives t1~πr/(aτ) and EPR*t1→2πa/(a+b), conditional on the Nash stable branch. Independent numeric 4×4 covariance KL for a non-normal anisotropic example gives zero at t≈1.73004528 and near-zero coefficient 0.259125 vs exact 0.259733, consistent with first-order finite h error.

## originality

PASS

Best-of-knowledge PASS for exact *full-state sampled planar Gaussian* two-time reversed KL identity, iff complete spectral zero-lag classification, and strict quadratic recovery constant. Stroboscopic aliasing and inference ambiguity themselves are well-known (Bauer–Seifert–van der Meer finite jump chains). Stationary current/OU dissipation decompositions are known (Nagayama–Kolchinsky–Ito), and Dey supplies the game drift and EPR. Scalar Gaussian projection invisibility (Lucente et al) is different: here the full state is observed and only special sampling cadences hide irreversibility. No inspected exact source gives these jointly evaluated conclusions, though older AR(1) Gaussian reversibility formulas could conceal the algebra.

## value

PASS

Identifies exactly when a genuinely dissipative, fully observed planar Gaussian system appears reversible under discrete observation, distinguishes complex from real spectra sharply, quantifies local information recovery, and translates the condition into a concrete short-foresight game where entropy per invisible interval remains positive. Full-state cadence-dependent aliasing is a nontrivial measurement-design invariant distinct from standard continuous-time EPR or trivial scalar-projection reversibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
