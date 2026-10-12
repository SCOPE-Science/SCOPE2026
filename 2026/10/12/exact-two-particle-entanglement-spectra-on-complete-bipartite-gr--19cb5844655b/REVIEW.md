# Scientific review: complete bipartite two-particle entanglement spectra

## Correctness — PASS

The complete quantifier range is all integer \(m,n\ge1\), both exchange signs, an arbitrary initial edge, and all discrete \(t\ge0\). On the supported \(K_{mn,mn}\) component the arc-reversal Grover walk is four-periodic. Direct scattering gives four exact amplitude blocks. Their nonzero singular-value squares are \((1/2)\), \((A/2,B/2)\), and \((A^2/2,AB/2,AB/2,B^2/2)\), respectively; the opposite-orientation block duplicates these eigenvalues. The time-two step is an exact partially transposed rank-one projector, not an empirical pattern. The exterior-product determinant proves \(AB=q^2\), while the row/column norm proves \(A+B=1\). The entropy and extremal conclusions follow with all degenerate cases included. Independently reconstructed finite-dimensional scattering verified 572 identities across 11 graph sizes. Finite tests do not prove the universal claim; the proof is algebraic.

## Originality — PASS, with priority risk

The most relevant original full text [1] is **not** omitted: its model, four-periodic balanced \(K_{r,r}\) amplitudes and classification of saturation of \(\log(2r^2)\) are credited. A simple application of its balanced formula already contains some balanced special-case spectrum information, so that alone would not be novel. The new result concerns the full **rectangular** \(K_{m,n}\) Schmidt and Rényi spectrum, the partial-transpose tensorization, and a graph-size-independent sharp rank/entropy bound. The primary paper confines its analysis to balanced complete bipartite graphs; the checked record and scientific-literature comparisons did not establish an earlier result dominating the rectangular theorem. Earlier implicit/unindexed computation remains a genuine risk; search absence is not a novelty certificate.

## Value — PASS

The work closes the specific gap between the known ambient bound \(\log(2mn)\) and actual entanglement obtainable by this natural edge-pair initialization. A universal ceiling \(\log8\) and exact rank-eight threshold, despite arbitrarily growing Hilbert dimension, are structural rather than numerical refinements. The full all-index Rényi spectrum and equality cases provide parameter-specific observables. The conclusion does not cover other preparations or operational identical-particle entanglement conventions.

## Closest literature and limitations

[1] S. Kubota, H. Matsubara, and E. Segawa, *Entanglement entropy in two-particle Grover walks on graphs*, arXiv:2607.09066 (2026-07-10), especially the original model in Section 3 and balanced-case amplitudes and saturation in Section 4. The source's exact balanced formula must not be misrepresented as original here. Full web-accessible manuscript transcription, including Section 4 and the final discussion, was consulted; no complete rectangular-spectrum result was found. The absence of a directly inspected publisher-style PDF is an access/provenance limitation, not evidence for priority. Reproducibility requires Python 3 and NumPy. There is no independent external review.

Self-review: passed. Independent audit: not yet performed.
