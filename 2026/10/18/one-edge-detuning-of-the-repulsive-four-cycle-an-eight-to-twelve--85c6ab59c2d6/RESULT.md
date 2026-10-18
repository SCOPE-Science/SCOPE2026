# One-edge detuning of the repulsive four-cycle: an eight-to-twelve Morse transition and sharp almost-global locking

## Finding
An arbitrarily small positive detuning of one edge of the repulsively coupled four-cycle eliminates its critical circles, but the **sign of detuning** changes the number of equilibria. For weights \((t,1,1,1)\), \(t>0\), \(t\ne1\), there are exactly eight isolated equilibria when \(0<t<1\) and exactly twelve when \(t>1\). All are Morse. Their numbers by Morse index \(0,1,2,3\) are respectively \((1,3,3,1)\) and \((1,5,5,1)\). At \(t>1\), the four additional equilibria occur in two index-one and two index-two configurations with explicit phase differences.

Let \(\Lambda_t=t+2+\sqrt{(t-1)^2+1}\). For every \(0<h<2/\Lambda_t\), every orbit of the discrete sine-coupled map converges to an equilibrium, and Lebesgue-almost every orbit converges to the unique alternating-antiphase equilibrium. The upper endpoint \(2/\Lambda_t\) is sharp for linear attraction of this equilibrium.

## Assumptions and scope
Orient the four edges of \(C_4\) cyclically. Let \(B\) be its \(4\times4\) oriented incidence matrix, with column \(i\) equal to \(e_i-e_{i-1}\), where indices are cyclic, and let \(W_t=\operatorname{diag}(t,1,1,1)\). The space of edge phase differences modulo simultaneous vertex rotations is the three-torus
\[
Z=\{z\in(\mathbb R/2\pi\mathbb Z)^4:\ z_1+z_2+z_3+z_4\equiv0\pmod{2\pi}\}.
\]
Define \(K=B^{\mathsf T}B\), the potential \(V_t(z)=t\cos z_1+\sum_{i=2}^4\cos z_i\), and the map
\[
F_{t,h}(z)=z+h K W_t\sin z\pmod{2\pi}, \qquad 0<h<2/\Lambda_t.
\]
This map is the Euler update of identical, reciprocally and repulsively sine-coupled oscillators with one variable positive edge weight; it preserves \(Z\). Morse indices are the number of negative eigenvalues of the Hessian of \(V_t|_Z\), and basin measure is normalized Haar (Lebesgue) measure on \(Z\). No statement is made at the excluded symmetry point \(t=1\) or the endpoint \(h=2/\Lambda_t\).

## Proof
**1. Stationarity and complete enumeration.** The critical points of \(V_t|_Z\) are exactly the configurations for which \(K W_t\sin z=0\): because \(K\) has kernel spanned by \((1,1,1,1)\), their condition is
\[
t\sin z_1=\sin z_2=\sin z_3=\sin z_4=:s.\tag{1}\]
This equality refers to the real phase-gradient vector. Every critical point is a fixed point of \(F_{t,h}\). Conversely, within the theorem's step range, the strict Lyapunov inequality (7) implies that any torus-map fixed point must be a critical point: a noncritical fixed point would force equality of potential values across a step. Thus the list below exhausts both critical points and all fixed points for \(0<h<2/\Lambda_t\), without a hidden winding loophole.

If \(s=0\), each \(z_i\) is \(0\) or \(\pi\), and closure requires an even number of \(\pi\)'s: exactly eight configurations.

Suppose \(s\ne0\). Take \(a\) with \(\sin a=s\). For each of \(z_2,z_3,z_4\), choose \(a\) or \(\pi-a\). If exactly \(k\) of these three coordinates are complemented, \(k\in\{0,1,2,3\}\), the closure relation gives \(z_1\equiv-(3-2k)a-k\pi\), and equation (1) becomes
\[
-t(-1)^k\sin((3-2k)a)=\sin a.\tag{2}\]
For \(k=1,2\), (2) says \((t-1)\sin a=0\), which is excluded. For \(k=0\) or \(3\), it reduces to \(-t\sin 3a=\sin a\). The two descriptions represent the same set because the choices \(a\) and \(\pi-a\) can be exchanged. By the triple-angle formula,
\[
\sin^2a=\frac{3t+1}{4t},\qquad
\cos^2a=\frac{t-1}{4t}.\tag{3}\]
No solutions exist for \(0<t<1\). For \(t>1\), precisely four values \(a\pmod{2\pi}\) satisfy (3), and their distinct solutions are \(z=(-3a,a,a,a)\pmod{2\pi}\). This proves the sharp \(8/12\) count of potential critical points.

