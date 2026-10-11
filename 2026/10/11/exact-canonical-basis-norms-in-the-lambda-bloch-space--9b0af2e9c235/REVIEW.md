# Review of Exact canonical-basis norms in the \(\lambda\)-Bloch space

## Correctness

PASS. The recent source defines
\[
\|f\|_{\mathfrak B_\lambda}
=
\sup_{z\in\mathbb D}
(1-|z|^2)
|D_z(zf(z))|
\]
and gives
\[
D_z(z\phi_n^\lambda)
=
(n+\lambda+1)\phi_n^\lambda
\]
together with
\[
|\phi_n^\lambda(z)|
\le
\epsilon_n^{-1}|z|^n.
\]

The upper bound is shown to be exact at every positive real radius: the defining finite sum collapses, by the coefficient identity for
\[
(1-t)^{-\lambda}(1-t)^{-(\lambda+1)},
\]
to
\[
\phi_n^\lambda(r)=\epsilon_n^{-1}r^n.
\]
Therefore the two-dimensional supremum reduces exactly to
\[
\max_{0\le r<1}(1-r^2)r^n.
\]
Differentiation gives the unique interior radial maximum at
\[
r^2=n/(n+2)
\]
and the stated value. The \(n=0\) case follows separately from \(\phi_0^\lambda=1\). The asymptotic constant follows from the gamma-ratio formula for \(\epsilon_n^{-1}\).

## Originality

PASS. The 2026 primary source introduces the \(\lambda\)-Bloch norm and contains all structural ingredients, but focused full-text inspection of its definition, basis facts, Banach-space proof, growth section, and basis-based examples found no exact formula for
\[
\|\phi_n^\lambda\|_{\mathfrak B_\lambda}.
\]

The 2022/2024 Hardy--Bergman source gives the canonical basis estimate and Dunkl identity but predates the \(\lambda\)-Bloch-space definition. It therefore supplies antecedent basis theory rather than the new norm computation.

Searches using the exact source, canonical-basis terminology, equivalent radial maximization, and the asymptotic constant returned no implication-equivalent result in the checked literature or published-finding database. The remaining risk is that an older paper may have optimized an equivalent weighted supremum without Bloch terminology.

## Value

PASS. The basis
\[
\{\phi_n^\lambda\}
\]
is the canonical orthonormal basis of
\[
H_\lambda^2(\mathbb D)
\]
and is used throughout the new \(\lambda\)-analytic function-space theory. Its exact size in the newly introduced Bloch norm is therefore a natural structural invariant, not an arbitrary test function.

The formula separates two mechanisms cleanly. The radial maximizing layer
\[
1-r_n\sim1/n
\]
is universal, while the reflection parameter enters through the exact amplitude
\[
n^\lambda/\sqrt{\Gamma(2\lambda+1)}.
\]
This gives sharp quantitative information for future basis, coefficient, and embedding estimates in the new space.

Same-model review: passed. Independent audit: not yet performed.
