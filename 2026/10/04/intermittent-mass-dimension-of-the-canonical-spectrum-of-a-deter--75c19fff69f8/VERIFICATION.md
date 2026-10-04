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

The claim is verified analytically from the explicit canonical spectrum in arXiv:2609.22772v1.

The critical proof checks are:

1. Mixed-radix uniqueness: a level digit difference has magnitude strictly smaller than its radix, so reduction modulo successive \(N_j\) forces equality digit by digit.
2. Exact stage size: \(\#\Lambda_n=\prod_{j\le n}M_j\).
3. Exact radius formula and uniform scale comparison:
\[
R_n=\frac12\sum_{j\le n}P_j\left(1-\frac1{M_j}\right),
\qquad
\frac49P_n\le R_n<\frac{27}{52}P_n.
\]
4. Stage isolation: the next center spacing \(G_{n+1}=P_nh_{n+1}\) satisfies \(G_{n+1}>3P_n>2R_n\), and later stages are farther away.
5. Completed-stage growth: last-scale domination from \(N_{n+1}>P_n^{\,n+1}\), together with \(r_n/q_n\to s\), gives \(\log A_n/\log P_n\to s\).
6. Sparse subsequence: because \((q_n-r_n)/q_n\to1-s>0\), the gaps before the next stage have logarithmic size much larger than \(\log P_n\), forcing the centered counting exponent to zero along a subsequence.
7. Between-stage control: only equally spaced level-\(n+1\) clusters enter before \(R_{n+1}\), and counting those clusters bounds every intermediate logarithmic exponent by a quantity whose endpoint tends to \(s\).

No finite enumeration, numerical fitting, timeout, or experimental failure is used to establish the infinite statement. The proof does not cover \(s=1\), arbitrary spectra, Beurling dimension, or lower discrete Hausdorff dimension.
