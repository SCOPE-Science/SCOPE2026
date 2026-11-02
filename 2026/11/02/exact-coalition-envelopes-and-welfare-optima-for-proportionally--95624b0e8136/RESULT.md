# Exact coalition envelopes and welfare optima for proportionally fair obnoxious facilities

## Finding

For every sorted profile of \(n\geq 1\) obnoxious-facility agents on \([0,1]\) and every \(\alpha>0\), the entire set of placements obeying the coalitional \(\alpha\)-proportional-fairness axiom has an explicit prefix--suffix representation. After sorting, its complete closed-interval representation, an exact fairness-violation witness, and an exactly utilitarian-welfare-optimal fair placement can all be computed using \(O(n)\) arithmetic operations and \(O(n)\) space. The fair set has at most \(n+1\) connected components; this bound is attained at \(\alpha=2\) for every \(n\geq1\). The known existence theorem guarantees a nonempty fair set whenever \(\alpha\geq2\); the representation also correctly diagnoses possible infeasibility for smaller \(\alpha\).

## Assumptions and scope

Agents are indexed in nondecreasing order, with \(0\leq x_1\leq\cdots\leq x_n\leq1\); coincident locations are allowed. Their utilities from facility \(y\in[0,1]\) are \(u_i(y)=|y-x_i|\). The coalition-wise \(\alpha\)-PF condition used in the initiating work is: for every nonempty set \(S\subseteq\{1,\ldots,n\}\) and every \(i\in S\),
\[
|y-x_i|\geq\frac{|S|}{\alpha n}-\left(\max_{j\in S}x_j-\min_{j\in S}x_j\right).
\]
This is an ex-post, deterministic, one-facility problem; no strategyproofness is asserted. Arithmetic complexity uses real-number comparisons and additions with the sorted input supplied; sorting arbitrary input adds \(O(n\log n)\) comparisons. For rational inputs and rational \(\alpha\), all outputs have exact rational descriptions.

Set \(h=1/(\alpha n)\), \(z_i=x_i-ih\),
\[
P_i=\max_{1\leq a\leq i}z_a,\qquad Q_i=\min_{i\leq b\leq n}z_b,\qquad
\rho_i=h+P_i-Q_i,
\]
\[
L_i=x_i-\rho_i,\qquad R_i=x_i+\rho_i,
\qquad R_0=0,\quad L_{n+1}=1.
\]
Then all the \(\rho_i\) are strictly positive, both endpoint sequences \((L_i)\) and \((R_i)\) are nondecreasing, and the **exact** feasible set is
\[
\mathcal F_\alpha(\boldsymbol x)
=[0,1]\setminus\bigcup_{i=1}^{n}(L_i,R_i)
=\bigcup_{\substack{0\leq k\leq n\\R_k\leq L_{k+1}}}[R_k,L_{k+1}].
\]
Intervals outside \([0,1]\) cannot appear on the right when nonempty; the two sentinel endpoints are interpreted as above. If none of the displayed intervals is nonempty, the fair set is empty.

Writing \(S_0=0\) and \(S_k=\sum_{j=1}^k x_j\), the utilitarian welfare on every nonempty interval with index \(k\) is
\[
W(y)=\sum_{i=1}^n|y-x_i|=(2k-n)y+S_n-2S_k.
\]
A welfare-optimal placement on this interval is its left endpoint if \(2k<n\), its right endpoint if \(2k>n\), and any point if \(2k=n\). Selecting the greatest of these at most \(n+1\) values gives a global optimum. The complete argmax set is the union of the endpoint maximizers on nonflat intervals and whole intervals when \(2k=n\) and their welfare equals the global maximum.

## Proof

