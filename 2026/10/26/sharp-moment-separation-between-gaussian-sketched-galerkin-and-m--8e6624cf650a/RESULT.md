# Sharp moment separation between Gaussian-sketched Galerkin and minimal-residual Krylov solvers

## Finding

Consider two widely used choices for solving an SPD linear system with a fixed Krylov space: sketched Galerkin orthogonality and sketched Euclidean residual minimization. Although both may satisfy arbitrarily high-probability approximation guarantees after sufficient oversampling, their unconditional error moments are fundamentally different.

For each real \(p>0\), every nonterminal \(k\)-step Lanczos space and every real Gaussian sketch with \(\ell\ge k\) rows obey
\[
\mathbb E\|x_F-x_*\|_A^p<\infty\quad\Longleftrightarrow\quad p<1,
\qquad
\mathbb E\|x_G-x_*\|_A^p<\infty\quad\Longleftrightarrow\quad p<\ell-k+1.
\]
Here \(x_*\) is the exact solution, \(x_F\) the sketched Galerkin approximation, and \(x_G\) the sketched minimal-residual approximation. At the critical exponent the corresponding moment is infinite. In particular, no finite number of Gaussian sketch rows makes the unconditional Galerkin mean error finite. This is an exact-arithmetic distributional result, not a claim that large errors are typical.

More sharply, put \(H=V^TAV\), let \(\beta>0\) be the next Lanczos coefficient, \(a=\beta H^{-1}e_k\), \(c=\beta\|b\|_2e_k^TH^{-1}e_1\), and let \(f\) be the density below. Define the affine hyperplane \(\mathcal H=\{g\in\mathbb R^k:a^Tg=-1\}\) with Euclidean surface measure \(d\sigma\). Then
\[
\lim_{R\to\infty}R\Pr\{\|x_F-x_*\|_A>R\}
=\frac{2|c|}{\|a\|_2}\int_{\mathcal H}\sqrt{g^TH^{-1}g}\,f(g)\,d\sigma(g)\in(0,\infty).
\]

## Assumptions and scope

Let \(n\ge2\), \(A\in\mathbb R^{n\times n}\) be symmetric positive definite, and \(b\in\mathbb R^n\setminus\{0\}\). Use exact-arithmetic Lanczos initialized at \(v_1=b/\|b\|_2\). Assume its first \(k\) orthonormal vectors form \(V\in\mathbb R^{n\times k}\), where \(1\le k<n\), and the next recurrence does not break down:
\[
AV=VH+\beta v_{k+1}e_k^T,\qquad H=V^TAV\succ0,\quad\beta>0,
\quad V^Tv_{k+1}=0,\quad\|v_{k+1}\|_2=1.
\]
As a genuine Lanczos tridiagonal matrix, \(H\) has all its subdiagonal entries strictly positive. Let \(S\in\mathbb R^{\ell\times n}\) have independent \(N(0,1/\ell)\) entries, with any fixed integer \(\ell\ge k\). The sketch is independent of the deterministic system. Define \(x_*:=A^{-1}b\) and \(\|z\|_A:=\sqrt{z^TAz}\).

Sketched Galerkin means finding \(x_F=Vy_F\) such that
\[
(SV)^TS(b-AVy_F)=0.
\]
Sketched minimal residual means \(x_G=Vy_G\), with \(y_G\) minimizing \(\|S(b-AVy)\|_2\). Both coefficient vectors exist uniquely almost surely; for Galerkin this follows from the continuous density of a nonconstant affine denominator, and for minimal residual from the full column rank of a Gaussian image of the rank-\(k\) matrix \(AV\).

## Proof

**1. The exact Gaussian regression law.** Let \(Z\in\mathbb R^{\ell\times k}\) and \(w\in\mathbb R^\ell\) be independent standard Gaussian arrays. Their regression coefficient
\[
g:=(Z^TZ)^{-1}Z^Tw
\]
has the isotropic density
\[
f_{k,\ell}(g)=\frac{\Gamma((\ell+1)/2)}{\pi^{k/2}\Gamma((\ell-k+1)/2)}
(1+\|g\|_2^2)^{-(\ell+1)/2},\qquad g\in\mathbb R^k.
\]
This follows either by Gaussian-Wishart integration or by applying rotational invariance to the augmented \(\ell\times(k+1)\) Gaussian matrix. Writing \(\nu=\ell-k+1\), radial integration against this density gives
\[
\mathbb E\|g\|_2^p<\infty\quad\Longleftrightarrow\quad p<\nu
\]
for every \(p>0\), with logarithmic divergence at equality. Indeed, the radial density at infinity is comparable to \(r^{-\nu-1}\). The distribution is the usual multivariate Student law with \(\nu\) degrees of freedom and isotropic coordinate scale \(\nu^{-1/2}\).

