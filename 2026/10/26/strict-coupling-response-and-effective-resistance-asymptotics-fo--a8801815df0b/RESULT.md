# Strict coupling response and effective-resistance asymptotics for nonlinear opinion equilibria

## Finding

Let \(G\) be a finite, connected, undirected graph with at least two vertices, positive symmetric edge weights and weighted Laplacian \(L\). Fix \(p>0\), \(\sigma_i>0\), and \(u_i>0\). Consider the nonlinear opinion dynamics
\[
\dot x_i=-\kappa (Lx)_i+\sigma_i x_i(u_i-x_i^p),\qquad \kappa\ge0.
\]
For each coupling \(\kappa\), the system has exactly one strictly positive equilibrium \(x(\kappa)\). Its unscaled edge-disagreement energy is
\[
D(\kappa)=\frac12 x(\kappa)^\mathsf{T}Lx(\kappa)
=\frac12\sum_{\{i,j\}\in E}a_{ij}(x_i(\kappa)-x_j(\kappa))^2.
\]
The energy is continuously differentiable at \(0\), smooth for positive coupling, and **strictly decreasing for every finite \(\kappa\ge0\)** whenever the convictions \(u_i\) are not all equal. Define
\[
H_\kappa=\kappa L+\operatorname{diag}\big(\sigma_i((p+1)x_i(\kappa)^p-u_i)\big).
\]
Then \(H_\kappa\) is positive definite and
\[
\boxed{D'(\kappa)=-(Lx(\kappa))^\mathsf{T}H_\kappa^{-1}(Lx(\kappa))<0.}
\]
For uniform convictions, the equilibrium is constant and \(D\equiv0\). The initial slope is exact: letting \(d_i=u_i^{1/p}\),
\[
\boxed{D(0)=\tfrac12d^\mathsf TLd,\qquad D'(0)=-\sum_i\frac{((Ld)_i)^2}{p\sigma_i u_i}.}
\]
For strong coupling put
\[
\bar u_\sigma=\frac{\sum_i\sigma_i u_i}{\sum_i\sigma_i},\quad
c=\bar u_\sigma^{1/p},\quad v_i=\sigma_i(u_i-\bar u_\sigma).
\]
Then \(x(\kappa)\to c\mathbf1\), and with the Moore–Penrose inverse \(L^\dagger\),
\[
\boxed{\lim_{\kappa\to\infty}\kappa^2 D(\kappa)
=\frac{c^2}{2}v^\mathsf{T}L^\dagger v.}
\]
This coefficient is strictly positive for nonconstant \(u\). In particular, the decay exponent is exactly two, independent of graph size and the nonlinear exponent.

## Assumptions and scope

All graph weights \(a_{ij}=a_{ji}\) on existing edges are positive and finite, and the graph is connected. The Laplacian is \((Lx)_i=\sum_{j:\{i,j\}\in E}a_{ij}(x_i-x_j)\). Opinions, convictions and stubbornness are strictly positive real numbers. The exponent \(p\) is an arbitrary fixed positive real. The parameter \(\kappa\) multiplies *all* interaction weights uniformly; the observable \(D\) is computed with the unscaled Laplacian. For the displayed right derivative at \(\kappa=0\), differentiability is understood one-sided. Positive equilibria are considered; the all-zero equilibrium lies outside this domain. No assertion is made for heterogeneous edge-by-edge changes, directed graphs, zero stubbornness, or nonpositive convictions.

## Proof

**1. Positivity, existence and uniqueness.** Let \(f_i(s)=\sigma_i s(u_i-s^p)\). Consider, on \([0,\infty)^n\),
\[
\Phi_\kappa(x)=\tfrac\kappa2x^\mathsf TLx+
\sum_i\sigma_i\big(\tfrac{x_i^{p+2}}{p+2}-\tfrac{u_ix_i^2}{2}\big).
\]
The function is coercive and has a global minimizer. Along small positive constant vectors its value is negative, whereas at zero it vanishes; hence a minimizer is nonzero. If \(\kappa>0\), a nonzero minimizer with a zero coordinate has a zero coordinate adjacent to a positive coordinate by connectedness. Its directional derivative into that coordinate is strictly negative, a contradiction. Thus the minimizer is strictly positive and satisfies \(\kappa Lx=f(x)\). At \(\kappa=0\), the coordinatewise positive minimizer is explicitly \(d_i=u_i^{1/p}\).

To see uniqueness, suppose \(x,y>0\) solve the equilibrium equation and let \(r=\max_i x_i/y_i>1\), attained at \(i\). Then \(x_i=ry_i\), and the Laplacian comparison \((Lx)_i\ge r(Ly)_i\) holds because \(x_j\le r y_j\) at every neighbor. Yet \(f_i(x_i)=r\sigma_i y_i(u_i-r^p y_i^p)<r f_i(y_i)\). The two equilibrium equations contradict these inequalities. Applying the same reasoning with \(x,y\) exchanged rules out differing equilibria (if the maximum ratio is at most one in one direction, it is greater than one in the other whenever the vectors differ).

**2. Nondegenerate linearization.** The Jacobian of \(\kappa Lx-f(x)\) at its positive equilibrium is precisely \(H_\kappa\). The equilibrium identity \(H_\kappa x=(p\sigma_i x_i^{p+1})_i>0\) follows by subtracting \(f'_i(x_i)x_i\) from \(f_i(x_i)\). The symmetric matrix \(\operatorname{diag}(x)H_\kappa\operatorname{diag}(x)\) has nonpositive off-diagonal entries and each row sum equal to \(p\sigma_i x_i^{p+2}>0\). It is therefore strictly diagonally dominant with positive diagonal, hence positive definite; the same holds for \(H_\kappa\). The implicit-function theorem gives smooth dependence on \(\kappa\), including a smooth extension to a neighborhood of zero. This argument also supplies a constructive proof of the needed nonstandard nondegeneracy lemma.

**3. Strict dissipation under stronger coupling.** Differentiate the equilibrium equation with respect to \(\kappa\):
\[
H_\kappa x'(\kappa)=-Lx(\kappa).
\]
Since \(D'=x'^\mathsf TLx\), its substitution gives the negative quadratic form displayed above. Equality requires \(Lx=0\); connectedness then makes \(x\) constant, and equilibrium requires every \(u_i\) to be the same. When \(u\) is nonconstant, strict negativity follows at every finite coupling. At zero, \(H_0=\operatorname{diag}(p\sigma_i u_i)\) and \(x(0)=d\), giving the initial formulas.

**4. Strong-coupling expansion without formal series.** At a coordinate maximizing \(x\), \((Lx)_i\ge0\), so \(u_i-x_i^p\ge0\); at a minimizing coordinate the reversed inequality holds. It follows, uniformly in \(\kappa\), that
\[
\min_i u_i^{1/p}\le x_j(\kappa)\le\max_i u_i^{1/p}\quad\text{for every }j.
\]
The force vector \(f(x(\kappa))\) remains bounded. For \(\kappa>0\), \(Lx=f(x)/\kappa\), and applying \(L^\dagger\) yields
\[
x-\Big(\frac1n\sum_i x_i\Big)\mathbf1=\frac1\kappa L^\dagger f(x).
\]
Thus the disagreement between coordinates tends to zero. Summing all equilibrium equations gives \(\sum_i f_i(x)=0\). Every subsequential limit is consequently \(c\mathbf1\) with \(c>0\) and \(\sum_i\sigma_i(u_i-c^p)=0\), so the whole equilibrium vector converges to the stated \(c\mathbf1\). The identity
\[
D(\kappa)=\frac1{2\kappa^2}f(x(\kappa))^\mathsf TL^\dagger f(x(\kappa))
\]
follows exactly from \(Lx=f(x)/\kappa\) and \(f(x)\perp\mathbf1\); it is not a formal approximation. Letting \(\kappa\to\infty\) proves the limit. As \(\sum_i v_i=0\) and \(L^\dagger\) is positive definite on the orthogonal complement of constants, the limit coefficient is positive exactly when the convictions differ.

## Verification

The accompanying standard-library program `verify.py` checks an exact two-agent equilibrium, exact derivative and strong-coupling coefficient with rational arithmetic, then independently computes positive equilibria on 35 connected weighted random-graph settings and checks the monotonicity, sensitivity identity, both asymptotic regimes and equilibrium residuals. In its recorded run it passed 4,949 assertions. Those finite checks do not establish the quantified theorem: the proof above does.

A fully rational benchmark is a single unit-weight edge, \(p=\sigma_1=\sigma_2=\kappa=1\), and \((u_1,u_2)=(3/2,10/3)\). Then \(x=(2,3)\), \(D=1/2\), \(D'=-31/71\), and the strong-coupling coefficient is \(101761/41472\). To reproduce, use Python 3 and run `python verify.py` alongside this document; there are no external packages.

## Relationship to prior work

Reynolds and Tudisco, *Unique Nash equilibrium of a nonlinear model of opinion dynamics on networks with friction-inspired stubbornness* (arXiv:2304.07556, earliest version dated 2023-04-15), introduce the same nonlinear forcing and establish positive-equilibrium uniqueness, smoothness and convergence (their equation (15) and Theorem 1.2). Their potential, equation (57), is also the basis for a direct variational formulation. Those are prior results, not claimed here. The present result specifically concerns **uniform interaction-intensity comparative statics**, an exact strictly negative derivative, the sharp weak-coupling slope, and a network pseudoinverse coefficient for the large-coupling \(\kappa^{-2}\) law, which the inspected source does not state.

Sun and Zhang's *Opinion Optimization in Directed Social Networks* (arXiv:2306.16847) studies linear directed Friedkin–Johnsen optimization and does not establish these nonlinear equilibrium identities. Bhalla, Lechowicz and Musco's *Local Edge Dynamics and Opinion Polarization* (arXiv:2111.14020) concerns edge-changing linear opinion dynamics; its abstract was inspected, but full text was not accessible during comparison. General convex-optimization and graph-resistance techniques are background and could imply aspects under a suitable reformulation, which is a residual priority risk.

## Limitations

The theorem assumes uniform scaling of all positive undirected weights, strictly positive heterogeneous stubbornness and convictions, and selects the unique strictly positive equilibrium. It does not claim robustness to signed/directed edges, arbitrary simultaneous parameter changes, zero forcing coefficients, or arbitrary time-dependent networks. The parameter derivative is global but pertains to the *unscaled* disagreement energy; if interaction weights are themselves included in the reported energy, that is a different observable. Publication priority is not independently certified and the result does not imply that every individual pairwise opinion difference decreases monotonically.

## References

1. D. N. Reynolds and F. Tudisco, *Unique Nash equilibrium of a nonlinear model of opinion dynamics on networks with friction-inspired stubbornness*. arXiv:2304.07556, first public version 2023-04-15; published in *Nonlinearity* 38 (2025), 055027. https://arxiv.org/abs/2304.07556 .
2. Y. Sun and J. Zhang, *Opinion Optimization in Directed Social Networks*. arXiv:2306.16847 (2023). https://arxiv.org/abs/2306.16847 .
3. S. Bhalla, A. Lechowicz and C. Musco, *Local Edge Dynamics and Opinion Polarization*. arXiv:2111.14020 (2021). https://arxiv.org/abs/2111.14020 .
