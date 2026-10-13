# Two sharp phenotype-extinction switches along pH payoff paths in a four-strategy tumor game

## Finding

Consider the deterministic four-phenotype replicator system specified below. Let the neutral payoff matrix be joined by straight line segments in payoff space to the acidic and pH-buffered payoff matrices printed in Rodrigues (2026). Along **each entire segment**, all solutions starting with four positive phenotype fractions converge to one uniquely determined equilibrium. There is exactly one support change on each segment, and the two changes occur at sharply different fractions of the corresponding environmental shift.

Precisely, let \(p_a(\theta)=\theta^3-2\theta^2+234\theta-60\) and \(p_b(\theta)=41\theta^3-712\theta^2+3201\theta-2520\). Their unique roots in \((0,1)\) are
\[
\tau_a\in(0.256901,0.256902),\qquad
\tau_b\in(0.994745,0.994746).
\]
For the neutral-to-acidic path, all four equilibrium fractions are positive precisely for \(0\le\theta<\tau_a\); for \(\tau_a\le\theta\le1\), the proliferative fraction is exactly zero and the other three are positive. For the neutral-to-buffered path, all four equilibrium fractions are positive precisely for \(0\le\theta<\tau_b\); for \(\tau_b\le\theta\le1\), the resistant fraction is exactly zero and the other three are positive. At both transition points the disappearing type is neutrally invadable at first order, but convergence to the unique boundary equilibrium still holds for every strictly positive initial state.

At the three original payoff matrices, the respective unique interior-attracting equilibria, in phenotype order \((P,I,R,C)\), are
\[
 x^*_{0}=\frac1{1387}(120,360,252,655),\qquad
 x^*_{a}=\frac1{677}(0,250,232,195),\qquad
 x^*_{b}=\frac1{334}(100,49,0,185).
\]
The exact logarithmic exclusion rates at the acidic and buffered endpoints differ strikingly: for every strictly positive initial population,
\[
\lim_{t\to\infty}\frac{\log x_P(t)}{t}=-\frac{173}{3385}
\quad\text{(acidic)},\qquad
\lim_{t\to\infty}\frac{\log x_R(t)}{t}=-\frac1{3340}
\quad\text{(buffered)}.
\]
Their absolute ratio is \(115564/677>170\). The existence of exactly one support transition on each path, with the same identities of disappearing phenotypes, survives sufficiently small changes to the three endpoint matrices.

## Assumptions and scope

The model has fractions \(x=(x_P,x_I,x_R,x_C)\) in the simplex \(\Delta_3=\{x_i\ge0,\ \sum_i x_i=1\}\) and solves
\[
\dot x_i=x_i\big((Ax)_i-x^{\mathsf T}Ax\big),\qquad i\in\{P,I,R,C\}.
\]
The theorem concerns **every** initial state satisfying \(x_i(0)>0\) for all four types; boundary initial states need not be attracted to the same equilibrium because missing strategies cannot reappear. The matrices are those of Rodrigues (2026), written as integer matrices divided by \(100\):
\[
100A_0=\begin{pmatrix}90&90&95&92\\105&85&95&92\\102&100&75&92\\103&104&100&80\end{pmatrix},
\quad100A_a=\begin{pmatrix}88&85&90&88\\110&88&100&90\\105&105&80&92\\100&102&95&78\end{pmatrix},
\]
\[
100A_b=\begin{pmatrix}92&90&95&93\\100&85&90&90\\95&95&75&90\\105&105&100&82\end{pmatrix}.
\]
The interpolation parameter \(\theta\in[0,1]\) is **fixed during any individual trajectory**; the two payoff paths are \(A_a(\theta)=(1-\theta)A_0+\theta A_a\) and \(A_b(\theta)=(1-\theta)A_0+\theta A_b\). These affine segments are mathematical continuations between the three displayed illustrative scenarios, not a fitted physical relation between pH and payoffs. Time is denoted by \(t\), separate from \(\theta\). No noise, mutation, treatment feedback, or other compartments are assumed.

## Proof

**1. Uniform strict stability of the games.** Let \(B=(e_P-e_C,e_I-e_C,e_R-e_C)\); every tangent vector to the simplex is \(Bu\). Define \(H(A)=-B^{\mathsf T}(A+A^{\mathsf T})B/2\). Exact arithmetic gives the three leading principal minors of \(H\):
\[
\begin{array}{c|ccc}
&\det H_1&\det H_2&\det H_3\\\hline
A_0&1/4&451/10000&47263/4000000\\
A_a&11/50&1447/40000&32387/4000000\\
A_b&6/25&1167/40000&911/160000
\end{array}
\]
(all fractions in this array denote ordinary rational numbers). Sylvester's criterion proves positive definiteness at the three endpoints. Since \(H(A_a(\theta))\) and \(H(A_b(\theta))\) are convex combinations of positive definite matrices, they are positive definite for all \(\theta\in[0,1]\). In particular,
\[
 v^{\mathsf T}A_j(\theta)v<0\quad\text{for every nonzero }v\text{ with }\sum_i v_i=0,
\qquad j\in\{a,b\}.
\]

