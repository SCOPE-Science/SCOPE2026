# Exact coupling and anti-CFL stability for symmetric thermo-poroelastic splitting

## Finding
Consider the scalar equal-storage, equal-diffusion specialization of the fully decoupled semi-explicit scheme (5.4) of Altmann–Maier–Schmeck. Let \(0<c<1\), \(d\geq0\), \(b>0\), and \(t=hb>0\), with definitions below. Its complete homogeneous amplification map is Schur stable **if and only if**
\[
t>4d^2-2-2c.
\]
At equality with \(t>0\), an undamped eigenvalue \(-1\) is present; below it, an eigenvalue lies strictly below \(-1\). In particular, the method is Schur stable for **every** positive step size exactly when \(2d^2\leq1+c\). If \(2d^2>1+c\), smaller steps are unstable while steps satisfying \(hb>4d^2-2-2c\) are stable.

With the constant histories \(p^{-1}=p^0\), \(\theta^{-1}=\theta^0\), and consistent \(u^0=d(p^0+\theta^0)\), convergence on each fixed finite time interval is first order for all initial data precisely when \(2d^2\leq1+c\). If \(2d^2>1+c\), every initial datum with \(p^0+\theta^0\ne0\) produces an exponentially growing alternating mode as \(h\downarrow0\) at a fixed positive final time. The boundary \(2d^2=1+c\) is convergent despite a limiting parasitic root of \(-1\).

## Assumptions and scope
The normalized, unforced scalar thermo-poroelastic differential-algebraic system is
\[
 u=d(p+\theta),\qquad
 d\dot u+\dot p-c\dot\theta+bp=0,\qquad
 d\dot u+\dot\theta-c\dot p+b\theta=0.
\]
These are the operators \(A=1\), \(C=\widetilde C=1\), \(D=\widetilde D=d\), \(B=\widetilde B=b\), and \(\widehat C=c\) in (5.4) of the cited source. The continuous reduced mass matrix is
\[
 \begin{pmatrix}1+d^2&d^2-c\\ d^2-c&1+d^2\end{pmatrix},
\]
with eigenvalues \(1+2d^2-c>0\) and \(1+c>0\); thus the underlying continuous homogeneous problem is well posed and decays for the entire parameter domain.

The discrete step, after division by the positive diagonal operators, is
\[
\begin{aligned}
 u^{n+1}&=d(p^n+\theta^n),\\
 (1+t)p^{n+1}&=d(u^n-u^{n+1})+p^n+c\theta^n-c\theta^{n-1},\\
 (1+t)\theta^{n+1}&=d(u^n-u^{n+1})+\theta^n+cp^n-cp^{n-1}.
\end{aligned}
\]
Schur stability means spectral radius strictly below one for the map on \((u^n,p^n,\theta^n,p^{n-1},\theta^{n-1})\). Convergence refers only to this finite-dimensional scalar model with the stated constant histories; no spatial-grid or general PDE stability is asserted.

## Proof
Put \(s_n=(p^n+\theta^n)/2\), \(q_n=(p^n-\theta^n)/2\), and \(K=2d^2-c\). Because \(u^{n+1}=2ds_n\), eliminating the displacement after its one-step transient gives the two independent recurrences
\[
 (1+t)s_{n+1}=(1-K)s_n+Ks_{n-1},\qquad
 (1+t)q_{n+1}=(1-c)q_n+cq_{n-1}.
\]
The characteristic polynomial of the full five-state map factors as
\[
 z\,\frac{[(1+t)z^2-(1-K)z-K][(1+t)z^2-(1-c)z-c]}{(1+t)^2}.
\]
For a real monic quadratic \(z^2+a_1z+a_0\), both roots lie strictly in the unit disk exactly when \(1+a_1+a_0>0\), \(1-a_1+a_0>0\), and \(1-a_0>0\). For the symmetric factor these expressions, after multiplying by \(1+t\), are respectively \(t\), \(2+t-2K\), and \(1+t+K\). Since \(K>-1\), the first and third are positive. Thus this factor is Schur exactly when \(t>2K-2=4d^2-2-2c\). The antisymmetric factor has identical tests with \(K=c<1\), so it is Schur for every \(t>0\). At \(t=2K-2>0\) the symmetric polynomial vanishes at \(z=-1\); for smaller positive \(t\), the same polynomial is negative at \(z=-1\) and positive as \(z\to-\infty\), giving a root less than \(-1\). This proves the complete stability classification.

