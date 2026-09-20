# Review — weighted-cosine Hadamard upper bound

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proposed counterexample uses a positive diagonal spectrum and an explicit real orthogonal matrix. Exact multiplication gives the stated weighted Gram matrix, from which the three off-diagonal squared weighted cosines are 1/5, 1/5, and 9/16. Their contribution yields 197/40, while the effective spectral dimension is 13/7 and the conjectured upper bound is 63/13; the exact positive gap is 41/520.

The same orthogonal matrix with spectrum diag(t,1,t^-1) yields an exactly factored gap whose denominator is positive for t>0. For t>=3/2, the remaining cubic factor is positive, establishing a continuum of violations. The block-diagonal order-four construction has exact value 237/40 against upper benchmark 28/5, with positive gap 13/40.

The dimension-two theorem was checked independently from the counterexample. After weighted row normalization, the squared weighted-cosine Frobenius norm is tr(G_U G_V), where each 2 by 2 positive-definite G_W has trace two. The determinant identity det(G_W)=ab/(d_1d_2), together with d_1+d_2=a+b, bounds the traceless part of G_W. Frobenius Cauchy-Schwarz then gives exactly 4(a^2+b^2)/(a+b)^2=4/gamma. A common 45-degree frame attains equality. Thus dimension three is genuinely minimal over real orthogonal frames.

The compact symbolic artifact verifies the explicit matrices, all exact rational gaps, and the one-parameter factorization.

## Originality

**PASS, to the best of our knowledge, with the claim limited to the stated conjecture.** The source manuscript, arXiv:2609.17947v1, explicitly states that its theorem does not establish a global Hadamard maximizer and that numerical experiments suggest the upper bound ||C_Σ(U,V)||_F^2 <= n^2/gamma. The currently listed arXiv submission history contains only v1. Searches for the paper title, arXiv identifier, the weighted-cosine terminology, the n^2/gamma bound, and Hadamard-maximizer variants did not locate an erratum, comment, or prior counterexample.

Classical frame-potential literature is relevant background but not coverage of the claim. Benedetto–Fickus theory and a modern account by Mixon, Needham, Shonkwiler, and Villar concern minimizers and optimization landscapes of the ordinary frame potential. The present result instead refutes a spectrum-dependent upper bound on the row-normalized weighted image of an orthogonal frame, and additionally proves the complete n<=2 case.

General correlation-matrix and diagonal-scaling literature was also searched at the level of fixed-spectrum/unit-diagonal/Frobenius formulations. Located sources concern nearest-correlation problems, prescribed spectra, or unrelated diagonal-scaling objectives; no source located implied the exact conjectured bound, the counterexample, or the minimal-dimension theorem.

No inaccessible source was identified as especially likely to contain this exact counterexample to a conjecture first stated in the September 2026 manuscript. Older frame and correlation-matrix literature remains a general residual originality risk, so the novelty statement is explicitly only to the best of our knowledge.

## Value

**PASS.** The conjecture is a structural claim in the source paper's weighted-cosine geometry intended to characterize how incoherent singular-vector frames distribute weighted angular mass. The counterexample changes that picture: a flat common Hadamard frame is stationary and has the stated value when it exists, but it is not a universal global maximizer. The result is exact, dimension-minimal, robust across a one-parameter spectral family, and remains false at order four where a real Hadamard matrix exists.

The dimension-two theorem also identifies a genuine boundary rather than merely producing an isolated numerical exception. This gives a concrete constraint on any corrected upper-bound theory: any replacement must use information beyond effective spectral dimension alone once n>=3, or must impose additional structure on the spectrum or frames.

## Limitations

The result refutes only the Appendix A conjectural global upper bound. It does not invalidate the paper's proved exterior-algebraic identities, lower bounds, stationarity statement for common Hadamard frames, pivoting algorithm, or numerical experiments. No sharp replacement upper bound is proved for n>=3, and no classification of global maximizers is given. The argument is stated for the real orthogonal setting O(n) used in the source manuscript.
