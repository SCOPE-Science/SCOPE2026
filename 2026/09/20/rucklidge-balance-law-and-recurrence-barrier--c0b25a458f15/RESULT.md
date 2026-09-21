# An exact balance law and a damping-sign recurrence barrier for the Rucklidge flow

## Statement

Consider the Rucklidge system
\[
\dot x=-ax+by-yz,\qquad \dot y=x,\qquad \dot z=-z+y^2,
\tag{1}
\]
with real parameters \(a,b\). Define
\[
\mathcal F(x,y,z)=\frac{x^2}{2}-\frac b2y^2+\frac12y^2z-\frac14z^2.
\tag{2}
\]
Then every classical solution of (1) satisfies the exact pointwise balance
\[
\boxed{\quad \dot{\mathcal F}=-a x^2+\frac12\dot z^{\,2}.\quad}
\tag{3}
\]

This identity has three global consequences.

**(i) Universal bounded-orbit and periodic-orbit balance.** If a forward solution is bounded, then
\[
\lim_{T\to\infty}\frac1T\int_0^T\bigl(\dot z^{\,2}-2a x^2\bigr)\,dt=0.
\tag{4}
\]
In particular, every non-equilibrium periodic orbit of period \(P\) obeys
\[
\int_0^P\dot z^{\,2}\,dt=2a\int_0^P x^2\,dt.
\tag{5}
\]
Hence a non-equilibrium periodic orbit can exist only when \(a>0\), and then
\[
\frac{\|\dot z\|_{L^2(0,P)}}{\|x\|_{L^2(0,P)}}=\sqrt{2a}.
\tag{6}
\]
Since \(x=\dot y\), (6) is an exact parameter-only ratio between the mean-square relaxation rate of \(z\) and the mean-square rate of change of the convective amplitude \(y\).

**(ii) Invariant-measure recurrence barrier.** Let \(\mu\) be a compactly supported invariant probability measure of (1). Then
\[
\int (y^2-z)^2\,d\mu=2a\int x^2\,d\mu.
\tag{7}
\]
Consequently, if \(a\le0\), every such invariant probability measure is supported on equilibria. Equivalently, every non-equilibrium compact invariant ergodic measure requires \(a>0\).

For reference, the equilibrium set is
\[
\mathcal E=\{(0,0,0)\}\cup
\begin{cases}
\{(0,\sqrt b,b),(0,-\sqrt b,b)\},&b>0,\\
\varnothing,&b\le0.
\end{cases}
\tag{8}
\]

**(iii) Convergence of every bounded forward orbit for nonpositive damping.** If \(a\le0\) and a forward solution of (1) is bounded, then it converges to a single equilibrium in \(\mathcal E\). Thus the half-plane \(a\le0\) admits no bounded non-equilibrium recurrent motion: no periodic orbit, quasiperiodic compact invariant torus, or bounded chaotic attractor.

## Proof

Differentiate (2) along (1):
\[
\begin{aligned}
\dot{\mathcal F}
&=x(-ax+by-yz)-byx+xyz
 +\frac12y^2(-z+y^2)-\frac12z(-z+y^2)\\
&=-ax^2+\frac12(y^2-z)^2
=-ax^2+\frac12\dot z^{\,2},
\end{aligned}
\]
which proves (3).

If the trajectory is bounded, \(\mathcal F\) is bounded on it. Integrating (3) over \([0,T]\) gives
\[
\frac1T\int_0^T(\dot z^{\,2}-2ax^2)\,dt
=\frac{2(\mathcal F(T)-\mathcal F(0))}{T}\to0,
\]
proving (4). Periodicity makes the endpoint difference exactly zero and yields (5). A non-equilibrium periodic orbit cannot have \(x\equiv0\): then \(y\) is constant, and the remaining equations force an equilibrium. Thus (5) implies \(a>0\) for every non-equilibrium periodic orbit.

