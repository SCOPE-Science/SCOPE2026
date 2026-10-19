# Exact complex-Gaussian randomized Ritz tails and a logarithmic mean-angle penalty

## Finding

The square complex-Gaussian randomized Rayleigh–Ritz (RRR) pencil can have a sharp distinction between high-probability eigenpair convergence and mean-square performance, even for a positive-semidefinite diagonal matrix with a simple exterior target eigenvalue. The following is an **exact finite-sample distributional result**, not an asymptotic simulation.

Fix real numbers \(a,b>0\), and let \(0<\theta<\pi/2\). Set
\[
A=\operatorname{diag}(0,a,b),\qquad
w_1=(\cos\theta,0,\sin\theta)^\mathsf T,\quad
w_2=e_2,\quad W=[w_1,w_2].
\]
Draw \(\Omega\in\mathbb C^{3\times2}\) with independent standard circular complex-normal entries, \(\mathcal{CN}(0,1)\). Form the generalized compressed eigenproblem
\[
\Omega^*AWy=\mu\Omega^*Wy.
\]
Here \(W\) is orthonormal and \(\Omega^*W\) is invertible almost surely. Define the randomized eigenvalue branch \(\mu\) by continuation from the eigenvalue zero as \(\theta\downarrow0\), and let \(\widehat v\) be its unit-normalized randomized Ritz vector. The other compressed eigenvalue is exactly \(a\); the branch labels are algebraically unambiguous except on a null event.

Write
\[
s=\sin\theta,\quad c=\cos\theta,\quad
\beta=bs^2,\quad \gamma=bsc,\qquad
q=\frac{\gamma^2}{(a-\beta)^2+\gamma^2}\in(0,1].
\]
For the squared sine of the angle to the true eigenvector \(e_1\),
\[
S=1-|e_1^*\widehat v|^2,
\]
there is the **exact law**
\[
S\ \stackrel{d}{=}\ s^2+c^2\frac{qV}{U+qV},
\qquad U,V\ \text{independent }\operatorname{Exp}(1).
\]
In particular, for \(0\le z\le1\),
\[
\Pr\!\left\{\frac{S-s^2}{c^2}\le z\right\}
=\frac{z}{q+(1-q)z},
\]
and
\[
\boxed{\quad \mathbb ES=s^2+c^2\,\Phi(q),\qquad
\Phi(q)=\frac{q(q-1-\log q)}{(1-q)^2}\quad(0<q<1),\qquad
\Phi(1)=\tfrac12.\quad}
\]
The unrefined randomized eigenvalue has the exact shifted radial tail
\[
\Pr\{\,|\mu-\beta|>t\,\}=\frac{\gamma^2}{t^2+\gamma^2}\quad(t\ge0),
\]
so \(\mathbb E|\mu|^2=\infty\) for every \(0<\theta<\pi/2\), even though \(\mu\to0\) in probability as \(\theta\downarrow0\).

For fixed \(a,b>0\) as \(\theta\downarrow0\),
\[
\boxed{\quad\mathbb ES
=2\frac{b^2}{a^2}\,\theta^2\log(1/\theta)+O(\theta^2).\quad}
\]
The deterministic Hermitian Rayleigh–Ritz vector on the *same* trial space is exactly \(w_1\), with squared sine error \(s^2\sim\theta^2\). Thus the ratio of randomized expected squared-angle error to the deterministic squared-angle error grows without bound, at the precisely identified logarithmic rate.

## Assumptions and scope

The matrix is finite-dimensional, Hermitian positive semidefinite and diagonal, with the eigenvalue zero simple. The trial space is precisely the two-dimensional subspace specified above. The random test matrix is **square with respect to the trial dimension** and consists of independent standard circular complex Gaussians; no oversampling, symmetrization, truncation, or residual-based rejection is performed. All assertions concern exact arithmetic. The labeled eigenbranch is the eigenvalue converging to zero in probability, not whichever eigenvalue happens to be numerically closest to zero after observing a particular sketch.

