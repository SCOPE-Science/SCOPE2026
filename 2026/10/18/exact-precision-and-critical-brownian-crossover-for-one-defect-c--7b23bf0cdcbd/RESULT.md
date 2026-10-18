# Exact precision and critical Brownian crossover for one-defect cycle Lipschitz balls

## Finding

For every integer \(d\ge 2\) and length \(0<t\le d\), take the cycle on \(d+1\) vertices whose consecutive path edges have length \(1\) and whose closing edge has length \(t\), with the geodesic metric. Let \(Q_{d,t}\) be the anchored-coordinate unit ball of its real Lipschitz dual, with the first path vertex fixed at value zero. Let \(F=(F_1,\ldots,F_d)\) be uniform in \(Q_{d,t}\), and put \(F_0=0\). The exact covariance and *precision* (inverse covariance) matrices of \(F\) admit one-dimensional finite-sum evaluations and the precision matrix is tridiagonal, with a strictly positive terminal pinning term precisely when the closing edge is nonredundant.

Set \(S_d=Z_1+\cdots+Z_d\), where the \(Z_i\) are independent \(\operatorname{Unif}[-1,1]\). Write its density as
\[
h_d(s)=\frac{1}{2^d(d-1)!}\sum_{k=0}^{d}(-1)^k\binom dk(s+d-2k)_+^{d-1},
\qquad (x)_+=\max\{x,0\}.
\]
All integrations below are over explicitly known piecewise polynomials, hence are finite binomial-sum expressions. Define
\[
P=2\int_0^t h_d(s)\,ds,\quad
J=\int_0^t s^2h_d(s)\,ds,\quad
K=\int_t^d s h_d(s)\,ds,
\]
\[
v=1-\frac{4(J+tK)}{dP},\qquad
b=\frac{2J}{P},\qquad
\eta=\frac{b-dv}{d(d-1)},\quad
\delta=v-\eta,\quad \mu=\frac bd.
\]
Then \(P>0\), \(\delta>0\), \(\mu>0\), and, for every \(1\le i,j\le d\),
\[
\boxed{\operatorname{Cov}(F_i,F_j)=\delta\min(i,j)+\eta i j.}
\]
Let \(D\) be the \(d\)-by-\(d\) first-difference matrix, \((Dx)_1=x_1\) and \((Dx)_i=x_i-x_{i-1}\) for \(i\ge2\). With \(e_d\) the final coordinate vector,
\[
\boxed{\operatorname{Cov}(F)^{-1}
=\frac1\delta D^{\mathsf T}D+\gamma e_de_d^{\mathsf T},
\quad \gamma=-\frac{\eta}{\delta\mu}.}
\]
In particular, all precision entries with \(|i-j|\ge2\) are exactly zero, the neighboring entries equal \(-1/\delta\), and \(\gamma>0\) if \(0<t<d\), while \(\gamma=0\) for \(t=d\). Moreover,
\[
\det\operatorname{Cov}(F)=\delta^{d-1}\mu.
\]
These are covariance statements, not assertions of conditional independence of the non-Gaussian coordinates. The familiar anchored volume formula \(\operatorname{vol}_d(Q_{d,t})=2^dP\) is included for normalization and is not itself claimed as a new volume theorem.

