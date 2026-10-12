# Sharp norm-distortion descent envelope for exact sketched least-squares minimizers

## Finding

An exact sketched least-squares minimizer has an extra orthogonality structure that a general comparison of approximate objective values discards. Accounting for it gives the **sharp lower envelope** for the original quadratic improvement:

\[
\boxed{\frac{F(x_0)-F(\widehat x)}{G(\widehat x)}\ge \Psi_\varepsilon(\delta):=\frac{\delta-\varepsilon\sqrt{\delta(\delta+4)}}{1-\varepsilon^2}.}
\]

When the sketched relative decrease \(\delta\) is positive, nonincrease of the unsketched objective is guaranteed for **every** admissible problem precisely when

\[
\boxed{\delta\ge\delta_*(\varepsilon):=\frac{4\varepsilon^2}{1-\varepsilon^2}.}
\]

The bound and its threshold are sharp, already for a one-parameter, two-row real least-squares problem. The separate case \(\delta=0\) yields equality of true objectives, not ascent. For fixed \(\varepsilon\) the threshold is quadratic in small embedding distortion, improving the sufficient linear-in-distortion threshold of [1, Proposition 1] when the sketched quadratic is minimized exactly.

## Assumptions and scope

Fix integers \(n,N,s\ge1\), a nonempty affine trial set \(\mathcal U\subseteq\mathbb R^n\), a matrix \(T\in\mathbb R^{N\times n}\), a vector \(c\in\mathbb R^N\), and a current iterate \(x_0\in\mathcal U\). Set \(r(x)=Tx-c\), \(F(x)=\|r(x)\|_2^2\), and \(G(x)=\|Sr(x)\|_2^2\) for a linear map \(S:\mathbb R^N\to\mathbb R^s\). Let

\[
W=\operatorname{span}\{r(x):x\in\mathcal U\}.
\]

Require the **squared-norm** embedding, for every \(w\in W\),

\[
(1-\varepsilon)\|w\|_2^2\le\|Sw\|_2^2\le(1+\varepsilon)\|w\|_2^2,
\qquad 0\le\varepsilon<1.
\]

Let \(\widehat x\in\mathcal U\) be an **exact global minimizer** of \(G\) on \(\mathcal U\). Such minimizers exist for finite-dimensional least squares, and although \(\widehat x\) need not be unique as a parameter vector, its sketched residual is unique. For the main formula assume \(G(\widehat x)>0\), and define

\[
\delta=\frac{G(x_0)-G(\widehat x)}{G(\widehat x)}.
\]

For augmented fixed-weight Tikhonov quadratics, the formulation includes \(r(x)=\bigl(Ax-b,\sqrt\lambda Cx\bigr)\) with a suitable stacked sketch. The proof treats each residual as a single Euclidean vector; it makes no assertion about approximate sketched solvers, moving trial spaces that exclude \(x_0\), nonlinear objectives lacking a verified tangent-majorant relation, finite precision, or non-embedding outcomes of randomized sketches.

## Proof

**Sketched normal equations.** Write \(z=r(\widehat x)\) and \(h=r(x_0)-r(\widehat x)\). Because \(x_0\) belongs to the same affine trial set, the line \(\widehat x+t(x_0-\widehat x)\) stays in \(\mathcal U\). Differentiating the exact sketched least-squares objective at \(t=0\) gives

\[
\langle Sz,Sh\rangle=0,
\qquad G(x_0)=G(\widehat x)+\|Sh\|_2^2.
\]

Therefore \(\delta=\|Sh\|_2^2/\|Sz\|_2^2\). If \(\delta=0\), then \(Sh=0\); the lower embedding bound implies \(h=0\), so \(F(x_0)=F(\widehat x)\). Henceforth take \(\delta>0\).

**Equivalent metric.** The embedding with \(\varepsilon<1\) makes \(S\) injective on \(W\). On the image \(SW\), the inverse map \(S|_W^{-1}\) defines a positive-definite metric \(M\) by

\[
\langle u,Mv\rangle=\langle S|_W^{-1}u,S|_W^{-1}v\rangle.
\]

The embedding hypothesis is equivalent to the spectral bounds

\[
\frac{1}{1+\varepsilon}I\preceq M\preceq\frac{1}{1-\varepsilon}I.
\]

