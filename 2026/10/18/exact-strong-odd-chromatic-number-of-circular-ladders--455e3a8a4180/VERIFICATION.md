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

# Reproducible scientific checks

Execute `python3 verify.py` with Python 3.9+ standard library from the extracted package directory. The program constructs prism graphs independently from their adjacency lists and checks properness and odd neighbourhood multiplicities. It enumerates every odd independent subset for orders three through nine, checks all palette sizes two through five by an independent exact column-state algorithm for orders three through twelve, tests the infinite-block local-window stabilization and verifies direct constructions through 499 rungs. The recorded output is `verify_output.txt`. The proof of the infinite claim relies on the algebraic propagation argument and the 13-state local inspection stated in `RESULT.md`; the finite runs are supporting checks.

No independent audit has been performed. The October 2026 focal complexity paper was not fully accessible; priority assessment is therefore qualified as documented in `REVIEW.md` and `RESULT.md`.
