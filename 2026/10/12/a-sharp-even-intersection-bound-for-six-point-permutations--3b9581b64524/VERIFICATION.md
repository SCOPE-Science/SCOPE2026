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

# Reproduction and logical scope

Execute `python3 verify.py` next to the supplied files. The deterministic standard-library program calculates the two conjugacy-class sizes by enumerating \(S_6\), evaluates all irreducible characters in the two classes by two separate exact constructions (Murnaghan–Nakayama and Jacobi–Trudi), checks the squared-dimension sum, verifies the weighted spectrum has least eigenvalue \(-48\) and valency \(672\), and tests the \(48\)-element subgroup for all pairwise even agreement relations. The expected output is included in `verify_output.txt` and terminates with `VERIFY_OK`.

The mathematical theorem uses the full character table and the weighted ratio inequality. The finite verification is an exact check of all character rows and the exhibited construction; it is not a numerical approximation or an inference from a failed optimization search. The computation does not classify all optimizers or establish a result for larger degrees. Independent external auditing remains unperformed.
