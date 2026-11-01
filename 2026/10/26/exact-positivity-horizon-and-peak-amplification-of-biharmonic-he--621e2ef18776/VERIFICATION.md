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

The complete-graph Laplacian L(K_a)=a V_a with V_a=I-J_a/a and U_a=J_a/a. Tensor spectral projections U_a⊗U_b, V_a⊗U_b, U_a⊗V_b, V_a⊗V_b yield L eigenvalues 0,a,b,a+b and thus exactly four kernel equality classes. Three classes are strictly positive for every t>0; only vertices differing in both coordinates have entry F_ab/(ab), negative immediately since F_prime(0)=-2ab. Writing H(t)=exp(b^2 t)(1-exp(-a^2 t))/(1-exp(-(a^2+2ab)t)), its logarithmic derivative b^2+a^2/(exp(a^2t)-1)-(a^2+2ab)/(exp((a^2+2ab)t)-1) is positive because u/(exp(ut)-1) decreases with u. H(0+)=a/(a+2b)<1 and H(infty)=infty, so exactly one cutoff. Every row sums to one, with precisely (a-1)(b-1) potentially negative entries; its absolute row sum proves the norm formula. Multiplying F_prime by exp((a+b)^2t) gives a strictly increasing exponential equation with one positive root, giving a unique peak before cutoff. At a=b=m, factor 1-2z+z^4=(z-1)(z^3+z^2+z-1), derive tau=-log(z*)/m^2, theta=log2/(3m^2), max gain as stated. For fixed a and b large, y=b²t and delta=a/b expansions at the unique monotone zero and peak prove y_cut=log(2b/a)+O_a(log b/b), y_peak=1+O_a(1/b), max gain=4(a-1)/(eb)+O_a(b^-2). Independently computed five explicit small rook-graph matrix exponentials, entries, negativity and norm; infinite statements rely on analytic monotonicity and uniform expansions.

## originality

PASS

Best-of-knowledge originality for the stated final claim after direct comparison of prior implications and source materials; foundational methods, source models and matching components are explicitly credited. Exact positivity horizon and peak amplification of biharmonic heat on rook graphs is not inferred new merely because an exact phrase search fails. Unindexed equivalent publications remain a disclosed risk.

## value

PASS

Fourth-order heat semigroups need not preserve positivity or maximum principles. Rook graphs are natural Cartesian products/line graphs with a complete four-level spectral decomposition. An exact worst-case maximum-coordinate norm and sharp eventual-positivity threshold for every rectangular parameter, including unusual logarithmic thin-board scaling, provide a motivated structural classification of transient positivity defects beyond general eventual-positivity existence criteria.

The dated certificate retains the supplied scientific assessment, sources and limitations.
