---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The exponential-family identity q∂E_q F/∂q=Cov_q(F,J) holds term-by-term for finite permutations, and q∂E_q J/∂q=Var_q(J)>0. At q=1 the fixed-point versus inversion-indicator covariance for a<b is (a−b)/[n(n−1)], and summing gives −(n+1)/6. At identity the n−1 adjacent swaps each destroy two fixed points, first Taylor coefficient c=−2(n−1). At reversal, only two central-adjacent swaps destroy one fixed point each for odd n (c=−2), while the central adjacent swap creates two for even n (c=+2). The q-factorial Mahonian level coefficients obey a_k<=n^k; |F−F_extreme|<=2k under k adjacent swaps bounds |b_k|<=2k a_k. Geometric series at x<=1/(100 n²) give uniform derivative error <1 while |c|>=2, so the derivative sign is certified for all n; reverse-bias x=1/q reverses the covariance sign. The n3 exact rational identity follows from complete six-permutation enumeration. Independent enumerations for n2..8 exactly reproduce unbiased and both cutoff signs. Continuity and positivity ensure odd-n covariance crossing and a local minimum, but not uniqueness beyond n3.

## originality

PASS

Prior Mallows permutation cycle theory includes fixed-point expectations and pronounced odd/even effects in n→infinity asymptotics. The 2024 MathOverflow discussion explicitly asks whether expected fixed points decrease with expected inversions, conjectures a monotonic response and notes uniform conditional-inversion counterexamples; it does not supply the stated finite-n Mallows high-bias covariance reversal. The new result gives a uniform explicit all-odd-n counterfamily and rigorous quantitative cutoff, beyond qualitative parity asymptotics.

## value

PASS

The fixed-point/inversion relation was explicitly posed as an unresolved monotonicity question in 2024. An exact counterfamily for every odd size, with a rigorous uniform polynomial high-bias bound, is a meaningful structural answer and identifies a parity-dependent sign reversal. It is not a tiny exceptional n3 example and does not infer finite-n behavior from asymptotic experiments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
