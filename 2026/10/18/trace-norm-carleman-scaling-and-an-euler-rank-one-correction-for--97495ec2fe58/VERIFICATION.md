---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The gamma moment map is Hilbert–Schmidt by summing Γ(β)/[n(q+2 log n)^β] for β>1. Its two Gram operators have exactly matching nonzero eigenvalues, with multiplicities. Rescaling x=qu on the weighted space contributes q^(−β); multiplying by q^(β−1) gives the factor 1/q in the zeta kernel. For F(v) the rank-one operator on a_β(x)e^(−vx), the companion is harmonic quadrature and the Carleman limit is the integral of F. The trace norm of F is Γ(β)(1+2v)^(−β). Using F(v)=−∫_v^∞ F′(s)ds justifies the discrepancy identity by absolute integration, including the n=1 atom at zero. The discrepancy satisfies 0<D_q≤1/q and |qD_q−γ|≤4e^(−qv). Combining this with the derivative bound 2√(Γ(β)Γ(β+2))(1+2v)^(−β−1) gives the stated remainder and its constant 8. Integrating the derivative bound without the exponential gives Γ(β)√((β+1)/β)/q and hence the ℓ¹ spectral bound. The traces of K_β and P_β are Γ(β−1)/2 and Γ(β), and q(S−K) tends in trace norm to γP, establishing both trace claims. Compactness and the strictly positive real kernel give a strictly positive top eigenvector and simplicity by the strict Rayleigh gain for any sign-changing top eigenvector; the isolated-eigenvalue first variation gives the positive first-order term with gap-controlled O_β(q^−2) remainder. This is nuclear convergence on the companion L² space, not a claim of direct matrix convergence on ℓ². The scalar script was inspected, not executed; the uniform estimate has an analytic verification.

## originality

PASS

The known moment/trace-class framework and exact zeta companion must be credited, as must existing qualitative Carleman comparisons. The distinct supported contribution is a parameter-explicit trace-norm expansion of the rescaled continuous gamma companion with a sharp Euler rank-one first term, and its spectral consequences. None of the compared fixed-weight theorems or distinct atomic and weak-coupling records gives that expansion.

## value

PASS

The estimate transfers the complete scaled nonzero spectrum in ℓ¹ and quantifies the leading nuclear defect, not just a pointwise kernel limit or a scalar trace. The rank-one Euler coefficient is meaningful for both trace and leading eigenvalue, and the bound explains precisely where this fixed-β trace-class comparison applies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
