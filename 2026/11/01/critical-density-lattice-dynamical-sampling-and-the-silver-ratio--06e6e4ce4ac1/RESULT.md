# Critical-density lattice dynamical sampling and the silver-ratio instability

## Finding

For each integer \(K\ge1\), set \((Rf)(n)=\tfrac12[f(n-1)+f(n+1)]\) on \(\ell^2(\mathbb Z)\). Let
\[
(\mathcal S_K f)_{q,s,t}=(R^t f)(2Kq+s),\qquad q\in\mathbb Z,\quad s\in\{0,1\},\quad 0\le t<K.
\]
Then \(\mathcal S_K\) is a bounded isomorphism of \(\ell^2(\mathbb Z)\) onto \(\ell^2(\mathbb Z\times\{0,1\}\times\{0,\ldots,K-1\})\). In particular the corresponding dynamical samples constitute a Riesz basis analysis system with critical, exactly unit information density.

Let \(H_K\) denote the explicit local analysis matrix below. Its determinant and asymptotic singular-value conditioning obey
\[
\boxed{|\det H_K|=2^{-K(K-1)}},\qquad
\boxed{\lim_{K\to\infty}\kappa_2(H_K)^{1/K}=1+\sqrt2}.
\]
Thus the optimal upper/lower frame-bound ratio has \(K\)-th root tending to \((1+\sqrt2)^2\). The latter rate is sharp: both matching upper and lower exponential estimates are established.

## Assumptions and scope

All sequences are complex-valued and square-summable. The averaging operator \(R=(S+S^{-1})/2\), with \(S\) the bilateral shift, is self-adjoint of norm one; it equals \(I-L\) for the normalized graph Laplacian \(L\) of the integer lattice. Only the prescribed **consecutive** times and the two **adjacent** sites per period are considered. The result is for each fixed finite \(K\), with the conditioning limit along positive integers \(K\to\infty\).

The disjoint blocks are
\[
B_q=\{2Kq-K+1,\ldots,2Kq+K\},\quad q\in\mathbb Z.
\]
Index the columns within \(B_0\) by \(0,1,-1,2,-2,3,\ldots,1-K,K\), in that order, and the rows by \((s,t)=(0,0),(1,0),(0,1),(1,1),\ldots,(0,K-1),(1,K-1)\). The entries are explicitly
\[
(H_K)_{(s,t),j}=
\begin{cases}
2^{-t}\binom{t}{(t+j-s)/2},&|j-s|\le t\text{ and }t+j-s\text{ is even},\\
0,&\text{otherwise}.
\end{cases}
\]
For \(K=1\), \(H_1=I_2\). Singular values use the unweighted Euclidean norm on each block; \(\kappa_2(H_K)=\sigma_{\max}(H_K)/\sigma_{\min}(H_K)\).

## Proof

**1. Exact block locality.** Binomial convolution gives
\[
(R^t f)(n)=2^{-t}\sum_{h=0}^{t}\binom th f(n+t-2h).
\]
For \(0\le t<K\) and \(s\in\{0,1\}\), the observed entries at \(2Kq+s\) only use indices in \(B_q\). The blocks partition \(\mathbb Z\) without gaps or overlap, hence \(\mathcal S_K\) is unitarily equivalent to the orthogonal direct sum of identical matrices \(H_K\). This is a statement about the infinite lattice, with no finite-volume approximation.

**2. Triangular structure and determinant.** At time zero the observations give \(f(0)\) and \(f(1)\). At time \(t\ge1\), the row at site zero introduces exactly one coordinate not seen at earlier times, namely \(f(-t)\), with coefficient \(2^{-t}\); its other new-side endpoint \(f(t)\) has already been reached from site one at time \(t-1\). Similarly the row at site one introduces \(f(t+1)\), also with coefficient \(2^{-t}\). In the displayed row/column orders, \(H_K\) is lower triangular with successive diagonal pairs \((2^{-t},2^{-t})\), \(0\le t<K\). Therefore
\[
|\det H_K|=\prod_{t=0}^{K-1}2^{-2t}=2^{-K(K-1)}.
\]
Invertibility of each finite matrix proves the bounded Riesz isomorphism for each fixed \(K\). Its *optimal* frame bounds are exactly \(A_K=\sigma_{\min}(H_K)^2\) and \(B_K=\sigma_{\max}(H_K)^2\).

**3. Chebyshev reconstruction.** Let \(T_j\) denote the first-kind Chebyshev polynomial, \(T_j(\cos\theta)=\cos(j\theta)\). Its Laurent-polynomial identity implies
\[
2T_j(R)f(n)=f(n-j)+f(n+j)\quad(j\ge1).
\]
Write \(y_{s,t}=(R^t f)(s)\), and let \(T_j(x)=\sum_{t=0}^j c_{j,t}x^t\). Starting with \(a_0=y_{0,0}=f(0)\) and \(b_0=y_{1,0}=f(1)\), calculate for \(1\le j<K\)
\[
\begin{aligned}
a_j=f(-j)&=2\sum_{t=0}^j c_{j,t}y_{0,t}-b_{j-1},\\
b_j=f(j+1)&=2\sum_{t=0}^j c_{j,t}y_{1,t}-a_{j-1}.
\end{aligned}
\]
This is a constructive exact inverse; note that \(b_{j-1}=f(j)\) and \(a_{j-1}=f(1-j)\). Every step uses only allowed measurements and previously reconstructed coordinates.

