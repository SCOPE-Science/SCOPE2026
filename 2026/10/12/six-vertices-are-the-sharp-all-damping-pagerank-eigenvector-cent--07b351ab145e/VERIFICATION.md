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
The embedded `verify_pagerank_eigenvector_boundary.py` performs two exact checks.

First, it generates all connected simple graph isomorphism classes through order five, reproducing
\[
1,2,6,21
\]
classes for orders \(2,3,4,5\).

For each graph it solves uniform-teleportation PageRank exactly as rational functions of
\[
\alpha.
\]
It isolates every real root in
\[
(0,1)
\]
where a pairwise PageRank difference can vanish, checks one exact point in every intervening interval, and checks the roots themselves.

Adjacency-eigenvector maximizers are compared exactly from principal cofactors evaluated at the Perron root.

Second, for the six-vertex witness with edges
\[
\{01,02,03,34,35,45\},
\]
the verifier checks the adjacency characteristic polynomial
\[
x(x+1)(x^4-x^3-5x^2+3x+4),
\]
certifies the unique eigenvector-centrality maximizer \(3\), derives the exact PageRank formulas, and proves that vertex \(0\) is the unique PageRank maximizer for every
\[
0<\alpha<1.
\]

Run:

`python3 verify_pagerank_eigenvector_boundary.py`

The first output line must be:

`VERIFY_OK`

SymPy is required for exact algebraic-root and symbolic-rational arithmetic.
