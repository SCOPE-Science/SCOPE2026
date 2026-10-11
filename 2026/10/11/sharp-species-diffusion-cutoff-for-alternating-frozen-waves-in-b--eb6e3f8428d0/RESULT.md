# Sharp species–diffusion cutoff for alternating frozen waves in biased cyclic replicators

## Finding

Consider the periodic reaction–diffusion system of Visomirski and Griffin [1] on a circle of circumference \(L>0\), with an **even** number \(N\ge4\) of species, common diffusion coefficient \(D>0\), and bias \(-1<a<0\). Let the initially alternating species be
\[
u_i(x,0)=\frac{1+(-1)^{i-1}\sin(2\pi x/L)}{N},\qquad 1\le i\le N.
\]
Put \(r=-a/N>0\) and \(\omega=2\pi/L\). There is a sharp alternative:

1. **Homogenization, including the critical case.** If \(r\le D\omega^2\), every species converges uniformly to the spatially homogeneous density \(1/N\). When \(r<D\omega^2\), convergence is exponential. At equality, the squared \(L^2\)-norm of the alternating amplitude is \(O(t^{-1})\).
2. **Persistent, exactly determined standing pattern.** If \(r>D\omega^2\), the solution converges to an explicitly determined, nonconstant, stationary alternating pattern. Define the complete elliptic integral with *parameter* \(m\in[0,1)\) by
\[
K(m)=\int_0^{\pi/2}\frac{d\theta}{\sqrt{1-m\sin^2\theta}}.
\]
There is exactly one \(m\in(0,1)\) satisfying
\[
L=4K(m)\sqrt{\frac{D(1+m)}{r}}.
\]
With \(\kappa=\sqrt{r/[D(1+m)]}\), the limiting alternating amplitude is
\[
Z(x)=\sqrt{\frac{2m}{1+m}}\,\operatorname{sn}(\kappa x\mid m),
\qquad u_i(x,t)\longrightarrow\frac{1+(-1)^{i-1}Z(x)}{N}.
\]
The elliptic function \(\operatorname{sn}(\cdot\mid m)\) has spatial period \(4K(m)\). The limiting profile is positive on \((0,L/2)\) and negative on \((L/2,L)\), with no additional zeros.
3. **An explicit, positive instability eigenvalue.** Every such nonconstant stationary alternating profile is linearly unstable to general periodic perturbations *inside the alternating-species subspace*, and hence also unstable in the full reaction–diffusion system. In that subspace, its top real eigenvalue is exactly
\[
\lambda_+=\frac{r}{1+m}\left[2\sqrt{1-m+m^2}-(1+m)\right]>0.
\]

Thus the exact nontrivial-pattern condition for the specified sine initial state is
\[
\boxed{-aL^2>4\pi^2ND}.
\]
In the source's spatial normalization \(L=2\pi\), taking \(a=-1/2\), \(D=1/100\), and \(N=52\) yields \(r=1/104<1/100=D\): **the sine-seeded niches disappear**, even though the source's lower-even-species numerical examples exhibit such patterns. This provides a concrete counterexample to an unconditional reading of Conjecture 2 in [1], not a claim about other initial data or all possible frozen-wave notions.

## Assumptions and scope

The state is a classical \(N\)-component solution on \(\mathbb R/L\mathbb Z\), indexed modulo \(N\), satisfying
\[
\partial_tu_i=D\partial_{xx}u_i+u_i(u_{i-1}-u_{i+1})-a u_i\bigl(C_N(u)-u_{i-1}\bigr),
\qquad C_N(u)=\sum_{j=1}^N u_j u_{j+1}.
\]
The source assumes \(-1<a\); here only \(-1<a<0\) is asserted. The initial components sum to one at every spatial point, lie in the probability simplex, and have the sine profile displayed above. Semilinear parabolic existence, maximum principles, and uniqueness give a unique bounded classical continuation for \(t>0\). No conclusion is asserted for odd \(N\), unequal species diffusion, different initial symmetries, or global stability in the unrestricted \(N\)-species phase space.

## Proof

