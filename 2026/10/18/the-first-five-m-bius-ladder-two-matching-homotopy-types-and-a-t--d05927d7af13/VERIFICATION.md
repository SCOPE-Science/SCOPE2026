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
# Finite homotopy verification

Execute `python3 verify.py` from the same directory. The program reconstructs every source graph and simplicial face, checks both equivalent independent incidence criteria, produces explicit greedy toggle pairs, exhaustively verifies directed Hasse acyclicity and computes the signed Morse boundary matrices by recursive unit elimination. It verifies the unimodular minors giving the homotopy cancellations. The expected completion marker is `MOBIUS_LADDER_TWO_MATCHING_CERTIFIED`.

Verified ranges: the five integers \(3\le n\le7\). The largest enumeration has 448,945 faces and 3,693,564 Hasse incidences. This establishes only the stated finite range. No external or independent mathematical review has been performed.
