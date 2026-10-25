# Sharp linear-in-mesh positivity frontier for Chebyshev-periodized Korobov lattice cubature

## Finding

**Theorem (sharp positivity frontier, even full lattices).** For each even integer \(N\ge4\), define
\[
B_N=\frac12-\frac{N}{4\pi}\sin\frac{2\pi}{N},\qquad a_N=\frac{\pi^2}{3N^2},\qquad d_N=1-\frac\pi N\cot\frac\pi N.
\]
The kernel-optimal weights specified below are nonnegative **if and only if**
\[
0<\gamma\le \gamma_N:=\frac{N B_N}{d_N-N a_N B_N}.
\]
At equality the two weights corresponding to the density's zeros are exactly zero; all others are positive. Above the threshold, those two weights are strictly negative, and the cubature may assign a negative answer to a nonnegative polynomial integrand. Furthermore,
\[
\gamma_N=N+\frac{\pi^2}{3}+O(N^{-1}).
\]
In sharp contrast, the cubature of the positive constant function is strictly positive for
\[
0<\gamma<\Gamma_N:=\frac{1}{d_N-a_N}
\]
and strictly negative for \(\gamma>\Gamma_N\), where
\[
\Gamma_N\sim\frac{45}{\pi^4}N^4,\qquad \gamma_N<\Gamma_N\quad(N\ge4\text{ even}).
\]
Thus loss of positivity of individual weights begins on the \(\gamma\asymp N\) scale, long before positivity of the constant-function output fails on the \(\gamma\asymp N^4\) scale.

## Assumptions and scope

Use exactly the one-dimensional, *full-lattice* specialization of the periodized kernel-interpolatory cubature construction of Bartel, Gilbert, Griebel, Kuo and Sloan, arXiv:2610.01113v1, equations (1.4), (2.4) and (3.2)–(3.5). Its nodes are \(t_j=j/N\), \(j=0,\ldots,N-1\), with even \(N\ge4\). The original integration coordinate is \(x=\psi(t)=\sin^2(\pi t)\), so
\[
\int_0^1 f(x)\,dx=\int_0^1 f(\psi(t))\,\mu(t)\,dt,\quad
\mu(t)=\frac\pi2|\sin(2\pi t)|.
\]
For the allowed smoothness \(\alpha=1\) and arbitrary finite \(\gamma>0\), set
\[
K_\gamma(s,t)=1+\gamma\sum_{k\in\mathbb Z\setminus\{0\}}\frac{e^{2\pi ik(s-t)}}{k^2},\quad
\mathcal K_{ij}=K_\gamma(t_i,t_j),\quad \kappa_i=\int_0^1K_\gamma(t_i,t)\mu(t)\,dt,
\]
with unique kernel-optimal weights \(w=\mathcal K^{-1}\kappa\). This is not a claim about arbitrary subsampling, other kernels, or higher dimensions. In particular, optimality means the source's unconstrained reproducing-kernel worst-case error minimum, *not* positivity-constrained quadrature optimality.

## Proof

