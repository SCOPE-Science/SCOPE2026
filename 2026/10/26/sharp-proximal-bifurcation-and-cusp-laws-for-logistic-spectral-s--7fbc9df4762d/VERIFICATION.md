---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of logistic proximal bifurcation

The proof in RESULT.md differentiates \(h_a\), shows the unique maximum of its slope, and reduces proximal stationarity to \(S_\beta(t)=s\). The energy identity \(\frac{d}{dt}J_{\beta,s}(h_a(t))=(S_\beta(t)-s)h_a'(t)\) enables a global comparison of the two local minima, and strict monotonicity of their energy difference proves a unique coexistence datum. Uniform Taylor limits around the critical point yield the cubic response and the two onset constants. A finite computation cannot replace these steps.

For reproducible numerical diagnostics, run `python prox_bifurcation_check.py` with Python 3 and SciPy. The script checks the slope maximum, identity \(s_c=2h_a(t_0)\), two folds, numerical equality of the two outer-well energies, and convergence to the analytically derived fold and jump constants for \(a\in\{1.5,4,8\}\) at offsets \(0.1\), \(0.02\), and \(0.002\) above the critical scale.

Observed diagnostic outcome: all 9 supercritical parameter cases passed, with numerical relative fold-width and jump ratios approaching one as the offset decreased. These finite evaluations do not prove uniqueness for every datum or the limiting statements for arbitrary hardness. No independent audit or external formal proof certification has been performed.
