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

# Reproducible checks

Run `python3 verify_hill.py` using Python 3 and only the standard library. The program executes two structurally different generators of integer partitions; both agree at every census size from \(1\) to \(14\). It checks \(20{,}283\) unordered profile pairs, finds exactly one strict triple-index reversal, and independently verifies the sharp upper/lower square-sum envelopes for every possible fixed richness and largest-part combination in this census range. The envelope-candidate list is exactly \([(14,5,6,6,52,54)]\).

The proof's infinite mathematical ingredients are simple discrete convexity and majorization; the finite parameter bound is established only through the verified, complete integer loop over census \(N\le14\). The program does not prove novelty, certify primary-source exhaustiveness, or address survey sampling. The order-dependent profile may have other properties outside the theorem's three selected diversity indices. Independent audit has not been performed.
