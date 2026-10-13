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

The theorem is established by an analytic block-incidence argument.

For one complete matching, the inspected source gives
\[
A_u=\frac{n_u^2+c_u}{16}.
\]
The verification of the new step is purely combinatorial: if \(m\) is the largest block size and \(C\) is the number of matching edges crossing blocks, then
\[
\sum_u c_u=2C\le
\begin{cases}
N,&m\le N/2,\\
2(N-m),&m>N/2.
\end{cases}
\]
The second branch follows because every crossing matching edge must consume a distinct vertex outside a largest block.

For \(k>N/2\), maximizing the resulting expression gives
\[
k^2+(N-k)^2+2(N-k).
\]
For \(k\le N/2\), the source's original partition extremum remains \(qk^2+s^2+N\). The source's QFI triangle inequality then recombines the two complete matchings.

`artifacts/verify.py` enumerates every integer block-size partition for even \(N\le30\) and confirms the closed-form combinatorial maximum for all \(k\) in that finite range. It also checks that the new numerator is strictly smaller than the source numerator exactly when \(k>N/2\), and that it equals \(N^2\) at \(k=N\).

The enumeration is not an exhaustive proof for arbitrary \(N\); it is a finite consistency check of the independently proved formula. No claim of tightness of the physical QFI maximum is made.
