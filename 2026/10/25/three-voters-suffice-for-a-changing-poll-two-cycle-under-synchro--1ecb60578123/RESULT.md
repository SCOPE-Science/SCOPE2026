# Three voters suffice for a changing-poll two-cycle under synchronous trembling-hand plurality

## Finding

For the independent uniform trembling-hand plurality response of Weigel, Berriaud, and Wattenhofer, three voters and three candidates suffice for a **truthfully initiated exact period-two orbit whose public vote counts also have period two**. Moreover, no such cycle exists with fewer than three voters (regardless of candidate count), or with fewer than three candidates (regardless of voter count). Thus these dimensions are simultaneously minimal.

Let candidates be \(A,B,C\). The three voters' rankings and normalized utilities are

\[
\begin{array}{c|ccc|c}
 &u(A)&u(B)&u(C)&\text{condition}\\\hline
1&1&\rho_1&0&0<\rho_1<\tfrac12\\
2&\rho_2&1&0&\tfrac12<\rho_2<\tfrac45\\
3&\rho_3&0&1&\tfrac12<\rho_3<\tfrac45
\end{array}
\]

For every parameter triple in this nonempty open box, starting from sincere ballots gives

\[
(A,B,C)\;\longleftrightarrow\;(A,A,A),\qquad
(1,1,1)\;\longleftrightarrow\;(3,0,0)
\]

for the ballot profiles and corresponding public count vectors respectively. The instance \(\rho_1=1/4,\ \rho_2=\rho_3=3/4\) uses rational utilities and strict comparisons throughout.

## Assumptions and scope

An electorate of \(N\ge1\) voters and \(m\ge2\) candidates has strict cardinal utilities. A plurality tie is resolved by the uniform lottery over tied winners. At ballot profile \(s\), voter \(i\) excludes her own ballot, views each other vote as staying fixed with probability \(1-p\) and switching independently to each *other* candidate with probability \(p/(m-1)\), then selects the ballot with maximum expected lottery utility for all sufficiently small positive \(p\). All voters revise simultaneously; the perceived trembles are beliefs, not realized ballot mutations. The initial ballot of each voter is her top-ranked candidate. Only this specific model is addressed.

## Proof

**Three-voter witness.** Let \(U_i^p(x\mid q)\) denote the expected utility of contemplated ballot \(x\) against private tally \(q\). It is enough to compare a voter's favorite with her middle candidate: a ballot for the least-preferred candidate is strictly dominated by the favorite under full-support trembles. To see the domination, fix any terminal opponent tally and compare adding a top versus a bottom vote: moving the vote to the top cannot lower the uniform-winning-lottery utility, and it strictly improves it for a reachable tied or near-tied tally. Every terminal tally has positive probability for \(p>0\).

At the sincere profile \((A,B,C)\), removing one's own ballot leaves two distinct rival votes. Direct uniform-lottery evaluation without any tremble gives, for each respective top-minus-middle comparison,

\[
U_i^p(\mathrm{top}_i\mid q_i)-U_i^p(\mathrm{middle}_i\mid q_i)
=\frac{1-2\rho_i}{3}+O(p)\qquad(i=1,2,3).
\]

The first coefficient is positive for voter 1 and negative for voters 2 and 3. Therefore the next simultaneous profile is \((A,A,A)\).

At \((A,A,A)\), all voters have private tally \(q=(2,0,0)\) in \((A,B,C)\) order. Without trembles, every contemplated favorite or middle ballot produces winner \(A\), so each comparison has zero constant coefficient. For voter 1, the two possible single-tremble *destinations* are \(A\to B\) and \(A\to C\), each with total first-order probability coefficient one after summing over the two rival ballots. Their respective top-minus-middle payoff changes are \(1-\rho_1\) and \((2-\rho_1)/3\). Hence

\[
U_1^p(A\mid q)-U_1^p(B\mid q)
=\frac{5-4\rho_1}{3}\,p+O(p^2)>0.
\]

For voter 2, the same two single-tremble destination classes give payoff changes \(1-\rho_2\) and \((1-2\rho_2)/3\), hence

\[
U_2^p(B\mid q)-U_2^p(A\mid q)
=\frac{4-5\rho_2}{3}\,p+O(p^2)>0.
\]

