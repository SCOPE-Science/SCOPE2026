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

The range 0<γ≤2/(α+β) implies |1−γα|,|1−γβ|<1, even at the upper endpoint. Every path converges absolutely in state to a feasible point. The independent first draw gives T=γσ_I+(1−γa_I²)T′ in law, with T′ independent. Solving the first two uncentered moment equations recovers both moments and the risk; the squared distance factor is αβy²/(α+β) by projection onto (b,−a). Independent symbolic replay: python3 /workspace/branches/check_selection_derivative.py (SymPy); it checks the moments, derivative coefficients, upper-step simplification and exact benchmark. Below 2/s, C₂>0 and C₀<0 for α>β, hence precisely one positive derivative root and negative derivative at 0. The derivative at 1 has the sign of 4−γ(3α+β), which proves the transition and uniqueness, including the equality case. At 2/s the displayed fractional linear risk strictly decreases; as γ tends to zero the risk converges uniformly to (2p−1)²/d², unique minimum at 1/2. The benchmark gives the stated algebraic root and relative loss reduction. In the fair case residuals are 2⁻ᵏ, the binary cylinders give Uniform[0,1], and nonnegative iterates with sum ≤1 satisfy the required uniform bound; the risk is 1/6. Jin–Liu Algorithm 1 is uniform and its theorem range is strict, but this fair example lies strictly inside it. It refutes only the minimum-norm implication of Remark 2.5, not Theorem 2.4's random-solution assertion; the terminal solution is not past-measurable in the conditional-expectation argument. The uploaded verifier was inspected, not run; the all-path and limiting arguments are analytical.

## originality

PASS

The supported distinction is the exact terminal minimum-norm selection risk optimized over fixed coordinate probabilities for unequal columns, with a sharp interior-to-boundary step threshold, and the bounded fair-digit witness for the specific prior remark. Bernoulli binary expansion is classical, and the equal-column limiting expected risk is directly shared with an indexed special case. Checked weighted-sampling results optimize objective/rate bounds or schedules, not this terminal selector. No exhaustive priority claim is made.

## value

PASS

The objective is which exact solution the algorithm selects, not whether it fits the data. The sharp threshold shows that even optimal iid selection can switch to never updating one coordinate despite a consistent problem with two usable coordinates. The fair-digit construction answers a concrete incorrect implication in the motivating literature and locates the obstruction despite pathwise boundedness and geometric residual convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
