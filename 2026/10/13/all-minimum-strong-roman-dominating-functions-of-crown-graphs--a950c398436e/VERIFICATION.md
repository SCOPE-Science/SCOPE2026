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

The proof uses an exact fixed-zero-support reduction. If the zero-index sets have sizes \(p\) and \(q\), intersection size \(c\), and \(r=n-p-q+c\) common-positive indices, then the least excess on the \(A\)-side needed to defend the \(q\) zero vertices in \(B\) is the smaller available value among
\[
\left\lceil\frac q2\right\rceil\quad(r\ge1)
\]
and
\[
2\left\lceil\frac{q-1}{2}\right\rceil\quad(q-c\ge2).
\]
The symmetric formula holds for the other side. This is exact because a common-positive strong vertex sees every opposite zero, whereas without such a vertex at least two inside-index strong vertices are necessary and two suffice.

The standalone script `verify_strong_roman_crown.py` performs three independent finite checks:

1. Direct exhaustive labeling enumeration for \(n=3,4,5\), using the defining strong Roman inequality at every zero vertex. It finds minimum values \(4,6,6\) and exactly \(3,76,5\) minimum functions, and checks equality of the entire enumerated minimum-function set with the theorem's classified family.
2. Exhaustive enumeration of every feasible integer zero-support triple \((p,q,c)\) for each \(3\le n\le50\), using the exact fixed-support formula. The only minimizing patterns are precisely the one odd pattern and five even patterns used in the proof.
3. Construction of every classified minimum function for \(3\le n\le20\), followed by direct evaluation of the defining strong Roman condition and the claimed weight.

Replay output:

`VERIFY_OK exhaustive_n=3..5 filtered_labelings=11182 pattern_n=3..50 pattern_checks=316236 classified_n=3..20 generated_minima=25719`

These finite checks validate boundary behavior and the implementation of the classification. They do not establish the theorem for unbounded \(n\); that is supplied by the symbolic fixed-support proof in RESULT.md.
