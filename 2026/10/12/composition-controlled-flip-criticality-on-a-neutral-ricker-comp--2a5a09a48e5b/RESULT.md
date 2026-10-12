# Composition-controlled flip criticality on a neutral Ricker competition foliation

## Finding

**Theorem (neutral two-species Ricker dynamics).** Fix real parameters \(\alpha>1\) and \(2<R<2\alpha\). On the strictly positive quadrant consider the discrete-generation competition map
\[
T(x,y)=\left(x\exp(R-x-\alpha y),\quad y\exp((R-x-\alpha y)/\alpha)\right).
\]
This is the classical two-species Ricker competition map with reciprocal interaction coefficients \(\beta=1/\alpha\) and proportional log-growth rates \(S=R/\alpha\). For every initial state \(x,y>0\), the composition quantity \(K=x/y^{\alpha}\) is exactly invariant. For every \(K>0\), the invariant leaf \(x=Ky^{\alpha}\) has exactly one positive equilibrium \(y=y_K\), characterized by \(Ky_K^{\alpha}+\alpha y_K=R\). These equilibria fill the entire positive segment \(x+\alpha y=R\).

Put
\[
y_c=\frac{R-2}{\alpha-1},\qquad x_c=\frac{2\alpha-R}{\alpha-1},\qquad
K_c=\frac{x_c}{y_c^{\alpha}}.
\]
For \(0<K<K_c\) the equilibrium is locally attracting *within its invariant leaf*. For \(K>K_c\) it is leafwise repelling, and **for every such \(K\) there exists at least one nonconstant strictly positive period-two orbit on that leaf**. At \(K=K_c\) the planar equilibrium has multipliers \(1,-1\); thus these assertions do not amount to asymptotic attraction of a point or a cycle in the full plane.

The leafwise flip at \(K=K_c\) changes criticality at a sharp competition-strength boundary. Set \(t=2\alpha-R\), so \(0<t<2(\alpha-1)\), and
\[
Q(\alpha,t)=3t^2+2(5-\alpha)t+8.
\]
If \(Q>0\), a leafwise attracting period-two orbit is born on the \(K>K_c\) side (supercritical flip). If \(Q<0\), a leafwise repelling period-two orbit is present on the \(K<K_c\) side and disappears at \(K_c\) (subcritical flip). These statements are local in \(K\); they assert no full-plane asymptotic stability. The inequality \(Q<0\) is attainable under the stated assumptions **if and only if**
\[
\alpha>5+2\sqrt 6.
\]
For such \(\alpha\), the subcritical range is exactly
\[
\frac{\alpha-5-\sqrt{(\alpha-5)^2-24}}3
<t<
\frac{\alpha-5+\sqrt{(\alpha-5)^2-24}}3.
\]
At \(Q=0\) the cubic flip test is degenerate; no higher-order flip type is asserted.

## Assumptions and scope

The state is a pair of **strictly positive** population abundances, time is discrete, all exponents and powers have their usual real values, and \(\alpha,R\) satisfy the strict inequalities above. Species grow according to the same density-dependent resource \(x+\alpha y\), with the second species experiencing exactly \(1/\alpha\) of the first species' logarithmic growth increment. In the standard parametrization \(x^+=rxe^{-x-\alpha y}\), \(y^+=sye^{-y-\beta x}\), this corresponds to \(r=e^R\), \(s=e^{R/\alpha}\), \(\beta=1/\alpha\). The result does not cover arbitrary growth-rate mismatch or \(\alpha\beta\ne1\).

A period-two orbit is an unordered pair of distinct positive states interchanged by one application of \(T\). “Leafwise attraction” means local asymptotic stability for the one-dimensional restriction with fixed positive \(K\). Every planar equilibrium has a neutral multiplier \(1\), because it belongs to a smooth curve of equilibria.

## Proof

**1. Exact foliation and equilibria.** Write \(H=R-x-\alpha y\). Direct substitution gives
\[
\frac{x^+}{(y^+)^{\alpha}}
=\frac{x e^H}{y^{\alpha}e^H}
=\frac{x}{y^{\alpha}}.
\]
Fixing \(K=x/y^{\alpha}>0\) yields the scalar leaf map
\[
f_K(y)=y\exp\!\left(\frac{R-Ky^{\alpha}-\alpha y}{\alpha}\right),\qquad y>0.
\]
The exponent vanishes exactly when \(Ky^{\alpha}+\alpha y=R\); its left-hand side is strictly increasing from zero to infinity, so the positive root \(y_K\) is unique. Every positive fixed point of \(T\) must have \(H=0\), and conversely every point \(x+\alpha y=R\), \(x,y>0\), is fixed. Thus \(K\) parameterizes the full equilibrium segment without overlap.

