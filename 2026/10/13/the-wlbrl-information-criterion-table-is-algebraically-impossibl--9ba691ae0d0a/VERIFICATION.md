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
The checker takes the WLBRL Table 5 values as printed constants.

For each dataset it evaluates
\[
\operatorname{AIC}=Q+2p
\]
and
\[
\operatorname{BIC}=Q+p\log n
\]
for both \(p=2\) and \(p=3\), verifying that neither reproduces the published AIC/BIC values.

For the model's actual three-parameter specification it verifies
\[
(555.37,\ 559.8595226844\ldots)
\]
for dataset 1 and
\[
(416.34,\ 422.6230336867\ldots)
\]
for dataset 2.

It also evaluates the conventional small-sample correction only as an auxiliary check. The central conclusion uses only the defining AIC/BIC identities.