**1. Fourier-to-hat identity.** Put \(h=1/N\) and let \(\phi_j\) be the period-one triangular nodal hat \(\phi_j(t)=\max(1-N\,\operatorname{dist}_{\mathbb T}(t,j/N),0)\), where \(\operatorname{dist}_{\mathbb T}\) is distance on the unit circle. Let \(b_j=\int_0^1\phi_j(t)\mu(t)\,dt\). Then \(\sum_j\phi_j=1\), \(\sum_j b_j=1\), and all \(b_j>0\). The Fourier coefficients of \(\mu\) are
\[
\widehat\mu(0)=1,\quad\widehat\mu(2k)=-\frac1{4k^2-1}\ (k\ne0),\quad
\widehat\mu(2k+1)=0.
\]
The hats have \(\widehat\phi_0(k)=N^{-1}\operatorname{sinc}^2(\pi k/N)\), with continuous value at zero. For each nonzero discrete Fourier residue \(r=1,\ldots,N-1\), the Fourier transform of the hat weights is
\[
\widehat b_r=
\frac{\sum_{k\equiv r\pmod N}\widehat\mu(k)/k^2}
{\sum_{k\equiv r\pmod N}1/k^2},
\]
since \(\sum_{k\equiv r\pmod N}1/k^2=\pi^2/[N^2\sin^2(\pi r/N)]\). Circulant diagonalization of \(\mathcal K\) gives exactly the same transform for \(w\) at every \(r\ne0\): the factor \(\gamma\) cancels. At the zero mode, writing
\[
a_N=\sum_{k\ne0}\frac1{(kN)^2}=\frac{\pi^2}{3N^2},\qquad
c_N=\sum_{k\ne0}\frac{\widehat\mu(kN)}{(kN)^2},
\]
yields
\[
\sum_jw_j=\frac{1+\gamma c_N}{1+\gamma a_N},\qquad
\sum_jb_j=1.
\]
Every weight therefore differs from its hat integral by the *same* offset:
\[
\boxed{w_j=b_j-\frac{\gamma(a_N-c_N)}{N(1+\gamma a_N)}.}
\]

**2. Exact correction and minimum.** Because \(N\) is even, each nonzero multiple of \(N\) is an even Fourier mode, so
\[
c_N=-2\sum_{k=1}^\infty\frac1{(kN)^2((kN)^2-1)}.
\]
Using \(1/[z^2(z^2-1)]=1/(z^2-1)-1/z^2\) and
\[
\sum_{k=1}^\infty\frac1{(kN)^2-1}=
\frac12-\frac\pi{2N}\cot\frac\pi N,
\]
we obtain \(a_N-c_N=d_N=1-(\pi/N)\cot(\pi/N)>0\). The hat at the cusp node \(t_0=0\) integrates to
\[
b_0=\pi\int_0^{1/N}(1-Nt)\sin(2\pi t)\,dt
=\frac12-\frac N{4\pi}\sin\frac{2\pi}N=B_N.
\]
The other cusp node \(t_{N/2}=1/2\) has the same integral. To see these are precisely the minimum hat integrals: \(\mu\) is period-\(1/2\), symmetric about its zeros, and strictly increasing with circular distance from the zeros until distance \(1/4\). For \(N\ge4\), folding the triangular hat to the circle of circumference \(1/2\) yields a nonnegative symmetric decreasing kernel. The convolution of that kernel with \(\mu\) is symmetric increasing in circular distance from each zero. Indeed, subtract \(\mu\) from its maximum and use the elementary layer-cake fact that overlap lengths of two centered arcs on a circle decrease with their center separation. Strictness at the finitely many interior lattice nodes follows from strict increase of \(\mu\) on \((0,1/4)\). Thus \(\min_j b_j=B_N\), only at \(j=0,N/2\).

**3. Threshold and witnesses.** The common subtraction increases strictly with \(\gamma\) and tends to \(d_N/(N a_N)\). The positive threshold denominator is assured because \(a_N-c_N=d_N>a_N\) (as \(c_N<0\)) and \(NB_N<1\) (the strict minimum of \(N\) positive hat integrals summing to one). Solving \(w_0=0\) gives \(\gamma_N\), with all other weights strictly positive there. For \(\gamma>\gamma_N\), \(w_0=w_{N/2}<0\). To witness negative cubature for a nonnegative original integrand, let \(x_j=\sin^2(\pi j/N)\) and set
\[
f(x)=\prod_{j=1}^{N/2}\left(1-\frac{x}{x_j}\right)^2\ge0\quad(0\le x\le1).
\]
This polynomial satisfies \(f(x_0)=1\) and \(f(x_j)=0\) for \(1\le j\le N/2\); reflected nodes have the same transformed \(x_j\). Therefore the cubature output equals \(w_0<0\), even though \(\int_0^1 f(x)dx>0\). The polynomial is smooth, so its transformed version satisfies the claimed smoothness assumptions.