**4. Sharp upper exponential bound on inverse norm.** Coefficients of \(T_j\) alternate in sign by powers of two, so their \(\ell^1\) norm is \(|T_j(i)|\). Defining \(\alpha=1+\sqrt2\) and using \(T_j((z+z^{-1})/2)=(z^j+z^{-j})/2\) at \(z=i\alpha\) gives, for \(j\ge1\),
\[
\sum_{t=0}^j|c_{j,t}|=|T_j(i)|=
\tfrac12\big[\alpha^j+(-1)^j\alpha^{-j}\big].
\]
Repeated substitution in the explicit reconstruction equations bounds the \(\ell^1\)-norm of each row of \(H_K^{-1}\) by \(1+2\sum_{j=1}^{K-1}|T_j(i)|\le C\alpha^K\), with a numerical constant \(C\) independent of \(K\). The Frobenius bound yields \(\|H_K^{-1}\|_2\le C\sqrt{2K}\alpha^K\).

**5. Matching lower exponential bound.** For \(K\ge2\), the linear output functional \(2\sum_{t=0}^{K-1}c_{K-1,t}y_{0,t}\) equals \(f(-(K-1))+f(K-1)\). These are two distinct signal coordinates, so the coefficient vector of this functional in the reconstructed signal has Euclidean norm \(\sqrt2\). By the dual operator-norm inequality,
\[
\|H_K^{-1}\|_2\ge \sqrt2\left(\sum_{t=0}^{K-1}|c_{K-1,t}|^2\right)^{1/2}
\ge\sqrt{\frac2K}\,|T_{K-1}(i)|.
\]
Thus \(\|H_K^{-1}\|_2^{1/K}\to\alpha\). Each row of \(H_K\) is a nonnegative binomial probability vector, whose Euclidean norm is at most one, and the time-zero evaluation row has norm one. Hence
\[
1\le\|H_K\|_2\le\|H_K\|_{\mathrm F}\le\sqrt{2K}.
\]
It follows that \(\kappa_2(H_K)^{1/K}\to\alpha\). Squaring the condition number gives the asserted limiting frame-bound ratio. This proves all claims.

## Verification

The standalone standard-library script `checker.py` reconstructs each rational matrix \(H_K\) for \(1\le K\le7\), computes its determinant by exact fraction elimination, verifies the Chebyshev identity on every finite standard-basis signal, and checks the coefficient-sign identity. Its successful message is `CHECK_OK: exact block determinants, Chebyshev inversion, coefficient alternation (k=1..7)`. These are *finite consistency checks* only; the assertion for all \(K\) and the limiting growth rate follow from Steps 1–5, not from computation.

## Relationship to prior work

Bulai–Cabrelli–Cordero–Molter–Saliani (2026) study dynamical frames in graph Paley–Wiener spaces on the lattice and general graph operators, with numerical conditioning on finite paths. Their accessible theorem statements and detailed constructions do not supply this adjacent-sensor finite-propagation block model on the full lattice, its determinant, or the exact silver-ratio limit. The primary-MSC 42C15 survey of Aldroubi et al. (first public 2025-11-13) frames the stability question; earlier space–time trade-off literature provides general recovery conditions; that general recovery insight is not claimed as new here. The advance is the specified full-bandwidth critical-density frame, a local exact inverse, and the quantified sharp exponential instability.

## Limitations

This does not prove that the given sensor geometry is optimal among all spatial arrangements or dynamics. The growth limit describes the Euclidean singular-value condition number for a fixed number of adjacent sensors and consecutive powers. The individual finite-\(K\) extreme singular values have not been expressed in elementary closed form. No uniform stability bound in \(K\) is possible, since the condition number grows exponentially. Historical implicit treatments of the same particular local stencil and conditioning rate may exist; independent priority checking is warranted.

## References

1. I. M. Bulai, C. Cabrelli, E. Cordero, U. Molter, S. Saliani, “Dynamical Sampling in Graph Paley–Wiener Spaces,” arXiv:2609.25472v1 (public 2026-09-21), https://arxiv.org/abs/2609.25472 .
2. A. Aldroubi, C. Cabrelli, I. Krishtal, U. Molter, “Dynamical Sampling: A Survey,” arXiv:2511.10769, https://arxiv.org/abs/2511.10769 .
3. A. Aldroubi, J. Davis, I. Krishtal, “Exact Reconstruction of Signals in Evolutionary Systems via Spatiotemporal Trade-off,” *J. Fourier Anal. Appl.* 21 (2015), 11–31, https://doi.org/10.1007/s00041-014-9359-9 .
4. A. Aldroubi, J. Davis, I. Krishtal, “Dynamical Sampling: Time–Space Trade-off,” *Appl. Comput. Harmon. Anal.* 34 (2013), 495–503, https://doi.org/10.1016/j.acha.2012.09.002 .
