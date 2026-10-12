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

Run `python3 verify_rank.py` with standard Python 3. The recorded run returned `VERIFY_OK`, confirming \(66{,}066\) exhaustive relations on one through four worlds, \(9{,}000\) seeded random relations on five through ten worlds, and the sharp path constructions for \(m=0,\ldots,50\).

The program independently evaluates \((\Box\Diamond)^j\top\) by Boolean successor masks and compares this with the predecessor-based failure-set recurrence. It also explicitly reconstructs the \(2j\)-world witness ladder whenever a new failure layer occurs and checks that no finite-rank point has only finite-rank successors.

No fixed-size or randomized computation proves the universal lower bound; its proof uses a minimal failure rank and an induction along the witness ladder. There is no external or independent audit evidence.
