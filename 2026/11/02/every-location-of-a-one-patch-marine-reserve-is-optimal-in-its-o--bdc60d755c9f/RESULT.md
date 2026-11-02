# Every location of a one-patch marine reserve is optimal in its own conservation-weight interval

## Finding
Consider three habitat patches on a line, numbered from a one-sided recruitment source. Exactly one patch must be a no-take marine reserve; the other two are harvested at the same positive per-capita rate. Adults diffuse symmetrically between adjacent patches and can leave the habitat at either endpoint. For **every** choice of positive natural mortality, movement and fishing rates, the unique optimal reserve location, as the weight on total standing stock increases, changes in the strict order **far endpoint, middle, recruitment endpoint**. Both transitions occur at positive, distinct, explicitly calculable weights; the middle reserve is always strictly optimal on a nonempty open interval.

Precisely, with the model in the next section, define the positive quantities \(T_j\) (steady-state total stock) and \(Y_j\) (steady-state total catch) for the reserve located at patch \(j\). Put
\[
Q_{23}=\frac{Y_3-Y_2}{T_2-T_3},\qquad
Q_{12}=\frac{Y_2-Y_1}{T_1-T_2}.
\]
The denominators are strictly positive, and \(0<Q_{23}<Q_{12}\). For every \(Q\geq 0\), the complete set of maximizers of \(Y_j+QT_j\) is
\[
\begin{cases}
\{3\},&0\le Q<Q_{23},\\
\{2,3\},&Q=Q_{23},\\
\{2\},&Q_{23}<Q<Q_{12},\\
\{1,2\},&Q=Q_{12},\\
\{1\},&Q>Q_{12}.
\end{cases}
\]
There is no triple tie. This classification is valid without asymptotic restrictions on the positive rates. It is a mathematical three-patch benchmark, not a field-derived prescription.

## Assumptions and scope
Let the adult population vector be \(u=(u_1,u_2,u_3)^\top\). Fix recruitment input \(R>0\) into patch \(1\) only, natural mortality \(\mu>0\), symmetric interpatch movement rate \(m>0\), fishing rate \(h>0\), and an exogenous conservation weight \(Q\geq0\). The two unoccupied ghost sites \(0\) and \(4\) have zero population, so each boundary patch also loses adults outward at rate \(m\). Recruitment is density independent. There are no feedbacks from catch to effort, economics of stock price, juvenile stages, or density-dependent reproduction.

When patch \(j\in\{1,2,3\}\) is the sole no-take reserve, set \(h_i^{(j)}=0\) for \(i=j\) and \(h_i^{(j)}=h\) otherwise. The linear ecological dynamics are
\[
\dot u_i=R\mathbf 1_{i=1}+m(u_{i-1}-2u_i+u_{i+1})-(\mu+h_i^{(j)})u_i,
\quad i=1,2,3,\quad u_0=u_4=0.
\]
Every scenario has a unique positive attracting steady state \(u^{(j)}\). Define \(T_j=\sum_{i=1}^3u_i^{(j)}\), \(Y_j=h\sum_{i\ne j}u_i^{(j)}\), and \(W_j(Q)=Y_j+QT_j\). This is a *mandatory one-patch reserve* problem: an unrestricted choice of zero, one, or multiple reserves is not part of the assertion. Values and formulas below are normalized to \(R=1\), because multiplying \(R\) rescales both outputs and leaves the threshold weights unchanged.

