---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Read RESULT.md full Hermite divided-difference/confluent-residue proof. The simplex Fourier integral equals (-2pi i)^(-5) times fifth divided difference of exp(-2pi i t) at the six integer barycentric frequency nodes. All distinct nodes give zero by constant interpolation. For multiplicities, each integer-node residue is a rational-coefficient polynomial in c=2pi i (all exp(-c*x)=1); since pi is transcendental, zero of that polynomial is equivalent to vanishing of each rational coefficient. A unique node with multiplicity >=3 forces an uncancelled high-degree c coefficient; types 3+3 and 2+2+2 have nonzero linear c coefficient. The only possible repeated-node zero type is 2+2+1+1, where cancellation of the two simple double-node residue coefficients occurs only for doubled positions (0,2) or (1,3), producing precisely the two gap equations. Algebraically these give divisibility parameterizations delta=r-p | 2p^2 and its reflection. An independently implemented rational formal-residue algorithm checked all 1287 integer-node six-multisets with min 0 and nodes in [0,8], matching exactly the classified families. This check is finite; exhaustive partition/degree argument proves all integer nodes.

## originality

PASS

General simplex transform and Fourier-zero geometry results furnish tools and other constraints, but none inspected gives the complete integer multiset classification. Priority qualified because a specialized confluent divided-difference treatment could duplicate it.

## value

PASS

Gives an exact arithmetic description of all lattice Fourier zeros for a canonical dimension-five polytope, including two infinite and nontrivial repeated-knot families that simple all-distinct vanishing does not capture. Useful for spectral and tiling/cubature questions involving integer Fourier data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
