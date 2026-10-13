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

The unrestricted proof is symbolic and appears in `RESULT.md`.

For the prime-square branch, the proof uses
\[
S(r^2)=r,
\]
the congruence modulo \(9\), and the monotone inequality
\[
r\le9(2\log_{10}r+1).
\]
This leaves only \(r=3,19,37\), all checked directly.

For the distinct-prime branch, the only alternative to the claimed identity is
\[
S(pq)=q.
\]
The same size bound gives \(q\le37\), and reduction modulo \(9\) leaves only
\[
(p,q)=(19,23),(19,29),(19,31),(19,37)
\]
after the small \((2,3)\) case. Their digit sums are checked directly.

The packaged checker also enumerates every integer through \(10^6\) with
\(\Omega(n)=2\). It confirms that exactly \(1617\) are Moran numbers and that
every one is squarefree with digit sum equal to its least prime factor.

The finite sweep is corroborative only. The infinite classification and the
zero-density theorem use the symbolic proof and standard asymptotic estimates.
