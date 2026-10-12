# Sharp first reentry of optimal pollinator protection

## Finding

In a bipartite plant–pollinator network with independent pollinator extinction probability \(q\in(0,1)\), one pollinator may be protected with certainty before primary extinctions occur. Each plant survives if and only if at least one of its pollinator partners survives. The objective is to maximize the expected number of plant species saved by protection, compared with no protection.

**Theorem.** If there are at most three pollinator species, no species can be uniquely optimal for protection at two extinction probabilities while being strictly suboptimal at an intervening probability. If there are four pollinators, this strict reentry is impossible when there are at most twelve plant species. With four pollinators and thirteen plants, strict reentry occurs: in the explicit network below, pollinator \(A\) is uniquely optimal when
\[
0<q<\frac{5-\sqrt5}{10}\quad\text{or}\quad\frac{5+\sqrt5}{10}<q<1,
\]
while pollinator \(B\) is uniquely optimal between these thresholds. Exactly \(A\) and \(B\) tie at either threshold. Thus four is the smallest primary-guild size permitting strict optimal-priority reentry, and thirteen is the smallest secondary-guild size conditional on four primary species.

## Assumptions and scope

A network is a finite simple bipartite graph \(G=(U,W,E)\) with \(r=|U|\ge1\) primary (pollinator) species and \(m=|W|\ge1\) secondary (plant) species. All vertices have at least one incident edge. Distinct plants may have identical partner sets. Write \(N(s)\subseteq U\), nonempty, for the pollinators associated with plant \(s\). Independently each pollinator is lost with probability \(q\), identically across the primary guild. A plant is lost exactly when all species in its partner set are lost. Protecting \(v\in U\) forces its survival while leaving the independent loss variables of other pollinators unchanged. There is no interaction rewiring, partial dependence, interplant feedback, or budget for multiple protected species.

Let \(G_v(q)\) denote the expected number of additional plant survivors under protection of \(v\), relative to the uncoupled baseline extinction outcome, using the natural common-randomness coupling. A *strict reentry* means there are \(0<q_1<q_2<q_3<1\) and a pollinator \(v\) uniquely maximizing \(G_u(q_1)\) and \(G_u(q_3)\) among all \(u\in U\), while \(v\) is not a maximizer at \(q_2\). This definition excludes a temporary tie that never makes \(v\) strictly suboptimal.

## Proof

**Gain identity.** A plant \(s\) can be rescued by protecting \(v\) precisely when \(v\in N(s)\) and all pollinators in \(N(s)\) would otherwise have been lost. This event has probability \(q^{|N(s)|}\). Linearity of expectation, without requiring the plant-loss events to be independent, gives
\[
G_v(q)=\sum_{s\in W:\,v\in N(s)}q^{|N(s)|}.
\]
For distinct \(v,w\), the terms for plants adjacent to both cancel from \(G_v-G_w\); any remaining plant has at most \(r-1\) neighbors. When \(r\le3\), the difference is \(q(a+bq)\), with integer coefficients \(a,b\). The set on which \(G_v(q)>G_w(q)\) is therefore an interval (possibly empty). Its intersection across all \(w\ne v\) is again an interval. Hence the set of probabilities for which \(v\) is uniquely optimal is an interval, ruling out strict reentry.

**Four-pollinator lower bound.** Suppose \(r=4\) and reentry occurs, with \(A\) optimal at two separated probabilities and \(B\) strictly beating \(A\) between them. Since the pairwise difference is \(q\) times a quadratic, it has two distinct roots in \((0,1)\), positive between neither and negative between them. Accordingly,
\[
G_A(q)-G_B(q)=q(a-bq+cq^2),\qquad a,b,c\in\mathbb Z_{>0}.
\]
Two distinct interior roots require \(b^2>4ac\), \(a+c>b\), and \(a<c\). The coefficients count net numbers of plants adjacent exclusively to \(A\) or exclusively to \(B\), at each partner-set size. Consequently at least \(a+b+c\) distinct plants are required.

These inequalities force \(b\ge5\): if \(b\le2\), the discriminant condition is impossible; if \(b=3\), then \(ac\le2\) gives \(a+c\le3\), contradicting \(a+c>3\); if \(b=4\), then \(ac\le3\) gives \(a+c\le4\), contradicting \(a+c>4\). Since \(a+c\ge b+1\), necessarily \(m\ge2b+1\ge11\). If \(m\le12\), then \(b=5\), \(a+c\in\{6,7\}\), \(ac\le6\), and \(a<c\), leaving exactly
\[
(a,b,c)=(1,5,5)\quad\text{or}\quad(1,5,6).
\]
There is room for at most one additional plant beyond those contributing to the stated coefficients, so there are no canceled pairs of opposing exclusive plants. Each of the \(c\) degree-three plants adjacent to \(A\) but not \(B\) has exactly the partner set \(\{A,C,D\}\), where \(C,D\) are the other pollinators. Each of the five degree-two plants adjacent to \(B\) but not \(A\) is adjacent to either \(C\) or \(D\). By pigeonhole, at least one of \(C,D\), say \(C\), is adjacent to at least three such degree-two plants. Write \(e=m-(a+b+c)\le1\). The gain identity yields for every \(q\in(0,1)\)
\[
G_C(q)\ge cq^3+3q^2,\qquad
G_A(q)\le q+cq^3+e q^2,
\]
and therefore
\[
G_C(q)-G_A(q)\ge q\bigl((3-e)q-1\bigr)>0\quad\text{whenever }q>1/2.
\]
For each of the two candidate coefficient triples, \(a-b/2+c/4\le0\). As the quadratic has exactly two roots in \((0,1)\), its larger root is at least \(1/2\). Any proposed return of \(A\) to global optimality after it loses to \(B\) would have to occur above the larger root, where \(q>1/2\); yet \(C\) then strictly beats \(A\). This contradiction excludes strict reentry when \(m\le12\).

