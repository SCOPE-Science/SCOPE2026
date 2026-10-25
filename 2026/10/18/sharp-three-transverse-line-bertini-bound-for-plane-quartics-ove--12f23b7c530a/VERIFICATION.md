---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The theorem counts 13 F3-rational lines on each geometrically smooth plane quartic, and a line is transverse precisely when its homogeneous restricted binary quartic has four distinct roots over the algebraic closure, equivalently nonzero and projectively squarefree via the derivative gcd and infinity-root check. Normalizing the first nonzero ternary coefficient to one leaves (3^15-1)/2=7,174,453 forms. I independently implemented the 13 restriction matrices by exact SymPy ternary polynomial substitution, a length-243 squarefree table, and three 5-trit base-243 block lookups. Fresh C++ exhaustively enumerated all 7,174,453 normalized forms and reproduced the complete transverse-line histogram t=0..13: [5395,15795,50544,172146,413829,565110,938808,921726,1161108,1220427,1123200,470340,116025,0]. Independently generating the two coordinate swaps, scaling, and two shears from substitution in homogeneous quartic monomials, I computed projective orbits of every t<=3 equation; the counts were exactly t=0:14, t=1:8, t=2:21, t=3:49, hence 92 orbits. A separate SymPy Gröbner unit-ideal test on all three affine charts of each of these 92 representatives found exactly two smooth representatives, coefficient codes 78805 and 80265, both with t=3 and orbit size312. All forms with t<3 are geometrically singular, so the lower bound for every smooth plane quartic is a *complete finite proof*, not unbounded extrapolation. Their 624 normalized equations split into exactly two orbits; independent source direct-line substitution gives exactly Y=0,X+Y=0,X+2Y=0, rational point counts 1 and 10, separating curve isomorphism classes. The code was written afresh rather than merely trusting source output; exact original source C++ and SymPy supporting scripts were also inspected and their SHA recorded.

## originality

PASS

Best-of-knowledge original sharp cardinality and equality-class census at the natural small-field Bertini threshold (degree q+1=4 over F3). Asgarli (2018) establishes at least one Fq rational transverse line for smooth reflexive degree<=q+1 and handles certain nonreflexive degrees; his theorem does not give a sharp minimum of three or the two extremal F3 plane-quartic orbits. Asgarli–Freidin (2020) gives an asymptotic incidence-probability result for transverse-free curves as degree grows, not an exact fixed q=3,d=4 extremal orbit classification.

## value

PASS

At the exact natural Bertini degree boundary d=q+1, the optimal *number* of transverse F3-rational lines is a nontrivial strengthening of the classic qualitative existence theorem. The complete small-field classification and two inequivalent extremal canonical genus-three curves, distinguished by F3-point counts, are meaningful exact algebraic/finite-geometric invariants. A finite exhaustive result is mathematically complete here: all coefficients and all potential bad low-transversality orbits were exhausted with algebraic-closure smoothness tests, not a partial census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