For an invariant probability measure with compact support, the generator identity \(\int L\mathcal F\,d\mu=0\) is legitimate because \(\mathcal F\) and its derivative are bounded on the support. Using (3) gives (7). If \(a<0\), both terms in
\[
0=|a|\int x^2\,d\mu+\frac12\int(y^2-z)^2\,d\mu
\]
are nonnegative, so \(x=0\) and \(y^2=z\) on \(\operatorname{supp}\mu\). The largest invariant subset of this zero set is \(\mathcal E\): preserving \(x=0\) requires \(y(b-y^2)=0\). If \(a=0\), (7) gives \(z=y^2\) on the support. Along a trajectory that remains in this surface,
\[
\frac d{dt}(z-y^2)=-2xy,
\]
so \(xy=0\). If \(y\ne0\), invariance forces \(x=0\) and then \(y(b-y^2)=0\). If \(y=0\), then \(z=0\); preserving \(xy=0\) forces \(x=0\) because \((xy)'=x^2+yx'\). Hence the largest invariant subset is again \(\mathcal E\). This proves (ii).

Finally suppose \(a\le0\) and a forward orbit is bounded. Then \(\mathcal F\) is nondecreasing and bounded above, hence convergent. The LaSalle invariance argument on the compact omega-limit set places that set in the largest invariant subset of \(\{\dot{\mathcal F}=0\}\), which by the preceding calculation is \(\mathcal E\). The omega-limit set of a precompact continuous-time trajectory is connected, whereas \(\mathcal E\) is finite; therefore the omega-limit set is a single equilibrium. This proves (iii).

## Additional exact stationary moments

For any compactly supported invariant probability measure, elementary generator identities give
\[
\int y^2\,d\mu=\int z\,d\mu=:m,\qquad
\int xy\,d\mu=0,
\tag{9}
\]
\[
\int z^2\,d\mu=\int x^2\,d\mu+b\,m,
\tag{10}
\]
and, combining (7) with \(\int y^2z\,d\mu=\int z^2\,d\mu\),
\[
\int y^4\,d\mu=(1+2a)\int x^2\,d\mu+b\,m.
\tag{11}
\]
These relations give exact diagnostics for numerically computed periodic and chaotic invariant measures in the usual \(a>0\) regime.

## Shimizu–Morioka form

The closely related Shimizu–Morioka equations
\[
\dot u=v,\qquad \dot v=u-\lambda v-uw,\qquad \dot w=-\alpha w+u^2
\tag{12}
\]
admit the parallel identity
\[
\mathcal G=\frac12v^2-\frac12u^2+\frac12u^2w-\frac\alpha4w^2,
\qquad
\boxed{\dot{\mathcal G}=-\lambda v^2+\frac12\dot w^{\,2}}.
\tag{13}
\]
Thus for \(\alpha>0\), the same argument gives a recurrence barrier at \(\lambda\le0\): every bounded forward trajectory converges to an equilibrium, and every non-equilibrium compact invariant probability measure requires \(\lambda>0\). This is consistent with the known linear-scaling equivalence between the Shimizu–Morioka and Rucklidge families.

## Relation to prior literature

Rucklidge's 1992 and 1993 papers introduced and analysed the low-order convection model, including homoclinic explosions, Lorenz-like chaos and escape to infinity in parts of parameter space. The 1993 author manuscript explicitly notes that the reduced ODE can have unbounded trajectories and restricts the physically relevant discussion to bounded ones. It does not state (3), the sharp damping-sign recurrence barrier, or the invariant-measure balances above.

Messias, Gouveia and Pessoa (2012) gave a global Poincare-compactification analysis of the Shimizu–Morioka equations and studied the degenerate heteroclinic structure at \(\alpha=0\). Their paper includes local information for negative \(\lambda\), but the located statements do not give (13) or the global bounded-orbit conclusion for \(\lambda\le0\).

Lima, Llibre and Valls (2014) studied Darboux and analytic integrability of exactly (1). Their introduction states that chaotic attractors occur, among other examples, at \((a,b)=(-0.1,-1)\). The theorem above shows that this specific claim cannot describe a bounded recurrent attractor of (1): because \(a<0\) and \(b<0\), every bounded forward trajectory converges to the unique equilibrium \((0,0,0)\). Any non-equilibrium behavior at those parameters must therefore fail to remain bounded indefinitely. This also illustrates why negative divergence alone does not prove the existence of a bounded attractor.

