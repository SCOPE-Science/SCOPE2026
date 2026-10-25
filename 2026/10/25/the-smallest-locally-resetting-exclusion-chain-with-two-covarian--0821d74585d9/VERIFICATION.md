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

Run `python check.py` using Python 3 and SymPy. The included `check_output.txt` is the actual console output of this command, with the exact counts, algebraic covariance identities, rational signs and numerical root approximations.

## Analytic scope

The finite generator balance identities hold as rational polynomial identities for every nonnegative resetting rate; rational checks are **not** a finite sampling claim. The two roots are exhaustive because the quartic has at most two positive roots by Descartes' rule, while strict signs at three rational rates force two distinct positive roots. The general two-site impossibility follows from the all-positive-boundary-rate closed formula. Parameter robustness follows from continuity of finite irreducible Markov-chain stationary probabilities. No infinite-volume or unequal-hop-rate claim is tested or made.

Independent audit has not been performed.
