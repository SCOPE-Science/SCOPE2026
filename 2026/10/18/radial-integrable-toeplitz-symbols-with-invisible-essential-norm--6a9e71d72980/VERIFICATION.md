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

# Verification and reproducibility

The main claim is analytic and concerns a real radial integrable symbol on the standard Bergman disk. Its decisive checks are:

1. Direct gamma integration proves the inverse-Laplace identity and exact positive diagonal profile \(\Phi_N\).
2. The integral-norm estimate \(\|h_N\|_1\le8^N/2\), together with the scale definition, proves global \(L^1\) convergence and arbitrarily small symbol mass.
3. Geometric separation of the integer scales bounds the entire eigenvalue sum by \(128/15\) and leaves eigenvalues of size at least one along infinitely many degrees.
4. The unimodal mesh comparison and the beta integral prove \(\sup B_{N,K}\le16/\sqrt N+12/K\). Summability across \(N_j=(j+1)^4\) and termwise convergence of the individual compact operators' Berezin transforms proves boundary vanishing for the full operator.
5. The operator-norm limit of the compact pieces is **not** assumed; the argument uses \(L^1\) convergence of symbols and diagonal boundedness instead.

Run `python3 check_formulas.py` using the adjacent standalone source. The checker exercises 333 deterministic *exact rational* assertions: binomial Laplace identities for nine orders and six positive rational arguments, beta bounds, peak normalization, positivity, and finite truncated Berezin sums over six scales and five radii. The completed run reported `PASS 333 finite exact rational assertions`. These finite checks are not proofs of the infinite assertions; the precise infinite argument is in `RESULT.md`.

Scientific limitations: no bound is claimed to be the optimal constant; only the unweighted disk and signed radial symbols are covered. The provenance comparison is a same-model analysis of identified primary literature and does not constitute independent validation or an exhaustive priority determination.