The result proves neither an infinite-dimensional statement nor a bound for an arbitrary Hermitian matrix or trial subspace. A real-Gaussian sketch has different heavy-tail exponents and is not covered by the formulas.

## Proof

1. **Exact compressed pencil.** Let \(u=-se_1+ce_3\). Then \([w_1,e_2,u]\) is an orthonormal basis, and \(Aw_1=\beta w_1+\gamma u\), while \(Ae_2=ae_2\). Put \(G=\Omega^*W\) and \(h=\Omega^*u\). Almost surely \(G\) is invertible; with \(r=G^{-1}h=(r_1,r_2)^\mathsf T\),
\[
G^{-1}\Omega^*AW=\begin{pmatrix}\beta+\gamma r_1&0\\\gamma r_2&a\end{pmatrix}.
\]
Thus the eigenbranch of interest is \(\mu=\beta+\gamma r_1\). As long as \(\mu\ne a\), its coefficient eigenvector is proportional to \((1,\eta)^\mathsf T\), where
\[
\eta=-\frac{\gamma r_2}{a-\beta-\gamma r_1}.
\]
Since \(r_1\) has a continuous law, \(\mu=a\) has probability zero. Consequently \(\widehat v=(w_1+\eta e_2)/\sqrt{1+|\eta|^2}\) up to a unit complex phase, and
\[
S=s^2+c^2\frac{|\eta|^2}{1+|\eta|^2}.
\]

2. **Exact projective Gaussian representation.** The \(2\times3\) matrix \([G,h]=\Omega^*[w_1,e_2,u]\) has independent standard complex-normal entries. Its kernel is almost surely a random one-dimensional subspace whose law is invariant under every unitary transformation of \(\mathbb C^3\). It is therefore Haar-distributed on complex projective two-space. The kernel is spanned by \((-r_1,-r_2,1)^\mathsf T\), whereas a Haar random line is spanned by \((Z_1,Z_2,Z_3)^\mathsf T\) with independent \(Z_j\sim\mathcal{CN}(0,1)\). Absorbing signs into these symmetric Gaussians gives
\[
(r_1,r_2)\stackrel d=(Z_1/Z_3,Z_2/Z_3).
\]
In particular \(\eta\) has the same distribution as \(-\gamma Z_2/[(a-\beta)Z_3-\gamma Z_1]\). The denominator \(D=(a-\beta)Z_3-\gamma Z_1\) is independent of \(Z_2\) and is circular complex normal with variance \((a-\beta)^2+\gamma^2\). Hence \(|\eta|^2\stackrel d=qV/U\), with independent \(U,V\sim\operatorname{Exp}(1)\). This proves the asserted law for \(S\).

3. **Distribution and mean.** For \(0\le z\le1\),
\[
\Pr\{qV/(U+qV)\le z\}
=\Pr\{V/U\le z/[q(1-z)]\}
=\frac{z}{q+(1-q)z},
\]
with the endpoint interpreted by continuity. Differentiating yields density \(q/[q+(1-q)z]^2\) on \((0,1)\). Equivalently, using the ratio density of two independent unit exponentials,
\[
\mathbb E\frac{qV}{U+qV}
=\int_0^\infty\frac{q}{(r+q)(1+r)^2}\,dr
=\frac{q(q-1-\log q)}{(1-q)^2}.
\]
At \(q=1\), exchangeability of \(U,V\) gives mean \(1/2\), and the fraction is uniform on \([0,1]\). In particular, the resonance \(a=b\sin^2\theta\), whenever attainable, gives an exactly uniform normalized angle excess.

4. **Eigenvalue tail and infinite second moment.** The complex Gaussian ratio satisfies
\[
\Pr\{|Z_1/Z_3|^2>x\}
=\mathbb E e^{-x|Z_3|^2}=\frac1{1+x}\quad(x\ge0).
\]
Since \(\mu-\beta\stackrel d=\gamma Z_1/Z_3\), this proves the stated tail. Integrating \(\Pr\{|\mu-\beta|^2>t\}\) over \(t\) proves that its second moment diverges. A finite deterministic shift \(\beta\) does not make the second absolute moment finite. At the same time \(\gamma\to0\) and \(\beta\to0\), proving \(\mu\to0\) in probability.

