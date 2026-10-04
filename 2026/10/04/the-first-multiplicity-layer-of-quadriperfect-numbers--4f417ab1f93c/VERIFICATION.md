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

The unrestricted argument is in `RESULT.md`. The packaged checker uses exact
`Fraction` arithmetic throughout.

For every total multiplicity \(1\le m\le8\), it generates every unordered
exponent partition of \(m\). For each partition it tries every distinct
assignment of those exponents to the first required primes, thereby computing
an exact global abundancy upper bound for that partition.

It confirms the lower-layer maxima
\[
\frac32,\ 2,\ \frac{12}{5},\ \frac{14}{5},\
\frac{16}{5},\ \frac{192}{55},\ \frac{208}{55}
\]
for \(m=1,\ldots,7\).

At \(m=8\), it confirms that only
\[
(3,2,1,1,1),\quad
(3,1,1,1,1,1),\quad
(2,2,1,1,1,1)
\]
have optimistic abundancy at least \(4\). It then searches those three
patterns with the monotone future-prime upper bound described in the proof.

The exact search returns one assignment only:
\[
(2,3),(3,2),(5,1),(7,1),(13,1).
\]
Finally it directly computes the divisor sum and verifies
\[
\sigma(32760)=131040=4\cdot32760.
\]

No floating-point thresholds or finite size cutoffs are used in the
classification.
