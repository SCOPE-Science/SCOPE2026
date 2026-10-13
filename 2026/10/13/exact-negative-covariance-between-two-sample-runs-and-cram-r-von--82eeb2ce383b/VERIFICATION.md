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

The proof is symbolic and all-size. The separate checker is corroborative.

Running `python verify.py` from the package directory produced:

- exact binary words enumerated: 8166;
- sample-size pairs checked by enumeration: 66;
- conditional aggregate identities checked: 777;
- all exact checks passed.

For each positive \((m,n)\) with \(m+n\le12\), the checker enumerates every fixed-composition label word and verifies exactly
\[
\mathbb ES=\frac{mnN(N+1)}6,
\]
\[
\operatorname{Cov}(R,S)=-\frac{mn(2mn-N)}3,
\qquad
\operatorname{Cov}(R,T)=-\frac{2mn-N}{3N^2}.
\]
For every positive \((m,n)\) with \(4\le m+n\le40\), it also evaluates the conditional hypergeometric formulas and verifies
\[
\sum_{i=1}^{N-1}\mathbb E[S\mid I_i=1]
=\frac{N(N-1)}6\bigl((N-1)mn+N\bigr).
\]

The checker uses exact rational arithmetic and has no numerical-tolerance step. Enumeration through a finite size is not an infinite proof; the theorem for all sample sizes rests on the combinatorial calculation in `RESULT.md`. The verification does not address unequal-distribution alternatives or tied samples.
