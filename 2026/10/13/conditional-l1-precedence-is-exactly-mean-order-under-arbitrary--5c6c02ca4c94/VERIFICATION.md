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

The accepted statement is verified by an exact identity. For integrable \(X,Y\), define
\[
A=\mathbb E[(Y-X)\mathbf 1_{\{X<Y\}}],
\qquad
B=\mathbb E[(X-Y)\mathbf 1_{\{X>Y\}}].
\]
The defining conditional products equal \(A\) and \(B\) whenever the conditioning events have positive probability; the truncated forms canonically cover zero-probability boundary events.

Directly,
\[
A-B=\mathbb E[(Y-X)\mathbf 1_{\{X<Y\}}]+\mathbb E[(Y-X)\mathbf 1_{\{X>Y\}}]=\mathbb E(Y-X),
\]
because \(Y-X=0\) on \(\{X=Y\}\). Hence the order condition \(A\ge B\) is exactly \(\mathbb E X\le\mathbb E Y\). Reversing the variables gives the equality characterization.

The source text was checked at Definition 2.1, Theorem 2.1, and the paragraph immediately after that theorem. The source proves the equivalence under independence and describes the dependent case as dependence-sensitive; the identity above verifies the stronger all-couplings statement without relying on that assertion.

No numerical computation, finite enumeration, asymptotic argument, or external certificate is part of the proof. The only unproved limit is bibliographic: targeted searches cannot rule out an unindexed prior observation or corrigendum.
