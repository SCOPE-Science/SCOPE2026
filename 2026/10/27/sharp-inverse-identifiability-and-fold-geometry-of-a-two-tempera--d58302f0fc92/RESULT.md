# Sharp inverse identifiability and fold geometry of a two-temperature harmonic Brownian gyrator

## Finding
Fix \(L>0\) and two distinct, known bath diffusivities \(T_1,T_2>0\). For the symmetric positive-definite harmonic trap
\[
K=\begin{pmatrix}a&c\\ c&b\end{pmatrix},\qquad a+b=L,
\]
consider the **mean potential torque** \(m\) and the **stationary probability-current angular frequency** \(\omega\), defined precisely below. Put \(\Delta=T_1-T_2\ne0\) and \(Q=T_1T_2>0\).

The complete feasible image for \(m\ne0\) consists exactly of the pairs satisfying
\[
m\omega<0,\qquad 0<|m|<|\Delta|,\qquad
0<|\omega|\le W_{\max}(m):=
\frac{L|m|}{2\sqrt{m^2+4Q}}
\sqrt{1-\frac{m^2}{\Delta^2}}.
\]
Each pair with strict last inequality determines **exactly two** distinct positive-definite matrices, whose diagonal entries are exchanged. Equality determines **exactly one**, with equal diagonal entries. For zero torque, the only possible angular frequency is zero and the inverse fibre is the entire one-parameter family \(K=\operatorname{diag}(a,L-a)\), \(0<a<L\). Every other pair is infeasible.

For nonzero \(m\) and feasible \(\omega\), the exact inverses are
\[
c=\frac{Lm}{2\Delta},\quad
P=\det K=\omega^2\left(1+\frac{4Q}{m^2}\right),\quad
\{a,b\}=\left\{\frac{L+d}{2},\frac{L-d}{2}\right\},\quad
d=\sqrt{L^2-4(P+c^2)}.
\]
The two diagonal branches have gap \(d\), with the exact **fold identity**
\[
d^2=4\left(1+\frac{4Q}{m^2}\right)
\bigl(W_{\max}(m)^2-\omega^2\bigr).
\]
At fixed nonzero \(m\), \(d\) therefore vanishes as the square root of the distance to the maximal-frequency boundary; the inverse has sharp one-half-Hölder, rather than Lipschitz, conditioning there.

A **single additional stationary scalar**,
\(V=\operatorname{Var}(X_1)-\operatorname{Var}(X_2)\), removes both the interior twofold ambiguity and the zero-torque continuum: the map \(K\mapsto(m,\omega,V)\) is injective on *all* positive-definite trace-\(L\) matrices. In the nonzero-torque case it recovers
\[
a-b=\frac{\Delta(L^2-4c^2)/L-2PV}{T_1+T_2}.
\]

## Assumptions and scope
Consider the Itô diffusion on \(\mathbb R^2\), in units of mobility one,
\[
dX_t=-KX_t\,dt+\sqrt{2D}\,dW_t,
\qquad D=\operatorname{diag}(T_1,T_2),\quad T_1\ne T_2>0,
\]
with \(K\) real symmetric positive definite and \(\operatorname{tr}K=L>0\) known. The normalized stationary law is \(N(0,\Sigma)\), with \(K\Sigma+\Sigma K=2D\); its stationary probability current is \(J(x)=(-Kx-D\nabla\log p(x))p(x)\). Let \(U(x)=x^{\mathsf T}Kx/2\). Define the torque on the *potential* as
\[
m=\mathbb E[X_1\partial_2 U(X)-X_2\partial_1 U(X)].
\]
(The torque of the potential force on the particle is \(-m\).) Define the current angular rate
\[
\omega=\int_{\mathbb R^2}\frac{x_1J_2(x)-x_2J_1(x)}{x_1^2+x_2^2}\,d^2x.
\]
The integrand is locally integrable. This is an ensemble current observable, not a claim of differentiable Brownian sample paths or of a noise-free individual angular velocity.

