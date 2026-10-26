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

# Verification record

The proof was checked against the original arXiv HTML statements and their exact quantified hypotheses. The following deterministic identities were explicitly reconstructed:

1. For Bernoulli selectors of probability \(\pi\), \(\mathbb E B_N=\pi A_N\) and \(\mathbb E B_N^2\le\pi A_N^2\), giving a uniform Paley--Zygmund survival probability \(\pi/4\).
2. With \(c=(\pi/4)(\pi/2)^{q/2}\), the integrated selector norm satisfies \(0\le V_N\le U_N\) and \(\mathbb E V_N\ge cU_N\); therefore \(\mathbb P(V_N\ge(c/2)U_N)\ge c/2\), independently of degree.
3. For \(0<q<2\), the block weights satisfy the exact deterministic budget \(\sum_{j\ge1}2^{-j}=1\), while the chosen random event forces the block contribution to be at least \(2^{-j}(2^{2j/(q/2)})^{q/2}=2^j\). Summability of failure probabilities permits Borel--Cantelli.
4. The selected blocks contain finite index sets from \(I_{k_j}\) with \(\#I_{k_j}\ge N_j\), and the resulting coefficients yield a Dirichlet series converging absolutely for all \(\operatorname{Re}s>1\).
5. The independent-copy difference retains symmetry and nondegeneracy, including when the original variable is not centered; if \(\mathbb E|X|^2=\infty\), it also has infinite second moment.

The analytic proof covers all parameter values in the theorem; no truncated experiment is used as an infinite certificate. The cited supporting statements are arXiv:2610.17876v1, Theorems 3.1, 3.4, 3.5 and Lemma 3.3, and arXiv:2402.00314v1, Theorem 1.6. The full text of the related ordinary Taylor-series 2026 work was not available; only its abstract was compared. No independent audit or independent validation has occurred.
