# Exact blind locus of a Radau node-deletion error estimator on logistic growth

## Finding
For the two-stage Radau IIA collocation method on the scalar logistic equation \(y'=y(1-y)\), with \(y(0)=a\in(0,1)\), use the normalized collocation nodes \(1/3\) and \(1\). Let \(U_1,U_2\) be a **real** solution of its collocation equations at a positive step \(h\), and consider the deleted-interior-node error signal
\[
\varepsilon=\left|U_1-\frac{2a+U_2}{3}\right|.
\]
Then \(\varepsilon=0\) if and only if \(0<a<1/2\),
\[
h=\frac{12(1-2a)}{(1+2a)(3-2a)},\qquad
U_1=\frac{1+2a}{4},\qquad U_2=\frac{3-2a}{4}.
\]
Thus the **entire non-equilibrium, positive-step zero-signal locus** is explicit. Both stages lie strictly between zero and one. The endpoint error is nevertheless strictly positive:
\[
U_2-\frac{a e^{h}}{1-a+a e^{h}}>0.
\]
Along this locus the endpoint error has sharp supremum \(3/4\), approached as \(a\downarrow0\), although the error signal remains identically zero. At the concrete point \(a=1/6\), \(h=9/4\), the solution \((U_1,U_2)=(1/3,2/3)\) is **the unique collocation-stage solution in \([0,1]^2\)**, so the zero signal is not explained away by selecting a different admissible positive stage root.

## Assumptions and scope
Use exact real arithmetic, the standard two-stage Radau IIA tableau
\[
Q=\begin{pmatrix}5/12&-1/12\\3/4&1/4\end{pmatrix},\qquad c=(1/3,1)^\mathsf T,
\]
and precisely solved nonlinear collocation stage equations
\[
U=a\mathbf 1+hQ\begin{pmatrix}U_1(1-U_1)\\U_2(1-U_2)\end{pmatrix}.
\]
The error indicator deletes the interior stage and interpolates linearly between the initial value and the endpoint, as in the dense-output node-deletion estimator of Saupe (formerly Baumann), Götschel, Lunet, Ruprecht and Speck. The classification concerns **collocation solutions and this indicator**, not guaranteed convergence of a particular nonlinear solver, an arbitrary number of unfinished correction sweeps, or a claim that every adaptive implementation selects this branch. The logistic flow's exact endpoint is \(a e^h/(1-a+a e^h)\).

## Proof
**1. Equivalence between a zero signal and an affine collocation polynomial.** Interpolation through \((0,a),(1/3,U_1),(1,U_2)\) defines the degree-at-most-two collocation polynomial \(p(t)\), with normalized time \(t\in[0,1]\). The indicator is zero precisely when its quadratic coefficient vanishes, that is, when \(p(t)=a+bt\) for \(b=U_2-a\). Collocation then says \(b=h f(U_1)=h f(U_2)\), where \(f(v)=v(1-v)\). Thus \(f(U_1)=f(U_2)\), or equivalently \((U_1-U_2)(1-U_1-U_2)=0\). If \(U_1=U_2\), affineness implies \(b=0\), but this contradicts \(0=b=hf(a)>0\) for \(0<a<1\) and \(h>0\). Hence \(U_1+U_2=1\).

**2. Complete parameterization and converse.** From \(U_1=a+b/3\), \(U_2=a+b\), and \(U_1+U_2=1\), obtain \(b=3(1-2a)/4\), \(U_1=(1+2a)/4\), and \(U_2=(3-2a)/4\). Both stage nonlinearities equal \((1+2a)(3-2a)/16\), which is positive for \(0<a<1\). Therefore \(b=hf(U_1)\) forces the stated \(h\), positive precisely when \(a<1/2\). Conversely those formulas give an affine \(p\) with \(p'(c_j)=hf(p(c_j))\) at both collocation nodes. Integrating its collocation derivative recovers the displayed tableau equations, and \(\varepsilon=0\). This proves the if-and-only-if classification, including real stage roots outside the unit interval.

**3. Strict endpoint error and sharp supremum.** Set \(s=1-2a\in(0,1)\). The endpoint is \(U_2=(2+s)/4\), the initial value is \(a=(1-s)/2\), and \(h=3s/(1-s^2/4)\). Because the exact logistic flow is strictly increasing in elapsed time, the time required to reach \(U_2\) from \(a\) is
\[
H(s)=\log\frac{U_2(1-a)}{a(1-U_2)}
=2\operatorname{artanh}(s)+2\operatorname{artanh}(s/2).
\]
For \(0<s<1\), both power series converge absolutely. The coefficient of \(s^{2j+1}\) in \(H\) is \(2(1+2^{-(2j+1)})/(2j+1)\), and in \(h\) it is \(3/4^j\). These coefficients agree for \(j=0,1\); for every \(j\ge2\), the first is greater because \(2\,4^j>3(2j+1)\). The last inequality holds at \(j=2\) and persists under induction after multiplication by four. Hence \(H(s)>h(s)\), proving \(U_2>y(h)\). Since \(0<y(h)<U_2<3/4\), the error is less than \(3/4\). As \(s\uparrow1\), one has \(a\downarrow0\), \(h\to4\), \(y(h)\to0\), and \(U_2\to3/4\). Therefore the supremum is exactly \(3/4\) and is not attained for \(a>0\).

**4. Uniqueness of the all-positive stage root at a rational witness.** For \(a=1/6\) and \(h=9/4\), clearing denominators from the two stage equations gives
\[
45x^2+3x-9y^2+9y-8=0,\qquad
81x^2-81x+27y^2+21y-8=0.
\]
Eliminating \(y\) gives, up to a nonzero constant,
\[
(3x-1)(81x^3-27x^2-26x-8)=0.
\]
If \(x,y\in[0,1]\), the first tableau equation implies
\[
0\le x\le\frac16+\frac{15}{64}=\frac{77}{192}.
\]
For this entire interval \(81x^2<26\), so the cubic factor is strictly negative. Necessarily \(x=1/3\). Substitution into both equations gives uniquely \(y=2/3\), which indeed solves them. Therefore the stated stages are the only physically bounded collocation stages at this rational test point.

## Verification
The standalone `verify.py` uses exact SymPy arithmetic to check the tableau identities, polynomial derivative, zero indicator, exact resultant factorization, and the rational witness; it checks the coefficient inequality on an initial finite range and samples the strict endpoint inequality at 70-digit precision. It reports 129 passing assertions. The universal coefficient comparison is established by the induction in the proof rather than by finite sampling. Run from the package directory with `python verify.py` (Python 3, SymPy and mpmath required). The numerical samples do not certify all real parameters.

## Relationship to prior work
Saupe (formerly Baumann), Götschel, Lunet, Ruprecht and Speck (arXiv:2403.13454, initially public 2024-03-20) introduce a generic SDC step-size controller using an interior-stage deletion and polynomial interpolation; their Section 2.2 specifies the estimator and notes that choosing the deletion node merits further investigation. The present theorem evaluates exactly its first nontrivial right-Radau instance on an autonomous nonlinear scalar test equation and proves a complete zero-indicator family with a sharp nonzero endpoint-error supremum. The result is not a general objection to embedded estimators or to SDC convergence.

Aves, Griffiths and Higham (1997) study error control and spurious discrete equilibria, a broader related phenomenon. Their abstract does not state this nonlinear right-Radau stage-deletion classification. Related exact error-estimator resonances for classical Fehlberg formulas and adaptive Simpson quadrature use different schemes and do not imply the specific collocation-stage formulas here. Such antecedents establish that estimator failures in other settings are not new as a concept. Exact publication priority remains subject to further specialist comparison.

## Limitations
No claim is made that a practical SDC iteration, initialized in a prescribed way, will select the zero-signal root in every case; some parameter values admit other collocation roots. The singular limit \(a\downarrow0\) is taken through **positive** initial conditions, not asserted as a unique physical solution at \(a=0\). The sharp \(3/4\) is an absolute one-step endpoint error under the particular normalization \(y'=y(1-y)\), not a universal error bound for other vector fields, node sets, controllers, or inexact solves. This finding provides a counterexample to unconditional reliability of the stated indicator, not a complete adaptive-stability analysis.

## References
1. T. Saupe (previously published as T. Baumann), S. Götschel, T. Lunet, D. Ruprecht, and R. Speck, *Adaptive time step selection for Spectral Deferred Correction*, arXiv:2403.13454, first posted 2024-03-20. https://arxiv.org/abs/2403.13454 ; accessible article HTML: https://arxiv.org/html/2403.13454.
2. M. A. Aves, D. F. Griffiths, and D. J. Higham, *Does Error Control Suppress Spuriosity?*, SIAM J. Numer. Anal. 34 (1997), 756–778, DOI:10.1137/S0036142994276980. https://doi.org/10.1137/S0036142994276980.
3. *An exact error-estimator resonance in the classical Fehlberg RK4(5) pair*, publicly indexed published-finding corpus mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-an-exact-error-estimator-resonance-in-the-classical-fehlberg-rk4--23eb200336ce (related but distinct method).
4. *Degree six is the first exact blind spot of adaptive Simpson's local error test*, publicly indexed published-finding corpus mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-degree-six-is-the-first-exact-blind-spot-of-adaptive-simpson-s-l--5c0302bec012 (different quadrature setting).