Later work on meromorphic non-integrability (2017), the Rucklidge/Shimizu–Morioka scaling relation and integrability (2020), unstable periodic-orbit organization (2021), and invariant algebraic manifolds (2023) addresses different questions. The accessible 2023 abstract states a classification of invariant algebraic manifolds and explicit solutions on them; its full theorem statements were not inspected, so it remains the most relevant residual prior-coverage risk. The 2021 study takes \(a,b>0\) and numerically catalogues periodic orbits, bifurcations, and chaos, but does not report the exact periodic-orbit constraint (5) or the invariant-measure identity (7).

## Limitations

The originality assessment is to the best of our knowledge. The literature search covered the original Rucklidge papers, global Shimizu–Morioka dynamics, Rucklidge integrability and non-integrability, the explicit Rucklidge/Shimizu–Morioka scaling literature, and recent periodic-orbit studies. No located source stated the polynomial balance (3), its invariant-measure form (7), or the global recurrence barrier at nonpositive damping. A mathematically equivalent identity could nevertheless exist under a different normalization or notation and remain unlocated. In particular, the full text of Demina and Ilyukhin (2023), which classifies invariant algebraic manifolds for the Rucklidge model, was not inspected; only its abstract and bibliographic description were available, so an equivalent balance hidden in that paper remains a specific residual risk.

The convergence theorem is conditional on forward boundedness; it does not assert global boundedness. In fact, escape to infinity is part of the established global picture of the reduced Rucklidge model. The result also concerns the autonomous ODE itself, not the higher-order corrected magnetoconvection model or the parent PDE.

## Reproducibility

`artifacts/verify_rucklidge_balance.py` symbolically differentiates both balance functions and verifies the stationary generator identities. `artifacts/verification.txt` records the resulting zero residuals. The verification uses SymPy 1.14.0 and exact symbolic arithmetic.

## References

1. A. M. Rucklidge, "Chaos in models of double convection," *Journal of Fluid Mechanics* 237 (1992), 209–229. https://doi.org/10.1017/S0022112092003392
2. A. M. Rucklidge, "Chaos in a low-order model of magnetoconvection," *Physica D* 62 (1993), 323–337. https://doi.org/10.1016/0167-2789(93)90291-8
3. M. Messias, M. R. A. Gouveia, C. Pessoa, "Dynamics at infinity and other global dynamical aspects of Shimizu–Morioka equations," *Nonlinear Dynamics* 69 (2012), 577–587. https://doi.org/10.1007/s11071-011-0288-8
4. X. Zhao, F. Jiang, Z. Zhang, J. Hu, "A New Series of Three-Dimensional Chaotic Systems with Cross-Product Nonlinearities and Their Switching," *Journal of Applied Mathematics* 2013, 590421. https://doi.org/10.1155/2013/590421
5. M. F. S. Lima, J. Llibre, C. Valls, "Integrability of the Rucklidge system," *Nonlinear Dynamics* 77 (2014), 1441–1453. https://doi.org/10.1007/s11071-014-1389-y
6. K. Huang, S. Shi, W. Li, "Meromorphic Non-Integrability of Several 3D Dynamical Systems," *Entropy* 19 (2017), 211. https://doi.org/10.3390/e19050211
7. K. Huang, S. Shi, W. Li, "Integrability analysis of the Shimizu–Morioka system," *Communications in Nonlinear Science and Numerical Simulation* 84 (2020), 105101. https://doi.org/10.1016/j.cnsns.2019.105101
8. E. Dong et al., "Symbolic Encoding of Periodic Orbits and Chaos in the Rucklidge System," *Complexity* 2021, 4465151. https://doi.org/10.1155/2021/4465151
9. M. V. Demina, D. O. Ilyukhin, "Invariant algebraic manifolds for the Rucklidge model of double convection," *Siberian Mathematical Journal* 64 (2023), 1145–1152. https://doi.org/10.1134/S0037446623050075
