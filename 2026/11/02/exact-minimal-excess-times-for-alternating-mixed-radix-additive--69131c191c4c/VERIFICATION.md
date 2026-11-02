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

Execute `python3 verify.py` with standard Python 3. It independently enumerates all lower-digit combinations of each finite radix tuple, verifies unique representation throughout the full finite interval, and compares all equality points with the claimed formula.

Nine tuples were checked: constant radices of lengths \(15,8,6,6\) for bases \(2,3,4,5\), respectively, and mixed tuples \((2,3,4,5,3,2)\), \((3,2,5,2)\), \((4,7,2,3)\), \((7,2,2,4)\), and \((2,3,2,5,3,2,2)\). The complete period sizes are \(32768,6561,4096,15625,720,60,168,112,720\); equality counts respectively \(16,17,19,25,14,9,13,12,13\). Each test printed `PASS` and the combined invocation printed `VERIFY_OK cases 9 scope finite_only`.

The mathematical proof of the unrestricted theorem depends on uniqueness of the digit decomposition and an explicit additional-pair argument, not on the finite enumeration. The test does not establish bibliographic novelty or independent certification.
