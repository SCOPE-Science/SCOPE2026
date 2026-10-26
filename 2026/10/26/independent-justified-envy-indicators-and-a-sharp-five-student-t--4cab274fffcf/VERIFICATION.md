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

## Reproduction

Run `python3 check.py` with a standard Python installation. This enumerates all strict individual school rankings in the exact sequential mechanism and checks the joint indicator law for every fixed serial order with one through four students. For five students it tests the two priority orders that witness the high-tail reversal. All operations use exact integer counts and rational probabilities.

## Observed outcomes

The checker returned 35 fully checked order instances (1 + 2 + 6 + 24 + 2), including joint probabilities for every possible zero-one envy pattern. It also checked 43 adjacent priority corrections in the one- through four-student markets at every upper-tail threshold. The five-student witness probabilities for at least two envious students were exactly 4/15 (before) and 3/10 (after); for at least one, exactly 13/15 and 4/5. Every assertion passed.

## Logical limits

The finite enumeration does not establish a theorem for unbounded market size. The proof uses conditional uniformity and a two-Bernoulli stochastic-order criterion. Verification does not cover correlated preferences, heterogeneous school priorities or random order selection conditional on preferences. No independent scientific audit has been carried out.
