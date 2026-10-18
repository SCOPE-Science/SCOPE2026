# Exact hub consolidation and stacking on friendship graphs

## Finding
For every integer \(k\ge2\), let \(F_k=K_1\vee(kK_2)\) be the friendship graph, with common vertex \(o\) and pairs of outer vertices \((u_i,v_i)\), \(1\le i\le k\). A pebbling move along an edge removes two pebbles from its source and places one at its destination. A configuration \(c\) assigns nonnegative integers to all vertices. Write \(h=c(o)\), \(a_i=c(u_i)\), and \(b_i=c(v_i)\).

Define, for nonnegative integers \(a,b\),
\[
\delta(a,b)=\begin{cases}
1,&(a,b)=(1,1),\\
1,&\text{exactly one coordinate is zero and the other is odd},\\
0,&\text{otherwise},
\end{cases}\qquad
f(a,b)=\left\lfloor\frac a2\right\rfloor+
\left\lfloor\frac b2\right\rfloor-\delta(a,b).
\]
Define the *hub surplus*
\[
\mathcal E(c)=h+\sum_{i=1}^{k}f(a_i,b_i).
\]
Then the following exact statements hold:

1. **Prescribed-hub consolidation.** A positive stack supported only at \(o\) is reachable from \(c\) if and only if \(\mathcal E(c)\ge1\).
2. **Free-destination consolidation.** Some positive stack at an arbitrary vertex is reachable from \(c\) if and only if \(\mathcal E(c)\ge1\), or \(c\) is already supported on a single vertex.
3. **Sharp stacking number.** With \(\operatorname{stack}(G)\) denoting the least positive integer \(t\ge2\) for which every size-\(t\) configuration is stackable,
\[
\boxed{\operatorname{stack}(F_k)=4k.}
\]
The hub criterion gives a complete decision rule for *individual configurations*, not merely the uniform threshold. The elementary case \(k=1\) is also governed by the same criterion and reduces to \(\operatorname{stack}(K_3)=4\), already known.

## Assumptions and scope
All graphs are finite, simple, and undirected. There are exactly \(k\) triangles with a single common vertex, no additional edges, and no initial restriction on pebble multiplicities. Reachability means a finite sequence of legal moves; a stack must have strictly positive size. The original definition of stacking with an unconstrained final vertex is used, while part 1 imposes the additional requirement that the final vertex be \(o\). No claim about the distinct *clearing number* (which demands a final configuration of size exactly one) is made.

## Proof
**Lemma 1 (monotone hub surplus).** Every legal pebbling move weakly decreases \(\mathcal E\).

For \(a\ge2\), the exceptional indicator satisfies \(\delta(a,b)\le\delta(a-2,b)\). Therefore a move \(u_i\to o\) changes the surplus by
\[
1+f(a_i-2,b_i)-f(a_i,b_i)=
\delta(a_i,b_i)-\delta(a_i-2,b_i)\le0.
\]
A move \(o\to u_i\) changes it by
\[
-2+f(a_i+1,b_i)-f(a_i,b_i)
=-2+(a_i\bmod2)+\delta(a_i,b_i)-\delta(a_i+1,b_i)\le0.
\]
For a move \(u_i\to v_i\), with \(a_i\ge2\), the change equals
\[
-1+(b_i\bmod2)+\delta(a_i,b_i)-\delta(a_i-2,b_i+1).
\]
If \(b_i\) is even, this is nonpositive since \(\delta(a_i,b_i)\le1\). If \(b_i\) is odd, then \(a_i\ge2\) forces \(\delta(a_i,b_i)=0\), so it is also nonpositive. Interchanging \(a_i,b_i\) covers the opposite orientation of each edge. This exhausts all move types, proving the lemma.

**Lemma 2 (exact local elimination).** For a single outer pair with counts \((a,b)\), the pair can be emptied while changing the hub count by exactly \(f(a,b)\), under these conditions: when \(f(a,b)\ge1\), no initial hub pebble is needed; when \(f(a,b)=0\), either \((a,b)=(0,0)\) requires nothing or the pair is \((3,0)\) or \((0,3)\) and one hub pebble suffices; when \(f(a,b)=-1\), two hub pebbles suffice.

