# A radial-to-boundary phase transition for quadratic projection on weighted balls

## Finding

Fix a real parameter \(\alpha>-1\), and write \(k=\alpha+1>0\). For each integer \(d\geq2\), let \(\mu_{d,k}\) be the probability measure on the closed Euclidean unit ball \(B^d\subset\mathbb R^d\) whose density, on the interior, is proportional to \((1-\|y\|^2)^{k-1}\). Let \(P_{d,k}\) be the \(L^2(\mu_{d,k})\)-orthogonal projector onto all real polynomials of total degree at most two, extended by its finite-rank kernel to bounded measurable real or complex functions. Then

\[
\boxed{\lim_{d\to\infty}\frac{\|P_{d,k}\|_{L^\infty(\mu_{d,k})\to L^\infty(\mu_{d,k})}}{d}
=\max\!\left\{\frac{k^k e^{-k}}{\Gamma(k+1)},\sqrt{\frac{2}{\pi e}}\right\}.}
\]

This maximum has an exact transition at \(k=1/2\), equivalently at \(\alpha=-1/2\). To state the location result precisely, set
\[
\Lambda_{d,k}(x)=\int_{B^d}|K_{d,k}(x,y)|\,d\mu_{d,k}(y),
\]
where \(K_{d,k}\) is the reproducing kernel below. If \(x_d\in B^d\) satisfies \(\Lambda_{d,k}(x_d)=\max_x\Lambda_{d,k}(x)\), then

- for \(-1<\alpha<-1/2\), every such sequence has \(\|x_d\|\to0\);
- for \(\alpha>-1/2\), every such sequence has \(\|x_d\|\to1\);
- at \(\alpha=-1/2\), the distance of \(\|x_d\|\) from the two-point set \(\{0,1\}\) tends to zero (no selection between the endpoints is asserted).

More precisely, let \(G_k\) have the Gamma law of shape \(k\) and unit scale and let \(Z\) be a standard normal variable, independently. Uniformly for \(0\le r\le1\),
\[
\lim_{d\to\infty}\sup_{0\le r\le1}\left|\frac{\Lambda_{d,k}(r e_1)}d-
\frac12\mathbb E\left|\frac{1-r^2}{k}(G_k-k)+r^2(Z^2-1)\right|\right|=0.
\]

At the center the finite-dimensional kernel has one radial sign change, at squared radius \((d+2)/(d+2k+2)\). In particular, the unweighted case has the exact identity
\[
\Lambda_{d,1}(0)=(d+4)\left(\frac{d+2}{d+4}\right)^{d/2+1}-1.
\]

## Assumptions and scope

All limits hold for a **fixed** \(k>0\) as the ambient **dimension** \(d\to\infty\); the polynomial degree remains exactly two. The probability measure is normalized to mass one. The ball is closed for point evaluation, and the essential-supremum operator norm equals the maximum of the continuous Lebesgue function on the closed ball. The theorem concerns the specific orthogonal projector, not the least norm among all projections onto the same polynomial space. No assertion is made for a dimension-dependent weight exponent or higher polynomial degree.

## Proof

**1. Exact polynomial reproducing kernel.** Write \(D=d+2k\), \(m=d/D\), and \(S=\|Y\|^2\) for \(Y\sim\mu_{d,k}\). The normalized ball moments are
\[
\mathbb E[Y_iY_j]=\frac{\delta_{ij}}D,\qquad
\mathbb E[Y_iY_jY_\ell Y_h]
=\frac{\delta_{ij}\delta_{\ell h}+\delta_{i\ell}\delta_{jh}+\delta_{ih}\delta_{j\ell}}{D(D+2)}.
\]
In particular, \(S\) has the \(\mathrm{Beta}(d/2,k)\) distribution and
\[
\mathbb ES=m,\qquad \operatorname{Var}(S)=\frac{4dk}{D^2(D+2)}.
\]
Constants, linear polynomials, trace-free quadratics, and the radial quadratic \(\|y\|^2-m\) form pairwise orthogonal subspaces. The moment identities give their four reproducing kernels. Summing them yields the explicit polynomial
\[
\boxed{K_{d,k}(x,y)=1+D\langle x,y\rangle
+\frac{D(D+2)}2\left(\langle x,y\rangle^2-\frac{\|x\|^2\|y\|^2}{d}\right)
+\frac{D^2(D+2)}{4dk}(\|x\|^2-m)(\|y\|^2-m).}
\]
This identity can also be checked by integration against each of the monomials \(1\), \(y_i\), and \(y_i y_j\). Since the kernel represents the orthogonal projector, \(\|P_{d,k}\|_{\infty\to\infty}=\max_{x\in B^d}\Lambda_{d,k}(x)\): the upper bound is immediate and the lower bound is witnessed, at any fixed point \(x\), by the phase or sign of \(K_{d,k}(x,\cdot)\). The Lebesgue function is continuous, rotationally invariant, and thus depends only on \(\|x\|\).

