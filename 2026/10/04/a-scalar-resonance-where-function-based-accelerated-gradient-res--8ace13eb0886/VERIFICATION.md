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

The proof is algebraic. For \(\lambda/L=5/8\) and \(\beta=1/3\), direct elimination of the momentum variable gives \(x^{k+1}=\tfrac12x^k-\tfrac18x^{k-1}\), with \(x^1=3x^0/8\). The characteristic roots are \((1\pm i)/4\), so their fourth powers equal \(-1/64\); hence \(x^{k+4}=-x^k/64\) for all \(k\).

`check.py` independently replays the recurrence using `fractions.Fraction`, verifies the first block, verifies the four-step identity over 80 updates, checks that \(|x^{k+1}|\le |x^k|\) always over that replay with the ratio pattern repeating, and checks that the gradient-restart sign is first positive at the update producing \(x^3\). The computation is finite verification of the displayed algebraic identities; the all-\(k\) statement rests on the characteristic-root proof, not on enumeration.

The literature check inspected the primary full text and the closest archive-era follow-up. Independent audit has not been performed.
