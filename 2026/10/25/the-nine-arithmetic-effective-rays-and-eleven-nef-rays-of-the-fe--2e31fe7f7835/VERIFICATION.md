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

# Verification of the arithmetic cone theorem

Run `python3 verify_fermat_cubic_F2.py` using Python 3 standard library. The file exactly constructs \(\mathbb F_4\), the 27 geometric lines of the characteristic-two Fermat cubic, all Frobenius orbits, the 27-by-27 incidence intersection form, the saturated rank-four Picard basis, and the nine effective ray generators. It computes all 84 potential supporting triple normals of their four-dimensional dual cone, verifies sign nonnegativity and each dual extremal support, and prints eleven nef ray covectors. The finite calculation exhausts the set of twenty-seven exceptional curves by the geometric 27-lines theorem; it does not claim a finite experiment proves the general theorem without that input.

Expected output begins with `VERIFY_OK: 27 lines=3+12*2` and includes `VERIFY_CONE_OK: 9 invariant effective extremal rays; 11 nef extremal rays`.

Scientific limits: the rational Picard rank uses the standard cubic-surface Frobenius point-count formula, and effective-ray completeness uses the standard cone of curves of a degree-three del Pezzo surface. Standard literature supports those geometric inputs; the enumerator supplies exact instance-specific computations. No independent audit has been performed.
