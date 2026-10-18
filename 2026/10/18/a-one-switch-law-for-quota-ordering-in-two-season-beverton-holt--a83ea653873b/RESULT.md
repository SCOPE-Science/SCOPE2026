# A one-switch law for quota ordering in two-season Beverton–Holt persistence

## Finding
Fix a two-season Beverton–Holt fishery with intrinsic multiplier \(r>1\), capacities \(K_1,K_2>0\), and fixed low quota \(L\ge0\). Let \(H>L\) be the high quota. Hold the order of the environmental capacities fixed, and compare the high-first quota assignment \((H,L)\) with low-first \((L,H)\).

**Theorem (at most one threshold reversal).** On any connected interval of high quotas \(H>L\) where both assignments possess two distinct physically positive two-cycles, the ordering of their lower initial-abundance thresholds can change at most once. More precisely, a tie of the lower thresholds is possible at only one explicitly determined value \(H_*\). This bound is sharp: for \(r=3\), \(K_1=4\), \(K_2=1\), and \(L=1/5\), both cycles are physically admissible throughout \(H\in[1/4,1/2]\), but the optimal assignment for maximizing the initial-abundance basin switches exactly once, at
\[
H_* = \frac{1345-159\sqrt{57}}{293}\in(0.49,0.50).
\]
Additionally, the transfer-matrix trace difference always has the exact sign
\[
\operatorname{tr}M_{HL}-\operatorname{tr}M_{LH}
 =(H-L)(r-1)^2(K_1-K_2).
\]
Thus an assignment maximizing the trace can fail to minimize the population needed for persistence, even though both quantities arise from the same two-step dynamics.

## Assumptions and scope
Each season applies \(F_{K,h}(x)=g_K(x)-h\), where
\[
g_K(x)=\frac{rKx}{K+(r-1)x},\qquad x\ge0,\quad r>1,\ K>0,\ h\ge0.
\]
For the high-first arrangement set \(P_{HL}=F_{K_2,L}\circ F_{K_1,H}\), and for the low-first arrangement set \(P_{LH}=F_{K_2,H}\circ F_{K_1,L}\). A **physically positive two-cycle** means a positive fixed point \(x>0\) of the two-step map for which the intermediate first-season abundance is also strictly positive. The theorem's comparison concerns the parameter regime where **each arrangement has two distinct such fixed points**, denoted \(0<u_{ab}<v_{ab}\). The lower root is the repelling persistence boundary and the upper root is attracting. In particular an initial population above the lower root approaches the upper two-cycle, while one below the lower root eventually becomes nonpositive under the model; the boundary itself belongs to the repelling cycle.

The model is deterministic and uses fixed numerical harvest quotas, not fractional harvesting; no stochastic demographic inference is claimed.

## Proof
**1. Rational fixed-point equations.** Write the fractional-linear transfer matrix
\[
T(K,h)=\begin{pmatrix}rK-(r-1)h&-Kh\\r-1&K\end{pmatrix},\qquad \det T(K,h)=rK^2.
\]
Set \(M_{HL}=T(K_2,L)T(K_1,H)\), \(M_{LH}=T(K_2,H)T(K_1,L)\). For a transfer matrix \(M=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\), a fixed point satisfies \(Q_M(x):=cx^2+(d-a)x-b=0\). Direct multiplication gives
\[
\operatorname{tr}M_{HL}-\operatorname{tr}M_{LH}=(H-L)(r-1)^2(K_1-K_2),
\]
\[
Q_{HL}(x)-Q_{LH}(x)=-(H-L)(r-1)R(x),
\]
where
\[
R(x)=(r-1)x^2+\bigl[(r+1)K_1-(r-1)K_2\bigr]x-K_1K_2.
\]
Because \(r-1>0\) and \(R(0)<0\), the polynomial \(R\) has exactly one positive zero \(\xi\).

**2. Uniqueness of a threshold tie.** If the lower fixed points of the two assignments agree for some \(H>L\), their common value must annihilate both quadratic equations, hence equal \(\xi\). For the low-first dynamics this requires
\[
\xi=F_{K_2,H}(F_{K_1,L}(\xi))
=g_{K_2}(g_{K_1}(\xi)-L)-H.
\]
There is therefore at most one admissible value,
\[
H_*=g_{K_2}(g_{K_1}(\xi)-L)-\xi.
\]
On any connected interval where both lower roots are simple, physically positive fixed points, they depend continuously on \(H\); their ordering can change only through equality. This proves the at-most-one-switch assertion. The formula is a necessary condition for a tie, not a claim that \(H_*\) is always admissible.

**3. Physical meaning of the smaller fixed point.** On the positive intermediate-state domain, each seasonal map is strictly increasing and strictly concave, so its positive two-step composition is strictly increasing and concave. When two positive fixed points exist, the lower one is repelling and the upper one is attracting. Directly, the sign of \(P(x)-x\) is opposite to the sign of the fixed-point quadratic when the transfer denominator is positive. Below the lower root the orbit decreases until harvest makes it nonpositive, whereas above the lower root it converges monotonically to the upper periodic orbit (after grouping steps in pairs). Thus comparing these smaller fixed points compares the first-season abundance threshold for persistence.

