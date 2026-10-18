# Uniform Hilbert–Schmidt crossover at the differential Hilbert endpoint

## Finding
Let \(-1<\alpha<0\) and let the normalized weighted Bergman Hilbert spaces \(A^2_\gamma\) use the probability measure \((\gamma+1)(1-|z|^2)^\gamma\,dA(z)\), where \(dA\) is normalized planar area. Consider the differential Hilbert operator
\[
(\mathcal H_2 f)(z)=\int_0^1\frac{f(t)}{(1-tz)^2}\,dt.
\]
For \(\delta\ge0\), view this as a map \(\mathcal H_{\alpha,\delta}:A^2_\alpha\to A^2_{\alpha+2+\delta}\). Let \(P_N\) be the orthogonal projection to polynomials of degree less than \(N\), in the corresponding source and target spaces, and put
\[
S_N(\delta)=\|P_N\mathcal H_{\alpha,\delta}P_N\|_{\mathcal S_2}^2,
\qquad c_\alpha(\delta)=\Gamma(\alpha+4+\delta)\Gamma(-\alpha).
\]
For every fixed \(\alpha\in(-1,0)\), set \(\delta_0=\min\{1/4,-\alpha/2\}\). The following **uniform logarithmic-to-pole crossover** holds:
\[
\boxed{\displaystyle S_N(\delta)=c_\alpha(\delta)\sum_{n=1}^{N}n^{-1-\delta}+O_\alpha(1)
\quad(N\ge2,\ 0\le\delta\le\delta_0).}
\]
The error constant is independent of both \(N\) and \(\delta\). In particular, as \(N\to\infty\) with \(\delta_N\ge0\) and \(\delta_N\log N\to\tau\in[0,\infty)\),
\[
\boxed{\displaystyle\frac{S_N(\delta_N)}{\log N}\longrightarrow
\Gamma(\alpha+4)\Gamma(-\alpha)\,\frac{1-e^{-\tau}}{\tau},}
\]
where the continuous value at \(\tau=0\) is \(1\). Meanwhile, for every \(\delta>0\) the full operator is Hilbert–Schmidt, and
\[
\boxed{\displaystyle\lim_{\delta\downarrow0}\delta\|\mathcal H_{\alpha,\delta}\|_{\mathcal S_2}^2=\Gamma(\alpha+4)\Gamma(-\alpha).}
\]
At \(\delta=0\), the full operator is not Hilbert–Schmidt and \(S_N(0)=\Gamma(\alpha+4)\Gamma(-\alpha)\log N+O_\alpha(1)\). The two formulas therefore resolve the exact competition between spectral truncation and approach to the noncompact boundary.

## Assumptions and scope
All dimensions are scalar and all Hilbert spaces are complex. The parameter \(\alpha\) is fixed in \((-1,0)\); the uniform estimate requires \(0\le\delta\le\delta_0\), where \(\delta_0\) depends on \(\alpha\). For the unrestricted Hilbert–Schmidt statement, any fixed \(\delta>0\) is permitted. Projections are taken in the orthonormal monomial bases of each space. The claim does not assert a sharp operator norm, a full singular-value distribution, or uniformity as \(\alpha\to0\) or \(\alpha\to-1\).

## Proof
For \(\gamma>-1\), the monomial norm squared is
\[
w_n(\gamma)=\|z^n\|_{A^2_\gamma}^2
=\frac{\Gamma(\gamma+2)\Gamma(n+1)}{\Gamma(n+\gamma+2)}.
\]
Expanding \((1-tz)^{-2}\), the matrix element between orthonormal source and target monomials is exactly
\[
b_{nk}(\delta)=\frac{n+1}{n+k+1}
\sqrt{\frac{w_n(\alpha+2+\delta)}{w_k(\alpha)}}
\qquad(n,k\ge0).
\]
Thus \(S_N(\delta)=\sum_{0\le n,k<N}|b_{nk}(\delta)|^2\).

For \(\delta\in[0,\delta_0]\), the Gamma-ratio expansion, uniformly on this compact parameter interval, gives for integers \(n,k\ge1\)
\[
\begin{split}
w_n(\alpha+2+\delta)&=\Gamma(\alpha+4+\delta)n^{-\alpha-3-\delta}(1+O_\alpha(n^{-1})),\\
w_k(\alpha)^{-1}&=\Gamma(\alpha+2)^{-1}k^{\alpha+1}(1+O_\alpha(k^{-1})).
\end{split}
\]
Define the untruncated squared row norm \(r_n(\delta)=\sum_{k=0}^\infty |b_{nk}(\delta)|^2\). Replacing the Gamma ratios and the factors \((n+1)/(n+k+1)\) by their leading expressions changes the result by \(O_\alpha(n^{-2-\delta})\): indeed the \(k^{-1}\) correction is bounded by a constant multiple of \(\int_0^\infty t^\alpha/(n+t)^2\,dt=O_\alpha(n^{\alpha-1})\), and the endpoint \(k=0\), integral-sum comparison, and \(n^{-1}\) corrections are no larger. The remaining integral is
\[
\int_0^\infty\frac{t^{\alpha+1}}{(n+t)^2}\,dt
=n^\alpha B(\alpha+2,-\alpha)
=n^\alpha\Gamma(\alpha+2)\Gamma(-\alpha).
\]
It follows, uniformly in \(\delta\), that
\[
\boxed{r_n(\delta)=\Gamma(\alpha+4+\delta)\Gamma(-\alpha)n^{-1-\delta}
+O_\alpha(n^{-2-\delta}).}
\]
The row \(n=0\) has uniformly finite squared norm, because its \(k\)-summand is \(O_\alpha(k^{\alpha-1})\) and \(\alpha<0\). Summing the row asymptotics therefore yields
\[
\sum_{n=0}^{N-1}r_n(\delta)=c_\alpha(\delta)\sum_{n=1}^N n^{-1-\delta}+O_\alpha(1).
\]
(The one-index shift changes the sum by a uniformly bounded amount.)

