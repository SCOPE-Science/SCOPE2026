# Three annual censuses sharply identify a one-year seed-bank occupancy model

## Finding

Consider the independent-source annual-patch model of Fréville et al. (2013), with strictly interior parameters: immigrant seedling probability \(c\in(0,1)\), immediate local recruitment probability \(g_0\in(0,1)\), one-year delayed recruitment probability \(g_1\in(0,1)\), and seedling disturbance probability \(d\in(0,1)\). Let \(Y_t\in\{0,1\}\) indicate above-ground occurrence at the annual census. In the stationary regime, the *joint probability distribution of only three consecutive annual observations*, \((Y_{t-1},Y_t,Y_{t+1})\), determines all four parameters uniquely. The stationary joint distribution of two consecutive annual observations does not determine the parameters: each admissible two-census law has a local two-dimensional family of compatible interior parameter vectors. Thus **three annual censuses are the exact minimal horizon for structural parameter identification from the full stationary observation law**.

More precisely, define the four observable transition probabilities
\[
q_{yz}=\Pr(Y_{t+1}=1\mid Y_t=y,\ Y_{t-1}=z),\qquad y,z\in\{0,1\}.
\]
For \(a=q_{10}-q_{00}\), \(b=q_{01}-q_{00}\), and \(r=q_{10}+q_{01}-q_{00}-q_{11}\), the complete interior image of the parameter family is exactly
\[
q_{00}>0,\quad a>0,\quad b>0,\quad 0<r<\min\{a,b\},\quad q_{00}+\frac{ab}{r}<1.
\]
For every quadruple meeting these inequalities, set \(w=ab/r\), \(u=q_{00}+w\); the unique parameter vector is
\[
\boxed{c=\frac{q_{00}}u,\quad g_0=\frac aw,\quad g_1=\frac bw,\quad d=1-u.}
\]
The Jacobian of the four observable probabilities with respect to \((c,g_0,g_1,d)\), with observation ordering \((q_{00},q_{10},q_{01},q_{11})\), has determinant \(-(1-c)^2(1-d)^3g_0g_1\). In particular, the inversion is singular at the zero-delayed-recruitment boundary, in agreement with the previously reported nonidentifiability of the no-seed-bank model.

## Assumptions and scope

Annual presence/absence is detected without error. All patches being compared share the same time-homogeneous parameters. Conditional on the two preceding above-ground occurrence indicators, immigrant, immediate local, and one-year-delayed sources independently produce at least one seedling with their stated probabilities; a common independent disturbance removes all seedlings with probability \(d\). Plants present at the current census always produce a potential one-year seed-bank contribution for the next census, and migrant seeds do not enter this seed bank. These are the specific life-cycle assumptions of the motivating four-state model, not assumptions about all seed banks.

Exact probability laws are assumed known for structural identification; three realized binary measurements at one patch, or three years of finite and noisy field data, do **not** determine four real parameters without sampling uncertainty. For the minimum-horizon statement, observations are drawn from the unique stationary regime, which exists because the induced chain of consecutive observable pairs has strictly positive branching probabilities and is irreducible and aperiodic. No assertion is made for imperfect detection, heterogeneous rates, interpatch dependence, multiyear dormancy, or sampling variances.

## Proof

**1. Reduction of the apparently hidden state.** Denote by \(B_t\) the binary presence of a locally generated one-year seed bank at census \(t\). Under the stated life-cycle rule, it satisfies the deterministic identity \(B_{t+1}=Y_t\). After one transition, the four nominal states \((B_t,Y_t)\) are precisely the four observable lagged pairs \((Y_{t-1},Y_t)\). Given \(Y_t=y\) and \(Y_{t-1}=z\), the absence of all three independent seedling sources has probability \((1-c)(1-g_0)^y(1-g_1)^z\). Multiplying the probability that at least one source succeeds by survival from disturbance yields
\[
q_{yz}=(1-d)\left[1-(1-c)(1-g_0)^y(1-g_1)^z\right].\tag{1}
\]
Thus the observed process has exact Markov order two. Its order is not reducible to one for interior parameters, since \(q_{y1}>q_{y0}\) for both \(y\).

**2. Inversion and observable feasibility.** Write \(u=1-d\) and \(w=u(1-c)\). Equation (1) implies
\[
q_{00}=u-w,\qquad q_{10}=u-w(1-g_0),\qquad q_{01}=u-w(1-g_1),\qquad q_{11}=u-w(1-g_0)(1-g_1).
\]
Subtracting gives \(a=wg_0\), \(b=wg_1\), and \(r=wg_0g_1>0\). Consequently \(w=ab/r\), \(u=q_{00}+w\), and the displayed inverse follows. The constraints \(0<c,g_0,g_1,d<1\) imply the five displayed observable inequalities. Conversely, those inequalities give \(0<w<u<1\), \(g_0=r/b\in(0,1)\), and \(g_1=r/a\in(0,1)\). The reconstructed parameters are strictly interior and reproduce all four \(q_{yz}\), proving necessity, sufficiency and global uniqueness. Direct differentiation yields the asserted nonzero Jacobian determinant.

**3. Why three consecutive observations suffice.** Under stationarity every ordered pair \((Y_{t-1},Y_t)=(z,y)\) has positive probability. Therefore the three-census law determines each of the four probabilities by
\[
q_{yz}=\frac{\Pr(Y_{t-1}=z,Y_t=y,Y_{t+1}=1)}{\Pr(Y_{t-1}=z,Y_t=y)}.
\]
Step 2 now identifies the complete parameter vector, not merely a local equivalence class.