**1. Exact coalitional envelope.** Fix agent \(i\). For any coalition \(S\ni i\), denote its least and greatest indices by \(a\leq i\leq b\). Filling in every index between \(a\) and \(b\) does not change the location range, while increasing the coalition size. Consequently, the strongest requirement on agent \(i\) is given by one of the consecutive coalitions \(\{a,a+1,\dots,b\}\). For such a coalition, the required right-hand side is
\[
(b-a+1)h-(x_b-x_a)
=h+(x_a-ah)-(x_b-bh)=h+z_a-z_b.
\]
The choices of \(a\leq i\) and \(b\geq i\) are independent, so the maximum is precisely \(h+P_i-Q_i=\rho_i\). In particular, selecting \(a=b=i\) yields \(\rho_i\geq h>0\). Attaining indices for the prefix maximum and suffix minimum give a concrete coalition witnessing this exact strongest bound. Therefore all exponentially many coalitional inequalities hold if and only if \(|y-x_i|\geq\rho_i\) for every \(i\), equivalently \(y\notin\bigcup_i(L_i,R_i)\).

**2. Ordered forbidden-ball endpoints.** Let \(d=x_{i+1}-x_i\geq0\) and \(\delta=z_{i+1}-z_i=d-h\). From the definitions of the running maximum and the suffix running minimum,
\[
0\leq P_{i+1}-P_i\leq\max(0,d-h),\qquad
0\leq Q_{i+1}-Q_i\leq\max(0,d-h).
\]
The second inequality follows from \(Q_i=\min(z_i,Q_{i+1})\): if \(Q_{i+1}>Q_i\), then \(Q_i=z_i\) and \(Q_{i+1}-Q_i\leq z_{i+1}-z_i\). Hence
\[
L_{i+1}-L_i=d-(P_{i+1}-P_i)+(Q_{i+1}-Q_i)
\geq d-\max(0,d-h)=\min(d,h)\geq0,
\]
\[
R_{i+1}-R_i=d+(P_{i+1}-P_i)-(Q_{i+1}-Q_i)
\geq\min(d,h)\geq0.
\]
Thus both sequences are ordered, including at coincident locations.

**3. Exact decomposition into gaps.** Since \(\rho_i>0\), a fair placement cannot coincide with an agent. Fix its gap index \(k\), so exactly \(k\) agent indices lie to its left. For indices \(i\leq k\), avoiding their forbidden balls is equivalent to \(y\geq R_i\), hence to \(y\geq R_k\) by orderedness. For \(i>k\), it is equivalent to \(y\leq L_i\), hence to \(y\leq L_{k+1}\). The outer gaps use \(R_0=0\) and \(L_{n+1}=1\). Conversely, every point of \([R_k,L_{k+1}]\) satisfies each inequality, and the positivity of the radii ensures it lies strictly between the adjacent agents whenever both exist. This proves the complete fair-set formula, even if a gap collapses to a singleton or the set is empty.

**4. Exact utilitarian optimization.** In gap \(k\), the first \(k\) summands are \(y-x_i\) and the remaining summands are \(x_i-y\). Summation gives \(W(y)=(2k-n)y+S_n-2S_k\). An affine function is maximized at its endpoint in the direction of its slope, or throughout the interval when the slope is zero. Scanning the at most \(n+1\) nonempty intervals with prefix sums gives every claimed optimizer. A forward maximum scan and backward minimum scan take \(O(n)\) time and space.

**5. Sharp component count.** There are at most \(n+1\) nonempty gaps, separated by open forbidden balls of positive radius. For every \(n\geq1\), choose \(\alpha=2\) and \(x_i=(2i-1)/(2n)\). Here \(h=1/(2n)\) and \(z_i=(i-1)/(2n)\), making \(P_i=Q_i=z_i\), so every \(\rho_i=h\). The forbidden balls are precisely the open intervals \(((i-1)/n,i/n)\). Thus \(\mathcal F_2=\{0,1/n,2/n,\ldots,1\}\), exactly \(n+1\) isolated components.

