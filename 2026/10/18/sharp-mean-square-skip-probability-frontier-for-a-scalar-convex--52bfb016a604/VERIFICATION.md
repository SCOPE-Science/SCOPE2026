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

For fixed \(p>0\), the Bernoulli update is exactly the two-matrix system displayed in `RESULT.md`. The standalone `verify.py` checks both equivalent symbolic Lyapunov identities, \(\det W(p)>0\)'s factorization, the critical root equation, and the determinant of the three-dimensional second-moment transfer map. It also enumerates all \(2^k\) update histories for \(0\le k\le6\), five rational probabilities, and three nonzero initial states, using exact rational arithmetic.

The script completed with `PASS: 111 exact algebraic / exhaustive finite-horizon consistency checks`. This verifies the formal algebra and finite-horizon specializations; it does not establish the infinite-horizon theorem by enumeration. Positive definiteness follows analytically from the two principal minors, and the all-iteration claims follow from the conditional Lyapunov identities. No numerical tolerance, heuristic fit, or automated independent review was used.

To reproduce, install `requirements.txt` and run `python verify.py` with an ordinary Python interpreter. Neither a cached result nor any external source file is required.
