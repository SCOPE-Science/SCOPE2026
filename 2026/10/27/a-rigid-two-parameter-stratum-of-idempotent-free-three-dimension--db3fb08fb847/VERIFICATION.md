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

# Verification details

The general proof is contained in `RESULT.md`. Execute `python3 verify.py` using Python 3 standard library; the program prints `VERIFY_OK` and its five exact rational centered-moduli pairs. It checks the relations \(U^2=0\), \(UV=U/2\), \(V^2=U+V\), \(\sum_i e_i^2=0\), pairwise nonproportionality, and translation-invariance of the two symmetric invariants on the specified rational examples.

The decisive infinite steps—the Lagrange identities, simultaneous-diagonalization rigidity, exhaustion from arbitrary natural bases, computation of automorphisms and cubic-root classification—are justified directly in the proof. Neither sample checking nor full enumeration over a finite subset of parameters constitutes proof over \(\mathbb C\). No independent audit or external formal certification has been performed.
