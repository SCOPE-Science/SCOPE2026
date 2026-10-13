# Normalization removes the quadratic localization-length law for average concurrence
## Finding

Li and Wang define the average concurrence of a normalized one-particle state by
\[
\bar C=\frac1M\left[\left(\sum_i |\psi_i|\right)^2-1\right],
\qquad M=\frac{N(N-1)}2.
\]
They then combine this quantity with an exponential localization ansatz and, in their Eq. (8), obtain a term proportional to \(\xi^2/M\). That power is incompatible with normalization of the same exponential ansatz.

With lattice spacing one, normalize the two-sided continuum profile as
\[
\psi(x)=\xi^{-1/2}e^{-|x|/\xi},
\qquad
\int_{-\infty}^\infty |\psi(x)|^2\,dx=1.
\]
Applying the source's own truncation to one localization length on each side gives
\[
\frac1M\left(
\left[2\int_0^\xi \psi(x)\,dx\right]^2-1
\right)
=
\frac{4(1-e^{-1})^2\xi-1}M,
\]
which is linear rather than quadratic in \(\xi\). If the full exponential profile is used instead,
\[
\frac1M\left(
\left[\int_{-\infty}^\infty |\psi(x)|\,dx\right]^2-1
\right)
=
\frac{4\xi-1}M.
\]

There is also an exact discrete version. On sites \(-L,\ldots,L\), put
\[
\psi_n=Z_L^{-1/2}r^{|n|},
\qquad r=e^{-1/\xi},
\]
with
\[
S_L=1+\frac{2r(1-r^L)}{1-r},
\qquad
Z_L=1+\frac{2r^2(1-r^{2L})}{1-r^2}.
\]
Then
\[
M\bar C_L=\frac{S_L^2}{Z_L}-1.
\]
For fixed \(\xi\), sending the boundaries away gives
\[
K_\infty(\xi)
=
\frac{2r(r^2+r+2)}{(1-r)(1+r^2)},
\qquad r=e^{-1/\xi},
\]
and, as \(\xi\to\infty\),
\[
K_\infty(\xi)
=
4\xi-1-\frac{2}{3\xi}
+\frac{59}{180\xi^3}
+O(\xi^{-5}).
\]
Thus the normalized exponential model has linear leading growth in localization length.

## Assumptions and scope

The statement concerns the analytic scaling inference made from the exponential ansatz in arXiv:quant-ph/0403178, with lattice spacing set to one. The continuum calculation treats the exponential envelope as a normalized model profile. The discrete calculation uses an exactly normalized geometric envelope and keeps the chain finite before taking the boundary-away limit at fixed \(\xi\).

No claim is made that every Anderson eigenstate is exactly exponential at all sites, that the envelope has no fluctuations, or that \(\bar C\) is universally linear in a localization length defined by an arbitrary estimator. The conclusion is narrower: normalization of the source's own exponential ansatz removes the quadratic power in its Eq. (8).

## Proof

For any normalized one-particle state, the pair concurrence is \(C_{ij}=2|\psi_i\psi_j|\). Hence
\[
\sum_{i<j}C_{ij}
=
\left(\sum_i |\psi_i|\right)^2
-
\sum_i |\psi_i|^2
=
\left(\sum_i |\psi_i|\right)^2-1.
\]
This is the source's Eq. (6).

For the normalized continuum exponential,
\[
1
=
A^2\int_{-\infty}^\infty e^{-2|x|/\xi}\,dx
=
A^2\xi,
\]
so \(A=\xi^{-1/2}\). Therefore
\[
2\int_0^\xi A e^{-x/\xi}\,dx
=
2\sqrt\xi(1-e^{-1}),
\]
whose square is proportional to \(\xi\), not \(\xi^2\). Integrating over the whole line gives \(2\sqrt\xi\), so the full-profile concurrence mass is \(4\xi-1\).

For the discrete profile, normalization gives
\[
Z_L=\sum_{n=-L}^L r^{2|n|},
\]
while
\[
S_L=\sum_{n=-L}^L r^{|n|}.
\]
Substitution into the exact concurrence identity immediately yields
\[
K_L:=M\bar C_L=\frac{S_L^2}{Z_L}-1.
\]
At fixed \(0<r<1\), letting \(L\to\infty\) gives
\[
S_\infty=\frac{1+r}{1-r},
\qquad
Z_\infty=\frac{1+r^2}{1-r^2},
\]
and straightforward simplification gives
\[
K_\infty
=
\frac{2r(r^2+r+2)}{(1-r)(1+r^2)}.
\]
Finally, substituting \(r=e^{-1/\xi}\) and expanding at \(1/\xi=0\) yields the stated asymptotic series.

## Verification

The bundled script `artifacts/verify.py` reconstructs \(K_L\) from direct pairwise concurrence sums for a grid of finite chains and compares those sums with \(S_L^2/Z_L-1\). It also checks convergence to the closed infinite-boundary formula, the normalized continuum identities, the source-truncated coefficient, and the displayed large-\(\xi\) asymptotic.

The recorded run in `artifacts/verification_output.txt` returns `VERIFY_OK`. These computations are supplementary; the proof above is analytic.

## Relationship to prior work

Li and Wang's paper explicitly defines \(\bar C\) through the normalized one-particle amplitudes, introduces the exponential localization ansatz, and then prints the quadratic estimate in Eq. (8). The present claim is a correction to that normalization-dependent step, not a replacement for the paper's numerical study.

Earlier and closely related one-particle entanglement papers connect participation ratios or squared concurrence to localization. In particular, Li, Wang and Hu derive an exact participation-ratio relation for average squared concurrence in the Frenkel--Kontorova setting. That result concerns \(\langle C^2\rangle\), not the \(L^1\)-based average concurrence \(\bar C\) used here, so it does not imply the normalization correction above.

Searches using the exact source identifier, the paper title, average-concurrence and localization-length terminology, normalized exponential aliases, and correction/erratum terminology did not locate a published statement equivalent to the corrected linear law. This is evidence of noncoverage, not a proof that no unindexed note exists.

## Limitations

The result isolates a normalization artifact in a model calculation. Real Anderson eigenstates need not be exact two-sided exponentials, and finite boundaries, envelope fluctuations, and the operational definition of localization length can affect quantitative comparisons. The source's qualitative observation that stronger localization tends to reduce average concurrence is not contradicted by this correction.

A residual originality risk is that the same normalization correction may exist in an unindexed comment, note, or differently worded calculation.

## References

1. H. Li and X. Wang, *Localized Entanglement in one-dimensional Anderson model*, arXiv:quant-ph/0403178, first public 2004-03-25; DOI 10.1142/S0217984905008487.
2. H. Li, X. Wang and B. Hu, *Mode entanglement of electrons in the one-dimensional Frenkel-Kontorova model*, arXiv:quant-ph/0308118.
3. H. Li, B. Hu and X. Wang, *Bipartite entanglement and localization of one-particle states*, arXiv:quant-ph/0308116.
4. A. Lakshminarayan and V. Subrahmanyam, *Entanglement sharing in one-particle states*, arXiv:quant-ph/0212049.
