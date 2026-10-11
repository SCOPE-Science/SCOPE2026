---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The objective is separately convex in x and y, so its maximum over the compact octagonal ball occurs at an extreme-point pair; these vertices lie on the sphere, so this equals the required sphere supremum. Dihedral symmetry reduces to four nontrivial separations. The exact Q(sqrt(2)) verifier checks the support-line regimes and polynomial factor comparisons. An independent direct maximization over all 64 ordered vertex pairs on a 101-point parameter grid agreed with the two claimed branch formulas to numerical roundoff, including the transition m*=(4-sqrt(2))/7 and midpoint value 4-2sqrt(2). The continuum upper bound itself is the exact finite quadratic comparison, not the grid check.

## originality

PASS

Originality passes. The 2021 defining paper was read completely: it defines exactly the target unit-sphere parameterized constant and proves general inequalities, but does not compute the regular octagon. The 2024 regular-octagon paper was also read in full; it computes L_YJ and L'_YJ, whose second norm term uses swapped parameter coefficients and is a different functional except at the symmetric midpoint. Its exact regular-octagon formula therefore does not imply the audited two-branch C'_NJ(lambda,X) profile.

## value

PASS

The regular octagon is a canonical non-Hilbert benchmark in Banach-space geometry, and the defining paper introduced the parameterized invariant specifically to quantify departures from Hilbert geometry. The exact all-parameter profile exhibits a genuine maximizing-pair phase transition and recovers the classical midpoint constant, so it is a motivated exact invariant rather than an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
