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

The proof uses two exact source implications.

First,
\[
\mathrm{RC}\Longrightarrow\mathfrak c\le\omega_2.
\]

Second,
\[
\mathfrak c\le\omega_2
\Longrightarrow
\mathfrak a\le\mathfrak d.
\]

The second implication is explicitly recorded by Pelayo-Gómez and follows from his theorem
\[
\mathfrak d=\omega_1\Longrightarrow\mathfrak a=\omega_1:
\]
if \(\mathfrak d=\omega_1\), use the theorem; if \(\mathfrak d=\omega_2\), use
\[
\mathfrak a\le\mathfrak c\le\omega_2=\mathfrak d.
\]

Composition gives
\[
\mathrm{RC}\Longrightarrow\mathfrak a\le\mathfrak d.
\]

For the model-specific clause, Honzik gives
\[
\mathfrak d=\omega_1,
\]
so Pelayo-Gómez gives
\[
\mathfrak a=\omega_1.
\]
Combining this with Honzik's other displayed invariant values yields
\[
\mathfrak a=\mathfrak d=\operatorname{non}(\mathcal N)=\omega_1
<
\operatorname{cov}(\mathcal N)=\mathfrak c=\omega_2.
\]

No computation is used.

## Limits

The relative-consistency conclusion retains Honzik's strongly compact cardinal hypothesis.

The full body of Honzik's paper was not available through the primary-source retrieval route used in this check; its abstract nevertheless states every premise used in the proof.

The theorem does not determine \(\mathfrak a\) or \(\mathfrak d\) separately in arbitrary models of Rado's Conjecture.
