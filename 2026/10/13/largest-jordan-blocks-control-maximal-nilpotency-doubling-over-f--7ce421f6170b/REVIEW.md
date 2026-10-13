# Self-review

## Correctness
PASS. For \(X_B=A+\varepsilon B\), the square-zero expansion gives \(X_B^{2r}=0\) and isolates the unique possible surviving term at exponent \(2r-1\), namely \(\varepsilon A^{r-1}BA^{r-1}\). This proves the maximal-index criterion. The failure set is the kernel of \(B\mapsto A^{r-1}BA^{r-1}\); vectorization gives rank \(s^2\), hence codimension \(s^2\) and the stated finite-field count. The edge case \(A=0\) is included by taking \(r=1\). Exhaustive checks over \(\mathbb F_2\) agree with the proof.

## Originality
PASS. The closest published result gives the complete distribution only when the real part is one Jordan block and explicitly leaves a general nilpotent real part with several blocks unclassified. The recent dual-matrix paper supplies nilpotency equivalence and the universal \(2r\) vanishing bound but not the multi-block maximal-stratum count. Searches for the invariant criterion, the codimension \(s^2\), and the density \(1-q^{-s^2}\) found no equivalent statement. The remaining risk is older square-zero-extension literature under different terminology.

## Value
PASS. The result resolves a natural part of the explicit multi-block gap: it shows that maximal nilpotency doubling is controlled by a canonical invariant, the multiplicity of the largest Jordan blocks, and that the exceptional set is a linear subspace of exact codimension \(s^2\). This extends the single-block probability \(1-q^{-1}\) to every nilpotent real part without attempting a routine block-by-block enumeration of all smaller indices.

## Closest literature and limitations
Özbay's published February 2026 abstract states the qualitative index-growth phenomenon. Şentürk--Özbay give the \(2r\) upper bound in arXiv:2609.29468v1. The closest published result record, `2026/10/4/SCOPE-exact-nilpotency-index-distribution-for-jordan-lifts-over-finite--a669645ca0b7`, proves the full one-block distribution and explicitly notes that the multi-block case remains unclassified. The new claim covers only the maximal-index stratum for arbitrary nilpotent real parts, not the full multi-block distribution.

Self-review: passed. Independent audit: not yet performed.
