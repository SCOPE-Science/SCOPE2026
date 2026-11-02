# Exact lottery compatibility and arithmetic periodicity for homogeneous weighted chores

## Finding
Let \(n\ge2\), \(m\ge1\), and let \(w_1,\ldots,w_n>0\) with \(\sum_iw_i=1\). Allocate \(m\) indivisible chores, each of cost one to every agent. A lottery is **admissible** if every realized allocation satisfies weighted envy-freeness up to any chore (WEFX); it is **unbiased** if it is weighted envy-free (WEF) in expectation. Write \(x_i\) for agent \(i\)'s number of chores. Then admissibility and unbiasedness are compatible **exactly** under the following finite test.

1. If \(m<n\), compatibility holds if and only if \(mw_i\le1\) for every \(i\).
2. If \(m=n\), compatibility holds if and only if \(w_i=1/n\) for every \(i\).
3. If \(m>n\), put \(L=m-n\) and form the \(nL\) priority scores \(k/w_i\), indexed by agents \(i\in\{1,\dots,n\}\) and integers \(1\le k\le L\). Let \(\alpha\) be the \(L\)-th smallest score **counting multiplicities**, and define
   \[
   q_i=\#\{k:1\le k\le L,\ k/w_i<\alpha\},\qquad
   T=\{i:\alpha w_i\in\{1,\ldots,L\}\}.
   \]
   Compatibility holds if and only if the following coordinate conditions hold simultaneously:
   \[
   mw_i=1+q_i\quad(i\notin T),\qquad
   1+q_i\le mw_i\le2+q_i\quad(i\in T).
   \]
   If they hold, an exact lottery supported on at most \(n\) WEFX allocations exists and can be computed by elementary rational dependent rounding when the weights are rational.

These tests have two structural consequences. **Arithmetic rigidity:** whenever \(m\ge n\) and an admissible unbiased lottery exists, *every* weight is rational. Thus every irrational entitlement vector is incompatible at every \(m\ge n\). **Periodicity:** if \(w_i=a_i/b\) with positive integers \(a_i\) summing to \(b\), compatibility for \(m\ge n\) is periodic in \(m\) with period \(b\), and in fact the set of feasible count vectors at \(m+b\) is exactly the set at \(m\) translated by \((a_1,\dots,a_n)\).

For two agents with coprime weights \((a/b,(b-a)/b)\), where \(1\le a<b\), the condition simplifies for **every** \(m\ge1\) to
\[
\boxed{\text{compatible}\iff m\equiv0\ \text{or}\ 1\pmod b.}
\]
In particular, among two-agent rational entitlements, equal weights are the only weights allowing compatibility for every chore count. All displayed criteria concern identical unit costs and the strong chore-removal convention; they do not assert compatibility for heterogeneous cost matrices.

## Assumptions and scope
A realized allocation is a partition of all chores, and its count vector \(x\) is an integer vector with \(x_i\ge0\) and \(\sum_i x_i=m\). For chores, WEFX requires for all agents \(i,j\) and each chore in \(i\)'s bundle that \(c_i(X_i\setminus\{e\})/w_i\le c_i(X_j)/w_j\); an empty bundle satisfies the outgoing condition. Because all chores cost one, WEFX and WEF1 coincide on this domain. Ex-ante WEF means \(\mathbb E[x_i]/w_i\le \mathbb E[x_j]/w_j\) for all \(i,j\). Summing the expected counts shows that ex-ante WEF is equivalent to \(\mathbb E[x_i]=mw_i\) for every \(i\). Any allocation is fractionally Pareto optimal here: fractional reassignments preserve total cost \(m\).

## Proof
**Step 1: exact deterministic characterization.** For a unit-cost count vector, the WEFX conditions are precisely
\[
\frac{x_i-1}{w_i}\le\frac{x_j}{w_j}\quad\text{for every }i,j.
\]
When \(x_i=0\), the left side is negative, so the inequality is harmless and agrees with the empty-bundle convention. Rearranging gives
\[
\max_i\frac{x_i-1}{w_i}\le\min_j\frac{x_j}{w_j}.
\]
Consequently, deterministic admissibility is equivalent to the existence of a real \(t\) such that \(x_i-1\le tw_i\le x_i\) for every \(i\).

