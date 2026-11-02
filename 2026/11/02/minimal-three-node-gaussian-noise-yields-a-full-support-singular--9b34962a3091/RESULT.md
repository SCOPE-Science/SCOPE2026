# Minimal three-node Gaussian noise yields a full-support singular Ornstein–Uhlenbeck invariant law

## Finding
For the Ornstein–Uhlenbeck (OU) equation \(dX_t=-\lambda X_t\,dt+\sqrt{2\lambda v}\,dW_t\), replace the exact-step standard-normal innovation with the minimal three-point Gauss–Hermite law \(\xi\in\{-\sqrt3,0,\sqrt3\}\) having weights \(1/6,2/3,1/6\). At \(h=(\log3)/\lambda\), the resulting stationary state has **interval support but a singular continuous distribution**, at total-variation distance one from the OU Gaussian invariant law. Nevertheless every stationary joint polynomial moment of total degree at most five, at every finite selection of grid times, matches the Gaussian OU exactly; the sixth centered moment is the first to differ. This is a counterexample to using finite moment fidelity or exact autocovariances as evidence of invariant-law fidelity.

Precisely, with stationary law \(\mu\),
\[
\operatorname{supp}\mu=[-\sqrt{6v},\sqrt{6v}],\qquad
\|\mu-N(0,v)\|_{\mathrm{TV}}=1,
\]
where total variation is \(\sup_B|\mu(B)-N(0,v)(B)|\). Its exact dimension is
\[
\dim_{\mathrm H}\mu=\frac{-2(1/6)\log(1/6)-(2/3)\log(2/3)}{\log3}\approx0.789690082143.
\]
The sixth-moment deficit is
\[
\mathbb E_\mu[Y^6]=\frac{981}{91}v^3,\quad
\mathbb E_{N(0,v)}[X^6]=15v^3,\quad
\kappa_6(\mu)=-\frac{384}{91}v^3.
\]

## Assumptions and scope
Fix \(\lambda,v>0\) and time step \(h>0\). Let \(r=e^{-\lambda h}\in(0,1)\), \(c=\sqrt{v(1-r^2)}\), and let all \(\xi_j\) be independent with \(\Pr(\xi=0)=2/3\) and \(\Pr(\xi=\pm\sqrt3)=1/6\). Define the numerical Markov chain \(Y_{n+1}=rY_n+c\xi_{n+1}\). The exact sampled OU chain has the same affine drift but standard-normal innovations. The key singularity and joint-moment statements concern the *stationary* regime at \(r=1/3\), i.e., \(h=(\log3)/\lambda\). At any fixed finite time, matching polynomial moments through degree five also holds from the same deterministic starting value.

The chain is an exact OU conditional-mean discretization with a finite-support noise surrogate, not Euler–Maruyama with Gaussian Brownian increments; no general-mesh or small-step total-variation approximation is asserted. The standard-normal invariant distribution is \(N(0,v)\).

## Proof
**1. Minimal Gaussian moment surrogate.** Direct calculation gives \(\mathbb E\xi=\mathbb E\xi^3=\mathbb E\xi^5=0\), \(\mathbb E\xi^2=1\), \(\mathbb E\xi^4=3\), whereas \(\mathbb E\xi^6=9\) rather than the Gaussian value \(15\). If a probability measure with one or two support points matched Gaussian moments through degree four, the nonzero polynomial vanishing at all its atoms (of degree at most two) would have square of expectation zero for that measure but positive for a nondegenerate Gaussian, a contradiction. For an arbitrary three-point rule matching moments through degree five, the monic cubic whose roots are the three atoms must be orthogonal to all polynomials of degree at most two under the standard Gaussian. The unique such cubic is \(z^3-3z\), giving nodes \(0,\pm\sqrt3\); the first two moments uniquely give their displayed probabilities.

**2. Stationarity and moment matching.** For every \(0<r<1\), the affine recursion has unique invariant probability law
\[
Y\overset d= c\sum_{j=0}^{\infty}r^j\xi_{-j},
\]
by geometric contraction (absolute convergence is immediate because the innovations are bounded). The exact stationary OU sampled on the same grid is \(X\overset d=c\sum_{j\ge0}r^jZ_{-j}\), with independent standard-normal innovations. For any finite truncation, any polynomial of total degree at most five in finitely many chain states is a polynomial of total degree at most five in the independent innovations; each innovation has the same moments through order five under \(\xi\) and \(Z\). Its expectations therefore agree identically. Geometric decay and bounded moments give convergence in \(L^5\) of the truncated stationary sums, which passes the identities to the limit. In particular \(\operatorname{Cov}(Y_n,Y_{n+k})=v r^k\) for every integer \(k\ge0\), exactly as in the sampled OU.

The sixth cumulant of \(\xi\) is \(9-15\cdot3\cdot1+30\cdot1^3=-6\). Additivity and scaling of cumulants in the stationary series give
\[
\kappa_6(Y)=-6c^6\sum_{j\ge0}r^{6j}=-6v^3\frac{(1-r^2)^3}{1-r^6}.
\]
At \(r=1/3\) this is \(-384v^3/91\); all cumulants of orders three through five vanish and variance equals \(v\). Thus the sixth central moment is \(15v^3-384v^3/91=(981/91)v^3\).