**2. Exact equilibrium branches and support checks.** For the acidic path, write
\[
\begin{aligned}
p_a&=\theta^3-2\theta^2+234\theta-60,\\
D_a&=34\theta^3-186\theta^2+2173\theta-13870,\\
N_a&=\big(20p_a,\;-10(\theta+2)(2\theta^2-37\theta+180),\\
&\hspace{18mm}-2(3\theta^3+113\theta^2+1196\theta+1260),\;5(8\theta^3-50\theta^2+189\theta-1310)\big).
\end{aligned}
\]
The normalized all-strategy equal-fitness solution is \(N_a/D_a\). The normalized equal-fitness solution on the face \(P=0\) is
\[
 x_{a,F}(\theta)=\frac{\big(0,\;-10(2\theta^2-\theta+24),\;2(5\theta^2-31\theta-90),\;5(4\theta^2+48\theta-91)\big)}{q_a(\theta)},
\quad q_a=10\theta^2+188\theta-875.
\]
At this face solution, the absent-type invasion excess fitness is exactly
\[
(A_a(\theta)x_{a,F})_P-x_{a,F}^{\mathsf T}A_a(\theta)x_{a,F}=\frac{p_a(\theta)}{5q_a(\theta)}.
\]
On the full interval \([0,1]\), \(D_a<0\), \(q_a<0\), the three all-strategy numerator components other than \(P\) are negative, and the three active face numerator components are negative. Moreover \(p_a(0)=-60\), \(p_a(1)=173\), and \(p_a'=3\theta^2-4\theta+234>0\). Thus \(N_a/D_a\) is a positive four-type state precisely before the unique root \(\tau_a\); at and beyond that root, \(x_{a,F}\) is a feasible equilibrium and its absent-type invasion excess is nonpositive.

For the buffered path, similarly put
\[
\begin{aligned}
p_b&=41\theta^3-712\theta^2+3201\theta-2520,\\
D_b&=31\theta^3-1382\theta^2+7871\theta-13870,\\
N_b&=\big(-5(2\theta^3-115\theta^2+313\theta+240),\\
&\hspace{18mm}5(9\theta^3-193\theta^2+687\theta-720),\;p_b,\;-5(9\theta^3+56\theta^2-560\theta+1310)\big).
\end{aligned}
\]
The all-strategy normalized equal-fitness solution is \(N_b/D_b\). The equal-fitness solution on \(R=0\) is
\[
 x_{b,F}(\theta)=\frac{\big(3\theta^2+37\theta+60,\;7\theta^2-138\theta+180,\;0,\;-7\theta^2-83\theta+275\big)}{q_b(\theta)},
\quad q_b=3\theta^2-184\theta+515.
\]
Its absent-type invasion excess is
\[
(A_b(\theta)x_{b,F})_R-x_{b,F}^{\mathsf T}A_b(\theta)x_{b,F}=-\frac{p_b(\theta)}{100q_b(\theta)}.
\]
Here \(D_b<0\), \(q_b>0\), all other all-strategy numerators are negative, and all three active face numerators are positive on \([0,1]\). Since \(p_b(0)=-2520\), \(p_b(1)=10\), and \(p_b'=123\theta^2-1424\theta+3201>0\), the same reasoning gives precisely one resistance-support transition at \(\tau_b\). Equal-fitness normalization and the invasion excess identities are **polynomial identities**, checked by the accompanying exact-rational program, not approximate trajectories. The certified root brackets follow by exact substitution into the two strictly increasing cubics.

**3. Convergence from every strictly positive state.** In both paths and on both sides of the respective transition, denote by \(x^*\) the feasible candidate from Step 2. Each active type has equal fitness \(\lambda=x^{*\mathsf T}Ax^*\), and every absent type has fitness at most \(\lambda\). Thus \((x-x^*)^{\mathsf T}Ax^*\le0\) for all \(x\in\Delta_3\). For a positive solution define the relative-entropy function
\[
V(x)=\sum_{i:x_i^*>0}x_i^*\log\frac{x_i^*}{x_i}\ge0.
\]
Direct differentiation along the replicator flow yields
\[
\dot V=(x-x^*)^{\mathsf T}A(x-x^*)+(x-x^*)^{\mathsf T}Ax^*<0
\quad\text{for }x\ne x^*.
\]
Strict negative tangential definiteness is from Step 1. The sublevel set of \(V\) reached by an interior initial condition keeps all types in the support of \(x^*\) bounded away from zero. It is compact and positively invariant within the simplex. Standard Lyapunov invariance (or integration of the strict quadratic bound followed by uniform continuity) therefore proves \(x(t)\to x^*\). The same strict inequality rules out any second feasible equilibrium attracting interior points, and actually implies uniqueness of the simplex Nash equilibrium: two such equilibria would contradict strict negative tangential definiteness by adding their two variational inequalities.

**4. Endpoint exclusion clocks and robust support changes.** At the acidic endpoint, the missing-type invasion excess evaluated in Step 2 is \(-173/3385\); at the buffered endpoint, it is \(-1/3340\). When \(x_i(0)>0\), integrating \(d\log x_i/dt=(Ax)_i-x^{\mathsf T}Ax\), using Step 3, and taking Cesàro limits proves the asserted logarithmic rates. Finally, positive definiteness is uniform over each compact parameter path; all nontarget support fractions are bounded away from zero, the two cubic roots are simple, and absent-type invasion fitness is strictly negative beyond each root. Continuity of the active-set solutions and the implicit-function theorem show that the unique support changes remain under sufficiently small endpoint-matrix perturbations, with perturbed threshold positions and unchanged identities of the extinct types.

## Verification

Run `python3 verify.py` with Python 3's standard library; expected final line is `VERIFY_OK`. It uses rational polynomial arithmetic to check all three Sylvester-minor triplets, exact normalization and equal-fitness identities for both full-support and face branches, the two invasion-fitness identities, strict signs of all required active numerators/denominators on \([0,1]\) through positive Bernstein coefficients, monotonicity of both threshold cubics, and exact rational root-bracket tests. The checker was run against this file package and returned `VERIFY_OK`.

The mathematical conclusion is global in continuous time and does not rest on numerical integration or finite enumeration. The code checks the finite exact polynomial certificates, while the convergence, uniqueness, and perturbation steps are justified analytically in the proof.

## Relationship to prior work

Rodrigues (2026) introduced the particular four-phenotype payoff matrices, reported numerical trajectories for neutral, acidic, and buffered scenarios, and provided general two- and three-strategy reduction formulas in its Appendix A. The present result gives a distinct exact two-path support phase diagram: the specific cubic transition locations, entire-path global convergence, and highly unequal asymptotic endpoint extinction exponents are not stated there. The matrices and the ecological motivation are **not** claimed as new. The same author's 2025 paper treats two metabolic phenotypes and different \(2\times2\) matrices, so its equilibrium examples cannot imply this four-strategy classification.

Strictly stable population games and their global replicator convergence mechanisms are classical, notably Hofbauer and Sandholm (2009), with related work by Murali and Shaiju (2023). The use of strict negative tangential definiteness and relative entropy is **not** claimed as new. The mathematical contribution is instead the explicit support-transition classification, sharp cubics, global conclusion for the two model-defined matrix segments, and limiting extinction rates. Published database queries have not established absolute novelty.

## Limitations

The affine payoff segments are natural mathematical interpolants between the paper's three illustrative matrices; they are not a mechanistic calibration to actual pH or therapy intensity. The result is for the fixed-payoff deterministic replicator equation only; it asserts neither stochastic persistence nor patient-level effects. It says nothing about paths outside the two specified segments, and it does not prove uniform convergence rates as the environmental parameter crosses a threshold. At an exact support-change parameter the excluded type has zero linear invasion rate, so the negative endpoint rates do not apply there. Initial data confined to a face that omits an equilibrium-supported type are outside the global-convergence claim. Full bibliographic coverage and independent scientific review remain outstanding.

## References

1. J. A. Rodrigues, *Modeling Tumor Phenotypic Heterogeneity with Multi-Strategy Evolutionary Games*, Preprints.org, posted 2026-01-22, DOI: 10.20944/preprints202601.1761.v1. Full public text: https://www.preprints.org/manuscript/202601.1761 .
2. J. A. Rodrigues, *Modeling Tumor Metabolic Heterogeneity through Evolutionary Game Theory: Insights into Therapy Design*, Preprints.org, posted 2025-08-18, https://www.preprints.org/manuscript/202508.1253 .
3. J. Hofbauer and W. H. Sandholm, *Stable games and their dynamics*, Journal of Economic Theory 144 (2009), 1665–1693, DOI: 10.1016/j.jet.2009.01.007.
4. D. Murali and A. J. Shaiju, *Dynamic stability of the set of Nash equilibria in stable stochastic games*, Journal of Dynamics and Games 10 (2023), 270–286, DOI: 10.3934/jdg.2023004.
