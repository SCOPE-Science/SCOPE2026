# Sharp flip threshold and unique attracting two-cycle for scalar Soft Muon

## Finding

Consider the deterministic Soft Muon update of a scalar strongly convex quadratic, with positive curvature \(a\), learning rate \(\alpha\), soft-sign regularizer \(\varepsilon\), and normalized momentum \(0\le\beta<1\):
\[
H_{n+1}=\beta H_n+(1-\beta)a x_n,\qquad
x_{n+1}=x_n-\alpha\frac{H_{n+1}}{\sqrt{H_{n+1}^2+\varepsilon^2}}.
\]
Set
\[
 c=\frac{\alpha a}{\varepsilon},\quad
 t=\frac{1-\beta}{1+\beta},\quad
 c_*=\frac2t=\frac{2(1+\beta)}{1-\beta}.
\]
The origin in the position–momentum plane is the unique fixed point. It is locally exponentially asymptotically stable for \(0<c<c_*\), locally asymptotically stable (but nonexponentially) at \(c=c_*\), and unstable for \(c>c_*\). The exact critical learning rate is therefore
\[
 \alpha_* = \frac{2\varepsilon(1+\beta)}{a(1-\beta)}.
\]

**Complete prime-period-two classification.** A nonconstant period-two orbit exists if and only if \(c>c_*\). Exactly one such orbit exists as an unordered pair, and it is locally asymptotically attracting. In dimensionless variables \(z=ax/\varepsilon\) and \(w=H/\varepsilon\), its two states are
\[
 (z,w)=(Z,-tZ)\quad\text{and}\quad(-Z,tZ),\qquad
 Z=\frac1t\sqrt{\left(\frac{ct}{2}\right)^2-1}.
\]
Its physical position amplitude is
\[
 X=\frac{\varepsilon Z}{a}
 =\sqrt{\frac{\alpha^2}{4}-\frac{\varepsilon^2(1+\beta)^2}{a^2(1-\beta)^2}}.
\]
The positive cycle is born at the sharp square-root scale
\[
\lim_{c\downarrow c_*}\frac{Z}{\sqrt{c-c_*}}=\frac1{\sqrt t}.
\]
In particular, with \(\alpha,a,\beta\) fixed, its position amplitude approaches \(\alpha/2\) as \(\varepsilon\downarrow0\).

**Critical relaxation.** At \(c=c_*\), introduce the local center coordinate
\[
 u=z+\kappa(w+t z),\qquad
 \kappa=\frac{2\beta(1+\beta)}{(1-\beta)^2}.
\]
For every sufficiently small nonzero orbit lying on a local one-dimensional center manifold, the sharp critical rate is
\[
 \lim_{n\to\infty}\sqrt n\,|u_n|=\frac1{\sqrt{2t}}.
\]
Trajectories on the strong-stable manifold, if present, are excluded from this rate statement. The result does not assert global attraction or a classification of periods greater than two.

## Assumptions and scope

The objective is exactly \(f(x)=a x^2/2\) for \(a>0\), with exact real arithmetic, a constant \(\alpha>0\), a constant \(\varepsilon>0\), and normalized momentum parameter \(\beta\in[0,1)\). The state is \((x,H)\in\mathbb R^2\), and the recurrence is well defined from arbitrary initial state. Local stability is in the full two-dimensional state; period-two uniqueness means uniqueness up to reversing the two points. A prime period-two orbit has two *distinct* states. Its attraction concerns a neighborhood of those two points, not every initialization.

This is the analytical Soft Muon surrogate, not an exact description of the finite-degree Newton–Schulz polynomial used by a practical Muon implementation. The equivalence and distinction are explicitly specified in the motivating source's equations (6)–(8) and surrounding discussion.

## Proof