## Proof
**1. Existence and exact stock/catch.** Put
\[
A=\mu+h+2m,\quad B=\mu+2m,\quad
D=A^2B-(A+B)m^2,\quad X=AB-2m^2.
\]
For each location, the stationary coefficient matrix has diagonal \((A,A,A)\) except that the protected diagonal is \(B\), and it has adjacent off-diagonal entries \(-m\). Since each diagonal exceeds the sum of the absolute off-diagonal entries in its row, it is a positive definite irreducible \(M\)-matrix. This proves unique positive equilibrium and asymptotic stability. Its determinant is \(D\) when \(j=1\) or \(j=3\), and \(AX\) when \(j=2\). Direct cofactors of the first column of the inverse yield
\[
\begin{array}{lll}
T_1=\dfrac{A(A+m)}D,&
T_2=\dfrac{B+m}{X},&
T_3=\dfrac{B(A+m)}D,\\[5pt]
Y_1=\dfrac{hm(A+m)}D,&
Y_2=\dfrac{hB}{X},&
Y_3=\dfrac{h[B(A+m)-m^2]}D.
\end{array}
\]
The actual normalized equilibrium vectors, which provide an independent route to all six formulas, are
\[
 u^{(1)}=\frac{(A^2-m^2,\ mA,\ m^2)^\top}{D},\qquad
 u^{(2)}=\frac{(AB-m^2,\ mA,\ m^2)^\top}{AX},\qquad
 u^{(3)}=\frac{(AB-m^2,\ mB,\ m^2)^\top}{D}.
\]

**2. Strict Pareto ordering and explicit thresholds.** Define
\[
\begin{aligned}
P&=A^2B-(2A+B)m^2-m^3,\\
S&=AB+Bm-m^2,\\
N_{12}&=AB^2-2ABm+B^2m-2Bm^2+2m^3,\\
N_{01}&=A^2B^2-A^2Bm-2ABm^2+2Am^3-B^2m^2+2m^4.
\end{aligned}
\]
Here the subscript \(01\) is only an algebraic label; patches remain numbered \(1,2,3\). Elementary expansion of the six displayed stock/catch fractions gives
\[
\begin{aligned}
T_1-T_2&=\frac{hP}{XD},&T_2-T_3&=\frac{hmS}{XD},\\
Y_2-Y_1&=\frac{hN_{01}}{XD},&Y_3-Y_2&=\frac{hmN_{12}}{XD}.
\end{aligned}
\]
All these differences are strictly positive, as the following expansions show (every coefficient is positive for \(\mu,m,h>0\)):
\[
\begin{aligned}
P={}&2h^2m+h^2\mu+6hm^2+8hm\mu+2h\mu^2+m^3+9m^2\mu+6m\mu^2+\mu^3,\\
S={}&2hm+h\mu+5m^2+5m\mu+\mu^2,\\
N_{12}={}&2hm\mu+h\mu^2+2m^3+6m^2\mu+5m\mu^2+\mu^3,\\
N_{01}={}&2h^2m^2+3h^2m\mu+h^2\mu^2+6hm^3+14hm^2\mu+10hm\mu^2+2h\mu^3\\
&+2m^4+10m^3\mu+15m^2\mu^2+7m\mu^3+\mu^4.
\end{aligned}
\]
Further, \(D>0\) and \(X>0\) follow from strict diagonal dominance; alternatively they have positive-coefficient expansions in these variables. Thus \(T_1>T_2>T_3>0\) and \(0<Y_1<Y_2<Y_3\). The two switching weights are explicitly
\[
Q_{12}=\frac{N_{01}}P,\qquad Q_{23}=\frac{N_{12}}S.
\]
The decisive polynomial identity is
\[
N_{01}S-N_{12}P=mXD.
\]
All factors on the right are strictly positive; consequently
\[
Q_{12}-Q_{23}=\frac{mXD}{PS}>0.
\]
These identities are exact formal polynomial identities, not fitted numerical claims.

**3. Global selection.** The three objectives are affine lines \(W_j(Q)=Y_j+QT_j\), with strictly increasing intercepts as \(j\) moves from \(1\) to \(3\), and strictly decreasing slopes. Their adjacent intersections are \(Q_{23}<Q_{12}\). The crossing weight of lines \(1\) and \(3\) is
\[
Q_{13}=\frac{(T_1-T_2)Q_{12}+(T_2-T_3)Q_{23}}{T_1-T_3},
\]
which lies strictly between the two adjacent crossings. Therefore the upper envelope follows the order \(3\), then \(2\), then \(1\), with precisely the pairwise ties stated in the finding. No third line can tie at either adjacent crossing. This completes the proof for every positive rate tuple and every \(Q\ge0\).

