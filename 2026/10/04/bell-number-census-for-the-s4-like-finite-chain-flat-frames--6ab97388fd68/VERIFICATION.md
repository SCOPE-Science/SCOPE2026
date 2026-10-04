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

Every upward-flat relation on the \(n\)-chain is represented by a threshold vector
\[
(t_0,\ldots,t_{n-1})\in\{0,\ldots,n\}^n,
\]
where
\[
iRj
\quad\Longleftrightarrow\quad
j\ge t_i.
\]

The verifier constructs the relation explicitly from every threshold vector through
\[
n=6.
\]
It checks reflexivity of
\[
\leq\circ R
\]
and transitivity of \(R\) directly at relation level.

Independently, it computes
\[
m_i=\min_{u\ge i}t_u
\]
and tests the symbolic criterion
\[
m_i\le i
\]
for all \(i<n\), together with
\[
m_q=q
\]
for every occurring finite threshold \(q\). The direct and symbolic tests agree for every enumerated relation.

The exact accepted counts are
\[
1,\ 3,\ 10,\ 37,\ 151,\ 674
\]
for
\[
n=1,\ldots,6.
\]

A second calculation sums the fixed-point plateau formula through
\[
n=12
\]
and independently computes Bell numbers by recurrence. The two values agree exactly at every checked size.

The script prints `VERIFY_OK`.

## Limits

The finite replay corroborates the proof. The theorem for arbitrary \(n\) follows from the threshold classification and generating-function argument, not from extrapolation. No general finite-poset census is claimed.
