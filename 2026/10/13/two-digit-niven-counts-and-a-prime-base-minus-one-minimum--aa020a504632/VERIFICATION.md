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

For a two-digit number
\[
n=(a,c)_b=ab+c,
\]
the checker directly tests
\[
a+c\mid n.
\]
It independently evaluates the divisor-lattice formula
\[
(b-1)+
\sum_{\substack{v\mid b-1\\v\ge2}}
\ \sum_{\substack{1\le u<v\\\gcd(u,v)=1}}
\left\lfloor
\frac{b-1}{\max\{u,v-u\}}
\right\rfloor.
\]

For every base
\[
2\le b\le300,
\]
the direct count and the formula agree exactly. The checker also verifies
\[
H_2(b)\ge2b-3
\]
through that range and, for every
\[
4\le b\le300,
\]
checks that equality is equivalent to primality of
\[
b-1.
\]

For each composite \(b-1\), the checker additionally constructs the explicit extra witness
\[
(1,d-1)_b,
\]
where \(d>1\) is the least proper divisor of \(b-1\), and confirms that it lies outside both universal families.

The computation is corroborative. The infinite theorem is established by the bijective normalization and prime/composite arguments in `RESULT.md`.
