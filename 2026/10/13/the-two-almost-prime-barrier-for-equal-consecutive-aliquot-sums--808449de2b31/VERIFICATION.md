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

The proof is symbolic and does not depend on computation. It classifies every integer with \(\Omega\le2\) as \(1\), a prime, a prime square, or a squarefree semiprime, then checks every possible type pairing for two consecutive integers.

The semiprime/semiprime step is exact: from equal aliquot sums and consecutive products,
\[
p+q=u+v,\qquad uv-pq=1.
\]
After ordering the prime factors, fixed-sum product monotonicity gives \(u>p\). Writing \(t=u-p\) gives
\[
1=t(q-p-t),
\]
forcing \(u=v\), contrary to squarefreeness.

`verify.py` evaluates the theorem independently through \(n=200000\). It factors each integer, computes \(\Omega\) and \(\sigma(n)-n\), and tests every adjacent pair satisfying the multiplicity hypotheses. The expected replay output is stored in `VERIFY_OUTPUT.txt`.

Finite verification cannot establish the unbounded theorem and is not used as a substitute for any proof step. No assertion is made for a pair in which either integer has \(\Omega\ge3\).
