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

The proof uses the actual finite-dimensional symplectic geometry and a Mayer–Vietoris exact sequence induced by the published surface-gluing diagram. The vertex, decorated-plane and incidence counts are evaluated symbolically for every odd prime in RESULT.md. The cohomology trace formulas follow from the graph chain exact sequence and pointwise identity of the transvection on fixed modular-curve components. No claim that a numerical experiment proves an infinite theorem is made.

The self-contained `verify.py` program enumerates signed nonzero vectors and wedge-decorated isotropic planes in \(\mathbb F_p^4\), tests the transvection action, computes fixed incidence counts and checks dimension, trace and rational cyclic representation identities at \(p=3,5,7\). Running `python3 verify.py` on the packaged file terminates with `VERIFY_OK`.

There is no standalone proof of a full \(\mathrm{Sp}_4(\mathbb F_p)\)-character. Potential implicit coverage by a broad group-character theorem remains a scientific literature risk. No independent audit has been performed.
