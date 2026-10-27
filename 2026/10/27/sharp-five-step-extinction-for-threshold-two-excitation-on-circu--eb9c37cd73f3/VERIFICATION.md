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

# Reproduction

Compile `verify.cpp` with an ISO C++17 compiler and run it without input. Its exact outputs are supplied in `verification_output.txt`. Each possible four-rung input is enumerated to build the pair language; every pair-admissible seven-rung word is then checked after three local updates. This proves a local lemma for any circumference, including wrapped small rings, because using all unconstrained input quadruples only enlarges the possible pair language. The verifier also exhaustively enumerates every cyclic configuration at circumferences 3 through 5 and checks explicit witnesses at circumferences 6 through 80. The witnesses for all circumferences above seven are certified mathematically by their three-step local backward cones.

# Limitations

The exact finite local enumeration is a computational part of the proof and has not been independently audited. The numerical witness checks through 80 are illustrative; the all-size witness statement relies on the local-radius argument, not on extrapolation. Prior-art searches and checks do not prove absolute novelty.
