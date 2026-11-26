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

For each i and each commutative k-algebra R, raising a proposed generator image to q_i=p^{e_i} gives only q_i-th powers of coefficients, by Frobenius. Its surviving monomials x^(q_i α) are distinct; their indices have α_j=0 for e_j≤e_i and 0≤α_j<p^(e_j−e_i) otherwise. Thus there are exactly c_i independent relations a^(q_i)=0, with no reduced-base assumption. Their universal coefficient ideal is nilpotent. Modulo this ideal the image of the origin is the origin and the linear coefficient matrix is block triangular by height, with unrestricted equal-height diagonal blocks. Over every residue field the finite local algebra criterion is invertibility on m/m², by the finite maximal-ideal filtration. Consequently the universal endomorphism determinant is invertible exactly on the open where the diagonal blocks are invertible: the conditions agree at all primes, and nilpotent terms cannot change that open. The remaining polynomial coordinates are independent and give precisely the stated affine dimension. In characteristic p all defining power equations have zero derivative, equivalently each derivation can assign arbitrary values to the generators, so the tangent dimension is rN and the excess is Σ_i c_i. This is a statement about schemes, not a splitting of the group law. In the mixed (2,4) example, the constrained coordinates are the constant and y coefficients for x and the constant for y, exhibiting all three over a nonreduced base by x↦x+ε+δy, y↦y+γ with ε²=δ²=γ⁴=0. Over F_2 they vanish, and two further free coefficients must be 1, leaving 11 binary choices, hence 2048 automorphisms. The frozen verifier was inspected, not run.

## originality

PASS

Credit the full mixed-height coordinate scheme over arbitrary bases, particularly the separate nilpotent factors for every surviving Frobenius coefficient and the exact count depending on all higher heights. The inspected common-height, one-variable, two-variable and Lie-algebra results do not establish that arbitrary-height package. The strongest further plausible equivalence is through the geometric splitting of modular purely inseparable field extensions; the relevant Chase theorem text was not accessible, so this is a genuine remaining prior-coverage risk, not a negative comparison.

## value

PASS

Over a field, all constrained coordinates vanish and field-valued automorphisms miss the entire infinitesimal structure being measured. The scheme product quantitatively isolates how taller variables create additional nilpotent directions for shorter generators, and gives the exact height-sensitive difference between dimension and tangent dimension for a natural family. This is more informative than a nonsmoothness assertion or a point count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
