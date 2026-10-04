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

The proof package contains `artifacts/span12_solution_table.json` and the standard-library checker `artifacts/verify_span12.py`.

For each residue \(R\in\{0,\ldots,59\}\), the table stores thirteen coefficient polynomials in \(n\). The verifier checks all defining equations exactly. Each residual has degree at most \(8\), so nine exact substitutions establish each polynomial identity.

The determinant of the \(13\times13\) system has degree at most \(10\). Exact Bareiss determinants at eleven distinct integers all equal
\[
6\,998\,400\,000,
\]
so the determinant polynomial is that nonzero constant.

For every residue the verifier reconstructs the quartic \(P(-1)\), applies the rational-root theorem to \(P(-1)-1\) and \(P(-1)+1\), and checks all integer divisor candidates. Exactly thirteen parameter choices survive, and all thirteen evaluate to \(f(t)=1\). The source's displayed span-\(12\) formal solution is separately reproduced at \(R=1,n=0\).

Replay output:

`VERIFY_OK residues=60 determinant=6998400000 determinant_compatible=13 all_trivial=true`

The finite substitution counts certify bounded-degree polynomial identities; they are not a heuristic search over the free integer parameter.

The independent-audit channel has not been performed.
