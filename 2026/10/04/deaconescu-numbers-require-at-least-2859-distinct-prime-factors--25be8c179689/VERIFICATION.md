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

The checker generates all primes through \(100000\) by an Eratosthenes sieve and splits them into the two nonzero residue classes modulo \(3\). The proof-critical comparisons are performed solely by exact integer cross-multiplication.

It certifies:
\[
2\prod_{j=1}^{2857}\frac{q_j-1}{q_j-2}<5,
\qquad
\prod_{j=1}^{2858}\frac{q_j-1}{q_j-2}<5,
\]
\[
\prod_{j=1}^{2858}\frac{s_j-1}{s_j-2}<3,
\qquad
\prod_{j=1}^{2859}\frac{s_j-1}{s_j-2}>3.
\]

It also verifies
\[
q_{2857}=56569,\quad q_{2858}=56599,\quad
s_{2858}=56081,\quad s_{2859}=56087.
\]

The finite certificate does not by itself prove the theorem. Exhaustiveness comes from the symbolic modulo-\(3\) classification and monotonicity argument in `RESULT.md`. A successful replay prints `VERIFY_OK`.