If \(m<n\), any count \(x_i\ge2\) forces some \(x_j=0\), violating the displayed inequality. Conversely any count vector with only zeroes and ones is admissible. Its convex hull is \(\{z\in[0,1]^n:\sum_i z_i=m\}\), because the extreme points of this slice of a unit cube are exactly the zero-one vectors of sum \(m\). Therefore \(mw\) is in this convex hull exactly if every \(mw_i\le1\). If \(m=n\), a zero count likewise forces another count at least two; hence the only admissible vector is \((1,\ldots,1)\), giving the second criterion.

Now assume \(m>n\). No admissible vector can have a zero count, by the same argument. Set \(y_i=x_i-1\), so \(\sum_i y_i=L\). The inequalities become
\[
\frac{y_i}{w_i}\le\frac{y_j+1}{w_j}\quad\text{for all }i,j.
\]
For each agent consider its increasing priority list \(1/w_i,2/w_i,\ldots\). The \(y_i\) selected scores from that list are \(1/w_i,\ldots,y_i/w_i\), and the first unselected score is \((y_i+1)/w_i\). Thus the displayed inequalities say **exactly** that all selected priority scores are no greater than all unselected scores. Every admissible vector therefore selects the \(L\) globally smallest priority scores, with arbitrary tie-breaking at the \(L\)-th score; conversely every such selection is admissible. Scores with \(k>L\) cannot enter the first \(L\), so the finite list in the finding is exhaustive.

With \(q_i\) scores strictly below \(\alpha\), every admissible count is
\[
 x_i=1+q_i+e_i,
\]
where \(e_i=0\) off the tied set \(T\), \(e_i\in\{0,1\}\) on \(T\), and \(\sum_{i\in T}e_i=L-\sum_iq_i\). An agent has at most one score tied at \(\alpha\). The convex hull of these vectors is obtained by replacing each tied \(e_i\) with a real number in \([0,1]\) while preserving their sum: this is the integer-slice (hypersimplex) description of a uniform matroid base polytope. The required expectation \(mw\) belongs to it precisely when the stated coordinate tests hold. Repeatedly moving mass between two fractional coordinates until one becomes integral gives an explicit convex decomposition; by dimension reduction it can be compressed to at most \(n\) allocations.

**Step 2: rationality.** Suppose \(m>n\) and compatibility holds. For \(i\notin T\), the equality \(mw_i=1+q_i\) makes \(w_i\) rational. Each tied agent satisfies \(\alpha w_i=k_i\) for a positive integer \(k_i\). Since the total weight outside \(T\) is rational, the positive tied mass \(W_T=1-\sum_{i\notin T}w_i\) is rational. Hence \(\alpha=(\sum_{i\in T}k_i)/W_T\) is rational, and so are the tied weights. The case \(m=n\) was already settled.

**Step 3: denominator periodicity.** If \(w_i=a_i/b\) and \(\sum_i a_i=b\), each positive score of agent \(i\) has form \(kb/a_i\). The scores in \((rb,(r+1)b]\) are the scores in \((0,b]\) translated by \(rb\), with exactly \(a_i\) scores from agent \(i\) in each band, including the right endpoint. Thus the sorted global score list repeats after every \(b\) entries under translation by \(b\), preserving the identities and multiplicities of all tied score groups. Selecting \(L+b\) smallest scores rather than \(L\) smallest adds exactly \(a_i\) selections for every agent, with the same choices at the boundary tie. For \(L=0\) the first full band uniquely allocates \(a_i\) extra chores to each agent. Therefore feasible counts translate by \(a\), and the quota vector does too: \((m+b)w=mw+a\). The convex-hull membership criterion is consequently periodic.

