# Sharp size-dependent onset of calorimetric peaks in minimal confined run-and-tumble chains

## Finding

The excess-heat capacity of a two- or three-site, single-particle, reflecting run-and-tumble Markov chain is an explicit positive rational function of the tumbling rate. A genuine interior calorimetric maximum occurs if and only if the dimensionless drive \(q=\exp(f/(2T))\) exceeds a model-size-specific sharp threshold. The threshold is strictly lower on three sites than on two sites. In the intervening drive regime the three-site chain has one unique finite-tumbling maximum, whereas the two-site chain has none.

For the two-site chain the threshold and optimizing rate are
\[
q_{2,c}=\sqrt{5+2\sqrt6},\qquad
\alpha_{2,*}=\frac{q^4-10q^2+1}{4q(q^2+1)}\quad(q>q_{2,c}).
\]
For the three-site chain, put
\[
z_*=(7+\sqrt{889})/6,\qquad q_{3,c}=\sqrt{(z_*+\sqrt{z_*^2-4})/2}.
\]
Then \(q_{3,c}=2.44304524035970\ldots<q_{2,c}=3.14626436994197\ldots\), and its optimizer is the unique positive root of the explicit quadratic \(H_q(\alpha)\) below. Equivalently the threshold values of \(f/T\) are \(1.78649062093337\ldots\) for three sites and \(2.29243166956117\ldots\) for two sites. At each threshold the response is strictly decreasing for all positive tumbling rates; the maximum then lies only at the excluded zero-rate boundary.

## Assumptions and scope

Fix \(f>0\), \(T>0\), and \(\alpha>0\), and consider either \(m=2\) or \(m=3\). The continuous-time chain has states \((j,\sigma)\) with \(j\in\{0,\ldots,m-1\}\) and \(\sigma\in\{-1,1\}\). Orientation flips at rate \(\alpha\). A permitted nearest-neighbor step by \(\delta\in\{-1,1\}\), leaving the reflecting channel, is suppressed; otherwise its rate is \(q^{\sigma\delta}\), where \(q=e^{f/(2T)}>1\). The microscopic hop prefactor is fixed to one, independent of temperature, and the internal orientation flips exchange zero bath heat. The heat delivered to the bath per permitted step is \(f\sigma\delta\), so the instantaneous conditional bath heat current is \(h(j,\sigma)=f\sum_{\delta\text{ permitted}}q^{\sigma\delta}\sigma\delta\).

Let \(G\) be the row generator and \(\pi_T\) its unique stationary row vector. Define the zero-mean quasipotential \(w_T\) by \(G w_T=-(h-\pi_T h\,\mathbf1)\) and \(\pi_Tw_T=0\). The nonequilibrium heat capacity, with the conventional sign for bath-released excess heat, is
\[
C_m(T,\alpha)=\left(\frac{d\pi_T}{dT}\right)w_T.
\]
Indeed, following a positive infinitesimal temperature step \(dT\), the time-integrated transient excess heat delivered to the bath is \(-C_m\,dT+o(dT)\). Rates \(\alpha\) and \(f\) are held fixed in this derivative. Define the dimensionless scaled capacity \(E_m(q,\alpha)=2T^2 C_m/f^2\). No claim is made about longer lattices, temperature-dependent kinetic prefactors, interactions, or zero tumbling rate.

## Proof

Reflection \((j,\sigma)\mapsto(m-1-j,-\sigma)\) reduces the two-site chain to boundary orientations outward/inward, denoted \(A,B\), and the three-site chain to outward boundary \(A\), inward boundary \(B\), and center \(C\). These are strongly lumpable because every state in each orbit has the same aggregate transition rates to each orbit, and the heat current is reflection invariant.

In this orbit order, the reduced row generators are
\[
G_2=\begin{pmatrix}-(\alpha+q^{-1})&\alpha+q^{-1}\\\alpha+q&-(\alpha+q)\end{pmatrix},
\quad
G_3=\begin{pmatrix}
-(\alpha+q^{-1})&\alpha&q^{-1}\\
\alpha&-(\alpha+q)&q\\
q&q^{-1}&-(q+q^{-1})
\end{pmatrix}.
\]
Their heat-current vectors divided by \(f\) are respectively \((-q^{-1},q)\) and \((-q^{-1},q,q-q^{-1})\). For two sites, the stationary outward weight is \(q(\alpha+q)/(2\alpha q+q^2+1)\); the other weight is its complement. For three sites, write \(P=3q(q^2+1)\), \(Q=q^4+q^2+1\), \(Z=P\alpha+Q\). The stationary orbit weights are
\[
\rho_A=\frac{q(\alpha q^2+\alpha+q^3)}Z,\quad
\rho_B=\frac{\alpha q^3+\alpha q+1}Z,\quad
\rho_C=\frac{q(\alpha q^2+\alpha+q)}Z.
\]
All weights are strictly positive, and direct substitution verifies \(\rho G=0\), \(\sum\rho=1\).

