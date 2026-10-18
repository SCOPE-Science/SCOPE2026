# Sharp fractional path-Laplacian norms, parity corrections, and a logarithmic crossover

## Finding

Let \(P_n\) be the unit-edge path on \(n\ge2\) vertices, let \(L_n\) be its *unnormalized* graph Laplacian, and, for every \(0<\alpha<1\), define the spectral matrix power \(T_{n,\alpha}=L_n^\alpha\). On counting-measure sequence spaces set
\[
N_n(\alpha)=\|T_{n,\alpha}\|_{\ell^1_n\to\ell^1_n}
             =\|T_{n,\alpha}\|_{\ell^\infty_n\to\ell^\infty_n}.
\]
Write
\[
s=1+2\alpha,\quad
c_\alpha=\frac{\Gamma(2\alpha+1)}{\Gamma(\alpha+1)^2},\quad
\kappa_\alpha=\frac{\Gamma(2\alpha+1)\sin(\pi\alpha)}{\pi},\quad
b_\alpha(r)=\kappa_\alpha\frac{\Gamma(r-\alpha)}{\Gamma(r+\alpha+1)}\quad(r\ge1),
\]
and let \(d_n=n\) for odd \(n\), and \(d_n=n-1\) for even \(n\).

**Exact norm and extremal vertices.** The maximum absolute row sum is attained at exactly the central vertex if \(n\) is odd, and exactly the two central vertices if \(n\) is even. In particular,
\[
\boxed{N_n(\alpha)=2\left[c_\alpha
-2\sum_{j=1}^\infty b_\alpha(2nj)
-\sum_{j\in\mathbb Z} b_\alpha(|d_n+2nj|)\right].}
\]
Every index in the displayed sums is nonzero. The sums converge absolutely, and the equality is sharp for bounded sign data adapted to a maximizing row. An independently usable finite formula is
\[
\boxed{N_n(\alpha)=\frac2n\sum_{k=1}^{n-1}
\left(4\sin^2\frac{\pi k}{2n}\right)^\alpha
\left[1+\cos\left(\frac{\pi k d_n}{n}\right)\right].}
\]
For every finite \(n\), \(N_n(\alpha)<2c_\alpha\). In the special case \(\alpha=1/2\) and odd \(n\),
\[
N_n(1/2)=\frac4n\cot\frac{\pi}{2n}.
\]

**Sharp finite-size and parity laws.** For each fixed \(0<\alpha<1\), put
\[
B_\alpha=\frac{\alpha(\alpha+1)(2\alpha+1)}6,\qquad
C_{\mathrm{odd}}(\alpha)=4\kappa_\alpha B_\alpha\zeta(s+2),
\]
\[
C_{\mathrm{even}}(\alpha)=C_{\mathrm{odd}}(\alpha)
+2\kappa_\alpha s(s+1)\bigl(1-2^{-(s+2)}\bigr)\zeta(s+2).
\]
Then along each fixed parity,
\[
\boxed{2c_\alpha-N_n(\alpha)
=4\kappa_\alpha\zeta(1+2\alpha)n^{-1-2\alpha}
+C_{\operatorname{parity}(n)}(\alpha)n^{-3-2\alpha}
+O_\alpha(n^{-5-2\alpha}).}
\]
Thus both parities have the same leading boundary deficit, but their first nonzero subleading coefficients differ strictly.

**Logarithmic zero-order crossover.** Let \(\alpha_n\in(0,1)\) satisfy \(\alpha_n\to0\) and \(\alpha_n\log n\to\lambda\in[0,\infty]\), allowing \(\lambda=+\infty\). Then
\[
\boxed{\lim_{n\to\infty}n\bigl(2c_{\alpha_n}-N_n(\alpha_n)\bigr)=2e^{-2\lambda},}
\]
with \(e^{-\infty}=0\). Equivalently, the transition between the zero-order finite-path boundary deficit and the fixed-positive-order power-law deficit occurs at the nontrivial scale \(\alpha\asymp1/\log n\). The displayed limit measures the difference from the *infinite-lattice* sharp norm \(2c_\alpha\), not from the finite-path value at \(\alpha=0\).

## Assumptions and scope

Vertices are \(0,\ldots,n-1\). For every adjacent pair, the graph Laplacian has off-diagonal entries \(-1\), interior diagonal entries \(2\), and endpoint diagonal entries \(1\). All spectral powers use \(0^\alpha=0\) when \(\alpha>0\). The operator is considered over real or complex scalars, in the stated counting-measure \(\ell^1\) and \(\ell^\infty\) norms. The exponents are confined to \(0<\alpha<1\); the parity expansion is a fixed-\(\alpha\) result, while the logarithmic crossover permits \(\alpha\) to vary with \(n\). The gamma and zeta functions have their standard classical meanings.

## Proof

