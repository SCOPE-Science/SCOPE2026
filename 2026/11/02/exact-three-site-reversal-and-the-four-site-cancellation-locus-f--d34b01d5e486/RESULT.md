# Exact three-site reversal and the four-site cancellation locus for site-trap exclusion currents

## Finding

For the continuous-time site-trap asymmetric simple exclusion process on a simple periodic ring, the first ring size that permits bias rectification is four. Every three-site ring has an exactly odd stationary current at all particle numbers and all positive site rates, even when its spatial profile lacks reflection symmetry. In the one-vacancy sector of a four-site ring, a complete all-bias criterion identifies three and only three algebraic hypersurfaces of exact current-reversal symmetry, including an alternating-sum cancellation not requiring spatial reflection.

Write the four positive departure rates in cyclic order as \(a,b,c,d\), and the right/left hopping probabilities as \(p=(1+\varepsilon)/2\) and \(q=(1-\varepsilon)/2\). Put
\[
X=a+c,\quad Y=b+d,\quad U=a-c,\quad V=b-d,
\]
\[
A(\varepsilon)=XY(X+Y)(1+\varepsilon^2)-2\varepsilon^2(U^2Y+V^2X),
\quad K=UV(X-Y).
\]
For three particles on four sites, the stationary particle current through each oriented bond is exactly
\[
J_3(\varepsilon)=\frac{4abcd\,\varepsilon(1+\varepsilon^2)}{A(\varepsilon)+\varepsilon(1-\varepsilon^2)K},\qquad -1<\varepsilon<1.
\]
Its even-in-bias component is
\[
\frac{J_3(\varepsilon)+J_3(-\varepsilon)}2
=-\frac{4abcd\,\varepsilon^2(1-\varepsilon^2)(1+\varepsilon^2)K}
{A(\varepsilon)^2-\varepsilon^2(1-\varepsilon^2)^2K^2}.
\]
Consequently the current obeys \(J_3(\varepsilon)=-J_3(-\varepsilon)\) for every \(|\varepsilon|<1\) **if and only if**
\[
(a-c)(b-d)(a+c-b-d)=0.
\]
If that product is nonzero, rectification is nonzero for **every** \(0<|\varepsilon|<1\). Its weak-bias coefficient is exact:
\[
\frac12J_3''(0)=-\frac{4abcd(a-c)(b-d)(a+c-b-d)}{(a+c)^2(b+d)^2(a+b+c+d)^2}.
\]
For three sites, with positive rates \(a,b,c\), the nontrivial currents are instead
\[
J_1(\varepsilon)=\frac{\varepsilon}{a^{-1}+b^{-1}+c^{-1}},\qquad
J_2(\varepsilon)=\frac{abc\,\varepsilon(3+\varepsilon^2)}{(a+b+c)^2-\varepsilon^2\bigl(a^2+b^2+c^2-2ab-2ac-2bc\bigr)}.
\]
Both are odd for all \(|\varepsilon|<1\); empty and full configurations have zero current.

## Assumptions and scope

The sites are \(\mathbb Z/L\mathbb Z\), with \(L\ge3\) so that right- and left-neighbor edges are distinct. An occupied site \(i\) attempts a jump to \(i+1\) at rate \(p w_i\) and to \(i-1\) at rate \(q w_i\), with unsuccessful moves into occupied sites suppressed. All \(w_i\) are strictly positive; \(-1<\varepsilon<1\); and the conserved particle count is \(0\le N\le L\). The field changes only the global right/left fractions \(p,q\), not the departure rates. The invariant distribution within each fixed-particle sector exists and is unique for nontrivial \(N\). The stationary current \(J_N\) is the net oriented jump rate through any fixed bond, not the sum over bonds.

The four-site theorem concerns \(N=3\) (one vacancy); no classification for the other nontrivial four-site particle count is asserted. The three-site minimality statement concerns all particle sectors. The explicit formulas include equilibrium \(\varepsilon=0\), while strict nonzero rectification concerns \(0<|\varepsilon|<1\). No assertion is made about \(|\varepsilon|=1\) as an irreducibility regime.

