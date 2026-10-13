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

Assume an \(I2\)-embedding exists.

Lücke--Poveda Theorem 1.3 supplies a transitive set-sized model
\[
M\models\mathrm{ZFC}+\text{“there is a proper class of exacting cardinals.”}
\]

Inside \(M\), this means that exacting cardinals are unbounded in \(\operatorname{Ord}^M\).

Osinski Corollary 5.9 is proved over ZFC and states that unboundedly many exacting cardinals are equivalent to the following scheme: for every logic \(\mathcal L\), there is a cardinal
\[
\lambda=\beth_\lambda
\]
such that for every
\[
\alpha<\lambda<\zeta
\]
there is a cardinal
\[
\alpha<\mu<\lambda
\]
for which \(\mathcal L\) is \((\mu,\lambda)\)-chain compact for rank type \((\zeta,\lambda)\).

Definition 3.2 in Osinski fixes rank type:
\[
\operatorname{rk}(A)=\zeta,\qquad \operatorname{rk}(P^A)=\lambda.
\]

Definition 5.3 fixes \((\mu,\lambda)\)-chain compactness: a theory of size \(\lambda\) that is an increasing \(\mu\)-union has a model of the required rank type whenever every stage does.

Because \(M\models\mathrm{ZFC}\), Corollary 5.9 applies internally to \(M\). This proves the claim.

## Limits

No absoluteness from \(M\) to the ambient universe is used.

No lower consistency bound or equiconsistency with \(I2\) is proved.

No computational or finite experimental evidence is involved.
