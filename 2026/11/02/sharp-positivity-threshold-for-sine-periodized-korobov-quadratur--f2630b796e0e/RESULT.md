# Sharp positivity threshold for sine-periodized Korobov quadrature

## Finding

For every integer \(N\ge2\) and kernel parameter \(\gamma>0\), the unique optimal weights on the complete uniform one-dimensional grid for the first-order periodic Korobov kernel and the sine-periodization density have an exact positivity transition. Put
\[
P_N=\frac12-\frac{N}{4\pi}\sin\frac{2\pi}{N},\qquad
H_N=\begin{cases}
\dfrac1{2\pi^2}-\dfrac1{2\pi N}\cot\dfrac\pi N,&N\text{ even},\\[4pt]
\dfrac1{8N^2}+\dfrac1{2\pi^2}-\dfrac1{4\pi N}\cot\dfrac\pi{2N},&N\text{ odd}.
\end{cases}
\]
Then \(6NH_N-P_N>0\), and the minimum weight is exactly
\[
\min_{0\le j<N}w_j
=P_N-\frac{2\pi^2\gamma H_N}{N\bigl(1+\pi^2\gamma/(3N^2)\bigr)}.
\]
Consequently, the weights are all strictly positive if and only if
\[
0<\gamma<\gamma_N,
\qquad \gamma_N=\frac{3N^2P_N}{\pi^2(6NH_N-P_N)}.
\]
They are all nonnegative at equality, at least one vanishes there, and at least one becomes negative for \(\gamma>\gamma_N\). The threshold has the sharp two-term asymptotic
\[
\gamma_N=N+\frac{\pi^2}{3}+O(N^{-1})\qquad(N\to\infty).
\]
The minimum is attained by the grid point at \(0\) (also at \(1/2\) when \(N\) is even). Thus for fixed positive \(\gamma\), every optimal weight is eventually positive. The result is for the full one-dimensional grid and first-order kernel, not for arbitrary subsampling, higher-order kernels, or multivariate lattices.

## Assumptions and scope

Work on the periodic unit interval \(\mathbb T=\mathbb R/\mathbb Z\). The density and kernel are
\[
\mu(y)=\frac{\pi}{2}|\sin(2\pi y)|,\quad
K_\gamma(u,v)=1+2\pi^2\gamma B_2(\{u-v\}),\quad
B_2(t)=t^2-t+\frac16.
\]
Here \(\int_0^1\mu(y)\,dy=1\), the nodes are \(x_j=j/N\), and the symmetric Gram matrix \(\mathsf K=(K_\gamma(x_i,x_j))_{i,j}\) is positive definite for every \(\gamma>0\). Let
\[
\kappa_j=\int_0^1K_\gamma(x_j,y)\mu(y)\,dy,\qquad
(w_0,\ldots,w_{N-1})^{\mathsf T}=\mathsf K^{-1}\boldsymbol\kappa.
\]
These are the unique worst-case-error-minimizing, unconstrained quadrature weights in the periodic Korobov RKHS with Fourier norm
\[
\|f\|_\gamma^2=\left|\int_0^1 f\right|^2+\frac1{4\pi^2\gamma}\int_0^1|f'(y)|^2\,dy.
\]
No positivity constraint is imposed during optimization. Negative weights beyond the transition are a property of this unconstrained optimizer.

## Proof

**1. Explicit minimum-norm interpolant.** For any nodal values \(v_j\), denote the periodic piecewise-linear interpolant by \(L_v\), let \(\overline v=N^{-1}\sum_jv_j\), and for \(y\in[x_j,x_{j+1}]\) (using the periodic last cell) define the continuous bubble
\[
q_N(y)=(y-x_j)(x_{j+1}-y).
\]
It vanishes at every node, is nonnegative, and has \(\int_0^1q_N=1/(6N^2)\). The unique minimum-RKHS-norm interpolant \(S_v\) satisfies, on each open cell, the Euler–Lagrange condition \(S_v''=4\pi^2\gamma\int_0^1S_v\). Hence
\[
S_v(y)=L_v(y)-2\pi^2\gamma\frac{\overline v}{1+\pi^2\gamma/(3N^2)}q_N(y).
\]
Indeed, the displayed function interpolates all data; its second derivative gives the Euler–Lagrange equation, and integration verifies its stated mean. Strict convexity of the RKHS norm gives uniqueness. The representer theorem identifies this interpolant with the kernel interpolant \(\sum_i(\mathsf K^{-1}\mathbf v)_iK_\gamma(x_i,\cdot)\).

