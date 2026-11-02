# A sphere-coupled randomized trapezoid is quadratically exact and has sharp cubic-order variance

## Finding
For every positive multiple \(n\) of three, put \(h=1/n\). Split the \(n\) cells of \([0,1]\) into consecutive blocks of three. Draw independent uniformly distributed sphere points \(V_k=(V_{k,0},V_{k,1},V_{k,2})\in S^2\) for different blocks. For cell \(i=3k+j\), set \(\tau_i=(1+V_{k,j})/2\) and define the two-evaluation-per-cell quadrature
\[
Q_n(f)=\frac h2\sum_{i=0}^{n-1}\left[f((i+\tau_i)h)+f((i+1-\tau_i)h)\right].
\]
This quadrature is unbiased for every continuous \(f\), and it integrates every polynomial of degree at most two **for every realization** of the sphere points. Moreover, for every real \(f\in C^3([0,1])\),
\[
\lim_{\substack{n\to\infty\\3\mid n}}n^7\operatorname{Var}(Q_n(f))
=\frac{1}{720}\int_0^1[f'''(t)]^2\,dt.
\]
The rate is sharp whenever \(f\) is not quadratic; it gives root-mean-squared error asymptotic to \(n^{-7/2}\bigl(\int[f''']^2/720\bigr)^{1/2}\). For \(f(t)=at^3+bt^2+ct+d\), the exact finite-grid identity is \(\operatorname{Var}(Q_n(f))=a^2/(20n^7)\). Three cells are the **smallest possible** block size for pathwise quadratic exactness using symmetric two-point samples with each sampling fraction uniform on \([0,1]\).

For comparison, if all \(\tau_i\) are independent uniforms (the rule of Wu), then for \(f\in C^2([0,1])\)
\[
\lim_{n\to\infty}n^5\operatorname{Var}(Q_n^{\mathrm{iid}}(f))
=\frac1{720}\int_0^1[f''(t)]^2\,dt.
\]
Thus the sphere coupling removes the leading cell-curvature fluctuation without adding function evaluations. This is a result about smooth deterministic integrands and is not a universal improvement on rough-function worst-case rates.

## Assumptions and scope
The integration domain is \([0,1]\), the grid is uniform, \(n\ge3\) is divisible by three, different sphere blocks are independent, and each sphere point has normalized surface-area distribution. Within each cell the two nodes are symmetric about the midpoint. All expectations and variances are with respect to the sphere draws. Each \(V_{k,j}\) is marginally uniform on \([-1,1]\), even though coordinates in the same block are dependent. The exactness result requires only that the integrand be a polynomial of degree at most two. The variance limit requires real-valued \(C^3\) regularity; no claim of a higher-order rate for merely \(C^2\) functions is made.

## Proof
**Unbiasedness.** The coordinate of a uniform point on \(S^2\) has the uniform distribution on \([-1,1]\) (the known spherical copula). Consequently each \(\tau_i\) is uniform on \([0,1]\). Both \((i+\tau_i)h\) and \((i+1-\tau_i)h\) are separately uniform in the cell, so the expected two-point cell contribution equals its exact integral; summing gives \(\mathbb E Q_n(f)=\int_0^1f\).

**Cell error.** Write \(m_i=(i+1/2)h\), \(Z_i=V_{k,j}\), so the nodes are \(m_i\pm hZ_i/2\). Taylor expansion about \(m_i\) and exact integration of the corresponding expansion give, uniformly over \(i\) and \(|Z_i|\le1\),
\[
\frac h2\bigl(f(m_i+hZ_i/2)+f(m_i-hZ_i/2)\bigr)
-\int_{ih}^{(i+1)h} f(t)\,dt
=\frac{h^3}{8}f''(m_i)(Z_i^2-1/3)+h^4\varepsilon_{i,n},
\]
where \(\sup_i|\varepsilon_{i,n}|\to0\) as \(n\to\infty\) for \(f\in C^3\). Indeed, the odd cubic Taylor term cancels between the symmetric nodes, and the integrated odd term also vanishes; uniform continuity of \(f'''\) controls the Peano remainder by \(o(h^4)\). Each cell error is centered exactly by the marginal-uniform property.

**Pathwise cancellation and quadratic exactness.** In block \(k\), the three squared coordinates sum to one. Thus \(\sum_{j=0}^2(Z_{3k+j}^2-1/3)=0\) identically. For a quadratic, \(f''\) is constant and the cell-error formula is exact with zero remainder, so every block has zero error.

**Leading block error.** Let \(c_k=(3k+3/2)h\). With \(f\in C^3\), its uniformly continuous third derivative gives \(f''(m_{3k+j})=f''(c_k)+(j-1)h f'''(c_k)+o(h)\) uniformly in \(k\). Summing the three cell errors and cancelling the common curvature yields
\[
B_{k,n}=\frac{h^4}{8}f'''(c_k)(V_{k,2}^2-V_{k,0}^2)+o(h^4),
\]
where the final remainder is uniformly \(o(h^4)\). Each block error \(B_{k,n}\) has mean exactly zero, and different blocks are independent. For a uniform sphere point the squared coordinates have Dirichlet law \(\operatorname{Dirichlet}(1/2,1/2,1/2)\), so
\[
\mathbb EV_j^2=1/3,\quad \mathbb EV_j^4=1/5,
\quad\mathbb EV_i^2V_j^2=1/15\ (i\ne j),\quad
\operatorname{Var}(V_2^2-V_0^2)=4/15.
\]
Uniformity of the centered remainder therefore implies
\[
\operatorname{Var}(B_{k,n})
=\frac{h^8}{240}[f'''(c_k)]^2+o(h^8)
\]
uniformly over blocks. There are \(n/3\) independent blocks, and their center-point Riemann sums converge, whence
\[
\operatorname{Var}(Q_n(f))
=\frac{h^8}{240}\sum_{k=0}^{n/3-1}[f'''(c_k)]^2+o(nh^8)
=\frac{h^7}{720}\int_0^1[f'''(t)]^2\,dt+o(h^7).
\]
If \(f'''\not\equiv0\), the limiting constant is positive, proving sharpness of the claimed rate. For a cubic the Peano remainders vanish exactly, and \(f'''=6a\) yields \(36a^2/(720n^7)=a^2/(20n^7)\) on every permitted grid.

