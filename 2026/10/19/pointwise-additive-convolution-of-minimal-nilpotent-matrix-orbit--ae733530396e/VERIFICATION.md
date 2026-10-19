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

# Computational verification

Run `python3 verify_fibers.py` (standard-library Python 3; no third-party packages). The program constructs all nonzero rank-one square-zero matrices directly from outer products and counts every ordered sum. Separately, it computes matrix rank, trace, square rank, invariant projective lines of the restriction to the image, and the predicted count. A mismatch raises an assertion. The final line must be `ALL_EXACT_CHECKS_PASSED`.

The full target spaces and all ordered summand pairs were exhaustively checked in dimensions and field sizes \((n,q)=(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(4,2)\). The implementation models \(\mathbb F_4\) as \(\mathbb F_2[x]/(x^2+x+1)\). It checks the normalization \(|\mathcal O|=(q^n-1)(q^{n-1}-1)/(q-1)\) and total mass \(\sum_C F(C)=|\mathcal O|^2\). Observed histogram for \((n,q)=(3,3)\): fiber size \(104\) occurs once, \(13\) occurs \(104\) times, \(6\) occurs \(624\) times, \(4\) occurs \(702\) times, and \(2\) occurs \(1404\) times; all other targets have zero fiber. No infinite proof is claimed from these computations.

The general proof is a direct bijection with complementary image-line decompositions, followed by a complete eigenline count in a two-dimensional vector space. No external certificates, unseen experiments, or independent audit are claimed.
