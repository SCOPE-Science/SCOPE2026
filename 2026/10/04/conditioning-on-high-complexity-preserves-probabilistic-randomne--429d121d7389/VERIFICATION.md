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

Let
\[
H_a=\{\omega:K(\omega)\ge a\}
\]
and
\[
B_g(a)=\{\omega\in H_a:\beta_\omega(g(K(\omega)))>c_2\}.
\]

The primary source gives
\[
\mathbf m(H_a)\ge\frac{\tau(a)}{c_1}
\]
and
\[
\mathbf m(B_g(a))\le c_3S_g(a),
\qquad
S_g(a)=\sum_{k\ge a}2^{-g(k)}.
\]
Therefore
\[
\mathbf Q_a(B_g(a))
\le
c_1c_3\frac{S_g(a)}{\tau(a)}.
\]

For any computable increasing \(h\to\infty\), the function
\[
f=1/h
\]
is computable, positive, decreasing, and tends to zero. The companion source proves
\[
\frac{\tau(a)}{f(a)}\to\infty.
\]
Hence
\[
\frac1{\tau(a)}=o(h(a)),
\]
and the master conditional estimate follows.

The four specializations use the exact source bounds
\[
S_g(a)=O(2^{-\theta a}),
\]
\[
S_g(a)=O\!\left(a^{1-\theta}2^{-a^\theta}\right),
\]
\[
S_g(a)=O\!\left(a^{1-(\log a)^{\theta-1}}\right),
\]
and
\[
S_g(a)=O(a^{1-\theta}),
\]
respectively.

For the superpolynomial case, after multiplying by any fixed power \(a^q\), the exponent
\[
q+1-(\log a)^{\theta-1}
\]
still tends to negative infinity. Thus the normalized bad share remains smaller than every inverse polynomial.

## Limits

The verification establishes no effective threshold for the little-\(o\) statements. It does not strengthen the source's absolute bad-set bound or its optimality results.
