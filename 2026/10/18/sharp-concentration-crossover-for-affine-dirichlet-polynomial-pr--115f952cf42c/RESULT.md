# Uniform gamma approximation and the concentration crossover for affine Dirichlet projections

## Finding

Let \(L_{n,a}\) be either endpoint norm, \(L^1\to L^1\) or \(L^\infty\to L^\infty\), of the affine \(L^2\)-orthogonal projection for the symmetric Dirichlet probability measure with \(n\ge2\) parameters all equal to \(a>0\). The endpoint norms coincide. If \(G_a\) is unit-scale Gamma of shape \(a\), put
\[
g(a)=\mathbb E|G_a-a|=2a^a e^{-a}/\Gamma(a).
\]
The dimension-uniform comparison is
\[
\left|L_{n,a}/n-g(a)\right|\le \sqrt{na+1}/n.
\]
As \(n\to\infty\), for any positive sequence \(a_n\), writing \(\lambda_n=na_n\), one has:

* If \(\lambda_n\to c\in[0,\infty)\), then \(L_{n,a_n}\to1+2c\).
* If \(\lambda_n\to\infty\), then \(L_{n,a_n}\sim n g(a_n)\to\infty\), without any convergence hypothesis on \(a_n\).

In particular \(\sup_n L_{n,a_n}<\infty\) if and only if \(\sup_n\lambda_n<\infty\), including sequences with no limiting total concentration. In the divergent regime the equivalents are \(2na_n\) if \(a_n\to0\), \(ng(a_0)\) if \(a_n\to a_0\in(0,\infty)\), and \(n\sqrt{2a_n/\pi}\) if \(a_n\to\infty\).

## Scope and exact-norm input

Here \(n\) counts barycentric coordinates, and \(\mu_{n,a}=\operatorname{Dirichlet}(a,\ldots,a)\) is a probability on \(\{x_i\ge0,\ \sum_i x_i=1\}\). Both endpoints use that law on domain and codomain. The analysis concerns symmetric parameters, degree at most one, and a joint dimension/concentration limit, not a fixed-dimensional large-concentration expansion.

The pointwise norm formula is a specialization of the asymmetric endpoint theorem in [1], where it is given by \(F_A(a_*)\) with total \(A\) and smallest parameter \(a_*\). Set \(\lambda=na\), \(b=(n-1)a\), \(t=a/(\lambda+1)\). The formula used here is
\[
L_{n,a}=\mathbb E|n(\lambda+1)Y-\lambda|
=1+2\{\lambda I_t(a,b)-(\lambda+1) I_t(a+1,b)\},
\qquad Y\sim\operatorname{Beta}(a,b).
\]
Here \(I_t(u,v)\) is the regularized incomplete beta function. For reproducibility, the Dirichlet covariance restricts to \(1/[n(\lambda+1)]\) times the identity on the sum-zero hyperplane. Inverting there and adding the constant reproducer gives \(K(x,y)=n(\lambda+1)\sum_i x_i y_i-\lambda\). The absolute row integral is convex in \(x\) and the vertex rows are identical in law; a vertex maximizes the integral. Using the sign of that row as input attains the norm because the output is continuous and the measure has full support. Symmetry of the kernel and duality give the \(L^1\) norm. At a vertex the row has law \(n(\lambda+1)Y-\lambda\) and mean one, so its absolute mean is \(1+2\mathbb E(\lambda-n(\lambda+1)Y)_+\). Truncating the beta integral at \(t\) gives the formula. In particular \(1<L_{n,a}<1+2\lambda\). These identities are inputs, not new sharp-norm claims here.

## Proof of the comparison and the crossover

Take \(S\sim\operatorname{Gamma}(\lambda,1)\) independent of \(Y\). The change of variables from two independent gamma variables to their fraction and sum shows \(YS\stackrel{d}{=} G_a\). Thus
\[
\begin{aligned}
|L_{n,a}/n-g(a)|
&=\big|\mathbb E|(\lambda+1)Y-a|-\mathbb E|SY-a|\big|\\
&\le \mathbb E[Y|\lambda+1-S|]
\le \tfrac1n\sqrt{\mathbb E(\lambda+1-S)^2}
=\tfrac{\sqrt{\lambda+1}}{n}.
\end{aligned}
\]
For the deviation formula, the centered variable has mean zero, and \((a-x)x^{a-1}e^{-x}\) is the derivative of \(x^a e^{-x}\). Integrating on \((0,a)\) and doubling gives \(g(a)\) as displayed.

If \(\lambda_n\to0\), the elementary bounds on \(L_{n,a_n}\) prove the claim. If \(\lambda_n\to c>0\), fix \(r\in(0,1)\). The beta moment is
\[
\mathbb E Y^r=\frac{\Gamma(a_n+r)\Gamma(\lambda_n)}{\Gamma(a_n)\Gamma(\lambda_n+r)}=O(n^{-1}),
\]
since \(a_n=O(n^{-1})\) and \(\lambda_n\) stays in a compact positive interval. Consequently \(\mathbb E[(n(\lambda_n+1)Y)^r]=O(n^{r-1})\). Markov's inequality gives convergence of \(n(\lambda_n+1)Y\) to zero in probability. The negative part \((\lambda_n-n(\lambda_n+1)Y)_+\) is bounded by \(\lambda_n\), so its expectation tends to \(c\).

The gamma function at zero and Stirling's formula give \(g(a)\sim2a\) as \(a\downarrow0\) and \(g(a)\sim\sqrt{2a/\pi}\) as \(a\to\infty\). By positivity and continuity these imply \(g(a)\ge C\min(a,\sqrt a)\) for an absolute constant \(C>0\). The relative error in the comparison is bounded by a constant times \(\lambda_n^{-1/2}+\lambda_n^{-1}\) on indices with \(a_n\le1\), and by a constant times \(n^{-1/2}\) on those with \(a_n\ge1\) (using \(\lambda_n\ge n\) on the latter). Hence it tends to zero along every path with \(\lambda_n\to\infty\), even when the indices alternate between the two bounds. The same lower bound shows \(ng(a_n)\to\infty\) on such a path. If \(\lambda_n\) is unbounded, apply this conclusion along a subsequence with \(\lambda_n\to\infty\); if it is bounded, use \(L_{n,a_n}<1+2\lambda_n\).

## Relationship to existing results and limitations

The asymmetric norm theorem [1] covers the exact norm and has a fixed-dimension, fixed-proportions concentration asymptotic. Record [2] treats fixed per-coordinate concentration and fixed positive total concentration under dimension growth, also supplying a finer correction in the latter case. These fixed paths do not constitute a uniform error bound or the divergent-total equivalent for arbitrary varying \(a_n\), including \(a_n\to0\), \(na_n\to\infty\). The result here is limited to the finite-parameter gamma comparison and its joint asymptotic consequences, not priority for the norm formula or the fixed paths. No optimality of the comparison's error term is asserted.

The original package's `CHECK.py` is an optional finite numerical regression script, including tests of the exact-norm input and of the comparison. It does not certify limits along arbitrary paths; those follow from the estimates above.

## References

1. *Least-concentrated vertices govern asymmetric Dirichlet affine-projection stability*, [RESULT.md, 5c9fbf13aa23](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-least-concentrated-vertices-govern-asymmetric-dirichlet-affine-p--5c9fbf13aa23/RESULT.md).
2. *A logarithmic concentration boundary for affine Jacobi projection norms*, [RESULT.md, 8de5a5d258c9](https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-a-logarithmic-concentration-boundary-for-affine-jacobi-projectio--8de5a5d258c9/RESULT.md).
