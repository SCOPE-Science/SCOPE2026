# Independent audit — SCOPE-20260914-012

Date: 2026-09-28 (UTC)  

## Disposition: PASSED

### Correctness
The exact rational certificate is valid. Recomputing the eleven prescribed nodes gives alternating errors with minimum absolute value 0.02908747... > 1/40, and the denominator has positive minimum 5265323239/5950768000 approximately 0.884814. If a type-(4,4) rational approximant had uniform error <1/40, its difference from the displayed rational would alternate in sign at the nodes, forcing at least nine distinct zeros of a numerator of degree at most eight, a contradiction. Hence E_{4,4}(|x^2-1/4|)>=0.025>0.02.

### Originality
Limited-to-moderate: the alternation/de la Vallee-Poussin mechanism is classical and modern minimax algorithms are well established, but this compact exact threshold certificate for the stated function/type was not found in the retrieved literature.

### Scientific value
Moderate as a small exact benchmark that cleanly separates a claimed 0.02 threshold without relying on floating minimax output.

### Sources checked
- Filip, Nakatsukasa, Trefethen and Beckermann, Rational minimax approximation via adaptive barycentric representations: https://arxiv.org/abs/1705.10132 — Modern rational-minimax context; the record itself uses a classical alternation lower-bound certificate rather than numerical optimality.

### Limitations
- The certificate proves only the lower threshold, not the exact minimax error.
- Several historical reproducibility paths in the record use output/artifacts although the files live under artifacts; this packaging typo does not affect the mathematical certificate.
