# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The key identity is direct from the product form of the singleton:
\[
D_JF_n(x)=2^{-k}\Bigl(\prod_{j\in J}x_j\Bigr)\prod_{i\notin J}\frac{1+x_i}{2}.
\]
It implies that a point with \(r\) negative coordinates contributes iff those coordinates lie in \(J\), leaving exactly \(\binom{n-r}{k-r}\) surviving derivatives. Summing by Hamming layers gives the exact norm formula. The fixed-\(p\) asymptotics follow from comparison of the finitely many powers \(r+(k-r)p/2\); the \(p=2\) identity follows from \(\binom nr\binom{n-r}{k-r}=\binom nk\binom kr\). The critical-window limit follows by fixed-\(k\) binomial asymptotics and the expansion of \(1/(2+\lambda/\log n)\).

The source-paper discrepancy was checked against its own derivative normalization \((D_jf)(x)=(f(x)-f(x^{(j)}))/2\) and its Section 6.3 computation. At a point with exactly the coordinates in \(J\) negative, the correct value is \((-1)^k2^{-k}\), not \((-2)^k\). A direct finite-cube enumeration independently confirmed the exact formula for several \((n,k,p)\), including an explicit failure of the source numerical lower bound. The corrected Hamming-layer lower bound still grows as \(n^{k/p}\), so the source conclusion that the spectral power cannot be smaller than \(k/p\) is repaired without using the false constant.

## Originality

**PASS, to the best of our knowledge.** The full text of arXiv:2609.09040v1 was inspected at the definition of the Walsh derivative, Theorem 1.3, Remark 1.4, and Section 6.3. Its Lemma 6.3 states a stronger numerical lower bound and contains the factor error identified above; it does not contain the exact Hamming-layer formula, the three-regime fixed-\(p\) asymptotics, or the \(1/\log n\) crossover. Targeted searches for the source identifier together with correction/erratum terms, and for point-mass/singleton higher Walsh square functions, exact binomial profiles, and Walsh-derivative formulas did not locate a correction or an equivalent statement. The contemporaneous Xu--Zhang endpoint paper arXiv:2609.03993v1 concerns the first-order endpoint estimate and does not provide this higher-order singleton calculation in the material located.

Residual risk remains because the exact identity is elementary and may occur in older Boolean-analysis literature under different notation, and both endpoint papers are very recent, so an unindexed correction or contemporaneous observation may exist. No inaccessible paper produced concrete evidence of prior coverage. Searches did not justify claiming exhaustive literature coverage.

## Value

**PASS.** The result does more than change a constant: it identifies and repairs a false lemma used in the exponent-sharpness argument of a recent endpoint Riesz-transform preprint, supplies the exact finite-dimensional quantity that the argument was attempting to bound, and reveals a nontrivial \(p=2\) phase transition with an explicit critical crossover. It also cleanly separates what is affected from what is not: the source higher-order upper estimate is untouched, and its exponent-optimality conclusion survives via the corrected lower bound.

## Limitations

The result does not determine the optimal \((p-1)\)-dependence of the higher-order fractional Riesz norm, does not show that singletons are global extremizers, and does not independently re-audit the source paper outside the statements needed here. Originality is to the best of our knowledge. No independent validation, independent audit, or formal proof-assistant verification is asserted.