There is a sharp dimension-dependent crossover. Let \(d\to\infty\) along positive lengths \(t_d\le d\) for which \(t_d/\sqrt d\to a\in(0,\infty]\). Let \(\Phi,\varphi\) be the standard normal distribution and density; put
\[
p_a=2\Phi(\sqrt3a)-1,\quad
\kappa_a=1-\frac{2\sqrt3a\,\varphi(\sqrt3a)}{p_a}
\]
for finite \(a>0\), and \(p_\infty=\kappa_\infty=1\). Then
\[
\boxed{\frac{\operatorname{vol}_d(Q_{d,t_d})}{2^d}\longrightarrow p_a,\qquad
 d\gamma\longrightarrow \frac{3(1-\kappa_a)}{\kappa_a}.}
\]
For \(s,u\in[0,1]\), with \(F_0=0\),
\[
\boxed{\frac1d\operatorname{Cov}\bigl(F_{\lfloor ds\rfloor},F_{\lfloor du\rfloor}\bigr)
\longrightarrow\frac13\bigl[\min(s,u)-(1-\kappa_a)su\bigr].}
\]
The piecewise-linear path interpolating the mesh values \(d^{-1/2}F_i\) at times \(i/d\) converges in law in \(C[0,1]\) to
\[
\frac1{\sqrt3}\bigl(B^{\mathrm{br}}(s)+sG_a\bigr),
\]
where \(B^{\mathrm{br}}\) is a standard Brownian bridge and \(G_a\) is an independent standard normal variable conditioned to lie in \([-\sqrt3 a,\sqrt3a]\) (unconditioned for \(a=\infty\)). For \(t_d/\sqrt d\to0\) the volume ratio tends to zero; for \(t_d/\sqrt d\to\infty\) it tends to one. Thus the scale \(t\asymp\sqrt d\) separates vanishing, nontrivial, and asymptotically full volume ratios. As \(a\downarrow0\), the displayed nondegenerate-crossover limit itself approaches a Brownian bridge; no small-event functional limit is asserted for arbitrary sequences with \(t_d/\sqrt d\to0\). Finally, for \(a\in(0,\infty]\), the affine-invariant isotropic constant of \(Q_{d,t_d}\) tends to \(1/\sqrt{12}\).

## Assumptions and scope

The graph is an undirected weighted cycle and distances are shortest-path distances. The condition \(0<t\le d\) ensures that the displayed edge-length data give those geodesic distances; the edge may be redundant at \(t=d\). The natural volume is Lebesgue measure in the \(d\) anchored function coordinates \((F_1,\ldots,F_d)\), not intrinsic Euclidean measure in the zero-sum edge hyperplane. The finite-dimensional covariance result is exact for all real \(t\) in this range, not merely rational values. The functional limit is stated only for the nonvanishing-event regimes \(a\in(0,\infty]\).

## Proof

**1. Polytope and measure.** The unit Lipschitz conditions are \(|F_i-F_{i-1}|\le1\) along each of the \(d\) path edges and \(|F_d|\le t\) at the closing edge. Every other pairwise Lipschitz inequality follows by the shortest-path property. Therefore \(Z_i=F_i-F_{i-1}\) maps \(Q_{d,t}\) bijectively onto \(\{z\in[-1,1]^d:|\sum_i z_i|\le t\}\). The triangular change of variables has determinant one. Hence the uniform law corresponds exactly to independent \(\operatorname{Unif}[-1,1]\) increments conditioned on \(|S_d|\le t\). Symmetry gives \(\mathbb E F_i=0\). The inclusion-exclusion formula above is the standard convolution formula for the sum of \(d\) uniforms; in particular \(P=\mathbb P(|S_d|\le t)\).

