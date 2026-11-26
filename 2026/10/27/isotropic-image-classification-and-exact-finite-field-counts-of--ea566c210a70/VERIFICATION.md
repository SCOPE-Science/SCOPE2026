---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Write N(v+tz)=Av+tu+(ell(v)+ct)z. Torsion on (v,z) forces omega(v,u)u=0 for every v, so u=0 by nondegeneracy. The residual torsion on V is exactly omega((A-cI)v,(A-cI)w)z. This is the isotropy of the image of B=A-cI, not the image of A. It needs no division or characteristic restriction. The number of rank-r maps B is the count of isotropic r-frames divided by the number of bases of a fixed r-space, times the full-row-rank count of surjections onto this space. Appending ell to B increases rank by one precisely outside its r-dimensional row space; the free c multiplies both counts by q. This gives both joint strata, also at r=0, and their sum. The characteristic polynomial factors as (T-c) times the shifted characteristic polynomial of B, for which the zero multiplicity is at least 2n-r. In a separate bounded computation the direct torsion test exhausted 512 and 19683 operators in dimension three over F2 and F3, with exact joint histograms (2,6,36,36) and (3,24,288,576) in order (0,0),(0,1),(1,1),(1,2). Exhaustion of all binary 4-by-4 B, followed by all ell,c for the isotropic B, gave (2,30,900,6300,25200,75600) in lexicographic order of feasible strata, total 108032. Both methods agree with the formulas.

## originality

PASS

The distinct supported claim is the classification of all ordinary binary Heisenberg Nijenhuis endomorphisms over arbitrary fields and the resulting joint finite-field census. The closest inspected exact classification has a fixed twisting map and commutation constraint; the regular-semisimple obstruction and symplectic frame counts are prior ingredients, not coverage of this result.

## value

PASS

This is a complete structural parametrization on the basic Heisenberg family, uniform in characteristic, not an isolated small count. It links an intrinsic rank on the quotient to the centered rank of the full map and gives every stratum, useful for comparison with classifications under additional constraints.

The dated certificate retains the supplied scientific assessment, sources and limitations.
