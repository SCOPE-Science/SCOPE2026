---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

With q=4 and τ(a,b,c)=(-c,-b,-a) mod4, there are exactly eight τ-fixed triples among 64, leaving 28 nonfixed τ-orbit edges. Quotient two-letter τ-orbits give ten multigraph vertices with six odd degrees (00,01,03,12,21,22). A negative-orientable cyclic word selects pairwise distinct quotient edges in a closed walk; an Eulerian selected subgraph must omit ≥3 edges, so length≤25. Exactly 25 would omit a perfect matching among those six odd vertices. Exhaustive 28-edge quotient construction yields exactly two matchings, represented by 001/032/122 and 003/012/221. For a nonfixed pair v, the τ-invariant edge flux φ_v(a,b,c)=p_v(a,b)−p_v(b,c) telescopes to zero along any cycle. The two omission choices leave total flux −2 at v=12 and +2 at v=03 respectively, obstructing a 25-cycle. The explicitly given cyclic word 003122113232010233313033 has 24 distinct nonfixed τ-orbits. Independently recomputed all 64 triples, quotient parity, two matching choices, both fluxes and witness windows; source verifier Git blob 2c77445b35319f5b725ad8d0e73c4a637a27b1c9 uses exhaustive finite universe. No extrapolation to other q,n.

## originality

PASS

The final claim is compared by statement and implication, not by title. The negative-reversal orbit condition differs from reversal-only orientability and from negative avoiding sequences which forbid additive negation without reversal. Prior de Bruijn subgraph balance methods are equivalent to the quotient graph parity obstruction at a conceptual level, but the two exact matching exclusions by invariant flux and a length-24 witness are additional. Existing 2025 general period upper bounds for NOS_4(3) give 27 (Table1); 2026 improved bounds leave a gap for n>2. Neither gives a general theorem implying the exact 24 for this instance in accessible material. Stronger recent manuscript inaccessible makes this best-of-knowledge. This is a concrete extremal finite alphabet/window invariant, not merely re-reading an OEIS table. Direct Resultary search yielded no q4 n3 exact 24 result; negative result alone is insufficient for absolute novelty. A stated upper bound 25 or 26 plus a known 22-period construction does not imply exact maximum 24. The independent flux obstruction to 25 and verified 24-word close that gap; possible later manuscript revision could still cover the same claim. Accessible primary texts were materially compared; inaccessible plausible primary texts are named as residual risks rather than treated as disproving novelty.

## value

PASS

Negative-orientable sequences are canonical cyclic position codes robust to reversal followed by additive negation. The four-symbol, length-three case is a natural explicitly published smallest open instance. Tightening the known construction and upper bounds to a provable 24-position exact maximum via combinatorial parity plus a new flux obstruction resolves a mathematically motivated finite classification, even without a general (q,n) theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
