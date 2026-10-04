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
# Verification

For \(N=qM+r\), \(0\le r<q\), direct index inspection shows that the sparse correlation sum differs from the first \(M\) sampled terms by at most one term. If \(B=\sup_m|b_m|\), the omitted-or-added contribution is bounded by \(B\|\varphi\|/N\), while changing the denominator from \(N\) to \(qM\) contributes a bound of order \(1/N\). Both vanish uniformly for fixed \(b\) and \(\varphi\). Repeating the same comparison for \(|a_n|\) and \(|b_m|\) verifies preservation of non-triviality.

Thus the correlation limsups differ by exactly the factor \(1/q\), which proves the correlated-point set identity without approximation assumptions. For the entropy consequence, Lemma 2.11(3) of Hou--Lin--Tian, arXiv:2604.05713v1, states the subset power law \(h_{\mathrm{top}}(f^q,Y)=q\,h_{\mathrm{top}}(f,Y)\) for every subset \(Y\). Applying it to the exact correlated set completes the argument.

No numerical experiment, finite enumeration, or external certificate is required. The proof does not establish a converse from an iterate to the original map.
