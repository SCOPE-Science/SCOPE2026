---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Independent support of an iDRDF on R_mn is a partial row/column matching with no 1-labels (a 1 would require a positive neighbor contrary to independence). Every zero requires a positive neighbor, forcing matching to saturate all m rows. When square, each zero sees one supported neighbor in each direction and exactly 2s suffice, giving weight 2m and m! permutation optima. When m<n, an unoccupied column gives one-positive-neighbor zero per row, forcing all supported 3s and weight 3m with n!/(n−m)! injections. The argument covers m,n≥2. Independently checked all four-label assignments on R_2,2, R_2,3, R_2,4 and R_3,3 (the largest 4^9 cases), with exact minima and optimizer counts; no extrapolation from these finite checks.

## originality

PASS

The same independent double Roman parameter has general sharp bounds and criteria for equality, which partly imply the square rook graph scalar optimum. The unequal rectangular phase and complete minimum-function classification are not implied by that scalar-bound theorem without additional matching geometry. Direct comparison of L(K_mn), K_m □ K_n, and rook graph aliases did not identify full prior coverage.

## value

PASS

Rectangular rook graphs are standard Cartesian products/line graphs. The sharp square-versus-nonsquare transition is forced by board geometry and gives complete algebraic families of every optimal labeling, bijectively permutations or injections. This is an exact structured classification beyond an isolated score; the pre-known square bound alone does not determine the strict rectangular phase or all optimizers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
