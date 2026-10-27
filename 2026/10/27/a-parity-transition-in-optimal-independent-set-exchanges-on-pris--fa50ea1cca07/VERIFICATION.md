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

The theorem is proved symbolically in `RESULT.md`, including its exact scope \(n\geq3\), all independent-set counts, and the vacancy-shift paths that establish connectivity. The two Python scripts construct the configurations in different representations, enumerate them exhaustively for each \(3\leq n\leq10\), compare actual selected vertices for every exchange, and compute connected components. Both scripts were run from their actual packaged paths, with outputs saved as `verify_bitmask.out` and `verify_ternary.out`. Running `python verify_bitmask.py` and `python verify_ternary.py` from this directory reproduces these files.

Finite tests cannot prove the infinite statement; the general proof is the evidence for the quantifier. No lower-level classification, independent external audit, or priority certification is asserted.
