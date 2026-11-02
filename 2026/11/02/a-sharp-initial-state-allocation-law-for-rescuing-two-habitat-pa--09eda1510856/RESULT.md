# A sharp initial-state allocation law for rescuing two habitat patches

## Finding
Consider a closed, two-patch stochastic metapopulation with local extinction rates \(a,b>0\). When only patch 1 is occupied, patch 2 can be recolonized at rate \(c\); when only patch 2 is occupied, patch 1 can be recolonized at rate \(d\). Fix a total colonization-rate budget \(c+d=B>0\), with \(0\le c\le B\). Once neither patch is occupied, the metapopulation is permanently extinct.

Let the initial probabilities of the nonextinct states \(11,10,01\) be \(w_{11},w_{10},w_{01}\ge0\), summing to \(1\). Write \(T(c)\) for the expected time until both patches become empty. **Theorem.** For every such choice of rates, budget and initial law, \(T(c)\) is a strictly concave quadratic with constant curvature
\[
T''(c)=-\frac{2}{ab(a+b+B)}.
\]
Its unique maximizing allocation is
\[
\boxed{c_* = \min\!\left\{B,\max\!\left\{0,\frac{B+a w_{10}-b w_{01}}2\right\}\right\},\qquad d_*=B-c_*.}
\]
Thus, a fixed-rate intervention that maximizes expected time to regional extinction is exactly balanced when both patches are initially occupied, but may be entirely directed toward the initially empty patch when only the other patch is occupied. More generally, the asymmetry of the optimum is determined only by \(a w_{10}-b w_{01}\), despite both local extinction rates affecting the achieved extinction time.

The classification is sharp: if \(a w_{10}-b w_{01}\ge B\) all capacity goes from patch 1 toward patch 2; if \(a w_{10}-b w_{01}\le-B\) all goes in the opposite direction; otherwise the unique optimum is interior, with \(c_*-d_*=a w_{10}-b w_{01}\). Equalities are included in the endpoint cases, and there are no other maximizers.

## Assumptions and scope
The continuous-time Markov chain has states \(11,10,01,00\). The only transitions are \(11\to10\) at rate \(b\), \(11\to01\) at rate \(a\), \(10\to11\) at rate \(c\), \(10\to00\) at rate \(a\), \(01\to11\) at rate \(d\), and \(01\to00\) at rate \(b\). The state \(00\) is absorbing. Extinction events in distinct occupied patches are represented by their competing exponential clocks. The rates \(a,b\) are strictly positive; \(c,d\) may be zero. Colonization occurs only into an empty patch, only from the other occupied patch, and rates remain fixed before and after observations. The objective is the unconditional mean absorption time from the specified initial law, not a finite-horizon survival probability or a quasi-stationary lifetime. Absorption occurs almost surely with finite mean, since all nonextinct states can reach \(00\) through positive-rate extinction events.

## Proof
Let \(t_{11},t_{10},t_{01}\) be the mean time to absorption from each nonextinct state. First-step analysis for the above generator gives
\[
\begin{aligned}
(a+b)t_{11}-bt_{10}-at_{01}&=1,\\
(a+c)t_{10}-ct_{11}&=1,\\
(b+d)t_{01}-dt_{11}&=1.
\end{aligned}
\]
The second and third equations yield \(t_{10}=(1+ct_{11})/(a+c)\) and \(t_{01}=(1+dt_{11})/(b+d)\). Inserting these into the first gives, after multiplication by \((a+c)(b+d)\),
\[
 t_{11}=\frac{a^2+ab+b^2+(a+b)(c+d)+cd}{ab(a+b+c+d)}.
\]
Back-substitution simplifies the other two means to
\[
 t_{10}=\frac{(b+c)(a+b+d)}{ab(a+b+c+d)},\qquad
 t_{01}=\frac{(a+d)(a+b+c)}{ab(a+b+c+d)}.
\]
The denominators are strictly positive at every permitted parameter and at both budget endpoints, so no limiting division is needed.

Set \(d=B-c\), and write \(D=ab(a+b+B)>0\). The three means then become
\[
\begin{aligned}
Dt_{11}&=a^2+ab+b^2+(a+b)B+c(B-c),\\
Dt_{10}&=(b+c)(a+b+B-c),\\
Dt_{01}&=(a+B-c)(a+b+c).
\end{aligned}
\]
Differentiation gives the exact derivatives
\[
Dt_{11}'=B-2c,\qquad Dt_{10}'=B+a-2c,\qquad Dt_{01}'=B-b-2c,
\]
with the same second derivative \(-2/D\) for each. Therefore the mixture \(T=w_{11}t_{11}+w_{10}t_{10}+w_{01}t_{01}\), using \(w_{11}+w_{10}+w_{01}=1\), satisfies
\[
 T'(c)=\frac{B+a w_{10}-b w_{01}-2c}{D},\qquad T''(c)=-\frac2D<0.
\]
The unique maximizer on the compact feasible interval \([0,B]\) is the projection of its free critical point \((B+a w_{10}-b w_{01})/2\) onto that interval. This proves the theorem including the boundary cases and uniqueness. Whenever the free critical point is feasible, the exact loss from any different allocation is \((c-c_*)^2/D\).

