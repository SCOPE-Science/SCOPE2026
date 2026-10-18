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

The all-cardinality argument is in `RESULT.md`: each component must be a convex block in any completion; only the two endpoints of adjacent blocks can create an additional successor pair. The lower bound charges each finite-component gap without a double-ray separator to a disallowed adjacent transition; the canonical construction attains the bound. Infinitely many components are realized via a dense index order.

Run `python3 verify_successor_completion.py` in an ordinary Python 3 environment with no external dependencies. Its endpoint matrix uses exactly the four possible directed path component types. It compares an exhaustive permutation search, a dynamic-programming minimum, the formula, and the explicit arrangement for every component multiset through size nine. Expected output ends with `SUCCESSOR_COMPLETION_VERIFY_OK`.

The script's finite tests are supporting evidence only. They do not check the proof for every finite size, certify the arbitrary-cardinal case, or settle historical priority. No independent audit has been performed.
