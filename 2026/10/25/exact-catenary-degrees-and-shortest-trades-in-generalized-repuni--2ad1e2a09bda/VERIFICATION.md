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

# Reproducibility and limits

Run `python3 verify.py` with standard Python 3 and no external dependencies. The program recomputes the generators and all the displayed matrix-minor identities, confirms every determinantal relation has fragment length at most \(a+b+1\), and exhaustively tests the absence of a smaller pure-generator replacement across 118 admissible parameter triples. For 18 small triples, it enumerates all factorizations in 59 distinct degree fibers and uses a minimum-bottleneck spanning-tree computation to check the maximal fiber degree equals \(a+b+1\). These are finite tests, not independent certification of the published determinantal theorem or an infinite proof.

The complete theoretical argument appears in `RESULT.md`. In particular, it depends on Corollary 9 of Branco–Colaço–Ojeda (arXiv:2111.03714), and it proves the complementary lower bound and the uniqueness of the critical factorization pair. Independent audit was not performed.