**3. Support frontier.** Put \(a=c\sqrt3\). The stationary support is the unique compact attractor of the maps \(u\mapsto ru-a\), \(u\mapsto ru\), and \(u\mapsto ru+a\), since every atom has positive probability. Its bounding interval is \(I=[-a/(1-r),a/(1-r)]\). The three images of \(I\) have radius \(ra/(1-r)\) and centers separated by \(a\). These intervals cover all of \(I\) exactly when \(2r/(1-r)\ge1\), equivalent to \(r\ge1/3\); uniqueness of the compact attractor then makes the support \(I\). Below \(1/3\), three disjoint pieces recur at every scale and the attractor is a proper nowhere-dense Cantor set. At \(r=1/3\), \(a=\sqrt{8v/3}\), so the interval endpoints are \(\pm3a/2=\pm\sqrt{6v}\).

**4. Full support but singularity at the frontier.** Write \(\xi_j=\sqrt3(D_j-1)\), where \(D_j\in\{0,1,2\}\) independently with probabilities \((1/6,2/3,1/6)\). At \(r=1/3\), the affine transform of \(Y\) given by
\[
U=\frac{1}{3}\left(\frac{Y}{c\sqrt3}+\frac32\right)
   =\sum_{j=0}^{\infty}\frac{D_j}{3^{j+1}}
\]
has biased independent ternary digits. Every ternary cylinder has positive probability, giving support \([0,1]\). Each single digit sequence has probability at most \((2/3)^n\) after \(n\) levels; allowing the countably many dual expansions changes nothing, so there are no atoms. By the strong law, almost every \(U\) has digit frequencies \((1/6,2/3,1/6)\), while Lebesgue-almost every \(u\in[0,1]\) has digit frequencies \((1/3,1/3,1/3)\). These disjoint full-measure properties prove singularity. Since the Gaussian invariant law has a Lebesgue density, their total-variation distance is one.

For completeness, the strong law also gives the cylinder-mass local exponent \(H=-\sum p_j\log p_j\). Typical-cylinder counting gives an upper Hausdorff dimension \(H/\log3\), and restricting to sets on which \(\mu(C_n(u))\le 3^{-ns}\) eventually, for every \(s<H/\log3\), gives the reverse lower bound by covering each short interval with at most two level-comparable ternary cylinders meeting that restricted set. Hence \(\dim_{\mathrm H}\mu=H/\log3\). The equality uses the standard definition \(\dim_{\mathrm H}\mu=\inf\{\dim_{\mathrm H}E:\mu(E)=1\}\).

## Verification
Run \(\texttt{python3 verify.py}\) with Python 3 and no third-party dependencies. The checker uses exact fractions to verify Gaussian three-node moments through degree six, the stationary moment recurrence, \(21\) mixed one-lag moments up to total degree five, \(12\) finite-time moment steps from a common deterministic initialization, and the support overlap inequality. It also prints the entropy-dimension constant. Analytical steps 1–4, not finite computations, establish the infinite-dimensional, singularity and support claims.

## Relationship to prior work
López-Yela and Míguez [1], first public in June 2021, develop polynomial moment propagation and density reconstruction for stochastic numerical methods. This theorem instead shows that an exact five-moment surrogate of the Gaussian OU transition can still have an invariant distribution singular to the Gaussian, with the maximal total-variation error, despite matching all lag covariances. Li, Lu, Mattingly and Wang [2] use the same characteristic three-point weights in a *Gaussian-mixture* weak integrator, but retain a conditional Gaussian component. Their analyzed transition laws are not this purely three-atom affine recursion and do not imply its biased-ternary singular invariant law or the precise six-moment gap. Biased ternary measures, their digit-frequency singularity, and Gaussian quadrature are classical inputs; originality is claimed for their numerical-sampling synthesis and sharp stationary counterexample, not for those classical facts individually. The complete specialized literature may contain an equivalent construction.

## Limitations
This is a scalar linear OU model at a particular finite step size; it is not a claim about weak convergence rates as \(h\to0\), nonlinear SDEs, or arbitrary finite-support noise laws. Total-variation singularity is shown at the critical ratio \(1/3\); an interval-supported invariant measure at other ratios need not be singular. Finite-moment tests alone cannot verify the measure-theoretic assertions. No independent scientific priority audit has been performed.

## References
1. A. López-Yela and J. Míguez, *Polynomial propagation of moments in stochastic differential equations*, arXiv:2106.06271, first public 2021-06-11. https://arxiv.org/abs/2106.06271. Subsequently published in *SIAM Journal on Applied Dynamical Systems* 22 (2023), 1153–1181, DOI 10.1137/21M1431497.
2. L. Li, J. Lu, J. Mattingly, and L. Wang, *Numerical methods for stochastic differential equations based on Gaussian mixture*, arXiv:1812.11932, first public 2018-12-31. https://arxiv.org/abs/1812.11932.
3. H. Zähle, *Weak Approximation of SDEs by Discrete-Time Processes*, *International Journal of Stochastic Analysis* (2008), DOI 10.1155/2008/275747; discusses weak approximations, without the fixed-step invariant-law claim here.
