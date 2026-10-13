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

For a squarefree semiprime \(pq\), the defining equation is
\[
pq=1+k(p+q).
\]
It is equivalent to
\[
(p-k)(q-k)=k^2+1.
\]

With \(p<q\), put
\[
d=p-k.
\]
The proof shows
\[
1\le d\le k
\]
and
\[
d\mid k^2+1.
\]
Thus every candidate is captured by
\[
p=k+d,\qquad
q=k+\frac{k^2+1}{d}.
\]

The attached checker exhausts all such divisors for every
\[
1\le k\le132.
\]
Primality is tested by exact trial division up to the integer square root. Every accepted pair is then substituted back into the original hyperperfect equation.

The asserted complete nonzero spectrum is embedded in the checker. It verifies:
\[
\max_{1\le k<132} M(k)=2,
\]
\[
\{k<132:M(k)=2\}=\{12,18\},
\]
and
\[
M(132)=3.
\]

For \(k=132\), the checker also verifies the three products
\[
96361,\quad130153,\quad495529
\]
and confirms that no other divisor of \(132^2+1\) produces a prime pair.

The finite computation proves only the stated cutoff through \(132\). No claim is made about the next value of \(k\) with multiplicity three or about higher multiplicities beyond this range.
