---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The positive-degree output branches multiply independently, and no further truncation equations arise. In a branch, multiplication modulo t^N is zero exactly when the two orders sum to at least N. If the minimum order a is below N/2 it is unique and imposes order ≥N−a elsewhere. Otherwise the central component suffices for even N; for odd N the all-high tuple lies in each space associated to a=(N−1)/2. The lower-bound vectors of the listed spaces are incomparable. The reduction/product step is valid here even over imperfect k: modulo any prime containing the coefficient equations, apply the valuation test in the fraction field of the domain quotient, so that the prime contains one of the listed coordinate primes in each branch. The radical is the intersection of the resulting coordinate primes; flat field extension preserves that finite intersection. This justifies geometric components without invoking a general rule about products of reduced schemes. Their dimensions follow by counting free coordinates. For even N the gap between the central space and a=1 when r,d≥3 is (r−2)(N/2−1); for odd N compare a=1 and a=2. Invertible tangent matrices are monomial, selecting exactly the permutation products of a=1 spaces. For counting, the all-high stratum contributes q^(r floor(N/2)), and fixing the unique low index and exact valuation a contributes (q−1)q^(d+(r−2)a). These counts are disjoint; independence gives the r-th power. All field-valued algebra maps preserve augmentation because each generator image is nilpotent.

## originality

PASS

Credit the complete valuation-component description and endomorphism count for arbitrary d, not the same-family automorphism theorem. The inspected prior work does not cover the noninvertible endomorphism geometry and count. There is an exact overlap on small truncation lengths in a later indexed record, not evidence of earlier coverage.

## value

PASS

End rather than Aut records which degenerations and noninvertible maps occur in this natural family of finite-dimensional singular algebras. A complete list of its geometric components, the exact equidimensionality boundary, and the fact that automorphism-bearing components can be smaller than components without automorphisms are useful geometric information distinct from the group. The uniform point count gives a comparable exact invariant over all finite fields.

The dated certificate retains the supplied scientific assessment, sources and limitations.
