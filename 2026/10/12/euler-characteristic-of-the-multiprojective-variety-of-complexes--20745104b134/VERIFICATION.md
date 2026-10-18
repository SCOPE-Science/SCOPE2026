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

The variety in product_i P Hom(V_{i-1},V_i) imposes f_{i+1}f_i=0 with each arrow nonzero, over C. The generic diagonal one-parameter subgroup has pairwise distinct weights on matrix coordinates in each projective factor, so its fixed tuples consist of matrix units. Consecutive units compose to zero iff their source/target intermediate indices differ. First arrow has d0*d1 choices, and arrow i>1 has (d_{i-1}-1)*d_i choices, totaling d0*d_n product_{i=1}^{n-1} d_i(d_i-1). Additivity of compactly supported Euler characteristic with C* fixed-point localization applies to possibly singular projective variety; projectivity gives ordinary topological Euler characteristic. If an intermediate dimension is one, nonzero adjacent maps cannot compose to zero, so the variety is empty. n=1 gives P^{d0*d1-1} chi=d0*d1. Independently enumerated fixed-point tuples for vectors (1,2,3)->6, (2,3,2)->24, (2,2,2,2)->16, (1,3,3,1)->36, (3,1,2)->0; finite checks corroborate universal C* proof.

## originality

PASS

Cukierman 2014 defines precisely the multiprojective variety of complexes and studies rank strata, tangent spaces, components and foliations, but relevant examined primary text states no topological Euler product formula. Its Euler characteristic terminology is the alternating dimension sum of a vector-space complex, a different invariant. Classical affine variety of complexes and singly projectivized type-A quiver loci do not have separately nonzero projective arrows, so their formulas do not formally imply the product of d_i-1 factors. A short standard C*-localization application may be folklore or appear in older unindexed literature; qualified best-of-knowledge PASS.

## value

PASS

Uniform integral Euler characteristic of the classical multiprojective parameter space for every length and dimension vector, with a simple relative factor for each intermediate dimension, supplies a natural topological invariant and exact emptiness boundary. Short general fixed-point proof is nontrivial application, not an arbitrary parameter slice; does not imply Betti numbers or smoothness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
