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

# Reproducibility

Execute `python3 verify_diagonal.py` with Python 3.9 or later. Only standard-library modules are required. The program constructs all \(30\) fixed-diagonal cores and all \(512\) cosets of each doubled core. It tests every candidate extension's minimum weight and full codeword weight distribution; compares an independent paired-difference classification to the exhaustive coset outcome; verifies every puncturing and full-code covering step; and checks that the \(2160\) classified codes are pairwise distinct. A deterministic sorted-code-list SHA-256 permits a bit-for-bit comparison.

Expected terminal line: `DIAGONAL_D5_VERIFY_OK`.

The separate impossibility of binary \([12,5,5]\) codes is established symbolically in `RESULT.md` by Griesmer and MacWilliams; the program does not pretend an enumeration of all possible binary length-twelve subspaces is a proof of nonexistence. All science claims are for explicitly finite dimensions. No external verification has been performed.
