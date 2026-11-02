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

Run `python3 checker.py` in the directory containing the extracted files. No packages beyond Python 3's standard library are used.

The test reconstructs and separately compares the source's five-state operation with the extension, evaluates **all** \(343\) ordered associativity instances, checks all \(49\) ordered coarse-projection constraints, verifies the four directed truth/error signatures, and checks that the optional involutive negation projects correctly. It also implements the six-state obstruction on the possible value of \(e\vee r\), and checks the generation closure of the seven-element algebra.

Expected output: `ALL_CHECKS_OK 343 associativity triples 49 projection pairs`.

The theorem is a **finite algebra** statement, so checking the full finite table is exhaustive; the proof of minimality is also reproduced symbolically in `RESULT.md`. There is no asymptotic claim and no external formal verification or independent audit.
