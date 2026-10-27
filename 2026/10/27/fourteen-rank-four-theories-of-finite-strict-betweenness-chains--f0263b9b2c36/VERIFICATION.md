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

# Reproducible verification

Run `python3 verify_bet4.py` with Python 3. The program uses only the standard library; it enumerates complete rank-\(r\) atomic extension types without numeric approximations or randomization. Compare stdout to `verify_bet4.out`.

The main check establishes fourteen distinct rank-four types on domain sizes one through fourteen, with the types at fourteen and fifteen identical. The separate pointed-character assertion checks the entire set of rank-three types realized after one pebble at sizes fourteen and fifteen. Consistency checks for lower ranks also run.

The program itself tests only finite domain sizes through fifteen. The theorem for arbitrary larger domains is proven independently through the standard pure-linear-order interval splitting and the quantifier-free strict-betweenness reduct; the code does not claim to enumerate infinitely many structures.