**4. Sharp exact example.** Take \(r=3\), \(K_1=4\), \(K_2=1\), \(L=1/5\). The two quadratic fixed-point equations are, with positive irrelevant scale factors retained,
\[
Q_{HL}(x)=\frac25\bigl[(65-10H)x^2-(67+7H)x+26H+2\bigr],
\]
\[
Q_{LH}(x)=\frac65\bigl[21x^2+(21H-27)x+2H+2\bigr].
\]
For \(H=1/4\), exact rational isolation gives
\[
\frac{141}{1000}<u_{HL}<\frac{143}{1000},\qquad
\frac{131}{1000}<u_{LH}<\frac{133}{1000},
\]
so high-first demands a **larger** founding population. At \(H=1/2\),
\[
\frac{278}{1000}<u_{HL}<\frac{280}{1000},\qquad
u_{LH}=\frac27>\frac{285}{1000},
\]
so high-first instead demands a **smaller** founding population.

For every \(H\in[1/4,1/2]\), both quadratic discriminants (after the harmless positive scalings above are removed) are positive:
\[
D_{HL}=1089H^2-5742H+3969>0,\qquad
D_{LH}=441H^2-1302H+561>0.
\]
Their leading, constant, and negative linear coefficients ensure two positive roots. Intermediate physical positivity follows as well: the first-season abundance vanishes at \(x=2H/(6-H)\) for the high-first regime and at \(x=2/29\) for the low-first regime. In both cases the corresponding quadratic is positive at this vanishing point, and that point lies strictly left of the quadratic's vertex and hence strictly below the smaller root. Specifically,
\[
Q_{HL}\!\left(\frac{2H}{6-H}\right)=\frac{72(3H+2)}{5(H-6)^2}>0,
\qquad Q_{LH}\!\left(\frac{2}{29}\right)=\frac{120(29H+2)}{841}>0.
\]

Here \(R(x)=2(x^2+7x-2)\) has positive root \(\xi=(\sqrt{57}-7)/2\). Substitution into the formula of step 2 yields the stated \(H_*\). At that quota both quadratic equations vanish at \(\xi\); the smaller-root assertion follows from the exact inequality that \(\xi\) lies left of both quadratic vertices. Thus the exact switch occurs inside \([1/4,1/2]\), and step 2 proves its uniqueness.

## Verification
Run the included `verify_quota_order.py` using Python 3 and SymPy. It verifies the general transfer determinant, trace and quadratic-difference identities symbolically, isolates all four example lower roots by rational sign tests, checks both first-season intermediate abundances are positive, and establishes the exact common threshold and high-quota formula. These finite rational checks are supporting certificates for the explicit example; the general one-switch theorem follows algebraically from the proof, not from numerical sampling.

## Relationship to prior work
AlSharawi and Ben Haj Rhouma (2010) develop matrix methods for periodically harvested Beverton–Holt dynamics, analyze permutations of *capacities*, and pose explicitly the question of how permuting *harvest quotas* affects the persistence set (their Question 2). The present result gives a structural, sharp answer for two seasons: there is at most one threshold-order reversal when the larger quota varies, and it can occur even though the trace ordering is fixed. Their 2009 study analyzes fixed-environment periodic harvesting and initial-population basins; fixed capacity does not establish the heterogeneous-capacity switch. Al-Ghassani and AlSharawi (2020) address map permutations and geometric means of global attractors, a nearby but different quantity. Its complete text could not be inspected here, so an overlooked specialization remains a residual originality risk.

## Limitations
Only two seasons are classified; no corresponding one-switch assertion is made for three or more phases. The theorem concerns deterministic abundance dynamics under a fixed sequence of capacities and quota permutations, and assumes two physically positive two-cycles for the threshold comparison. Trace ordering alone is **not** a universal extinction guarantee. The 2020 related paper was accessible only in abstract and catalog form; its full text remains an unresolved literature-access risk. Independent audit has not been performed.

## References
1. Z. AlSharawi and M. Ben Haj Rhouma, "The Discrete Beverton-Holt Model with Periodic Harvesting in a Periodically Fluctuating Environment," *Advances in Difference Equations* (2010), Article 215875. Published online 2010-03-08. DOI: 10.1155/2010/215875.
2. Z. AlSharawi and M. Ben Haj Rhouma, "The Beverton–Holt Model with Periodic and Conditional Harvesting," *Journal of Biological Dynamics* 3 (2009), 463–478. DOI: 10.1080/17513750802601041.
3. A. S. Al-Ghassani and Z. AlSharawi, "The Effect of Maps Permutation on the Global Attractor of a Periodic Beverton–Holt Model," *Applied Mathematics and Computation* 370 (2020), Article 124905. DOI: 10.1016/j.amc.2019.124905.