**Step 4: two-agent congruence.** Write \(w=w_1\), \(1-w=w_2\), and \(x=x_1\). The deterministic inequalities reduce exactly to
\[
(m-1)w\le x\le(m-1)w+1,
\]
with \(x\) integral. If \((m-1)w\) is integral, both endpoints are admissible and their mixture realizes the target \(mw\). Otherwise the only admissible integer is \(\lceil(m-1)w\rceil\), so unbiasedness is possible exactly when \(mw\) is integral. For \(w=a/b\) in lowest terms these are the congruences \(m\equiv1\pmod b\) and \(m\equiv0\pmod b\). An irrational \(w\) fails both for every \(m\ge2\), in agreement with arithmetic rigidity.

## Verification
The supplied standalone Python 3 script `verify.py` independently enumerates deterministic WEFX occupancy vectors using the original pairwise inequalities and compares them with the priority-score characterization. It additionally tests exact ex-ante feasibility by enumerating barycentric representations of the target count vector over independently enumerated admissible outcomes; it does not rely on the priority score inequalities for this latter check. All arithmetic uses `fractions.Fraction`. Its completed run reports 154 rational weight profiles, 1,120 population-size profiles, 42,000 integer occupancy vectors examined, 560 independent exact lottery-feasibility tests, 770 exact periodicity checks, and 1,827 two-agent modular checks. Invoke `python3 verify.py` from the package directory.

The code checks finite small instances only. The exact infinite-domain statements rest on the proof above. The tie test requires equality of real numbers; computational use with approximate floating-point weights requires exact or certified representations of those comparisons.

## Relationship to prior work
Lin, Wu, and Zhou (2026) prove simultaneous WEFX and fractional Pareto optimality for binary additive chores and exhibit two unequal-weight agents with two identical chores for which ex-ante WEF and ex-post WEF1 cannot coexist. The present characterization retains that obstruction but distinguishes exactly which entitlement vectors and chore counts permit an unbiased lottery; it establishes a general tie-polytope test, rationality obstruction, and denominator periodicity, none of which is stated in their inspected Section 4 counterexample or their other relevant theorem sections.

The deterministic score rule coincides with the classical Adams divisor ranking in apportionment: this correspondence is a substantive antecedent, not a claim of a newly invented allocation algorithm. Cembrano et al. analyze deterministic stationary divisor outcomes and randomization over divisor parameters, while Correa et al. construct quota-respecting ex-ante proportional lotteries with different permissible ex-post support. Neither inspected source states the fixed-Adams-support unbiasedness criterion here. The result would be covered if an earlier source already established that criterion or an equivalent characterization of the convex hull of tied Adams outcomes; this is a residual literature risk, not ruled out solely by search.

## Limitations
The characterization concerns fully identical strictly positive unit chore costs, complete allocations, positive normalized entitlements, and ex-ante weighted envy-freeness. It does not cover agent-dependent binary costs, mixed goods and chores, or other weighted-EFX conventions. The rational-weight periodicity asserts a period, not necessarily the least period. Its finite feasibility test requires exact comparisons of score ties. No computational experiment is claimed to establish the all-parameter theorem, and no independent audit has been performed.

## References
1. Zehan Lin, Xiaowei Wu, Shengwei Zhou, *Revisiting EFX and fPO Allocations for Binary Chores*, arXiv:2609.13970v1 (public submission 12 September 2026), especially Definitions 2.2–2.4 and Section 4. https://arxiv.org/html/2609.13970
2. Javier Cembrano, José Correa, Ulrike Schmidt-Kraepelin, Alexandros Tsigonias-Dimitriadis, Victor Verdugo, *New Combinatorial Insights for Monotone Apportionment*, Mathematics of Operations Research (2025), Sections 3–4. https://www.dii.uchile.cl/~jcorrea/papers/Journals/2025CCSTV.pdf
3. José Correa, Paul Gölz, Ulrike Schmidt-Kraepelin, Jamie Tucker-Foltz, Victor Verdugo, *Monotone Randomized Apportionment*, arXiv:2405.03687v1 (2024), Sections 2–4. https://arxiv.org/html/2405.03687v1
4. Mithun Chakraborty, Ayumi Igarashi, Warut Suksompong, Yair Zick, *Weighted Envy-Freeness in Indivisible Item Allocation*, arXiv:1909.10502 (2019); weighted picking-sequence/Adams connection. https://arxiv.org/abs/1909.10502