Here is an explicit construction, with each arrow denoting one legal pebbling move. If both outer counts are even, move half of each pile directly to the hub. If one count is odd and the other is positive and even, move once from the positive even pile to the odd pile; both remaining piles become even and may be sent to the hub. If both counts are odd and at least one is at least three, move once from that pile to the other and then once back: the resulting outer counts are both even; send both to the hub. These operations deliver \(\lfloor a/2\rfloor+\lfloor b/2\rfloor\) hub pebbles.

If exactly one outer pile contains \(2m+1\) pebbles and the other is empty, then for \(m\ge2\) send \(m\) pebbles to the hub, leaving one on the outer vertex; use one hub-to-outer move followed by one outer-to-hub move, leaving \(m-1=f(2m+1,0)\) at the hub. For \(m=1\), the same procedure requires one initial hub pebble and returns it. For \(m=0\), one hub-to-outer move and one return move require two initial hub pebbles and consume one. Finally, for the pair \((1,1)\), two initial hub pebbles permit hub-to-first-outer, first-to-second-outer, second-to-hub, consuming one hub pebble. These cases cover every nonnegative pair. Any hub pebbles already present can be left untouched during the constructions that need none.

**Lemma 3 (prescribed-hub criterion).** By Lemma 1, a configuration reaching \(q\ge1\) pebbles only at \(o\) must have \(\mathcal E(c)\ge q\ge1\). Conversely, assume \(\mathcal E(c)\ge1\). Eliminate every pair with \(f(a_i,b_i)>0\) first, using Lemma 2 without any hub reserve. The hub then contains
\[
H=h+\sum_{f(a_i,b_i)>0}f(a_i,b_i).
\]
Let \(m\) be the number of pairs with \(f=-1\). Because all remaining pair contributions are zero or minus one, \(H-m=\mathcal E(c)\ge1\); hence \(H\ge m+1\). Eliminate all zero-surplus pairs using the available hub pebble when needed. Next eliminate the \(m\) negative-surplus pairs. Before each such elimination the hub contains at least two pebbles, since it starts with at least \(m+1\) and each operation consumes exactly one. The final configuration has exactly \(\mathcal E(c)\ge1\) pebbles at \(o\) and none elsewhere. This proves part 1.

**Lemma 4 (free-destination criterion).** If a configuration is already supported at one vertex, it is stackable. Lemma 3 covers configurations with \(\mathcal E\ge1\). For necessity, consider any successful sequence from a configuration not initially stacked and take the *first* time at which a stack appears. Its last step has a source with exactly two pebbles, a destination containing at least one pebble beforehand, and no other occupied vertices. Thus the first stack has size \(q\ge2\). If the destination is \(o\), its surplus is \(q\ge1\). If the destination is an outer vertex, its surplus is \(f(q,0)\ge1\) whenever \(q\ge2\) and \(q\ne3\). In the exceptional case \(q=3\), the immediately preceding configuration has exactly two pebbles at the destination and exactly two at an adjacent source. When that source is the hub, its surplus is \(2+f(2,0)=3\); when the source is the other vertex of the same outer pair, its surplus is \(f(2,2)=2\). In every case a state of surplus at least one occurs on the successful path. Lemma 1 then forces the initial surplus to be positive, proving part 2.

**Theorem (threshold).** For every pair of nonnegative counts,
\[
2f(a,b)\ge a+b-4,
\]
with equality if and only if \((a,b)=(1,1)\). This follows immediately by separating the even-even, even-odd, odd-odd, and one-odd-one-zero cases in the definition of \(f\). For any configuration of total size \(t\), summation gives
\[
2\mathcal E(c)\ge 2h+\sum_i(a_i+b_i-4)
=h+t-4k.
\]
If \(t\ge4k\), this implies \(\mathcal E(c)\ge0\). Equality at zero would require \(h=0\), \(t=4k\), and every outer pair to be \((1,1)\), but then \(t=2k\), a contradiction. Hence \(\mathcal E(c)\ge1\), and Lemma 3 stacks every configuration of size at least \(4k\) at the hub.

