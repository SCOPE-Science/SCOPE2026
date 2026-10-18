---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Finite Esakia duality sends the (2^m+1)-element top extension of Boolean P([m]) to the rooted star P_m. A p-morphism P_n→P_m sends source root either to a target leaf (forcing constant map, m choices and two-valued algebra image) or to target root (forcing a surjective function of n leaves onto m leaves, m! S(n,m) possibilities and injective algebra map). Surjective p-morphic quotients of P_m are singleton or rooted stars with k≤m leaves, and their fibers are partitions of the original leaves; this proves the exact Bell-graded subalgebra spectrum and inclusion order by coarsening. For n=m, bijections give m! automorphisms; m leaf constants give the only other endomorphisms and are idempotent; only identity is an idempotent permutation, yielding m+1 idempotents but just two distinct retract images. We reconstructed dual upcone conditions and verified small m,n counts against independent direct algebra implication/residuation reasoning. The source standard-library program exhaustively enumerates n,m≤5 p-morphisms and m≤4 all subalgebras; that finite enumeration does not stand in for the all-parameter argument.

## originality

PASS

The combined hom-set image-rank polynomial, entire partition-indexed subalgebra lattice and exact two-retract rigidity for the specific Boolean-with-one-new-top witness family were not found stated in inspected old Heyting lattice/duality work or Bumpus–Kocsis. Classical Esakia duality and general subalgebra-congruence correspondences are essential known inputs, not new discoveries.

## value

PASS

Provides a complete exact natural example with unexpectedly divergent structure: B_m+1 distinct subalgebras but only two embedded retract subalgebras, with all morphism image sizes and exact counts. This is a useful invariant of the concrete finite Heyting satisfiability-gap witness family, not an arbitrary unmotivated parameter slice; no general theorem or paper-sized contribution is demanded.

The dated certificate retains the supplied scientific assessment, sources and limitations.
