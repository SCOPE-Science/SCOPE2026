---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For odd q substitute x=(s+t)/2,y=(s-t)/2, obtaining 8(h_a(x)+h_a(y))=t^4+(6s^2+4a)t^2+s^4+4as^2. For fixed s the even quartic fibers reduce to square pairs with w1+w2=-B; the quadratic-character correlation sum and exclusion of diagonal pairs give the precise H_0..H_4 histogram. B=0 yields the D_j quartic power map histogram; the Z,T character sums count the slice multiplicities, with distinct branches for characteristics two and three. The resulting A_j, sumset and energy formulas follow from partitioning all q choices of s. In char 2, x->x^4+ax^2 is F2-additive, so every image target has q ordered representations. I inspected the exact finite-field checker and independently brute-force compared all q^2 ordered pairs and all q^2 targets for 158 coefficient choices across prime q=3,5,7,11,13,17,19,23,29,31: every histogram matched the theorem. This finite test supports, not substitutes for, the symbolic proof over every prime power.

## originality

PASS

Known one-variable quartic-image results by Sun and Ding–Zieve can imply support cardinalities for individual s-slices; the previously published quartic-graph energy at a=0 is directly covered and acknowledged. The surviving contribution is the complete all-a, all-characteristic global *ordered representation multiplicity histogram* over targets (s,v), including char2/3 and sign-class switching; the published fifth-power graph spectrum is a different polynomial family. No existing full all-parameter histogram was found in primary-source comparisons or Resultary.

## value

PASS

Additive representations of polynomial graphs are natural arithmetic-combinatorial statistics. The entire zero-to-four fiber multiplicity spectrum, exceptional Frobenius regimes, energy and exact sign-dependent sumset reversal offer a coherent complete classification with explicit consequences beyond known support size or a=0 special case; not merely an arbitrary numerical coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