For the reverse inequality, let \(k\ge2\) and take the configuration with \(2k+1\) pebbles on \(u_1\), none on \(o,v_1\), and one on each vertex \(u_i,v_i\) for \(2\le i\le k\). Its total size is \(4k-1\); its surplus is
\[
\mathcal E(c)=f(2k+1,0)+(k-1)f(1,1)=(k-1)-(k-1)=0.
\]
It occupies several vertices and is therefore nonstackable by Lemma 4. Thus \(\operatorname{stack}(F_k)\ge4k\). Together with the upper bound this proves part 3. \(\square\)

## Verification
The standalone program `verify_friendship.py` implements independent exhaustive backward dynamic programming on all pebbling configurations of sizes from \(1\) to \(4k\) for \(k=1,2,3,4\). It compares direct reachability to the hub and to any stack with the two closed criteria and checks the sharp nonstackable witnesses. It examined 2,094,681 configurations in total; no discrepancy occurred. It also separately tested the indicator inequalities, one-step surplus monotonicity, and the sharp bound on \(f\) for all 3,721 ordered outer count pairs \((a,b)\) with coordinates at most \(60\). These are finite consistency checks. The proofs above establish the infinite statements without relying on experiments.

Reproduce with `python verify_friendship.py` using only a standard Python installation. No external data or solver is required.

## Relationship to prior work
Csernák and Soukup introduced this unconstrained-destination stacking parameter in *Stacking and Clearing in Graph Pebbling* (arXiv:2604.22341v1, April 24, 2026). Their complete-graph, complete-bipartite, complete-multipartite and path formulas, together with general independence-number bounds, are prior results. The friendship graph for \(k\ge2\) is none of those graph families: its outer nonedges and central triangles preclude a complete multipartite representation. Its independence number is \(k\); the published general bound \(\operatorname{stack}(G)\ge3\alpha(G)+1\) gives \(3k+1\), below the exact \(4k\) for \(k\ge2\). The cited paper does not state the friendship-graph stacking number or this hub-surplus criterion.

Prabha and Sandhiya's *Cover pebbling number of Comb, Friendship and Helm graphs* (2021) computes a different parameter: every vertex must receive a pebble, rather than all pebbles being consolidated onto one vertex. Their friendship-graph cover-pebbling result therefore neither states nor implies the present classification. Standard rooted pebbling (reach at least one pebble at a prescribed vertex while retaining others) also differs from the requirement to empty all other vertices. Searches for these equivalent or potentially dominating formulations have not identified another covering theorem.

## Limitations
The theorem concerns friendship graphs with nonnegative integral pebbling configurations under the \(2\)-for-\(1\) undirected move rule. It does not classify arbitrary cactus or block graphs, their clearing numbers, or the number of successful pebbling sequences. The computational checks cover only the explicit finite ranges given above. Bibliographic originality is assessed against accessible indexed records and inspected literature; an unindexed equivalent theorem remains possible. No independent external audit is claimed.

## References
1. T. Csernák and L. Soukup, *Stacking and Clearing in Graph Pebbling*, arXiv:2604.22341v1 (first public version: 2026-04-24), https://arxiv.org/html/2604.22341v1 . Relevant material: definitions and Section 1; general bounds in Sections 3 and 5; complete multipartite formulas in Section 8; computational discussion in Section 11.
2. R. Prabha and B. Sandhiya, *Cover pebbling number of Comb, Friendship and Helm graphs*, Journal of Physics: Conference Series 1770 (2021), 012064. DOI:10.1088/1742-6596/1770/1/012064. Accessible author-posted full text: https://www.researchgate.net/publication/350731857_Cover_pebbling_number_of_Comb_Friendship_and_Helm_graphs .
