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
Run `python3 verify.py`.

The verifier constructs all twenty three-element subsets of
\[
\{1,2,p,2p,q,2q\}.
\]
For each subset it extracts coefficients \(a,b,c\), forms
\[
C=(a+3)(b+3)+c+3,
\]
enumerates every positive divisor \(u\mid C\), and reconstructs
\[
p=b+3+u,\qquad q=a+3+\frac{C}{u}.
\]
It retains only ordered odd-prime pairs \(p<q\) satisfying the original deficiency equation.

The resulting prime pairs are exactly
\[
(5,13),(7,11),(5,17),(7,13),(5,29),(7,31).
\]
The checker then recomputes \(\sigma(2pq)\), verifies each displayed deficient-divisor triple, and confirms the six integers
\[
130,154,170,182,290,434.
\]

As a separate regression check, it also brute-forces all odd prime pairs below \(1000\) and obtains the same six pairs. That bounded check is not used for exhaustiveness; the twenty factorization cases are the proof.

A successful replay prints `VERIFY_OK`.
