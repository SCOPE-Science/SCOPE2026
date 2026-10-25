# Sharp triple coexistence at balanced dispersal in a two-patch Allee model

## Finding
Consider the positive-parameter two-patch population model with linear symmetric migration
\[
\dot u=u\left(\frac{u}{m+u}-e-hu\right)+\delta(v-u),\qquad
\dot v=sv(1-v)+\delta(u-v).
\]
Assume \(m,h,s,\delta>0\) and \(0<e<1\). At the natural **balanced-dispersal condition** \(\delta=s\), the system has between one and three distinct strictly positive equilibria. The upper bound of three is sharp, and there is an exact criterion for its attainment.

Write
\[
P(z)=-hz^5+(1-e-s-hm)z^3+sz^2-m(e+s)z+sm.
\]
Every positive equilibrium is uniquely \((u,v)=(z^2,z)\) with \(z>0\) and \(P(z)=0\). There are **three distinct positive equilibria if and only if** the derivative \(P'\) has two distinct positive zeros \(a<b\) satisfying
\[
P(a)<0<P(b).
\]
They are all simple. With three equilibria ordered by increasing \(v\), the first and third are locally asymptotically stable and the middle one is a saddle. More generally every simple positive root with \(P'<0\) gives a locally asymptotically stable equilibrium, and each with \(P'>0\) gives a saddle. If \(P'\) has two positive zeros, equality \(P(a)=0\) or \(P(b)=0\) gives two distinct positive equilibria, one degenerate; outside these cases there is exactly one distinct positive equilibrium. When \(P'\) has fewer than two distinct positive zeros, there is exactly one distinct positive equilibrium.

The sharpness witness is
\[
(m,e,h,s,\delta)=(1,2/5,1/10,1/5,1/5).
\]
Here \(10P(z)=-z^5+3z^3+2z^2-6z+2\), which has one root in \((1/3,1/2)\), the exact root \(z=1\), and one root in \((3/2,8/5)\). These are the only positive roots and yield, respectively, a stable equilibrium, a saddle, and another stable equilibrium. All three equilibria are hyperbolic, so the pair of distinct positive attractors persists under sufficiently small perturbations of **all five parameters**, including perturbations for which \(\delta\ne s\). This is robust positive-population bistability, not an extinction/coexistence alternative restricted to a single parameter surface.

## Assumptions and scope
The system is autonomous, deterministic and continuous-time, with two nonnegative patch abundances and symmetric **linear** exchange. All \(m,h,s,\delta\) are strictly positive and \(0<e<1\). The sharp number bound and exact criterion apply only when \(\delta=s\), the point at which the intrinsic small-density growth rate \(s\) in the logistic patch equals its emigrant loss rate. A positive equilibrium means both coordinates strictly positive. Stability assertions about roots of \(P\) concern only simple roots. Robustness near the explicit witness uses a standard hyperbolic-equilibrium continuation argument and does not assert a sharp upper bound for arbitrary unequal \(\delta,s\).

## Proof
**1. Exact reduction and existence.** At \(\delta=s\), the second right-hand side is identically \(s(u-v^2)\). Therefore every strictly positive equilibrium has \(u=v^2\). Substituting \(u=z^2,v=z\) into the first right-hand side yields the exact identity
\[
\dot u\big|_{(z^2,z)}=\frac{zP(z)}{m+z^2},
\]
where \(P\) is the displayed polynomial. Since \(P(0)=sm>0\) and \(P(z)\to-\infty\) as \(z\to+\infty\), at least one positive equilibrium exists.

**2. A sharp upper bound and complete count criterion.** Put \(c=1-e-s-hm\). Then
\[
P'(z)=-5hz^4+3cz^2+2sz-m(e+s),\qquad
P''(z)=-20hz^3+6cz+2s.
\]
The cubic \(P''\) has exactly one positive zero. Indeed, if \(c\le0\), it decreases strictly from \(2s>0\) to \(-\infty\). If \(c>0\), it first increases, reaches one positive maximum, then decreases strictly to \(-\infty\), so it still crosses zero exactly once. Thus \(P'\) first increases and then decreases on \((0,\infty)\). As \(P'(0)=-m(e+s)<0\) and \(P'(z)\to-\infty\), it has zero, one tangential, or two distinct positive zeros. Consequently \(P\) has at most three distinct positive zeros. If \(P'\) has two zeros \(a<b\), then \(P\) strictly decreases on \((0,a)\), increases on \((a,b)\), and decreases on \((b,\infty)\); the endpoint signs \(P(0)>0>P(+\infty)\) give exactly the claimed three-root and boundary criteria. With fewer critical zeros, \(P\) is strictly decreasing apart from isolated stationary points, hence has exactly one distinct positive root.

**3. Stability determined by a scalar slope.** At a positive equilibrium parameterized by \(z\), the Jacobian is
\[
J(z)=\begin{pmatrix}
\dfrac{z^2(2m+z^2)}{(m+z^2)^2}-e-2hz^2-s&s\\
s&-2sz
\end{pmatrix}.
\]
Differentiating the exact scalar identity from step 1 gives \(2zJ_{11}(z)+s=zP'(z)/(m+z^2)\), because \(P(z)=0\). Therefore
\[
\det J(z)=-s\bigl(2zJ_{11}(z)+s\bigr)
=-\frac{szP'(z)}{m+z^2}.
\]
If \(P'(z)>0\), the determinant is negative, so the equilibrium is a saddle. If \(P'(z)<0\), the determinant is positive, which implies \(J_{11}(z)<-s/(2z)<0\); consequently \(\operatorname{tr}J(z)=J_{11}(z)-2sz<0\). The planar Hurwitz criterion yields local asymptotic stability. With three simple roots, their scalar slopes necessarily alternate negative, positive, negative.

**4. Exact three-equilibrium witness and persistence.** For the specified rational parameters, set \(Q(z)=10P(z)\). Direct exact evaluation yields
\[
Q(1/3)=80/243>0,\quad Q(1/2)=-5/32<0,\quad Q(1)=0,
\]
\[
Q(3/2)=1/32>0,\qquad Q(8/5)=-2118/3125<0,
\]
and \(Q'(1)=2>0\). Hence there are three distinct positive simple roots in the stated brackets, and step 2 excludes all additional positive roots. Step 3 gives stability–saddle–stability in that order. For example the middle equilibrium \((1,1)\) has \(\det J=-1/50\) and is a saddle. Since all three equilibria have invertible Jacobians, the implicit-function theorem applied separately to their two-equation equilibrium systems provides smooth, positive branches for all parameter tuples in a sufficiently small open neighborhood of the witness. Eigenvalue signs persist by continuity, giving two distinct positive local attractors separated by a saddle throughout that neighborhood.

## Verification
The accompanying standard-library `verify.py` evaluates the equilibrium polynomial reduction and determinant identity independently over exact rational parameter grids, checks every listed rational sign and the exact saddle determinant, and prints its assertion count. It performs 543 exact-rational assertions. These computations independently check algebraic identities and a finite witness, but the unlimited-parameter root bound and full stability classification follow from the analytical proof above, not finite enumeration. Run `python3 verify.py` from the same directory.

## Relationship to prior work
Xia, Chen, Srivastava and Parshad (2023, Section 2, equation (2.11)) introduced this linear-dispersal comparison model alongside a different nonlinear-dispersal model. They explicitly leave complete qualitative analysis of the linear model for future work. Their Theorems 2.9 and 2.10 treat sufficient cases including \(m\ge1/h\), whereas the sharp three-equilibrium witness here satisfies \(m<1/h\). Neither theorem entails the present three-equilibrium example or its exact balance criterion. The paper's nonlinear-dispersal conclusions apply to another system.

Bistability under Allee effects is well established in other spatial and two-patch population systems, notably Kang and Lanchier (2011) and Vortkamp and collaborators (2020); it is not claimed to be a new general phenomenon. Chen, Liu and Chen (2022) analyze a different additive-Allee two-patch system. Ketchemen Tchouaga and Lutscher (2023) analyze a spatial reaction–diffusion/interface model, not the present finite-dimensional symmetric-exchange system. The contribution here is confined to the exact sharp multiplicity and stability criterion for the identified linear comparison model at its biologically natural balance, together with a fully explicit robust witness.

## Limitations
The complete root-count criterion is restricted to the balance \(\delta=s\). It is not a global basin classification, an assertion about stochastic extinction, an analysis of the spatial PDE, or a claim that other two-patch Allee models cannot exhibit multiple positive attractors. At degenerate roots, determinant-zero linearization does not determine nonlinear stability. The implicit-function argument gives at least three persistent equilibria near the witness but does not prove that no additional equilibria arise far away in the unbalanced system. Literature-priority risk remains because stronger general results not located in the inspected literature might subsume a model-specific statement.

## References
1. Yue Xia, Lijuan Chen, Vaibhava Srivastava, Rana D. Parshad, *Stability and bifurcation analysis of a two-patch model with Allee effect and dispersal*, arXiv:2310.10558v1, initially public 16 October 2023; *Mathematical Biosciences and Engineering* 20 (2023), doi:10.3934/mbe.2023876. Particularly equation (2.11), Section 2.3 and Theorems 2.9–2.10.
2. Lijuan Chen, Tingting Liu, Fengde Chen, *Stability and bifurcation in a two-patch model with additive Allee effect*, *AIMS Mathematics* 7 (2022), 536–551, doi:10.3934/math.2022034.
3. Yang Kang and Nicolas Lanchier, *Expansion or extinction: deterministic and stochastic two-patch models with Allee effects*, arXiv:1003.0121.
4. Laurence Ketchemen Tchouaga and Frithjof Lutscher, *Steady-state dynamics in a two-patch population model with and without Allee effect*, *Mathematics in Applied Sciences and Engineering* 4 (2023), 196–226, doi:10.5206/mase/16474.
5. Wendi Wang, *Population dispersal and Allee effect*, *Ricerche di Matematica* 65 (2016), 535–548, doi:10.1007/s11587-016-0273-0.
6. Irina Vortkamp et al., *Multiple Attractors and Long Transients in Spatially Structured Populations with an Allee Effect*, *Bulletin of Mathematical Biology* 82 (2020), article 82, doi:10.1007/s11538-020-00750-x.
