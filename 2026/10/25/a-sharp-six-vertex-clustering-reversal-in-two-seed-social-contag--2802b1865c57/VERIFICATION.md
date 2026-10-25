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

# Reproducible verification

Run `python3 artifacts/verify_cone.py` under Python 3 without external packages. The program performs the following exact checks using integer bitmasks and Python `fractions.Fraction`:

- Every peripheral simple graph with two through six vertices (33,866 cases), directly simulating all 704,182 choices of two distinct initial seeds in the corresponding cone; its final-size frequency table must equal the component-size generating-function table.
- Full enumeration of the \(2,8,64,1024\) labeled graphs with \(2,3,4,5\) vertices; the connected subtotals are \(1,4,38,728\). All degree-matched comparisons across distinct triangle counts are checked, ruling out a strict opposite ordering before six vertices.
- The two explicit network constructions at six, seven, eight, nine, thirteen and twenty-four vertices, with exact counts, degree multisets, triangle counts and rational expected final sizes.

The verifier must end in `ALL_CHECKS_PASSED`. The accompanying JSON certificate records counts and SHA-256 of the observed verification output. The code and certificate are reproducibility aids, not independent or externally certified mathematical audits.

The infinite-family statement rests on the symbolic component law and the explicit degree and triangle calculations, not on finite experiments. The nonnegative model has no stochastic transmission failures; its only randomness is the initial choice of two seeds.
