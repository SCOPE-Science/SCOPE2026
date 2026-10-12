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

The package includes the standalone file `verify.py`. Run `python verify.py` with Python 3 and no third-party packages. It must print `VERIFY_OK` and the eight inspected field/twist cases. It checks finite-field arithmetic, complete commutator-fiber tables, centralizer-size distributions, exact proper centralizer subgroups, noncentral clique component counts, and a constructive additive intertwiner for two twists of \(\mathbb F_{32}\). All arithmetic is exact (bit-polynomial finite fields and integers).

Computational coverage: characteristic \(2\) with \(q=4,8,16,32\), eight nontrivial field twists. The verifier does not enumerate all primes, field sizes or twists, and its checks do not replace the general proof. The arbitrary-characteristic statement uses the symbolic commutator formula and elementary linear algebra over finite fields. The older literature is used for context and distinctions; no independent audit or external certification was performed.
