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
The embedded `verify_slater_markov_first_layer.py` performs a complete exact census of labeled tournaments on one through five alternatives using only the Python standard library.

The Slater set is computed independently by:
1. enumerating every linear order and maximizing its number of forward tournament arcs;
2. a subset dynamic program that recursively maximizes the same objective and identifies all possible optimal first alternatives.

The Markov stationary distribution is computed independently by:
1. exact rational Gaussian elimination on the stationary linear system;
2. exact integer diagonal cofactors of the tournament Markov Laplacian via the directed matrix-tree theorem.

The verifier confirms:
- no Slater–Markov disparity at orders \(1,2,3,4\);
- exactly \(240\) disparities among the \(1024\) labeled tournaments of order \(5\);
- exact incidence \(15/64\);
- \(MA(T)\subsetneq SL(T)\) in every first-layer disparity;
- exactly \(120\) strict cases with sizes \((3,1)\);
- exactly \(120\) strict cases with sizes \((2,1)\);
- exactly two divergent isomorphism classes;
- orbit size \(120\) for each class, hence trivial automorphism groups;
- the two displayed out-neighborhood descriptions;
- stationary vectors \((9,3,1,13,17)/43\) and \((1/4,1/12,1/6,1/8,3/8)\).

Run:

`python3 verify_slater_markov_first_layer.py`

The first output line must be:

`VERIFY_OK`

The computation proves only the stated finite threshold layer through order \(5\).
