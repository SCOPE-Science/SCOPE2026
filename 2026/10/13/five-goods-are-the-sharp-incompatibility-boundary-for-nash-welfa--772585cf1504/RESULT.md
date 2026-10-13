# Five goods are the sharp incompatibility boundary for Nash welfare and leximin under positive bi-valued utilities
## Finding
Consider two agents and a finite set of indivisible goods. Utilities are additive, every good is allocated to exactly one agent, and every item value lies in
\[
\{1,2\}.
\]

For an allocation \(A\), let its utility vector be \((u_1(A),u_2(A))\). A maximum Nash welfare allocation uses the standard convention of first maximizing the number of agents receiving positive utility and then maximizing the product of their positive utilities. In this positive-valued two-agent setting with at least two goods, this is simply maximization of
\[
u_1(A)u_2(A).
\]
A leximin allocation lexicographically maximizes the sorted utility vector
\[
(\min\{u_1(A),u_2(A)\},\max\{u_1(A),u_2(A)\}).
\]
Write \(M(I)\) and \(L(I)\) for the sets of MNW and leximin allocations of an instance \(I\).

For every such instance with at most \(4\) goods,
\[
M(I)\cap L(I)\ne\varnothing.
\]
The bound is sharp. With \(5\) labeled goods there are
\[
4^5=1024
\]
labeled valuation profiles, because each good independently has one of the four valuation types
\[
(1,1),\quad(1,2),\quad(2,1),\quad(2,2).
\]
Exactly
\[
100
\]
of these profiles have disjoint optimizer sets,
\[
M(I)\cap L(I)=\varnothing.
\]
Thus the exact incidence is
\[
\frac{100}{1024}=\frac{25}{256}.
\]

Let \((a,b,c,d)\) count goods of the four types above. Up to permuting goods and swapping the two agents, the complete first incompatibility layer consists of exactly four classes:
\[
(0,0,4,1),\qquad
(0,1,4,0),\qquad
(1,0,3,1),\qquad
(1,1,3,0).
\]
Their orbit sizes under goods permutations and agent swap are respectively
\[
10,\quad10,\quad40,\quad40,
\]
which sum to \(100\).

Every one of these \(100\) profiles has the same welfare conflict. Every MNW optimum has sorted utility profile
\[
(3,6),
\]
whereas every leximin optimum has sorted utility profile
\[
(4,4).
\]
The Nash products are therefore \(18\) and \(16\), respectively.

A compact witness is
\[
v_1=(1,1,1,1,2),\qquad v_2=(1,2,2,2,1).
\]
The unique MNW allocation gives goods \(1,5\) to agent \(1\) and goods \(2,3,4\) to agent \(2\), yielding
\[
(u_1,u_2)=(3,6).
\]
Leximin instead gives agent \(1\) good \(5\) together with any one of goods \(1,2,3,4\) that has value \(1\) to agent \(1\), subject to agent \(2\) retaining two of its value-\(2\) goods. For the displayed witness there are exactly three such allocations, and all yield
\[
(u_1,u_2)=(4,4).
\]
Hence no allocation is optimal for both criteria.

A weaker difference appears earlier. With \(3\) goods there are \(8\) profiles for which \(L(I)\) is a proper subset of \(M(I)\), and with \(4\) goods there are \(16\); nevertheless the intersection is always nonempty. Five goods are therefore the exact first point of **incompatibility**, not merely the first point at which the optimizer sets can differ.

## Assumptions and scope
There are exactly two agents. Goods are indivisible, all goods are allocated, and utilities are additive.

Each per-good value is either \(1\) or \(2\). This is the simplest strictly positive two-level additive domain. It differs from the binary \(\{0,1\}\) domain, where zero values permit goods that an agent does not value.

The generalized MNW convention is used so that the definition also covers the one-good base case. Because all item values here are positive, every welfare optimum for two or more goods gives both agents positive utility, so ordinary product maximization and generalized MNW coincide there.

The theorem classifies incompatibility of the **full optimizer sets**. It does not impose a tie-breaking rule within MNW or leximin.

## Proof
For a profile, let \((a,b,c,d)\) be the numbers of goods of types
\[
(1,1),\ (1,2),\ (2,1),\ (2,2).
\]
Suppose agent \(1\) receives \(x_a,x_b,x_c,x_d\) goods of these four types. Then
\[
u_1=x_a+x_b+2x_c+2x_d,
\]
and agent \(2\)'s utility is
\[
u_2=(a-x_a)+2(b-x_b)+(c-x_c)+2(d-x_d),
\]
where
\[
0\le x_a\le a,\quad0\le x_b\le b,\quad0\le x_c\le c,\quad0\le x_d\le d.
\]
Thus, for a fixed count vector, all feasible utility pairs are obtained by a finite rectangular enumeration of these four integers.

The verifier performs the proof by two independent finite routes.

First, it enumerates every labeled valuation profile for \(1\) through \(5\) goods and, for each profile, every complete allocation. MNW and leximin optimizer sets are obtained directly from the utility pairs. The exact relation census is:
\[
\begin{array}{c|r|r|r}
\text{goods}&M=L&L\subsetneq M&M\cap L=\varnothing\\
\hline
1&4&0&0\\
2&16&0&0\\
3&56&8&0\\
4&240&16&0\\
5&892&32&100
\end{array}
\]
No other relation type occurs through five goods.

