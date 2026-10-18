# A sharp density-controlled rectification boundary in a four-site disordered exclusion chain

## Finding
Consider the four-site boundary-driven exclusion process specified below. Let \(J(u,v)\) denote its stationary left-to-right particle current when the reservoir occupancies are \(u\) and \(v\). At contrast \(d=u-v>0\) and mean occupancy \(\rho=(u+v)/2\), put
\[
E(\rho,d)=J(\rho+d/2,\rho-d/2)+J(\rho-d/2,\rho+d/2).
\]
This even-in-drive response measures rectification: it is zero when reversing the reservoirs exactly reverses the current. Let
\[
\begin{aligned}
Q(d)={}&413067648d^6+18917449838d^5+324236281277d^4\\
&+2454897307300d^3+6770005929628d^2\\
&-1324169822640d-8093326579200.
\end{aligned}
\]
There is exactly one root \(d_c\) of \(Q\) in \((0,1)\), with \(0.992760<d_c<0.992763\). For every \(0<d<d_c\) there is exactly one mean density \(\rho_c(d)\) in \((d/2,1-d/2)\) such that
\[
 E(\rho,d)<0\quad(d/2\leq\rho<\rho_c(d)),\qquad
 E(\rho,d)>0\quad(\rho_c(d)<\rho\leq 1-d/2).
\]
At \(d=d_c\), the even response vanishes only at the lower boundary \(\rho=d/2\), and is strictly positive at every other admissible density. For \(d_c<d\leq1\), the even response is strictly positive at every admissible density, including the unique density \(\rho=1/2\) when \(d=1\). This completely classifies the rectification sign on the physical two-parameter reservoir square for the stated four-site sample.

## Assumptions and scope
The state space is \(\{0,1\}^4\), with at most one particle per site. Site departure rates, from left to right, are
\[
(r_1,r_2,r_3,r_4)=(1,1/4,1/2,1).
\]
Across neighboring sites, an occupied site \(i\) sends its particle to a vacant site \(i+1\) at rate \(r_i\), and conversely at rate \(r_{i+1}\) if that is occupied and \(i\) is empty. The left boundary site flips from empty to occupied at rate \(u\), and from occupied to empty at rate \(1-u\); the right boundary flips at rates \(v\) and \(1-v\), respectively. Here \(u,v\in[0,1]\). The stationary current is the net flux across the bond between sites 2 and 3. For all \(u,v\) the finite continuous-time Markov process has a unique stationary law; including boundary values follows from transitions at the opposite boundary and internal transport. We consider \(d\in(0,1]\) and \(\rho\in[d/2,1-d/2]\); the zero-contrast case \(d=0\) is excluded from sign statements because then \(E=0\) identically.

## Proof
**1. An exact rational current.** Index binary configurations by \(0,\ldots,15\), with the \(i\)-th binary digit recording the occupancy at site \(i+1\). For every transition from configuration \(x\) to \(y\) at the rate above, write \(L_{yx}\) for its rate and set each diagonal entry to minus the total outgoing rate. Replace the last row of \(L\) with a row of ones; solving this rational linear system with right side zero except for last entry one gives the stationary vector. Its expected site-2-to-site-3 current simplifies *exactly* to
\[
J(u,v)=\frac{(u-v)P(u,v)}{D(u,v)}.
\]
The complete integer coefficients of \(P,D\) are supplied as `P_terms` and `D_terms` in `polynomial_certificate.json`, indexed by powers of \((u,v)\). Their identity with the actual finite-state generator is checked by `verify.py`. Importantly, \(D(u,v)>0\) throughout the closed unit square. Every coefficient of \(D\) is positive except \(-6912u^3v^3\) and \(-23328u^2v^3\), both absorbed by its term \(+651144u^2v^2\) since \(651144-6912uv-23328v>0\) when \(0\leq u,v\leq1\). The remaining constant term is positive. Similarly, the only negative term in \(P\) is \(-3408u^2v^2\), overwhelmed by \(+47258u^2v\), so \(P>0\). The forward flux consequently has the correct sign for all unequal reservoirs.

**2. Polynomial governing rectification.** Set \(U=\rho+d/2\), \(V=\rho-d/2\). Then the *exact algebraic identity* is
\[
E(\rho,d)=\frac{-4d^2F(\rho,d)}{D(U,V)D(V,U)},\qquad
F(\rho,d)=-\frac{P(U,V)D(V,U)-P(V,U)D(U,V)}{4d}.
\]
The apparent quotient by \(d\) is a polynomial; its full rational coefficients appear as `F_terms` in the accompanying certificate and are reconstructed from the generator in `verify.py`. Because both denominators are strictly positive, the sign of \(E\) for \(d>0\) is the opposite of the sign of \(F\).

