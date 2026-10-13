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
The embedded `verify_freeman_tree_centralization_reversal.py` gives an exhaustive exact replay.

For every order
\[
3\le n\le8,
\]
all labeled trees are generated from all Prüfer sequences of length \(n-2\). Tree isomorphism classes are then deduplicated using the standard center-or-bicenter recursive branch code.

The recovered unlabeled-tree counts are
\[
1,\ 2,\ 3,\ 6,\ 11,\ 23.
\]

For a tree \(T\), degree centralization is computed exactly from the degree list. Betweenness of a vertex is computed without shortest-path numerics: if deleting the vertex produces component sizes
\[
s_1,\ldots,s_k,
\]
then
\[
b(v)=\sum_{i<j}s_i s_j.
\]

The strict-reversal counts for orders \(3\) through \(8\) are
\[
0,\ 0,\ 0,\ 0,\ 0,\ 8.
\]

For the witness,
\[
S(4,1,1,1):
\quad
C_D=\frac37,\quad C_B=\frac{11}{21},
\]
and
\[
S(3,2,2):
\quad
C_D=\frac5{21},\quad C_B=\frac47.
\]

Run:

`python3 verify_freeman_tree_centralization_reversal.py`

The first output line must be:

`VERIFY_OK`
