# Two negative folds and a transcritical collision in the ETM-3D equilibrium diagram

## Finding
Consider the one-parameter quadratic flow
\[
\dot x=-2x-\rho y+yz,\qquad
\dot y=x-y+\rho z-2xz,\qquad
\dot z=\rho y-5z+xy.
\]
On the previously unclassified range \(\rho\leq0\), its **entire real equilibrium census** is controlled by precisely two ordinary saddle-node folds and one transcritical collision with the origin. Let
\[
P(t)=594t^8-2076t^7-5948t^6+20050t^5+25505t^4-66100t^3-63325t^2+77500t+75000.
\]
This polynomial, already known from the positive-parameter equilibrium discriminant, has exactly two negative roots \(\beta_1<\beta_2\), both simple, enclosed by the rational intervals
\[
-2.011934533282<\beta_1<-2.011934533281,\qquad
-1.308660544092<\beta_2<-1.308660544091.
\]
Define \(\tau=(5-\sqrt{105})/4=-1.311737691489899\ldots\). Then \(\beta_1<\tau<\beta_2\). For **all real** \(\rho\leq0\), the number \(E(\rho)\) of distinct real equilibria, including the origin, equals
\[
E(\rho)=\begin{cases}
5,&\rho<\beta_1,\\
4,&\rho=\beta_1,\\
3,&\beta_1<\rho<\beta_2,\ \rho\ne\tau,\\
2,&\rho=\tau\text{ or }\rho=\beta_2,\\
1,&\beta_2<\rho\leq0.
\end{cases}
\]
The exceptional value \(\rho=-\sqrt5\) is included in the five-equilibrium regime: it has the additional equilibrium \((0,5,-\sqrt5)\), not a missing or additional fifth root. At \(\tau\), a simple quartic root represents the origin rather than a distinct nonzero equilibrium; this is the one-point drop in the otherwise three-equilibrium interval.

The folds are nondegenerate. Their nonzero equilibrium abscissae satisfy, respectively,
\[
0.620900<x_1<0.620902,\qquad 0.103166<x_2<0.103169.
\]
At the first fold, the two nonzero transverse eigenvalues have opposite signs; at the second fold they both have negative real part. At \(\tau\), the origin has one simple zero eigenvalue and two stable transverse eigenvalues, and its one-dimensional center dynamics has the generic transcritical normal form
\[
\dot u=b(\rho-\tau)u+a u^2+O\!\left(|u|^3+|\rho-\tau|u^2+(\rho-\tau)^2|u|\right),
\quad a=\frac{2\tau(1+\tau)}{3(8-\tau)}>0,\quad
b=\frac{2(4\tau-5)}{3(8-\tau)}<0.
\]
The finding classifies equilibrium existence and these three local bifurcations, **not** global attractors or the stability of every nonzero branch.

## Assumptions and scope
The parameter \(\rho\) is any real number in \(( -\infty,0]\). Equilibria are distinct real solutions of the displayed three polynomial equations. A fold is an ordinary codimension-one saddle-node in the original three-dimensional vector field. The transcritical claim is a local smooth center-manifold statement with the origin as a fixed equilibrium for all parameters. Numerical decimals only locate exact algebraic quantities; all changes of root count are justified by exact rational Sturm and sign certificates. No boundedness or uniqueness of invariant measures is asserted.

## Proof
**Equilibrium reduction and exceptional axis.** Set \(D=2x^2+\rho x+5-\rho^2\). For every equilibrium with \(x\ne0\), the second and third equations give
\[
y=5x/D,\qquad z=x(\rho+x)/D,\qquad D\ne0.
\]
The first equation reduces exactly to
\[
F(x,\rho)=2D^2+5\rho D-5x(\rho+x)=0.
\]
Conversely, for a real root \(x\ne0\) of \(F\), \(D=0\) is impossible because \(F=-5x(\rho+x)=0\) would then require \(x=-\rho\), yielding \(D=2\rho^2-\rho^2+5-\rho^2=5>0\). Thus every nonzero root yields exactly one genuine equilibrium. For \(x=0\), the original system has the origin for every \(\rho\), and exactly one further axial equilibrium \((0,5,\rho)\) when \(\rho=\pm\sqrt5\). In particular, at \(\rho=-\sqrt5\) the quartic's zero root is not to be inserted via the singular rational expressions; it is replaced by the genuine axial equilibrium. The zero roots of the quartic satisfy
\[
F(0,\rho)=(\rho^2-5)(2\rho^2-5\rho-10)=0.
\]
Besides \(\rho=-\sqrt5\), the only nonpositive parameter where a quartic root vanishes is \(\tau=(5-\sqrt{105})/4\). At \(\tau\), \(D=5-\tau^2\ne0\), so the zero root yields the origin, not a new equilibrium.

