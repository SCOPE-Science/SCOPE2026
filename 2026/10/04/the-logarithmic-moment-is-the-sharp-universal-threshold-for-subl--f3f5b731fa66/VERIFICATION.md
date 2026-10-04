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

The proof was checked symbolically from the stated assumptions.

For the sufficient direction, with \(Y=\log(1+T)\), finite \(\mathbb EY\) implies
\[
\sum_{k\ge1}\Pr(Y\ge ck)<\infty
\]
for every \(c>0\). Geometric sampling and the first Borel--Cantelli lemma therefore give sublinear age on \(n_k=\lceil a^k\rceil\). The bounded-growth inequality fills each interval \([n_k,n_{k+1})\), and the countable choice \(a=1+1/j\) makes the resulting upper bound tend to zero.

For the converse, the identity
\[
\sum_{k\ge1}\Pr(T\ge2^k-1)=\infty
\]
follows from the tail-sum formula for \(\log_2(1+T)\). Independent dyadic activation blocks then obey both the unit-growth age condition and pointwise stochastic domination by \(T\). The second Borel--Cantelli lemma forces infinitely many active blocks, and their endpoints have age ratio tending to \(1/2\).

For the harmonic-window consequence, once \(\tau_n/n\to0\),
\[
\sum_{m=n-\tau_n}^{n-1}\frac1{m+1}
\le
\frac1{n-\tau_n+1}
+
\log\!\left(\frac{n}{n-\tau_n}\right),
\]
and the right side tends to zero.

No numerical computation, exhaustive enumeration, or unproved asymptotic approximation is used. The literature comparison was performed against the full relevant parts of the 2026 preprint, its 2023 predecessor, and the corresponding 2024 dissertation treatment. The 2022 comparison was limited to its accessible published statement and is recorded as a residual literature risk.
