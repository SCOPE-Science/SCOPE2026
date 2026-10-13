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

Let \(R\) be a consistent same-language extension of ACFA.

First, \(R\) is model-complete. Indeed, for models \(M,N\models R\), every embedding
\[
M\hookrightarrow N
\]
is an embedding between models of ACFA. Since ACFA is model-complete, that embedding is elementary.

Second, choose a completion \(R'\) of \(R\). Then \(R'\) is a completion of ACFA. Beyarslan--Kowalski Theorem 1.2 therefore gives
\[
(R')_\tau\text{ has no model companion.}
\]

Third, Beyarslan--Kowalski Corollary 6.2 states that if a model-complete theory \(S\) has \(S_\tau\) with a model companion, then every completion \(S'\) of \(S\) has \((S')_\tau\) with a model companion.

Taking \(S=R\), existence of a model companion for \(R_\tau\) would imply existence for \((R')_\tau\), contradicting the previous paragraph. Hence
\[
R_\tau\text{ has no model companion.}
\]

## Limits

The extension must be in the original difference-field language. The proof does not classify existentially closed expansions and does not address richer language expansions.

No computation or experimental evidence is used.
