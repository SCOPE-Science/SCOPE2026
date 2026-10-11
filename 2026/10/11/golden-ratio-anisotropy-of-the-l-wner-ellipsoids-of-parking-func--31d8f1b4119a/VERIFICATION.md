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
# Verification of the parking-function Löwner ellipsoid limit

The proof establishes an asymptotic statement for all integer dimensions \(n\ge2\) using exact orbit covariance formulas, a determinant duality argument and the polynomial identity in \(\mathbb Q(\sqrt5)[s]\). No finite experiment proves the infinite limit. The uniform perturbation argument is written in Step 4 of `RESULT.md`.

Reproduce the included checks by running `python3 verify.py` in the unpacked artifact directory, using only a standard Python 3 installation. This checks coefficient-by-coefficient equality in the quartic identity, permutation-orbit means and covariance for 27 cases in dimensions 2 through 7, exact finite Löwner contact certificates in dimensions 2, 3 and 4, and six two-orbit determinant lower benchmarks up to dimension 1280. The larger benchmarks are *dual designs* rather than purported exact optimal ellipsoids. No external solver, expert review, or independent audit was invoked. The proof's limiting upper bound and all contact-layer conclusions remain analytic, not computationally certified by enumeration.

The geometric scope is ordinary Euclidean coordinates, not arbitrary affine images. Finite-dimensional exact coefficients and exact finite-dimensional counts of contacting layers remain outside the claim.