Exchanging \(B,C\) yields exactly \((4-5\rho_3)p/3+O(p^2)>0\) for voter 3's contemplated \(C\) over \(A\). The neglected two-tremble events have order \(p^2\). Thus all three choose their favorites and the next profile returns to \((A,B,C)\). Every displayed decisive coefficient is nonzero on the claimed open box. Since the two complete ballot profiles and the two public count vectors are distinct, both periods equal exactly two.

**Lower bounds.** For one voter, the favorite ballot wins outright and is uniquely optimal. For two voters and *any* number of candidates, condition on any realized vote \(z\) of the only other voter. Voting for one's favorite \(x\) produces either winner \(x\) or the equal lottery on \(\{x,z\}\). Any other ballot \(y\ne x\) produces either winner \(z\) or the equal lottery on \(\{y,z\}\). Since \(u(x)>u(y)\), the former yields strictly greater utility in each case \(z=x\), \(z=y\), or \(z\notin\{x,y\}\). Therefore voting for \(x\) strictly maximizes expected utility, independently of polls and tremble parameter; the truthful profile is a fixed point and every starting profile converges after one update.

With only two candidates and any voter count, choosing one's favorite weakly dominates the other ballot pointwise for every realized tally of opponents; it is strictly better on at least one reachable pivotal tally. Full-support independent trembles give that tally positive probability for \(p>0\), so every voter chooses her favorite on every update. Again the truthful profile is fixed. This proves the separate sharp voter and candidate lower bounds.

## Verification

The standalone \`verify.py\` constructs all nine pairs of realized rival ballots for each of the six needed voter/profile cases, multiplies their exact polynomial tremble probabilities \((1-p)\) and \(p/2\), and computes uniform-winner lottery payoffs using rational arithmetic. It independently confirms all six decisive affine coefficient identities, the exact rational witness cycle, and 27 additional rational parameter triples in the open box. It is a finite cross-check of the displayed analytical proof; the all-parameter and lower-bound statements follow from the proof, not sampling. Run \`python verify.py\` with a standard Python 3 installation.

## Relationship to prior work

Weigel, Berriaud, and Wattenhofer (2026), Section 3, define precisely this synchronous vanishing-tremble best-response model. Section 5, Example 5.1, gives a **four-voter** period-two cycle but its public poll stays fixed at \((2,1,1)\); their later constructions produce changing polls with more voters and periods at least three. Their Theorem 5.2 concerns a lower bound on **period-three** active voters and does not prohibit the period-two orbit exhibited here. The present result identifies a smaller, sharply minimal *changing-poll period-two* behavior, with a nonempty open cardinal-utility region. It is not a new proof that cycles exist at all.

Obraztsova et al. (2016) study trembling-hand plurality *equilibria* and give an earlier nonexistence example; the 2026 authors explicitly identify its induced four-voter period-two behavior. Goldberg, Mavronicolas, and Wąs (2026), discussed in the 2026 paper, consider a different top-bottom iterative update rule; their two-voter cycles do not imply two-voter cycling under the present independent uniform-tremble response.

## Limitations

The oscillation uses exactly three candidates and three voters with cardinal utilities in the displayed open region, simultaneous deterministic updates, full-support *uniform* trembling-hand beliefs, and uniform tie lotteries. Changing the tremble destination weights, update timing, or tie-resolution convention may change the phenomenon. The theorem establishes simultaneous minimality for *existence of a truthfully initiated changing-poll period-two cycle* in the defined model, not a classification of every small cycle, a distributional frequency, or a claim about actual human voters. Priority relative to unindexed or inaccessible prior work is not independently established.

## References

1. M. Weigel, D. Berriaud, and R. Wattenhofer, **Trembling toward Duverger: Convergence and Cycles in Synchronous Plurality Dynamics** (2026), arXiv:2610.23330v1, first posted 2026-10-16; especially Sections 3, 5 and Appendix E. https://arxiv.org/html/2610.23330v1
2. S. Obraztsova, Z. Rabinovich, E. Elkind, M. Polukarov, and N. R. Jennings, **Trembling Hand Equilibria of Plurality Voting**, IJCAI (2016), pp. 440–446. https://www.ijcai.org/Proceedings/16/Papers/069.pdf
3. P. W. Goldberg, M. Mavronicolas, and T. Wąs, **Complexity of (Non-)Convergence in Iterative Voting**, AAMAS (2026), pp. 2545–2553; related update model described in Ref. 1, Section 2.
