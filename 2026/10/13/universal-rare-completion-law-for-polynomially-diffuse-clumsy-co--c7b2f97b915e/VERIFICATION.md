---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Under product stationarity, choosing the unique absent coordinate and refreshing it to 1 contributes w_i p q^n to the entrance flux. From all present, given the touched set U after r draws, its last refresh bits are independent; the same calculation on U gives p q^|U| sum_{i in U} w_i. Counting designated repeats for r≤d=floor(1/(64 w_+)) bounds the probability of fewer than r/2 distinct indices by 4^(−r); after d the touched set can only grow. These bounds give a sum of return-entrance probabilities over b=ceil(n^(B+4)) steps bounded by O(w_+) plus a polynomial times exp(−Ω(n^γ)), uniformly. By the Markov property after an entrance, this makes the factorial second moment in a stationary block o(bμ), proving the one-block probability bμ(1+o(1)). The shared-refresh coupling after h=ceil(H n^(B+1)) steps has TV error at most n exp(−cHn)=o(bμ); this applies to the whole next-block event even conditional on preceding failed blocks. Gaps and the incomplete terminal block have negligible expected stationary entrance count, and from empty a burn-in visit has probability at most h q^n. The product of conditional block survival probabilities therefore tends to exp(−t). In blocks of h+b steps every starting state has hit probability at least bμ/2, yielding a uniform scaled exponential tail and uniform integrability for each fixed moment. Uniformity is over the row vectors satisfying the specified inequalities at n. The Zipf profile has minimum of order n^(−1) and maximum of order n^(s−1) for fixed s<1; the exceptional coordinate's union bound is (x/p)exp(−(θ+log q)n) at time x/μ. The frozen checker was inspected and an independent small rational check agreed with the flux and exact touched-set identity; neither checks the asymptotic bounds.

## originality

PASS

The exponential scale and fixed-moment law for uniform draws are prior. The supported distinction is the uniform nonuniform-weight theorem: a scalar missing-count chain cannot provide its block probability, and the new touched-set return estimate does. The general block theorem assumes this input. The strongest distinct indexed match gives an exact finite transform for the same process but not a uniform asymptotic estimate; extracting one requires a new weighted small-denominator and tail argument. No equivalent existing asymptotic claim was established in the inspected evidence.

## value

PASS

The extension preserves an exact time scale and all fixed moments for a wide range of uneven frequencies, including fixed Zipf profiles, despite loss of the uniform model's count-chain reduction. The touched-set estimate resolves the consequential short-return issue, and the exponentially rare coordinate delineates a real obstruction rather than an arbitrary numerical cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
