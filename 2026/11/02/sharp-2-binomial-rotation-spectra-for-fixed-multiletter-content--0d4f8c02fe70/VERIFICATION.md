---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For arbitrary positive content c on k>=3 symbols, B_ab(vu)-B_ab(uv)=c_a s_b-c_b s_a, so equal scattered ordered-pair profiles iff the intervening segment Parikh vector is length*c/N. Coprime p=c/d forces segment length a multiple of L=N/d. Hence the L residue classes of indexed rotation starts are distinct; equality L forces all length-L windows balanced, so successive window differences force w=v^d. A grouped word with k>=3 monochromatic runs cannot have a proper circular interval containing a strict fraction of each run (only two boundary runs), attaining N. For arbitrary w, centered prefix counts H_i=N P_i-i c have equalities exactly the collision equivalence; a neighboring transposition changes only H_{t+1}, so distinct-count changes by at most one while sorting v^d into grouped form, realizing the entire interval. Cases d=1 and repeated literal rotations follow. Independent direct/prefix enumerations corroborate, not replace, the all-content proof.

## originality

PASS

Originality concerns the all-positive-multiletter, all-content attainable spectrum and equality/collision characterization. Rigo–Salimov introduce binomial-equivalence methods and address infinite-word factors plus binary cyclic shifts, not a general distinct-signatures-within-one-rotation-orbit spectrum. Poovanandran–Simpson–Teh average subword counts over conjugates of circular words, a genuinely different operation from counting distinct signatures per conjugate. Published semantic Resultary hits such as fixed-content dihedral bracelet orbit profiles treat different invariants. No inspected primary theorem implies the all-integer interval with its upper endpoint k>=3, subject to unindexed Parikh-matrix/conjugacy priority risk.

## value

PASS

The fixed-composition rotation orbit is natural in combinatorics on words; classification of which 2-binomial signatures are distinct is a nontrivial invariant. The exact interval, gcd lower equality and maximal balanced-arc avoidance solve a complete family, explaining the sharp k=2 versus k>=3 difference. Adjacent-swap witnesses make intermediate spectra constructive, not arbitrary finite tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