**2. Common negative correction.** Let \(L_j\) denote the periodic hat equal to one at node \(j\) and zero at the others, and write
\[
P_{N,j}=\int_0^1L_j(y)\mu(y)\,dy,\qquad
H_N=\int_0^1q_N(y)\mu(y)\,dy.
\]
Integrating \(S_v\) against \(\mu\) gives
\[
w_j=P_{N,j}-T_{N,\gamma},\qquad
T_{N,\gamma}=\frac{2\pi^2\gamma H_N}{N\bigl(1+\pi^2\gamma/(3N^2)\bigr)}.
\]
The density is normalized, so \(P_{N,j}>0\) and \(\sum_jP_{N,j}=1\). Notice that \(T_{N,\gamma}\) is independent of \(j\); this common correction is why positive density alone does not guarantee positive optimal weights.

**3. The smallest hat integral is at a zero of the density.** Since \(\mu\) has period \(1/2\), fold each hat onto the circle of length \(1/2\). The folded hat at zero is
\[
B_N(t)=(1-Nt)_++(1-N(\tfrac12-t))_+\quad(0\le t\le\tfrac14),
\]
extended evenly and periodically. It is nonincreasing on \([0,1/4]\): for \(N\ge4\) its second summand vanishes there, for \(N=3\) the two slopes cancel where they overlap, and for \(N=2\) the sum is constant. On the same circle, \(g(t)=\pi/2-\mu(t)\) is nonnegative, even and nonincreasing. The convolution of two nonnegative, even, symmetric-decreasing functions on a circle is symmetric-decreasing. To verify this standard fact directly, use layer-cake decompositions into centered arcs; the length of intersection of two centered arcs is largest when their centers coincide (and decreases with circular center separation). Thus \(g*B_N\) is largest at zero, so \(\mu*B_N\) is smallest at zero. Therefore \(P_{N,j}\ge P_{N,0}\) for every \(j\). Direct integration yields
\[
P_{N,0}=\pi\int_0^{1/N}(1-Ny)\sin(2\pi y)\,dy
=\frac12-\frac{N}{4\pi}\sin\frac{2\pi}{N}=P_N.
\]
The density's half-period gives the same minimum at index \(N/2\) for even \(N\).

**4. Exact bubble integral.** On every cell the bubble has average \(1/(6N^2)\), and its Fourier expansion is
\[
q_N(y)=\frac1{6N^2}-\frac1{\pi^2N^2}\sum_{\ell\ge1}\frac{\cos(2\pi\ell Ny)}{\ell^2}.
\]
The density's absolutely convergent Fourier expansion is
\[
\mu(y)=1-2\sum_{m\ge1}\frac{\cos(4\pi my)}{4m^2-1}.
\]
Orthogonality therefore gives
\[
H_N=\frac1{6N^2}+\frac1{\pi^2N^2}
\sum_{\substack{\ell\ge1\\2\mid\ell N}}\frac1{\ell^2((\ell N)^2-1)}.
\]
For even \(N\), partial fractions and \(\sum_{\ell\ge1}(\ell^2-a^2)^{-1}=(2a^2)^{-1}-(\pi/(2a))\cot(\pi a)\) give \(H_N=(2\pi^2)^{-1}-(2\pi N)^{-1}\cot(\pi/N)\). For odd \(N\), only even \(\ell\) survive, equivalently \(H_N=H_{2N}+1/(8N^2)\), proving the second expression.

