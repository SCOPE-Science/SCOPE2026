# Universal cubic slowing at a doubly tangent predator-only threshold

## Finding
Consider the zero-delay specialization of the predator–prey system in Yao, Yang and Yuan [1]. At the simultaneous loss of the prey-invasion eigenvalue and its first nonlinear coefficient, the predator-only equilibrium is globally asymptotically stable for every strictly positive initial state, and prey extinction is algebraic rather than exponential:
\[
\lim_{t\to\infty}t x(t)^2=\frac{u}{2P},\qquad
\lim_{t\to\infty}\frac{y(t)-a}{x(t)}=n.
\]
This is a global critical result; it does not assert dynamics of the source system with nonzero delays.

## Assumptions and scope
Let \(a,n,k,b,d_1,d_2,s,r,q>0\). The equations, with both the fear and gestation delays set to zero, are
\[
\dot x=x\left(\frac{r}{1+ky}-d_1-d_2x-\frac{by}{1+qx}\right),\qquad
\dot y=sy\left(1-\frac{y}{a+nx}\right).
\]
In the source model \(b=m/(1+ck)\); every \(b>0\) here can be realized with positive capture rate \(m\) and protection parameter \(c\). Define \(u=1+ka\) and impose exactly
\[
r=u(d_1+ab),\qquad b(qa-n)=d_2+\frac{rkn}{u^2}.
\]
The first equality is precisely the zero prey-invasion eigenvalue at \(E=(0,a)\); the second annihilates the first derivative of the prey per-capita growth along the predator nullcline. Both equalities are compatible with strictly positive parameters, because \(r\) and then \(q\) can be chosen from them. Write
\[
P=d_1knq+d_2(uq+kn)+bkn^2>0,\qquad Q=d_2knq>0,
\quad \gamma=P/u.
\]
All global and asymptotic conclusions are for arbitrary finite \(x(0)>0\), \(y(0)>0\). The classification is primarily about global stability of an ordinary differential equation (MSC2020: 34D23).

## Proof
**1. Exact double-tangency identity.** At an interior equilibrium the predator equation forces \(y=a+nx\). Substitute into the prey per-capita growth and put
\[
G(x)=\frac{r}{u+knx}-d_1-d_2x-\frac{b(a+nx)}{1+qx}.
\]
Multiplying by the strictly positive denominator \((u+knx)(1+qx)\) and using *both* critical equalities gives the exact identity
\[
G(x)=-\frac{x^2(P+Qx)}{(u+knx)(1+qx)}<0\qquad(x>0).
\]
Consequently the system has no interior equilibrium. Its only equilibria in the nonnegative quadrant are \((0,0)\), \((0,a)\), and \(((r-d_1)/d_2,0)\); the third is positive in its first coordinate because \(r>d_1\).

**2. Global existence and invariant boundaries.** Positivity is preserved by the multiplicative factors \(x\) and \(y\). For positive solutions,
\[
\dot x\le x(r-d_1-d_2x).
\]
With \(M=\max\{x(0),(r-d_1)/d_2\}\), comparison yields \(0<x(t)\le M\). The predator equation is bounded above and below by logistic equations:
\[
sy(1-y/a)\le\dot y\le sy\left(1-\frac{y}{a+nM}\right).
\]
Thus the solution exists for every \(t\ge0\), is bounded, and satisfies \(\liminf_{t\to\infty}y(t)\ge a>0\).

**3. Global attraction.** The Jacobian at \(E=(0,a)\) has eigenvalues \(0\) and \(-s\). Step 4 proves that \(E\) is locally asymptotically stable. Let \(\omega\) denote the nonempty compact omega-limit set of any strictly positive solution. Its points all have \(y\ge a\). If \(\omega\) lay wholly in the open quadrant, it would contain no equilibrium and the planar Poincaré–Bendixson theorem would force a periodic orbit. A periodic orbit in the open quadrant is impossible: its Jordan interior stays in the open quadrant (which is convex), yet its index is one and hence it must enclose an equilibrium. If \(\omega\) meets \(x=0\), the full bounded orbit through that boundary point follows the scalar logistic equation \(\dot y=sy(1-y/a)\). A bounded complete boundary orbit constrained to \(y\ge a\) must be the equilibrium \(y=a\): every point \(y>a\) blows up in finite negative time. Therefore \(E\in\omega\). Because \(E\) is locally asymptotically stable, a forward orbit whose omega-limit contains \(E\) enters its attracting neighborhood and converges to \(E\). This proves global attraction for every strictly positive initial point.

