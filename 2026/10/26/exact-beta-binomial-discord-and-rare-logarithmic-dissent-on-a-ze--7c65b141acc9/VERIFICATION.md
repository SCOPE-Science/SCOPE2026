---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The lumped Markov generator has transitions (0,k)→(0,k-1) at rate k and (0,k)→(1,k) at (k+1)/(m+2), and complementary (1,k) analogues. Positive hub-flip rates make the labeled chain irreducible. Zero net flux across count cuts forces (k+1)a_(k+1)=(m-k)b_k, global complement symmetry b_k=a_(m-k), giving beta-binomial recurrence with alpha=1/(m+3); Vandermonde normalizes each hub mass to 1/2. Factorial moments give E[M]=m/(m+5) and Var[M]=m(m+1)/(2(m+5))−(m/(m+5))². The product form yields uniform P(M=k)=(alpha/k)(1+O(alpha H_m)) and P(M>0)=alpha H_m(1+O(alpha H_m)), hence conditional harmonic law, uniform log M/log m and conditional mean m/log m. I independently implemented rational stationarity and factorial-moment tests m=1..8 and large-m rare-tail diagnostics; finite checks are not substituted for the analytic recursion and uniform product estimates.

## originality

PASS

PASS with caveat. General stubborn-agent moment duality and classical beta-binomial distributions are known; Mori et al. Appendix B is a complete graph with different update neighborhood, not the exactly pinned heterogeneous star. The full finite-star law and harmonic conditional rare-event asymptotics are not given by inspected specific theorems.

## value

PASS

Rare but macroscopic bursts of follower dissent despite expected dissent approaching one and typical zero are a meaningful stochastic-network phenomenon. The complete conditional joint hub/count distribution and logarithmically uniform dissent size quantify a natural pinned-star mechanism beyond standard marginals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
