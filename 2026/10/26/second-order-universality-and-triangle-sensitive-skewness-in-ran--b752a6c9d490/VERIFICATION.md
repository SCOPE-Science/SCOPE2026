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

# Reproduction checks

Run `python3 check.py` in the same directory. The checker uses only the Python standard library, enumerates **all** uniform orientations of all simple host graphs on one to four vertices, plus the complete graph on five vertices, the triangular prism, \(K_{3,3}\), and the Petersen graph. For each host it computes centered dispersion directly from outdegrees, calculates exact integer raw moment sums, and compares to the all-graph formulas. For regular hosts it evaluates every mean and every entry of the score-frequency covariance matrix exactly using rational arithmetic. In the recorded local run it printed:

`PASS: 444 exact integer/rational assertions; all host graphs through 4 vertices, plus K5, prism, K3,3, and Petersen.`

The analytic Rademacher monomial proof in `RESULT.md` independently covers arbitrary finite simple graphs, including graphs larger than those enumerated. Exact finite computations do not prove infinite-domain identities. Independence of the review, historical originality and extension to dependent/biased orientations have not been established.
