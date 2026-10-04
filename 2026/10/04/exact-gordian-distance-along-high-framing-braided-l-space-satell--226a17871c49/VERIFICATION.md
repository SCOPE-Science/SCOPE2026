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

The claim reduces to matching lower and upper bounds.

For the lower bound, the published high-framing formula is
\[
\tau(P(K,n))=g_3(P)+\frac{p(p-1)}2n+p\tau(K),
\]
for the \(p\)-strand braided case under the stated hypotheses. Therefore
\[
|\tau(P(K,m))-\tau(P(K,n))|
=\binom{p}{2}|m-n|.
\]
The standard crossing-change cobordism and the four-ball genus bound on \(\tau\) imply
\[
d_G(A,B)\ge|\tau(A)-\tau(B)|.
\]

For the upper bound, one unit of framing is one full twist \(\Delta_p^2\). The factorization
\[
\Delta_p^2
=A_{12}(A_{13}A_{23})\cdots(A_{1p}\cdots A_{p-1,p})
\]
has exactly
\[
1+2+\cdots+(p-1)=\binom{p}{2}
\]
factors. Each \(A_{ij}\) is conjugate to \(\sigma_i^2\), and one crossing change turns the central square into a canceling pair. Hence a full twist costs at most \(\binom{p}{2}\) crossing changes. Repeating for \(|m-n|\) unit framing changes gives the matching upper bound.

No computational enumeration is needed. The proof establishes the theorem for every integer \(p\ge2\) and every pair of integer framings in the stated range. It does not establish any statement below the threshold or for other move metrics.
