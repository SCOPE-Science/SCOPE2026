# Scientific review

## Correctness — PASS
The proof uses the precise truncation-based limited-precision upward probability, establishes an increasing finite-state chain, characterizes every absorbing state, and prevents overshooting the first absorber. The final predecessor and exact geometric residence time follow by direct binary-grid arithmetic. In 224 exact rational finite parameter combinations the standalone program exhaustively reconstructed the reachable transition graphs and matched the theorem. This computation corroborates, but does not prove, arbitrary-precision claims; those are established analytically.

## Originality — PASS (subject to independent historical checking)
The principal 2026 source explicitly excludes fused multiply-add Horner (Remark 3), and its finite-degree bounds do not imply an almost-sure absorbing state or a sharp random-bit threshold. The foundational 2024/2025 source treats limited-precision rounding, summation, and inner products, not this contraction; the 2025 few-bit paper treats alternative rounding modes and their bias; and the 2026 survey is background. Searches for geometric-polynomial, fused-Horner, quantized-contraction and absorption aliases in published research records produced no equivalent mathematical implication. A negative search is not proof of priority; the main residual risk is a previously published specialized fixed-point quantization theorem covering the same state-dependent rounded affine map.

## Mathematical value — PASS
This is a natural exact benchmark for the FMA variant expressly left outside the most relevant 2026 Horner analysis. It resolves whether additional random bits eliminate permanent long-horizon stagnation for a canonical near-one geometric polynomial, gives the exact nonzero bias when they do not, and also quantifies the final waiting time required even when the bias vanishes. The result is restricted to a particular representable evaluation point and rounding mechanism, but the exact threshold addresses a mathematically motivated open corner rather than an arbitrary invariant.

## Relationship to literature and limitations
Closest: El Arar et al., arXiv:2603.24161 (Definition 2, §3, Remark 3, §5.1); El Arar et al., arXiv:2408.03069 (§§2.3,4,6); Fitzgibbon–Felix, arXiv:2504.20634 (§§I–III); and El Arar et al., arXiv:2603.06060 (§§1–2). Results are restricted to the exact FMA and truncation-based rounding, fixed \(p,q,r\), independent random decisions, and the all-one geometric polynomial; no claims about general polynomials or hardware. Specialized literature may contain an equivalent theorem, and further external comparison is warranted.

Self-review: passed. Independent audit: not yet performed.
