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

The proof uses Maithani--Singh--Watanabe, arXiv:2609.32003v1, Theorem 2.8, in the form
\[
b(S^G)=d-2c-n
\]
for characteristic different from \(2\). In the diagonal action with \(r\ge2\), direct support counting gives \(c=0\) and \(n=rm\).

For odd \(r\), the monomial stabilizer is alternating exactly when the exponent columns are pairwise distinct. The count of weight-\(s\) columns is \(\binom{s+r-1}{r-1}\), and the two identities used are
\[
\sum_{s=0}^{q-1}\binom{s+r-1}{r-1}=\binom{q+r-1}{r}
\]
and
\[
\sum_{s=0}^{q-1}s\binom{s+r-1}{r-1}=r\binom{q+r-1}{r+1}.
\]
These yield the stated minimum degree and hence the exact \(b\)-invariant.

At \(m_0=\binom{2r+1}{r}\), the cumulative shell ends at weight \(r+1\) and the weighted sum equals \(rm_0\), so \(b=0\). Before this point the running value is negative; every subsequent added exponent column has weight at least \(r+2\), so the value becomes and remains positive. The first increment is \(2\).

Consistency checks: \((r,m)=(3,36)\) gives \(q=5\), \(d=110\), and \(b=2\), exactly matching the motivating source. The next odd-copy threshold is \(r=5\), \(m=463\), again with first positive value \(b=2\). No finite experiment is used as a proof of the arbitrary-parameter statement.
