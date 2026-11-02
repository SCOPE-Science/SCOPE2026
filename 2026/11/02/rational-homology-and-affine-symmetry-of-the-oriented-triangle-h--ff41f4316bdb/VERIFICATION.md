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

The standalone `verify.py` enumerates cells from the quadratic-residue arc relation, not from a stored face table. The generated product cell vector is \((855,5130,9234,4959,684)\), summing to \(20862\). Columnwise and separately rowwise exact binary elimination return ranks \((854,4276,4275,684)\); each signed product-cell boundary is checked to have zero second boundary. Euler characteristic and the mod-two universal-coefficient rank bound give rational Betti vector \((1,0,683,0,0)\).

Every one of the \(171\) affine actions on all product cells is evaluated using signed orientation permutations. The degree-two character takes values \(683\) once, \(8\) on \(38\) elements, and \(-1\) on \(132\) elements; its mean is five. The check independently evaluates the proposed summand character on all elements. The expected execution marker is `PALEY19_HOM_C3_RATIONAL_AFFINE_CHARACTER_VERIFY_OK`.

These checks prove no integral homotopy classification, and do not rule out odd-primary integral torsion or undiscovered equivalent literature. The classification is one of rational homology representations, not homotopy representations.
