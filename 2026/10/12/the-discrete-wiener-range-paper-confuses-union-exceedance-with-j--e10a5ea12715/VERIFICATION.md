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
For independent coordinates with marginal CDFs \(F_i\),
\[
F_{\mathrm{joint}}(\mathbf r)
=
\prod_iF_i(r_i).
\]
Therefore
\[
1-F_{\mathrm{joint}}(\mathbf r)
=
\Pr(\exists i:R_i>r_i),
\]
whereas simultaneous strict survival is
\[
\Pr(R_i>r_i\ \forall i)
=
\prod_i\{1-F_i(r_i)\}.
\]

For two identical margins with strict tail \(s\),
\[
S_{\mathrm{pub}}=2s-s^2,
\qquad
S_{\cap}=s^2,
\]
so
\[
S_{\mathrm{pub}}/S_{\cap}=2/s-1.
\]

For the inclusive discrete hazard used in the source,
\[
\Pr(\mathbf R=\mathbf r\mid R_i\ge r_i\ \forall i)
=
\prod_i
\frac{p_i(r_i)}{1-F_i(r_i-1)}.
\]
Componentwise rectangular truncation preserves independence, so the same product structure applies after truncation.

The included checker verifies these identities for arbitrary marginal CDF values and gives an explicit independent-geometric example showing that division by \(1-F_{\mathrm{joint}}\) does not equal the simultaneous-survival conditional hazard.
