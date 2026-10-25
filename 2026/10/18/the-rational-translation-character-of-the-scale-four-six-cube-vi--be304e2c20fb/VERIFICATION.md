---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

The inclusive Rips complex on the 64 Hamming vertices is the independence complex of the 7-regular forbidden graph with edges at distances 5 and 6. Every nonidentity translation acts freely in 32 two-element vertex orbits; stable simplices are unions of eligible orbits, with the chain-orientation sign contributing the negative of the quotient signed independence sum. Independent exact memoized branching of the 64-vertex independence polynomial gave Z=253 (3,974,224 states); independent quotient bit-mask recursions gave signed sums 9,9,53,53,1,1 for weights 1..6. The Fourier inversion over all 64 translations returns multiplicities (36,1,0,6,6,0,1), with dimensions summing 253 and 36 invariants. Passage from virtual reduced Lefschetz to genuine trace explicitly depends on the published 2026 rational homology concentration: reduced H7 rank 239 and H15 rank 14, both odd degrees; those very large homology matrices were NOT recomputed. No assertion about separate-degree characters or torsion.

## originality

PASS

Best-knowledge originality PASS: the nonidentity translation traces and dual-weight Fourier multiplicities are not implied by the published nonequivariant ranks (239,14), scalar signed face count 253, or different-scale and different-complex equivariant results. Existing full cube-symmetry results are for scales at most three or the penultimate distance five; this is the interior distance-four case. Literature overlap and independent verification of the large external homology premise remain explicit risks.

## value

PASS

Translation action on higher homology is an explicitly motivated equivariant problem for hypercube Rips complexes. The complete 7-row rational character for a natural first interior case gives exact invariant dimension 36 and rules out dual weights 2 and 5, strictly more information than Euler or Betti numbers. Its finite quotient method is reproducible and applicable to other symmetry modules; it claims neither a broader dimension theorem nor integral torsion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
