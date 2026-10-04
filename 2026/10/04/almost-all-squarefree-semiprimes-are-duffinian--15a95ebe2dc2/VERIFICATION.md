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

The unrestricted proof is in `RESULT.md`.

The exact finite checker `verify.py` uses a standard sieve to enumerate every
squarefree semiprime \(pq\le10^6\) with \(p<q\). For each pair it computes
\[
\sigma(pq)=(p+1)(q+1)
\]
and verifies that
\[
\gcd(pq,\sigma(pq))=1
\]
is equivalent to
\[
p\ne2\quad\text{and}\quad q\not\equiv-1\pmod p.
\]

The checker also reports counts at \(10^4\), \(10^5\), and \(10^6\). These
counts only test the exact finite criterion and illustrate the slowly declining
exceptional proportion. They do not certify the asymptotic theorem.

The analytic proof uses:
1. Brun--Titchmarsh for \(p\le x^{1/3}\);
2. the elementary prime-counting upper bound and a bounded reciprocal-prime sum
   for \(x^{1/3}<p<\sqrt{x}\);
3. Landau's asymptotic for integers with two prime factors.

No effective constant in the \(O(x/\log x)\) term and no secondary asymptotic
constant are claimed.
