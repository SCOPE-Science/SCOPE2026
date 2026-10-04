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

The bundled checker implements Definition 3.1 literally.

For a relation \(R\) on
\[
C_n=\{0,\ldots,n-1\},
\]
it tests:

\[
vRw\le w'
\Longrightarrow
\exists v'\ge v\;v'Rw',
\]
and
\[
v'\ge vRw
\Longrightarrow
\exists w'\ge w\;v'Rw'.
\]

For every relation through
\[
n=4,
\]
it separately computes row maxima \(a_i\) and column maxima \(b_j\), using \(-1\) for emptiness, and checks that the direct Definition 3.1 predicate is equivalent to monotonicity of both maxima sequences.

The direct counts are
\[
2,\ 9,\ 118,\ 4849.
\]

The checker then independently enumerates nondecreasing maxima pairs through
\[
n=6.
\]
It tests
\[
i\le b_{a_i}
\]
for every nonempty row and
\[
j\le a_{b_j}
\]
for every nonempty column, forms
\[
A(a,b)=\{(i,j):j\le a_i,\ i\le b_j\}
\]
and the forced boundary set \(F(a,b)\), and sums
\[
2^{|A(a,b)|-|F(a,b)|}.
\]

The resulting counts are
\[
2,\ 9,\ 118,\ 4849,\ 697066,\ 378458905.
\]

Where both methods are run, the counts agree exactly.

The script prints `VERIFY_OK`.

## Limits

The finite replay corroborates the proof. The maxima equivalence and reconstruction theorem are proved for arbitrary finite \(n\); no inference from the first six counts is used. No asymptotic claim is made.