**3. A uniform exact root count across all densities.** For \(0<d<1\), make the bijective coordinate change
\[
t=\frac{\rho-d/2}{1-d/2-\rho},\qquad
\rho=\frac{d/2+(1-d/2)t}{1+t}.
\]
The lower reservoir-density endpoint corresponds to \(t=0\); interior densities to \(0<t<\infty\), and the upper endpoint to \(t=\infty\). Multiplying by the positive denominator yields the degree-nine polynomial
\[
H_d(t)=(1+t)^9F\!\left(\frac{d/2+(1-d/2)t}{1+t},d\right)
=\sum_{k=0}^9c_k(d)t^k.
\]
All coefficients are specified exactly in `H_t_coefficients` of `polynomial_certificate.json` and verified directly from \(F\). For \(k=9,8,7,6\), one has \(c_k(d)<0\) for every \(0<d<1\). For each \(k=5,4,3,2,1,0\), the polynomial \(c_k\) is positive for \(0<d<\theta_k\) and negative for \(\theta_k<d<1\), where its unique zero \(\theta_k\in(0,1)\) is bracketed by
\[
\begin{array}{c|cccccc}
k&5&4&3&2&1&0\\\hline
10^6\theta_k\ \text{lies between}&930915,930917&974592,974595&984394,984397&988735,988738&991185,991189&992760,992763
\end{array}
\]
(the endpoints in the displayed brackets are **integers**, and the claimed interval divides each by \(10^6\)). These sign assertions are exact, not numerical observations: for each univariate polynomial \(c_k(d)\) of degree \(m\), transform it to
\[
B_k(z)=(1+z)^m c_k\!\left(\frac{z}{1+z}\right).
\]
For \(k\geq6\), every coefficient of \(B_k\) is negative. For \(k\leq5\), the coefficient list of \(B_k\) has exactly **one** sign change, while \(c_k(0)>0>c_k(1)\). Descartes' rule, continuity and the exact rational endpoint evaluations give exactly one zero in \((0,1)\) in the listed interval. The computational certificate independently reconstructs the coefficients and checks each of these finite rational sign tests. In particular, the thresholds are strictly ordered
\[
\theta_5<\theta_4<\theta_3<\theta_2<\theta_1<\theta_0.
\]
The constant coefficient is \(c_0(d)=-Q(d)/2\). Thus \(d_c=\theta_0\), and for every \(0<d<d_c\), the nonzero coefficients of \(H_d\), ordered from highest power to constant, exhibit exactly **one** sign change: negative high-order coefficients followed by positive lower-order ones. Since \(H_d(0)=c_0(d)>0\) and its leading coefficient is negative, Descartes' rule gives exactly one positive zero, necessarily crossing from positive to negative. Recalling the negative prefactor in \(E\), the specified signs and the unique \(\rho_c(d)\) follow. If \(d=d_c\), then \(c_0=0\) and every other coefficient is negative; the zero is only at \(t=0\). If \(d_c<d<1\), every coefficient is strictly negative and there is no zero anywhere on the density interval.

**4. The degenerate contrast endpoint.** When \(d=1\), the only possible pair of reservoirs is \((u,v)=(1,0)\), with reversed pair \((0,1)\). Direct substitution into the exact current gives
\[
E(1/2,1)=J(1,0)+J(0,1)=\frac{3246744814}{54087920537585}>0,
\]
completing the closed-parameter-boundary cases.

## Verification
With Python 3 and SymPy, run `python verify.py` in the directory containing both `verify.py` and `polynomial_certificate.json`. The script reconstructs the entire sixteen-state generator, solves the stationary linear equations exactly, asserts that its current equals the rational-polynomial expression, derives \(F\) and the nine-degree polynomial \(H_d\), checks the closed-form critical polynomial, evaluates all Descartes sign tests and exact rational threshold brackets, and checks the maximal-contrast endpoint. A second stationary calculation uses a separately implemented Gaussian elimination over Python's `fractions.Fraction` on five explicit rational reservoir pairs; it agrees with the symbolic current. The certificate JSON is a complete human-readable list of polynomial coefficients; no external files or precomputed logs are required. These finite integer-sign certificates substantiate the infinite-range sign classification because Descartes' rule applies to all positive real \(t\).

## Relationship to prior work
Sakai and Akimoto's September 2026 study introduces the boundary-driven disordered exclusion process, reports sample-dependent rectification, and develops approximations and finite numerical examples. Its framework motivates resolving rectification as a function of both reservoir contrast and mean density. Their December 2025 work instead studies a field-driven periodic system, not the open boundary process. An earlier exact investigation of this specific four-site sample established a single rectification zero **along the one-dimensional section of fixed mean occupancy \(\rho=1/2\)**. That section does not determine either the number of zeros on *every vertical mean-density section* at fixed \(d\), or their disappearance at the newly identified contrast \(d_c\). The present result is the full two-parameter sign-phase classification, proved through a joint nine-degree coefficient sign certificate rather than extrapolated from any one-dimensional section. Related finite-state rational approaches and Descartes root counting are standard methods; the model-specific all-parameter theorem and its sharp threshold are the claimed result, not the methods themselves.

## Limitations
The theorem concerns the specified four-site sample, with departure-rate disorder and the explicit boundary rates above; it makes no universal claim for longer chains, other disorder realizations, or different boundary kinetics. It gives the existence and uniqueness of the interior zero curve, not a compact elementary formula for that curve. The critical contrast is defined exactly as the unique root of \(Q\) in \((0,1)\), not by a decimal approximation. Exact rational verification is provided for this finite Markov model; it is not an independent external audit. Unindexed or implicit earlier coverage cannot be ruled out solely by search results.

## References
- I. Sakai and T. Akimoto, *Sample-specific rectification-like response in a boundary-driven exclusion process*, arXiv:2609.03560v1 (first public release 2026-09-03).
- I. Sakai and T. Akimoto, *Symmetry Breaking of Current Response in Disordered Exclusion Processes*, arXiv:2512.03316v1 (first public release 2025-12-03).
- `polynomial_certificate.json` and `verify.py`, exact standalone algebraic data and reproduction code accompanying this result.
