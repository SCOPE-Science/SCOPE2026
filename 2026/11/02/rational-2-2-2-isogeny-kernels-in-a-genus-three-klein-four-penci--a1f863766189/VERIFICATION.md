---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For every odd q and smooth ordered coefficients (a,b), Frobenius commutes with the regular Klein-four action on each reciprocal quartic, so a quartic contributes identity or 2^2 involution, never a 4-cycle; splitting count is S=(q-1-gcd(4,q-1))/4 and nonsplit U=q-2-S. The hyperelliptic even-subset/complement 6-dimensional symplectic model gives 135 geometric maximal isotropic 3-spaces. The 105 perfect-matching subgroups are distinct; the other 30 are the S8/AGL(3,2) affine spaces. Their fixed-point counts follow from invariant matchings (105,9,25) and affine centralizers (30,6,14), hence 135,15,39. Group descent is Frobenius invariance, not an assumption of individually rational generators; rational 2-torsion sizes 64,16,16 are independently reproduced. The claimed ordered-pair frequencies include q=3 empty case and every kernel splits over q². Verified actual RESULT.md and verify_isotropic.py at their frozen blob hashes and independently enumerated 64 even-subset classes/135 isotropic subspaces and three Frobenius actions. Finite-field script examples do not prove all q; the analytic group action does.

## originality

PASS

The 135 geometric kernels and the genus-three family with Klein-four automorphisms are established prior knowledge. The assessed new object is the ordered-coefficient Frobenius-stable Lagrangian census, the 15 versus 39 distinction despite equal rational 2-torsion, and the matching/affine splits. Target-level isogeny classification is not claimed. Primary geometric paper was inspected; no inspected stronger theorem yields these arithmetic strata.

## value

PASS

An all-odd-field arithmetic descent classification of 135 natural maximal-isotropic kernels, with exact coefficient frequencies and the 15/39 discrepancy at identical rational 2-torsion rank, supplies a structurally motivated invariant useful in genus-three rational (2,2,2)-isogeny enumeration. The distinction is not a textbook count of all 135 geometric kernels and does not depend on an unproved application.

The dated certificate retains the supplied scientific assessment, sources and limitations.
