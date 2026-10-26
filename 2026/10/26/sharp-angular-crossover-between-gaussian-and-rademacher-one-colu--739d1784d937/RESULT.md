# Sharp angular crossover between Gaussian and Rademacher one-column subspace iteration

## Finding

Consider the standard one-column randomized subspace iteration applied to an arbitrary rotation of a real positive-definite matrix with two unequal eigenvalues. Although Gaussian and independent Rademacher starting vectors are both isotropic, their expected squared Frobenius approximation errors have **an exact angular ordering that reverses across a sharp boundary at every finite power depth**.

Specifically, put \(a>b>0\), \(q\in\{0,1,2,\ldots\}\), \(\alpha=a^{2q+1}\), \(\beta=b^{2q+1}\), \(S=\alpha^2+\beta^2\), \(D=\alpha^2-\beta^2\), and \(T=\sin^2(2\theta)\). Write \(G_q\) for Gaussian expected squared Frobenius error and \(B_q(\theta)\) for the corresponding independent-sign error. Then

\[
G_q=b^2+(a^2-b^2)\frac{\beta}{\alpha+\beta},\qquad
B_q(\theta)=b^2+(a^2-b^2)\frac{\beta^2(S+DT)}{S^2-D^2T}.
\]

The latter is strictly increasing in \(T\). In particular, letting \(r=(b/a)^{2q+1}\) and \(T_c=(1+r^2)/(1+r)^2\),

\[
B_q(\theta)<G_q\quad\Longleftrightarrow\quad \sin^2(2\theta)<T_c,
\]

with equality precisely at \(T_c\) and the reverse strict inequality beyond it. Thus the sign sketch improves mean squared Frobenius error on a nonempty range of orientations but performs strictly worse around the diagonal orientations. At \(\theta=\pi/4\) modulo \(\pi/2\),

\[
B_q(\pi/4)=\frac{a^2+b^2}{2}\quad\text{for every integer }q\ge0,
\]

while \(G_q\to b^2\) as \(q\to\infty\). For \(0\le\theta\le\pi/2\), the interval on which the sign sketch is worse is exactly \(\lvert\theta-\pi/4\rvert<\delta_q\), with

\[
\delta_q=\frac12\arcsin\!\left(\frac{\sqrt{2r}}{1+r}\right)
\sim\frac{1}{\sqrt2}\left(\frac ba\right)^{q+1/2}
\quad(q\to\infty).
\]

Consequently the sign risk converges to the optimal squared rank-one error \(b^2\) at every fixed orientation outside the resonances, **but not uniformly in the orientation**, even as the number of subspace power steps increases.

## Assumptions and scope

