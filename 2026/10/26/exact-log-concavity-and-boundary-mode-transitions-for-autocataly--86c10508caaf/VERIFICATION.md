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

# Analytical and finite verification

Analytically, the source generator gives the stationary ratio \(R_k\). The identity \(R_k/R_{k-1}=F_k(a)F_{n-k}(b)\) makes all nonboundary comparisons strictly log-concave and reduces the full theorem to the first and last two cells. The root's uniqueness, population-uniform limit, reflection symmetry and leading asymptotic are established in the included proof; they are not inferred from numerical scans.

Run `python verify.py` using Python 3 with no external packages. The program computes exact rational unnormalized stationary weights and direct ratios for all \(2\le n\le24\) over a nontrivial grid of positive rational parameters, comparing every local inequality to the theoretical criterion. It explicitly checks odd-length central plateaus and boundary local peaks for \(4\le n\le31\), and numerical root brackets and large-size asymptotic spot checks. The recorded output from the included script is:

`PASS: 114964 exact finite checks and root/asymptotic spot checks`

Scope: exhaustive only over the indicated finite parameter grid; exact infinite-parameter statements rest on the proof. Independent audit and independent validation were not performed.
