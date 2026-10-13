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

The finite check is implemented in `verify.py` with exact arithmetic modulo \(17\).

It reconstructs the nine projective columns \(P(t)=(1,t^3,t^4)\) for \(t\in\{0,2,3,4,5,7,9,10,16\}\).  First it checks all \(84\) three-column subsets have rank \(3\), independently verifying the MDS premise for the displayed generator.

For each surviving subset \(T\) of size \(5\) through \(9\), it forms the matrix of evaluations of \(X^2,Y^2,Z^2,XY,XZ,YZ\) and computes its rank by exact modular row reduction.  Rank below \(6\) is exactly the existence of a conic through \(T\); because the projective points form an arc and \(|T|\ge5\), such a conic cannot be degenerate.

The exhaustive expected census is:

- size \(9\): one rank-\(6\) set;
- size \(8\): nine rank-\(6\) sets;
- size \(7\): thirty-six rank-\(6\) sets;
- size \(6\): six rank-\(5\) sets and seventy-eight rank-\(6\) sets;
- size \(5\): one hundred twenty-six rank-\(5\) sets.

The verifier also reconstructs one quadratic equation for each exceptional six-set and checks that their complements are exactly the six deletion triples stated in the result.  No probabilistic, numerical, or incomplete search step is used.

Unproved limits: this finite verification does not prove a family-wide statement for the source constructions, does not study shortening, and does not establish absolute literature novelty.
