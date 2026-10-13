# A sharp Gaussian Hutch++ variance crossover on rank-two spectra

## Finding
Consider the three-matrix-vector-product **fully Gaussian Hutch++** estimator: one Gaussian range sketch, one exact projected-trace evaluation, and one independent Gaussian residual probe. On every nonzero positive-semidefinite matrix of rank two, its centered error is a positive random spectral factor times an independent centered chi-square variable. This gives an exact variance and a **sharp spectral transition** against the equal-cost three-probe Gaussian Hutchinson estimator.

Precisely, let \(A\in\mathbb R^{n\times n}\) be symmetric positive semidefinite, \(n\ge2\), of rank exactly two, with positive eigenvalues \(a\ge b>0\). Let \(g,z\sim N(0,I_n)\) be independent. Define
\[
q=Ag/\|Ag\|_2,\quad P=I_n-qq^\top,\quad
T_{++}=q^\top A q+z^\top PAPz.
\]
Here \(T_{++}\) uses exactly three matrix-vector products with \(A\): \(Ag\), \(Aq\), and \(A(Pz)\). For independent \(h_1,h_2,h_3\sim N(0,I_n)\), let
\[
T_H=\frac13\sum_{i=1}^3 h_i^\top Ah_i.
\]
Then \(\mathbb ET_{++}=\mathbb ET_H=\operatorname{tr}A=a+b\), and
\[
\boxed{\operatorname{Var}(T_{++})=\frac{ab(a^2+6ab+b^2)}{(a+b)^2},\qquad
\operatorname{Var}(T_H)=\frac23(a^2+b^2).}
\]
Write \(t=a/b\ge1\), \(u_*=(\sqrt{145}-1)/4\), and
\[
t_* =\frac{u_*+\sqrt{u_*^2-4}}2=2.331488011135\ldots.
\]
The comparison is exact:
\[
\begin{cases}
\operatorname{Var}(T_{++})>\operatorname{Var}(T_H), &1\le t<t_*,\\
\operatorname{Var}(T_{++})=\operatorname{Var}(T_H), &t=t_*,\\
\operatorname{Var}(T_{++})<\operatorname{Var}(T_H), &t>t_*.
\end{cases}
\]
Moreover, for an independent \(Z\sim N(0,1)\), there is a positive spectral random variable \(r\), independent of \(Z\), for which
\[
T_{++}-(a+b)\ \overset{d}=\ r(Z^2-1).
\]
Thus the overestimation probability is exactly \(\mathbb P(T_{++}>\operatorname{tr}A)=\mathbb P(Z^2>1)=1-\operatorname{erf}(1/\sqrt2)\), independent of the eigenvalues, whereas the variance ordering changes at \(t_*\). For each fixed ambient dimension, the two *strict* variance orderings also persist on nonempty open sets of full-rank positive-definite matrices near the corresponding rank-two examples.

## Assumptions and scope
The matrix dimension \(n\) is any finite integer at least two. All random vectors have independent standard real normal entries and the sketch and residual probe are independent. Multiplications and orthogonalization are exact. A rank-two matrix is allowed to be singular when \(n>2\); the sketch denominator is nonzero almost surely because \(a,b>0\). Variance is over both independent Gaussian stages. The baseline consumes exactly three oracle queries, as does the stated Hutch++ allocation. This compares two specified algorithms, **not** all possible three-query trace estimators.

## Proof
**1. Reduction and error factorization.** By rotational invariance, work in an orthonormal eigenbasis with \(A=\operatorname{diag}(a,b,0,\ldots,0)\). The Gaussian sketch direction in the positive range is \((\cos\theta,\sin\theta)\) with \(\theta\) uniform on \([0,2\pi)\). Set \(D=a^2\cos^2\theta+b^2\sin^2\theta\). Within that range,
\[
q=\frac{(a\cos\theta,b\sin\theta)}{\sqrt D},\qquad
v=\frac{(-b\sin\theta,a\cos\theta)}{\sqrt D}.
\]
The residual \(PAP\) is rank one with positive eigenvalue
\[
r=v^\top Av
=\frac{ab^2\sin^2\theta+ba^2\cos^2\theta}{D}
=\frac{ab}{a+b}\left(1+\frac{ab}{D}\right).
\]
The last identity follows after multiplying through by \((a+b)D\). As \(q,v\) are orthonormal and span the range of \(A\), \(q^\top Aq+r=a+b\). Conditional on \(g\), the scalar \(v^\top z\) is standard normal and its conditional law does not depend on \(g\). Consequently \(Z=v^\top z\) is independent of \(g\), and the estimator obeys the asserted \(r(Z^2-1)\) error factorization. It is centered conditionally on \(g\); \(r>0\) makes the overestimation event precisely \(Z^2>1\).

**2. Exact residual second moment.** For positive \(a,b\), elementary angular integration gives
\[
\frac1{2\pi}\int_0^{2\pi}\frac{d\theta}{D}=\frac1{ab},\qquad
\frac1{2\pi}\int_0^{2\pi}\frac{d\theta}{D^2}=\frac{a^2+b^2}{2a^3b^3}.
\]
For completeness, write \(D=\alpha+\beta\cos(2\theta)\), with \(\alpha=(a^2+b^2)/2\), \(\beta=(a^2-b^2)/2\). The standard tangent-half-angle integral \((2\pi)^{-1}\int(\alpha+\beta\cos\phi)^{-1}d\phi=(\alpha^2-\beta^2)^{-1/2}\) gives the first expression because \(\alpha^2-\beta^2=a^2b^2\). Differentiating with respect to \(\alpha\), holding \(\beta\) fixed, yields the second: \(\alpha/(\alpha^2-\beta^2)^{3/2}\). These operations are valid since \(\alpha>|\beta|\).