Second, independently of good labels, it enumerates every composition
\[
a+b+c+d=m
\]
and all feasible quadruples \((x_a,x_b,x_c,x_d)\). Each bad count vector is then weighted by its multinomial number of labeled profiles. This route reproduces the same disjointness counts
\[
0,0,0,0,100
\]
for \(m=1,2,3,4,5\).

At \(m=5\), the bad count vectors are exactly
\[
\begin{aligned}
&(0,0,4,1),(0,1,4,0),(0,4,0,1),(0,4,1,0),\\
&(1,0,3,1),(1,1,3,0),(1,3,0,1),(1,3,1,0).
\end{aligned}
\]
Swapping the agents interchanges the second and third coordinates. Therefore these eight vectors reduce to the four canonical classes listed in the Finding.

Their multinomial counts, paired with their agent-swapped vectors, give orbit sizes \(10,10,40,40\). Direct allocation enumeration and the count-vector calculation both show that all bad profiles have MNW utility profile \((3,6)\) and leximin utility profile \((4,4)\).

## Verification
The embedded `verify_mnw_leximin_bivalued_boundary.py` uses only the Python standard library and exact integer arithmetic.

It verifies:
- all \(4^m\) labeled two-agent \(\{1,2\}\)-valuation profiles for every \(1\le m\le5\);
- every complete allocation of every profile;
- the complete relation census between MNW and leximin optimizer sets;
- zero disjoint optimizer sets through four goods;
- exactly \(100\) disjoint profiles at five goods;
- an independent count-vector reconstruction using all compositions \(a+b+c+d=m\) and multinomial weights;
- exactly eight bad count vectors and four classes after swapping agents;
- orbit sizes \(10,10,40,40\);
- the universal first-conflict utility profiles \((3,6)\) and \((4,4)\);
- the explicit witness and all of its optimizer allocations.

Run:

`python3 verify_mnw_leximin_bivalued_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Ramezani and Endriss study Nash social welfare for indivisible multiagent resource allocation and describe the Nash product as combining efficiency and fairness considerations. This supplies an early resource-allocation formulation of the objective.

Caragiannis, Kurokawa, Moulin, Procaccia, Shah, and Wang establish maximum Nash welfare as a central rule for fair division of indivisible goods with additive valuations.

Halpern, Procaccia, Psomas, and Shah prove that, for binary additive valuations \(v_i(g)\in\{0,1\}\), the sets of MNW and leximin allocations coincide. Benabbou, Chakraborty, Igarashi, and Zick extend related MNW/leximin equivalence structure to matroid-rank valuations, whose marginal gains are binary; this does not cover positive additive values \(\{1,2\}\).

Recent work of Lin, Wu, and Zhou explicitly contrasts MNW and leximin in bi-valued instances and shows sharply different EFX, GMMS, and PMMS approximation behavior. Its leximin appendix studies asymptotic fairness guarantees and examples with variable numbers of goods. It does not, in the inspected text, state the smallest number of goods at which the MNW and leximin optimizer sets become disjoint, nor the exact two-agent \(\{1,2\}\) first-layer census proved here.

The contribution here is therefore restricted to that finite structural boundary: coexistence of an MNW/leximin optimum through four goods, exactly \(100\) incompatible labeled profiles at five goods, four symmetry classes, and the universal \((3,6)\) versus \((4,4)\) utility conflict.

## Limitations
The theorem concerns exactly two agents and item values exactly in \(\{1,2\}\).

The exhaustive classification stops at five goods. It gives no density or structural claim for larger instances or other bi-valued ratios \(\{1,k\}\).

The result concerns optimizer-set intersection, not EFX, MMS, PMMS, GMMS, strategyproofness, or computational complexity.

The literature search cannot exclude an equivalent small-instance observation in an unindexed thesis, code corpus, exercise, or supplementary table.

## References
1. S. Ramezani and U. Endriss, “Nash Social Welfare in Multiagent Resource Allocation,” *BNAIC 2009*, pp. 359–360; expanded in *Agent-Mediated Electronic Commerce*, LNBIP 59, 117–131, 2010. DOI: 10.1007/978-3-642-15117-0_9.
2. I. Caragiannis, D. Kurokawa, H. Moulin, A. D. Procaccia, N. Shah, and J. Wang, “The Unreasonable Fairness of Maximum Nash Welfare,” *EC 2016*, 305–322. DOI: 10.1145/2940716.2940726.
3. D. Halpern, A. D. Procaccia, A. Psomas, and N. Shah, “Fair Division with Binary Valuations: One Rule to Rule Them All,” arXiv:2007.06073, 2020.
4. N. Benabbou, M. Chakraborty, A. Igarashi, and Y. Zick, “Finding Fair and Efficient Allocations for Matroid Rank Valuations,” arXiv:2003.07060; SAGT 2020.
5. Z. Lin, X. Wu, and S. Zhou, “When Maximum Nash Welfare Becomes Strongly Fair: Bi-valued Goods,” arXiv:2610.00122, 2026.
