# Exact Nash spectrum and linear welfare loss on double-star distance games

## Finding

For every pair of integers \(a,b\ge1\), let \(D_{a,b}\) be the double-star tree, with adjacent hubs \(u,v\), \(a\) leaves adjacent only to \(u\), and \(b\) leaves adjacent only to \(v\). In the non-normalized score-based social distance game with distance scores \((1,0,-1)\), the **entire collection of Nash-stable partitions** consists of precisely the following:

1. The two complete stars (one coalition around each hub).
2. The coalition of both hubs and all \(a\) left leaves, with the \(b\) right leaves singleton.
3. The coalition of both hubs and all \(b\) right leaves, with the \(a\) left leaves singleton.
4. For every left leaf \(x\) and right leaf \(y\), the four-agent coalition \(\{u,v,x,y\}\), with all remaining leaves singleton.

Therefore the exact labeled Nash-equilibrium count and its welfare multiset are

\[
\#\mathrm{NS}(D_{a,b})=ab+3,
\qquad
\{\!\{\mathrm{SW}(\pi):\pi\in\mathrm{NS}\}\!\}
=\{\!\{2(a+b),2(a+1),2(b+1),\underbrace{4,\ldots,4}_{ab\ \text{copies}}\}\!\}.
\]

The global maximum welfare (even without stability) is \(2(a+b)\). Consequently the price of stability equals \(1\) and the price of anarchy equals \((a+b)/2\). In the balanced family \(a=b=t\), the price of anarchy is exactly \(t\) despite a fixed diameter of three and treewidth one. The social optimum is unique when \(a,b\ge2\); it has exactly two optimal partitions when precisely one of \(a,b\) equals one, and four when \(a=b=1\).

## Assumptions and scope

All players are vertices of the labeled simple tree \(D_{a,b}\), where \(a,b\ge1\). A strategy outcome is an **unordered partition** \(\pi\) into nonempty coalitions. Distances are measured in the subgraph induced by each player's current coalition (not the ambient graph). An agent's utility is the sum, over other members of its coalition, of the score at the induced distance: \(s(1)=1\), \(s(2)=0\), \(s(3)=-1\), and \(s(d)=-\infty\) for distances exceeding three or disconnected pairs. A singleton's utility is zero; a disconnected coalition gives its members utility \(-\infty\). Utilities are *not* divided by coalition size.

A Nash deviation moves one player unilaterally to any other current coalition or to a newly created singleton, and is profitable if and only if that player's own utility **strictly increases**, without requiring the destination coalition's consent. Social welfare is the sum of all agents' utilities. The price of anarchy is optimal welfare divided by worst Nash-stable welfare, and price of stability uses best Nash-stable welfare. Both ratios are well-defined here because the worst stable welfare equals four.

## Proof

**1. Reduce the candidate partitions to connected coalitions.** A partition with a disconnected coalition gives each member of that coalition utility \(-\infty\); such a player can strictly improve by becoming a singleton. Therefore all Nash-stable coalitions are connected, and all globally optimal partitions can be chosen connected because the partition into all singletons already has finite welfare zero. In a double star every nonsingleton connected coalition contains at least one hub.

**2. Separate hubs.** Suppose \(u,v\) are in different coalitions. If any leaf is not in its adjacent hub's coalition, it is singleton and can strictly improve from zero to one by joining that hub's coalition. Hence every leaf must join its own hub. This gives exactly one partition, with welfare \(2(a+b)\). Its leaves have utility one. Its hubs have utilities \(a,b\ge1\). A hub moving into the other star would receive utility one, since the other hub is at distance one and its leaves at distance two; joining a singleton would give zero. Thus no such move strictly improves utility, and the partition is Nash stable.

**3. Join hubs.** If \(u,v\) are together, the sole nonsingleton coalition contains \(p\) left leaves and \(q\) right leaves for unique integers \(0\le p\le a\), \(0\le q\le b\); all other leaves are singleton. A participating left leaf earns \(1-q\), a participating right leaf earns \(1-p\), the left hub earns \(1+p\), and the right hub earns \(1+q\). A participating leaf can leave to a singleton (utility zero), whereas an excluded left or right leaf can join the hub coalition and earn \(1-q\) or \(1-p\), respectively. Every hub already earns at least one, and its most profitable possible move to another coalition yields at most one, since all outsider coalitions are singletons. All other leaf moves are to nonadjacent isolated leaves and are never profitable.

Therefore the necessary-and-sufficient Nash conditions are

\[
\begin{aligned}
p>0&\Longrightarrow q\le1,&p<a&\Longrightarrow q\ge1,\\
q>0&\Longrightarrow p\le1,&q<b&\Longrightarrow p\ge1.
\end{aligned}
\]

Because \(a,b\ge1\), their **only** integer solutions are \((p,q)=(a,0),(0,b),(1,1)\). The first two use a uniquely determined coalition; the third uses an arbitrary choice of one of the \(a\) left leaves and one of the \(b\) right leaves. The equilibrium count follows as \(1+1+1+ab\).

