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
The symbolic proof was checked from the closed-neighborhood identities
\[
|N[a_i]\cap S|=q+\mathbf 1_{i\in P}-\mathbf 1_{i\in Q},
\qquad
|N[b_i]\cap S|=p+\mathbf 1_{i\in Q}-\mathbf 1_{i\in P}.
\]
The only side-size value below \(k\) compatible with all inequalities is the \(k=1\) full-side exception. At \(q=k\), feasibility is exactly \(Q\subseteq P\); at \(p=k\), it is exactly \(P\subseteq Q\). For larger side sizes the corresponding inequalities are automatic.

`checker.py` exhaustively tests every subset of \(\operatorname{Cr}_n\) for \(3\le n\le8\) and every \(1\le k\le n\). It verifies the iff criterion, the bivariate and univariate coefficient tables, and the claims \(\gamma_{\times k}=2k\) and \(m_k=\binom nk\). Its expected terminal line is:

`VERIFY_OK n_range=3..8 k_values=33 subset_checks=669888 criterion_checks=669888 bivariate_checks=199684 coefficient_checks=546 minimum_checks=33 max_order=16`

No finite computation is used to justify the infinite theorem. The literature comparison is limited by normal bibliographic coverage and does not constitute a proof of global uniqueness.