**1. Endpoint norm equals twice the largest diagonal.** For \(0<\alpha<1\) the Bernstein subordination identity gives
\[
L_n^\alpha=\frac{\alpha}{\Gamma(1-\alpha)}
\int_0^\infty(I-e^{-tL_n})t^{-1-\alpha}\,dt.
\]
The connected-path heat kernel has strictly positive entries at every positive time. Therefore all off-diagonal entries of \(L_n^\alpha\) are strictly negative. Since \(L_n^\alpha\mathbf1=0\), the absolute row sum at vertex \(i\) equals \(2(L_n^\alpha)_{ii}\). Symmetry supplies the same sharp \(\ell^1\) norm. Choosing a sign vector matching a maximizing row proves attainment, including for complex inputs.

**2. Exact reflection formula and strict central localization.** Let the absolutely summable coefficients of the full-line lattice fractional Laplacian be
\[
q_\alpha(r)=\frac1{2\pi}\int_{-\pi}^{\pi}
(2-2\cos\theta)^\alpha e^{ir\theta}\,d\theta.
\]
The beta integral gives \(q_\alpha(0)=c_\alpha\), and for each positive integer \(r\),
\[
q_\alpha(r)=q_\alpha(-r)=-b_\alpha(r).
\]
Reflecting the path at the two half-integer boundaries, or equivalently grouping the cosine eigenvectors into the even subspace of a cycle on \(2n\) sites, gives the exact matrix identity
\[
(L_n^\alpha)_{ij}=
\sum_{h\in\mathbb Z}\left[q_\alpha(i-j+2nh)+q_\alpha(i+j+1+2nh)\right].
\]
Define \(A_{n,\alpha}=\sum_hq_\alpha(2nh)\) and \(H_{n,\alpha}(d)=\sum_hq_\alpha(d+2nh)\). The diagonal is \(A_{n,\alpha}+H_{n,\alpha}(2i+1)\).

For \(1\le d\le n\), the Euler beta identity implies
\[
H_{n,\alpha}(d)=
-\frac{\sin(\pi\alpha)}\pi
\int_0^1 \frac{t^{-\alpha-1}(1-t)^{2\alpha}}{1-t^{2n}}
\bigl(t^d+t^{2n-d}\bigr)\,dt.
\]
The sum \(t^d+t^{2n-d}\) is **strictly decreasing** as \(d\) rises from \(1\) to \(n\) for every \(0<t<1\); hence \(H_{n,\alpha}(d)\) is strictly increasing there. Its symmetry \(H_{n,\alpha}(d)=H_{n,\alpha}(2n-d)\) proves that exactly the central one or two diagonal entries are maximal. Substituting the central value \(d_n\) yields the two exact norm formulas. All reflected nonzero coefficients are negative, proving the strict bound \(N_n(\alpha)<2c_\alpha\).

The displayed cosine spectral sum follows from path eigenvalues \(4\sin^2(\pi k/(2n))\) and normalized eigenvectors \(\sqrt{2/n}\cos(\pi k(i+1/2)/n)\), for \(1\le k<n\). At \(\alpha=1/2\), \(b_{1/2}(r)=1/[\pi(r^2-1/4)]\). If \(n\) is odd, the center's two image sums combine into all nonzero integer multiples of \(n\); the classical cotangent partial-fraction identity then yields \(4\cot(\pi/(2n))/n\).

**3. Two-term finite-size parity expansion.** Put \(s=1+2\alpha\) and \(B_\alpha=\alpha(\alpha+1)(2\alpha+1)/6\). The gamma-ratio Stirling expansion, using the reflection relation between the two shifts \(-\alpha\) and \(1+\alpha\), gives
\[
\frac{\Gamma(x-\alpha)}{\Gamma(x+\alpha+1)}=
 x^{-s}\left(1+B_\alpha x^{-2}+O_\alpha(x^{-4})\right),\qquad x\to\infty.
\]
For odd \(n\), the total deficit in the maximizing diagonal equals \(2\sum_{j\ge1}b_\alpha(nj)\). Summing the expansion against positive integer multiples produces
\[
2c_\alpha-N_n(\alpha)=4\kappa_\alpha\zeta(s)n^{-s}
+4\kappa_\alpha B_\alpha\zeta(s+2)n^{-s-2}+O_\alpha(n^{-s-4}).
\]
For even \(n\), the reflected distances to the odd image multiples of \(n\) occur in the pairs \((2j+1)n-1\) and \((2j+1)n+1\). Taylor expansion of the pair, uniformly summed in \(j\), supplies the additional \(s(s+1)\sum_{j\ge0}(2j+1)^{-s-2}\) term in the diagonal deficit. Twice that expression is exactly the displayed \(C_{\mathrm{even}}-C_{\mathrm{odd}}\), with \(O_\alpha(n^{-s-4})\) residual. The parity difference is strictly positive because all its factors are positive.

