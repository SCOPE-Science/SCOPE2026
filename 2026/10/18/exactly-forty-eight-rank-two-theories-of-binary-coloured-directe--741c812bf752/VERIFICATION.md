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

# Reproducibility

All calculations use Python's standard library. From a directory containing the accompanying files, run `python verify_cycle_rank2.py` and `python verify_cycle_bruteforce.py`. Their recorded exact outputs are in `closure_output.txt` and `direct_output.txt`; `theory_catalogue.tsv` lists all 48 signature keys and shortest cyclic witnesses.

The transition-closure verifier starts from every two-letter word and repeatedly appends either symbol while retaining the first and last two letters, capped symbol counts, and all internal three-letter factors. It reaches exactly 758 states and checks the resulting 48 distinct cyclic rank-two signatures, including the length distribution of shortest representatives and the four length-nine witnesses. A state is a sufficient statistic for all future appends and for cyclic closure; therefore a closed reachable-state set proves the calculation for words of unbounded length.

The brute-force verifier directly builds the set of atomic two-point diagrams around every root in each binary directed cycle of length 3 through 15. It checks that this game-type invariant and the stated neighbour signature classify exactly the same words; it also enumerates 758 finite-word summary states and verifies that the resulting finite set is closed under appending either colour. Thus both computations agree on the count and shortest-representative distribution, using distinct implementations.

This does not constitute external or independent mathematical auditing. Finite brute-force enumeration by itself does not prove an all-size statement; the transition closure and the Ehrenfeucht--Fraïssé characterization supply that proof. The result is restricted to rank-two ordinary first-order logic on two-coloured, consistently oriented, loopless directed cycles of length at least three.
