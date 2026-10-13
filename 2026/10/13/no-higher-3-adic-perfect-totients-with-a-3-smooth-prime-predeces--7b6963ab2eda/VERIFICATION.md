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

The proof is exact and universal; the computation below is corroborative.

The attached `verify.py` first evaluates actual totient trajectories of
\[
2^A3^B
\]
and checks the closed formula
\[
2^{A-1}\left(3^{B+1}+1\right)-1.
\]

It then enumerates a finite rectangle of primes
\[
p=2^a3^b+1
\]
and directly evaluates the full iterated-totient sum of \(3^k p\). Every tested equality lies on the classical branch
\[
k=1,\qquad a=2.
\]
No tested parameter with \(k\ge2\) survives.

Finally, a larger exponent box checks the reduced equation
\[
2^a=3^k+1
\]
and finds only
\[
(a,k)=(2,1).
\]

The finite replay is not used to certify the infinite claim. The proof in `RESULT.md` supplies the complete quantifier argument.
