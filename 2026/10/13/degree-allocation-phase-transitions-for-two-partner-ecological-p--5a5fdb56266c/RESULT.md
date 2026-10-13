# Degree-allocation phase transitions for two-partner ecological persistence
## Finding
Consider a binary bipartite interaction network with \(m\ge3\) primary species, \(n\ge2\) secondary species, and exactly \(E\) interactions. Assume
\[
\max(m,n)\le E\le mn
\]
and neither guild has isolated species. Independently, each primary species goes extinct with probability \(q\in(0,1)\). A secondary species survives exactly when at least two of its original primary partners remain.

Write the secondary degrees as \(d_1,\ldots,d_n\). Their expected surviving count is
\[
F_q(d_1,\ldots,d_n)=\sum_{i=1}^{n}f_q(d_i),
\qquad
f_q(d)=1-q^d-d(1-q)q^{d-1}.
\]

**Low primary-extinction probability.** For every \(0<q<1/2\), the unique maximizing degree multiset is balanced: with \(E=an+r\) and \(0\le r<n\), it has \(n-r\) degrees equal to \(a\) and \(r\) equal to \(a+1\). This multiset also maximizes at \(q=1/2\), where ties with unbalanced degree multisets may occur.

**High primary-extinction probability.** For every
\[
\frac{m-2}{m-1}<q<1,
\]
the unique maximizing degree multiset is maximally concentrated. Write
\[
E-n=u(m-1)+r,
\qquad 0\le r<m-1.
\]
Take \(u\) secondary degrees equal to \(m\), one degree equal to \(1+r\) if \(r>0\), and all remaining degrees equal to \(1\). This multiset also maximizes at \(q=(m-2)/(m-1)\), possibly nonuniquely.

**Intermediate probabilities.** When
\[
\frac12<q<\frac{m-2}{m-1},
\qquad R=\left\lceil\frac{q}{1-q}\right\rceil,
\]
every maximizing multiset has at most one degree in \(\{2,\ldots,R\}\), while all degrees at least \(R+1\) differ by at most one. Thus an exact optimum can be found by comparing at most \(O(nm^2)\) candidate degree multisets. The intermediate optimizer need not be balanced or maximally concentrated.

At \((m,n,E,q)=(4,3,7,3/5)\), the unique maximizing multiset is \((1,3,3)\), with
\[
F_{3/5}(1,3,3)=\frac{88}{125}
>\frac{84}{125}=F_{3/5}(2,2,3),
\]
and
\[
\frac{88}{125}>\frac{428}{625}=F_{3/5}(1,2,4).
\]

**Trajectory-averaged robustness.** If primary species are removed in a uniformly random order and expected secondary survival is averaged equally over all \(m+1\) stages, from none to all removed, then a secondary degree \(d\) contributes exactly
\[
\bar f(d)=\frac{d-1}{d+1}.
\]
Consequently, the balanced secondary degree multiset uniquely maximizes this averaged robustness for every permitted \((m,n,E)\), even in the high-probability regime where concentrated degrees maximize survival at a fixed independent-extinction probability.

## Assumptions and scope
All interactions are binary, unweighted, and simple. Secondary persistence is a stipulated two-partner threshold, not a dynamical population model. The probability of primary extinction is common and independent across primary species. There are no subsequent secondary-to-primary feedbacks or extinction cascades.

The edge budget \(E\), both guild sizes, and the absence of isolates on either guild are fixed. All secondary degree multisets satisfying
\[
1\le d_i\le m,\qquad\sum_i d_i=E
\]
are realizable with nonisolated primary species, as established below. Therefore optimizing degree multisets exactly optimizes the stated graph class.

The low/high regimes are strict open probability ranges for **uniqueness of the maximizing degree multiset**, not uniqueness of a labeled incidence matrix. Boundary probability values permit ties. In the intermediate range the structural restrictions are necessary conditions and give an exact finite candidate algorithm, not a claim that every structurally admissible candidate maximizes.

Trajectory averaging is uniform across the \(m+1\) integer removal stages, not integration against an arbitrary extinction-time distribution.

## Proof
### Survival formula and exact marginal gains
For a secondary species with \(d\) distinct partners, the number of extant partners is binomial with parameters \((d,1-q)\). The secondary species survives if that count is at least two. Hence
\[
f_q(d)=1-q^d-d(1-q)q^{d-1}.
\]
Linear expectation gives \(F_q=\sum_i f_q(d_i)\), without requiring independence among secondary survival events.

Its exact gain from one additional partner is
\[
\Delta_d:=f_q(d+1)-f_q(d)
=d(1-q)^2q^{d-1},
\quad 1\le d<m,
\]
so
\[
\frac{\Delta_{d+1}}{\Delta_d}
=q\frac{d+1}{d}
\]
whenever both sides are defined. The marginal gains therefore rise until a single discrete transition and then fall.

