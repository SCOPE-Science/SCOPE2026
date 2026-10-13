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

The attached checker compares the theorem with direct enumeration for every base
\[
2\le b\le500.
\]

For each base it forms the direct set
\[
\{(a,c):1\le a,c<b,\ ac\mid ab+c\}
\]
and the predicted set obtained from
\[
d\mid b,\qquad d\ge2,\qquad a\mid d+1,\qquad a<d,
\]
with
\[
c=a\frac{b}{d}.
\]
The two sets are asserted equal.

The checker separately verifies
\[
Z_2(b)
=
\sum_{\substack{d\mid b\\d\ge2}}
(\tau(d+1)-1),
\]
the bound
\[
Z_2(b)\ge\tau(b)-1,
\]
the equality classification for every
\[
3\le b\le500,
\]
and the prime-base formula.

For base \(10\), it asserts the exact list
\[
11,\ 12,\ 15,\ 24,\ 36.
\]

These finite checks are corroborative. The infinite classification follows from the bijection proved in `RESULT.md`.
