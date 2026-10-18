# A sign-selective two-cycle obstruction for coupled node–group opinions

## Finding

Consider the finite-support node–group mean-field map (19) of Sampson, Restrepo, and Porter, generalized to two possibly distinct differentiable nondecreasing response functions. For **every** nonnegative joint hyperdegree law with positive dyadic and triadic means, every nondecreasing response pair, and **all** parameters \(a\ge0\), \(b\le0\), \(c\ge0\), \(d\ge0\), the map has **no nonconstant period-two orbit** anywhere in the order-parameter cube. At every point of that cube its Jacobian has **no strictly negative real eigenvalue**; in particular, a fixed point cannot undergo a flip (period-doubling) bifurcation through an eigenvalue \(-1\).

The sign condition is qualitatively material rather than a generic prohibition on oscillation: for \(b>0\), the same response family admits explicit *locally attracting* prime-two cycles, and these cycles persist in an open region with all four interaction parameters strictly positive.

## Assumptions and scope

Let \(P(k,q)\) be a finitely supported probability distribution on pairs of nonnegative integers. Define positive means \(\bar k=\sum P(k,q)k>0\), \(\bar q=\sum P(k,q)q>0\) and normalized degrees \(v_{kq}=k/\bar k\), \(u_{kq}=q/\bar q\). Let \(f,g:\mathbb R\to[0,1]\) be continuously differentiable and nondecreasing. Define \(F:[0,1]^3\to[0,1]^3\) by

\[
\begin{aligned}
F_V(V,U,Y)&=\sum_{k,q}P(k,q)v_{kq}f(av_{kq}V+bu_{kq}Y),\\
F_U(V,U,Y)&=\sum_{k,q}P(k,q)u_{kq}f(av_{kq}V+bu_{kq}Y),\\
F_Y(V,U,Y)&=Yg(cU+d)+(1-Y)g(cU).
\end{aligned}
\]

The sums defining the first two components are convex combinations because \(\sum Pv=\sum Pu=1\); the third component is also a convex combination. Thus the unit cube is invariant. The original model is the special case \(f=g=\tfrac12[1+\tanh(m(\cdot-\mu))]\), with its corresponding parameters. We consider the **deterministic mean-field map**, not the finite-size stochastic hypergraph model. There is no assumption about independence or correlation of \(k\) and \(q\).

## Proof

**1. A nonnegative weighted Gram determinant.** For arbitrary distinct candidate states \(X_0=(V_0,U_0,Y_0)\) and \(X_1=(V_1,U_1,Y_1)\), write \(\Delta V=V_1-V_0\), etc., and define

\[
s_{kq}=\int_0^1 f'\!\left(av_{kq}(V_0+t\Delta V)+bu_{kq}(Y_0+t\Delta Y)\right)dt\ge0.
\]

Set \(A=\sum Pv^2s_{kq}\), \(B=\sum Pvu s_{kq}\), \(C=\sum Pu^2s_{kq}\). The weighted Cauchy–Schwarz inequality yields \(A,C\ge0\) and \(AC-B^2\ge0\), also when some degrees or response slopes vanish.

**2. Global exclusion of primitive period two.** Assume \(F(X_0)=X_1\) and \(F(X_1)=X_0\). The fundamental theorem of calculus applied to the first two components gives

\[
(1+aA)\Delta V=-bB\Delta Y,\qquad
\Delta U=-aB\Delta V-bC\Delta Y.
\]

Eliminating \(\Delta V\) gives

\[
\Delta U=(-b)\frac{C+a(AC-B^2)}{1+aA}\,\Delta Y=K\Delta Y,\qquad K\ge0.
\]

For \(G(U,Y)=Yg(cU+d)+(1-Y)g(cU)\), every point of \([0,1]^2\) has \(\partial_U G=c[Yg'(cU+d)+(1-Y)g'(cU)]\ge0\), \(\partial_Y G=g(cU+d)-g(cU)\ge0\), using \(c,d\ge0\). Integrating its derivative along the segment joining the two states gives nonnegative secant coefficients \(E,H\) such that \(G(U_1,Y_1)-G(U_0,Y_0)=E\Delta U+H\Delta Y\). The period-two relation in the third component forces

\[
(1+H+EK)\Delta Y=0.
\]

Its coefficient is at least one, so \(\Delta Y=0\). The two preceding equations then imply \(\Delta V=\Delta U=0\), a contradiction. Consequently every orbit satisfying \(F^2(X)=X\) is a fixed point. This is a global statement for all admissible degree correlations and sigmoid steepnesses.