**1. Dimensionless map and equilibrium.** With \(z=ax/\varepsilon\), \(w=H/\varepsilon\), and \(g(s)=s/\sqrt{1+s^2}\), the map is
\[
 s=\beta w+(1-\beta)z,\qquad
 F_c(z,w)=(z-cg(s),s).
\]
A fixed point has \(w=s=z\), and \(cg(z)=0\) then gives \(z=w=0\). Direct differentiation gives, for all states,
\[
 DF_c(z,w)=\begin{pmatrix}
 1-d(1-\beta)&-d\beta\\
 1-\beta&\beta
 \end{pmatrix},\qquad
 d=c(1+s^2)^{-3/2}.
\]
The determinant is \(\beta\), and the trace is \(1+\beta-d(1-\beta)\). At the origin \(d=c\). The second-order real Schur/Jury conditions are precisely \(1-\beta>0\), \(c(1-\beta)>0\), and \(2(1+\beta)-c(1-\beta)>0\). Hence both eigenvalues lie strictly inside the unit circle exactly when \(0<c<c_*\). At \(c=c_*\), they are \(-1\) and \(-\beta\); at \(c>c_*\), one real eigenvalue lies below \(-1\), proving instability.

**2. Every prime two-cycle is symmetric.** Write a hypothetical cycle as \((z_1,w_1)\mapsto(z_2,w_2)\mapsto(z_1,w_1)\), and set \(m=(z_1+z_2)/2\), \(D=(z_1-z_2)/2\). Summing the two momentum relations shows \((w_1+w_2)/2=m\); subtracting them gives
\[
 w_1=m-tD,\qquad w_2=m+tD.
\]
The position updates are \(g(w_2)=2D/c\) and \(g(w_1)=-2D/c\). The function \(g\) is odd and strictly increasing; therefore \(w_1=-w_2\), hence \(m=0\). For a prime cycle \(D\ne0\), so the two states must be \((D,-tD)\) and \((-D,tD)\), with
\[
 2D=c\,\frac{tD}{\sqrt{1+t^2D^2}}.
\]
The only positive solution is \(D=Z\) displayed above, and it exists exactly when \(ct/2>1\). The negative choice merely interchanges the two cycle points. This proves existence, uniqueness, and nonexistence at/below the threshold without assuming symmetry in advance.

**3. Attraction of the unique cycle.** At either point of the period-two orbit the intermediate momentum has magnitude \(tZ\). Thus both one-step Jacobians are identical to the matrix in step 1 with the effective coefficient
\[
 d_\mathrm{cyc}=
 \frac{c}{(1+t^2Z^2)^{3/2}}
 =\frac{8}{c^2t^3}.
\]
Since \(c>2/t\), we have \(0<d_\mathrm{cyc}<2/t=c_*\). Applying the same strict Schur inequalities to this Jacobian proves that both its eigenvalues have modulus strictly below one. The monodromy Jacobian is its square, hence both Floquet multipliers also have modulus strictly below one. Consequently the cycle is locally asymptotically attracting. Expanding the exact expression for \(Z\) at \(c=c_*\) proves the square-root onset, while direct substitution proves the physical amplitude formula and the vanishing-regularizer limit.

**4. Exact critical cubic and rate.** At \(c=2/t\) define
\[
 v=w+t z,\qquad u=z+\kappa v,
 \quad\kappa=\frac{2\beta(1+\beta)}{(1-\beta)^2}.
\]
This invertible linear coordinate change has \(z=u-\kappa v\), \(w=-t u+v/t\). The intermediate momentum is \(s=t u-\beta v/t\). The map's linear part in these coordinates is diagonal \((-1,-\beta)\). The expansion
\[
 g(s)=s-\frac{s^3}{2}+O(s^5)
\]
gives the exact local form
\[
 u^+=-u+\frac{s^3}{t^2}+O(s^5),\qquad
 v^+=-\beta v+s^3+O(s^5).
\]
A local one-dimensional center manifold is a graph \(v=q(u)=O(u^3)\). On that graph,
\[
 u^+=-u+t u^3+O(u^4).
\]
Because \(t>0\), sufficiently small nonzero center-manifold orbits move toward zero with alternating sign; moreover
\[
 \frac1{(u^+)^2}-\frac1{u^2}=2t+o(1).
\]
Summing this identity along the orbit yields \(u_n^{-2}/n\to2t\), proving the claimed rate. The other eigenvalue is \(-\beta\) with modulus below one, so the center-manifold stability theorem implies local asymptotic stability of the full two-dimensional fixed point at the threshold. No claim about global basins follows from this local argument.

## Verification

