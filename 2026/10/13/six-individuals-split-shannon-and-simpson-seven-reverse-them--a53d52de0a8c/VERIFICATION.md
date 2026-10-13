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
The embedded `verify_shannon_simpson_minimal_reversal.py` performs a complete exact replay.

For every census size
\[
2\le N\le7,
\]
it independently constructs the full set of abundance profiles in two ways:
- recursive integer partitions;
- all compositions of \(N\), sorted and deduplicated.

For each profile \(\lambda=(n_1,\ldots,n_s)\), Shannon ordering is computed without floating logarithms through
\[
P(\lambda)=\prod_i n_i^{n_i},
\]
because
\[
H(\lambda)=\ln N-\frac1N\ln P(\lambda).
\]

Simpson ordering is computed from
\[
Q(\lambda)=\sum_i n_i(n_i-1)
\]
and exact rational values of
\[
D(\lambda)=1-\frac{Q(\lambda)}{N(N-1)}.
\]

The replay verifies profile counts
\[
2,\ 3,\ 5,\ 7,\ 11,\ 15,
\]
ordering-mismatch counts
\[
0,\ 0,\ 0,\ 0,\ 2,\ 4,
\]
and strict-reversal counts
\[
0,\ 0,\ 0,\ 0,\ 0,\ 2.
\]

It also checks the exact first tie-splitting pairs at \(N=6\), the exact first strict-reversal pairs at \(N=7\), and fixed-\(N\) ordering equivalence between the finite-sample Simpson convention and population Gini-Simpson diversity.

Run:

`python3 verify_shannon_simpson_minimal_reversal.py`

The first output line must be:

`VERIFY_OK`
