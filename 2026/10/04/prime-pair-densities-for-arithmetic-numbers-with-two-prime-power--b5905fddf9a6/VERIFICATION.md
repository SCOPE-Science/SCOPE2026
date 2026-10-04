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
# Verification record

The exact claim has two proof layers.

First, the arithmetic criterion for
\[
N=P^{\ell-1}Q^{m-1}
\]
is obtained by specializing Oller-Marcén's Proposition 6. The resulting equivalence is
\[
\tau(N)\mid\sigma(N)
\quad\Longleftrightarrow\quad
\ell\mid P-1
\quad\text{and}\quad
\left(m\mid Q-1\ \text{or}\ \operatorname{ord}_m(P)=\ell\right).
\]
The proof in `RESULT.md` then counts the relevant reduced residue classes and applies prime distribution in fixed arithmetic progressions.

Second, `verify.py` performs bounded checks that are independent of the asymptotic argument. It tests eight fixed exponent-prime pairs, all admissible ordered variable-prime pairs up to \(500\), and the corresponding residue-class counts. Its replay output is:

`VERIFY_OK pair_checks=68448 exponent_pairs=8 prime_bound=500`

The computation does not certify the limit as \(x\to\infty\), does not replace the published cyclotomic criterion, and does not test literature originality. It is only a finite consistency check of the algebraic specialization and residue counting.
