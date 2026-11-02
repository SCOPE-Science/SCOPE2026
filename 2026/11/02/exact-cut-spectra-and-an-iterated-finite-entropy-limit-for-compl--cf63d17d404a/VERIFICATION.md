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

# Reproduction instructions

The analytic theorem and proof are in `RESULT.md`. The code `checker.py` requires Python 3 (tested with NumPy) and does not need external data or network access. Execute `python checker.py` from the extracted finding directory. `CHECK_OUTPUT.txt` contains the recorded output of the packaged checker. Its full-state verification uses \(\binom{w}{k}\bmod 2\) independently of the residue formula, then compares all nonzero Schmidt spectral values. Additional tests check normalization, rank, integer antiperiodic matrix identities, the limiting trigonometric spectrum and purity, and root-of-unity residue counts. All infinite-family steps rely on the exact proof, **not** the finite tests.

The code checks only selected finite sizes and numerical asymptotic approximations. It does not verify the absence of unlocated prior art, does not establish a uniform simultaneous scaling limit, and should not be treated as an independent scientific audit.
