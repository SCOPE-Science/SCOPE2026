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

The scalar denominator is positive on the Laplacian spectrum, so the inverse is positive definite (in particular its diagonal is positive), and fixes the all-ones vector. Thus entrywise nonnegativity, a discrete min/max principle and sup-norm contractivity are equivalent. Multiplication of scalar series gives r(z)=1−z+z²/2−z⁴/4+O(z⁵). At distance four the first nonzero Laplacian power entry occurs at power four and is +1, from the unique geodesic. The two-vertex case follows from r(2h)<1; projection onto constant, leaf-difference and hub-versus-leaves subspaces gives the star formulas, with strict convexity of r ensuring positive leaf–leaf entries. Every diameter-three tree is a double star. The four-cell Laplacian is symmetric in the class-size weighted inner product and is a restriction of the original positive semidefinite operator. Its Padé denominator has positive determinant. Cross-cell inverse entries per vertex are quotient entries divided by destination cell size; same-leaf off-diagonals are the difference between the quotient diagonal entry and r(h), divided by class size, by the eigenvalue-one leaf-difference action. I reconstructed all eight numerator polynomials from alternating permutation sums for determinants and cofactors, verified exact leaf-count divisibility, and compared every rational monomial coefficient with the frozen certificate. All coefficients are strictly positive, with counts 18,22,15,15,22,10,28,28 and minimum h-degrees 1,1,2,2,1,4,2,2. This verifies the infinite positive direction, not just samples.

## originality

PASS

The distance-four obstruction is exactly covered on trees by the earlier all-graph obstruction and is explicitly not claimed as new. The independently assessed distinct contribution is strict all-step positivity of all double stars, including arbitrarily unequal and unbounded leaf counts, and hence the exact all-tree diameter classification. No inspected covering statement supplies this positive direction.

## value

PASS

The all-step maximum principle is a natural structural requirement for a graph heat update. The result supplies a sharp topology test on the full class of trees: the known local obstruction becomes necessary and sufficient because every double star, even highly unbalanced, passes uniformly. This is useful beyond the already-known path obstruction or any finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
