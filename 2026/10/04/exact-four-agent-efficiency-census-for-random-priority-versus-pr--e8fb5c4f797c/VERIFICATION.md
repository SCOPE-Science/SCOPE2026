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
The embedded `verify_rsd_ps_four_agents.py` performs an exact exhaustive replay with the Python standard library.

The domain contains
\[
24^4=331776
\]
labeled strict-preference profiles.

For every profile, the verifier computes random priority by averaging all \(24\) serial-dictatorship priority orders and computes probabilistic serial by exact rational object-exhaustion events.

Random-priority ordinal efficiency is evaluated with the Bogomolnaia-Moulin acyclicity relation. Probabilistic-serial stochastic dominance is checked agent by agent at every rank cutoff.

The verifier confirms:
- \(72288\) equal assignments with random priority ordinally efficient;
- \(190512\) distinct, incomparable assignments with random priority ordinally efficient;
- \(57312\) distinct, incomparable assignments with random priority ordinally inefficient;
- \(11664\) profiles where probabilistic serial stochastically dominates random priority;
- \(68976\) total random-priority-inefficient profiles;
- exact probabilities \(479/2304\) and \(9/256\);
- exact conditional share \(81/479\).

Run:

`python3 verify_rsd_ps_four_agents.py`

The first output line must be:

`VERIFY_OK`

The computation is exhaustive for the stated four-agent domain only.
