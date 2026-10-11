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

The final claim was checked from the exact published matrix-masa angle formula and the published characterization of maximal angle.

For a relative unitary \(Z\in\mathrm U(k)\), write
\[
Q_k(Z)=|Z|^{\circ2}\circ Z-\frac1kZ.
\]
The verified formula is
\[
\cos\alpha=\frac{k}{k-1}\|Q_k(Z)\|_{\mathrm{op}}.
\]
If the first factor has maximal angle, its relative unitary \(H\in\mathrm U(m)\) is Hadamard and therefore \(|H|^{\circ2}\circ H=m^{-1}H\). Direct entrywise calculation gives
\[
Q_{mn}(H\otimes W)=\frac1mH\otimes Q_n(W).
\]
Because \(H\) is unitary,
\[
\|Q_{mn}(H\otimes W)\|_{\mathrm{op}}=\frac1m\|Q_n(W)\|_{\mathrm{op}},
\]
which yields exactly
\[
\cos\alpha(A_1\otimes A_2,B_1\otimes B_2)=\frac{n-1}{mn-1}\cos\alpha(A_2,B_2).
\]

The coincident-second-factor case gives cosine \((n-1)/(mn-1)\); the maximally-angled-second-factor case gives cosine \(0\). These are exact boundary checks, not numerical tests.

The comparison literature was inspected at statement level. The nearest tensor theorem preserves the angle only under a common tensor factor and therefore does not imply this two-pair tensor law. No claim is made for two arbitrary nonmaximal factor pairs, for infinite-dimensional algebras, or for higher-dimensional Kadison--Kastler distance.
