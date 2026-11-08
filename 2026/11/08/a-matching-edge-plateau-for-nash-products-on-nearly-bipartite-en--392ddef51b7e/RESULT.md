# A matching-edge plateau for Nash products on nearly bipartite enemy graphs

## Finding
Let \(a\ge4\), \(b\ge2\), and \(1\le t\le\lfloor a/2\rfloor\) be integers. Start with the complete bipartite enemy graph \(K_{a,b}\) on labeled parts \(A,B\), and add \(t\) pairwise vertex-disjoint enemy edges inside \(A\). Every other unordered pair of distinct players is friendly. Under the symmetric aversion-to-enemies game with \(N=a+b\) players, mutual friendship value \(+1\), and mutual enemy value \(-N\), let \(P_t(a,b)\) be the maximum product of the players' coalition utilities over all individually rational partitions.

Then every maximizer has exactly three coalitions: the whole of \(B\) and two mutually independent subsets of \(A\). The exact optimum is
\[
P_t(a,b)=(b-1)^b\begin{cases}
(a-3)^{a-2},&t=1,\\
(t-1)^t(a-t-1)^{a-t},&2\le t\le\lfloor a/2\rfloor.
\end{cases}
\]
For \(t=1\) the two \(A\)-coalition sizes are \(a-2,2\); for \(t\ge2\) they are \(a-t,t\). The number of maximizing partitions of the labeled players, with unordered coalitions, equals
\[
M_t(a)=\begin{cases}
2,&t=1,\ a=4,\\
2(a-2),&t=1,\ a>4,\\
2^{t-1},&t\ge2,\ a=2t,\\
2^t,&t\ge2,\ a>2t.
\end{cases}
\]
In particular, \(P_1(a,b)=P_2(a,b)\) for every \(a\ge4\), although the optimizer counts differ for \(a\ge5\). For fixed \(a\), the optimum strictly decreases as the number of added matching edges increases from \(2\) to \(3\), and thereafter, whenever those parameters exist.

Without the added matching, the optimum is \(P_0(a,b)=(a-1)^a(b-1)^b\), attained by the two original bipartition coalitions. Thus, for fixed \(b\) and \(a\to\infty\),
\[
\frac{P_1(a,b)}{P_0(a,b)}=\frac{P_2(a,b)}{P_0(a,b)}\sim\frac{e^{-2}}{a^2},
\qquad
\frac{P_t(a,b)}{P_0(a,b)}\sim \frac{(t-1)^t e^{-t}}{a^t}\quad(t\ge2\text{ fixed}).
\]
These are ratios of **Nash products**, not the ratios of their \(N\)-th roots.

## Assumptions and scope
Coalition partitions are disjoint nonempty subsets covering all \(N\) labeled players. For player \(i\) in coalition \(S\), \(u_i(S)=\sum_{j\in S\setminus\{i\}}v_{ij}\), where \(v_{ij}=v_{ji}\in\{1,-N\}\). Individual rationality means \(u_i(S)\ge0\) for every player. Zero utility is permitted, but any singleton makes the product zero. The graph \(K_{a,b}\) and its added matching describe **enemy** pairs, not friendly pairs. No edges are added inside \(B\), and each added edge has two distinct endpoints disjoint from all other added edges.

## Proof
**1. Enemy edges cannot occur inside an individually rational coalition.** If a coalition of size \(s\le N\) contains an enemy of player \(i\), then \(u_i(S)\le(s-2)-N\le-2\). Hence every individually rational coalition is an independent set of the enemy graph, and each player in an independent set of size \(s\) has utility exactly \(s-1\). The product of a partition with coalition sizes \(s_1,\ldots,s_k\) is therefore \(\prod_{j=1}^k(s_j-1)^{s_j}\), with value zero when a singleton occurs.

**2. Separate the two parts.** The complete cross-part enemy edges prohibit every mixed \(A\)-\(B\) coalition. In any positive-product partition, merging two separate all-friendly \(B\)-coalitions strictly improves every involved player's utility, and thus strictly increases the product. Therefore the unique optimal \(B\)-coalition is all of \(B\), with factor \((b-1)^b\). The remaining problem is an independent-set partition of \(A\), where the only forbidden internal pairs are the \(t\) disjoint matching edges.

**3. A convex majorization bound.** For \(x\ge0\), define \(h(x)=0\) when \(0\le x\le2\), and \(h(x)=x\log(x-1)\) when \(x\ge2\). This continuous function is convex: its left derivative at \(2\) is \(0\), its right derivative is \(2\), and on \(x>2\) its second derivative is \((x-2)/(x-1)^2\ge0\). For every positive-product partition, the log product contributed by \(A\) is \(\sum_j h(s_j)\), with every \(s_j\ge2\).

