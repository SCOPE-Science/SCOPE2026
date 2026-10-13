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
The checker verifies, for
\[
1\le m\le200,
\]
that two copies of
\[
\mathbb P^{m-1}
\]
have total Euler characteristic
\[
2m,
\]
equal to the Euler characteristic of
\[
\mathbb P^{2m-1}.
\]

It also checks the resulting formulas for standard dimension families
\[
\mathfrak{gl}_n,\quad
\mathfrak{sl}_n,\quad
\mathfrak{so}_n,\quad
\mathfrak{sp}_{2n}
\]
over a finite regression range.

These numerical checks are not the proof. The all-Lie-algebra theorem follows from the exact fixed-locus calculation for the algebraic \(\mathbb C^*\)-action in `RESULT.md`.