Writing \(h=f h_0\), the Poisson solution \(w=f w_0\) and \(dq/dT=-fq/(2T^2)\) yield
\[
E_m(q,\alpha)=-q\,(\partial_q\rho)\cdot w_0,
\quad G_m w_0=-(h_0-\rho h_0\,\mathbf1),\quad\rho w_0=0.
\]
Solving these two- and three-dimensional systems by elimination gives the exact closed forms
\[
E_2(q,\alpha)=\frac{q(q^2+1)[\alpha(q^2+1)+2q]}{[2\alpha q+q^2+1]^3},
\]
\[
E_3(q,\alpha)=\frac{q[A(q)\alpha^2+B(q)\alpha+C(q)]}{[P(q)\alpha+Q(q)]^3},
\]
with
\[
\begin{aligned}
A(q)&=q(q^2-1)^2(q^4+6q^2+1),\\
B(q)&=3q^{10}+14q^8+19q^6+19q^4+14q^2+3,\\
C(q)&=2q(q^8+5q^6+6q^4+5q^2+1).
\end{aligned}
\]
Each expression is strictly positive for \(q>1,\alpha>0\).

Differentiation in the tumbling rate gives
\[
\partial_\alpha E_2=
\frac{q(q^2+1)[q^4-10q^2+1-4\alpha q(q^2+1)]}{[2\alpha q+q^2+1]^4}.
\]
For \(q>1\), the zero-rate derivative becomes positive precisely when \(q>q_{2,c}\). Its numerator decreases strictly in \(\alpha\), proving both the no-maximum regime and unique global maximum formula; \(E_2\to0\) as \(\alpha\to\infty\).

For three sites let
\[
H_q(\alpha)=-AP\alpha^2+2(AQ-PB)\alpha+(BQ-3PC),
\qquad \partial_\alpha E_3=\frac{qH_q(\alpha)}{(P\alpha+Q)^4}.
\]
Straight polynomial multiplication yields the two useful factorizations
\[
AQ-PB=-2q(4q^{12}+23q^{10}+52q^8+58q^6+52q^4+23q^2+4)<0,
\]
\[
BQ-3PC=(q^2+1)(q^4+q^2+1)
(3q^8-7q^6-64q^4-7q^2+3).
\]
When \(q>1\), \(A,P>0\), so \(H_q\) is strictly decreasing on \([0,\infty)\). Its sign at the origin is that of \(K(t)=3t^4-7t^3-64t^2-7t+3\) at \(t=q^2>1\). Setting \(z=t+t^{-1}>2\),
\[
K(t)/t^2=3z^2-7z-70.
\]
This is strictly increasing on \(z>2\) and has the sole zero \(z_*=(7+\sqrt{889})/6\), hence the claimed unique threshold \(q_{3,c}\). Below and at it, \(H_q(\alpha)<0\) for every positive \(\alpha\). Above it, \(H_q\) starts positive, crosses zero exactly once, then remains negative; \(E_3\to0\) as \(\alpha\to\infty\), so that crossing is the unique global maximum. Finally, \(K(1)<0\) and \(K(6)>0\) imply \(q_{3,c}^2<6\), while \(q_{2,c}^2=5+2\sqrt6>6\). This proves the strict two-size separation.

## Verification

The standalone `verify.py` builds the complete four-state and six-state row generators independently of orbit lumping. Exact symbolic linear algebra reconstructs both stationary distributions, solves each centered heat Poisson equation, verifies the rational capacity formulas, and checks both tumbling-derivative factorizations. Ten independent small temperature perturbations (five parameter pairs at each size) compare the formula with direct stationary/Poisson finite differences and separately with numerical integration of the transient heat current using full-generator matrix exponentials. The ten tested response values agree within the specified relative/absolute tolerances; these numerical checks corroborate, but do not replace, the exact finite-state proof. Reproduce with `python verify.py` using Python, SymPy, NumPy, and SciPy.

## Relationship to prior work

Santra (2026) establishes calorimetric maxima associated with shape transitions in confined lattice run-and-tumble particles and highlights the effect of kinetic prefactors. That broad observation is prior work. The present contribution is the sharp, size-dependent minimal-chain criterion and its exact positivity/uniqueness classification, for the explicitly fixed unit kinetic prefactor. Dolai, Maes, and Netočný (2023) develop active-particle calorimetry, mostly for continuous-space potential models; Khodabandehlou and Maes (2023) give a general finite-state Drazin-inverse method for ring walks. Their general framework underlies the Poisson equation here, but the stated explicit two- versus three-site drive thresholds were not identified in the inspected material. The full 2026 Santra manuscript could not be inspected; its possible explicit treatment of the same small chains remains an originality risk, not a claim of noncoverage.

## Limitations

The theorem treats only two and three sites with one particle, symmetric reflecting endpoints, temperature-independent hop prefactor one, local-detailed-balance exponential hop rates, and orientation flips at constant temperature-independent rate. The peak is a function of the tumbling rate at fixed drive and temperature, not a temperature peak. Neither the comparison nor the positivity law is asserted for other rate prefactors, lattice lengths, interactions, or nontrivial onsite potentials. The active-drive threshold is not a thermodynamic phase transition, and finite numerical checks do not certify infinite-system behavior. Novelty remains provisional pending full-text comparison with Santra (2026) and independent review.

## References

1. Ion Santra, *Heat capacity as a marker for shape and jamming transitions in active systems*, arXiv:2608.17903v1 (first public 2026-08-18).
2. Pritha Dolai, Christian Maes, Karel Netočný, *Calorimetry for active systems*, SciPost Physics 14, 126 (2023), DOI:10.21468/SciPostPhys.14.5.126.
3. Faezeh Khodabandehlou, Irene Maes, *Drazin-inverse and heat capacity for driven random walkers on the ring*, Stochastic Processes and their Applications 164, 337–356 (2023), arXiv:2204.04974.