Put \(a=\|Sz\|_2=\sqrt{G(\widehat x)}\) and choose the orthonormal vectors \(e_1=Sz/a\) and \(e_2=Sh/(a\sqrt\delta)\) in \(SW\). Their \(2\times2\) metric compression, again denoted \(M\), satisfies the same eigenvalue bounds. Direct expansion gives

\[
\frac{F(x_0)-F(\widehat x)}{G(\widehat x)}
=\delta M_{22}+2\sqrt\delta M_{12}
=\operatorname{tr}(MK),
\quad K=\begin{pmatrix}0&\sqrt\delta\\\sqrt\delta&\delta\end{pmatrix}.
\]

**Sharp spectral minimization.** The two eigenvalues of \(K\) are

\[
\lambda_\pm=\frac{\delta\pm\sqrt{\delta(\delta+4)}}2,
\qquad \lambda_-<0<\lambda_+.
\]

Set \(\alpha=(1+\varepsilon)^{-1}\) and \(\beta=(1-\varepsilon)^{-1}\). Every admissible compressed metric has the form \(M=\alpha I+(\beta-\alpha)P\) for some \(0\preceq P\preceq I\). In an eigenbasis of \(K\), \(\operatorname{tr}(PK)\ge\lambda_-\), since the diagonal entries of \(P\) lie in \([0,1]\). It follows that

\[
\operatorname{tr}(MK)\ge\alpha\lambda_++\beta\lambda_-=
\frac{\delta-\varepsilon\sqrt{\delta(\delta+4)}}{1-\varepsilon^2}.
\]

The lower bound is attained by choosing \(P\) to be the orthogonal projector onto the negative eigendirection of \(K\). This proves both the displayed envelope and its optimality as a metric inequality.

**Every-parameter extremizer.** Fix \(0\le\varepsilon<1\) and \(\delta>0\). In \(\mathbb R^2\), take the metric \(M\) just constructed and its symmetric positive square root \(L=M^{1/2}\). Let \(S=L^{-1}\) and define the affine least-squares residual

\[
 r(x)=L\begin{pmatrix}1\\x\sqrt\delta\end{pmatrix},
\qquad x\in\mathbb R,\qquad x_0=1,\qquad\widehat x=0.
\]

The sketch satisfies \(Sr(x)=(1,x\sqrt\delta)^{\mathsf T}\), so \(\widehat x=0\) is the unique exact minimizer, \(G(\widehat x)=1\), and the relative sketched improvement is precisely \(\delta\). The eigenvalues of \(L^{-2}=S^{\mathsf T}S\) are \(1-\varepsilon\) and \(1+\varepsilon\), so the embedding bounds hold with equality in extremal directions. By construction the original improvement equals \(\Psi_\varepsilon(\delta)\). This realizes **every positive \(\delta\)** and every permitted distortion with only two rows and one free parameter.

**Exact nonexpansion frontier and endpoint cases.** For \(\delta>0\), the sign of \(\Psi_\varepsilon(\delta)\) is the sign of \(\sqrt\delta-\varepsilon\sqrt{\delta+4}\), hence it is nonnegative exactly when

\[
\delta(1-\varepsilon^2)\ge4\varepsilon^2.
\]

The extremizer shows that any strictly positive \(\delta\) below this frontier allows a strict increase in the original quadratic. For \(\delta\) at the threshold equality can occur; above it, original descent is strict. Separately \(\delta=0\) implies identical original residual vectors. Finally, if \(G(\widehat x)=0\), then \(Sr(\widehat x)=0\) and embedding injectivity forces \(r(\widehat x)=0\), so \(F(\widehat x)=0\) without needing a relative ratio.

## Verification

A standalone standard-library-only script, `verify.py`, is supplied. Run `python verify.py`. The script returned:

`VERIFY_OK rational_witness=1 sharp_extremizers_and_comparisons=5000`

An **exact rational extremizer** uses

\[
T=\begin{pmatrix}-3/2\\1\end{pmatrix},\quad
c=\begin{pmatrix}-2\\-1/3\end{pmatrix},\quad
S=\begin{pmatrix}2/5&3/5\\-1/5&6/5\end{pmatrix},
\quad x_0=1,\quad \widehat x=0.
\]