## Proof

**1. A one-vacancy generator.** For \(N=L-1\), record the location \(i\) of the unique empty site. A particle from \(i+1\) moves left into this vacancy with rate \(q w_{i+1}\), moving the vacancy right, while a particle from \(i-1\) moves right with rate \(p w_{i-1}\), moving the vacancy left. Thus the row generator \(Q\) has
\[
Q_{i,i+1}=q w_{i+1},\qquad Q_{i,i-1}=p w_{i-1},\qquad
Q_{i,i}=-q w_{i+1}-p w_{i-1},
\]
with indices modulo \(L\). These are distinct off-diagonal entries for \(L\ge3\). Positivity of rates ensures irreducibility. By the finite directed matrix-tree theorem, the cofactors
\[
t_i=\det(-Q)_{\widehat i,\widehat i}>0,\qquad S=\sum_i t_i>0
\]
give \(\pi_i=t_i/S\). Across the bond from site zero to site one, a right jump occurs if the vacancy is at site one, and a left jump if it is at site zero. Hence
\[
J_{L-1}(\varepsilon)=\frac{p w_0 t_1-q w_1 t_0}{S}.
\]
This identity derives the current from the actual exclusion generator, rather than treating the vacancy current as the particle current with the same sign.

**2. Three-site sectors.** When \(L=3,N=1\), the full one-particle stationary weights are proportional to \(w_i^{-1}\): the incoming and outgoing flow-balance sums match because \(p+q=1\). Therefore the particle current through any bond is \((p-q)/(a^{-1}+b^{-1}+c^{-1})\). For \(L=3,N=2\), compute the three directed cofactors from the generator above. Direct expansion yields
\[
p a t_1-q b t_0=\frac14abc\,\varepsilon(3+\varepsilon^2),
\]
\[
S=\frac14\left[(a+b+c)^2-\varepsilon^2\bigl(a^2+b^2+c^2-2ab-2ac-2bc\bigr)\right].
\]
Dividing gives the stated \(J_2\). Its denominator is strictly positive for \(|\varepsilon|<1\) because \(S>0\), and both displayed three-site currents are odd. For \(N=0,3\), every transition is blocked. This exhausts the full three-site model.

**3. Four-site one-vacancy formula.** For \(w_0=a,w_1=b,w_2=c,w_3=d\), the corresponding four directed cofactors obey, by direct determinant expansion,
\[
p a t_1-q b t_0=\frac12 abcd\,\varepsilon(1+\varepsilon^2),
\]
\[
S=\frac18\left[XY(X+Y)(1+\varepsilon^2)
-2\varepsilon^2(U^2Y+V^2X)
+\varepsilon(1-\varepsilon^2)UV(X-Y)\right].
\]
Both identities are polynomial identities in the four rates and the field. Their substitution into the current-cofactor quotient yields the stated exact rational formula. The verifier gives independent symbolic expansions of every minor, in addition to separate full-exclusion master-equation checks. As \(S>0\), the denominator \(H(\varepsilon)=8S\) is positive throughout the stated parameter domain.

**4. Symmetry and its sharp onset.** Decompose \(H(\varepsilon)=A(\varepsilon)+B(\varepsilon)\), where \(A\) is even and \(B(\varepsilon)=\varepsilon(1-\varepsilon^2)K\) is odd. The current numerator \(4abcd\,\varepsilon(1+\varepsilon^2)\) is odd. Taking the half-sum at opposite fields therefore gives exactly the displayed even part. Its denominator equals \(H(\varepsilon)H(-\varepsilon)>0\). For \(0<|\varepsilon|<1\), every factor in its numerator is nonzero except possibly \(K\), and the four site rates are positive. This proves the **if and only if** criterion and its strict all-field complement. A Taylor expansion at zero yields the stated half-second-derivative. The three-site exhaustion and a four-site example with \(K\ne0\) prove minimality.

