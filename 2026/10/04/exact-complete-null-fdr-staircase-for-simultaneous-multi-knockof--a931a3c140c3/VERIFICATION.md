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
`verify.py` checks the package claim without external data.

It performs four checks:

1. Direct exact-rational enumeration of all grouped original-win/knockoff-win sequences for several small \((\kappa,r,d)\) cases, compared with the displayed Raney-number formula.
2. Direct enumeration of first-hit paths compared with the ballot count \(r((r+1)b+r)^{-1}\binom{(r+1)b+r}{b}\).
3. Boundary checks that the finite FDR is zero for \(d<r\) and changes only at \(d=(r+1)b+r\).
4. Numerical bisection of the smaller root of \(f=(\kappa+1)^{-1}+\kappa(\kappa+1)^{-1}f^{r+1}\) for the three displayed \(q=0.1\) examples.

A successful run prints `VERIFY_OK`.

The exhaustive checks are finite replay tests, not the proof of the infinite theorem. The proof of the finite formula is the first-passage/Raney argument in `RESULT.md`; the infinite limit follows from the bounded harmonic equation. The verifier does not test tied gap statistics, non-null mixtures, or misspecified knockoff generation, all of which are outside the claim.