**1. Exact invariant alternating reduction.** Write \(s_i=(-1)^{i-1}\) and set
\[
u_i(x,t)=\frac{1+s_i z(x,t)}N.
\]
Because \(N\) is even, the nearest neighbors both have sign \(-s_i\). Consequently
\[
C_N(u)=\frac{1-z^2}{N},\quad u_{i-1}-u_{i+1}=0,\quad
u_i\bigl(C_N(u)-u_{i-1}\bigr)=\frac{s_i z(1-z^2)}{N^2}.
\]
Substitution and uniqueness of the parabolic initial-value problem give precisely
\[
\boxed{z_t=D z_{xx}+r z(1-z^2),\qquad r=-a/N.}
\]
The scalar solution retains \(|z|\le1\) by comparison with the constant equilibria \(\pm1\), ensuring nonnegative species densities. Odd reflection about \(x=0\) and anti-periodicity \(z(x+L/2,t)=-z(x,t)\) are preserved by uniqueness. Therefore the restriction \(w=z|_{[0,\ell]}\) with \(\ell=L/2\) solves the scalar Allen–Cahn Dirichlet problem
\[
w_t=D w_{xx}+rw(1-w^2),\quad w(0,t)=w(\ell,t)=0,\quad w(x,0)=\sin(\pi x/\ell)>0
\]
for \(0<x<\ell\). The parabolic strong maximum principle gives \(0<w(x,t)<1\) for positive times and interior points.

