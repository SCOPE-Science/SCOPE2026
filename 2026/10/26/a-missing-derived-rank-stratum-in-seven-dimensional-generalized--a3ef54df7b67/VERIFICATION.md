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

# Verification and reproducibility

The proof gives a symbolic all-field argument; the standalone executable checker is supplementary and finite. Execute `python3 verify.py` with Python 3 and no third-party packages. It directly creates the seven-dimensional multiplication tensor, extends arbitrary generator images to a derivation, verifies all 49 basis-pair derivation identities on each tested map, builds all 28 unordered basis-pair brackets, checks their ranks, and verifies the nonmock correction term.

The checker enumerates all 19,683 matrices over \(\mathbb F_3\) for the **linear-algebra lemma** only, yielding rank counts \(3,1014,18666\) for the relevant symmetric-square map. It separately checks 2,250 derivations (including arbitrary higher-degree coefficients) over \(\mathbb F_5\), \(\mathbb F_7\), and \(\mathbb F_{11}\), as well as all three displayed representative types over each field. The completed run ends in `VERIFY_OK`.

Finite test samples do not exhaust all derivations over the latter fields and are not a proof for infinite fields; characteristic-three tests establish only the separate linear rank statement. No external or independent certification was performed.
