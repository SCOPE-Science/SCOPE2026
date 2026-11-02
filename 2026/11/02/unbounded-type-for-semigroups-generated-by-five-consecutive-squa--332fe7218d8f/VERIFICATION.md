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

The theorem is established by the symbolic integer proof in `RESULT.md`, including exact generator-translate identities, an upper bound on the number of putative generators, and the parity-and-moment contradiction.

Execute `python3 verify.py` with Python 3. The script builds complete shortest-residue Apéry tables for \(n=12k\) at \(k=4,5,6,7,8,9,10\), checks all \(98\) explicit pseudo-Frobenius witnesses, and recomputes full types \(47,57,68,78,89,99,110\). It additionally checks the identities and strict inequality conditions for \(k=11,20,50,100,1000\). No nonstandard package is required. A finite check is evidence about those parameters only, not a substitute for the all-parameter proof. Historical equivalence and independent mathematical correctness assessment remain unperformed externally.
