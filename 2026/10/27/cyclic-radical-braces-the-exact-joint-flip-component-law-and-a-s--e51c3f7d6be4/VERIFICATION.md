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

Run `python3 verify_cyclic_brace_orbits.py` from the same directory. The standard-library-only checker reports `VERIFY_OK` after 25 exhaustive parameter triples. It constructs the left-action maps directly, computes orbit closures without using the theoretical orbit classification, checks the right actions preserve those components, and compares the three probabilities with direct ordered-pair counts. All solution triple identities are checked exhaustively in the smallest cases.

The general identities and asymptotics require the valuation proof in `RESULT.md`. The checker tests only finite parameter ranges; it does not certify the infinite assertions or literature originality. Independent mathematical validation has not been performed.
