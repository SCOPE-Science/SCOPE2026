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

# Verification notes

The executable `verify.py` constructs all ordered Boolean-join decompositions and all distinct unordered decompositions directly from bitmask unions. It enumerates all choices of two random truth sets for dimensions \(k=0,1,2,3\), using rational weights at \(p=1/2\) and \(p=1/3\), and directly recomputes the two expectations, two variances, and covariance. It separately enumerates cross-type shared-bit pairs and checks the degree-square inequality for these dimensions. Self-fusion is checked against an independent double loop over all ordered pairs; its only diagonal witness is the top world.

Execute using `python3 verify.py` (standard Python 3 only). Expected final line: `VERIFY_OK 8 exact enumerations and 4 dependency-graph checks`. These checks are finite and do not establish convergence. The proof of the limiting Poisson product law relies on the precise dependency-neighborhood hypotheses of Arratia–Goldstein–Gordon (1989), Theorem 2, after separately computing the \(3^k\), \(5^k\), and \(2^k\) incidence sums. No computer-assisted infinite proof is asserted.
