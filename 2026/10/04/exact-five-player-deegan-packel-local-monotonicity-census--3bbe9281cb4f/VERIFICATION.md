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

Run `python verify_deegan_packel_census.py dp_census.json` with Python 3 standard library only. A successful replay prints `VERIFY_OK` and the exact counts used in the finding.

The verifier generates all five-player monotone Boolean games recursively and independently generates weighted games from nonincreasing integer weights in \(\{0,1,2,3,4,5\}\) and all feasible positive quotas. It canonicalizes minimal-winning-coalition antichains under all player permutations, checks that both routes produce the same \(117\) weighted isomorphism classes, and computes Deegan–Packel scores with `fractions.Fraction`.

The archived `dp_census.json` records all \(17\) violating classes, one explicit integer weighted representation for each, exact normalized Deegan–Packel vectors, and all violating dominance pairs. The verifier regenerates the census and requires exact JSON-value equality.

Limit: this is exhaustive finite verification, not a proof for more than five players. Literature originality is assessed separately and is not certified by the replay.
