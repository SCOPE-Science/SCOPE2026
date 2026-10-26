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

# Verification and limits

Run `python3 CHECK.py` with standard Python 3. It enumerates every binary word of lengths \(1\) through \(13\) and groups every one-gap deck through length \(3\) by exact integer signature; at length \(13\) there are exactly \(8188\) groups, four of size two and \(8184\) singleton groups. All \(8192\) length-\(13\) signatures are independently replayed by explicit index-subset enumeration and a recurrence indexed by the last selected position. All four pairs are checked to share their intact three-deck and three separate punctured two-decks. Full punctured three-decks differ. Explicit two-sided contexts, independent concatenation choices for up to three blocks, and all \(16\) maximum-codebook symmetry actions are also tested.

The exact success message is `GAPPED_THREE_DECK_PASS words=8192 classes=8188 doubletons=4 codebooks=16 orbits=6`. Direct finite checks do **not** prove all-context substitution or the multiplicity bound for arbitrary numbers of blocks; their general proofs appear in `RESULT.md`, Sections 3–4. The primary source already gives one length-\(13\) pair and the threshold. No formal proof assistant or independent audit was used.
