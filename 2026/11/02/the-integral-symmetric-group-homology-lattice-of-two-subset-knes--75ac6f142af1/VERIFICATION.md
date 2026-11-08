---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For m>=5, maximal faces of pairwise-intersecting two-subsets are the m star simplices and exceptional triangles. The star union has H1 integrally the cycle lattice of K_m, identified equivariantly with wedge^2 ker(epsilon:Z^m->Z); every exceptional oriented triangle attaches by contraction delta:wedge^3 Z^m -> wedge^2 U. Splitting by a vector of augmentation 1 shows delta surjective, ker delta=wedge^3 U integrally and naturally, without using a non-equivariant contraction. Exterior-character determinant gives [t^3] prod(1-(-t)^lambda)/(1+t). Finite invariants are exact over Q so rational quotient H2 is C_m-averaged character; independently computed cyclic dimensions for all 5<=m<=29. Entire source verifier calculates mod2 homology and signed permutation traces up through m8; finite cases only corroborate the unrestricted topological proof.

## originality

PASS

Barmak Theorem4.11 already gives nonequivariant wedge of C(m-1,3) S^2; Feng–Nukala likewise study Vietoris–Rips scale2 of two-subsets. The symmetric-group integral lattice, character and resulting cyclic quotient dimensions are not determined by the mere nonequivariant Betti count or a star-collapse based on one preferred label. Published equivariant Kneser results from search concerned the distinct neighborhood-complex functor.

## value

PASS

Upgrades a familiar nonequivariant homotopy count to a canonical integral permutation representation for an infinite natural Kneser family and explicit group-quotient invariants; useful distinction of symmetry structure invisible to Betti numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
