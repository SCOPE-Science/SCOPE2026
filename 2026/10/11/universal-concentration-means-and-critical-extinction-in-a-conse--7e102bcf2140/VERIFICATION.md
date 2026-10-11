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

The proof requires positivity and total-mass conservation, a logarithmic coboundary, two linear balance laws, an eventual lower bound for the supercritical concentration, and a critical convolution-ratio lemma. All hypotheses and limits are stated in RESULT.md, and the crucial analytic estimates are proved there rather than inferred from simulations.

Run \(\texttt{python verify_mean.py}\) after installing \(\texttt{sympy}\); the script asserts polynomial and rational identities for the exact four-species vector field and its equilibrium and prints \(\texttt{CHECK_OK}\) when successful. The symbolic replay performed on the embedded-file source returned this string. The checker verifies algebraic identities only; it does not serve as an independent formal proof of positivity, dominated convergence, global time averages, or mathematical novelty. A separate same-model correctness/originality/value review is recorded in REVIEW.md; no independent audit has been performed.

Known limits: the conserved-total parameter remains fixed, initial conditions must be strictly positive, and the \(O(T^{-1})\) estimate has an initial-condition-dependent constant. Bibliographic priority remains conditional on available literature and comparison of exact statements.
