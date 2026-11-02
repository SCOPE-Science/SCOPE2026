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

The stand-alone Python 3 checker `check_affine_heisenberg.py` uses no third-party dependencies. Run `python3 check_affine_heisenberg.py`. Its exact output is included in `verification_output.txt`. Over \(\mathbb F_2\) and \(\mathbb F_3\), it enumerates linear idempotents, tests the weight-minus-one Lie identity, checks all normalizing translation vectors, and directly evaluates the **full affine Rota–Baxter identity for each resulting map and every ordered input pair**. Over \(\mathbb F_2\) it also independently enumerates all affine maps, comparing the exact sets of solutions.

It constructs every affine automorphism of the canonical Heisenberg Lie affgebra in these two fields, conjugates each solution, and checks complete orbit partitions against the formula. The observed total counts are 57 and 244; corresponding orbit-size multisets are respectively \(\{1,2,6,12,12,24\}\) and \(\{1,3,24,36,72,108\}\). The last output line is `VERIFY_OK`.

The checker was executed from the file embedded with this result; its bytes and output hashes are validated when the enclosing package is reopened. These computations are finite and do not certify arbitrary fields. The proof in `RESULT.md` establishes the universal statement. No independent mathematical audit was performed.
