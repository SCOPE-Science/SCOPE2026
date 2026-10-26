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

The complete proof is in `RESULT.md`. Independent future validation is not represented as performed here.

Run `python3 verify.py` alongside `RESULT.md` with standard Python 3. No third-party packages are needed. The recorded output is in `verify_output.txt`: `VERIFY_OK 98 exact finite-state / combinatorial assertions`.

The program enumerates onto words and short future sequences under genuine entry conditioning for small alphabets and lengths, checks the conditional survival sandwich, solves finite-state rational mean equations, and checks the exact Stirling-number identity. These checks validate the finite recurrences and several boundary cases only. They do not prove the asymptotic singleton hazard, the Fourier local limit, or global historical novelty; these are supported by the argument and primary-literature comparisons separately.
