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

Failure of standard JR is exactly the existence of an outside candidate approved by at least r=ceil(n/k) unrepresented voters: such voters themselves form a violating group, and any violating group's common candidate must be outside the committee. The unrepresented set is determined by elected columns alone; its size U is Bin(n,q_W). Given that set, independent outside columns give Bin(U,p_c) counts, so the conditional no-violation probability is the specified product of lower tails, depending only on U. This gives the exact mixture, including q_W=0 or 1, endpoint probabilities, U=0 and the empty product at m=k. For a swap of a lower-probability winner with a higher-probability outsider, couple by common uniforms, aligning the old and new winner columns and aligning the two outside columns. The newly unrepresented voter set is contained in the old one, and each outside approval set is contained in its old counterpart or unchanged. Thus success cannot decrease, proving the finite-n maximizer, including ties, without any independence assumption on the unconditional violation counts. Rational evaluation is polynomial in numerical n, m and rational bit lengths: the supplied binomial-sum count is O(mn²) arithmetic operations and every full-mixture probability admits common denominator ∏_c d_c^n for probability denominators d_c. This is not a polynomial-time claim in log n for a succinct input with output written in full. For an outsider to a top-k committee, the per-voter violation probability is a=p_c q_W≤p_c(1−p_c)^k≤a_k<1/k. Chernoff at 1/k and the union bound give the stated uniform finite-n bound. At equal probabilities 1/(k+1) one outsider attains a_k, and the single mass at ceil(n/k) has logarithmic rate D(1/k||a_k) by Stirling for k>1. When k=1 the tail is exactly 4^(−n); the lower bound uses an outsider, so requires m>k. Squeezing for fixed m>k proves the limit after the supremum. Independently, the example's failure numerator is 6·31²+4·31+1=5891 over 32⁴, as stated.

## originality

PASS

The supported distinct contribution is the exact conditional-size formula with all-finite-n top-k optimality in the homogeneous-by-voter heterogeneous-by-candidate class, together with the explicit uniform limiting rate. The existing JR definition, conditionally independent outsider calculation for deterministic elected columns, common-p maximization, and heterogeneous top-k exponential guarantees are credited below. The sharp exponent is especially close to a synthesis of prior bounds and textbook binomial tails; it is not treated as a wholly new probabilistic method or the sole basis for acceptance. No inspected result covers the exact finite-n mixture and selection theorem together.

## value

PASS

Exact JR probability and MaxJR are naturally motivated by the general uncertain-voting problems. The result isolates a tractable nontrivial homogeneous-by-voter class and gives a one-dimensional exact calculation and a deterministic sorting rule that is optimal already at finite sizes, without treating positively correlated witness counts as independent unconditionally. The sharp worst-case rate quantifies, rather than replaces, this finite-n guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