**5. Explicit nonsymmetric witnesses.** The four distinct site rates \((a,b,c,d)=(1,2,4,3)\) satisfy \(a+c=b+d=5\), giving exact reversal symmetry even though both opposite-site differences are nonzero. Conversely, with \((a,b,c,d)=(1,2,3,5)\),
\[
J_3(\varepsilon)=\frac{60\varepsilon(1+\varepsilon^2)}{154-9\varepsilon+90\varepsilon^2+9\varepsilon^3}.
\]
At \(\varepsilon=1/2\) and \(-1/2\), the values are \(60/277\) and \(-300/1439\), respectively, with the nonzero full sum \(3240/398603\). These exact witnesses separate geometric asymmetry from dynamically effective rectification.

## Verification

The standalone file `verify.py` requires Python and `sympy` (version 1.13 or later). Execute `python verify.py` in the directory containing it. The script independently constructs directed vacancy generators, expands their matrix-tree cofactors symbolically, and asserts both cofactor normalization formulas, the odd three-site formulas, the even four-site formula, and the exact second derivative. Separately, it constructs full exclusion generators on occupation configurations, solves exact-rational stationary linear systems at 120 deterministic positive-rate/field samples, and checks predicted currents, normalization, and positivity. It passed 378 exact assertions, including the 120 full-configuration comparisons.

Finite samples do not establish universal quantifiers; the proof above rests on positive matrix-tree weights and symbolic polynomial identities. The symbolic minor identities were independently compared with the full-chain equations and can be reproduced with the included code. No continuum limit, simulation extrapolation, or numerical zero test is used as a proof.

## Relationship to prior work

Sakai and Akimoto's work on current-response symmetry in disordered exclusion processes establishes the physical motivation and discusses bond-versus-site disorder, reflection symmetries, and rectification; it does not, in the inspected full-text sections, state the complete three-site all-sector identity or the exact four-site one-vacancy cancellation criterion. Kehr and Koza derive finite-ring lattice-gas currents, including a different four-site **two-particle** master-equation example. Their general formalism allows finite-state current calculations but does not present the particular sharp four-site **three-particle** factorization. Sakai and Akimoto's subsequent boundary-driven model addresses reservoir-imposed rather than global-bias driving and discusses cancellations without specifying this periodic one-vacancy locus.

The vacancy-to-random-walk reduction, matrix-tree theorem, and rational finite-state current calculations are established tools, **not claimed as new**. The assessed contribution is the complete algebraic classification of field-reversal behavior in the smallest disordered site-trap rings and the hidden alternating-sum symmetry locus. In particular, a general finite-state stationary determinant formula is not, without evaluating and factoring the relevant minors, the explicit cancellation classification.

## Limitations

The result is exact only for site-factorized departure rates and a spatially uniform right/left bias on periodic rings. It excludes zero rates, two-site multigraph conventions, additional interactions, reservoirs, and non-Poisson clocks. The four-site classification is for one vacancy, not for every density. The current at fully directional limiting fields is outside the strict-field criterion. The result makes no thermodynamic-limit prediction. General earlier ring-walk current formulas could support alternate derivations of the factorization, and literature-wide priority has not been independently established.

## References

1. I. Sakai and T. Akimoto, *Symmetry Breaking of Current Response in Disordered Exclusion Processes*, arXiv:2512.03316v1, publicly submitted 2025-12-03, https://arxiv.org/abs/2512.03316 .
2. K. W. Kehr and Z. Koza, *Hopping motion of lattice gases through nonsymmetric potentials under strong bias conditions*, arXiv:cond-mat/9909154, https://arxiv.org/abs/cond-mat/9909154 .
3. I. Sakai and T. Akimoto, *Sample-specific rectification-like response in a boundary-driven exclusion process*, arXiv:2609.03560v1, https://arxiv.org/abs/2609.03560 .
4. The directed finite-state Markov-chain tree theorem (standard result; used solely as the stationary normalization identity).
