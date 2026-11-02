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

# Reproduction and limits

The supplied programs require Python 3 and only its standard library. From the directory containing the extracted files run `python3 verify_permutations.py certificate.json` and then `python3 verify_bitboards.py certificate.json`.

The permutation checker examines all \(40320\) candidates and all \(4186\) unordered pairs of the resulting \(92\) valid configurations, recomputes the entire threshold-four and threshold-five adjacency tables, performs complete traversals and all-source breadth-first searches, checks the symmetry orbit, and reconstructs the exactly-five-exchange graph. The bitboard checker independently generates \(92\) placements through diagonal masks, uses population counts of board-symmetric differences for the exchange rule, separately constructs and traverses the required graphs, recomputes distance statistics, and crosschecks the shipped certificate neighbor sets.

Replayed checks yielded `PERMUTATION_EXHAUSTIVE_PASS` and `BITBOARD_INDEPENDENT_PASS`. The computed values are \(168\) threshold-four edges with component orders \(84,2,2,2,2\), \(464\) threshold-five edges with radius \(3\) and diameter \(4\), and \(296\) exactly-five-change edges with radius \(4\) and diameter \(5\). The full threshold-five unordered-pair distance profile is \((464,2002,1704,16)\).

This is a complete finite calculation, not a general-board proof. Two programs give a useful crosscheck but are not independent scholarly validation. The external audit status remains not performed.
