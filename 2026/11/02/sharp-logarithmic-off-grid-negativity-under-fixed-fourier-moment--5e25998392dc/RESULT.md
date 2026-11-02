# Sharp logarithmic off-grid negativity under fixed Fourier moment conservation

## Finding

Write \(d\mu(x)=dx/(2\pi)\) on the periodic circle \(\mathbb T\). Fix an integer \(K\geq1\). For every integer \(N\geq K\), let \(m=2N+1\), let \(x_j=2\pi j/m\) for \(0\leq j<m\), and define the closed convex class
\[
\mathcal C_{N,K}=\{p\in\mathcal T_N:\ p(x_j)\geq0\ (0\leq j<m),\ \widehat p(0)=1,\ \widehat p(k)=0\ (1\leq k\leq K)\},
\]
where \(\mathcal T_N\) is the real trigonometric-polynomial space with frequencies of absolute value at most \(N\), and \(\widehat p(k)=\int p(x)e^{-ikx}\,d\mu(x)\). Let \(\mathcal A_K\) be the strictly positive, real-analytic, periodic functions \(f\) satisfying these same Fourier-moment equations. Denote the unique constrained \(L^2(\mu)\) projection of \(f\in\mathcal A_K\) onto \(\mathcal C_{N,K}\) by \(Q_{N,K}f\).

For the integrated off-grid negative mass \(\mathcal N(p)=\int_{\mathbb T}(-p(x))_+\,d\mu(x)\), the sharp worst-case law is
\[
\boxed{\sup_{f\in\mathcal A_K}\mathcal N(Q_{N,K}f)
=\frac{2}{\pi^2}\log N+O_K(1),\qquad N\longrightarrow\infty.}
\]
In particular, preserving any **fixed positive number of low Fourier moments** does not improve the logarithmic leading coefficient already associated with the classical Dirichlet kernel. The lower bound uses strictly positive real-analytic inputs for each resolution, not merely nonnegative nodal data. No claim of a common adverse input as \(N\) varies is made.

## Assumptions and scope

The result concerns one-dimensional equispaced Fourier collocation with \(2N+1\) points, mass normalization \(\widehat f(0)=1\), conservation of the complex Fourier moments \(\widehat f(k)=0\) for \(1\leq k\leq K\), and positivity **only on the collocation grid**. These Fourier-moment constraints are a natural linear-moment variant of positive, moment-preserving spectral projection; they are not asserted to be the polynomial kinetic-energy and momentum constraints of every application. The number \(K\) is fixed as \(N\to\infty\), and the supremum permits the positive input to depend on \(N\).

The feasible set contains the constant polynomial \(1\), so it is nonempty. Strict convexity of the squared \(L^2\) distance in the finite-dimensional real space ensures the projection exists and is unique. The complex Fourier constraints are equivalent to \(2K\) real sine/cosine moment constraints.

## Proof

**1. A universal upper bound from the interpolation simplex.** Let
\[
D_N(t)=\sum_{k=-N}^{N}e^{ikt}=\frac{\sin((N+1/2)t)}{\sin(t/2)},
\]
with its removable values at integral multiples of \(2\pi\). Exact trigonometric interpolation gives, for every \(p\in\mathcal T_N\),
\[
p(x)=\sum_{j=0}^{m-1}\frac{p(x_j)}m D_N(x-x_j).
\]
If \(p\in\mathcal C_{N,K}\), the coefficients \(a_j=p(x_j)/m\) are nonnegative and sum to \(1\), by the exact grid quadrature of its constant Fourier coefficient. Because the negative-part map is convex and the circle integral is translation invariant,
\[
\mathcal N(p)\leq\sum_j a_j\mathcal N(D_N)=\mathcal N(D_N).
\]
Also \(\int D_N\,d\mu=1\), so \(\mathcal N(D_N)=(\int|D_N|\,d\mu-1)/2\). The classical Dirichlet estimate, reproduced here from the explicit kernel, is
\[
\int_{-\pi}^{\pi}|D_N(x)|\,dx=\frac8\pi\log N+O(1).
\]
Indeed, on a fixed small neighborhood of zero, \(|\sin(x/2)|^{-1}=2/|x|+O(|x|)\) and \(\int_1^T|\sin y|\,dy/y=(2/\pi)\log T+O(1)\); away from zero the kernel is uniformly bounded. Consequently
\[
\mathcal N(D_N)=\frac2{\pi^2}\log N+O(1).
\]
This upper bound applies to all feasible projections, independently of the moment equations.

