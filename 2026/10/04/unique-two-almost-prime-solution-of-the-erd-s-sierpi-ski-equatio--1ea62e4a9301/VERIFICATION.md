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

The case partition is exhaustive for \(\Omega\le2\):
\[
1,\qquad p,\qquad p^2,\qquad pq.
\]
Prime endpoints and \(1\) are excluded directly. The even composite endpoint
is \(4\) or \(2p\), and \(4\) has prime neighbors. For \(2p\), the odd
neighbor is \(q^2\) or \(qr\). The four orientation/shape combinations reduce
to:
\[
(q-1)^2=0,
\qquad
q^2-2q+7=0,
\qquad
(q-2)(r-2)=3,
\qquad
(q-2)(r-2)=-3.
\]
Only the third has an odd-prime solution, namely \(q=3,r=5\), which gives
\(p=7\) and the pair \(14,15\).

The packaged checker independently computes \(\sigma\) and \(\Omega\) for
every integer through \(10^6+1\) and verifies that the only consecutive pair
in this multiplicative layer with equal divisor sums is \(14,15\).

The finite check is corroborative only and is not used to extend the theorem
beyond its tested range.