It follows by direct expansion that
\[
\mathbb E[r^2]
=\frac{a^2b^2}{(a+b)^2}\left(1+2ab\frac1{ab}+a^2b^2\frac{a^2+b^2}{2a^3b^3}\right)
=\frac{ab(a^2+6ab+b^2)}{2(a+b)^2}.
\]
Independence and \(\operatorname{Var}(Z^2)=2\) now give \(\operatorname{Var}(T_{++})=2\mathbb E[r^2]\). For \(T_H\), each independent Gaussian quadratic form has variance \(2\operatorname{tr}(A^2)=2(a^2+b^2)\); averaging three gives \(\operatorname{Var}(T_H)=2(a^2+b^2)/3\).

**3. Unique sharp crossover.** Substituting \(a=bt\) in the difference gives
\[
\operatorname{Var}(T_H)-\operatorname{Var}(T_{++})
=\frac{b^2}{3(t+1)^2}\left(2t^4+t^3-14t^2+t+2\right).
\]
The sign of the parenthesis, upon division by \(t^2>0\), is the sign of
\[
2(t+t^{-1})^2+(t+t^{-1})-18.
\]
For \(t\ge1\), \(u=t+t^{-1}\ge2\) is strictly increasing for \(t>1\), and \(2u^2+u-18\) is strictly increasing on \([2,\infty)\), negative at two and positive for large \(u\). Its unique zero in this interval is \(u_*=(\sqrt{145}-1)/4>2\). Solving \(t+t^{-1}=u_*\) for \(t\ge1\) gives the displayed unique \(t_*\) and the three cases. At \(a=b\), the variances are \(2a^2\) versus \(4a^2/3\); at \(a=3b\), they are \(21b^2/4\) versus \(20b^2/3\).

**4. Full-rank persistence.** Fix dimension \(n\ge3\) and rank-two \(A_0\) with positive eigenvalues having \(a/b\ne t_*\). For positive-semidefinite \(A\) near \(A_0\), the sketch projector \(q(A,g)q(A,g)^\top\) tends pointwise almost surely to the projector for \(A_0\) as \(A\to A_0\), since \(A_0g\ne0\) almost surely. Let \(B_A=(I-q q^\top)A(I-q q^\top)\). Conditional unbiasedness gives error \(z^\top B_Az-\operatorname{tr}B_A\), bounded in absolute value by \(\|A\|_2(\|z\|_2^2+n)\). On a bounded matrix neighborhood the square of this bound is integrable, so dominated convergence proves continuity of the Hutch++ variance. The Hutchinson variance \((2/3)\operatorname{tr}(A^2)\) is continuous. The nonzero gap at \(A_0\) therefore keeps its sign for all sufficiently small positive-definite perturbations, including \(A_0+\varepsilon I_n\) for small \(\varepsilon>0\).

## Verification
The standalone `verify.py` runs without third-party dependencies. It checks the closed variance and quartic relations with exact rational arithmetic, checks the two angular integrals and residual-moment formula by dense deterministic midpoint quadrature, verifies the unique crossover numerically, and simulates the actual three-query Gaussian estimator at three well-separated spectra. An observed `VERIFY_OK` is a transcription check; finite computations are **not** used to prove the universal rank-two theorem, uniqueness, or continuity.

## Relationship to prior work
Meyer, Musco, Musco and Woodruff introduced Hutch++ and stated its three-part query allocation, allowing Gaussian sketches and residual probes (Algorithm 1). Their Section 5 gives the general conditional-variance identity and a dimension-free bound; the Gaussian-sketch specialization called Gaussian-Hutch++ in their Algorithm 3 uses **sign-valued residual probes**, so it is not the fully Gaussian minimum-budget distribution studied here. The novel comparison is the closed, **rank-two full-average variance formula** and its unique exact equal-budget spectral transition, not the conditional-variance identity itself.

Persson, Cortinovis and Kressner study a Gaussian Hutch++ implementation, adaptive allocation and Nyström++ (Algorithms 1, 3 and 5). Their generic Gaussian Hutchinson variance formula agrees with the baseline, while their adaptive and Nyström analyses concern different allocation or approximation questions. In the inspected primary sections, no result states or implies the unique variance crossover without the additional rank-two residual angular calculation. The analysis is a precise benchmark of these fixed estimators, not an improvement to their general high-probability query complexity.

## Limitations
The exact variance threshold is proved only for rank-two positive-semidefinite spectra and the specified fully Gaussian **one-sketch, one-residual-probe** allocation; full-rank persistence concerns signs of variance differences, not a full-rank closed formula. It says nothing about stochastic trace estimators using Rademacher probes, adaptive resampling, other budgets, or their tail-risk ordering. In dimension two or when rank is known and favorable, alternative algorithms using two suitable matrix-vector products can recover the trace exactly; therefore the comparison is **not a query-optimality claim**. Strictly speaking, the Gaussian Hutch++ variant here differs from the Gaussian-sketch/Rademacher-residual choice of the original paper's separate Algorithm 3. Priority uncertainty remains for equivalent specialized formulas not located in the inspected publications.

## References
1. R. A. Meyer, C. Musco, C. Musco, and D. P. Woodruff, *Hutch++: Optimal Stochastic Trace Estimation*, arXiv:2010.09649, first public version 2020-10-19; Algorithm 1, Section 5, https://arxiv.org/html/2010.09649v5 .
2. D. Persson, A. Cortinovis, and D. Kressner, *Improved variants of the Hutch++ algorithm for trace estimation*, arXiv:2109.10659, first public version 2021-09-22; Algorithms 1, 3, 5 and Sections 2-3, https://arxiv.org/html/2109.10659v3 .
