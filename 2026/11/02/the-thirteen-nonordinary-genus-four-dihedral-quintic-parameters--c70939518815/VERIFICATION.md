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

For p≥7 the branch polynomial is separable at λ≠0,1. The coefficient at x^(pi−j) can be nonzero only for j equal to the nonzero residue of pi modulo 5. Rows i and 5−i have complementary coefficient indices in the degree-(p−1) power in z=x^5, and their coefficients differ by a nonzero power of λ. The two row pairs give ranks 4,2,0. For p mod 5 equal to 1,2,3,4, the sums d3+d4 agree with floor(3(p−1)/5). The binomial coefficient ratio gives the displayed second-order ODE; P(0) and P(1) are nonzero by its constant coefficient and Vandermonde. If a root away from 0,1 had multiplicity m≥2, the unique lowest-order term of the ODE would come from z(1−z)P'', with coefficient proportional to m(m−1)≠0 since m≤d<p. The separable root counts follow by inclusion-exclusion. At p=23 the two polynomial degrees are 9 and 4, and the replay finds 13 rank-two values already over F529, exhausting the degree bound. The single 4-cycle of possible entries has zero fourth iterate when broken, irrespective of semilinear twists. Inversion is the full geometric equivalence by Ohashi–Kudo Prop. 3.3.4. Independently, the stabilizer of the ten branch points has faithful permutation action and hence 5-part at most 25; it cannot contain a subgroup of order 25, because a group of that order is abelian and the centralizer in PGL2 of a projective element of order 5 is a torus, with no 25th roots of unity in a subgroup of exponent 5. A cyclic subgroup of order 25 cannot act faithfully on ten points. Thus the visible order-five groups can be matched by target conjugacy and the residual change of coordinate is x↦a x or a/x. Its effect on the two fifth-power values gives exactly inversion or equality. The replay of t=λ+1/λ gives the seven distinct roots of the stated polynomial with fiber sizes 1,2,2,2,2,2,2 and three rational t values. This does not determine twists or all Ekedahl–Oort types.

## originality

PASS

Credit prior work for the same family, Cartier sparsity, common-root superspecial criterion, geometric inversion and the four-or-zero p-rank phenomenon. The inspected statements do not provide the general separable-root a-number census together with, or subsuming, the characteristic-23 nonordinary rank-two locus and its exact moduli polynomial and arithmetic.

## value

PASS

The known absence of superspecial members in characteristic 23 makes the remaining nonordinary locus a meaningful missing layer of an already studied natural automorphism pencil: it has thirteen marked points, all p-rank zero but a=2, with seven coarse points of specified residue degrees. The exact polynomial locates those points rather than merely testing specialness. The all-prime argument distinguishes reduced marked-parameter strata, beyond a single factorization, without claiming a closed formula for the gcd degree.

The dated certificate retains the supplied scientific assessment, sources and limitations.