**2. Galerkin is a hyperplane-pole rational function.** Because \(SV\) and \(Sv_{k+1}\) are independent Gaussian matrices/vectors after scaling by \(\sqrt\ell\), the projected equation becomes
\[
(H+\beta ge_k^T)y_F=\|b\|_2e_1.
\]
Put \(y_0=\|b\|_2H^{-1}e_1\), \(a=\beta H^{-1}e_k\), and \(c=\beta e_k^Ty_0\). Sherman–Morrison gives
\[
y_F=y_0-\frac{cH^{-1}g}{1+a^Tg}.
\]
The coefficient \(c\) is nonzero. In fact, by the cofactor formula for a nonsingular irreducible tridiagonal matrix, the off-corner inverse entry \(e_k^TH^{-1}e_1\) is a nonzero signed product of all adjacent Lanczos coefficients divided by \(\det H\). Also \(a\ne0\).

The deterministic Galerkin approximation \(Vy_0\) is the exact orthogonal projection of \(x_*\) onto \(\operatorname{range}(V)\) in the energy inner product. Pythagoras therefore gives the precise random error identity
\[
\boxed{\quad
\|x_F-x_*\|_A^2
=\|Vy_0-x_*\|_A^2+
\frac{c^2g^TH^{-1}g}{(1+a^Tg)^2}.
\quad}
\]
The denominator vanishes on the affine hyperplane \(\mathcal H\), which does not contain the origin; thus the numerator is strictly positive on that entire plane. The Student density is continuous and strictly positive there. Integrating transversely across any bounded positive-measure patch of \(\mathcal H\) proves divergence for every \(p\ge1\), since the local singularity is a positive multiple of \(|u|^{-p}\).

Conversely, for \(0<p<1\), split the integration into \(|1+a^Tg|\ge1\) and its complement. On the first region the random term is bounded by a constant multiple of \(\|g\|_2^p\), integrable because \(p<1\le\nu\). On the second region decompose \(g=su+z\), where \(u=a/\|a\|_2\) and \(z\perp u\). The strip constrains \(s\) to a bounded interval. There, the density is bounded by a constant times \((1+\|z\|_2^2)^{-(\ell+1)/2}\), and the numerator is at most a constant multiple of \((1+\|z\|_2)^p\). Transverse integration of \(|1+\|a\|_2s|^{-p}\) is finite and the remaining integral over \(\mathbb R^{k-1}\) converges because \(p<1\le\ell-k+1\). For \(k=1\), this is the ordinary zero-dimensional surface integral. Thus exactly the orders \(p<1\) are finite.

**3. The sharp Galerkin tail.** Let \(D=\|Vy_0-x_*\|_A\). The exact error identity shows that, for \(R>D\), the event \(\|x_F-x_*\|_A>R\) is equivalent to
\[
|1+a^Tg|<|c|\sqrt{g^TH^{-1}g}/\sqrt{R^2-D^2}.
\]
Use the coordinate transverse to \(\mathcal H\): \(g=g_0+z+su\), where \(g_0=-a/\|a\|_2^2\), \(z\perp u\), and \(u=a/\|a\|_2\). The transverse window collapses onto \(s=0\) with length asymptotic to \(2|c|\sqrt{(g_0+z)^TH^{-1}(g_0+z)}/(R\|a\|_2)\). For sufficiently large \(R\), the window lies in \(|s|\le C(1+\|z\|_2)/R\); integrating the Student density in that strip gives an integrable domination on \(z\perp u\) because its dimension is \(k-1\) and \(\ell\ge k\). Dominated convergence gives the displayed hyperplane integral. The constant is finite by the same radial bound and strictly positive because \(g\ne0\) on \(\mathcal H\). In particular, the Galerkin error tail has exactly order \(R^{-1}\), independently of oversampling.

