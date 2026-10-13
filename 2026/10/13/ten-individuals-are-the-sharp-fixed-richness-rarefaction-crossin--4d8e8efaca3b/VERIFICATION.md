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
For a positive integer abundance profile
\[
n=(n_1,\ldots,n_S)
\]
with total
\[
N,
\]
the expected richness after drawing \(m\) individuals uniformly without replacement is
\[
R_m(n)
=
\sum_{i=1}^{S}
\left[
1-
\frac{\binom{N-n_i}{m}}{\binom{N}{m}}
\right].
\]

The embedded `verify_rarefaction_crossing_boundary.py` performs a complete finite check through
\[
N=10.
\]

It independently generates every abundance multiset in two ways and requires the generated sets to coincide for every fixed richness.

It then checks every unordered same-\((N,S)\) pair at every interior sample size and verifies:

\[
N\le9:
\]
no strict rarefaction crossing;

\[
N=10:
\]
exactly one unordered crossing pair,
\[
(6,2,2)
\quad\text{and}\quad
(5,4,1).
\]

It also checks all exact witness values, the sign change between
\[
m=3
\]
and
\[
m=4,
\]
and the identities
\[
R_2
=
2-
\frac{\sum_i n_i(n_i-1)}{N(N-1)}
\]
and
\[
R_{N-1}
=
S-\frac{f_1}{N}.
\]

Run:

`python3 verify_rarefaction_crossing_boundary.py`

The first output line must be:

`VERIFY_OK`

All expectations and comparisons use exact rational arithmetic.