**2. Sharp leafwise stability threshold.** Differentiating at the leaf equilibrium gives
\[
\lambda(K)=f_K'(y_K)=1-Ky_K^{\alpha}-y_K
=1-R+(\alpha-1)y_K.
\]
The implicit function theorem yields
\[
\frac{dy_K}{dK}=-\frac{y_K^{\alpha}}{\alpha(1+K y_K^{\alpha-1})}<0.
\]
Consequently \(\lambda(K)\) is strictly decreasing, from the limit \(1-R/\alpha\) as \(K\downarrow0\) to \(1-R\) as \(K\to\infty\). The chosen strict range \(2<R<2\alpha\) puts these limits on opposite sides of \(-1\), while \(\lambda(K)<1\) throughout. The unique crossing \(\lambda=-1\) requires \(x_K+y_K=2\); solving this alongside \(x_K+\alpha y_K=R\) gives precisely \((x_c,y_c,K_c)\) above. At the crossing,
\[
\lambda'(K_c)=-\frac{(\alpha-1)y_c^{\alpha+1}}{2\alpha}<0.
\]
For \(K<K_c\), \(-1<\lambda<1\) and the scalar fixed point is locally attracting; for \(K>K_c\), \(\lambda<-1\) and it is locally repelling. The full Jacobian at an equilibrium is
\[
DT=\begin{pmatrix}1-x&-\alpha x\\-y/\alpha&1-y\end{pmatrix},
\]
whose eigenvalues are \(1\) and \(1-x-y=\lambda\), consistent with the invariant family.