**4. A uniform estimate and zero-order crossover.** For \(0<\alpha\le\alpha_0<1\), the gamma-ratio estimate
\[
\frac{\Gamma(x-\alpha)}{\Gamma(x+\alpha+1)}
=x^{-1-2\alpha}\bigl(1+O_{\alpha_0}(x^{-2})\bigr)
\]
holds uniformly for all sufficiently large \(x\). For even paths, the paired shift errors are \(O_{\alpha_0}(x^{-3-2\alpha})\); for odd paths no shifts occur. Consequently the full leading boundary deficit has the **uniform** estimate
\[
2c_\alpha-N_n(\alpha)=4\kappa_\alpha\zeta(1+2\alpha)n^{-1-2\alpha}
+O_{\alpha_0}\!\left(\kappa_\alpha n^{-3-2\alpha}\right).
\]
As \(\alpha\downarrow0\), \(\kappa_\alpha/\alpha\to1\) and \(2\alpha\zeta(1+2\alpha)\to1\); thus \(4\kappa_\alpha\zeta(1+2\alpha)\to2\). Multiplication by \(n\) and passage to \(\alpha_n\log n\to\lambda\) proves the crossover even for \(\lambda=+\infty\). At each fixed \(n\), \(L_n^{\alpha}\to I-\mathbf1\mathbf1^\top/n\) as \(\alpha\downarrow0\), explaining the endpoint convention at the singular zero eigenvalue.

## Verification

The accompanying `CHECK.py` uses independent cosine-eigenvector summation and quadrature for the gamma Fourier coefficients. It checks strict central localization, symmetry, strict off-diagonal signs, row-sum zero, exact norm equality, the cotangent identity, the two different parity corrections, and finite-size realizations of the logarithmic crossover. Running `python CHECK.py` with Python 3 and `mpmath` produced **2,775 passed finite checks**. These tests exercise finite instances only. The universal and asymptotic assertions are justified by Steps 1–4 of the proof, not by extrapolating finite tests.

## Relationship to prior work

Riascos and Mateos introduce spectral fractional graph Laplacians and compute the gamma-function lattice coefficients and fractional degrees on rings; these are **prior ingredients**, not new coefficient identities. The current theorem instead treats reflecting finite paths, proves strict vertex localization, and determines both the parity-dependent endpoint-norm correction and the logarithmic zero-order crossover. Zhang, Lin, and Yang establish the general finite-graph spectral definition and positivity of fractional off-diagonal weights; these imply the basic diagonal-row-sum norm reduction but do not provide reflecting-path maximizers or any zeta/parity/crossover asymptotic. Grubb studies regularity of spectral fractional Neumann realizations in continuous domains; the present counting-measure graph norm is a different invariant. Estrada, Hameed, Hatano, and Langer study transformed \(k\)-path Laplacians on infinite one-dimensional graphs; their operators and infinite-volume setting do not imply the finite reflecting spectral-power theorem. The infinite-lattice endpoint norm alone supplies \(2c_\alpha\) but not its finite-path correction.

## Limitations

The result is restricted to the unnormalized unit-edge path Laplacian, \(0<\alpha<1\), and its specified endpoint norms. The fixed-order expansion is not asserted uniform up to \(\alpha=1\); the near-zero uniform estimate is separately proved. No claim is made about arbitrary graphs, normalized Laplacians, other fractional-order regimes, or complete historical priority. An independently discovered equivalent formulation involving Neumann image kernels or fractional graph degrees remains a literature risk. Neither the finite numerical tests nor the source searches constitute external mathematical certification.

## References

1. A. P. Riascos and J. L. Mateos, *Fractional dynamics on networks: Emergence of anomalous diffusion and Lévy flights*, Physical Review E **90** (2014), 032809, DOI: `10.1103/PhysRevE.90.032809`. Open author preprint: `arXiv:1506.06167`, particularly equations (4), (11)–(16).
2. G. Grubb, *Regularity of spectral fractional Dirichlet and Neumann problems*, `arXiv:1412.3744` (public 2014-12-11); published in Mathematische Nachrichten **289** (2016), 831–844.
3. E. Estrada, E. Hameed, N. Hatano, and M. Langer, *Path Laplacian operators and superdiffusive processes on graphs. I. One-dimensional case*, `arXiv:1604.00555` (public 2016-04-02).
4. M. Zhang, Y. Lin, and Y. Yang, *Fractional Laplace operator on finite graphs*, `arXiv:2403.19987` (public 2024-03-29), Sections 3.1–3.2; a general finite-graph operator definition and off-diagonal positivity.
5. Classical Euler beta, reflection, Stirling gamma-ratio, and cotangent partial-fraction identities; derivations needed here are stated in the proof.