### Graph realization
Enumerate the \(m\) primary vertices cyclically, repeating their labels periodically. For each secondary species, assign the next \(d_i\) consecutive labels as its distinct neighbors. Because \(d_i\le m\), no secondary has repeated partners. Because the concatenated blocks cover \(E\ge m\) consecutive labels, every primary species appears. This realizes any degree multiset with the stipulated bounds and no isolated primary or secondary species.

### Balanced regime
When \(0<q<1/2\), the gain ratio is less than one for every \(d\ge1\). Hence the positive marginal gains strictly decrease with degree. If two secondary degrees satisfy \(a+2\le b\), moving one link from the larger to the smaller changes the objective by
\[
\Delta_a-\Delta_{b-1}>0.
\]
Repeated balancing terminates at the unique multiset whose degrees differ by at most one, which is therefore the unique maximizer. At \(q=1/2\) the marginal sequence is nonincreasing, so the same argument gives optimality but possibly with ties.

### Concentrated regime
If \(q>(m-2)/(m-1)\), then \(\Delta_{d+1}>\Delta_d\) for every \(1\le d\le m-2\). Thus the degree reward is strictly discretely convex. Whenever two degrees are interior and neither has reached the permitted extreme, shifting an edge from the smaller to the larger strictly improves the objective. Repeating pushes all extra edges above the required degree-one baseline into full degrees \(m\), with at most one partial interior degree. The resulting multiset is exactly the concentrated construction in the Finding section and is unique up to permutation. At the stated upper boundary, the marginal sequence is nondecreasing, so this multiset remains an optimizer, not necessarily the only one.

The probability boundaries are sharp uniformly over graph sizes. For \(m=3\), \(n=2\), \(E=4\), the degree multisets \((1,3)\) and \((2,2)\) are both feasible, and their survival difference is
\[
F_q(1,3)-F_q(2,2)
=(1-q)^2(2q-1).
\]
For any larger \(m\), adjoining a secondary degree \(m\) preserves this difference and covers every primary species, showing that the balanced regime cannot extend above \(q=1/2\) uniformly in \(m\). At the other end, consider \((m,m-2)\) versus \((m-1,m-1)\). Their difference is
\[
F_q(m,m-2)-2f_q(m-1)
=\Delta_{m-1}-\Delta_{m-2}.
\]
For \(q<(m-2)/(m-1)\), this is negative, excluding uniform optimality of the fully concentrated degree multiset below the upper threshold.

### Intermediate normal form and exact algorithm
Let \(1/2<q<(m-2)/(m-1)\) and \(R=\lceil q/(1-q)\rceil\). Then \(2\le R\le m-2\). Marginals \(\Delta_1,\ldots,\Delta_R\) are strictly increasing, while \(\Delta_{R+1},\ldots,\Delta_{m-1}\) are strictly decreasing; at integral \(q/(1-q)\), the only intervening equality is \(\Delta_R=\Delta_{R+1}\).

If an optimizer contained two degrees \(2\le a\le b\le R\), moving an edge from the former to the latter would give gain
\[
\Delta_b-\Delta_{a-1}>0,
\]
a contradiction. Thus at most one degree lies in \(\{2,\ldots,R\}\).

If two degrees in the higher range obeyed \(R+1\le a<b-1\le m-1\), moving an edge from \(b\) to \(a\) would yield
\[
\Delta_a-\Delta_{b-1}>0,
\]
another contradiction. Thus all degrees in \(\{R+1,\ldots,m\}\) differ by at most one.

For exact optimization enumerate the number of degree-one vertices (at most \(n\) choices), the optional single middle degree (at most \(m\) choices), and the smaller value of the two possible high degrees (at most \(m\) choices). The count at the larger high degree is determined by the fixed edge sum. Discard infeasible choices and compare the exact \(F_q\) values. The enumeration has at most \(O(nm^2)\) degree-multiset candidates; it includes every global optimizer by the preceding necessary conditions. A fixed multiset can be scored using three counts, so the stated bound counts constant-time objective evaluations in exact arithmetic.

### Uniformly stage-averaged robustness
Take a uniform random permutation of the \(m\) primary species and independently select one of the \(m+1\) cut positions uniformly. For the \(d\) interacting partners of one secondary species, symmetry of the induced relative ordering of those partners and the cut means that the number already removed is uniform on \(\{0,1,\ldots,d\}\). Survival requires at least two partners still present, hence the proportion of favorable possibilities is
\[
\bar f(d)=\frac{d-1}{d+1}.
\]
The discrete marginal of this averaged reward is
\[
\bar f(d+1)-\bar f(d)=\frac{2}{(d+1)(d+2)},
\]
which is strictly decreasing in \(d\). The same edge-balancing exchange therefore gives the unique balanced maximizing multiset for the full random-removal trajectory.

