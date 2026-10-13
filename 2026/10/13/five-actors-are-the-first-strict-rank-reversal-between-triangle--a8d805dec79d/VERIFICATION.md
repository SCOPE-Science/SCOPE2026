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
The embedded `verify_signed_balance_rank_reversal.py` performs an exact finite replay using only the Python standard library.

It exhausts all raw sign assignments on \(K_3\), \(K_4\), and \(K_5\).

For each signing it computes:
- unbalanced triangles directly from edge-sign products;
- frustration by exhaustive vertex bipartitions;
- frustration independently as the minimum number of negative edges over every switching.

It then switches every signing to the unique representative having all edges incident with vertex \(0\) positive and quotients the normalized switching classes under all vertex permutations using the unbalanced-triangle pattern.

The verified switching-isomorphism tables are:
\[
K_3:\ (0,0),(1,1),
\]
\[
K_4:\ (0,0),(2,1),(4,2),
\]
and
\[
K_5:\ (0,0),(3,1),(4,2),(5,3),(6,2),(7,3),(10,4),
\]
where each ordered pair is \((U,L)\).

The corresponding labeled switching-class multiplicities at order five are
\[
1,10,15,12,15,10,1.
\]

There is exactly one strict rank-reversing pair:
\[
(5,3)\quad\text{versus}\quad(6,2).
\]

The packaged representatives have normalized negative-edge sets
\[
\{12,14,23\}
\]
and
\[
\{14,23\},
\]
with
\[
(T,F)=\left(\frac12,\frac25\right)
\]
and
\[
(T,F)=\left(\frac25,\frac35\right).
\]

Run:

`python3 verify_signed_balance_rank_reversal.py`

The first output line must be:

`VERIFY_OK`
