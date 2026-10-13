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

The universal argument is analytic and does not depend on finite enumeration.

The attached `verify.py` first sieves all primes needed for an exhaustive check of odd squarefree semiprimes
\[
pq\le2\,000\,000.
\]
For every such pair \(p<q\), it computes
\[
\Phi(pq)=\bigl(p-\beta(p)\bigr)\bigl(q-\beta(q)\bigr)
\]
and verifies exactly that
\[
\gcd(pq,\Phi(pq))>1
\quad\Longleftrightarrow\quad
p\mid q-\beta(q).
\]

It then reports the exact number of tested semiprimes and exceptional pairs.

Separately, the script sieves primes through
\[
10^7
\]
and computes the partial sum
\[
C_{10^7}=\sum_{\substack{3\le p\le10^7\\p\ {\rm prime}}}\frac1{p(p-1)}.
\]
The omitted prime tail is bounded by
\[
0<
C-C_{10^7}
<
\sum_{m>10^7}\frac1{m(m-1)}
=
10^{-7}.
\]
This certifies the six-decimal value stated in the result.

The computation is corroborative. The asymptotic itself follows from the prime number theorem in arithmetic progressions, Brun--Titchmarsh, and the explicit tail decomposition in `RESULT.md`.