## Verification
The standalone Python 3 file `check.py` uses only the standard library and exact rational arithmetic. It verifies five polynomial identities, strictly positive coefficients in the six decisive polynomials, the matrix-inverse formulas for 27 positive-rational rate triples, and 135 exact welfare comparisons at boundaries and between them. In total there are 216 equilibrium/ordering/optimality checks, plus the polynomial certificates. Run `python check.py` after extracting this file.

For the fully explicit normalized example \(\mu=m=h=R=1\), the yield/stock pairs are
\[
(Y_1,T_1)=\left(\frac5{41},\frac{20}{41}\right),\quad
(Y_2,T_2)=\left(\frac3{10},\frac25\right),\quad
(Y_3,T_3)=\left(\frac{14}{41},\frac{15}{41}\right),
\]
so \(Q_{23}=17/14\) and \(Q_{12}=73/36\). Both switches and the strictly exposed middle patch can be reproduced without floating-point arithmetic. The universal assertion rests on the symbolic proof, not on sampling parameter grids.

## Relationship to prior work
De Leenheer's 2013 *Optimal placement of Marine Protected Areas* (arXiv:1307.1581) analyzes a continuous-coast reaction-diffusion fishery with spatially **uniform** adult recruitment, absorbing coast endpoints and a yield-plus-standing-stock objective. Its Theorems 2 and 5 classify unrestricted spatial harvesting controls, with no reserve or a central reserve depending on scaled coastal length and weight. The present model retains the linear recruitment/mortality, diffusion and weighted-yield motivation but changes to **one-sided recruitment** and a **mandatory exactly-one-of-three patch reserve**. Uniform-source reflection symmetry and unrestricted-control conclusions therefore do not imply this three-way switching diagram.

Neubert's 2003 *Marine reserves and optimal harvesting* studies a spatial logistic fishery optimized for harvest; the publicly accessible abstract reports central reserves for one regime and finely alternating fishing/protection for another. Its yield-only, density-dependent setting does not state the present all-positive-rate, one-sided-recruitment, weighted-stock threshold classification. Ding and Lenhart (2009) give an accessible nonlinear elliptic fishery analysis with logistic growth, Dirichlet boundaries, and yield-minus-effort-cost objectives; this is likewise a different population equation and control space, with no three-line weighted-stock envelope. Earlier marine reserve configuration and source–sink papers motivate the geometry but their accessible treatments do not establish these exact threshold identities. This is a comparison of statements and assumptions, not a claim that keyword searches establish world-wide priority.

## Limitations
The result is structural, not empirical. In particular, the minimal three-patch coastline, one recruitment source, equal movement rates, lethal boundary leakage, fixed catch effort, deterministic density-independent reproduction and mandatory single reserve are essential hypotheses. It does not optimize any other reserve budget, claim a continuum-coast limit, or account for larval movement, economic prices, uncertainty or nonlinear population feedback. Full text of Neubert (2003) was not accessible during the comparison, and unlocated more general linear-resolvent or bioeconomic placement theorems could imply portions of the result. Historical novelty therefore remains provisional pending broader independent primary-literature review.

## References
- P. De Leenheer (2013), *Optimal placement of Marine Protected Areas*, arXiv:1307.1581, first publicly posted 2013-07-05. https://arxiv.org/abs/1307.1581
- W. Ding and S. Lenhart (2009), *Optimal Harvesting of a Spatially Explicit Fishery Model*, Natural Resource Modeling 22(2), 173–211. https://doi.org/10.1111/j.1939-7445.2008.00033.x
- M. G. Neubert (2003), *Marine reserves and optimal harvesting*, Ecology Letters 6, 843–849, first published 2003-08-11. https://doi.org/10.1046/j.1461-0248.2003.00493.x
- C. M. Roberts (1998), *Sources, sinks, and the design of marine reserve networks*, Fisheries 23(7), 16–19. https://pure.york.ac.uk/portal/en/publications/sources-sinks-and-the-design-of-marine-reserve-networks/
- L. W. Botsford, F. Micheli and A. Hastings (2003), *Principles for the design of marine reserves*, Ecological Applications 13, 25–31. https://doi.org/10.1890/1051-0761(2003)013[0025:PFTDOM]2.0.CO;2