For the finite-time convergence claim, the exact continuous modes solve
\[
 \dot s=-\frac{b}{1+K}s,\qquad \dot q=-\frac{b}{1+c}q,
\]
and \(u=2ds\). Constant histories imply \(s_{-1}=s_0\) and \(q_{-1}=q_0\), hence each scalar recurrence has first value \(v_1=v_0/(1+t)\). If \(-1<K<1\), the two symmetric roots satisfy \(r_+(t)=1-t/(1+K)+O(t^2)\) and \(r_-(t)=-K+O(t)\). The coefficient of \(r_-^n\) in the constant-history solution is \(O(t)\); because \(|K|<1\), this gives \(O(h)\) global error uniformly for \(0\leq nh\leq T\). The antisymmetric recurrence has the same argument with \(K=c\). Since \(u^{n+1}=2ds_n\), displacement also has \(O(h)\) error.

At the exact boundary \(K=1\), the symmetric recurrence reduces to \((1+t)s_{n+1}=s_{n-1}\), so constant history gives the exact formula
\[
 s_n=s_0(1+t)^{-\lceil n/2\rceil}.
\]
This approximates \(s_0\exp(-bnh/2)\) uniformly with error \(O(h)\) on each fixed time interval; the other mode is still first order. For \(K>1\), the symmetric roots approach \(1\) and \(-K\) as \(t\downarrow0\). Solving from the two constant-history starting values gives a coefficient \(s_0Kt/(1+K)^2+O(t^2)\) on the latter root. With \(t=bh\) and \(n=\lfloor T/h\rfloor\), its magnitude grows as a positive multiple of \(h(K+o(1))^{T/h}\) whenever \(s_0\ne0\). This disproves finite-time convergence in that regime and establishes the stated if-and-only-if condition.

## Verification
The attached standalone `verify.py` constructs the exact five-state matrix, symbolically checks its characteristic factorization, compares six explicit parameter cases with the predicted boundary, checks 300 deterministic pseudorandom parameter points, and demonstrates the convergent interior/boundary and divergent supercritical cases for constant histories. The resulting actual output is included as `verify_output.txt`. The rigorous all-parameter result follows from the displayed factorization and quadratic Schur criterion, not from finite sampling.

For example, \(c=1/2\), \(d^2=3/5\), \(b>0\) lies strictly inside the unconditionally stable regime, whereas \(c=1/2\), \(d^2=1\) is unstable for \(0<hb<1\), has an eigenvalue \(-1\) at \(hb=1\), and is Schur stable for \(hb>1\).

## Relationship to prior work
Altmann, Maier and Schmeck (2026), Section 5.4, derive this fully decoupled three-field scheme and Theorem 5.4 provides a sufficient weak-coupling condition, supplemented by numerical sharpness diagrams in Section 6.4. In the present scalar normalization, their displayed sufficient bound becomes \(2d^2+c\leq1\), with the additional scalar inf-sup hypothesis \(d^2>c\). The exact result instead has the all-step boundary \(2d^2\leq1+c\). Thus for every \(c\in(0,1)\), the interval \(c<d^2\leq(1+c)/2\) is nonempty and stable; when \(c\geq1/3\), their two sufficient hypotheses cannot simultaneously hold anywhere in this interval. This is an exact analytical explanation of a stable region beyond those sufficient bounds, and additionally identifies the reversed step-size threshold when coupling is larger.

The 2021 Altmann–Maier work analyzes a two-field poroelastic split, without the present symmetric pressure–temperature cross coupling. Chen, Cui and Zhou (2025) study a different, stabilized sequential discontinuous Galerkin method for nonlinear thermo-poroelasticity, rather than the unstabilized recurrence (5.4). Their results are not implications of the exact five-state characteristic factorization proved here.

## Limitations
The result is confined to a scalar equal-storage/equal-diffusion, equal-mechanical-coupling specialization with zero forcing. General spatial discretizations, variable or nonsymmetric couplings, inhomogeneous forcing, nonlinear transport and other splitting algorithms are not covered. A standard quadratic Schur test is used; novelty concerns its sharp application to the cited scheme, not the test itself. The classification is based on the original 2026 preprint and related primary sources inspected below; a complete universal prior-art exclusion is not claimed.

## References
1. R. Altmann, R. Maier, J. Schmeck, *Semi-explicit time discretization for linear thermo-poroelasticity*, arXiv:2603.14149v1, first public 2026-03-14. Equation (5.4), Theorem 5.4, Section 6.4. https://arxiv.org/pdf/2603.14149
2. R. Altmann, R. Maier, *A decoupling and linearizing discretization for weakly coupled poroelasticity with nonlinear permeability*, arXiv:2104.10092, first public 2021-04-20. https://arxiv.org/abs/2104.10092
3. F. Chen, M. Cui, C. Zhou, *Sequential symmetric interior penalty discontinuous Galerkin method for fully coupled quasi-static thermo-poroelasticity problems*, arXiv:2509.06480, first public 2025-09-08. https://arxiv.org/abs/2509.06480
