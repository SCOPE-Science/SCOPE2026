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

The primary source was inspected at the exact theorem and application statements used in the proof. The source formula is
\[
b_2(N)+2g
\ge
\max_{0\le j<d}
\left|
\sigma(N)-\frac{2j(d-j)}{d^2}\,x\cdot x
+\sigma_K(e^{2\pi ij/d})
\right|
\]
for positive genus, under \(H_1(\Sigma_d(K))=0\), together with a separate genus-zero Arf condition.

The supporting topological signature theorem was inspected in a source explicitly working with locally flat topological embeddings. For knots it gives
\[
|\sigma_L(\omega)|\le2g_4^{\mathrm{top}}(L).
\]

After additivity,
\[
\sigma_K(\omega)-\sigma_J(\omega)=\sigma_{K\#-J}(\omega),
\]
so every signature coordinate changes by at most twice the topological concordance distance. Taking maxima preserves that bound.

The bundled verifier checks the remaining ceiling and zero-branch arithmetic lemma over a finite rectangle of parameters and returns:

`VERIFY_OK cases=1696768 b2=0..15 scores=0..63 h=0..15`

This finite calculation is only a regression check. The universal theorem follows from the symbolic inequalities and concordance invariance of the Arf invariant.

No independent audit has been performed.
