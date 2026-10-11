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

The critical starting identity was checked against the Lyons–Zumbrun theorem and against formula (3) reproduced in the focal source. The focal paper's Theorem 1 and its first open problem were inspected directly.

For a multi-index \(\alpha=(a,2m_2,\ldots,2m_d)\), write \(q=m_2+\cdots+m_d\). Expanding the \(k\)-th Laplacian shows that only \(k=q+\ell\) can survive on \(re_1\), and the surviving coefficient factors as
\[
\left(\prod_{i=2}^d(2m_i-1)!!\right)
\frac{a!}{2^\ell\ell!(a-2\ell)!}.
\]
The remaining finite sum is the one-dimensional Lyons–Zumbrun expansion for \((D^qg)^{(a)}\). A transverse odd exponent leaves an odd residual power and therefore vanishes at the axis.

The Frobenius sum counts an unordered multi-index with multiplicity \(n!/\alpha!\). The resulting coefficient is
\[
\frac{n!}{(n-2q)!}
\sum_{m_2+\cdots+m_d=q}
\prod_{i=2}^d
\frac{1}{4^{m_i}}\binom{2m_i}{m_i}.
\]
Using
\[
\sum_{m\ge0}\frac{1}{4^m}\binom{2m}{m}z^m=(1-z)^{-1/2}
\]
gives
\[
\frac{n!}{(n-2q)!}
\frac{\prod_{k=0}^{q-1}(d-1+2k)}{2^q q!},
\]
which is algebraically identical to the stated \(\alpha^d_{n,q}\).

Exact symbolic sanity checks of this coefficient identity were run for \(1\le n\le8\) and \(2\le d\le6\), and polynomial radial examples were differentiated directly for several low orders. These checks are not used to justify the all-order result.

The proof is limited to smooth Euclidean radial functions and the Frobenius tensor norm. It does not claim a spectral theory for higher-order tensors or a non-Euclidean analogue.
