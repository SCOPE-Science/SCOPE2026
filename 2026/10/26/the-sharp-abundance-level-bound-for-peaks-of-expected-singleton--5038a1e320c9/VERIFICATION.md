---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Indicator linearity gives s_n=n sum_i p_i(1-p_i)^(n-1). Group equal values q_j and extend to S(t)=t sum_j c_jq_j/(1-q_j) e^{t log(1-q_j)}. S’ is an exponential polynomial with L distinct real rates and polynomial multipliers of degree at most 1. Repeated Rolle differentiation proves at most 2L-1 real zeros counting multiplicity, so k strict integer maxima force at least 2k-1 derivative zeros and k<=L. For sharpness use p_j=eps^{2^{j-2}} (j>=2), p_1=1-sum p_j: initial n=1 peak, and L-1 separated scales n~1/p_j where a single species contributes e^-1, with vanishing intermediate valleys. Choosing sufficiently small transcendental eps avoids all adjacent ties because s_{n+1}-s_n is a nonzero polynomial for each integer n. Independent arbitrary-precision exact integer sign checks verified all neighboring inequalities of the explicit vector (9899,100,1)/10000 at n=1,102,9999; the all-L statement relies on the analytical construction.

## originality

PASS

Qualified PASS: the Chebyshev zero-bound and sampling expectation are established tools; the sharp abundance-level strict-peak count and L-scale realizability are a natural, apparently uncovered specialization, with full-text risk for nearby mixture literature.

## value

PASS

Expected observed-once species count is a standard sampling diagnostic. A sharp bound on how often its expectation can reverse with sampling effort, controlled by the number of abundance levels rather than number of species, answers a natural shape question and gives explicit extreme examples useful in sampling design and interpretation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
