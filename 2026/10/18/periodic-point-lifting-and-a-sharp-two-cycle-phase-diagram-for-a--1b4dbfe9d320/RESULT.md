# Periodic-point lifting and a sharp two-cycle phase diagram for a polynomial modular skew map

## Finding

Consider the three-dimensional polynomial modular map of Zhang, Dong, Zhang and Ding, now with a **fixed** forcing parameter. For every positive integer \(n\), its periodic-point counts obey the exact **skew-fiber factorization**
\[
\#\operatorname{Fix}(T^n)=(a^n-1)(c^n-1)\,\#\operatorname{Fix}(g^n),\qquad g(z)=\{ez+r\}_{\beta},
\]
whenever \(a,c\) are integers at least \(2\) and \(e>1\) is real. The count is **independent of both polynomial coupling coefficients and the positive integral power**. If \(e\) is also an integer at least \(2\), the exact Artin–Mazur zeta function is
\[
\zeta_T(t)=\frac{(1-act)(1-aet)(1-cet)(1-t)}{(1-acet)(1-at)(1-ct)(1-et)}.
\]

There is also a **sharp fixed-point-free, period-two phase diagram** at a nonintegral base expansion. Set \(\beta=1\), assume \(1<e<2\) and \(0<r\le2-e\), and put
\[
L_e=\frac{1+e-e^2}{e+1},\qquad U_e=\frac1{e+1}.
\]
Then \(T\) has no fixed points. Its number of **distinct primitive two-cycles**, counting unordered pairs, is
\[
\boxed{\quad N_2(T)=(a^2-1)(c^2-1)\mathbf1_{\{L_e<r\le U_e\}}.\quad}
\]
The strict lower and closed upper inequalities are essential. For \(1<e<(1+\sqrt5)/2\), the cycle count follows a **zero–positive–zero** pattern as \(r\) traverses \((0,2-e]\); for \((1+\sqrt5)/2\le e<2\), every such positive \(r\) gives the positive count. In the original source's gain example \(a=2\), \(c=3\), \(e=17/10\), with fixed \(r=1/5\), there are exactly \(24\) distinct primitive two-cycles and no fixed points, regardless of \(b,d\) or integral \(\gamma\ge1\). This last statement uses a fixed input, not independently sampled noise.

## Assumptions and scope

Write \(\{u\}_{\beta}=u-\beta\lfloor u/\beta\rfloor\in[0,\beta)\) for the half-open remainder of a real number. Fix \(\beta>0\), integer \(a,c\ge2\), real \(b,d,r\), real \(e>1\), and integer \(\gamma\ge1\). The autonomous map \(T:[0,\beta)^3\to[0,\beta)^3\) is
\[
T(x,y,z)=\bigl(\{ax+by^\gamma\}_{\beta},\{cy+dz^\gamma\}_{\beta},\{ez+r\}_{\beta}\bigr).
\]
\(\operatorname{Fix}(S^n)\) means **points** fixed by the \(n\)-th iterate, not primitive orbits; the latter count is half the period-two point count when no fixed point exists. All periodic points are counted with the stated half-open boundary convention. The polynomial coupling is evaluated on real representatives before each remainder, so the system is not assumed to define a continuous torus endomorphism. The scalar base map is \(g(z)=\{ez+r\}_{\beta}\).

## Proof

**Lemma (integer fiber of arbitrary phase).** For every integer \(m\ge2\), every real phase \(s\), and \(\beta>0\), the equation
\[
u=\{mu+s\}_{\beta},\qquad 0\le u<\beta
\]
has exactly \(m-1\) solutions. Indeed, the equation is equivalent to \((m-1)u=k\beta-s\) for an integer \(k\) satisfying \(s/\beta\le k<s/\beta+m-1\). A half-open interval of integer length \(m-1\) contains exactly \(m-1\) integers. This remains true if any solution lies precisely at the chosen boundary.

**Lifting an arbitrary base-periodic point.** Fix \(n\ge1\) and \(z_0\in\operatorname{Fix}(g^n)\), with its prescribed cyclic orbit \(z_0,\ldots,z_{n-1}\). Since \(c\) is an integer, remainders can be composed through multiplication by \(c\). Thus, for this fixed base orbit, the \(n\)-fold second-coordinate map is
\[
y\longmapsto\left\{c^ny+d\sum_{j=0}^{n-1}c^{n-1-j}z_j^\gamma\right\}_{\beta}.
\]
The lemma gives exactly \(c^n-1\) choices of \(y_0\) fixed after \(n\) steps. Each choice uniquely determines the whole \(n\)-step \(y\)-itinerary. With that itinerary fixed, the first coordinate after \(n\) steps is
\[
x\longmapsto\left\{a^nx+b\sum_{j=0}^{n-1}a^{n-1-j}y_j^\gamma\right\}_{\beta}.
\]
The lemma gives \(a^n-1\) choices of \(x_0\). Conversely any \(T^n\)-fixed point projects onto a \(g^n\)-fixed point and must arise from these choices. Different initial triples are different points. Therefore the factorization is exact, including all discontinuity boundaries. Since every iterate of the scalar base has finitely many affine branches of slope \(e^n>1\), it has finitely many periodic points.

