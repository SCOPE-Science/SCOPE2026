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
# Verification

The supplied `check.py` needs Python 3 standard library only; execute it beside `WITNESSES.tsv` using `python3 check.py`.

It evaluates one-jumble scattered-factor membership directly from the two defining requirements: componentwise Parikh domination and a shared scattered factor after deleting at most one target-pattern position. It tests every binary word of lengths zero through twelve, a total of 8191 words, comparing its direct signature against the structurally predicted one. It independently generates and checks 66 explicitly constructed class representatives and confirms their signatures are pairwise distinct.

Expected fixed-length output class counts are `1,2,3,4,10,16,21,26,31,31,31,31,31` for lengths zero to twelve. The generated 66-row witness file stores truncated zero and one counts, the missing balanced patterns, and a representative (an empty final field means the empty word).

The exhaustive test is finite and does **not** by itself certify the infinite index or saturation. Those follow from the seven-type classification, symbol-count restrictions, and representatives in RESULT.md. There has been no independent scientific audit or external formal certification.