**4. Minimal residual has the ordinary Student integrability frontier.** Set \(B=AV\), let \(y_*=\operatorname*{argmin}_{y}\|b-By\|_2\), and put \(r=b-By_*\). The residual is nonzero. Otherwise the exact solution would belong to \(\operatorname{range}(V)\), contradicting \(\beta e_k^Ty_0\ne0\) in the Lanczos residual of its Galerkin approximation. Let \(L=(B^TB)^{1/2}\succ0\) and \(Q=BL^{-1}\), so \(Q^TQ=I_k\) and \(Q^Tr=0\). Gaussian invariance implies \(\sqrt\ell SQ\) and \(\sqrt\ell S(r/\|r\|_2)\) are independent standard Gaussian arrays, whence
\[
y_G=y_*+\|r\|_2L^{-1}g',
\]
where \(g'\) has the density \(f_{k,\ell}\). The error \(x_G-x_*\) is a fixed vector plus \(\|r\|_2VL^{-1}g'\). Because \(VL^{-1}\) has full column rank, the energy norm of the variable term is bounded above and below by positive multiples of \(\|g'\|_2\). Adding a fixed vector does not alter which positive moments exist. The criterion is therefore exactly \(p<\ell-k+1\), including divergence at equality.

This completes all statements for arbitrary positive real moment order and arbitrary nonterminal Lanczos step.

## Verification

The bundled `verify.py` recomputes the Galerkin rank-one coefficient identity with exact fractions for a three-dimensional SPD tridiagonal example, compares predicted and directly solved sketched FOM systems, independently solves sketched least-squares residual equations for multiple Lanczos dimensions and sketch sizes, and verifies the Student density normalization and representative finite fractional moments. It is run as `python verify.py` with NumPy. Finite tests do not prove either infinite-moment threshold; the density integration and hyperplane arguments above do so.

For an explicit dimension-three witness, choose \(A=\begin{psmallmatrix}2&1/2&0\\1/2&3&1/2\\0&1/2&4\end{psmallmatrix}\), \(b=e_1\), and the two-step Krylov space \(V=[e_1,e_2]\). Then \(H^{-1}=\frac1{23}\begin{psmallmatrix}12&-2\\-2&8\end{psmallmatrix}\) and the sketched Galerkin denominator is \((23-g_1+4g_2)/23\), exposing the exact singular line \(g_1-4g_2=23\). With \(\ell=3\), the Galerkin mean error diverges but the minimal-residual mean error exists (its second moment diverges); with \(\ell=4\), the minimal-residual second error moment also exists.

## Relationship to prior work

The sketched Galerkin, sketched FOM and sketched GMRES constructions, together with high-probability embedding guarantees, occur in the primary literature listed below. In particular, the finite-dimensional rational projected equations and classical Gaussian regression/Student laws are prior mathematical ingredients. The present result concerns their combination into exact *unconditional* error integrability frontiers on every nonterminal SPD Lanczos space, the singular-hyperplane mechanism for Galerkin, and a sharp positive Galerkin error-tail constant. The statements do not follow from high-probability guarantees alone. The same unregularized sketched Galerkin formula is discussed in randomized projection approaches to model reduction.

## Limitations

The hypotheses require deterministic SPD data, a genuine nonterminal Lanczos step, independent unconditioned real Gaussian sketch rows, and exact arithmetic. The Galerkin calculation does not apply to regularized, rejected, safeguarded, conditioned-on-success, or truncated sketches. Once the Krylov method converges exactly, both errors are zero. These facts do not quantify how frequently extreme events occur at a practical fixed tolerance, nor do they establish stability properties for finite-precision implementations, other sketch distributions or general nonsymmetric operators. Published precedence cannot be ruled out by bounded literature searches; the described distributional thresholds remain subject to external independent review.

## References

1. C. Timsit, L. Grigori, and O. Balabanov, *Randomized Orthogonal Projection Methods for Krylov Subspace Solvers*, arXiv:2302.07466 (first posted 2023-02-15), Sections 2–5 and numerical comparisons. https://arxiv.org/abs/2302.07466
2. S. Güttel and M. Schweitzer, *Randomized Sketching for Krylov Approximations of Large-Scale Matrix Functions*, arXiv:2208.11447 (first posted 2022-08-24), sketched FOM and GMRES constructions. https://arxiv.org/abs/2208.11447
3. Y. Nakatsukasa and J. A. Tropp, *Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, arXiv:2111.00113 (first posted 2021-10-29), randomized minimal residual and embedding analysis. https://arxiv.org/abs/2111.00113
4. O. Balabanov and A. Nouy, *Randomized Linear Algebra for Model Reduction. Part I: Galerkin Methods and Error Estimation*, arXiv:1803.02602 (first posted 2018-03-07), Section 4.1 and Appendix. https://arxiv.org/abs/1803.02602
