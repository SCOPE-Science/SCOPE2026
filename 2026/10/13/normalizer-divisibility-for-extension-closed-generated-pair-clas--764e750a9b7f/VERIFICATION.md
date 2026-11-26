---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Reconstructed the induction on |K|. For H=N_G(<x>)∩K and A={a∈K:<x,a>∈C}, conjugation by H preserves A. An admissible maximal T⊴K in H exists starting with 1. The lift D of (H/T)∩Z(K/T) normalizes U=<x,a,T>: it normalizes <x> and T and centralizes a modulo T. Thus UD/U is a quotient of the abelian group D/T; it lies in C because finite abelian groups are built from cyclic factors, not because C is quotient-closed. Extension closure forces D=T by maximality. A is T-coset-saturated by subgroup closure. Nonidentity hT has a proper centralizer preimage L<K, and induction for L gives |C_{H/T}(hT)| dividing the fixed-point count on A/T. Grouping Burnside's sum by conjugacy classes gives the divisibility of the identity term, then multiplying by |T| restores the target. The argument also handles H/T trivial, K=1, and x outside K. For π-separability one can intersect and splice subnormal π/π′ series; equivalently all composition factors are π or π′ groups, and a chief series gives a normal series in the whole group if that convention is intended. No enumeration, quotient-closure assumption, or formal verification is needed.

## originality

PASS

The ordinary soluble case and essentially the entire counting strategy occur in Sabatini. The supported distinct content is the relative theorem uniformly for the stated class axioms and its nonsoluble π-separable and p-solvable instances. The soluble-set divisibility does not imply a divisibility for a larger generated-pair set; the maximal normal subgroup and coset-saturation steps must be justified under the new axioms.

## value

PASS

Identifies a reusable closure mechanism for a relative normalizer divisor that previously applied to solubilizers, with no quotient-closure or formation assumption. The nonsoluble π-separable instances are genuinely different counting problems, not a renaming of solvability. The contribution is the closure generalization, not the Burnside method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
