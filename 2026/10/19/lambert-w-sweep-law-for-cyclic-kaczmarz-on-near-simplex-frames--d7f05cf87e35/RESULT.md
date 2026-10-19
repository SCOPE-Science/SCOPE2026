# Lambert-W sweep law for cyclic Kaczmarz on near-simplex frames

## Finding
For each integer \(n\ge 2\) and each \(0<\alpha<1\), consider any invertible real \(n\)-by-\(n\) matrix \(A_n\) whose rows have norm one and whose distinct rows have common inner product \(-\alpha/(n-1)\). Perform exactly one unrelaxed cyclic Kaczmarz projection on each row, in any fixed order. Let \(K_n(\alpha)\) be the resulting linear error-propagation operator. Then its spectral radius \(r_n(\alpha)\) has the following **exact and asymptotically sharp classification**.

Define \(x_n=x_n(\alpha)>0\) to be the unique solution of
\[
\frac{1}{n-1}\sum_{k=1}^{n-1}\exp\!\left(\frac{kx_n}{n}\right)=\frac1\alpha.
\]
Then
\[
\boxed{r_n(\alpha)=\exp(-x_n).}
\]
This is the exact spectral factor per complete row sweep, independent of the fixed ordering. For each fixed \(0<\alpha<1\),
\[
\boxed{\lim_{n\to\infty} r_n(\alpha)=r_\infty(\alpha)
=-\frac{\alpha}{W_{-1}(-\alpha e^{-\alpha})},}
\]
where \(W_{-1}\) is the real lower branch of Lambert's \(W\) function. Equivalently, \(r_\infty(\alpha)=e^{-x}\), where \(x>0\) uniquely solves \((e^x-1)/x=1/\alpha\).

