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

# Computational verification

The two Python 3 standard-library programs `sunlet_direct.py` and `sunlet_orbit.py` were executed from the packaged directory. Their full machine-readable outputs are `direct_result.json` and `orbit_result.json`. The direct program enumerates every ordered tuple, including repetitions, for rim lengths \(3\) through \(12\); the orbit program separately reduces by precisely the dihedral automorphisms for rim lengths \(3\) through \(15\). Both perform exact first-order quantifier-type recursion, not numerical approximation.

Both return the eight classes represented by \(3,4,5,6,7,8,9,10\), with every tested length from \(10\) onward sharing one type. The two implementations yield the same sequence of numbers of globally interred types for tuple lengths \(4,3,2,1,0\): \(116,122,46,14,8\).

This computation proves the finite bridge and separations conditional on the explicitly inspectable algorithms. The infinite extension is a separate mathematical argument transferring the published four-round cycle equivalence for all lengths at least \(11\); it does not follow from checked examples alone. The proof and verification do not constitute independent human audit.
