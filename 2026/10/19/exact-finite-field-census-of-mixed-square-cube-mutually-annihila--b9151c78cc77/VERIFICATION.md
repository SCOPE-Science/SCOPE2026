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

Rank r of A fixes a unique square-zero Jordan type. Its labeled realizations are counted by choosing im A in ker A and then an isomorphism from the quotient to im A, giving the two Gaussian factors times |GL_r|. In U⊕W⊕T with A:T→U, annihilation means B vanishes on U and has image in U⊕W. Direct cubing leaves Z³, XZ², Z²H and XZH, with Y free. On each length-three chain, H lands in ker Z² and applying Z puts its component in im Z², which X kills; one r-coordinate row and column per such chain have been constrained. Length-one chains have Z=0. The length-two chains supply exactly X_2 H_2=0, while the other X,H coordinates contribute q^{2r(s−u−v)}. For rank h of H_2, choose its image, count surjections onto that h-space, then let X_2 factor through the v−h quotient. These are exactly the three factors in H_{r,v}. To check the Z orbit size, the dimension of its F_q[t]-module endomorphism space is the sum of min(i,j) over pairs of cyclic blocks, equal to (u+v+w)²+(u+v)²+u². Reducing on M/tM gives a triangular map by block length (a map from a shorter cyclic summand into a longer one has image in tM). Invertibility is equivalent to invertibility of each same-length diagonal block, by nilpotence of t. The fraction of invertible endomorphisms is therefore the three stated products. Orbit–stabilizer gives J and every term of the sum, including the zero-dimensional empty case. For n=2,3, the A=0 terms are respectively q² and q⁶ (also from summing the allowed single-matrix Jordan orbits), while the rank-one fibers have q and q³ choices for B, giving the advertised polynomials. Independent GF(4) enumeration of all n=2 labeled pairs gave 76, and GF(2) fixed-A/Z enumeration gave 384 and 320 for Z chains (3,2) and (2,2), respectively, exercising the three-block constraint and the two-chain coupling. Additional exact fixed-A enumerations gave total counts 10, 232 and 3537 at (n,q)=(2,2),(3,2),(3,3).

## originality

PASS

The bounded-exponent variety, the individual Jordan orbit weights, and broadly unrefined mutually annihilating counts are known. The supported distinct finding is the exact labeled point count at mixed square–cube bounds, including the residual size-two coupling in the fixed-A fiber. The inspected exact square-zero slices omit all B with a size-three Jordan block, and the inspected unrefined nilpotent totals sum over types without tracking those bounds.

## value

PASS

This counts labeled finite-field representations of a natural small mixed-exponent annihilator algebra, a geometric family with a previously inspected component theory but no point count there. The fixed-rank residual formula separates the exact coupling from standard orbit weights, so it gives usable arithmetic information for each population of square-zero first factors. It is more informative than brute-force small dimensions or replacing this asymmetric problem with the square–square subvariety.

The dated certificate retains the supplied scientific assessment, sources and limitations.