For a concrete symmetric landscape, take \(a=b=B=1\). If both patches are initially occupied, the optimum is \(c=d=1/2\), and \(t_{11}=7/4\), compared with \(5/3\) at \(c=1\). If instead only patch 1 is initially occupied, the optimum is \(c=1,d=0\), and \(t_{10}=4/3\), compared with \(5/4\) at the symmetric allocation. The direction of optimal asymmetry therefore depends on initial occupancy even when both habitats have identical local extinction rates; both displayed improvements are exactly \(1/12\).

## Verification
The standalone file `verify.py` forms the three-state transient generator independently and solves the first-passage linear system using exact rational Gaussian elimination. It compares the resulting times against the three closed forms over positive rational parameter grids (including \(c=0\) and \(c=B\)), checks the unique clipped optimum for six initial-state mixtures, verifies the universal curvature by exact finite differences, and reproduces the symmetric example. Execute `python verify.py`; the supplied run passed 2916 exact checks. The finite checks do not establish the theorem outside their test grid; the proof above supplies the general statement.

## Relationship to prior work
Day and Possingham (1995) construct state-transition matrices for stochastic patch occupancy with heterogeneous patches, using a discrete-time extinction-then-colonization cycle; their model supplies a general analysis framework, but the examined text does not give the continuous-time initial-law-dependent optimal directional split above. Etienne and Heesterbeek (2001) study conservation interventions to extend metapopulation persistence, making their work the most important historical-priority risk; only their abstract was accessible for this comparison. Vuilleumier and Possingham (2006) demonstrate effects of asymmetric connectivity primarily by simulation on many patches, initially all occupied, rather than the present exact two-patch mean-first-passage optimization. Bode, Burrage and Possingham (2008) include a two-patch appendix showing that symmetric connectivity maximizes the leading nonabsorbing eigenvalue in a discrete-time model with equal extinction probabilities. That is a different objective from the unconditional mean first-passage time for a fixed arbitrary initial distribution, and does not imply the state-dependent directional optimum. Ross and Pollett (2010) optimize overall colonization versus extinction management in a homogeneous stochastic Levins formulation; no matching directional initial-state law was found in accessible material. A broader uninspected conservation-optimization theorem may subsume the present specialization, so historical priority is provisional.

## Limitations
This is a deliberately minimal occupancy model, not a demographic abundance model. It excludes background immigration, environmental correlations, rescue effects on within-patch extinction, density dependence, unequal marginal investment costs, time-dependent controls, and colonization while both patches are occupied. The result applies to expected absorption time; optimizing probability of persistence at a particular finite horizon or maximizing the quasi-stationary decay time may give a different rule. Inferring practical intervention rates from finite ecological data can be difficult. The scientific review is not independent, and historical novelty has not been externally certified.

## References
1. Day, J. R. and Possingham, H. P. (1995), *A Stochastic Metapopulation Model with Variability in Patch Size and Position*, Theoretical Population Biology 48:333–360. DOI: 10.1006/tpbi.1995.1034.
2. Etienne, R. S. and Heesterbeek, J. A. P. (2001), *Rules of Thumb for Conservation of Metapopulations Based on a Stochastic Winking-Patch Model*, American Naturalist 158:389–407. DOI: 10.1086/321986.
3. Vuilleumier, S. and Possingham, H. P. (2006), *Does Colonization Asymmetry Matter in Metapopulations?*, Proceedings of the Royal Society B 273:1637–1642. DOI: 10.1098/rspb.2006.3469. Public full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC1634917/.
4. Bode, M., Burrage, K. and Possingham, H. P. (2008), *Using Complex Network Metrics to Predict the Persistence of Metapopulations with Asymmetric Connectivity Patterns*, Ecological Modelling 214:201–209. DOI: 10.1016/j.ecolmodel.2008.02.040.
5. Ross, J. V. and Pollett, P. K. (2010), *Simple Rules for Ranking and Optimally Managing Metapopulations*, Ecological Modelling 221:2515–2520. DOI: 10.1016/j.ecolmodel.2010.02.016.
