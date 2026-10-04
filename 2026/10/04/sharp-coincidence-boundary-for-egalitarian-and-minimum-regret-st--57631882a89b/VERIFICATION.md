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
The embedded `verify_egalitarian_minregret_boundary.py` provides an exact finite replay.

It uses two independently written stability tests. One precomputes rank maps and searches for blocking pairs by rank comparison. The other performs direct preference-list index comparisons. Their complete stable-matching sets must agree for every tested instance.

The replay exhausts:
- all \(16\) strict \(2\times2\) profiles;
- all \(46656\) strict \(3\times3\) profiles and all six perfect matchings of each;
- all \(24\) perfect matchings of the displayed \(4\times4\) witness.

For \(3\times3\), it verifies the exact objective-set relation counts:
- \(40056\) profiles with \(E(I)=R(I)\);
- \(5400\) profiles with \(E(I)\subsetneq R(I)\);
- \(1200\) profiles with \(R(I)\subsetneq E(I)\);
- zero profiles with nonnested overlap;
- zero profiles with disjoint optimum sets.

It independently reproduces the stable-count marginal \(34080,11484,1092\) for one, two, and three stable matchings.

For the \(4\times4\) witness, it verifies that exactly two perfect matchings are stable. Their participant-rank vectors are
\[
(1,1,3,2,1,3,3,1)
\]
and
\[
(2,1,4,2,1,1,1,1),
\]
with objective pairs
\[
(15,3)
\quad\text{and}\quad
(13,4)
\]
for total rank and regret. Thus the unique egalitarian and minimum-regret optima are different.

Run:

`python3 verify_egalitarian_minregret_boundary.py`

The first output line must be:

`VERIFY_OK`

The computation proves only the stated finite boundary and does not infer a larger-market classification.
