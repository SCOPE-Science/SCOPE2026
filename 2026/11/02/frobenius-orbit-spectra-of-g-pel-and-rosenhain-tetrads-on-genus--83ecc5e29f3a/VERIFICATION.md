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

The six branch points identify J[2] equivariantly with even subsets modulo complement: an even subset A maps to the class of its branch-point sum minus |A|/2 copies of the hyperelliptic pencil. The relations 2W_i∼H and ΣW_i∼3H give the quotient and addition. Nonempty size-two representatives map to nonzero classes since distinct branch points are not linearly equivalent; hence the sixteen classes are distinct. The standard Weil form is intersection parity. In the four-dimensional symplectic space, for any nonzero first basis vector there are six independent perpendicular second vectors and eight nonperpendicular ones; dividing either basis count by six gives fifteen and twenty directions, with four affine translates per direction. The classical tetrad identification is compatible with the node labels, so the exact finite census tests the bound arithmetic claim. Independent replay: python3 /workspace/branches/f93ff698-598e-4607-8d2c-72e7d10f4a89/reconstruct_tetrads.py. Its execution built 35 directions and 60/80 planes, computed the actions of all 720 permutations, and verified all 22 spectra, fixed counts via stability of cosets, and both lcms. The frozen script was not executed. The lcm assertion also follows from faithfulness: the intersection of all affine planes of a given species through a node is that node, since for any nonzero vector some plane of that species excludes it. Fixing every plane therefore fixes all nodes and hence every two-subset of the six labels. Each length-d orbit contributes d points precisely over extensions of degree divisible by d and contributes (1−T^d)⁻¹ to zeta. Realizability uses distinct irreducibles; repeated degrees can only be 1, 2 or 3, with at most six, three or two required respectively, available at q≥7 by the standard irreducible counts. No assertion is made for unrealizable types at smaller q or for characteristic two.

## originality

PASS

Supported credit is limited to the complete arithmetic spectra of the two affine tetrad sets. Neither the 60/80 geometric classification nor standard consequences of a permutation spectrum are credited as new. The strongest exact matching primary record is in a later-dated directory and its matching content supplies no evidence of earlier priority. The inspected earlier texts establish the geometric models, not the full permutation enumeration.

## value

PASS

Affine tetrads are natural classical configurations of four nodes; their full arithmetic spectra are reusable exact descent data, not just a new count of the 60 and 80 geometric objects. For instance, the spectra separate splitting types with the same underlying node spectra in the transposition-product cases, and distinguish which species admits rational tetrads or needs an extension. The classification covers every allowed branch type and yields field-of-definition data for each species that geometric counts or linear direction spectra do not give without additional calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