Let \(R(\theta)=\begin{psmallmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{psmallmatrix}\) and

\[
A(\theta)=R(\theta)\begin{pmatrix}a&0\\0&b\end{pmatrix}R(\theta)^{\mathsf T},\qquad a>b>0.
\]

In exact real arithmetic, independently draw the two coordinates of the one-column vector \(\omega\) either from the standard normal law (Gaussian case) or independently from \(\{-1,+1\}\), each sign with probability one half (Rademacher case). Form \(y=A^{2q+1}\omega\), \(Q=y/\|y\|_2\), and \(\widehat A=QQ^{\mathsf T}A\). The quantity compared is \(\mathbb E\|A-\widehat A\|_F^2\), not the expected unsquared norm, the spectral norm, or a rank-truncated oversampled approximation. Since \(A\) is positive definite and \(\omega\ne0\) almost surely, \(Q\) is always defined. Both distributions have mean zero and covariance \(I_2\). The optimal deterministic rank-one squared Frobenius error is \(b^2\).

## Proof

**1. Exact residual for an arbitrary sketch direction.** Work in the eigenbasis of \(A\). For any starting direction with squared normalized leading coordinate \(t\in[0,1]\), the sketch \(y\) has squared components proportional to \(\alpha^2t\) and \(\beta^2(1-t)\). The projector trace identity gives

\[
\|A-QQ^{\mathsf T}A\|_F^2=\operatorname{tr}(A^2)-\frac{y^{\mathsf T}A^2y}{y^{\mathsf T}y}
=b^2+(a^2-b^2)\frac{\beta^2(1-t)}{\alpha^2t+\beta^2(1-t)}.\tag{1}
\]

This identity is valid also for the extreme directions \(t=0,1\), since \(\alpha,\beta>0\).

**2. Gaussian average.** A standard Gaussian direction has a uniform polar angle \(\varphi\) modulo \(2\pi\), independently of \(\theta\), so \(t=\cos^2\varphi\). For every \(\alpha,\beta>0\), direct substitution \(z=\tan\varphi\) in the four quadrants yields

\[
\frac1{2\pi}\int_0^{2\pi}\frac{d\varphi}{\alpha^2\cos^2\varphi+\beta^2\sin^2\varphi}=\frac1{\alpha\beta}.
\]

Alternatively combining this integral with the identity \(\alpha^2 I_c+\beta^2 I_s=1\), where \(I_c\) and \(I_s\) are the respective cosine- and sine-weighted integrals, and \(I_c+I_s=1/(\alpha\beta)\), gives \(I_s=1/[\beta(\alpha+\beta)]\). Multiplying by \(\beta^2\) in (1) proves the displayed formula for \(G_q\).

**3. Rademacher average.** The four sign vectors represent exactly two projective directions, each with probability one half. After rotation to the eigenbasis, their squared leading coordinates are

\[
t_+=\frac{1+\sin(2\theta)}2,\qquad t_-=\frac{1-\sin(2\theta)}2.
\]

Substitute \(t_\pm\) into (1). Putting \(u=\sin(2\theta)\), the mean of the two rational terms simplifies by a common denominator to

\[
\frac12\sum_{\varepsilon\in\{-1,1\}}\frac{\beta^2(1-t_\varepsilon)}{\alpha^2t_\varepsilon+\beta^2(1-t_\varepsilon)}
=\frac{\beta^2(S+Du^2)}{S^2-D^2u^2}.
\]

The denominator is at least \(S^2-D^2=4\alpha^2\beta^2>0\). Its derivative with respect to \(T=u^2\) is

\[
\frac{d}{dT}\left[\frac{\beta^2(S+DT)}{S^2-D^2T}\right]
=\frac{2\alpha^2\beta^2DS}{(S^2-D^2T)^2}>0,
\]

because \(\alpha>\beta>0\). This proves the Rademacher formula and strict monotonicity.

**4. Unique exact crossover.** Equating the excess risks above \(b^2\) and clearing positive denominators gives

\[
\beta^2\frac{S+DT}{S^2-D^2T}=\frac{\beta}{\alpha+\beta}
\quad\Longleftrightarrow\quad
T=\frac{S}{(\alpha+\beta)^2}=\frac{1+r^2}{(1+r)^2}.
\]

Since \(0<r<1\), \(1/2<T_c<1\), and strict monotonicity yields both inequalities and uniqueness of the crossing. At \(T=1\), one sign direction exactly annihilates the leading eigendirection, giving the error \(a^2\), while the other captures it exactly, giving the error \(b^2\); their average is \((a^2+b^2)/2\), independent of \(q\).

**5. Angular width and nonuniform power-depth limit.** For \(\theta\in[0,\pi/2]\), write \(\theta=\pi/4+\varepsilon\). Then \(T=\cos^2(2\varepsilon)\). The worse-than-Gaussian condition \(T>T_c\) is

\[
\sin^2(2\varepsilon)<1-T_c=\frac{2r}{(1+r)^2},
\]

which gives the stated \(\delta_q\) using \(\lvert 2\varepsilon\rvert\le\pi/2\). As \(r\downarrow0\), \(\arcsin(\sqrt{2r}/(1+r))\sim\sqrt{2r}\), and hence the claimed expansion follows. For any fixed \(T<1\), the Rademacher excess term is \(O(r^2)\) by its exact formula; at \(T=1\) the excess remains \((a^2-b^2)/2\). This proves pointwise (off resonance) but not uniform convergence. \(\square\)

## Verification

`verify.py` is a standalone Python standard-library checker. It independently enumerates all four sign vectors, constructs the exact rational \(2\times2\) matrix, forms \(A^{2q+1}\), and evaluates the projected Frobenius error using matrix arithmetic. For three spectral pairs, four rational rotations, and five power depths, it compares the exact direct mean against the theorem's closed form. Separate exact tests check diagonal and resonant orientations, the crossover equation, and strict inequalities, while an angular midpoint quadrature checks the Gaussian integral at three selected parameter tuples. It returned `VERIFY_OK 123`. Finite checks do not prove the universal quantifiers or the asymptotic statement; the proof above does.

To replay: extract `verify.py` beside this document and execute `python3 verify.py` with Python 3. No network, third-party packages, or input data are required.

## Relationship to prior work

Saibaba and Międlar's 2023 preprint studies randomized subspace iteration for non-Gaussian, notably Rademacher and other sub-Gaussian, sketches. Its Algorithm 1 is the same numerical primitive; its Theorem 5 gives an oversampling-dependent probability guarantee, not the exact unoversampled mean-square risk as a function of orientation, spectrum, and all power depths. The present statement specializes to exactly one sketch column and supplies a closed-form comparison where those general guarantees are not sharp.

Epperly and Webber's 2026 study proves minimax optimality of rotation-invariant embeddings in a regime requiring more sketch columns and reports qualitatively that low-dimensional sign sketches may annihilate leading eigenspace vectors. That qualitative annihilation phenomenon **is prior work**; the contribution asserted here is the complete quantitative crossover, finite-depth formulas, and boundary-layer width in the specified one-column planar model. Neither the minimax theorem nor the experiments imply the displayed exact formulas. The 2026 paper is used only as supporting literature, not as the date or ownership basis for the 2023-led research direction.

## Limitations

The theorem is confined to real \(2\times2\) SPD matrices, a single sketch vector, exact arithmetic, squared Frobenius loss, and independently sampled standard Gaussian or Rademacher coordinates. It is not a statement about the spectral-norm error, floating-point power-iteration behavior, the more common oversampled schemes, or higher dimensions. The pointwise limit excludes the exact resonant orientations. While full-text comparison did not identify an equivalent previously published phase diagram, an overlooked exact two-dimensional discrete-sketch calculation remains possible; the scientific originality assessment is not an independent literature certification.

## References

1. A. K. Saibaba and A. Międlar, *Randomized low-rank approximations beyond Gaussian random matrices*, arXiv:2308.05814v1, first publicly submitted 2023-08-10. https://arxiv.org/abs/2308.05814
2. E. N. Epperly and A. Webber, *Sharp analysis of sketched least squares and randomized low-rank approximation*, arXiv:2605.19096, 2026, §§3.1–3.3. https://arxiv.org/abs/2605.19096
3. N. Halko, P.-G. Martinsson, and J. A. Tropp, *Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions*, SIAM Review 53 (2011), 217–288; arXiv:0909.4061. https://arxiv.org/abs/0909.4061