Every independent subset of \(A\) contains at most one endpoint of each matching edge, so its size is at most \(a-t\). If \(t=1\), the stronger restriction \(s_j\le a-2\) holds for every positive-product partition: a class of size \(a-1\) would force a singleton complement. Put \(L=a-2\) for \(t=1\), and \(L=a-t\) for \(t\ge2\). Since \(2\le a-L\le L\), the vector \((L,a-L,0,\ldots,0)\) majorizes any feasible positive-product size vector (pad with zeros). Convexity gives
\[
\sum_j h(s_j)\le h(L)+h(a-L).
\]
The inequality is strict unless the positive sizes are precisely \(L,a-L\): the only flat part of \(h\) is on \([0,2]\), and all actual coalition sizes are at least \(2\), so a differing partition cannot attain equality through a nontrivial split into allowable positive sizes. This proves an upper bound on both the product and the possible maximizing coalition-size pattern.

**4. Attain the bound and count the maximizers.** For \(t\ge2\), put exactly one endpoint from each matching edge into the small \(A\)-coalition of size \(t\), and put the other endpoints and all \(a-2t\) unmatched vertices into the large \(A\)-coalition of size \(a-t\). The construction is independent on both sides and attains the upper bound. There are \(2^t\) choices; if \(a=2t\), swapping the two equal-sized coalitions duplicates each unordered partition, giving \(2^{t-1}\).

For \(t=1\), let the size-two coalition consist of one of the two endpoints of the added enemy edge and one of the \(a-2\) unmatched vertices. The complement is independent of size \(a-2\). This gives \(2(a-2)\) choices; when \(a=4\), the two size-two coalitions are interchangeable, so there are \(a-2=2\) unordered partitions. This proves the optimum and the counts. It also shows every optimizer has exactly three coalitions, including the \(B\)-coalition.

**5. Plateau and decay.** The formula at \(t=2\) is \((t-1)^t(a-t-1)^{a-t}=(a-3)^{a-2}\), identical to \(t=1\). For \(t\ge2\), strict convexity on sizes larger than \(2\) shows that shifting one unit from \(a-t\) to \(t\) strictly reduces the logarithmic product whenever \(t+1\le\lfloor a/2\rfloor\). Finally, \((1-c/(a-1))^{a-d}\to e^{-c}\) for fixed positive integers \(c,d\); applying this with \(c=2\) for the plateau and \(c=t\) for the general matching case proves the displayed asymptotics.

## Verification
Run `python3 VERIFY.py` with Python 3 and its standard library. The supplied standalone script checks the exact optimum, optimizer counts, and unique optimal size pattern by enumerating every set partition, not just partitions into three coalitions. Its separate first stage checks all \(4\le a\le10\) and \(1\le t\le\lfloor a/2\rfloor\) on the internal \(A\)-graph; its second stage checks complete enemy graphs for \(4\le a\le6\), \(2\le b\le3\). It visits 772,452 set partitions across 37 exact instances and reports `VERIFY_OK`. A direct exact-integer plateau identity is additionally tested for \(4\le a\le100\). These finite checks support but do not establish the infinite-parameter theorem; that conclusion rests on the proof above.

## Relationship to prior work
Pagano and Schlenga (2026) introduce Nash welfare for additively separable hedonic games, prove general complexity and approximation results, and study the boundary between two and three permitted coalitions. Their publicly accessible abstract does not state a matching-perturbed complete-bipartite exact optimum or optimizer enumeration. Detailed public secondary descriptions discuss the general positivity criterion and two-coalition algorithms; these do not directly imply the present three-coalition product or its plateau. **The complete primary text was not accessible during this comparison, so coverage by an uninspected result or appendix remains an explicit priority risk.**

Elkind, Flammini and Varricchio (2025) study egalitarian welfare in friends-and-enemies games; their minimum-utility objective differs from the Nash product. A separate graph-coloring literature concerns feasible partitions or chromatic numbers; those invariants do not by themselves determine the product and its number of attaining partitions.

## Limitations
The result assumes symmetric \(+1/-N\) utilities, complete cross-part hostility, and disjoint added matching edges on one side only. It does not classify arbitrary added edges, asymmetric valuations, or Nash stability. It counts only positive-product maximizers and does not enumerate zero-product individually rational partitions outside the stated domain. The paper-priority comparison was limited by inaccessible full primary text and potentially unindexed literature. Neither the finite verifier nor absence of search hits proves originality.

## References
- M. Pagano and A. Schlenga, *Nash Welfare in Additively Separable Hedonic Games*, first posted 18 May 2026, arXiv:2605.19030. https://arxiv.org/abs/2605.19030
- E. Elkind, M. Flammini and G. Varricchio, *Maximizing the Egalitarian Welfare in Friends and Enemies Games*, first posted 23 December 2025, arXiv:2512.20261. https://arxiv.org/abs/2512.20261
