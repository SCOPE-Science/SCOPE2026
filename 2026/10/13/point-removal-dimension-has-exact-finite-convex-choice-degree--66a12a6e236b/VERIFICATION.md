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

The verification is symbolic and follows the source constructions with exact arity bookkeeping.

For an input realization of size \(r\), the forward proof of Marcone--Volpi Theorem 5.3 applies linear separation only to
\[
(L_j,I,F)_{j<r-1}.
\]
The final input order is transformed directly into two linear extensions. Hence exactly \(r-1\) separator solutions suffice.

Conversely, starting from \(m\) separation instances, the source normalizes them and introduces one additional computable linear order. The resulting point-removal instance therefore has exactly
\[
m+1
\]
input realization orders. The \(\mathsf{DB}_p^+\) preservation clause applies to the first \(m\) output orders, and taking the elements below the new point recovers all \(m\) separators.

Thus, for every fixed
\[
r\ge1,
\]
the two computable transformations give
\[
\mathsf{DB}_{p,r}^+
\equiv_{\mathrm W}
\mathsf{LS}^{r-1}.
\]

Appendix Proposition A.1 of the same source gives
\[
\mathsf{LS}
\equiv_{\mathrm W}
\mathsf{XC}_1.
\]
Taking fixed finite products yields
\[
\mathsf{DB}_{p,r}^+
\equiv_{\mathrm W}
(\mathsf{XC}_1)^{r-1}.
\]

Taking finite parallelizations gives the global identity
\[
\mathsf{DB}_p^+
\equiv_{\mathrm W}
\mathsf{XC}_1^*.
\]

## Limits

The argument establishes ordinary Weihrauch reductions only.

It does not prove a strict hierarchy among finite powers of \(\mathsf{XC}_1\).

It does not classify the weaker point-removal principle \(\mathsf{DB}_p\).