**3. No negative-real Jacobian eigenvalue.** At any \(X\in[0,1]^3\), redefine \(A,B,C\) with pointwise weights \(s_{kq}=f'(av_{kq}V+bu_{kq}Y)\), and take \(E=\partial_U G\), \(H=\partial_Y G\). Direct differentiation yields

\[
DF(X)=\begin{pmatrix}aA&0&bB\\aB&0&bC\\0&E&H\end{pmatrix}.
\]

For every real \(s>0\), expansion of the determinant gives

\[
\det(sI+DF)=s(s+aA)(s+H)+E(-b)\left[sC+a(AC-B^2)\right]>0.
\]

The strict inequality follows from the first term; all other summands are nonnegative. Thus \(DF\) cannot have any eigenvalue \(-s\) with \(s>0\). In particular \(-1\) is excluded throughout the physical cube. The claim does **not** preclude complex eigenvalues or longer-period/aperiodic dynamics.

**4. Attracting two-cycles with a sign reversal.** To see why the sign hypothesis matters, take \(P(1,1)=1\), \(a=d=0\), \(b=c=1\), and the original response \(f=g=h_m\) with

\[
h_m(z)=\tfrac12\left[1+\tanh\big(m(z-\tfrac12)\big)\right],\quad m>2.
\]

The map becomes \(F(V,U,Y)=(h_m(Y),h_m(Y),h_m(U))\). Because \(h_m(0)>0\), \(h_m(1/2)=1/2\), \(h_m'(1/2)=m/2>1\), and \(h_m\) is strictly convex on \((0,1/2)\), there is exactly one fixed point \(\ell\in(0,1/2)\); it crosses the diagonal downward, so \(r=h_m'(\ell)\in(0,1)\). Reflection symmetry gives another fixed point \(h=1-\ell\in(1/2,1)\) with the same derivative \(r\). Consequently the two distinct points

\[
X_0=(\ell,\ell,h),\qquad X_1=(h,h,\ell)
\]

satisfy \(F(X_0)=X_1\) and \(F(X_1)=X_0\). At each point \(DF=\begin{psmallmatrix}0&0&r\\0&0&r\\0&r&0\end{psmallmatrix}\); hence the eigenvalues of the two-step monodromy \(D(F^2)(X_0)\) are \(0,r^2,r^2\), all strictly inside the unit circle. This prime-two orbit is locally attracting. Since \(I-D(F^2)(X_0)\) is invertible and the orbit is hyperbolic, the implicit-function theorem continues it as a locally attracting prime-two orbit for sufficiently small simultaneous **positive** perturbations of \(a,d\) and nearby positive \(b,c\). Distinctness and interiority persist by continuity. Thus an open set with \(a,b,c,d>0\) supports an attracting two-cycle.

## Verification

The standalone `verify.py` uses only the Python 3 standard library. Its exact-rational portion generates 1,167 admissible weighted Gram examples and verifies \(AC-B^2\ge0\), the secant coefficient sign, and the expanded \(\det(sI+DF)\) identity at three positive \(s\) values per example. Its numerical portion constructs the two-cycle for eight values \(m\in\{2.01,2.1,2.5,3,4,6,10,20\}\) and runs three local perturbation checks each (24 total). All tests passed. They supplement the algebraic proof; no finite sampling establishes the theorem for all degrees and parameters.

Run: `python3 verify.py`.

## Relationship to prior work

Sampson, Restrepo, and Porter derive the same three-order-parameter mean-field map as equation (19), identify group–node disagreement states, and numerically study self-sustained oscillation and excitability. Their analyzed antagonistic group-to-node channel has negative \(b\), while their examples vary hyperdegree correlations. The new statement is **not** a consequence of an observed oscillator or a local stability diagram: it proves a correlation-independent global exclusion of primitive two-cycles and a pointwise spectral obstruction across the entire antagonistic sign cone. A separate constructive positive-feedback example shows that the excluded route can occur elsewhere in the model family. Golovin, Mölter, and Kuehn analyze stochastic adaptive-voter hypergraphs with different state-update and rewiring rules; Reynolds and Tudisco treat a continuous-time nonlinear-network opinion model, neither implying the synchronous three-variable Gram/secant result.

## Limitations

There is no general exclusion here of periods at least three, invariant circles, excitable transients, chaos, or stochastic-network oscillations. The sign hypothesis \(b\le0\) is essential to this proof, and the positive-feedback construction does not assert that all \(b>0\) choices oscillate or that a fixed-parameter bifurcation occurs at \(b=0\). The finite-support condition can be relaxed under integrability of the displayed derivatives, but that extension is not claimed. The locally attracting construction is a property of the mean-field reduction; when degrees are sparse, the reduction need not accurately approximate a finite stochastic hypergraph. Literature coverage cannot certify universal novelty.

## References

1. C. R. Sampson, J. G. Restrepo, and M. A. Porter, *Oscillatory and Excitable Dynamics in an Opinion Model with Group Opinions*, arXiv:2408.13336, first posted 23 August 2024; revised open full text https://arxiv.org/html/2408.13336v2; Phys. Rev. E 112, 024303 (2025), doi:10.1103/PhysRevE.112.024303.
2. A. Golovin, H. Mölter, and C. Kuehn, *Polyadic Opinion Formation: The Adaptive Voter Model on a Hypergraph*, arXiv:2308.03640, https://arxiv.org/html/2308.03640v2.
3. P. Reynolds and F. Tudisco, *Nonlinear opinion dynamics with unique Nash equilibrium*, arXiv:2303.07628, https://arxiv.org/abs/2303.07628.