5. **Logarithmic mean-angle asymptotic.** As \(\theta\downarrow0\), \(s=\theta+O(\theta^3)\), \(c=1+O(\theta^2)\), \(\beta=O(\theta^2)\), and
\[
q=(b/a)^2\theta^2+O(\theta^4).
\]
Direct expansion of the proven exact expression gives \(\Phi(q)=-q\log q+O(q)\), hence
\[
\mathbb ES=2(b/a)^2\theta^2\log(1/\theta)+O(\theta^2).
\]
Finally, the deterministic compressed matrix \(W^*AW=\operatorname{diag}(\beta,a)\) has Ritz eigenvector \(w_1\) for its branch near zero, giving squared sine exactly \(s^2\). This completes the comparison.

## Verification

The standalone `verify.py` evaluates the integral identity with high-precision quadrature, tests the small-angle coefficient, verifies the resonance case, constructs the compressed matrices from independent complex-Gaussian sketches, and compares their eigenbranch and eigenvector statistics with the exact CDF, expectation and eigenvalue tail. It checks the reduced triangular form directly. Run with `python verify.py` using Python 3, NumPy and mpmath; the script raises an exception if a test fails. Random sampling supplies finite consistency checks, **not** the proof of the exact law or infinite second moment.

## Relationship to prior work

Shao (2026, arXiv:2604.01037, first public version April 1, 2026) introduced this square complex-Gaussian RRR pencil and established nonasymptotic, high-probability eigenpair convergence, including a probabilistic linear bound for Ritz-vector angles. Section 5.3 experimentally studies success frequencies. Those guarantees do not give the present exact angle distribution, mean-square logarithmic coefficient, or infinite second moment of the unrefined eigenvalue. There is no contradiction: a random variable can converge in probability while its second moment is infinite.

Nakatsukasa and Tropp's sketched Rayleigh–Ritz analysis uses embedding sketches, typically with oversampling, and compares sketched and standard compressed problems. Its §6.8 notes that sketching Hermitian problems need not yield real eigenvalues; it does not establish the square Gaussian law derived here. Haas and Nakatsukasa (2025) give sharp deterministic Rayleigh–Ritz eigenvalue bounds, but not this random test-space distribution.

The complex Gaussian ratio and its heavy tails are classical probability facts. The mathematical claim here is their exact propagation through the **specific randomized eigenpencil and normalized eigenvector geometry**. Earlier literature may contain an equivalent specialized distribution under different terminology; this is a bibliographic limitation rather than a proven uniqueness assertion.

## Limitations

This is a tractable model with a diagonal \(3\times3\) matrix and a two-dimensional trial space. It demonstrates a genuine boundary of interpreting high-probability convergence as mean-square convergence, not failure of the underlying algorithm on typical sketches. It does not establish the rate for arbitrary matrices, oversampled versions, alternative eigenpair-selection policies, symmetrized projections, or real Gaussian tests. The unrefined complex Ritz value is used for the infinite-second-moment statement; a refined real Rayleigh quotient of a Hermitian matrix is bounded and does **not** share that divergence.

## References

1. N. Shao, *Stabilizing the Rayleigh–Ritz procedure by randomization*, arXiv:2604.01037v1, first public April 1, 2026. https://arxiv.org/html/2604.01037v1
2. Y. Nakatsukasa and J. A. Tropp, *Fast Randomized Algorithms for Linear Systems and Eigenvalue Problems*, §6 (sketched Rayleigh–Ritz), available draft. https://tropp.caltech.edu/drafts/NT21-Fast-Accurate-draft.pdf
3. I.-B. Haas and Y. Nakatsukasa, *Sharp error bounds for approximate eigenvalues and singular values from subspace methods*, arXiv:2506.01207, first public June 1, 2025. https://arxiv.org/pdf/2506.01207