## Verification
The accompanying `verify_two_partner_robustness.py` uses Python's standard library and exact `Fraction` arithmetic. Run:

`python3 verify_two_partner_robustness.py`

It must print `VERIFY_OK` and then exact test counts. It independently enumerates all primary survival/extinction patterns and their Bernoulli probabilities, checks the formula for expected survival, compares all removal stages with the integrated formula, constructs a no-isolate graph realizing every tested degree multiset, and exhaustively optimizes over secondary degree profiles for \(3\le m\le8\) and \(2\le n\le6\) over seven rational extinction probabilities.

The verified run reported 189 independent probability/stage checks and 3,605 exact degree-allocation optimization instances, including 181 cases with multiple optimizers. These checks independently stress-test the formulas and boundary cases; universal validity comes from the proved marginal-gain exchanges and graph-realization argument, **not** from bounded enumeration.

A further independent enumeration of labeled adjacency matrices with \(m=n=3\) and all nonempty guild neighborhoods confirmed that the survival objective depends only on the secondary degree multiset and that the degree-reduction argument has no hidden primary-isolate obstruction.

## Relationship to prior work
Memmott, Waser, and Price (2004) introduced ecological-network robustness simulations under random pollinator removals and the usual topological convention that a plant disappears upon loss of all its interacting partners. Their paper establishes the original conservation motivation and that convention, but does not ask for two surviving partners.

Vieira and Almeida-Neto (2015) show that the simplistic all-partners-lost assumption can underestimate complex cascades. Their stochastic model varies dependence on individual partners and permits secondary coextinction before all partners disappear, but does not state this two-survivor fixed-edge allocation theorem.

Jones, Zurell, and Wiesner (2024), in their degree-equality optimization section and equations (8)–(13), prove balanced secondary degrees maximize **trajectory-averaged** robustness under the all-partners-lost rule. They give more general hypergeometric threshold calculations and discuss weighted interactions. Their optimizing theorem explicitly assumes extinction after losing **all** neighbors; it does not imply the present strict probability-driven transition to concentration under the two-survivor rule, nor the intermediate optimizer's normal form. The integrated balanced result here concerns the changed two-survivor rule and is included to distinguish the two robustness summaries, not as a claim that generic balancing is new.

The exact survival reward is an instance of a discrete single-inflection resource-allocation objective, so standard exchange or majorization reasoning informs the proof. The claim is the ecological degree-allocation phase diagram with sharp parameter ranges, explicit viable-network realization, and the simultaneous contrast between fixed-probability and full-trajectory optima, not the discovery of exchange arguments themselves.

Targeted searches for two-live-partner survival, fixed edge count, degree allocation, Bernoulli extinction, binomial-tail optimization, sigmoid resource allocation, and the exact threshold expressions did not locate this result; search absence alone does not certify absolute novelty.

## Limitations
The theorem concerns **expected** number of persistent secondary species, not their joint survival law. Secondary extinctions are threshold responses without population dynamics, competing resources, stochastic partner strengths, or cascades. All primary extinctions have the same independent probability. Real ecological systems need not obey these assumptions.

The optimizer is characterized by its secondary degree multiset; multiple nonisomorphic incidence networks realize that multiset. At the probability boundaries, degree-multiset ties can occur.

The intermediate regime receives a complete finite candidate reduction, not a closed formula for the winning multiset for every parameter value. All graph sizes and edge budgets in the theorem are finite; the proof is universal across such finite values.

Prior ecological literature provides general threshold and robustness methods. A general separable discrete resource-allocation theorem or an inaccessible supplement may subsume some of the exchange-based structural statements; this possibility remains a stated originality risk.

## References
1. J. Memmott, N. M. Waser, and M. V. Price, “Tolerance of pollination networks to species extinctions,” *Proceedings of the Royal Society B* 271 (2004), 2605–2611. DOI: 10.1098/rspb.2004.2909. First public article date: 6 December 2004.
2. M. C. Vieira and M. Almeida-Neto, “A simple stochastic model for complex coextinctions in mutualistic networks: robustness decreases with connectance,” *Ecology Letters* 18 (2015), 144–152. DOI: 10.1111/ele.12394.
3. C. Jones, D. Zurell, and K. Wiesner, “Novel analytic methods for predicting extinctions in ecological networks,” *Ecological Monographs* 94 (2024). DOI: 10.1002/ecm.1601.
4. *Mathematics Subject Classification 2020*, section 92D40: Ecology.
