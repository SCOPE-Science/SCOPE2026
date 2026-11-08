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
# Reproducible finite checks

Run `python3 verify.py` in this directory. The standalone script builds the support-disjointness graph directly and checks **explicit cycles**: one on 25 supports for rank 5, two disjoint cycles covering 52 supports for rank 6, and three disjoint cycles covering 108 supports for rank 7. It also independently checks a rank-5 single 25-cycle. Every witness uses valid, distinct, nonpendant supports; successive and closing supports are disjoint; no support occurs twice across cycles.

For ranks 5 through 10, the checker constructs the graph edges and tests the structural restrictions on edges within the upper layer used in the proof, as well as exact Boolean level counts and the upper bound's numerical values. It is not an exhaustive search over all cycles or a proof for unbounded rank. Its finite certificates establish lower bounds for particular ranks only; the universal upper bound follows from the degree-two argument in RESULT.md.

Independent numerical integer-programming exploration with degree constraints found 2-factor coverage values 25, 52 and 108 for ranks 5, 6 and 7, respectively. No solver is needed to replay the delivered witnesses. The results do not prove an exact circumference formula at rank 8 or above; self-review is not an independent audit.
