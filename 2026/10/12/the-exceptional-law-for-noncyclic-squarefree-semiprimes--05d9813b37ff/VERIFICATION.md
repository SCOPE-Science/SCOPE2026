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

The proof has two logically separate components.

First, for distinct primes \(p<q\),
\[
\varphi(pq)=(p-1)(q-1),
\]
so
\[
\gcd(pq,\varphi(pq))>1
\]
is equivalent to
\[
p\mid q-1.
\]
This is the exact local reduction.

Second,
\[
E(x)=\sum_{p<\sqrt x}\pi(x/p;p,1).
\]
For each fixed \(p\), the prime number theorem in arithmetic progressions gives the main term
\[
x/[p(p-1)\log x].
\]
The remaining moduli are controlled uniformly by Brun--Titchmarsh up to \(x^{1/3}\), while for larger \(p\) the representation
\[
q=kp+1,\qquad k\le x/p^2,
\]
gives the elementary bound \(O(x^{2/3})\). Since
\[
\sum_p\frac1{p(p-1)}
\]
converges, the cutoff can be removed.

The packaged checker verifies the local criterion against direct evaluation of \(\gcd(n,\varphi(n))\) for every squarefree semiprime through \(200000\), computes exceptional counts at several cutoffs, and computes a partial sum for the constant together with an elementary tail enclosure.

These finite calculations corroborate the formulas but do not replace the infinite asymptotic proof.
