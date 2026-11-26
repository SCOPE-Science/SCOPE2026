---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Independent uniform parent and pre-existing removal draws give offspring type-1 probability x+μ(1−2x), x=k/n; multiplying with the opposite removal probabilities gives the two stated off-diagonal entries. Reflection is legitimate by allele symmetry. At the top it adds both jump probabilities when n is even and makes the original upward jump a hold when n is odd. Below the top p+q is at most 1−2x(1−x)<1, so holding is positive, and downward probabilities are positive even at μ=1. Finiteness and positive descending paths give eventual absorption with a geometric upper bound. By skip-free motion and the strong Markov property, starting one step higher adds a nonnegative first-passage time in distribution, so each survival vector is nondecreasing with initial minority count. The derivative D favors up over down on those vectors, with zero top row for even n and a nonnegative action at the odd top. Differentiating Q^t gives the sum of nonnegative terms; since D1 has first component (1−2/n)/n>0 for n>=3, the j=0 term reaches any r by t>=r using r−1 downward steps and arbitrary positive holds. Hence survival is one for t<r and strictly increasing in μ at every other horizon, endpoints included by integration. Summing finite means proves strict mean ordering. The primitive killed matrix has simple Perron root in (0,1). Its positive right Perron vector is a limit of rescaled nondecreasing survival vectors, so Dv is nonnegative with first component at least (1−2/n)v_1/n>0. The simple-root derivative w^T Dv/(w^T v) is therefore positive, including one-sided endpoint derivatives; the left and right Perron vectors give the positive survival prefactor. The one-state matrices at n=2 and 3 yield respectively 1/2 and (7+μ)/9. An independently written integer replay on the full allele count (python3 /workspace/branches/frozen_math_replay.py 5) used literal ordered individual draws and mutation weights; 1872 adjacent-rate comparisons passed, n=2..9, μ=j/4, t=0..12, including both small-size formulas. The reported exact-rational checks of the inspected supplied script cover other finite cases; the Perron conclusion is established by the proof, not by either computation.

## originality

PASS

Gaeta treats exactly the update and first entrance in this record, and already reports the mean trend. The defensible distinct contribution is pointwise strict ordering at every reachable finite horizon, with its exact onset, and positivity of the mutation derivative of the reflected killed-chain Perron root. These do not follow from the prior mean recursion or from general state hitting and stationary analyses in the inspected results.

## value

PASS

In a natural finite neutral model, strict comparison of the whole first-homogeneity law is stronger than comparison of its mean. It holds for the entire flip range even though mutation increases the probability of any allele-count change away from the central count. The order starts exactly at the first reachable horizon and has a sharp population-size boundary. The strict Perron derivative also resolves sensitivity of the asymptotic survival scale, which does not follow just from ordering finite horizons. This is about temporary pure-state entrance and does not claim biological fixation in a system with continuing mutation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
