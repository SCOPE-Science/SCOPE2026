# Exact Fibonacci decorrelation cutoff and four resonant modes for the Arnold cat map

## Finding

Let \(A=\begin{pmatrix}2&1\\1&1\end{pmatrix}\), and let \(T:\mathbb T^2\to\mathbb T^2\) be the area-preserving automorphism \(T(x)=Ax\pmod{\mathbb Z^2}\). Write \(F_0=0\), \(F_1=1\), and \(F_{j+1}=F_j+F_{j-1}\). For every integer \(n\geq1\), the sharp frequency-return threshold is

\[
\min_{k\in\mathbb Z^2\setminus\{0\}}
\max\bigl\{\|k\|_\infty,\|A^nk\|_\infty\bigr\}=F_{n+1}.
\]

There are exactly **four** nonzero minimizing lattice vectors:

\[
\pm(F_n,-F_{n+1}),\qquad\pm(F_{n-1},-F_n).
\]

For integer \(K\geq1\), let \(\mathcal H_K\) be the complex mean-zero trigonometric polynomials on \(\mathbb T^2\) supported at Fourier frequencies \(k\) with \(\|k\|_\infty\leq K\), and let \(P_K\) be the orthogonal projection onto \(\mathcal H_K\). For the Koopman operator \(Uf=f\circ T\),

\[
P_KU^nP_K=0\quad\Longleftrightarrow\quad K<F_{n+1},
\]

and precisely at \(K=F_{n+1}\), the compression \(P_KU^nP_K\) has **rank four**. Equivalently, the connected lag-\(n\) Haar correlation of *every* pair of observables in \(\mathcal H_K\) is zero exactly when \(K<F_{n+1}\); at equality, some real cosine observables have correlation \(1/2\). Thus the smallest universal decorrelation lag for a prescribed integer bandwidth \(K\) is \(N(K)=\min\{n\geq1:F_{n+1}>K\}\), and \(N(K)=\log_\varphi K+O(1)\), where \(\varphi=(1+\sqrt5)/2\).

## Assumptions and scope

The torus is \(\mathbb T^2=\mathbb R^2/\mathbb Z^2\), endowed with normalized Haar probability measure. The frequency norm is the square (maximum-coordinate) norm \(\|(u,v)\|_\infty=\max\{|u|,|v|\}\); the exact Fibonacci cutoff is specific to this norm and this matrix. The time \(n\) is a positive integer; the bandwidth \(K\) is a nonnegative integer (at \(K=0\) the mean-zero space is trivial). All Fourier sums are finite; no smoothness assumptions beyond being trigonometric polynomials are needed. A connected correlation means

\[
\operatorname{Cov}_n(f,g)=
\int_{\mathbb T^2}\overline{f(x)}\,g(T^nx)\,dx
-\overline{\int_{\mathbb T^2}f\,dx}\int_{\mathbb T^2}g\,dx.
\]

The rank statement refers to a complex vector space. Real cosine and sine observables give equivalent sharp nonvanishing witnesses.

## Proof

**1. Fibonacci unimodular basis.** Define

\[
v_n=(F_n,-F_{n+1}),\qquad w_n=(F_{n-1},-F_n),\qquad C=F_{n+1}.
\]

Cassini's identity \(F_{n+1}F_{n-1}-F_n^2=(-1)^n\) implies \(\det(v_n,w_n)=(-1)^n\). Therefore every \(k\in\mathbb Z^2\) has a *unique* representation \(k=a v_n+b w_n\) with \(a,b\in\mathbb Z\). Since \(A=Q^2\) for \(Q=\begin{pmatrix}1&1\\1&0\end{pmatrix}\), write \(J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\). The columns of \(JQ^n\) are exactly \(v_n,w_n\). Symmetry and determinant \(\det Q=-1\) imply the exact all-index identity \(Q^nJQ^n=(-1)^nJ\), hence \(A^nJQ^n=(-1)^nQ^nJ\). Reading the two columns yields

\[
A^nv_n=(-1)^{n+1}(F_n,F_{n-1}),\qquad
A^nw_n=(-1)^n(F_{n+1},F_n).
\]

In particular, each of \(\pm v_n\) and \(\pm w_n\) has \(\max\{\|k\|_\infty,\|A^nk\|_\infty\}=C\), giving the upper bound.

**2. A two-coordinate integer obstruction.** Suppose \(\|k\|_\infty\leq C\) and \(\|A^nk\|_\infty\leq C\). The second coordinate of \(k=a v_n+b w_n\) is \(-aC-bF_n\). The first coordinate of \(A^nk\), up to the common sign \((-1)^n\), is \(-aF_n+bC\). Set \(r=F_n/C>0\). The two necessary inequalities are therefore

\[
|a+rb|\leq1,\qquad |b-ra|\leq1.
\]

