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

With normalized weighted Bergman measure dμ_α=(α−1)(1−|z|²)^(α−2)dA/π, α>1, the monomial moments μ_n=n!/(α)_n are the correct normalization. Orthogonality yields ||f(r·)||_4^4=Σ μ_n r^(2n)|Σ_{k=0}^n c_kc_{n−k}|². At r²=1/2 the quadratic deficit in a cancels identically. For f=1+az+h, h=Σ_{n>=2}b_nz^n, decompose f²=P+R with P=1+2az+a²z²+2h and R=2azh+h². R has no degrees 0,1,2, preventing cross-terms with the constant/critical mode. Completing the square gives exactly |a|^4/[α²(α+1)]+μ_2|b2−a²/2|²+Σ_{n>=3}(2−2^{2−n})μ_n|b_n|², where μ_2=2/[α(α+1)]. The dilation reproducing kernel bounds ||h(r·)||∞ by C_α||h||₂, and cross-tail orthogonality bounds the remainder by C_α(|a|+H+(|a|+H)²)H²+O(|a|²H²+H⁴), hence little-o of |a|⁴+H² uniformly over all high modes. The positive form controls this scale; the rigidity iff b2=a²/2+o(a²), higher-mode H=o(a²) follows. The affine comparison coefficient is (α+2)/[2α²(α+1)]. Source checks/check.py uses exact rational complex coefficients and derives the structural remainder; independently checked first moments and square completion. Finite checks are not the infinite-dimensional proof. This is a local fixed-α theorem, not global stability.

## originality

PASS

Global A²-to-A⁴ weighted Bergman dilation contractivity at the sharp radius belongs to Melentijević and earlier selected-parameter work by Bayart et al. The evaluated quartic defect, resonant b2=a²/2 correction, strictly coercive higher modes and all-mode remainder are finer local data not stated in the inspected hypercontractivity theorems. A general published nonlinear stability theorem might implicitly contain this special expansion; the risk is documented rather than treating failed searches as priority proof.

## value

PASS

At the sharp contractivity radius the first-mode quadratic variation vanishes: ordinary Hessian stability is inadequate. The exact quartic normal form identifies the unique nonlinear tangent direction of least deficit and measures each higher mode, a mathematically natural degeneracy/stability invariant. It distinguishes the finite-weight effect from Gaussian scaling and is more than a Taylor calculation on an arbitrary polynomial because the proof controls infinitely many analytic modes uniformly.

The dated certificate retains the supplied scientific assessment, sources and limitations.