The standalone `verify.py` uses only the Python standard library. Running `python verify.py` checks 63 parameter configurations across seven momentum values; 3,000 finite-difference Jacobian comparisons; the determinant identity; seven center-cubic algebra configurations; four critical-rate experiments of 40,000 steps each; and the exact explicit cycle with \(\beta=1/2\) and \(c=8\). All tests passed. Finite comparisons are checks of the calculations, not substitutes for the proofs of statements quantified over all parameters.

For \(\beta=1/2\), \(a=1\), \(\varepsilon=0.1\), and \(\alpha=0.8\), the critical learning rate is \(0.6\), and the attracting cycle has dimensionless positions \(\pm\sqrt7\), physical positions \(\pm0.1\sqrt7\), and matching momenta \(\mp0.1\sqrt7/3\). Higher-period behavior at other parameter values is outside the present classification.

## Relationship to prior work

De Oliveira, Jatkar, Vicinansa, and Sontag (arXiv:2609.30546v1, equations (6)–(8), Section 3, and Appendix A) define the precise soft-sign iteration and establish convergence at sufficiently small steps under more general assumptions; their reported simulations display a regularization-dependent switch between oscillation and convergence. Those sufficient convergence theorems do not supply the sharp full-momentum local threshold or a complete enumeration and stability proof of all prime two-cycles on the quadratic.

Mustafi, Mukherjee, and Sriperumbudur (arXiv:2605.23871v1) provide a related regularized orthogonalization formulation and small-step discrete-time convergence theory in a broader Hamiltonian framework, not the exact fixed-step two-cycle law. Gonon, Muşat, and Boumal (arXiv:2602.11948v1) study quadratics chiefly with exact or approximate polar steps and grid confinement; this does not imply the soft-sign two-dimensional classification. Oikonomidis, Quan, and Patrinos (arXiv:2510.11312v1) study other nonlinear preconditioners and heavy-ball-type methods with sufficient convergence results.

Published scalar Signum calculations classify a continuum of neutral cycles for a **discontinuous** hard-sign map. That result does not imply the **unique hyperbolically attracting** cycle obtained here for every strictly positive soft-sign regularizer. Likewise, exact flip analyses for a fourth-root Polar Express surrogate and for momentum SAM concern distinct update laws and do not cover this map.

## Limitations

The local stability result is not a global-convergence theorem. Only prime periods one and two are classified; higher-period orbits and their basins are unaddressed, and numerical experiments suggest such behavior can occur for some choices of parameters. The precise critical \(n^{-1/2}\) constant is asserted for nontrivial orbits on a local center manifold, not for arbitrary faraway initial data or strong-stable exceptional orbits. The complete theorem concerns noiseless scalar quadratic dynamics and the analytical soft-sign update, not general functions, stochastic gradients, matrix-size effects, or practical finite-degree Newton–Schulz Muon. Claims of historical priority remain subject to independent literature confirmation.

## References

1. A. C. B. de Oliveira, D. D. Jatkar, G. S. Vicinansa, and E. D. Sontag, *Convergence guarantees for Muon: New parameter regimes and generalizations*, arXiv:2609.30546v1 (24 September 2026), https://arxiv.org/abs/2609.30546.
2. A. Mustafi, S. Mukherjee, and B. K. Sriperumbudur, *Move on Muon: A Hamiltonian probability gradient flow perspective of Muon optimizer*, arXiv:2605.23871v1 (22 May 2026), https://arxiv.org/abs/2605.23871.
3. A. Gonon, A.-A. Muşat, and N. Boumal, *Insights on Muon from Simple Quadratics*, arXiv:2602.11948v1 (12 February 2026), https://arxiv.org/abs/2602.11948.
4. K. Oikonomidis, J. Quan, and P. Patrinos, *Nonlinearly Preconditioned Gradient Methods: Momentum and Stochastic Analysis*, arXiv:2510.11312v1 (13 October 2025), https://arxiv.org/abs/2510.11312.
5. *Exact continuum of neutral two-cycles for scalar Signum*, publicly accessible result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-continuum-of-neutral-two-cycles-for-scalar-signum--5eb1801a903e.
6. *A sharp flip frontier for the Polar-Express surrogate on scalar quadratics*, publicly accessible result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-sharp-flip-frontier-for-the-polar-express-surrogate-on-scalar--5f6e926df82f.