**3. A positive two-cycle on every leaf beyond the flip.** For \(K>K_c\) let \(h(y)=f_K(f_K(y))-y\). Since \(f_K(y)/y\to e^{R/\alpha}>1\) and \(f_K^2(y)/y\to e^{2R/\alpha}>1\) as \(y\downarrow0\), one has \(h(y)>0\) for all sufficiently small positive \(y\). At the unique fixed point, \(h(y_K)=0\) and \(h'(y_K)=\lambda(K)^2-1>0\), so \(h(y)<0\) just to the left of \(y_K\). By the intermediate value theorem there exists \(0<y_-<y_K\) with \(h(y_-)=0\). As \(y_-<y_K\), the exponent defining \(f_K(y_-)\) is positive and \(y_+=f_K(y_-)>y_-\). The point \(y_+\) cannot lie below \(y_K\), because then \(f_K(y_+)>y_+\), contradicting \(f_K(y_+)=y_-\); it cannot equal \(y_K\) either. Hence \(y_-<y_K<y_+\), and \((Ky_-^{\alpha},y_-)\), \((Ky_+^{\alpha},y_+)\) form a strictly positive genuine period-two orbit.

**4. Criticality and the strength threshold.** At \(K_c\), write \(z=y-y_c\). Ordinary differentiation of the explicit scalar map at the critical equilibrium gives
\[
f_{K_c}'(y_c)=-1,\qquad
f_{K_c}''(y_c)=-\frac{t}{y_c},\qquad
f_{K_c}'''(y_c)=\frac{4+(5-\alpha)t}{y_c^2}.
\]
Accordingly its centered Taylor form is \(-z+az^2+bz^3+O(z^4)\), with
\[
a=-\frac{t}{2y_c},\quad b=\frac{4+(5-\alpha)t}{6y_c^2},\quad
c=a^2+b=\frac{Q(\alpha,t)}{12y_c^2}.
\]
For the moving fixed point, set \(\mu(K)=-1-\lambda(K)\). Then \(\mu(K_c)=0\) and \(\mu'(K_c)>0\). The second iterate centered at that point satisfies
\[
f_K^2(y_K+z)-(y_K+z)
=2\mu z-2cz^3+O(\mu^2|z|+|\mu|z^2+|z|^4),
\]
where the coefficients are smooth near \(K_c\). Because \(c\ne0\), the smooth one-dimensional flip normal form, or an implicit-function argument after the scaling \(z=\sqrt{|\mu|}\,w\), gives precisely two nearby nonfixed points when \(\mu/c>0\), at
\[
z_{\pm}=\pm\sqrt{\mu/c}+O(\mu).
\]
They form one period-two orbit. Its second-iterate multiplier is \(1-4\mu+O(|\mu|^{3/2})\): therefore it is attracting within its leaf when \(c>0\) and \(\mu>0\), but repelling within its leaf when \(c<0\) and \(\mu<0\). The neutral transverse family forbids inference of asymptotic stability of a particular period-two orbit in the full plane.

Finally, \(Q\) is an upward quadratic in \(t\). Its discriminant is \(4[(\alpha-5)^2-24]\). A negative value at an admissible positive \(t\) is possible exactly when \(\alpha>5+\sqrt{24}=5+2\sqrt6\); the two positive roots then lie in the allowed interval \((0,2(\alpha-1))\). The root formula yields the stated sharp subcritical parameter band.

Two exact examples demonstrate both signs. At \((\alpha,R)=(2,3)\), the critical equilibrium is \((1,1)\), \(K_c=1\), and \(Q=17>0\). At \((\alpha,R)=(10,55/3)\), the critical equilibrium is \((5/27,49/27)\), \(K_c=(5/27)/(49/27)^{10}\), and \(Q=-1/3<0\).

## Verification

The standalone script `verify.py` uses SymPy to check the derivative identities for arbitrary symbolic \(\alpha\), the exact coefficient \(Q/(12y_c^2)\), the crossing derivative, and the two rational examples. Using high-precision numerical arithmetic, it also locates one leafwise attracting cycle for \((\alpha,R,K/K_c)=(2,3,1.0001)\) and one leafwise repelling cycle for \((10,55/3,0.999999)\), checking both period-two equations and their multipliers. Run `python verify.py` with Python 3, SymPy, and mpmath installed. These numerical examples are illustrations, not a substitute for the all-parameter proof or a rigorous finite-precision certificate.

## Relationship to prior work

Goldar and collaborators' 2026 paper studies the same two-species Ricker equations and flip dynamics for an isolated coexistence equilibrium, but its explicit equilibrium formula divides by \(1-\alpha\beta\) and its planar flip argument requires a nonresonant second multiplier. The present coincident-isocline case has \(\alpha\beta=1\) and multipliers \((1,-1)\) at the flip, so it is not implied by that theorem. Luís, Elaydi and Oliveira (2011) explicitly put aside the case \(\alpha\beta=1\) as parallel isoclines; the additional equality of growth-rate intercepts instead makes the isoclines coincide. Kulakov, Neverova and Frisman (2022) discuss the \(\alpha\beta=1\) competition boundary and phase multistability, but not this leafwise criticality polynomial. Baigent and collaborators' 2023 global-convergence theorem covers log-growth rates at most \(2\); the present construction requires \(R>2\). Earlier scalar Ricker flips and generic bifurcation normal forms are standard tools, not claimed as new.

The added result is specifically the invariant composition foliation, the exact global existence of two-cycles beyond its transverse flip threshold, and the sharp parameter transition between supercritical and subcritical leafwise flips.

## Limitations

The theorem is restricted to exact rank-one competition and exactly aligned intrinsic growth rates, not to all two-species Ricker systems. The fixed-point stability statement is local along each invariant leaf; the global two-cycle existence result does not classify the number, stability, or basins of all other cycles. Near \(Q=0\) the cubic criterion vanishes and no quintic flip conclusion is supplied. No perturbative persistence under deviations from \(\alpha\beta=1\), no demographic stochasticity, and no biological calibration are asserted. Possible overlap with unindexed analyses of degenerate Ricker maps remains an originality risk.

## References

1. S. Goldar and collaborators, “Dynamics and Bifurcations in a Two-Species Ricker Competition Model With Nonmonotonic Growth,” *Discrete Dynamics in Nature and Society* (2026), first published 16 September 2026, DOI: 10.1155/ddns/7255117. https://onlinelibrary.wiley.com/doi/10.1155/ddns/7255117
2. R. Luís, S. Elaydi and H. Oliveira, “Stability of a Ricker-type competition model and the competitive exclusion principle,” *Journal of Biological Dynamics* (2011), DOI: 10.1080/17513758.2011.581764. https://digituma.uma.pt/bitstream/10400.13/3774/1/Stability%20of%20a%20Ricker%20type%20competition%20model%20and%20the%20competitive%20exclusion%20principle.pdf
3. M. Kulakov, G. Neverova and E. Frisman, “The Ricker Competition Model of Two Species: Dynamic Modes and Phase Multistability,” *Mathematics* 10 (2022), 1076, DOI: 10.3390/math10071076. https://www.mdpi.com/2227-7390/10/7/1076
4. S. Baigent, Z. Hou, S. Elaydi, E. C. Balreira and R. Luís, “A global picture for the planar Ricker map: convergence to fixed points and identification of the stable/unstable manifolds,” *Journal of Difference Equations and Applications* 29 (2023), 575–591, DOI: 10.1080/10236198.2023.2222855. https://repository.londonmet.ac.uk/8616/