**4. Why two do not suffice.** Set \(\pi_{zy}=\Pr(Y_{t-1}=z,Y_t=y)\). Stationarity forces \(\pi_{01}=\pi_{10}\), and balance of the pair-state chain gives
\[
\frac{\pi_{01}}{\pi_{00}}=\frac{q_{00}}{1-q_{01}},\qquad
\frac{\pi_{11}}{\pi_{01}}=\frac{q_{10}}{1-q_{11}}.
\]
The full two-census law is determined by only these two ratios and normalization \(\pi_{00}+2\pi_{01}+\pi_{11}=1\). In the four-dimensional open set of admissible \(q\)-quadruples established in Step 2, the two ratio maps use disjoint pairs of coordinates and have differential rank two. Their local fibers are therefore two-dimensional by the implicit function theorem, and the inverse map transfers these fibers to distinct ecological parameters with identical two-census laws. Thus no shorter observation horizon identifies all four parameters.

**5. Exact witness and boundary.** For \((c,g_0,g_1,d)=(1/5,1/2,1/3,1/4)\), the observable quadruple \((q_{00},q_{10},q_{01},q_{11})=(3/20,9/20,7/20,11/20)\). Here \((a,b,r)=(3/10,1/5,1/10)\), yielding \((w,u)=(3/5,3/4)\) and recovering all four inputs exactly. The stationary two-census law is \((\pi_{00},\pi_{01},\pi_{10},\pi_{11})=(13/22,3/22,3/22,3/22)\). At \(g_1=0\), the difference \(q_{y1}-q_{y0}\) and the interaction \(r\) vanish; the above inversion is not asserted at that boundary.

## Verification

The standalone `check_seedbank.py` uses SymPy for symbolic differentiation and exact `fractions.Fraction` arithmetic for 256 strictly interior parameter quadruples. It verifies the inverse, the positivity and stationarity of the four observable pair states, the exact three-census recovery identity, the Jacobian determinant, the singular zero-delayed-recruitment boundary, and the rational example. Its output terminates in `PASS`. This finite computation verifies examples and algebra but is not substituted for the preceding proof of the all-parameter statements.

## Relationship to prior work

Fréville, Choquet, Pradel and Cheptou (2013) introduced precisely the four-state one-year seed-bank metapopulation model, wrote its independent-source recruitment rules, and investigated estimation from long presence/absence series with a hidden Markov implementation. They established that the zero-delayed-recruitment case is not structurally identifiable and tested estimation statistically. Those modeling facts, the general approach to hidden-state identification, and the existence of parameter identifiability in the interior are prior results, not claimed here. The present result isolates a sharper exact finite-horizon theorem: after one step the bank indicator equals last year's observed presence, the visible process itself is second-order Markov, its four ecological parameters have the displayed global rational inverse and exact feasible-table test, and three consecutive annual observations form the minimal population-law horizon. These claims are not established by the inspected main article.

Borgy et al. (2015) investigate a different multilevel, multiyear seed-bank HMM with management-dependent probabilities. Manna et al. (2017) assess identification of seed-bank versus dispersal *scenarios* in simulated surveys; their accessible abstract mentions three-year surveys for 1,000 patches but neither establishes the present exact four-parameter global inversion nor concerns the same homogeneous model. Louvet et al. (2021) use a different seed-bank-survival HMM and a characteristic-event probability rather than the four ecological parameters here. General noisy-OR factorization underlies the elementary algebra in Step 2 and is not asserted as an independent discovery. The distinctive claim is the exact observable order-two reduction, full feasible-domain inversion, and sharp stationary census horizon for this ecological life cycle. Historical priority against broader probabilistic identifiability work remains a residual risk.

## Limitations

The theorem is about structural identifiability from *exact* three-census joint distributions, not the sample size or accuracy of field estimates. Near \(g_0=0\), \(g_1=0\), \(c=1\), or \(d=1\), the inversion is ill-conditioned or singular. If previous plants do not deterministically establish the next year's seed-bank presence, or if observation is imperfect, the order-two reduction can fail. It does not imply identifiability for richer ecological models. The 2013 article's supplementary transition-matrix appendix and the complete 2017 follow-up text were not accessible in the inspected sources; this limits historical-priority certainty, not the mathematical proof. Independent scientific validation has not been performed.

## References

- Fréville, H., Choquet, R., Pradel, R., and Cheptou, P.-O. (2013). *Inferring seed bank from hidden Markov models: new insights into metapopulation dynamics in plants*. Journal of Ecology 101, 1572–1580. First publicly posted 26 June 2013. https://doi.org/10.1111/1365-2745.12141
- Choquet, R., and Cole, D. J. (2012). *A hybrid symbolic-numerical method for determining model structure*. Mathematical Biosciences 236, 117–125. https://doi.org/10.1016/j.mbs.2012.02.002
- Borgy, B., Reboud, X., Peyrard, N., Sabbadin, R., and Gaba, S. (2015). *Dynamics of weeds in the soil seed bank: a hidden Markov model to estimate life history traits from standing plant time series*. PLoS ONE 10, e0139278. https://doi.org/10.1371/journal.pone.0139278
- Manna, F., Pradel, R., Choquet, R., Fréville, H., and Cheptou, P.-O. (2017). *Disentangling the role of seed bank and dispersal in plant metapopulation dynamics using patch occupancy surveys*. Ecology 98, 2662–2672. https://doi.org/10.1002/ecy.1960
- Louvet, A., et al. (2021). *Detecting seed bank influence on plant metapopulation dynamics*. Methods in Ecology and Evolution 12, 655–664. https://doi.org/10.1111/2041-210X.13547
