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

The mathematical argument is given in `RESULT.md`. The source's Theorem 5.8 was inspected in its publicly available complete HTML rendition and supplies the precise normalization and ramification data. The new argument establishes the base-coordinate rigidity, classifies the residual Witt-unit ambiguity and proves the deck normalizer equality.

Run `python3 CHECK.py` in the same directory to reproduce exact characteristic-two Witt identities, the parameter-shift coboundary, and the \(\mathbb F_{16}\) parameter-fibre check. These tests do not decide geometric uniqueness on their own; that is the role of the rational-function pole-order proof. No external independent audit has been performed.
