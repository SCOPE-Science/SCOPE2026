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
# Reproducibility and verification

Execute `python3 verification.py` using Python 3.9 or newer from the same directory. The program deterministically constructs the complete sets of occurring factors by covering a factor of length \(n\) with two sufficiently long substitution-aligned blocks; all four underlying adjacent-letter pairs are included. The final output is `VERIFY_OK` when all assertions pass.

Actual checks: at dyadic lengths \(N=4,8,16,32,64,128,256,512\), the program checks every rotation class-size count, identifies the all-rotation class, checks the three explicit doubleton representatives, tests all circular one-step extendible factors, and verifies the opposite-endpoint factor count at length \(N+1\). For lengths at most 17, it crosschecks the complete-factor cover against a direct prefix and the efficient minimal rotation algorithm against exhaustive rotations. It also independently crosschecks complete sets using a long direct prefix at dyadic lengths through 128.

These are finite computations; they do not establish the claim for infinitely many lengths. The proof in RESULT.md supplies the exact parity splitting, the unique circular-pair defect, the circular-extension recurrence, the endpoint count, and induction. No independent mathematical audit or external validation is claimed.
