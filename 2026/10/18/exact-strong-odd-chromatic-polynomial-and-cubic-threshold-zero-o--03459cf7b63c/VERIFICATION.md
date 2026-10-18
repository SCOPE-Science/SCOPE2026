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

# Verification record

The included `verify.py` uses only Python's standard library and independently tests the definition of strong-odd coloring on actual labeled sunlet graphs. Execute `python3 verify.py` from the directory containing this file. The captured output is included as `verification_output.txt`.

The verifier exhaustively tests 1,185,894 candidate color assignments for sunlet orders \(3\le n\le5\) and palettes \(1\le k\le4\), compares 224 direct weighted-transfer evaluations to the spectral formula for \(3\le n\le30\) and \(1\le k\le8\), enumerates three-defect center colorings in six odd orders \(3\le n\le13\), and checks parity identities through order \(64\). All checks passed and the recorded output was reproduced.

The unrestricted polynomial identity and its zero multiplicity are mathematical deductions in `RESULT.md`. The tests do not establish claims for untested graph orders or rule out prior publication. No independent audit was performed.
