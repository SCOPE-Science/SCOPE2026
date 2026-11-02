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

# Verification of the finite group-with-zero classification

Execute `python3 verify.py` with a standard Python 3 interpreter. The program is self-contained and uses exact integer computations only. It checks all predicted relations for closure, verifies symmetric/transitive congruence counts, and independently exhausts **every reflexive relation** for the cyclic groups of orders \(1\), \(2\), and \(3\). The larger cyclic examples and the nonabelian \(S_3\) example check all constructed relations, but do not exhaust the ambient relation space.

Recorded output is embedded in `verification_output.txt`. The final line is `VERIFY_OK`. The theorem for arbitrary finite groups is established by the complete symbolic normal-form argument; exhaustive small computations cannot substitute for its proof.
