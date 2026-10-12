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

# Verification

The mathematical proof is universal; the following independent computations are supplementary.

Run \(\texttt{python3 verify\_fair\_coalition.py}\). The included program constructs the graph adjacency masks directly, checks the exact two-neighbour fair-domination predicate over every nonempty vertex subset, and exhaustively enumerates all set partitions on \(K_{3,3,3}\), \(K_{3,3,4}\), and \(K_{3,4,4}\) using restricted-growth words. The counts are respectively 21,147, 115,975, and 678,570 partitions, with optimum coalition numbers 6, 7, 8. It also checks no proper eligible union for complete multipartite graphs with four or more parts, for multiple small graph profiles.

A separate enumeration of all 13,860 three-pair matchings of 12 vertices verifies that precisely 1,728 represent optimum coalition partitions of \(K_{4,4,4}\), all with pair types \(AB\), \(AC\), \(BC\), agreeing with \(8\binom42^3\). Original program output is supplied as \(\texttt{verification\_output.txt}\).

Finite checks do not certify any infinite statement; the part-occupancy lemma, extremal excess obstruction, and explicit constructions in RESULT.md supply the general proof. The primary source on ordinary multipartite \(k\)-coalition numbers has not been inspected in full, so precise coverage risk remains. No independent external audit has been performed.