The finite-dimensional correction is explicit. Write
\[
I(x)=\frac{e^x-1}{x},\qquad E(x)=\frac{1+e^x}{2},\qquad I'(x)=\frac{(x-1)e^x+1}{x^2}.
\]
For fixed \(0<\alpha<1\), with \(x=-\log r_\infty(\alpha)\),
\[
x_n=x+\frac{E(x)-I(x)}{(n-1)I'(x)}+O_\alpha(n^{-2}),
\]
so \(r_n(\alpha)<r_\infty(\alpha)\) for all sufficiently large \(n\), and the first finite-size correction is strictly positive in the exponent.

The convergence law has sharp, qualitatively distinct parameter ends:
\[
\boxed{r_\infty(\alpha)\sim\frac{\alpha}{\log(1/\alpha)}\quad(\alpha\downarrow0),}
\qquad
\boxed{1-r_\infty(\alpha)\sim2(1-\alpha)\quad(\alpha\uparrow1).}
\]
More strongly, for every \(n\ge2\), putting \(\varepsilon=1-\alpha\),
\[
\boxed{r_n(1-\varepsilon)=1-2\varepsilon+
\frac{4n-2}{3n}\varepsilon^2+O(\varepsilon^3).}
\]
The remainder can be chosen uniformly for all integers \(n\ge2\). Thus the **near-simplex first-order spectral gap is exactly twice the Gram spectral gap, uniformly in dimension**. At \(\alpha=1\) the Gram matrix is singular; that boundary is excluded from the theorem.

## Assumptions and scope

The system \(A_n z=b\) is consistent and uniquely solvable. The rows of \(A_n\) are nonzero and normalized to unit norm, and all pairwise inner products are exactly \(-\alpha/(n-1)\). The update on row \(i\) is the exact Euclidean orthogonal projection
\[
z\longmapsto z-(a_i^{\mathsf T}z-b_i)a_i.
\]
One sweep uses each row once, in a fixed order; the same fixed order repeats on subsequent sweeps. All statements concern exact real arithmetic. The spectral radius is an *asymptotic per-sweep error multiplier*, not an assertion that the one-sweep Euclidean operator norm equals that number.

Such matrices exist: the prescribed row Gram matrix is
\[
G_n=\left(1+\frac\alpha{n-1}\right)I_n-
\frac\alpha{n-1}\mathbf1\mathbf1^{\mathsf T}.
\]
Its eigenvalues are \(1-\alpha>0\) on constants and \(1+\alpha/(n-1)>0\) on the orthogonal complement. Hence the positive-definite square root of \(G_n\) supplies an admissible \(A_n\). As \(\alpha\) increases to one, the row geometry approaches a regular simplex and loses one rank.

## Proof

**1. Reduction to a positive Gauss--Seidel sweep.** Set \(\beta=\alpha/(n-1)\). Let \(L\) and \(U=L^{\mathsf T}\) be the strictly lower and upper triangular matrices with every entry strictly below or above the diagonal equal to one. Then \(G_n=I_n-\beta(L+U)\). Under the invertible change of variables \(z=A_n^{\mathsf T}y\), the projection on row \(i\) becomes the exact coordinate minimization \(y_i\mapsto y_i-(G_ny)_i\). A full sweep therefore acts in \(y\)-coordinates by
\[
T_n=(I_n-\beta L)^{-1}\beta U.
\]
The Kaczmarz sweep \(K_n\) is similar to \(T_n\), and consequently their spectral radii are equal. Any fixed row ordering gives the same coefficient matrix after reindexing, because every permutation leaves \(G_n\) unchanged.

The first column of \(T_n\) vanishes. The principal submatrix on indices \(2,\ldots,n\) is strictly positive entrywise: \((I_n-\beta L)^{-1}=I_n+\beta L+\cdots+(\beta L)^{n-1}\) is nonnegative, and every entry in the indicated principal block of its product with \(\beta U\) receives a positive contribution through index one. Thus the Perron--Frobenius theorem identifies the spectral radius with a simple strictly positive eigenvalue, and a strictly positive eigenvector is sufficient to identify it.

**2. Exact Perron root.** Consider the polynomial
\[
P(t)=t^{n-1}-\beta\sum_{j=0}^{n-2}t^j.
\]
It is negative at zero and strictly positive at one, since \(\beta(n-1)=\alpha<1\). Its coefficient signs have exactly one change; Descartes' rule and continuity therefore give exactly one positive root \(t_n\in(0,1)\). The polynomial equation is equivalent to
\[
t_n^{n-1}=\beta\frac{1-t_n^{n-1}}{1-t_n}.
\]
For \(v=(1,t_n,\ldots,t_n^{n-1})^{\mathsf T}\), the first component of \(T_nv=t_n^n v\) follows immediately from \(t_n^n=\beta\sum_{j=1}^{n-1}t_n^j\). For consecutive coordinates, subtracting the two equations
\[
\beta\sum_{j>i}v_j=t_n^n\left(v_i-\beta\sum_{j<i}v_j\right)
\]
leaves precisely \(t_n^n(1+\beta-t_n)=\beta t_n\), which follows from the polynomial identity. The first equation and all consecutive differences establish the entire eigenvector relation. Since \(v>0\), Perron--Frobenius gives
\[
\rho(T_n)=t_n^n.
\]
Writing \(t_n=e^{-x_n/n}\) and dividing the polynomial identity by \(t_n^{n-1}\) gives
\[
\frac1{n-1}\sum_{k=1}^{n-1}e^{kx_n/n}=\frac1\alpha.
\]
The left side increases strictly from one to infinity, so the positive \(x_n\) is unique. An initial error proportional to \(A_n^{\mathsf T}v\) contracts in norm by the exact factor \(r_n(\alpha)\) on every full sweep. Hence the spectral factor is attained by a real error trajectory; it is not just a formal complex-eigenvalue bound.

**3. Dimension limit and Lambert branch.** For fixed \(\alpha\), let \(S_n(y)=(n-1)^{-1}\sum_{k=1}^{n-1}e^{ky/n}\). On every compact interval of nonnegative \(y\), these interior Riemann averages converge uniformly to
\[
I(y)=\int_0^1e^{uy}\,du=\frac{e^y-1}{y},\qquad I(0)=1.
\]
The limit is continuous and strictly increasing from one to infinity. Monotone root continuity yields \(x_n\to x\), the unique positive solution \(I(x)=1/\alpha\). Rearranging gives \(e^x=1+x/\alpha\). With \(w=-x-\alpha\), this becomes \(we^w=-\alpha e^{-\alpha}\). The principal Lambert branch gives \(w=-\alpha\), hence \(x=0\), the unwanted removable solution arising from multiplication by \(x\). The strictly positive solution is instead
\[
x=-\alpha-W_{-1}(-\alpha e^{-\alpha}),
\]
which gives \(e^{-x}=-\alpha/W_{-1}(-\alpha e^{-\alpha})\).

**4. Finite-size correction.** For fixed \(y\) in a compact interval, the trapezoidal rule applied to \(e^{uy}\) yields
\[
\frac1n\left(\frac{1+e^y}{2}+\sum_{k=1}^{n-1}e^{ky/n}\right)
=I(y)+O(n^{-2}).
\]
Rearranging shows, uniformly on that interval,
\[
S_n(y)=I(y)+\frac{I(y)-E(y)}{n-1}+O(n^{-2}).
\]
Since \(I'(x)=\int_0^1u e^{ux}\,du>0\), the implicit root expansion gives
\[
x_n-x=\frac{E(x)-I(x)}{(n-1)I'(x)}+O(n^{-2}).
\]
Strict convexity of \(e^{ux}\) on \([0,1]\) for \(x>0\) makes its trapezoidal endpoint average \(E(x)\) strictly greater than its integral \(I(x)\). This proves the sign and the exact first correction.

**5. Two endpoint laws.** The relation \(\alpha=x/(e^x-1)\) gives, when \(\alpha\downarrow0\), \(x\to\infty\) and
\[
x=\log(1/\alpha)+\log x+o(1),\qquad
x/\log(1/\alpha)\to1.
\]
Since \(e^{-x}=\alpha/(x+\alpha)\), it follows that \(r_\infty(\alpha)\sim\alpha/\log(1/\alpha)\).

For the near-simplex endpoint put \(\varepsilon=1-\alpha\). The Taylor identity \(I(x)=1+x/2+x^2/6+O(x^3)\) gives \(x=2\varepsilon+(2/3)\varepsilon^2+O(\varepsilon^3)\) and hence \(r_\infty(1-\varepsilon)=1-2\varepsilon+(4/3)\varepsilon^2+O(\varepsilon^3)\).

For finite \(n\), the exact first two derivatives of \(S_n\) at zero satisfy
\[
S_n(0)=1,\quad S_n'(0)=\frac12,\quad
S_n''(0)=\frac{2n-1}{6n}.
\]
Taylor expansion of \(S_n(x_n)=1/(1-\varepsilon)\) therefore gives
\[
x_n=2\varepsilon+\frac{2(n+1)}{3n}\varepsilon^2+O(\varepsilon^3),
\]
and exponentiation yields the stated coefficient \((4n-2)/(3n)\) in \(r_n\). The remainders can be bounded uniformly in \(n\): the derivatives \(S_n^{(j)}(y)\) on bounded \(y\)-intervals are uniformly bounded by \(e^{|y|}\), and \(S_n'(0)=1/2\) uniformly. This completes the proof.

## Verification
The included `VERIFY.py` reconstructs complete exact-rational Gauss--Seidel sweep matrices and independently simulates coordinate corrections for multiple dimensions and coupling strengths. It checks that the predicted geometric eigenvector is indeed an eigenvector, that the eigenvalue matches the numerically computed full spectral radius, that Gram matrices are positive definite, and that the Perron block is strictly positive. Further checks compare the Lambert law, first finite-dimensional correction and two endpoint expansions with numerical roots. The script passed 307 checks in the supplied environment. None of these finite tests substitute for the analytical proof of statements with infinitely many parameters or limiting quantifiers.

For the parameter \(\alpha=1/2\), the limiting per-sweep spectral factor is approximately \(0.2846681370408385\). For \(n=2\), the exact factor is \(\alpha^2\), which at this parameter equals \(0.25\). The finite-size factors approach the limiting factor from below at the checked dimensions.

## Relationship to prior work
Yu and Diakonikolas (2026) motivate precise cyclic Kaczmarz convergence guarantees and give general characterization and bounds in terms of the input matrix; the available abstract does not resolve this signed-equicorrelation limit. Sun and Ye (2016), Section 4.3 and Lemma 4.1, establish a characteristic-root representation for the **positive** equicorrelation family and analyze the singular positive-correlation limit, where cyclic ordering can perform badly. The characteristic-polynomial approach is accordingly credited, not claimed as new. Lee and Wright (2018/2019), Sections 1--3, explicitly define the broader permutation-invariant Gram family allowing either sign of off-diagonal correlation and derive the Gauss--Seidel sweep matrix, but their quantitative cyclic-rate comparison and sharp estimates are developed in the small-positive-\(\delta\) regime corresponding to **positive** off-diagonal correlations; they do not state the Lambert-branch negative-correlation limit, its finite-size correction, or the uniform near-simplex expansion derived above. These are the precise claims assessed here.

The comparison with positive-correlation examples is structural, not a claim that this proof supplies improved rates for those examples. Both regular-simplex frames and their near-singular perturbations are standard objects; their geometry and the base Gauss--Seidel representation are prior knowledge. The derived rate law is an explicit evaluation, not a claim of discovering the underlying algorithm.

## Limitations
The model requires an exactly permutation-invariant **negative** row-correlation Gram matrix, equal unit row norms, a square invertible system and exact cyclic projections; these assumptions are restrictive. No universal rate for arbitrary nearly-simplex row systems or inaccurate projections is asserted. The spectral factor does not generally equal the worst-case induced Euclidean norm of one sweep, and the bounds say nothing about finite-precision roundoff near \(\alpha=1\).

The most relevant contemporary motivating manuscript, arXiv:2609.32034, was verified from its public bibliographic record and abstract, but its complete manuscript could not be accessed for a line-by-line comparison. This is a concrete residual priority for independent literature review. Unindexed equivalent results may also exist. The proofs here are self-contained conditional on standard Perron--Frobenius theory, the elementary trapezoidal-error formula, and the defining branches of Lambert's \(W\) function.

## References
1. R. Yu and J. Diakonikolas, *Tight Convergence Bounds for the Classical Kaczmarz Method*, arXiv:2609.32034v1, first posted September 25, 2026. https://arxiv.org/abs/2609.32034
2. R. Sun and Y. Ye, *Worst-case Complexity of Cyclic Coordinate Descent: O(n²) Gap with Randomized Version*, arXiv:1604.07130, first posted April 25, 2016, especially Section 4.3 and Lemma 4.1. https://arxiv.org/abs/1604.07130
3. C.-p. Lee and S. J. Wright, *Random permutations fix a worst case for cyclic coordinate descent*, IMA Journal of Numerical Analysis 39 (2019), 1246--1275; published online July 27, 2018, DOI:10.1093/imanum/dry040; especially Sections 1--3. https://doi.org/10.1093/imanum/dry040