**Global real-root census.** Expanding \(F\) gives the quartic in the source. Exact elimination yields
\[
\operatorname{disc}_xF=12000P(\rho),\qquad
\gcd(P,P')=1.
\]
An exact Sturm chain shows that \(P\) has precisely two negative zeros, isolated by the rational intervals in the finding. The quartic has respectively four, two, and zero real roots at the exact rational test parameters \(\rho=-3,-3/2,-1\). Its leading coefficient is the constant \(8\), so roots cannot escape to infinity at finite \(\rho\), and the only possible multiplicity changes occur where \(P=0\). The root counts therefore are four, two, and zero in the three open parameter intervals. At each fold the subresultant of \(F\) and \(F_x\) is a nonzero linear polynomial, certifying a unique double real root; hence the distinct quartic-root counts at the folds are three and one. Adding the origin and correcting the two zero-root exceptions as described above yields precisely the displayed census for all \(\rho\leq0\).

**Fold nondegeneracy.** The last nonzero signed subresultant has the exact form
\[
-1280\bigl(A(\rho)x+B(\rho)\bigr),
\]
where
\[
A(t)=576t^4-1000t^3-3280t^2+2900t+5250,\qquad
B(t)=306t^5-610t^4-2120t^3+2275t^2+4325t.
\]
At either negative root of \(P\), exact interval arithmetic verifies \(A\ne0\), so the unique multiple-root abscissa is \(x=-B/A\) and lies in the positive intervals stated above. Along the corresponding equilibrium, interval evaluations certify
\[
\begin{array}{c|ccc}
 &F_\rho&F_{xx}&c_2\\\hline
\beta_1&(-40,-37)&(-43,-40)&(-32,-30)\\
\beta_2&(30,34)&(16,20)&(13,15)
\end{array}
\]
where \(c_2\) is the coefficient of \(\lambda\) in the Jacobian characteristic polynomial, given exactly by
\[
c_2=17+(\rho-z)(1-2z)-y^2-(\rho-2x)(\rho+x).
\]
Since \(F_{\rho}\ne0\) and \(F_{xx}\ne0\), the reduced equilibrium equations have ordinary fold geometry. The Jacobian of the original \(y,z\) equilibrium equations with respect to \(y,z\) has determinant \(D\), nonzero at both folds, so this is a smooth local elimination. Because \(c_2\ne0\), the full Jacobian has exactly one simple zero eigenvalue there; hence both folds are generic in the full flow. The Jacobian trace is always \(-8\). At \(\beta_1\), \(c_2<0\) implies opposite-sign transverse eigenvalues. At \(\beta_2\), \(c_2>0\) implies both transverse eigenvalues have negative real part.

**Transcritical collision.** At the origin the Jacobian is
\[
A_0(\rho)=\begin{pmatrix}-2&-\rho&0\\1&-1&\rho\\0&\rho&-5\end{pmatrix},\qquad
\det A_0=2\rho^2-5\rho-10.
\]
At its negative simple root \(\rho=\tau\), a right zero eigenvector is \(v=(-\tau/2,1,\tau/5)\) and a left zero eigenvector is \(w=(1,2,2\tau/5)\). They have \(w\cdot v=3(8-\tau)/10>0\). The other eigenvalues solve
\[
\lambda^2+8\lambda+3(8-\tau)/2=0
\]
and thus have negative real part. Writing the quadratic vector field as \(A_0(\rho)X+N(X)\), projection onto the center direction gives
\[
a=\frac{w\cdot N(v)}{w\cdot v}
=\frac{2\tau(1+\tau)}{3(8-\tau)}\ne0,\qquad
b=\frac{w\cdot A_0'(\tau)v}{w\cdot v}
=\frac{2(4\tau-5)}{3(8-\tau)}\ne0.
\]
The origin persists for all \(\rho\). The nonzero quadratic and crossing coefficients therefore yield a generic transcritical exchange of center-direction stability. The strict ordering of \(\tau\) between the two folds follows from the displayed exact root-isolating intervals and the rational square bounds \(10.2469507<\sqrt{105}<10.2469509\).

## Verification
Run `python CHECK.py` with Python 3 and SymPy. The standalone checker verifies the original-equation elimination and reconstructs the equilibrium quartic; verifies the discriminant and subresultant identities symbolically; uses exact Sturm counts to isolate both negative roots and certify root numbers at the three test parameters; checks the special-axis factorization; encloses both folds and their Jacobian and nondegeneracy coefficients using rational interval arithmetic; and verifies the center-normal-form coefficients. No floating-point sign test is used in the certificates. The checker does not prove global attraction or the nonexistence of periodic or chaotic attractors.

## Relationship to prior work
Khalili-Amirabadi and Jalaeian-Farimani (arXiv:2610.04768v1, first posted 2026-10-03) introduce the vector field and its quartic reduction and study the benchmark domain \(\rho\geq0\), explicitly proposing the negative branch as future work. The negative equilibrium counts, negative folds, and transcritical parameter proved here are outside that domain. The publicly accessible research record *Exact global-stability threshold at the first ETM-3D saddle-node* (2026-10-11) derives the **same polynomial \(P\)** as a positive-parameter discriminant, and proves a global-stability statement only for \(\rho\geq0\). Therefore neither the polynomial itself nor the reduction is claimed as original; the new contribution is the exact and complete **negative-parameter bifurcation classification** and its generic local structure. Classical saddle-node and transcritical normal-form theory supplies the implication of the verified nondegeneracy coefficients, not this specific diagram.

## Limitations
The classification covers real equilibria and three local codimension-one events for \(\rho\leq0\), not their global invariant manifolds, periodic orbit branches, or full nonlinear attractor structure. The rational intervals are certificates for exact algebraic quantities; displayed decimal approximations are explanatory only. A dynamically equivalent classification from earlier work not indexed by the searched scholarly records remains a literature risk. No independent audit or independent validation has been performed.

## References
1. R. Khalili-Amirabadi and M. Jalaeian-Farimani, *ETM-3D: A One-Parameter Multistable Quadratic Flow with an Explicit Absorbing Set and Intermittent Chaos*, arXiv:2610.04768v1 (2026-10-03), https://arxiv.org/abs/2610.04768 .
2. *Exact global-stability threshold at the first ETM-3D saddle-node*, public published-finding corpus research record (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-global-stability-threshold-at-the-first-etm-3d-saddle-node--997f2098aca6 .
3. Y. A. Kuznetsov, *Elements of Applied Bifurcation Theory*, 3rd edition, Springer, 2004 (for general fold and transcritical criteria, not an ETM-specific calculation).