**Minimal block size.** For any symmetric two-point cell rule with marginally uniform \(\tau_i\), exact quadratic integration across a block of \(m\) equal cells requires \(\sum_{i=1}^m (2\tau_i-1)^2=m/3\) almost surely. For \(m=1\), this contradicts the nondegenerate distribution of \((2\tau_1-1)^2\). For \(m=2\), \(\mathbb P((2\tau_1-1)^2>2/3)=1-\sqrt{2/3}>0\), which contradicts a fixed total \(2/3\) because the second square is nonnegative. The constructed triple attains the lower bound, hence the minimum is three.

**IID benchmark.** Each independent cell has leading centered error \(h^3 f''(m_i)(Z_i^2-1/3)/8+o(h^3)\). Since \(\operatorname{Var}(Z_i^2)=1/5-1/9=4/45\), independent variance summation and Riemann convergence give \(n^5\operatorname{Var}(Q_n^{\rm iid}(f))\to(1/720)\int_0^1[f'']^2\).

## Verification
The included `verify.py` performs exact rational checks of sphere moments, symmetric-cell polynomial integration and cubic block-error identities on rational sphere points. It also verifies the exact cubic variance law at six finite grid sizes. It outputs `VERIFY_OK 184 exact sphere moments, rational quadratic/cubic paths, and variance identities`. These finite calculations do not replace the uniform Taylor expansion, Riemann limit, or minimality proof above. Run with `python3 verify.py`; no third-party dependencies are required.

## Relationship to prior work
Wu's *A randomised trapezoidal quadrature* (arXiv:2011.15086, 2020) introduced the symmetric random two-point cell rule with **independent** uniformly distributed fractions and proved fractional-Sobolev error estimates. The present claim changes only the inter-cell coupling and establishes an exactness/variance result not implied by those IID bounds. Perlman and Wellner (arXiv:1101.0145; *Symmetry* 2011) **already establish** that a uniform sphere point in three dimensions has uniform coordinate marginals; that probability distribution itself is not claimed as new. The prior theory of complete/joint mixability concerns how to obtain constant sums of marginal variables and motivates the construction, but existence of such a coupling alone does not imply the present exact stochastic quadrature variance limit. Goda, Kazashi and Suzuki (arXiv:2212.11476) analyze a different Gaussian-weight integration algorithm and its Sobolev minimax rates; those rates do not directly subsume this finite-interval, fixed-smooth-integrand covariance statement. An unlocated earlier specialized dependent-strata quadrature theorem could imply this result; scientific priority requires independent checking.

## Limitations
The smooth-integrand asymptotic holds for three-cell blocks and uniform grids only, with a specific sphere-induced dependence law. It does not prove variance optimality among all couplings or all quadrature procedures, nor improvement for rough integrands, unequal grids, stochastic integrands, or high-dimensional integration. The sphere copula and broader joint-mixability constructions are established previous work. The verification program checks finite algebra, not a substitute for the infinite-dimensional proof. Independent priority and scientific validation have not been performed.

## References
- Yue Wu, *A randomised trapezoidal quadrature*, arXiv:2011.15086, first posted November 30, 2020, https://arxiv.org/abs/2011.15086 .
- Michael D. Perlman and Jon A. Wellner, *Squaring the Circle and Cubing the Sphere: Circular and Spherical Copulas*, arXiv:1101.0145 (2010 preprint), *Symmetry* 3 (2011), 574–599, https://doi.org/10.3390/sym3030574 .
- Takashi Goda, Yoshihito Kazashi and Yuya Suzuki, *Randomizing the trapezoidal rule gives the optimal RMSE rate in Gaussian Sobolev spaces*, arXiv:2212.11476, first posted December 22, 2022, https://arxiv.org/abs/2212.11476 .
- Complete/joint mixability literature: Wang and Wang, *Complete mixability and convex minimization with monotone marginal densities* (2011), and subsequent *Joint Mixability* results (2016); concept used as prior context, not asserted novel here.
