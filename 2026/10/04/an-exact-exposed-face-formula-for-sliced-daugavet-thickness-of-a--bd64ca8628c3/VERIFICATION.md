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

The final claim was checked by reconstructing both inequalities from the definitions.

For the upper inequality, the key implication is
\[
\alpha f(u)+\beta g(v)>1-\delta
\Longrightarrow
\alpha\|u\|+\beta\|v\|>1-\delta,
\]
followed by
\[
\|(cx,dy)-(u,v)\|_N\le N(c+\|u\|,d+\|v\|).
\]
Compactness of \(B_N\cap[0,\infty)^2\) then forces the limiting scalar supremum onto \(F_N(h)\).

For the lower inequality, the Daugavet slice characterization produces a vector simultaneously almost maximizing the active functional and almost antipodal to the normalized center coordinate. A norming functional for that difference gives the scaled estimate
\[
\|x_0-au\|\ge(1-\eta)(c+a),
\]
and similarly in the second coordinate. Zero center coordinates and zero functional coordinates were checked separately.

The known \(\ell_p\) values from arXiv:2005.02045 are consistent with the formula. No finite computation, exhaustive enumeration, or external certificate is required. The principal unresolved verification limitation is literature access: arXiv:2607.02227 was available only at abstract level.