**2. Positive discrete quadrature annihilating the prescribed moments.** Put \(q=2K+1\). For each sufficiently large \(N\), select \(q\) distinct grid phases \(\theta_{j,N}\), each within \(O_K(m^{-1})\) of \(2\pi j/q\), for \(0\leq j<q\). Consider the square real matrix whose rows, evaluated at these phases, are \(1\) followed by \(\cos(kx),\sin(kx)\) for \(1\leq k\leq K\). At the exact \(q\)-th roots of unity this is an invertible real discrete Fourier matrix; the weights \(1/q\) solve the mass-one and zero-low-moment equations. By continuous dependence of the inverse on the phases, for sufficiently large \(N\) there are unique weights \(w_{j,N}=1/q+O_K(m^{-1})>0\) satisfying
\[
\sum_j w_{j,N}=1,\qquad \sum_j w_{j,N}e^{-ik\theta_{j,N}}=0\quad(1\leq k\leq K).
\]
The nodes remain separated by a positive constant depending only on \(K\).

**3. Moment-feasible interpolants with maximal leading negative mass.** Set
\[
p_N(x)=\sum_{j=0}^{q-1}w_{j,N}D_N(x-\theta_{j,N}).
\]
Its Fourier coefficients satisfy precisely the required equations. At a grid site, \(D_N(x_\ell-x_j)=m\) if the two sites agree and \(0\) otherwise. Thus \(p_N\) has the nonnegative nodal values \(m w_{j,N}\) at the selected sites and zero at every other site: \(p_N\in\mathcal C_{N,K}\).

To estimate its continuous \(L^1\) norm, choose disjoint fixed-radius neighborhoods of the \(q\) selected phases, all of radius depending only on \(K\). On the neighborhood of \(\theta_{j,N}\), every shifted Dirichlet kernel centered at another selected phase is uniformly \(O_K(1)\), because its denominator stays separated from zero. Therefore the difference between \(|p_N|\) and \(w_{j,N}|D_N(x-\theta_{j,N})|\) integrates to \(O_K(1)\) there. Outside these neighborhoods the entire sum is uniformly \(O_K(1)\). Every fixed-radius neighborhood of a Dirichlet singularity contributes \((8/\pi)\log N+O_K(1)\) to its \(L^1\) integral. Summing and using \(\sum_jw_{j,N}=1\) yields
\[
\int_{-\pi}^{\pi}|p_N(x)|\,dx=\frac8\pi\log N+O_K(1),\qquad
\mathcal N(p_N)=\frac2{\pi^2}\log N+O_K(1).
\]

**4. Strictly positive analytic input realization.** Let \(P_r(t)=(1-r^2)/(1-2r\cos t+r^2)\) for \(0<r<1\). Its Fourier coefficient at frequency \(k\) is \(r^{|k|}\), and it is strictly positive and real analytic. For each fixed \(N\), define
\[
f_{r,N}(x)=\sum_{j=0}^{q-1}w_{j,N}P_r(x-\theta_{j,N}).
\]
The positive weights imply \(f_{r,N}>0\). Its mass and its first \(K\) complex Fourier moments are precisely those of \(p_N\), since \(\widehat f_{r,N}(k)=r^{|k|}\widehat p_N(k)\) for \(|k|\leq N\). Hence \(f_{r,N}\in\mathcal A_K\), and its ordinary degree-\(N\) Fourier projection \(\mathcal P_N f_{r,N}\) tends to \(p_N\) in \(L^2(\mu)\) as \(r\uparrow1\).

