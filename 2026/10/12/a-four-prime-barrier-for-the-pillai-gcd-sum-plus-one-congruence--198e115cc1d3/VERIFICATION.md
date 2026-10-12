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

The proof in `RESULT.md` is universal and does not infer the theorem from finite computation.

The attached `verify.py` performs four exact checks.

First, it compares the multiplicative prime-power formula
\[
P(p^a)=p^{a-1}\bigl((a+1)p-a\bigr)
\]
with the defining gcd sum on a finite sample.

Second, it exhaustively checks every
\[
2\le n\le2{,}000{,}000
\]
having
\[
\Omega(n)\le3.
\]
Every integer in this range satisfying
\[
n\mid P(n)+1
\]
is prime.

Third, it verifies the algebraic identities used after forcing the quotients in the two- and three-prime cases.

Fourth, it checks the currently recorded composite counterexample
\[
n=3\cdot37\cdot43\cdot42307\cdot116341
\]
and confirms
\[
P(n)+1=26n.
\]

The finite checks corroborate the formulas and boundary handling. The unbounded conclusion rests on the complete proof in `RESULT.md`.