**4. Derive welfare.** When hubs share a coalition containing \(p,q\) leaves, the induced tree has \(1+p+q\) distance-one pairs and \(pq\) distance-three pairs; the distance-two pairs contribute zero. Its total welfare is therefore

\[
W(p,q)=2(1+p+q-pq).
\]

At the three Nash solutions this gives \(2(a+1),2(b+1),4\), respectively. Combined with the separated-hub welfare in step 2, this proves the multiset claim.

**5. Bound global welfare.** For separated hubs, a partition can earn at most \(2(a+b)\), because only edges can contribute positively, and the tree has \(a+b+1\) edges but the hub-to-hub edge is cut, leaving at most \(a+b\) positive pairs. For joined hubs the coalition has parameters \(p,q\) as above, and

\[
1+p+q-pq\le1+\max\{a,b\}\le a+b.
\]

The first inequality follows from \(q=0\) maximizing at any fixed \(p\ge1\) (where \(1+p+q-pq\le1+p\le1+a\)), whereas for \(p=0\) the expression is \(1+q\le1+b\). The second inequality uses \(\min(a,b)\ge1\). Every feasible connected partition is either separated-hub or joined-hub, so this is a global upper bound. The separated full stars attain it and are Nash stable. The minimum Nash welfare is four, from every \((1,1)\) equilibrium; all other stable welfares are at least four. Hence the two price ratios follow.

For completeness, the optimum equality cases are: both hubs separated with all leaves attached; plus \((0,b)\) if \(a=1\); plus \((a,0)\) if \(b=1\); plus \((1,1)\) if \(a=b=1\). No other joined case attains equality, as follows by inspecting the strict inequalities for \(p,q\) outside these possibilities. This proves the optimal-partition multiplicities.

## Verification

The accompanying standalone program `verify_double_star.py` implements direct induced-subgraph distances, enumerates every labeled set partition, checks every possible unilateral Nash deviation independently of the theorem's proposed structure, computes social welfare, and compares the complete Nash welfare multiset and global optimum to the closed forms. It passed 217,219 total partitions across 18 parameter pairs: all \(1\le a,b\le4\) with \(a+b\le7\), as well as \((a,b)=(4,4),(1,6),(2,5)\). Each finite check is independent corroboration and does not replace the infinite-family proof above. Run with `python3 verify_double_star.py` (Python standard library only).

## Relationship to prior work

Ganian, Hamm, Knop, Roy, Schierreich and Suchý [1] define exactly this non-normalized integer score-based social distance game, use \((1,0,-1)\) as an explicit motivating example, and obtain general welfare and stability algorithms on tree-like networks. Their theorems do not provide the all-size double-star Nash partition classification, exact equilibrium count, Nash welfare spectrum, or price-of-anarchy formula stated here. General algorithms for an individual graph are not closed forms for all values of \(a,b\).

Flammini, Kodric, Olsen and Varricchio [2] study Nash stability and price ratios for **normalized** distance-hedonic utilities, dividing scores by the current coalition size and treating disconnected pairs differently. They establish broader inefficiency phenomena with negative scores, which motivates this question, but those results do not entail the present unnormalized, family-exact classification. Earlier inverse-distance social distance games [3,4] also have different preferences and do not directly imply these formulas.

## Limitations

The claims are restricted to labeled double-star networks with two nonempty leaf classes, exact scores \((1,0,-1)\), induced distances, and strictly improving unilateral deviations. They do not assert the same formulas for general trees, normalized utility, larger scoring vectors, group deviations or stronger equilibrium concepts. The originality comparison is based on inspected primary sources, identified closely related models and mathematical-index searches; independent specialist priority verification has not been performed. Finite enumeration is not a proof of the universal statement.

## References

1. R. Ganian, T. Hamm, D. Knop, S. Roy, Š. Schierreich and O. Suchý, *Maximizing Social Welfare in Score-Based Social Distance Games*, EPTCS 379 (2023), 272–286, https://arxiv.org/abs/2307.05061, DOI:10.4204/EPTCS.379.22; expanded preprint https://arxiv.org/abs/2312.07632.
2. M. Flammini, B. Kodric, M. Olsen and G. Varricchio, *Distance Hedonic Games*, AAMAS 2020, pp. 1846–1848, https://aamas.csc.liv.ac.uk/Proceedings/aamas2020/pdfs/p1846.pdf.
3. A. Balliu, M. Flammini, G. Melideo and D. Olivetti, *Nash Stability in Social Distance Games*, AAAI 2017, DOI:10.1609/aaai.v31i1.10608.
4. A. Balliu, M. Flammini, G. Melideo and D. Olivetti, *On Non-Cooperativeness in Social Distance Games*, JAIR 66 (2019), 625–653, DOI:10.1613/jair.1.11808.
