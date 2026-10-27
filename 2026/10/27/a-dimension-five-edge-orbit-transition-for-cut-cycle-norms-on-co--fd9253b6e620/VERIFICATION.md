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

# Verification

The independently written check `coned_cube_exact_checker.py` uses Python 3, SymPy for exact grounded-Laplacian matrix inversion, and the standard-library `fractions.Fraction` class. Invoke it with `python coned_cube_exact_checker.py`.

For dimensions \(2\) through \(6\), the checker constructs the entire unweighted graph, grounds the apex, and solves two exact rational Laplacian systems, one for each edge orbit. Every edge current is summed directly and compared with both analytical projection-column formulas and exact diagonal currents; these graphs contain 444 edges in total. This is distinct from evaluating the radial symbolic expression.

For dimensions \(1\) through \(30\), a second calculation forms the resolvent from the Walsh eigenvalue expansion. It verifies positivity and strict monotonicity of the radial current differences, all absolute-current sum identities, and every edge-orbit inequality. The algebraic proof of the unrestricted statement appears in RESULT.md and uses heat-kernel integrals; these finite checks are not an exhaustive proof for all dimensions.

The strict inequality for all \(n\ge6\) is analytic: the diagonal resolvent exceeds \(1/(n+1)\), so the cycle orbit gap exceeds \((n-1)/15-2/(n+1)>0\). Dimensions \(2\), \(3\), \(4\) and \(5\) are evaluated exactly as rational fractions. The ordinary-cube comparison follows by direct subtraction of its established exact formula.

Limitations: no independent mathematical audit; exact checks assume the unweighted incidence Laplacian and canonical orthogonal projections; no additional parameter ranges or weighted claims are asserted.
