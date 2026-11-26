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

Use the even-weight representatives of T, where direction i is the complement of e_i. The vertices at distance two from zero are the ten distinct sums of two directions; each is identified by its two neighbors in the zero-neighborhood. The vertex stabilizer is therefore faithful on those five neighbors, so the affine subgroup is full. Rebuilt all open-neighborhood faces and reduced their augmented boundaries over Q: 352 nonempty faces, ranks (1,15,65,64,16) including the augmentation, only reduced H2 of dimension 31. Computed reduced Lefschetz traces by invariant unions of simplex vertex cycles. Compared each of the 1,920 exact values directly to the proposed representation's trace: sum over fixed translation-weight labels, with their stabilizer character multiplied by the corresponding translation scalar. All matched, including the claimed full trace histogram. Character equality implies rational isomorphism. For each orbit a rational invariant submodule splits into translation weights; the one weight space is an irreducible stabilizer module and its conjugates exhaust the orbit, proving irreducibility of each summand. The orbit-zero module has dimension six and no S5 invariants. Replay: python3 /workspace/independent/recompute_complexes.py 2.

## originality

PASS

Credit only the full affine action beyond the nonequivariant Betti number and translation restriction. Three distinct indexed statements give equivalent full actions, in later-dated catalogue entries. The closest equivalent's prior-work passage supplies no evidence of an earlier full action or of a carry-forward. The inspected evidence does not establish earlier full coverage; the chronology is not an assertion of priority or of independent discovery.

## value

PASS

The full affine action is a natural missing invariant of a standard highly symmetric graph complex. It distinguishes six translation-invariant classes from zero full-group invariants and determines the effects of coordinate permutations on each weight orbit, which the rank or translation character cannot answer. This provides an exact test case for equivariant topology of folded cubes rather than a rerun of the ordinary Betti calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
