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

The accepted statement is the direct composition of two checked implications.

First, Zapletal proves, relative to
\[
\operatorname{Con}(\mathrm{ZFC}),
\]
the existence of a model
\[
W\models
\mathrm{ZF}+\mathrm{DC}+\mathrm{BPI}
+\text{“there is no total \(E_0\)-selector.”}
\]

The paper explicitly defines the relevant Vitali set as a selector for eventual equality on \(2^\omega\), so the no-selector conclusion is about the same \(E_0\) appearing below.

Second, Larson and Zapletal prove in
\[
\mathrm{ZF}+\mathrm{DC}
\]
that
\[
\text{“\(\mathbb R\) has a Hamel basis over \(\mathbb Q\)”}
\Longrightarrow
\text{“there is a total \(E_0\)-selector.”}
\]

Since \(W\) satisfies DC, this implication holds internally in \(W\). Its conclusion is false there, so its antecedent is false there. Hence
\[
W\models
\text{“\(\mathbb R\) has no Hamel basis over \(\mathbb Q\).”}
\]

Therefore
\[
\operatorname{Con}(\mathrm{ZFC})
\Longrightarrow
\operatorname{Con}\!\left(
\mathrm{ZF}+\mathrm{DC}+\mathrm{BPI}
+\text{“no Hamel basis of \(\mathbb R\) over \(\mathbb Q\)”}
\right).
\]

BPI implies Hahn--Banach, so the same model gives the Hahn--Banach corollary.

## Limits

This is a relative-consistency nonimplication, not a proof that BPI is incompatible with Hamel bases.

The argument uses DC in the Larson--Zapletal bridge.

No computation, enumeration, or experimental evidence is used.