**2. Exact individual increment variance.** Write \(q_d(s)\) for the joint density in \(s\) of \(\mathbb E[Z_1^2\mathbf1_{\{S_d\in ds\}}]\). With Fourier convention \(\widehat h(u)=\int e^{ius}h(s)\,ds\), the one-step transform is \(\psi(u)=\sin(u)/u\). Its differential equation is \(\psi''+(2/u)\psi'+\psi=0\), with removable origin. Consequently
\[
\widehat q_d(u)=-\psi''(u)\psi(u)^{d-1}
=\psi(u)^d+\frac{2}{du}\frac{d}{du}\bigl(\psi(u)^d\bigr).
\]
Set \(H(s)=\int_{|s|}^d xh_d(x)\,dx\). It is integrable, and \(H'(s)=-s h_d(s)\) almost everywhere, so \(\widehat H(u)=-(\psi(u)^d)'/u\). Fourier uniqueness yields the nonstandard but elementary identity
\[
q_d(s)=h_d(s)-\frac2d\int_{|s|}^d xh_d(x)\,dx.
\]
Integrate over \([-t,t]\) and use Fubini: \(\int_{-t}^t\int_{|s|}^d xh_d(x)\,dx\,ds=2(J+tK)\). Thus \(\mathbb E[Z_1^2\mid |S_d|\le t]=v\). Also \(\mathbb E[S_d^2\mid|S_d|\le t]=b=2J/P\). Because the conditioned increments are exchangeable and centered, their distinct-coordinate covariance is \(\eta=(b-dv)/(d(d-1))\). It follows that
\[
\operatorname{Cov}(Z)=\delta I_d+\eta\mathbf1\mathbf1^{\mathsf T},
\quad \delta=v-\eta,\quad \mu=\delta+d\eta=b/d.
\]
Both eigenvalues \(\delta,\mu\) are strictly positive since the conditioned law has positive Lebesgue density on an open subset of \(\mathbb R^d\).

**3. Strict sign and local precision.** For \(d\ge3\), let \(T=Z_3+\cdots+Z_d\), and for \(d=2\) take \(T=0\). The function \(g(w)=\mathbb P(|T+w|\le t)\) is even and nonincreasing on \([0,\infty)\): the law of \(T\) is an iterated convolution of symmetric uniform densities, hence is symmetric unimodal, and convolution with the interval indicator preserves this property. Conditional on \(Z_1=x\) and the slab event, the density of \(Z_2=y\) is proportional to \(\mathbf1_{[-1,1]}(y)g(x+y)\). For \(x>0\), pairing \(y\) and \(-y\) shows that its mean is nonpositive, because \(g(x+y)\le g(x-y)\) for \(0<y\le1\). This inequality is strict on a set of positive \((x,y)\)-measure whenever \(t<d\), since \(g\) is then nonconstant on the accessible range \((-2,2)\). The opposite sign holds for \(x<0\); hence \(\eta=\mathbb E[Z_1Z_2\mid|S_d|\le t]<0\). For \(t=d\) the slab is the full cube and \(\eta=0\).

Let \(L=D^{-1}\), so \(F=LZ\). Then \(\operatorname{Cov}(F)=L(\delta I+\eta\mathbf1\mathbf1^{\mathsf T})L^{\mathsf T}\), yielding the displayed \(\delta\min(i,j)+\eta ij\). The Sherman--Morrison rank-one inverse is \((\delta I+\eta\mathbf1\mathbf1^{\mathsf T})^{-1}=\delta^{-1}I-\eta(\delta\mu)^{-1}\mathbf1\mathbf1^{\mathsf T}\). Since \(D^{\mathsf T}\mathbf1=e_d\), conjugating by \(D\) gives the claimed tridiagonal precision plus \(\gamma e_de_d^{\mathsf T}\). Determinants are preserved by \(L\), and the increment covariance has eigenvalues \(\delta\) (multiplicity \(d-1\)) and \(\mu\) (multiplicity one), proving the determinant formula.

**4. Critical asymptotic.** Let \(a\in(0,\infty]\). The ordinary central limit theorem for bounded uniform increments gives \(S_d/\sqrt d\Rightarrow N(0,1/3)\). Therefore \(P\to p_a>0\), since the limiting normal distribution puts no mass on the boundary. Conditioning any Donsker functional limit on \(|S_d|\le t_d\) is legitimate here: the event has a positive limiting probability and is a continuity set of the joint Brownian-path limit. This proves weak convergence in \(C[0,1]\) of the linearly interpolated paths to a variance-\(1/3\) Brownian motion conditioned on its endpoint lying in \([-a,a]\). Gaussian regression decomposes this process as the independent standard bridge plus an endpoint truncated normal, with the displayed scale.

Since \(P\) stays bounded away from zero, unconditioned fourth-moment bounds give uniform integrability of \(S_d^2/d\) under conditioning. Thus \(b/d\to\kappa_a/3\). Also \(d^{-1}\sum_iZ_i^2\to1/3\) in \(L^2\) unconditionally and hence under the conditioning; by exchangeability \(v\to1/3\). Substitution yields \(d\eta\to(\kappa_a-1)/3\), \(\delta\to1/3\), \(\mu\to\kappa_a/3\) and \(d\gamma\to3(1-\kappa_a)/\kappa_a\). The covariance kernel limit follows from the exact finite formula, not from distributional convergence alone. If \(t_d/\sqrt d\to0\), the Gaussian weak limit and absence of an atom at zero imply \(P\to0\); if it tends to infinity, Chebyshev's inequality gives \(P\to1\). The isotropic constant is \((\det\operatorname{Cov}(F))^{1/(2d)}/\operatorname{vol}(Q_{d,t})^{1/d}=\bigl(\delta^{d-1}\mu\bigr)^{1/(2d)}/(2P^{1/d})\), and its stated limit follows.

## Verification

The standalone `check.py` computes the exact rational volume and covariance matrix independently by enumerating vertices of the cube-slab polytope, triangulating its facets, and integrating the simplex second moments by rational Dirichlet formulas. It compares those values against independent finite polynomial-density integrals and verifies the predicted inverse, determinant-relevant eigenvalues, and strict sign. The exact check passed 18 configurations with \(d\in\{2,3,4\}\) and \(t\in\{1/2,1,3/2,2,5/2,4\}\), including redundant-edge cases. The script invokes `python check.py` with `sympy`, `numpy` and `scipy`. Finite tests corroborate the analytic all-dimensional proof; they do not establish it by enumeration.

## Relationship to prior work

Novotný's 2019 study treats Schauder bases for graph-circle Lipschitz-free spaces, rather than bulk second moments of their uniformly distributed Lipschitz dual balls. Alexander, Fradelizi, García-Lirola and Zvavitch study finite-metric Lipschitz-free geometry and volume products, including cycle examples, not this precision-matrix theorem. Earlier weighted-cycle volume formulas already imply the scalar volume calculation in Step 1, which is used here only as a normalization rather than claimed as new. De Bruyne, Majumdar and Schehr give a general sampling construction for random-walk bridges and fixed endpoints; their paper neither evaluates the full finite cube-slab covariance and precision matrices nor identifies the weighted-cycle metric deformation parameter with the strict terminal precision correction. The Donsker and Gaussian conditioning ingredients are standard and are not separately claimed as discoveries. The claimed addition is the exact finite-dimensional geometric precision law, its strict redundancy criterion, and its sharp dimension-dependent interpolation with the conditioned-path covariance kernel.

## Limitations

The precision zeros describe linear partial correlations only; the uniform polytope law is non-Gaussian and no Markov conditional-independence claim follows. The asymptotic functional convergence is proved for \(t_d/\sqrt d\to a>0\) and \(a=\infty\), not for arbitrary sequences with vanishing ratio. The exact volume formula is known through equivalent weighted-cycle computations. Although available close literature and research records did not reveal the combined precision theorem, undiscovered equivalent work remains possible. No independent scientific audit has been performed.

## References

- Matěj Novotný, *Some Remarks on Schauder Bases in Lipschitz Free Spaces*, first publicly available 2019-05-30, arXiv:1905.13188v1, https://arxiv.org/abs/1905.13188. Primary 2010 MSC 46B20.
- Matthew Alexander, Matthieu Fradelizi, Luis C. García-Lirola and Artem Zvavitch, *Geometry and Volume Product of Finite Dimensional Lipschitz-Free Spaces*, first publicly available 2019-11-24, arXiv:1911.10642v1, https://arxiv.org/abs/1911.10642.
- Benjamin De Bruyne, Satya N. Majumdar and Grégory Schehr, *Generating Discrete-Time Constrained Random Walks and Lévy Flights*, first publicly available 2021-04-13, arXiv:2104.06145v1, https://arxiv.org/abs/2104.06145.