The constrained projection is the metric projection of \(\mathcal P_N f\) onto the **fixed** closed convex set \(\mathcal C_{N,K}\). Metric projections onto closed convex subsets of a Hilbert space are nonexpansive. Since \(p_N\) already belongs to this set,
\[
\|Q_{N,K}f_{r,N}-p_N\|_{L^2(\mu)}
\leq\|\mathcal P_N f_{r,N}-p_N\|_{L^2(\mu)}\longrightarrow0.
\]
The negative-mass functional is \(L^1\)-Lipschitz, and the normalized circle measure has mass one, so \(\mathcal N(Q_{N,K}f_{r,N})\to\mathcal N(p_N)\). The supremum over strictly positive analytic inputs is therefore at least \(\mathcal N(p_N)\). Combining with Step 1 proves the claimed sharp leading coefficient.

## Verification

The standalone `verify.py` reconstructs the real moment matrix on actual odd Fourier grids for \(K=0,1,2,3\) and \(N=31,47,79,127\), solves for positive weights, checks all moment equations and \(2288\) nodal interpolation identities, and numerically compares the resulting negative mass with the Dirichlet upper bound. It also checks Parseval coefficient convergence of the Poisson regularization and differences of high-degree Dirichlet negative masses against the theoretical coefficient \(2/\pi^2\). Run `python verify.py` with Python 3 and its standard library. These finite checks support, but do not replace, the proof of the uniform asymptotic law or the analytic-input supremum statement.

## Relationship to prior work

Cai, Lin and Lin's 2023 positive moment-preserving Fourier spectral method uses a convex projection enforcing nonnegative values at equispaced Fourier collocation points and conservation laws; it proves spectral approximation accuracy for suitable **fixed** nonnegative inputs. That source expressly distinguishes collocation positivity from unrestricted pointwise positivity. The present result addresses a different issue: the sharp worst-case amount of **between-grid** negative mass as the Fourier degree increases, under fixed low-Fourier-moment constraints and input families varying with the degree. It does not contradict fixed-input convergence.

The classical logarithmic growth of the Dirichlet kernel's \(L^1\) norm is used as a known starting point (and rederived to leading order), not claimed as new. The added structural step is that any fixed finite number of Fourier moment constraints still permits **the same sharp coefficient**, with positive quadrature weights and analytic-input realization. Prior spectral positivity-limiters study pointwise control at prescribed nodes but do not, in the consulted material, state this moment-constrained sharp integrated-negative-mass extremal law.

## Limitations

Only one-dimensional odd-grid trigonometric collocation and finitely many zero-valued low Fourier moments are treated. No result is asserted for arbitrary nonzero polynomial kinetic moments, for a number of moments increasing with degree, or for multidimensional grids. The supremum uses a different narrow positive analytic input at each resolution and therefore gives no fixed-function divergence result. The \(O_K(1)\) remainder is not an exact finite-degree extremum. There is no rounding-error, PDE time-step or quantitative physical-prediction claim. The direct publication-priority comparison is not independently audited; specialized prior approximation-theory results may still overlap.

## References

1. Z. Cai, B. Lin, M. Lin, *A positive and moment-preserving Fourier spectral method*, arXiv:2304.11847v1, first posted 2023-04-24. https://arxiv.org/html/2304.11847v1
2. M. P. Laiu and C. D. Hauck, *Positivity limiters for filtered spectral approximations of linear kinetic transport equations*, Journal of Scientific Computing 78 (2019), DOI:10.1007/s10915-018-0790-y; first published online 2018-08-11. https://doi.org/10.1007/s10915-018-0790-y
3. G. H. Hardy, *Note on Lebesgue's constants in the theory of Fourier series*, Journal of the London Mathematical Society 17 (1942), 4–13, DOI:10.1112/jlms/s1-17.1.4. https://doi.org/10.1112/jlms/s1-17.1.4