Squaring and adding gives \((1+r^2)(a^2+b^2)\leq2\). Since \(a^2+b^2\) is a nonnegative integer and \(2/(1+r^2)<2\), it follows that \(a^2+b^2\leq1\). For nonzero \(k\), exactly one of \(a,b\) is \(\pm1\) and the other is zero. Consequently the *only* nonzero vectors satisfying both bounds at \(C\) are \(\pm v_n,\pm w_n\). They all attain the threshold, proving the minimax value and its complete equality classification. In particular no nonzero vector satisfies both strict inequalities \(\|k\|_\infty<C\) and \(\|A^nk\|_\infty<C\).

**3. Fourier correlation and rank.** For \(e_k(x)=e^{2\pi i k\cdot x}\), orthogonality and symmetry of \(A\) give \(U^ne_k=e_{A^nk}\). The compression \(P_KU^nP_K\) therefore maps a basis vector \(e_k\) to \(e_{A^nk}\) if both frequencies lie in the square band, and to zero otherwise. Because \(A^n\) is invertible over \(\mathbb Z\), distinct surviving input vectors give distinct outputs. Thus the rank equals the number of nonzero \(k\in\mathbb Z^2\) with \(\|k\|_\infty\leq K\) and \(\|A^nk\|_\infty\leq K\). Step 2 makes this count zero for \(K<C\), and exactly four for \(K=C\). For \(K\geq C\), at least one such pair persists, hence the operator is not zero.

If \(k=v_n\) and \(q=A^nk\), both have norm at most \(C\). Choosing \(f(x)=\cos(2\pi q\cdot x)\) and \(g(x)=\cos(2\pi k\cdot x)\) gives \(g(T^nx)=f(x)\) and \(\operatorname{Cov}_n(f,g)=\int f^2\,dx=1/2\). This proves sharpness within real-valued observables. The formula for \(N(K)\) follows from the strict monotonicity of the positive-index Fibonacci numbers after the repeated initial ones, and Binet's asymptotic formula proves \(N(K)=\log_\varphi K+O(1)\).

## Verification

The included standalone `CHECK.py` verifies the Fibonacci power identities and the determinant identity exactly for many lags. It also enumerates integer frequencies in the entire square of the predicted cutoff for \(1\leq n\leq9\), comparing the full set of exact minimizers with the four claimed vectors. This is a finite regression check, **not** an infinite proof. The arbitrary-lag result follows solely from the unimodular-basis and two-coordinate argument in the proof.

## Relationship to prior work

Fourier propagation under hyperbolic toral automorphisms is classical. Hu and Rosenhaus (2022) study correlation functions in the cat map via Fourier expansions, explicitly extending earlier work by Crawford and Cary. Moudgalya, Devakul, von Keyserlingk and Sondhi (2018) develop a Fourier-basis Koopman treatment of cat-map dynamics, especially for a different hyperbolic matrix. These works motivate the observable finite-band correlation question and provide the general Fourier-evolution framework.

The contribution here is **not** Fourier orthogonality itself, but the exact all-time integer minimax value for the canonical matrix and square bandwidth, its complete four-vector equality classification, and the resulting sharp operator cutoff and first-onset rank. These statements are not established by the general Fourier-propagation identity *without* the additional lattice minimization proved above. A separate result on coupled cat maps by Fouxon and Gutkin (2022) establishes qualitatively finite-time disappearance of certain finitely supported correlations in a different space-time system, rather than this single-map bandwidth threshold or its equality classification.

## Limitations

The result is restricted to the canonical matrix \(A\), square Fourier cutoff, Haar measure, positive integer lag and finite Fourier sums. It does not claim that arbitrary smooth or measurable correlations vanish at finite lag: unbounded Fourier spectra generally retain correlations. No statement is made about noninteger times, noisy maps or perturbations. The available abstract of Hu–Rosenhaus confirms its relevant Fourier-correlation topic, but the complete preprint was not accessible for line-by-line priority comparison; an earlier equivalent cutoff concealed in that source or older cat-map literature remains a genuine priority risk. A lack of search hits is not a proof of absolute novelty.

## References

1. X.-Y. Hu and V. Rosenhaus, *Correlation functions in linear chaotic maps*, arXiv:2204.13655, first posted 2022-04-28. https://arxiv.org/abs/2204.13655
2. S. Moudgalya, T. Devakul, C. W. von Keyserlingk and S. L. Sondhi, *Operator Spreading in Quantum Maps*, arXiv:1808.04889, first posted 2018-08-14. https://arxiv.org/abs/1808.04889
3. I. Fouxon and B. Gutkin, *Local correlations in coupled cat maps with space-time duality*, Journal of Physics A 55 (2022) 504004, DOI:10.1088/1751-8121/aca730.
