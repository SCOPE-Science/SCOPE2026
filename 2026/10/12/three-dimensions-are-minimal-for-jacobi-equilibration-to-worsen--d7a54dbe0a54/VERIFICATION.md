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

For A=[[a,c],[c,b]] SPD set rho=|c|/sqrt(ab), q=sqrt((a−b)^2+4c²)/(a+b). Direct exact algebra gives q²−rho²=(a−b)²(ab−c²)/(ab(a+b)²)≥0, and the increasing function (1+t)/(1−t) proves κ(J(A))≤κ(A), with equality precisely at a=b. In n=3 the rank-one Aκ has eigenvalues (1,1,κ); use interchange symmetry of coordinates 2 and 3 to diagonalize J in antisymmetric and two-dimensional symmetric sectors. The least eigenvalue is 9/(4κ+5), and ratio λmax/λmin equals [2κ+1+2(κ−1)sqrt((κ+2)/(κ+8))]/3. Its excess above κ is (κ−1)(2sqrt((κ+2)/(κ+8))−1)/3>0 for all κ>1; large-κ ratio→4/3. Independently checked symbolic rank-one identities with Sympy and at κ=10 exact equilibrated eigenvalues (1/5,(7±2√6)/5), giving κ(J)=7+2√6>10. The original proof, not finite evaluations, establishes all κ.

## originality

PASS

PASS with explicit scope. Full van der Sluis 1969 near-optimality theorem for symmetrically scaled SPD equal-diagonal matrices bounds the condition number relative to the *optimally* scaled matrix, not to unscaled A, and thus permits Jacobi to worsen it. Braatz–Morari optimize over diagonal scaling; this does not describe the sharp low-dimensional safe/unsafe boundary for this fixed choice. Targeted searches for minimal dimension and exact fixed-κ family found no implication-equivalent classification; possibility of an older elementary counterexample remains a risk.

## value

PASS

A useful boundary for widely used diagonal preconditioning: universal harmlessness through dimension two versus a quantified failure already in three dimensions, for each given original condition number. The explicit rank-one family and limiting 4/3 factor clarify a practical numerical misconception without claiming globally worst possible inflation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
