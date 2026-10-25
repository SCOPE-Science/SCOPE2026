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

# Verification record

The theorem's infinitary assertions are established by explicit extremum constructions in `RESULT.md`; finite experiments alone cannot prove them. The proof separately checks both directions for arbitrary inputs to the Gödel box and diamond, finite-range inputs, the continuity of the positive-degree cutoff, and all endpoint cases including zero weights and \(\delta=1\).

Replay the exact rational arithmetic checker from its containing directory with `python3 checker.py`. It exhausts all length-one through length-three rows and valuations over a four-degree rational palette, then verifies closed-form finite-prefix identities for three infinite counterexample families at lengths \(4,8,16,32\). It printed:

`EXACT_PREFIX_CHECKS_OK: enumerations n<=3; illustrative prefixes 4,8,16,32`

The checker does not certify an infinite theorem or determine bibliographic priority. Modal validity, proof-search complexity, and any nested finite-palette closure are outside the claim. No independent audit has been performed.
