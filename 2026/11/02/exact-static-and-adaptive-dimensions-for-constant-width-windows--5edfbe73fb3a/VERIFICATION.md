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

# Reproducibility and limits

Run `python3 verify_windows.py` using Python 3 and its standard library, from the directory containing the verification program. The saved `verification_output.txt` contains the actual deterministic output of the verified invocation.

The program directly enumerates each fixed-width window family for every permitted width on paths and cycles of orders \(2\) through \(16\). Its VC check enumerates query supports of sizes at most three and their complete trace sets. Its adaptive check computes exact Littlestone dimension by restricting the *actual concept masks* at each queried vertex and recursing on all two-sided splits. Neither checking function calls the closed-form predictions.

An independent constructive-tree routine selects \(2^d\) prescribed start positions and checks every proposed midpoint query, including cyclic wrapping, recursively to all leaves. There are \(255\) parameter cases and \(1090\) leaf-witness occurrences in these explicit trees. The recursion and constructive tree are separate implementations; the theorem's unrestricted proof is in `RESULT.md`.

The checks do not establish uniqueness in literature, and do not replace the proof for arbitrary \(n,k\). No external audit or formal proof assistant certification was performed.