**2. Nondegeneracy and Morse indices.** On the tangent hyperplane \(E=\{u\in\mathbb R^4:\sum_i u_i=0\}\), the Hessian quadratic form is
\[
Q_z(u)=-t\cos z_1\,u_1^2-\sum_{i=2}^4\cos z_i\,u_i^2.\tag{4}\]
At the all-zero critical point it is negative definite (index three), and at the all-\(\pi\) point it is positive definite (index zero). Each Boolean critical point with exactly two \(\pi\)-coordinates has positive and negative directions supported on the equal-sign pairs and is indefinite. Its constrained determinant in coordinates \(u_4=-u_1-u_2-u_3\) is nonzero and proportional to \(t-1\), as follows directly from the diagonal-plus-rank-one determinant formula; therefore it has index one or two. Since there are six such configurations, their index counts sum to three of each: directly, the four patterns with one of \(z_1,z_4\) equal to \(\pi\) split two/two, and the remaining two split one/one. Alternatively the Euler characteristic \(\chi(Z)=0\) and the involution \(z\mapsto z+(\pi,\pi,\pi,\pi)\) sends the Hessian to its negative, interchanging indices one and two. Hence the Boolean index census is \((1,3,3,1)\) on both sides of \(t=1\).

At a non-Boolean solution write \(c=\cos a\ne0\). Since \(\cos3a=(4c^2-3)c=-(2t+1)c/t\), (4) becomes
\[
Q_z(u)=c\left[(2t+1)u_1^2-u_2^2-u_3^2-u_4^2\right],\qquad u\in E.\tag{5}\]
For \(c>0\), (5) is negative definite on the two-dimensional subspace \(u_1=0\), and it is positive on \(u=(-3,1,1,1)\). Thus its Morse index is two. For \(c<0\), its index is one. There are two critical points in each case. Their potential values are \(V_t=(2-2t)c\), i.e. \(\pm (t-1)^{3/2}/\sqrt t\) (each twice). This completes the census and proves every critical point is Morse for \(t\ne1\).

**3. Exact spectral and step-size threshold.** The symmetric weighted Laplacian \(L_t=BW_tB^{\mathsf T}\) has eigenvalues
\[
0,\quad 2,\quad t+2-\sqrt{(t-1)^2+1},\quad t+2+\sqrt{(t-1)^2+1}.\tag{6}\]
The Hessian of the vertex-phase potential has operator norm at most \(\Lambda_t\), because \(|\cos z_i|\le1\). The standard smooth-gradient descent inequality on the vertex-phase quotient therefore gives
\[
V_t(F_{t,h}z)\le V_t(z)-h(1-h\Lambda_t/2)\|BW_t\sin z\|_2^2.\tag{7}\]
For \(0<h<2/\Lambda_t\), the right-hand correction is strictly negative outside critical points. The orbit stays in a compact torus, and its gradient norms tend to zero. Since the critical set is finite, the connectedness of the omega-limit set for an asymptotically regular orbit implies convergence to one critical point: indeed \(\|F(z)-z\|\to0\), every omega-limit point is critical, and a finite omega-limit set of asymptotically vanishing jumps is a singleton.

**4. Almost-everywhere selection, including noninvertible updates.** In vertex coordinates, the derivative at a critical point is \(I-h\nabla^2 V_t\) on the three-dimensional phase quotient. A non-minimal Morse critical point has at least one negative Hessian eigenvalue, hence an expanding multiplier \(1-h\mu>1\). Every positive Hessian eigenvalue is at most \(\Lambda_t\), so for the specified \(h\) its multiplier has absolute value below one. Therefore these equilibria are hyperbolic, with local stable manifolds of codimension at least one and hence zero Haar measure.