**Attaining network.** Take four pollinators \(A,B,C,D\). The thirteen *distinct* plant species have the following partner sets, with multiplicities: one \(\{A\}\), two \(\{A,B\}\), three \(\{B,C\}\), two \(\{B,D\}\), and five \(\{A,C,D\}\). Every vertex is nonisolated. The exact gains are
\[
\begin{aligned}
G_A(q)&=q+2q^2+5q^3, &G_B(q)&=7q^2,\\
G_C(q)&=3q^2+5q^3, &G_D(q)&=2q^2+5q^3.
\end{aligned}
\]
For all \(0<q<1\), \(G_A-G_C=q(1-q)>0\) and \(G_A-G_D=q>0\). Thus only \(A\) or \(B\) can be globally optimal, and
\[
G_A(q)-G_B(q)=q(1-5q+5q^2).
\]
The two simple roots are exactly \((5\pm\sqrt5)/10\), both strictly between zero and one; the sign is positive outside and negative between. This proves the stated complete priority switch and the two sharp size bounds.

## Verification

The standalone Python standard-library program `verify.py` specifies all thirteen plant neighborhoods without compressed or external dependencies. It verifies the four gain polynomials, independently enumerates all \(2^4=16\) primary-extinction masks for each of three rational probabilities, and checks that the analytically predicted gain matches the expected difference in survivors. It also enumerates all strictly positive integer coefficient triples of total weight at most twelve satisfying the two-interior-root criterion, finding exactly \((1,5,5)\) and \((1,5,6)\); this computation corroborates, but does not replace, the preceding general pigeonhole proof. Run `python3 verify.py`. Expected final line: `VERIFY_OK plant_species=13 primary_species=4 exact_masks=48 coefficient_cases=2 roots=(5+-sqrt(5))/10`.

## Relationship to prior work

The elementary all-partners-lost coextinction convention comes from studies of pollinator loss by Memmott, Waser and Price and related ecological-network work by Dunne, Williams and Martinez. Traveset, Tur and Eguíluz compare pollinator-importance rankings in more elaborate stochastic coextinction models. Jones, Zurell and Wiesner provide general analytic formulas for secondary extinctions under random or targeted primary loss. The one-protection gain identity here is a direct specialization of that probability calculus and is **not** claimed as novel. The result assessed here is the sharp *reentry and minimum-size* theorem for optimal protection, including proof that an isolated pairwise score reversal cannot be promoted to a genuine global-optimum reentry below the boundary.

## Limitations

The result is exact only in the independent, homogeneous, single-step, all-neighbors-lost model with one perfectly protected primary species. Repeat neighborhoods among biologically distinct plants are permitted and are used in the witness. The four-pollinator thirteen-plant minimality is conditional on having exactly four pollinators; no minimum for total vertices over networks with more pollinators is asserted. No empirical prevalence, statistical detectability, biological equivalence of pollinators, or optimality under heterogeneous extinction probabilities is established. Existing general coextinction formulas make the gain identity expected; the literature assessment supports, but cannot certify, that the specific global-optimum sharp boundary is unpublished.

## References

1. Dunne, J. A., Williams, R. J. and Martinez, N. D. (2002). *Network structure and biodiversity loss in food webs: robustness increases with connectance*. Ecology Letters 5, 558–567. DOI: 10.1046/j.1461-0248.2002.00354.x. First published 10 July 2002.
2. Memmott, J., Waser, N. M. and Price, M. V. (2004). *Tolerance of pollination networks to species extinctions*. Proceedings of the Royal Society B 271, 2605–2611. DOI: 10.1098/rspb.2004.2909. First published online 6 December 2004; open PDF at https://www.bio.bris.ac.uk/research/community/article_PDF/Memmottetal2004.pdf.
3. Traveset, A., Tur, C. and Eguíluz, V. M. (2017). *Plant survival and keystone pollinator species in stochastic coextinction models: role of intrinsic dependence on animal-pollination*. Scientific Reports 7, 6915. DOI: 10.1038/s41598-017-07037-7.
4. Jones, C., Zurell, D. and Wiesner, K. (2024). *Novel analytic methods for predicting extinctions in ecological networks*. Ecological Monographs. DOI: 10.1002/ecm.1601; freely accessible full text on the journal website.
