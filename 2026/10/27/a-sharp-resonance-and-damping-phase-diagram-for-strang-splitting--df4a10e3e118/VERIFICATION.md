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

The exact flow is Hurwitz since its characteristic polynomial is λ²+γλ+ω² with γ,ω>0. Multiplying the three exact substeps gives S_h=[[r²c,−rs],[rs,c]] with r=e^(−γh/2), c=cos(ωh), s=sin(ωh). The determinant is r² and the trace (1+r²)c, so the determinant-normalized quadratic gives the stated radius in both discriminant regimes. Equality in the norm contraction requires a vector in the undamped axis before the first damping factor and after rotation; this happens precisely when s=0, with undamped eigenvalue ±1. The determinant bound is attained on |c|≤sech(γh/2). At fixed damping per step α the angular width is 2arcsin(sech α)=4e^(−α)+O(e^(−3α)); this is not a fixed-width claim in h when α follows h. At a fixed positive resonance let δ=ω(h−h_m) and r_m=e^(−γh_m/2). For the absolute dominant eigenvalue the simple unit root gives deficit ((1+r_m²)/(2(1−r_m²)))δ²+O(δ³). For squared singular values the trace is 2r²+(1−r²)²cos²δ and the determinant r⁴. Expanding its larger simple root at one gives deficit ((1−r_m²)/(1+r_m²))δ²+O(δ³); taking the square root halves it. Changes of r by O(δ) first affect cubic terms. Both leading coefficients are positive, and discriminant-zero spectral rates do not imply bounds without a possible Jordan prefactor. Independent NumPy eigenvalue and SVD checks on both sides of three positive resonances corroborated the two distinct limits (python3 /workspace/reproductions/frozen_checks.py 3).

## originality

PASS

Passivity and the Strang update are known; the normalized 2×2 trace/discriminant calculation likewise uses a standard test, and qualitative resonance is not novel. The distinct claim is the sharp quantitative classification for this particular rank-one-damped exact map, pairing its optimally decaying phase band with two different near-resonant laws for asymptotic spectral versus single-step Euclidean decay. The strongest inspected exact-oscillator result is about the RK4 stability polynomial, not this map. The primary statements on port-Hamiltonian passivity and conservative splitting resonance do not supply the joint quantitative result. This is a modest model-specific contribution, not a new general stability criterion.

## value

PASS

A passive integrator that does not decay at specific steps is a useful counterexample to inferring asymptotic stability from an energy inequality. The optimally decaying band and its narrowing quantify where this simple split performs best, while the unequal sharp coefficients distinguish relative long-run decay from one-step Euclidean energy control. This gives a parameter-uniform benchmark beyond the textbook quadratic formula alone, without claiming multi-mode or finite-precision guarantees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
