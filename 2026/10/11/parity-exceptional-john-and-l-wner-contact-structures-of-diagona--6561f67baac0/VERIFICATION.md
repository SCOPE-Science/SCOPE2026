---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The convex body has permutation symmetry, so uniqueness restricts both optimal ellipsoids to center t*1 and two shape eigenvalues u,v. The one-sided coordinate and sum hyperplanes form a containing simplex whose John ellipsoid fits all missing lower cube facets, proving the exact John formula. Cube vertices with sum >=0 and, only for odd d, zero-coordinate cut-edge midpoints exhaust the vertices. Their squared ellipsoid norms are F_d(s,q)=(s-dt)^2/(du)+(q-s^2/d)/v; with 0<u<v strict convexity in s proves no missing cube-orbit contacts. Exact positive orbit weights for the pole, low-sum cube layer, and exceptional edge-midpoint layer have the prescribed mean and covariance Q/d. Independent rational calculations tested all 99 dimensions 2..100 and verified every equality, weight positivity and orbit inequality; the displayed symbolic formulas and Löwner moment criterion establish all dimensions. For odd d>=7, midpoint squared norm 4/(d-1)^2+(d-1)/d<1; d=3,5 are boundary exceptions.

## originality

PASS

The JOHN component is precisely a known specialization of the published capped-hypercube three-phase formula, under y=(1-x)/2 and tau=d/2. That prior theorem yields t=1/(d+1) and the reported u,v after scaling. Therefore John is NOT newly claimed as independent priority. The substantive distinct finding is the complete LÖWNER ellipsoid, its positive exact moment certificates and sharp exceptional cut-edge midpoint contacts only in dimensions 3 and 5; the capped-hypercube theorem determines no containing ellipsoid. Published central-section papers study volumes of slices, not ellipsoids of the one-sided half-body; no inspected stronger theorem covers the Löwner component. Best-of-knowledge PASS for the original full result is based on this genuinely new principal component and transparent prior overlap.

## value

PASS

Exact minimum-volume enclosing ellipsoid of a natural diagonal halfcube is a motivated geometric extremal invariant; the sharp exceptional dimensions 3 and 5 classify an otherwise hidden vertex-orbit transition. Its rational global covariance certificates and all-dimensional contact counts are independently useful beyond the already known John special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
