---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The Gaussian exponential identity Im E exp((k+2πi)Z)=exp((k²-4π²)/2)sin(2πk)=0 for each nonnegative integer k proves μ+ and μ− are normalized nonnegative distinct lognormal Stieltjes laws with identical moments m_k=exp(k²/2). The shared fair latent sign S makes each row conditionally iid, and E(Y^k|S)=m_k; total variance is the conditional kth-power variance averaged over S divided by n, O_k(n^-1). Finite R truncated Ψ_R is a polynomial and every marginal has all finite moments, so a single K bounds the norm across rows. Conditional iid empirical convergence in expected W1 holds by finite first moment. The reverse triangle inequality then gives the exact limit E W1(μ_n,μbar)=W1(μ+,μ−)/2>0 because μbar=(μ++μ−)/2 and the one-dimensional CDF W1 formula. The claim does not cover independent unconditionally observed rows nor growing R.

## originality

PASS

Best-of-knowledge qualified PASS for the specific counterexample to weakening Amini–Vinas 2026 growing-order Ψ assumptions: the shared-sign construction yields all fixed empirical moment variances O(1/n) yet a fixed positive expected-W1 gap. The Stieltjes perturbations and the general moment-indeterminacy warning are classical and excluded from the novelty claim. A direct abstract moment-mixture argument makes this a narrow corollary-style contribution; its exact intersection of hypotheses and quantitative gap is not stated in the inspected 2026 primary theorem. Earlier implicit demonstrations remain possible.

## value

PASS

A precise, natural necessity boundary for an assumption in a current dependent-data empirical-Wasserstein theorem: uniformly controlling any fixed tail-moment order cannot replace controlled orders tending to infinity in the absence of determinacy. The result is not a free-floating toy obstruction: it preserves every fixed empirical-moment variance bound and gives a computable positive limiting transport gap. It does not claim the growing-order condition is individually necessary when other hypotheses are added.

The dated certificate retains the supplied scientific assessment, sources and limitations.