## Proof
Write \(P=ab-c^2>0\), \(S=T_1+T_2\) and \(\Delta=T_1-T_2\). The unique covariance \(\Sigma=(\sigma_{ij})\) solves
\[
a\sigma_{11}+c\sigma_{12}=T_1,\qquad
b\sigma_{22}+c\sigma_{12}=T_2,\qquad
L\sigma_{12}+c(\sigma_{11}+\sigma_{22})=0.
\]
Solving this system and combining the entries gives
\[
\sigma_{12}=-\frac{c(bT_1+aT_2)}{LP},\qquad
\det\Sigma=\frac{QL^2+c^2\Delta^2}{L^2P},
\]
\[
\sigma_{11}-\sigma_{22}
=\frac{\Delta(L^2-4c^2)}{2LP}-\frac{S(a-b)}{2P}.
\]
The potential-torque definition then implies
\[
m=c(\sigma_{11}-\sigma_{22})+(b-a)\sigma_{12}
=\frac{2c\Delta}{L}.
\]
Since \(D-K\Sigma\) is antisymmetric by the Lyapunov equation, it equals \(\begin{psmallmatrix}0&q\\-q&0\end{psmallmatrix}\) for \(q=c\Delta/L=m/2\). Therefore \(J(x)=(D-K\Sigma)\Sigma^{-1}xp(x)\). The local angular-current numerator is \(-q\,x^{\mathsf T}\Sigma^{-1}x\,p(x)\). In polar coordinates \(x=r e_\theta\), the radial integration is exact:
\[
\int_0^\infty (e_\theta^{\mathsf T}\Sigma^{-1}e_\theta)
\,p(r e_\theta)\,r\,dr
=\frac{1}{2\pi\sqrt{\det\Sigma}}.
\]
Integrating over \(\theta\) yields
\[
\omega=-\frac{q}{\sqrt{\det\Sigma}}
=-\frac{c\Delta\sqrt P}{\sqrt{QL^2+c^2\Delta^2}}
=-m\sqrt{\frac{P}{m^2+4Q}}.
\]
Consequently \(m=0\) if and only if \(c=0\), and in that case \(\omega=0\). For \(m\ne0\), the preceding equations invert uniquely to \(c=Lm/(2\Delta)\) and \(P=\omega^2(1+4Q/m^2)\). The necessary and sufficient condition that \(a,b\) be real and satisfy \(a>0,b>0,ab=P+c^2\) and \(a+b=L\) is
\[
0<P\le \frac{L^2}{4}-c^2,
\]
together with \(|c|<L/2\), and this is exactly the stated strict bounds on \(m\), sign of \(\omega\), and sharp upper bound \(W_{\max}(m)\). The quadratic roots \((L\pm d)/2\) are both strictly positive because \(P+c^2>0\), and provide all inverse matrices, proving both necessity and sufficiency and the exact fibre cardinalities. Substitution proves the fold identity, and Taylor expansion at \(|\omega|=W_{\max}(m)>0\) gives the sharp square-root exponent.

For nonzero \(m\), the displayed covariance-difference formula determines \(a-b\) uniquely from \(V\); the two branches differ in that observed variance by exactly \(-S d/P\ne0\) whenever \(d>0\). If \(m=0\), then \(c=0\) and \(V=T_1/a-T_2/(L-a)\). The derivative in \(a\) is \(-T_1/a^2-T_2/(L-a)^2<0\); the function maps \((0,L)\) continuously onto \(\mathbb R\). Thus \(V\) determines exactly one \(a\), proving global injectivity also on the zero-torque line. No regularity or inverse conclusion beyond this model is asserted.

## Verification
The standalone program `bg_inverse_checker.py` solves the full covariance Lyapunov equation independently of the displayed formulas, obtains angular circulation from numerical quadrature of the stationary current, and compares against the inversion formulas. A fixed-seed run checked 1,200 independent parameter samples, their two-branch reconstruction and variance discrimination, twelve boundary/interior tests, three infeasibility tests, and three zero-torque inversions. These are numerical cross-checks, not substitutes for the preceding analytical necessity-and-sufficiency proof. Reproduce with `python bg_inverse_checker.py` after installing NumPy and SciPy.

## Relationship to prior work
Filliger and Reimann (2007) derive the general stationary mean torque for a Brownian gyrator. Dotsenko and collaborators (2013) analyze Gaussian stationary currents for a two-temperature parabolic potential. Mancois and collaborators (2018), especially their overdamped Model B and Eq. (30), already give the **general forward angular-velocity formula** covering arbitrary positive-definite two-dimensional stiffness matrices after reparametrization. Neither the torque identity nor this forward angular-frequency identity is claimed to be new. The present result concerns the joint inverse image at *fixed trace and known bath temperatures*, including its complete feasibility frontier, exact fibre count, singular fold, and the minimal additional variance observable that resolves the ambiguity. No negative claim about inaccessible or unexamined specialized prior literature is inferred from search results.

## Limitations
The theorem assumes exactly known and unequal bath diffusivities, isotropic scalar mobility scaled to one, an exact stationary distribution, strictly positive-definite stiffness, and a known trace. The inverse square-root fold implies sensitivity near boundary, but the theorem supplies no statistical inference error bounds for finite trajectories. Nonequilibrium torque conventions must be respected; torque on the particle has the opposite sign. The angular-current statistic is an ensemble integral, not an instantaneous trajectory derivative. Historical priority of the complete inverse classification remains subject to independent specialist review, and no independent audit has been performed.

## References
1. R. Filliger and P. Reimann, *The Brownian gyrator: a minimal heat engine on the nano-scale* (2007), arXiv:0710.3735, https://arxiv.org/abs/0710.3735.
2. V. Dotsenko, A. Maciołek, O. Vasilyev, and G. Oshanin, *Two-temperature Langevin dynamics in a parabolic potential* (2013), arXiv:1302.4056, https://arxiv.org/abs/1302.4056.
3. V. Mancois, B. Marcos, P. Viot, and D. Wilkowski, *Two-temperature Brownian dynamics of a particle in a confining potential* (2018), arXiv:1802.04584, https://arxiv.org/abs/1802.04584; in particular §II.1.2, Eq. (30).
