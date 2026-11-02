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

# Verification and scope

Run `python3 verify_fermat_plane_orbits.py` with the Python standard library. The saved script was executed and printed `VERIFY_OK` after checking every reduced-row-echelon plane, the complete orbit partition, every geometric-plane weight distribution, Frobenius fixedness, and all 4 representative-versus-orbit intersection count vectors.

The exhaustive finite search covers all \(376805\) candidate three-spaces over \(\mathbb F_4\). The independent geometric completeness argument in RESULT.md uses maximal Hermitian isotropy and the degree-\(3\) Fermat equation to show all *geometric* planes descend to \(\mathbb F_4\). The normal-bundle computation separately shows infinitesimal reducedness; it is not inferred from a finite point count.

Full unitary-group incidence is classical and is not a novelty claim. Originality of the three restricted two-cell matrices has only been reviewed against the identified sources and accessible prior claims; it is not independently certified.