**6. A strict gap from the weaker fairness axiom.** At \(n=3\), \(\alpha=2\) and \(\boldsymbol x=(0,17/24,3/4)\), the radii are \((1/6,7/24,7/24)\). The full 2-PF set is \([1/6,5/12]\), and its welfare maximum is \(31/24\) at \(1/6\). In contrast, each location occurs only once, so 2-UFS requires just distance at least \(1/6\) from each of the three agents. The endpoint \(y=1\) satisfies 2-UFS and attains the unrestricted utilitarian maximum \(37/24\), but it fails 2-PF for the agent at \(3/4\) because \(1/4<7/24\). This also shows why a welfare optimizer for 2-UFS is not an optimizer for 2-PF.

## Verification

The standalone Python 3 program `verify_pf.py` uses standard-library rational arithmetic. It independently enumerates all nonempty coalitions for each agent and checks the prefix--suffix radii and attaining coalitions, checks endpoint monotonicity, compares the claimed fair-set decomposition at every relevant rational endpoint and interval midpoint, and compares the linear-time welfare optimizer to an independently computed brute-force candidate maximum. It passed \(2{,}548\) rational profile/parameter instances (including ties, \(n\leq8\) and approximations smaller than, equal to, and larger than \(2\)), twelve exact sharpness examples and the strict 2-UFS/2-PF welfare example. Run with `python3 verify_pf.py`. Exhaustive checks are limited to these finite instances; the proof above supplies the universal statements.

## Relationship to prior work

Lam, Aziz, Li, Ramezani and Walsh introduce this obnoxious \(\alpha\)-PF axiom in Section 6 of their paper, prove universal existence at \(\alpha=2\) in Theorem 11 and Appendix S, and distinguish it from 2-UFS via Lemma 5. Their detailed deterministic and randomized welfare analyses concern the weaker 2-IFS/2-UFS axioms; their discussion identifies PF welfare analysis as an extension. The result here concerns **all** PF-feasible placements, optimal deterministic welfare subject to the stronger PF inequalities, explicit binding coalitions and a tight topological bound, rather than re-proving their existence theorem.

Aziz, Lam, Lee and Walsh previously noted for the *classic* (attractive) facility-location PF axiom that it suffices to check contiguous coalitions rather than all subsets (Section 3, footnote 20). This existing consecutive-coalition reduction is acknowledged and is not claimed as new. The additional exact prefix--suffix factorization, ordered forbidden-endpoint geometry, sharp connected-component count, and global welfare algorithm concern the *obnoxious* objective and are the contributions assessed here. The explicit strict 2-UFS/2-PF welfare example rules out simply using the weaker axiom's optimizer.

## Limitations

The model is one-dimensional, metric distances are absolute, and agent weights are equal. The algorithm is for deterministic ex-post feasibility, not randomized feasibility, incentive compatibility, or equilibrium behavior. It does not establish a worst-case price-of-fairness ratio or a social-cost objective outside the stated welfare function. Complexity claims use a sorted representation and exact-real arithmetic. The novelty comparison is based on inspected literature and indexed mathematical records, not an exhaustive proof that no equivalent unpublished or unindexed algorithm exists. Independent external validation has not been performed.

## References

1. Alexander Lam, Haris Aziz, Bo Li, Fahimeh Ramezani, Toby Walsh, *Proportional Fairness in Obnoxious Facility Location*, arXiv:2301.04340, first public version January 11, 2023. https://arxiv.org/abs/2301.04340 . Relevant: Section 6, Definition 12, Lemma 5, Theorem 11, Appendix S, Section 8.
2. Haris Aziz, Alexander Lam, Barton E. Lee, Toby Walsh, *Strategyproof and Proportionally Fair Facility Location*, arXiv:2111.01566, first public version November 2, 2021. https://arxiv.org/abs/2111.01566 . Relevant: Section 3, Definition 6, footnote 20 (the preexisting contiguous-coalition check in the attractive model).