**2. Coupled Gaussian and Gamma limit.** For every \(d\) take \(R_d^2\sim\mathrm{Beta}(d/2,k)\) and an independent uniform spherical direction \(U_d\in\mathbb S^{d-1}\), so that \(Y_d=R_d U_d\) has law \(\mu_{d,k}\). Set
\[
V_d=\frac d2(1-R_d^2),\qquad Z_d=\sqrt d\,(U_d)_1.
\]
There is a coupling for which \(V_d\to G_k\) and \(Z_d^2\to Z^2\) almost surely and in \(L^1\), while their respective pairs remain independent. Indeed, take independent infinite sequences of standard Gaussian variables \((H_j)\) and \((J_j)\) and a Gamma variable \(G_k\), and put
\[
R_d^2=\frac{\frac12\sum_{j=1}^dH_j^2}{\frac12\sum_{j=1}^dH_j^2+G_k},\qquad
U_d=\frac{(J_1,\ldots,J_d)}{(\sum_{j=1}^d J_j^2)^{1/2}}.
\]
The strong law proves almost-sure convergence. The nonnegative variables satisfy \(\mathbb EV_d=dk/(d+2k)\to k=\mathbb E G_k\) and \(\mathbb EZ_d^2=1=\mathbb EZ^2\); these equalities, together with almost-sure convergence, imply convergence in \(L^1\) (Scheffé's lemma).

With \(x=r e_1\), divide the exact kernel by \(d\). The constant term is \(1/d\). The linear term has uniformly bounded expected absolute value of order \(d^{-1/2}\). The trace-free quadratic term is
\[
\frac{D(D+2)}{2d^2}\,r^2 R_d^2 (Z_d^2-1)
\longrightarrow\frac{r^2}2(Z^2-1)
\]
in \(L^1\), uniformly in \(r\in[0,1]\). For the radial term, use the exact identity \(R_d^2-m=2k/D-2V_d/d\); its normalization by \(d\) converges in \(L^1\), again uniformly in \(r\), to \((1-r^2)(G_k-k)/(2k)\). The required uniform convergence of \(\Lambda_{d,k}(r e_1)/d\) follows from \(|\mathbb E|A|-\mathbb E|B||\le\mathbb E|A-B|\), with the same coupling for all \(r\).

**3. Optimize the limiting radial profile.** Put \(t=r^2\) and
\[
F_k(t)=\frac12\mathbb E\left|(1-t)\left(\frac{G_k}{k}-1\right)+t(Z^2-1)\right|,
\quad 0\le t\le1.
\]
The function \(F_k\) is convex, hence its maximum occurs at one or both endpoints. Its endpoint values can be evaluated without approximation:
\[
F_k(0)=\frac{1}{2k}\mathbb E|G_k-k|=\frac{k^k e^{-k}}{\Gamma(k+1)},
\qquad
F_k(1)=\frac12\mathbb E|Z^2-1|=2\frac{e^{-1/2}}{\sqrt{2\pi}}.
\]
For the Gamma identity, integrate \((u-k)u^{k-1}e^{-u}\) on \([k,\infty)\) by parts and use its zero mean. For the Gaussian identity, integrate \((z^2-1)e^{-z^2/2}\) over \([1,\infty)\) and use symmetry.

The function \(k\mapsto F_k(0)\) is strictly decreasing. An elementary proof uses Gamma additivity: if \(0<k_1<k_2\), write \(X\sim\mathrm{Gamma}(k_1,1)\), \(Y\sim\mathrm{Gamma}(k_2-k_1,1)\) independently. Then \(\mathbb E[X/k_1\mid X+Y]=(X+Y)/k_2\). Conditional Jensen for \(u\mapsto|u-1|\) gives \(F_{k_2}(0)\le F_{k_1}(0)\), strictly because on the event \(X+Y>k_1\), which has positive probability, the conditional Beta law of \(X/k_1\) crosses \(1\) with positive probabilities on both sides. At \(k=1/2\), the variable \(G_k/k\) has the same chi-square-one distribution as \(Z^2\). Therefore
\[
F_{1/2}(0)=F_{1/2}(1)=\sqrt{\frac2{\pi e}},
\]
and strict monotonicity establishes the unique transition. For \(0<t<1\), the convexity inequality is strict because the two independent centered random variables have opposite signs on an event of positive probability. Thus \(F_k\) has its unique maximizer at \(t=0\) below the threshold and at \(t=1\) above it; at the threshold its maximizing set is exactly \(\{0,1\}\).

The convergence in Step 2 is uniform in radius on a compact interval. Its maxima therefore converge to the maximum of \(F_k\), and every limit point of maximizing radii belongs to the just-identified maximizing set. This proves both the sharp norm constant and the location assertions.

**4. Exact finite-dimensional center check.** At \(x=0\), the kernel from Step 1 reduces to
\[
K_{d,k}(0,y)=\frac{D(D+2)}{4k}\left(\frac{d+2}{D+2}-\|y\|^2\right).
\]
Thus the stated sign-change radius is exact. For \(k=1\), the variable \(S=\|Y\|^2\) has density \((d/2)s^{d/2-1}\) on \((0,1)\). Splitting the integral at \((d+2)/(d+4)\) and using \(\int K_{d,1}(0,y)\,d\mu_{d,1}(y)=1\) gives the center formula in the finding.

## Verification

The accompanying standalone `check_ball_quadratic.py` evaluates the exact reproducing-kernel identities over four dimensions and four rational weights; checks every monomial of total degree at most two; checks the exact center sign factorization; compares the center beta-integral formula with independent quadrature; checks Gamma-deviation values and transition ordering; and compares finite-dimensional samples with the derived asymptotic endpoints. Its output for the stated version is `PASS: 308 independent finite/exact computations.` Numerical simulation checks are diagnostic only. The infinite-dimensional and dimension-limit assertions are established in the proof above, not by those computations. Run with `python check_ball_quadratic.py` in an environment with SymPy, SciPy, and NumPy.

## Relationship to prior work

Li and Xu (2013, arXiv:1310.2283) develop polynomial orthogonal expansions and Sobolev spectral approximation on Euclidean balls, including a degree decomposition but not the present sharp dimension-asymptotic endpoint norm or radial maximizer transition. Figueroa (2016, arXiv:1607.00930, first posted 2016-07-04) studies the same weighted orthogonal projectors in weighted Sobolev norms; its main theorem concerns convergence with the polynomial cutoff at fixed dimension. The present claim instead fixes polynomial degree two and lets dimension grow, computing the sharp \(L^\infty\) amplification coefficient.

Defant, Galicer, Mansilla, Mastyło and Muro (2024, arXiv:2405.12123) analyze minimal projection constants for polynomial spaces on **spheres**. Their spherical endpoint machinery can account for a related Gaussian quadratic constant, but their measure, target space, and minimization problem do not give the weighted-ball radial Gamma contribution or its \(\alpha=-1/2\) transition. A published quadratic simplex computation likewise concerns a different geometry: the simplex moment law does not imply the weighted-ball radial profile.

## Limitations

No finite-dimensional closed formula for the global norm or exact finite-dimensional maximizing radius is claimed. At the critical weight \(\alpha=-1/2\), the result proves only that maximizing radii approach the union of center and boundary; it does not choose which region dominates at finite dimension. No rate of convergence is asserted uniformly as the weight parameter varies. The conclusion applies to this canonical \(L^2\)-orthogonal projector, not arbitrary degree-two projection schemes or all polynomial degrees. A historical equivalent under a less direct Christoffel/Lebesgue-function formulation is possible and requires independent bibliographic scrutiny.

## References

1. Huiyuan Li and Yuan Xu, *Spectral approximation on the unit ball*, arXiv:1310.2283, first publicly posted 2013-10-08; especially §2.2, §4, and the appendices. https://arxiv.org/abs/1310.2283
2. Leonardo E. Figueroa, *Orthogonal polynomial projection error measured in Sobolev norms in the unit ball*, arXiv:1607.00930, first publicly posted 2016-07-04; especially §§1–4. https://arxiv.org/abs/1607.00930
3. Andreas Defant, Daniel Galicer, Martín Mansilla, Mieczysław Mastyło and Santiago Muro, *Minimal projections onto spaces of polynomials on real Euclidean spheres*, arXiv:2405.12123, first publicly posted 2024-05-20; §5. https://arxiv.org/abs/2405.12123
