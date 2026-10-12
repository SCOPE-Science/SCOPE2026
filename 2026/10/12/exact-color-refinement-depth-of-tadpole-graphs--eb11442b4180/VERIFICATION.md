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
The theorem was checked by a standalone implementation of ordinary color refinement.

For every pair
\[
3\le m\le50,\qquad 1\le k\le80,
\]
the checker constructs \(T_{m,k}\), runs refinement from the uniform coloring until the first repeated partition, and compares the observed depth with
\[
\max\left\{
\left\lfloor\frac m2\right\rfloor,\,
\left\lceil\frac k2\right\rceil,\,
\min\{m,k\}
\right\}.
\]
For the same \(3840\) pairs it also verifies the critical lower-bound witness: a cycle neighbor of the attachment vertex and the tail neighbor split for the first time exactly in round \(\min\{m,k\}\).

Finally, for each total order \(4\le N\le100\), the checker maximizes the formula over all admissible \(m+k=N\) and verifies the fixed-order extremum \(1\) at \(N=4\) and \(\lfloor N/2\rfloor\) for every \(N\ge5\).

The checker returns:

`VERIFY_OK depth_checks=3840 cross_witness_checks=3840 order_checks=97 m=3..50 k=1..80 N=4..100`

The computation is finite corroboration. The all-parameter theorem is established by the universal-cover proof in `RESULT.md`.