**4. Critical center dynamics and exact rate.** Introduce the predator-nullcline discrepancy \(z=y-a-nx\). The origin in \((x,z)\) coordinates has one zero eigenvalue and one stable eigenvalue \(-s\); the strong-stable manifold coincides locally with the invariant line \(x=0\). A smooth center manifold \(z=h(x)\) exists. Its first nonzero term is cubic: using Step 1 and \(\dot z=-s z\,y/(a+nx)-n\dot x\) in the center-manifold invariance equation gives
\[
h(x)=\frac{n\gamma}{s}x^3+O(x^4),\qquad
\dot x=-\gamma x^3+O(x^4),\quad\gamma=P/u>0.
\]
(The quadratic term of \(h\) is zero because its invariance equation has coefficient \(-s\) at quadratic order.) The negative cubic and negative transverse eigenvalue establish local asymptotic stability of \(E\). Since the strong-stable manifold is exactly \(x=0\), each nearby trajectory with \(x>0\) tracks a positive center trajectory exponentially closely; none has the exceptional exponentially decaying center amplitude. Therefore along each globally converging strictly positive solution,
\[
\frac{d}{dt}\bigl(x(t)^{-2}\bigr)=2\gamma+o(1),
\]
which implies \(x(t)^{-2}/t\to2\gamma\), and hence \(t x(t)^2\to1/(2\gamma)=u/(2P)\). Exponential tracking and \(y=a+nx+h(x)\) on the center manifold also yield \((y-a)/x\to n\). This completes the proof.

## Verification
`checker.py` verifies the symbolic rational identity in Step 1, its leading coefficient, and an exact strictly positive parameter witness using SymPy. Run `python checker.py` with the dependency in `requirements.txt`. For
\[
(a,n,k,b,s,d_1,d_2,r,q)=(1,1,1,1,1,1,1,4,3),
\]
we have \(u=2\), \(P=11\), \(Q=3\),
\[
G(x)=-\frac{x^2(11+3x)}{(2+x)(1+3x)},\qquad
\lim_{t\to\infty}t x(t)^2=\frac1{11}.
\]
The sign, global omega-limit argument, stable-manifold exclusion and asymptotic integration are analytic arguments; finite calculations or symbolic simplification alone are not substitutes for these infinite-time steps.

## Relationship to prior work
Yao, Yang and Yuan [1], Section 3.1 and Theorem 3.2, analyze equilibrium existence and linear local stability of the model with two delays. Their predator-only characteristic equation is explicit and their proof treats the strict signs of the invasion eigenvalue; it does not resolve the zero-eigenvalue double-tangency case, global attraction, or its cubic decay coefficient. The statement in their theorem that the equilibrium is unstable "otherwise" is not supported by their proof at equality. Yu [2], Sections 1–3, studies global stability mainly of positive coexistence equilibria in a different fear-free modified Leslie–Gower system; its theorem is not a stronger statement about this critical predator-only state. Broad theoretical similarities to other nonhyperbolic systems do not imply this exact global classification or coefficient.

## Limitations
Only the zero-delay system is analyzed. With either positive delay, the planar omega-limit and center-manifold arguments in this form do not apply. The algebraic extinction law assumes both initial densities strictly positive; on the invariant boundary \(x=0\) the predator alone relaxes exponentially, while on \(y=0\) prey can approach a positive equilibrium. Parameter perturbations away from either exact tangency may have different equilibrium and relaxation behavior. No claim is made about all published or unpublished related work, about robustness under delays, or about independent mathematical certification.

## References
[1] S. Yao, J. Yang, S. Yuan, *Bifurcation analysis in a modified Leslie-Gower predator-prey model with fear effect and multiple delays*, Mathematical Biosciences and Engineering 21 (2024), 5658–5685. DOI: 10.3934/mbe.2024249. Publisher full text: https://www.aimspress.com/aimspress-data/mbe/2024/4/PDF/mbe-21-04-249.pdf (public release: 2024-04-19).

[2] S. Yu, *Global Asymptotic Stability of a Predator-Prey Model with Modified Leslie-Gower and Holling-Type II Schemes*, Discrete Dynamics in Nature and Society 2012, article 208167. DOI: 10.1155/2012/208167. Open full text: https://onlinelibrary.wiley.com/doi/10.1155/2012/208167.

[3] M. A. Aziz-Alaoui, M. Daher Okiye, *Boundedness and global stability for a predator-prey model with modified Leslie-Gower and Holling-type II schemes*, Applied Mathematics Letters 16 (2003), 1069–1075. DOI: 10.1016/S0893-9659(03)90096-6. The abstract was consulted; the full text was not used to establish a non-coverage claim.
