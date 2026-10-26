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

# Verification and limits

The proof uses published opinion convergence and confidence dichotomy from Li, Luo, and Porter (arXiv:2303.07563v3, Theorem 5), then a newly verified predictable-time sampling lemma. Formally, for filtration \(\mathcal F_t\) before draw \(U_t\), \(A_e(t)\in\mathcal F_t\) and \(\mathbb P(U_t=e\mid\mathcal F_t)=1/|E|\). The conditional Borel–Cantelli conclusion links infinitely many receptive time steps to infinitely many selected receptive interactions. A confidence-zero edge admits only finitely many selected receptive events, because each restores confidence to at least \(\gamma>0\). A confidence-one edge has vanishing opinion gap, so it becomes persistently receptive. Both edge classes are exhausted by the source's theorem; finiteness of the edge set supplies a common almost-sure finite stabilization time.

A standalone, standard-library-only `verify.py` was executed from the package's current paths with the result:

```
VERIFY_OK exact_rational_transitions=250 exact_fixed_updates=800 stochastic_steps=12000
```

It verifies exact rational state-transition identities, opinion-sum conservation, quadratic-energy decrements, confidence reset inequalities, an exact permanently receptive/blocked path example, and randomized boundedness/conservation checks. These finite calculations verify local formulas and example behavior only. They do not certify the infinite-time almost-sure theorem, which is established analytically. General bibliographic independence and expert audit have not been performed.