**2. The exact diffusion threshold.** Let \(\lambda_1=(\pi/\ell)^2=\omega^2\) and \(Y(t)=\int_0^\ell w^2\,dx\). Integration by parts, Poincaré's inequality and Cauchy–Schwarz give
\[
\tfrac12 Y'=-D\!\int_0^\ell w_x^2+rY-r\!\int_0^\ell w^4
\le -(D\lambda_1-r)Y-\frac r\ell Y^2.
\]
For \(r<D\lambda_1\), \(Y\) decays exponentially. At \(r=D\lambda_1\), integration of \(Y'\le-2rY^2/\ell\) gives
\[
Y(t)\le\left[Y(0)^{-1}+\frac{2r}{\ell}t\right]^{-1}.
\]
Uniform parabolic smoothing upgrades convergence in \(L^2\) to uniform convergence. This includes the equality boundary, not just the strictly subcritical case.

**3. Existence, uniqueness and attraction of the patterned equilibrium.** Suppose \(r>D\lambda_1\). The positive Dirichlet stationary equation is
\[
D W''+rW(1-W^2)=0,\quad W(0)=W(\ell)=0,\quad W>0\text{ on }(0,\ell).
\]
Every positive solution has one maximum in \((0,1)\), is symmetric about \(\ell/2\), and is uniquely specified by its amplitude and energy first integral. The Jacobi identity
\[
\frac{d^2}{dy^2}\operatorname{sn}(y\mid m)=-(1+m)\operatorname{sn}(y\mid m)+2m\operatorname{sn}^3(y\mid m)
\]
shows that every positive Dirichlet solution has the displayed form, with its first two zeros separated by \(2K(m)/\kappa\). As \(m\) rises from zero to one, \(K(m)\sqrt{1+m}\) rises strictly from \(\pi/2\) to infinity. Thus exactly one \(m\in(0,1)\) obeys \(\ell=2K(m)/\kappa\), proving both the sharp existence condition and uniqueness of \(W\).

To prove convergence *for the stated initial state*, take \(\phi(x)=\sin(\pi x/\ell)\) and a sufficiently small \(\eta>0\) with \(r\eta^2\le r-D\lambda_1\). Then \(\eta\phi\) is a time-independent subsolution, initially below \(w\), so \(w(x,t)\ge\eta\phi(x)\). The Dirichlet Allen–Cahn energy
\[
\mathcal E(w)=\int_0^\ell\left[\frac D2w_x^2-\frac r2w^2+\frac r4w^4\right]dx
\]
satisfies \(d\mathcal E/dt=-\int_0^\ell w_t^2\,dx\). Uniform bounds and parabolic smoothing make positive-time trajectories precompact; every omega-limit point is a nonnegative stationary solution. The positive lower subsolution excludes zero, and uniqueness leaves only \(W\). Hence \(w(\cdot,t)\to W\), and the odd anti-periodic extension converges to \(Z\) on the full circle. Standard parabolic regularity also yields convergence in fixed finite spatial derivatives.

**4. Exact linear instability within the alternating subspace.** Along the nonconstant equilibrium \(Z\), the scalar periodic linearization is
\[
\mathcal L=D\partial_{xx}+r(1-3Z^2).
\]
Set \(y=\kappa x\), \(q=\sqrt{1-m+m^2}\), \(c=1+m-q\), and
\[
\psi(x)=1-c\operatorname{sn}^2(\kappa x\mid m).
\]
The identity \((\operatorname{sn}^2)''=2-4(1+m)\operatorname{sn}^2+6m\operatorname{sn}^4\) directly gives
\[
\mathcal L\psi=\lambda_+\psi,\qquad
\lambda_+=\frac r{1+m}\bigl(2q-(1+m)\bigr).
\]
Since \(q>m\), we have \(0<c<1\) and \(\psi>0\); moreover \(4q^2-(1+m)^2=3(1-m)^2>0\), hence \(\lambda_+>0\). The eigenfunction is periodic (its period divides \(L\)). The positive eigenvalue is the principal scalar periodic eigenvalue by one-dimensional positivity, and its alternating lift supplies a growing perturbation of the full system. This does not assert stability of patterns in any smaller reflection-antisymmetric, fixed-node subspace.

## Verification

The standalone `verification.py` contains only Python-standard-library dependencies. Run `python verification.py` in its extracted directory. It checks, with exact rational arithmetic, the replicated source reaction term against the invariant cubic reduction for many even sizes and rational amplitudes; the threshold comparison for the explicit large-even-species example; and the polynomial identities underlying the Jacobi stationary profile and positive Lamé eigenvalue. It also verifies representative elliptic-period monotonicity and eigenvalue positivity numerically using the arithmetic–geometric mean. These finite checks validate algebraic and normalization steps, **not** the infinite-dimensional convergence theorem, which is proved above using comparison, the energy identity and compactness.

Independent computational diagnostics also integrated the reduced periodic PDE with Fourier differentiation at \(N=8\) and \(N=52\), \(a=-1/2\) and \(D=0.03\) on a circumference \(2\pi\). The patterned case approached the elliptic profile to maximum absolute discrepancy less than \(2\times10^{-12}\); the homogenizing case had maximum amplitude below \(4\times10^{-5}\) at simulation time \(500\). Those numerical observations are supplementary, not proofs of the asymptotic claims.

## Relationship to prior work

Reference [1], Section 4.2 and Conjecture 2, numerically reports alternating, stationary-looking niches for biased even cycles with \(N=4,6,8\) and proposes analogous behavior at all even sizes. The new statement uses **exactly the source's reaction term and prescribed alternating sine initial profile**, derives a scalar invariant manifold, and provides an if-and-only-if species–diffusion cutoff. In particular its explicit \(N=52\) homogenization outcome distinguishes the theorem from the unconditional large-even-cycle conjecture. It does not refute the source's reported smaller cases or its broader observation of other stationary-looking states.

The scalar Allen–Cahn equation, its energy, metastability, Jacobi elliptic solutions and Lamé eigenfunctions are established mathematical tools, not claimed as new; see [2]–[4]. The mathematical claim here is the complete **source-specific** reduction, sharp parameter/species dichotomy for the source's initialized multi-species model, explicit standing-profile selection, and its exact instability eigenvalue. No claim of universal priority is made for generic Allen–Cahn statements.

## Limitations

The result treats equal diffusion, negative bias, even species number, and one specified smooth sine initial state. The nonconstant equilibrium is attracting within the fixed-node positive Dirichlet symmetry class, but is unstable in the larger periodic alternating class and hence in the full periodic multi-species system. Stationary-like transients or patterns with broken alternating species symmetry may behave differently. No theorem about open basins of attraction in the full unrestricted initial-condition space, traveling waves, higher spatial dimensions, or unequal diffusivities is asserted. The journal version of [1] was confirmed bibliographically but not compared line by line with its accessible arXiv version; equivalent specialized prior arguments outside the inspected sources remain possible. Independent scientific audit has not been performed.

## References

1. M. Visomirski and C. Griffin, *Coherent Structures and Travelling Waves in Spatial Replicators from a Biased Volterra Lattice*, arXiv:2601.06314v1, first posted 9 January 2026, especially equations (6), (21)–(23), Section 4.2, Conjecture 2, and Appendix A. https://arxiv.org/html/2601.06314v1 . Later journal appearance: *Chaos, Solitons & Fractals* **208** (2026), 118260, doi:10.1016/j.chaos.2026.118260.
2. M. G. Westdickenberg, *On the Metastability of the 1-d Allen–Cahn Equation*, *Journal of Dynamics and Differential Equations* **33** (2021), 1853–1879, doi:10.1007/s10884-020-09874-z. The generic scalar Allen–Cahn framework is prior art.
3. NIST Digital Library of Mathematical Functions, §§22.5 and 22.13, Jacobi functions, complete elliptic integrals and differential identities. https://dlmf.nist.gov/22.13 .
4. NIST Digital Library of Mathematical Functions, Chapter 29, Lamé functions and spectral equations. https://dlmf.nist.gov/29.1 .