Even if the full map is not globally invertible, the global preimage of each such null local stable manifold is null. Indeed its Jacobian determinant is a real-analytic function of position and is not identically zero: at the all-zero point every transverse multiplier equals \(1+h\lambda_j>1\). Consequently its critical locus has measure zero; away from that locus the inverse function theorem gives countably many local inverse charts, on which preimages of null sets are null. Countably many iterated preimages cover all points converging to non-minima. It follows that almost every point converges to the only minimum, \(z_\star=(\pi,\pi,\pi,\pi)\). This argument proves the statement throughout the descent interval without assuming global invertibility.

At \(z_\star\), the three transverse multipliers are \(1-h\lambda_j\), with \(\lambda_j\) the three positive values in (6). Their moduli are strictly below one exactly when \(0<h<2/\Lambda_t\); for \(h>2/\Lambda_t\), at least one modulus exceeds one. Thus the interval is optimal for linear attraction of the alternating state. No nonlinear classification is asserted at equality.

## Verification
Running `python3 verify.py` in a Python environment with NumPy performs 1,852 finite diagnostic checks at nine weights on both sides of \(t=1\). Tests include the exact spectral formula, phase closure and stationary-flux conditions, the complete candidate counts and Hessian inertia, numerical Lyapunov inequalities, and local stability at a step close to the upper bound. All passed. The arbitrary-parameter assertions, completeness, almost-everywhere conclusion, and sharpness come from the preceding proof, not finite enumeration. Strict descent also excludes noncritical torus-update fixed points throughout the stated step interval; larger steps are outside the theorem.

## Relationship to prior work
Buescu, D'Aniello and Oliveira (2026, arXiv:2610.10993v1, published October 7) establish the weighted potential framework and descent criterion, but do not classify one-edge-weighted four-cycle critical points or their weight-dependent Morse indices. Buescu and Oliveira (arXiv:2610.19953, posted October 14) analyze *unit-weight* Huygens rings, including critical circles for the unweighted four-cycle and almost-global convergence, but not their detuning or the \(8/12\) transition.

Chen, Korchevskaia and Lindberg (arXiv:2210.00784) analyze algebraic solution bounds for Kuramoto graphs, obtaining the upper complex count twelve for a generic four-cycle. Lindberg, Zachariah, Boston and Lesieutre (arXiv:2010.03069) show that twelve real roots can occur for a four-cycle using a **negative** edge weight. Neither prior statement supplies the sharp classification when all weights are **positive** and three are normalized to one, the Morse-index distribution, or the a.e. discrete attraction interval. Those earlier root bounds and general descent mechanisms are prior results, not claimed as new.

## Limitations
The theorem concerns four identical oscillators with repulsive reciprocal sine coupling and one positive edge perturbation. It does not classify basins by volume, heteroclinic transversality, dynamics at \(t=1\), or the non-hyperbolic step endpoint. Outside the stated descent interval, the torus Euler update may have additional winding fixed points, which are not classified here. The result gives an almost-everywhere basin, not global attraction from every initial condition. A historically equivalent positive-weight four-cycle solution count may exist in power-flow or Kuramoto literature; bibliographic priority remains a risk. No independent scientific audit has been performed.

## References
1. Jorge Buescu, Emma D'Aniello and Henrique M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1 (first posted 2026-10-07). https://arxiv.org/abs/2610.10993
2. Jorge Buescu and Henrique M. Oliveira, *Almost-global convergence to twisted states in discrete Huygens rings*, arXiv:2610.19953 (first posted 2026-10-14). https://arxiv.org/abs/2610.19953
3. Tianran Chen, Evgeniia Korchevskaia and Julia Lindberg, *On the typical and atypical solutions to the Kuramoto equations*, arXiv:2210.00784 (first posted 2022-10-03). https://arxiv.org/abs/2210.00784
4. Julia Lindberg, Alisha Zachariah, Nigel Boston and Bernard C. Lesieutre, *The Distribution of the Number of Real Solutions to the Power Flow Equations*, arXiv:2010.03069 (first posted 2020-10-06). https://arxiv.org/abs/2010.03069
