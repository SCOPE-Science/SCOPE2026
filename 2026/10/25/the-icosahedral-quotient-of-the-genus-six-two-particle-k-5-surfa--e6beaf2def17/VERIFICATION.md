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

Run `python3 check_k5.py` with Python 3 standard library. The checker reconstructs the cell sets and signed differentials, ensures the top cycle is primitive and satisfies each boundary relation, checks circular links and 1-skeleton connectivity, and replays every permutation and coordinate-exchange action. It then verifies the Lefschetz traces of double transpositions, three-cycles and five-cycles, the branch orbit arithmetic, and exact Riemann–Hurwitz identity using `fractions.Fraction`.

The package calculation has 20 vertices, 60 one-cells and 30 squares, Euler characteristic \(-10\), and 240 group-action checks. Its group actions are finite and exhaust all \(S_5\times C_2\) elements. The general geometric step (indices of fixed points of nontrivial orientation-preserving finite-order surface maps) is invoked as a standard theorem, not inferred from a sample.

The exact quotient depends on the indicated natural PL action. No complex-analytic structure, uniqueness among arbitrary genus-six actions, or independent audit is asserted.
