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

The proof in `RESULT.md` is the infinite argument. The verifier is an exact finite regression check.

It reconstructs the valuations of \(a_n\) through \(n=200000\). Because
\[
a_n=a_{n-1}(1+b_n),
\]
it stores only prime-adic exponents, so the calculation never relies on floating point or on truncating the enormous integers \(a_n\).

For every prime \(5\le p\le100000\), it checks
\[
b_{2p}=1\quad\Longleftrightarrow\quad b_{2p-1}=2p-1.
\]
It separately compares the observed event with primality of \(2p-1\) in the same finite range. That second comparison is not used as an infinite proof.

Run:

`python artifacts/verify.py`

The expected exact output is stored in `artifacts/verification_output.txt`.
