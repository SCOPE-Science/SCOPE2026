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

# Verification record

The exact formula and the deck-fiber coefficient identity follow from reconstruction of the marker order, reconstruction of all two-letter gap compositions, the adjacent-swap interval lemma, and symmetry of weak compositions, as established in `RESULT.md`. The source checker separately computes each deck by literal ordered position pairs and counts their fibers, then obtains predicted fibers from within-gap Gaussian polynomials. Execute `python3 checker.py` to reproduce the 36 tested parameter triples and 23,526 total source words, with recorded output `checker-output.txt`.

The finite tests do not establish general validity by themselves, and the literature comparison has a stated access limitation for one relevant recent source. No independent scientific audit has been performed.