**5. Sharp crossing and asymptotics.** The series in Step 4 is positive beyond its first term, so \(H_N>1/(6N^2)\). Since \(P_N\le1/N\), the denominator \(6NH_N-P_N\) is strictly positive. The common correction \(T_{N,\gamma}\) is strictly increasing from zero to \(6NH_N\) as \(\gamma\) increases from zero to infinity. Solving \(P_N=T_{N,\gamma}\) gives the unique positive \(\gamma_N\), including every equality and sign case. Finally, Taylor expansion of sine and cotangent yields, for either parity,
\[
P_N=\frac{\pi^2}{3N^2}+O(N^{-4}),\qquad
H_N=\frac1{6N^2}+O(N^{-4}),
\]
and substitution, retaining the next term of \(P_N\), gives \(\gamma_N=N+\pi^2/3+O(N^{-1})\). No finite numerical enumeration is used to establish the all-\(N\) or all-\(\gamma\) claims.

## Verification

A standalone \(\texttt{verify.py}\) compares (i) the derived \(H_N\) with independently integrated cell bubbles, (ii) the analytical weights against the original Gram-matrix solve with numerically integrated kernel means, (iii) the explicit interpolant against direct kernel interpolation off-grid, and (iv) below/at/above-threshold sign patterns. It executed successfully for all \(2\le N\le14\), with 13 bubble comparisons, 65 kernel-system comparisons, 140 interpolant comparisons and 65 sign-classification checks. High-precision evaluations at six larger values of \(N\) corroborate the constant \(\pi^2/3\). These finite checks complement rather than replace the proof.

Reproduce using Python 3 with \(\texttt{numpy}\), \(\texttt{scipy}\), and \(\texttt{mpmath}\): run \(\texttt{python verify.py}\) from the directory containing the extracted file.

## Relationship to prior work

Bartel, Gilbert, Griebel, Kuo and Sloan, *A higher order lattice-based method for high-dimensional numerical integration using periodization* (2026), introduce the sine periodization, Korobov kernel, full-lattice interpolatory weights \(\mathsf K^{-1}\boldsymbol\kappa\), and convergence analysis. Their Sections 3 and 7 provide the method and discuss asymptotic positivity in other product-integration settings, but do not supply this univariate all-parameter minimum-weight classification or exact positive-weight frontier. General optimal-weight/spline-representer theory appears in Oettershagen (2017), especially Sections 3.3–3.4, and is used here rather than claimed as new. Sloan and Smith (1982) concern asymptotic positivity for interpolatory polynomial product-integration rules, a different setting. The result distinguishes its explicit \(\gamma_N\) law from general representer formulas, asymptotic convergence guarantees, and classical product-integration positivity statements.

## Limitations

Only the univariate complete uniform grid, the sine-periodization density, and the first-order Korobov kernel are treated; no result is claimed for multivariate, shifted, randomly subsampled or higher-order constructions. Negative weights concern the unique unconstrained RKHS-optimal formula and do not imply numerical instability or negative output for every positive input. The rule generally does not integrate constants exactly at finite \(\gamma\); its weight sum is \(1-NT_{N,\gamma}\). The local searches and source inspections do not establish absolute historical priority; older spline and product-integration texts may contain equivalent specializations.

## References

- F. Bartel, A. D. Gilbert, M. Griebel, F. Y. Kuo, I. H. Sloan, *A higher order lattice-based method for high-dimensional numerical integration using periodization*, arXiv:2610.01113v1, 2026-10-01, https://arxiv.org/html/2610.01113v1 .
- J. Oettershagen, *Construction of Optimal Cubature Algorithms with Applications to Econometrics and Uncertainty Quantification*, doctoral thesis, University of Bonn, 2017, https://ins.uni-bonn.de/media/public/publication-media/diss_oettershagen.pdf?pk=460 .
- I. H. Sloan and W. E. Smith, *Properties of Interpolatory Product Integration Rules*, SIAM Journal on Numerical Analysis 19 (1982), https://doi.org/10.1137/0719027 .