**4. Asymptotics and the constant test.** Writing \(z=\pi/N\) and using Taylor expansions,
\[
B_N=\frac{\pi^2}{3N^2}-\frac{\pi^4}{15N^4}+O(N^{-6}),\quad
 a_N=\frac{\pi^2}{3N^2},\quad
 d_N=\frac{\pi^2}{3N^2}+\frac{\pi^4}{45N^4}+O(N^{-6}).
\]
Substituting into the exact threshold gives \(\gamma_N=N+\pi^2/3+O(N^{-1})\). The constant's numerical integral is
\[
Q_\gamma(1)=\sum_jw_j=\frac{1+\gamma(a_N-d_N)}{1+\gamma a_N},
\]
whose unique zero is \(\Gamma_N=(d_N-a_N)^{-1}\sim45N^4/\pi^4\). Since at \(\gamma_N\) only two weights vanish and the remaining weights are positive, \(Q_{\gamma_N}(1)>0\), so \(\gamma_N<\Gamma_N\) for every even \(N\ge4\).

## Verification

Run \(\texttt{python verification/check.py}\) with Python 3, NumPy and SciPy. The independent numerical implementation assembles the Bernoulli-polynomial kernel matrix directly, evaluates the non-smooth density integrals by adaptive quadrature, solves the linear system, and compares all weights to the closed-form hat-plus-offset formula. It tested \(N=4,6,8,10,12\) at six independent parameter values per mesh, including both sides of the threshold and at equality: **30 passing cases**. The finite tests corroborate the formulas; the infinite statements follow from the Fourier, rearrangement and trigonometric arguments above. The reproducibility artifact is not an independent audit or exhaustive verification.

## Relationship to prior work

Bartel et al. (2026) introduce the exact transformed-lattice kernel cubature \(w=\mathcal K^{-1}\kappa\) and derive convergence estimates, but do not state a sharp positive-weight regime for the smoothness-one even lattice or distinguish the positivity and constant-output scales. Karvonen, Kanagawa and Särkkä (2019) establish general connections between kernel cubature stability and positive weights; their observation that Brownian-motion kernel interpolation produces nonnegative hat functions concerns a different kernel-normalization geometry. Here the nonconstant Fourier modes reproduce hat weights, but penalization of the constant mode induces a *negative common shift* and an exact \(\gamma\asymp N\) positivity boundary. Earlier work on optimal periodic Sobolev interpolation can share the hat decomposition and leaves a genuine priority risk; equivalent treatment of the complete Chebyshev-density threshold is not established by the inspected evidence.

## Limitations

Only one-dimensional, fully sampled, even \(N\ge4\), smoothness \(\alpha=1\), and the stated density and Korobov kernel are classified. No positivity or rate claim is made for odd grids, other smoothness, subsampling, general densities, or multivariate lattice nodes. Very large \(\gamma\) is allowed mathematically but may be outside typical practical tuning ranges. The source's worst-case RKHS error guarantees remain valid; this result identifies a different property (positive integration of nonnegative data). Independent mathematical priority and audit checks have not been performed.

## References

1. F. Bartel, A. D. Gilbert, M. Griebel, F. Y. Kuo and I. H. Sloan, *A higher order lattice-based method for high-dimensional numerical integration using periodization*, arXiv:2610.01113v1 (first posted 2026-10-01), especially Sections 1–3. https://arxiv.org/html/2610.01113v1
2. T. Karvonen, M. Kanagawa and S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, Statistics and Computing 29 (2019), 1317–1333, DOI:10.1007/s11222-019-09901-0. https://link.springer.com/article/10.1007/s11222-019-09901-0
3. Kh. M. Shadimetov, A. R. Hayotov and N. H. Mamatova, *Optimal interpolation formulas in the periodic function space of S. L. Sobolev*, arXiv:1012.1953 (2010), abstract inspected; full text not verified.
