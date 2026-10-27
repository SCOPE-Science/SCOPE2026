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

# Verification instructions

Execute `python verify.py` with Python 3.9 or later. The verifier uses only the standard library and terminates with five `VERIFY_OK` messages. It exhaustively generates the proper colouring quotient in two independently normalized ways, compares two implementations of every Kempe component move, checks graph undirectedness and all degrees, breadth-first-searches the entire graph from all \(2080\) roots, and computes automorphism orbits from all adjacency-preserving vertex bijections. Assertions check \(2080\) states, \(12600\) edges, eccentricity counts \((5:60,6:1860,7:160)\), radius \(5\), diameter \(7\), \(120\) base automorphisms and the complete \(21\)-orbit classification.

The computation is exhaustive for this one finite graph; it makes no extrapolation to infinitely many graphs or different colouring spaces. No independent audit has been performed.
