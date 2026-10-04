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

The analytic proof was checked from the published dual-pgf differential identity. With \(s=-\log\theta\), the semigroup pgf obeys
\[
\partial_s H_s(t)=H_s(t)\bigl(\phi(H_s(t))-1\bigr).
\]
Under \(\mathbb E[J^2]<\infty\), differentiating once and twice at \(t=1\) gives the stated first- and second-factorial-moment ODEs. The algebra was independently replayed in `verify_dispersion_frontier.py` using exact rational arithmetic for the discrete extremal inequality, equality cases, mean-preserving interpolation, and the integer-extremal semigroup identity.

The checker is deliberately finite: it verifies algebraic identities and witness constructions, not the universal quantifiers. The universal moment formulas and sharpness statement are established in `RESULT.md`. No finite computation is used as evidence for the infinite theorem.

Scientific limits: the variance formula is finite only under \(\mathbb E[J^2]<\infty\). The claim concerns stopping-count distributions in the composition-closed family and does not assert properties of an external process stopped at those counts. Classical branching-process moment equations are background; the sharp fixed-exponent dual-law frontier is the asserted contribution.
