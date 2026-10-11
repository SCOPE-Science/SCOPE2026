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

The source defines
\[
C=\sum_{i\in[m]}\sum_{j\in I}v_{ij}^{2}\|\Lambda_{ij}\|^{2}.
\]
For \(f\in R(K)\), boundedness of the Moore--Penrose inverse gives
\[
\|f\|^{2}
\le
\|K^\dagger\|^{2}\|K^*f\|^{2}.
\]
Hence the deleted energy satisfies
\[
E_{\mathrm{deleted}}(f)
\le
C\|K^\dagger\|^{2}\|K^*f\|^{2}.
\]
Subtracting from the original woven lower bound yields
\[
E_{\mathrm{remain}}(f)
\ge
\bigl(A-C\|K^\dagger\|^{2}\bigr)\|K^*f\|^{2}.
\]

For the counterexample,
\[
H=\mathbb C,\qquad K=\frac12I_H,\qquad
J=\{0,1\},\qquad m=2.
\]
Both labels use
\[
\Lambda_{i0}=\frac12I_H,\qquad
\Lambda_{i1}=0,
\]
with full subspaces and unit weights. Every full weave has energy
\[
\frac14\|f\|^{2}=\|K^*f\|^{2},
\]
so \(A=B=1\) are admissible universal bounds.

For deletion \(I=\{0\}\),
\[
K^\dagger=2I_H,\qquad
\|K^\dagger\|^{2}=4,\qquad
C=2\cdot\frac14=\frac12.
\]
The printed condition is satisfied:
\[
\frac12<4.
\]
The remaining energy is identically zero, so the conclusion fails.

The publisher PDF was inspected both as extracted text and as page images on printed pages 952--953. The theorem statement and the proof display the inconsistent factors directly. The foundational open-access \(K\)-\(g\)-fusion paper and the later continuous controlled weaving preprint were inspected for the closest pseudoinverse and erasure formulations.
