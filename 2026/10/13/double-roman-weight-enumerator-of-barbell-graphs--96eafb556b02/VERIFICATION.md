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

The symbolic proof conditions each clique on the label of its bridge endpoint and the label across the bridge. The four endpoint rows are exhaustive, and gluing the two sides yields the matrix identity
\[
\mathcal D_n(x)=\operatorname{tr}\bigl(M_n(x)^2\bigr).
\]
For \(n\ge4\), the minimum-layer proof is separate from the generating-function calculation: every clique side has weight at least \(3\), and side weight \(3\) is possible exactly with one label \(3\) and all other labels \(0\). Hence the minimum weight is \(6\) with exactly \(n^2\) minimum functions.

The packaged `verify_double_roman_barbell.py` constructs the graph directly and tests the double Roman conditions from adjacency. It exhaustively checks all \(4^{2n}\) labelings for \(2\le n\le5\), compares the full coefficient table to the closed transfer formula, and verifies the minimum layers. It then evaluates the exact formula through \(n=12\) as an additional finite consistency check.

Replay output:

`VERIFY_OK n_bruteforce=2..5 labelings=1118464 valid_functions=892974 formula_n=2..12 coefficient_checks=408 max_order=24`

The finite replay does not establish the infinite family. The all-\(n\) statement rests on the symbolic endpoint-state proof in `RESULT.md`.
