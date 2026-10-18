# Sharp parameter-uniform oscillation cutoff in a weak-Allee liquidity–profit flow

## Finding
For the positive-quadrant dynamics
\[
\dot x=\frac{x^2}{x+M}-xy,\qquad
\dot y=r y\left(1-\frac{y}{x}\right),\qquad M>0,\quad r>0,
\]
**no nonconstant periodic orbit entirely in the open positive quadrant exists whenever \(r\ge1/4\)**, for *any* \(M>0\). This uniform threshold is optimal: when \(M=1/2\), a nondegenerate supercritical Hopf point at \(r=1/4\) produces a small attracting positive cycle for every sufficiently close \(r<1/4\). The statement concerns periodic orbits, not stability of every trajectory.

## Assumptions and scope
The vector field is smooth on \(\mathcal Q=\{(x,y):x>0,\ y>0\}\). A periodic orbit means a nonconstant classical solution whose image is a compact closed curve inside \(\mathcal Q\); all times use the time variable as printed in the differential equations. Parameters satisfy \(M>0\) and \(r>0\). The sharpness example uses the genuine weak-Allee coexistence range \(0<M<1\). There is no assumption about convergence or absorbing sets outside the periodic orbit.

## Proof
**Global exclusion.** Write \(f(x)=x/(x+M)\), so \(\dot x=x(f(x)-y)\). On \(\mathcal Q\), take the positive smooth Dulac weight \(D(x,y)=1/(xy^2)\). The weighted vector-field divergence is exactly
\[
\partial_x(D\dot x)+\partial_y(D\dot y)
=\frac{f'(x)}{y^2}-\frac{r}{xy^2}
=\frac{\frac{Mx}{(x+M)^2}-r}{xy^2}.
\]
The identity \((x+M)^2-4Mx=(x-M)^2\ge0\) gives \(Mx/(x+M)^2\le1/4\) for every \(x>0\), equality only at \(x=M\). Thus for \(r\ge1/4\) the weighted divergence is nonpositive everywhere in \(\mathcal Q\) and strictly negative off the vertical line \(x=M\), which has zero planar measure. Every nonempty open region in \(\mathcal Q\) has strictly negative divergence integral. A purported periodic orbit is a smooth simple closed curve bounding a domain lying inside the convex set \(\mathcal Q\). Along this boundary the weighted vector field is tangent, so its outward flux is zero. Green's theorem would make that flux equal to the strictly negative integral of the divergence over the bounded domain, a contradiction. This includes the equality case \(r=1/4\).

**Sharpness through a genuinely positive Hopf cycle.** Fix \(M=1/2\). The positive equilibrium for all nearby rates is \(E=(1/2,1/2)\). Its Jacobian at \(r=1/4\) is
\[
A=\begin{pmatrix}1/4&-1/2\\1/4&-1/4\end{pmatrix},\qquad
\operatorname{spec}(A)=\{i/4,-i/4\}.
\]
At the same equilibrium for variable \(r\), the trace is \(1/4-r\), and the determinant at the critical point is \(1/16>0\). Thus the real part of each eigenvalue crosses zero with derivative \(-1/2\) as \(r\) increases.

For transparency, the following standard complex-eigenvector normalization is used for the first Lyapunov coefficient. Define \(q=(1,(1-i)/2)^\mathsf T\), \(p=((1+i)/2,-i)^\mathsf T\), so \(Aq=(i/4)q\), \(A^\mathsf Tp=(-i/4)p\), and \(\langle p,q\rangle=\bar p^\mathsf Tq=1\). Expand the smooth field at \(E\) as
\[
\dot u=Au+\tfrac12 B(u,u)+\tfrac16 C(u,u,u)+O(\|u\|^4),
\]
where \(B\) and \(C\) are the second and third derivative multilinear forms. Direct differentiation and exact complex arithmetic give
\[
\begin{aligned}
G_{21}&=\langle p, C(q,q,\bar q)-2B(q,A^{-1}B(q,\bar q))\\
&\qquad\quad + B(\bar q,(2i\omega I-A)^{-1}B(q,q))\rangle
=-\tfrac14-\tfrac5{12}i,\qquad \omega=\tfrac14.
\end{aligned}
\]
Therefore the first Lyapunov coefficient in this eigenvector convention is \(\ell_1=\operatorname{Re}(G_{21})/(2\omega)=-1/2<0\). (Its magnitude depends on the eigenvector/amplitude convention; its sign does not.) The Hopf theorem supplies a unique nearby small stable cycle on the side where the equilibrium is unstable, namely \(r<1/4\) sufficiently close to criticality. Since the cycle shrinks to \(E\) and \(E\) lies strictly within \(\mathcal Q\), these cycles are positive. Hence no smaller parameter-uniform upper cutoff could exclude cycles for all \(M\).

## Verification
The included `verification/check.py` recomputes the exact weighted-divergence identity, nonnegative-square bound, critical linear eigenvectors, adjoint normalization, the complex multilinear coefficient \(G_{21}\), and transversality using SymPy. Run `python verification/check.py` from the extracted package; the only external Python dependency is listed in `requirements.txt`. This symbolic check supports the explicitly proved algebra; it does not substitute finite simulation for the global Bendixson–Dulac argument or the Hopf theorem.

## Relationship to prior work
Demetrian and Zimka (2026), Eq. (5.1) and Theorem 5.1, introduce and analyze this weak-Allee liquidity–profit subsystem, proving the existence of a local supercritical Hopf bifurcation at \(r=M(1-M)\) for \(0<M<1\). That local conclusion does **not** by itself exclude large-amplitude cycles at larger \(r\), nor establish an \(M\)-uniform global no-cycle bound including equality. The present result supplies that exclusion with a constructive sharpness witness. The Bendixson–Dulac theorem and classical first-Lyapunov formula are standard tools rather than newly claimed general theorems.

Zhang and Yan (2017) prove general nonexistence criteria for a Leslie–Gower predator–prey family via a generalized Dulac argument; their full text was unavailable for a direct coefficient-level comparison, so possible subsumption by that work remains an explicit novelty risk. González-Olivares, Rojas-Palma, and González-Yañez (2017) analyze multiple cycles in a **different** weak-Allee Leslie–Gower-type predator–prey vector field. The fact that both involve weak Allee effects does not establish an implication between their theorems and this precise \(1/4\) boundary.

## Limitations
Only the exact smooth two-dimensional model above is covered. No assertion is made about global attraction, coexistence persistence, invariant sets touching a singular boundary, other functional responses, delayed/stochastic versions, or a full bifurcation diagram. The universal constant is sharp among parameter-uniform cutoffs, not necessarily the best condition for every fixed \(M\). A full-text comparison with the broader 2017 generalized-Dulac criterion could affect originality.

## References
1. M. Demetrian and R. Zimka, *Aggregate models of liquidity-profit dynamics*, arXiv:2607.19422v1 (first posted July 20, 2026), Section 5, equation (5.1), Theorem 5.1. https://arxiv.org/abs/2607.19422
2. D. Zhang and P. Yan, *Necessary and sufficient conditions for the nonexistence of limit cycles of Leslie–Gower predator–prey models*, Applied Mathematics Letters **71** (2017), 1–5. https://doi.org/10.1016/j.aml.2017.03.008
3. E. González-Olivares, A. Rojas-Palma and B. González-Yañez, *Multiple limit cycles in a Leslie–Gower-type predator–prey model considering weak Allee effect on prey*, Nonlinear Analysis: Modelling and Control **22** (2017), 347–365. https://doi.org/10.15388/NA.2017.3.5
4. Bendixson–Dulac exclusion theorem and standard nondegenerate Hopf bifurcation theorem (classical methods).