It remains to estimate the omitted column tail. Uniform Gamma-ratio inequalities give
\[
|b_{nk}(\delta)|^2\le C_\alpha
(n+1)^{-\alpha-1-\delta}(k+1)^{\alpha-1},
\qquad 0\le n<N\le k.
\]
Since \(\delta_0<-\alpha\), summing this inequality first over \(k\ge N\) and then over \(n<N\) yields
\[
\sum_{n<N}\sum_{k\ge N}|b_{nk}(\delta)|^2
\le C_\alpha N^{\alpha}\sum_{n<N}(n+1)^{-\alpha-1-\delta}
\le C'_\alpha N^{-\delta}\le C'_\alpha.
\]
Subtracting proves the stated uniform finite-section formula.

For \(\delta>0\), the same row estimate with \(\delta\) fixed proves \(\sum_{n,k\ge0}|b_{nk}(\delta)|^2<\infty\), hence the full operator is Hilbert–Schmidt. Uniformly for \(0<\delta\le\delta_0\), the full squared norm equals \(c_\alpha(\delta)\zeta(1+\delta)+O_\alpha(1)\); since \(\delta\zeta(1+\delta)\to1\), its residue is \(c_\alpha(0)\). The row asymptotic at \(\delta=0\) instead yields divergence of the full squared norm.

Finally, the uniform integral comparison
\[
\sum_{n=1}^N n^{-1-\delta}=\frac{1-N^{-\delta}}{\delta}+O(1)
\]
(for \(\delta=0\), interpret the main term as \(\log N\)) proves the double-scaling limit by dividing by \(\log N\) and taking \(\delta_N\log N\to\tau\). Every stated limit and boundary follows.

## Verification
The identities can be checked by expanding the kernel in powers of \(z\), integrating each monomial over the normalized weighted disk, and comparing the resulting finite matrix with the coefficient formula above. The included standalone `verify.py` independently computes weighted monomial norms from Gamma functions, forms finite sections, tests the matrix trace identity and monotonicity under increasing truncation size, and records finite-size crossover ratios. These computations check normalization and behavior but do not prove the infinite-parameter limits, for which the uniform integral/summation estimates above are essential.

## Relationship to prior work
Li and Zhou (2026) identify the boundedness, compactness, sharp critical operator norm, and Schatten membership of this differential Hilbert operator between weighted Bergman spaces; their results do not state the present *uniform finite-section Hilbert–Schmidt crossover coefficient*. Tang and Zhang (2022/2024) establish Hilbert–Schmidt criteria for generalized Hilbert operators on Bergman spaces, without this two-weight near-critical limit. Pushnitski (2021) and Štampach (2022) establish general spectral-density results for symmetric homogeneous Hardy kernels and finite Hilbert-type matrices, but do not give the displayed two-parameter two-weight Hilbert–Schmidt transition. The standard Gamma-ratio and beta-integral tools are used as established facts. Published general methods may provide alternate proofs of parts of the result; no novelty is claimed for them.

## Limitations
The asymptotic concerns squared Hilbert–Schmidt norms, not individual singular values, spectral multipliers, the operator norm, or an endpoint eigenvalue classification. The error bound need not be uniform at the endpoints of the admissible \(\alpha\) interval. Although relevant primary articles were compared, unindexed equivalent two-weight asymptotics remain a historical-priority risk. An independent audit has not been performed.

## References
- S. Li and M. Zhou, *The Differential Hilbert Operator Between Weighted Bergman Spaces*, arXiv:2610.05672 (first posted 2026-10-05), https://arxiv.org/abs/2610.05672.
- P. Tang and X. Zhang, *Generalized Hilbert Operator Acting on Bergman Spaces*, arXiv:2208.10747 (2022), https://arxiv.org/abs/2208.10747.
- A. Pushnitski, *The spectral density of Hardy kernel matrices*, arXiv:2103.12642 (2021), https://arxiv.org/abs/2103.12642.
- F. Štampach, *The Hilbert L-matrix: spectral properties, asymptotics and determinants*, arXiv:2202.04116 (2022), https://arxiv.org/abs/2202.04116.