In this example \(Sr(x)=(1,3x/2)^{\mathsf T}\), \(S^{\mathsf T}S\) has eigenvalues \(1/5\) and \(9/5\), and

\[
\varepsilon=4/5,\quad G(\widehat x)=1,\quad
\delta=9/4,\quad F(\widehat x)=37/9,\quad
F(x_0)=73/36.
\]

Thus the true improvement is \(-25/12=\Psi_{4/5}(9/4)\), so a substantial sketched improvement can accompany true-objective ascent. The exact-rational check reconstructs each equality, and independent generated metrics check the sharp envelope numerically over 5,000 parameter pairs. **Finite checks do not establish the universal result; the proof above does.**

## Relationship to prior work

Sabaté Landman and Nakatsukasa [1, Proposition 1, equations (5.7)–(5.8)] derive true-objective monotonicity for sketch-and-solve flexible Krylov iteratively reweighted quadratic models when the relative sketched decrease is at least \(2\varepsilon/(1-\varepsilon)\) under their squared-norm comparison. That is a sufficient bound obtained by separately bounding two quadratic values; the first-order normal equations of the exact sketched minimizer are not exploited in that argument. For \(\varepsilon\in(0,1)\), the threshold proved here, \(4\varepsilon^2/(1-\varepsilon^2)\), is strictly smaller and **optimal**. The separate Proposition 2 in [1] concerns sketch-to-precondition algorithms that minimize the unsketched quadratic and thus does not subsume a sketched-objective acceptance threshold.

Epperly and Webber [2, Theorems 2.1–2.2 and Lemma 5.1] give optimal distributional and expectation results for the final sketch-and-solve residual relative to the best unsketched least-squares solution, not a deterministic sharp decrease test relative to a specified incumbent. Nakatsukasa and Tropp [3, Fact 2.2] establish quasi-optimal residual bounds under embeddings, again without an observed-improvement-dependent exact frontier. Pilanci and Wainwright [4] analyze randomized sketching errors and iterative Hessian sketch, rather than the present exact-minimizer acceptance quantity. Classical spectral rearrangement underlies the short two-dimensional proof; its novelty is not claimed.

A tangent quadratic majorant \(Q\) of a nonlinear objective \(f\), satisfying \(f(x)\le Q(x)\) and \(f(x_0)=Q(x_0)\), inherits a valid **conditional** nonlinear descent step whenever the new criterion proves \(Q(\widehat x)\le Q(x_0)\). A changing regularization parameter or an approximate sketched minimizer falls outside these assumptions.

## Limitations

The statement is deterministic and conditional on an actual squared-norm embedding over the entire residual span. Random sketch distributions require a separate success-probability analysis. Exact minimization and membership of the incumbent in the affine trial space are essential. The sharpness construction allows a square two-row sketch and does not claim that a particular randomized sketch distribution achieves the extremizer with positive probability. The result concerns Euclidean squared residuals (including fixed-weight stacked regularization); it is neither a multistep convergence theorem nor a finite-precision guarantee. A zero observed improvement is a tie, not a counterexample; a zero sketched optimum gives zero true residual. An equivalent form of this elementary spectral rearrangement may exist in older unindexed literature.

## References

[1] M. Sabaté Landman and Y. Nakatsukasa, *Randomized flexible Krylov methods for \(\ell_p\) regularization*, arXiv:2510.11237v1 (first posted 2025-10-13), especially Proposition 1, eqs. (5.7)–(5.8), and Proposition 2. https://arxiv.org/html/2510.11237v1

[2] E. N. Epperly and R. J. Webber, *Sharp analysis of sketched least squares and randomized low-rank approximation*, arXiv:2605.19096v2 (2026), Theorems 2.1–2.2 and Lemma 5.1. https://arxiv.org/html/2605.19096v2

[3] Y. Nakatsukasa and J. A. Tropp, *Fast and accurate randomized algorithms for linear systems and eigenvalue problems*, arXiv:2111.00113v2 (2022), Fact 2.2. https://arxiv.org/pdf/2111.00113

[4] M. Pilanci and M. J. Wainwright, *Iterative Hessian Sketch: Fast and Accurate Solution Approximation for Constrained Least-Squares*, Journal of Machine Learning Research 17(53), 1–38 (2016). https://www.jmlr.org/papers/volume17/14-460/14-460.pdf
