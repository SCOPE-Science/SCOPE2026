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
The correspondence consists of the two Möbius graphs of the identity and \(R(z)=e^{2\pi i(\sqrt2-1)}z\). Both coordinate projections of each graph are bijective, so the generic topological degree is two.

Normalized arclength \(\mu\) on \(\mathbb S^1\) is invariant under \(R\), hence
\[
\frac12\int\left(f(z)+f(R^{-1}z)\right)d\mu(z)=\int f\,d\mu
\]
for every continuous \(f\).

For an almost-invariant Borel set \(A\), the defining full-measure subset \(A'\) satisfies \(R^{-1}(A')\subseteq A\). Since \(A'=A\) modulo \(\mu\), this gives \(R^{-1}(A)=A\) modulo \(\mu\), and irrational-rotation ergodicity forces \(\mu(A)\) to be zero or one.

For the arc \(E\) of angular length \(1/10\), its rotation by \(\sqrt2-1\) is disjoint from \(E\). Thus the identity branch realizes first return at time one and
\[
\mathcal F_E(z)=\{z\}
\]
for every \(z\in E\). The half-arc \(B\) is induced-almost-invariant with \(\mu_E(B)=1/2\), so the induced measure is not ergodic.

The full primary manuscript was inspected at the definitions and proof locations relevant to this claim. A public audit was compared at statement level; it identifies the proof gap but does not supply or imply this counterexample.

Limits: this verifies only the stated counterexample to the literal theorem and does not establish a general repair theorem.
