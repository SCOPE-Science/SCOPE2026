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

The exhaustive certificate consists of `verify.py` and `templates.csv`. Run `python3 verify.py` in the same directory. A successful run regenerates all 512 cases from the four binary source pairs and 128 offsets, checks every candidate root up to 36 by two independent equivalence tests, verifies the full nine-level frequency table and source-pair weights, and confirms the sharpness witness at starting index 19. It also compares independently generated length-72 factor sets and 8192 arbitrary starting indices.

The infinite-word coverage is mathematical: any index is uniquely 128 times a source index plus an offset, and the next 72 symbols lie inside the two corresponding length-128 substitution blocks. The finite computation exhausts that domain; the extra finite-prefix tests do not independently establish a universal theorem. Integer arithmetic is exact. Independence here refers only to two computational methods, not independent scientific audit. Scientific and historical-priority limitations are in `RESULT.md`.
