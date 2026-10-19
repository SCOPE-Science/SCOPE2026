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

# Reproduction
Run `python3 verify.py` from this directory. The script requires only the standard Python library and constructs its own finite-field arithmetic tables. It directly enumerates the absolute-nilpotent equations for 38 field/length combinations involving fields with 2, 3, 4, 5, 7 and 9 elements. Its output terminates with `VERIFY_OK 38 exhaustive finite-field and zeta checks`.

The script separately checks the proposed zeta factors by formal-logarithm coefficient extraction through extension degree six. It includes the split/non-split comparison of \(\mathbb F_3\) and \(\mathbb F_9\) at cycle length four.

# Proof versus computation
The proof in RESULT.md, not the program, establishes the assertions for every finite field and every cycle length \(n\ge3\). The program does not test every field or length, does not establish geometric irreducibility, and does not verify nonreduced scheme structures. Those geometric assertions are proved set-theoretically using the explicit recurrence and root parametrizations. The intrinsic scheme structure is outside the claim.
