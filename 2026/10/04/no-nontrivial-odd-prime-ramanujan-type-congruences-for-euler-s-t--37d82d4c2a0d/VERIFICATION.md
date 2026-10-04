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

The checker tests every odd prime
\[
p\le19
\]
and every coprime pair
\[
1\le A,B\le35.
\]
It independently constructs the residue classes used by the proof, finds prime representatives by direct primality testing, and verifies the resulting identity
\[
m=An+B
\]
together with
\[
p\nmid\varphi(m).
\]

In the exceptional branch
\[
p\mid A,\qquad B\equiv1\pmod p,
\]
the checker additionally verifies that \(m\) is the product of two distinct primes and that neither prime is \(1\) modulo \(p\). In every other branch it verifies that \(m\) is prime.

The finite replay is a regression check, not the infinite proof. The all-parameter theorem is established symbolically in `RESULT.md` using the Chinese remainder theorem and Dirichlet's theorem.

A successful replay prints `VERIFY_OK`.