**Integer-base zeta.** If \(e\ge2\) is also an integer, the lemma gives \(\#\operatorname{Fix}(g^n)=e^n-1\) for arbitrary \(r\). Expanding the product yields
\[
P_n=(ace)^n-(ac)^n-(ae)^n-(ce)^n+a^n+c^n+e^n-1.
\]
Apply \(\exp(\sum_{n\ge1}\lambda^nt^n/n)=1/(1-\lambda t)\) formally to each term to obtain the displayed rational zeta formula, without any continuity assumption.

**Sharp noninteger-base two-cycle boundary.** Normalize \(\beta=1\), assume \(1<e<2\) and \(0<r\le2-e\). Every branch digit \(k=\lfloor ez+r\rfloor\) is either \(0\) or \(1\). A fixed point with digit zero would have \(z=-r/(e-1)<0\); one with digit one would have \(z=(1-r)/(e-1)\ge1\), using \(r\le2-e\). Thus \(g\) has no fixed point. An orbit of primitive period two must use different branch digits, because two consecutive iterates on the same increasing affine branch would otherwise be a fixed point: solving the two equalities gives a single repeated value. After cyclic reindexing its digits are \(0,1\); write
\[
z_1=ez_0+r,\qquad z_0=ez_1+r-1.
\]
Solving gives the **unique candidate**
\[
z_0=\frac{1-(e+1)r}{e^2-1},\qquad
z_1=\frac{e-(e+1)r}{e^2-1},\qquad
z_1-z_0=\frac1{e+1}>0.
\]
Both states lie in the correct half-open branches precisely when \(z_0\ge0\) and \(z_1<1\); under the standing assumptions the other inequalities then follow automatically. These are equivalent to \(r\le U_e\) and \(r>L_e\), respectively. At \(r=L_e\), the second state would equal \(1\), excluded by the domain; at \(r=U_e\), the first state equals \(0\), included. Hence the scalar map has two points of primitive period two exactly in this region, and none otherwise. The fiber factorization at \(n=2\), together with the absence of fixed points, gives exactly \((a^2-1)(c^2-1)\) **distinct cycles**.

Finally, \(1+e-e^2\) changes sign at \(e=\varphi=(1+\sqrt5)/2\). For \(e<\varphi\), \(0<L_e<U_e<2-e\); for \(e=\varphi\), \(L_e=0\) and \(U_e=2-e\); for \(e>\varphi\), \(L_e<0\) and \(U_e>2-e\). This proves both sides of the golden-ratio parameter transition.

## Verification

The included standalone `verify.py` computes exact rational periodic points for \(a=2\), \(c=3\), \(e=17/10\), \(b=-1/5\), \(d=6/5\), \(r=1/5\), \(\gamma=2\) and \(\beta=1\). It enumerates **all possible scalar digit words of lengths one through four**, reconstructs every periodic fiber point algebraically, and verifies its exact return. The respective three-dimensional point counts are \(0,48,546,7200\). It checks the strict and closed boundaries of the phase diagram at forty rational parameter configurations, the symbolic rational-zeta identity, and thirty-nine integer-base primitive-count divisibility cases. Run in an environment with Python 3 and SymPy using `python3 verify.py`; the recorded execution printed `PASS`. The infinite theorem is proved analytically above; finite checks only detect mistakes in representative algebra and branch handling.

## Relationship to prior work

Zhang, Dong, Zhang and Ding introduced this **specific** polynomial modular skew family as equation (1) and studied triangular Jacobians, Lyapunov exponents, numerical behavior and image encryption. The exact periodic-point factorization, autonomous noninteger-base fixed-point-free two-cycle phase boundary, and integer-base zeta formula are not stated in the inspected sections of their article. Their experiments allow a time-varying random disturbance; that is **not** the fixed \(r\) iteration treated here.

Classical periodic-point formulas for **linear integer toral endomorphisms** (Baake, Lau and Paškūnas) provide a useful analogous product expression, but cannot directly cover arbitrary nonperiodic polynomial couplings on a half-open cube or a noninteger base slope. Scalar generalized beta-transformations and their zeta functions are studied by Suzuki; these do not directly establish the **coupling-independent three-dimensional lift** or the specified additive-shift bifurcation diagram. The argument here is elementary once the correct skew decomposition is recognized; priority beyond the inspected literature remains an open risk, not a certified uniqueness claim.

## Limitations

The result does not assert cryptographic security, stochastic-noise periodicity, topological conjugacy to a toral map, mixing, or stability of the cycles. In the fixed-input regime the source's random disturbance is replaced by a constant. Only integer expanding gains in the two polynomial fibers are covered; a general noninteger \(e\) is allowed for factorization, but the closed zeta formula requires integer \(e\). The two-cycle phase diagram assumes \(\beta=1\), \(1<e<2\), and \(0<r\le2-e\); it does not classify other shifts or all higher periods of the noninteger scalar base. The numerical evidence is not a proof of completeness: completeness follows from the scalar lemma and digit inequalities. Independent scrutiny of novelty and proof has not been performed.

## References

1. Y. Zhang, W. Dong, J. Zhang and Q. Ding, *An Image Encryption Transmission Scheme Based on a Polynomial Chaotic Map*, Entropy **25** (2023), 1005, DOI: 10.3390/e25071005, first public date 2023-06-29. Equation (1), Section 2.
2. M. Baake, E. Lau and V. Paškūnas, *A note on the dynamical zeta function of general toral endomorphisms*, arXiv:0810.1855 (2008).
3. S. Suzuki, *Artin-Mazur zeta functions of generalized beta-transformations*, Kyushu J. Math. **71** (2017), 85–103, DOI: 10.2206/kyushujm.71.85; accessible 2017 dissertation version, DOI: 10.18910/61509.
