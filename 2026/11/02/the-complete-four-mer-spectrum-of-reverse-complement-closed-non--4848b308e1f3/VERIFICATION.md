---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and reproducibility

The finite theorem is proved by an exact orbit-to-clique bijection and a terminating integer recurrence, whose full input graph is provided in `adjacency.tsv`. The proof's computational portion is a transparent, finite exhaustive calculation, not a claim of externally certified correctness.

Run `python3 verify_graph.py adjacency.tsv` to regenerate all 136 reverse-complement orbits, select 56 admissible orbits (12 fixed and 44 paired), rebuild the 420-edge compatibility graph, compare the complete text of the graph certificate and derive every coefficient via exact integer polynomial recursion. Actual replay output began with `GRAPH_VERIFY_OK` and reported the vector `(1, 12, 88, 288, 584, 760, 688, 424, 160, 32)` and 1318 distinct memoized states.

Run `python3 crosscheck_direct.py` to enumerate all valid codebooks independently by extension with direct Hamming and prefix/suffix tests, without the primary graph recurrence or memoization. Actual replay output began with `DIRECT_CROSSCHECK_OK` and independently reproduced the ten coefficients, total 3037, 32 size-nine maximizers, four eight-element relabeling orbits, and optimal-codeword compositions `(5,2)` in 24 cases versus `(1,4)` in eight cases (first component: fixed words; second: two-word reverse-complement orbits). The four example codebooks are written in `maxima_orbits.tsv`.

All arithmetic is exact and both programs require only Python 3 standard-library modules. `spectrum.csv` records the complete distribution. No computation for larger word lengths or stricter Hamming distances is implied. An independent scientific audit has not been performed.
