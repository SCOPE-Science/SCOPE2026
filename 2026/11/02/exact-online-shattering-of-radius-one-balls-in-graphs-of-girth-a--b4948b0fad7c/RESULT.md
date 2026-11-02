# Exact online shattering of radius-one balls in graphs of girth at least five

## Finding

Let \(G=(V,E)\) be any finite connected simple graph on \(n\ge5\) vertices containing neither a triangle nor a four-cycle. Its closed radius-one balls are \(B(v)=\{v\}\cup N_G(v)\), and the associated concept class is \(\mathcal B(G)=\{B(v):v\in V\}\) with binary queries \(q\in V\) answered by \(\mathbf1[q\in B(v)]\). Put
\[
r_x=|V\setminus B(x)|=n-\deg(x)-1,\qquad s_{xy}=|B(y)\setminus B(x)|.
\]
Then the following is an exact all-graph classification:
\[
\operatorname{VCdim}(\mathcal B(G))=2,\qquad
\operatorname{Ldim}(\mathcal B(G))=
\begin{cases}
3,&\exists x,y\in V:\ \deg(x)\ge3\ \text{and}\ 2\le s_{xy}\le r_x-2,\\
2,&\text{otherwise}.
\end{cases}
\]
The criterion involves only vertex degrees and cardinalities of intersections of two closed neighborhoods. It is not a decision-tree recurrence and is directly computable in polynomial time. The upper bound of three is attained by an eight-vertex tree, and no graph on fewer than eight vertices can attain it. The condition also gives a complete test for every finite tree of order at least five.

For completeness, the exceptional connected trees/graphs of smaller order in this girth class have dimension pairs \((\operatorname{VCdim},\operatorname{Ldim})\): the one-vertex graph and single edge \((0,0)\); the three-vertex path \((1,1)\); the four-vertex path \((1,2)\); and the four-vertex claw \((2,2)\).

## Assumptions and scope

Graphs are finite, simple, undirected, and connected. Girth at least five includes acyclic graphs; equivalently triangles and quadrilaterals are forbidden as (not necessarily induced) subgraphs. The concept class consists of **closed** vertex neighborhoods, with a fixed one-step radius. The known open-neighborhood classifications for Johnson and Hamming graphs do not define this class. The Littlestone dimension is the greatest depth of a complete binary decision tree whose every root-to-leaf answer word has a consistent concept. The VC dimension is the greatest cardinality of a set of fixed query vertices whose every zero-one pattern occurs.

## Proof

**Distinct centers.** For a connected graph on at least three vertices with no triangles, \(B(u)=B(v)\) for distinct \(u,v\) is impossible. Equality would force \(u\sim v\); any additional neighbor of either endpoint would create a triangle. Thus the only possible graph component with coincident closed balls is an isolated edge, excluded by connectedness and \(n\ge3\). Consequently every candidate set of at least two vertices is distinguishable by at least one vertex query, and has Littlestone dimension at least one.

**Local two-center intersection.** For distinct \(x,y\), \(|B(x)\cap B(y)|\le2\). If \(x\sim y\), the intersection is exactly \(\{x,y\}\), since a third common point would form a triangle. If \(x\not\sim y\), common points must be common neighbors, at most one because two would form a four-cycle. It follows that, conditional on a positive answer at query \(x\), every subsequent *distinct* query \(y\) has at most two positive candidate centers. The second positive branch therefore cannot have Littlestone depth two. Query \(x\) itself does not split this positive version space. Hence the positive first-answer class has Littlestone dimension at most two, and no complete depth-four decision tree exists. Thus \(\operatorname{Ldim}\le3\).

**Exactly when the first positive branch has depth two.** After positive query \(x\), the possible centers are precisely \(B(x)\), of size \(\deg(x)+1\). If \(\deg(x)\le2\), fewer than four centers remain, excluding depth two. If \(\deg(x)\ge3\), take a neighbor \(y\) of \(x\) as the next query. In this version space the positive side consists of exactly \(\{x,y\}\); the negative side consists of the other \(\deg(x)-1\ge2\) neighbors of \(x\). The distinct-centers lemma makes each side distinguishable by an additional query. The positive first-answer class therefore has dimension exactly two if and only if \(\deg(x)\ge3\).

**Exactly when the first negative branch has depth two.** After negative query \(x\), possible centers form \(C_x=V\setminus B(x)\), of size \(r_x\). A query \(y\) divides this set into \(C_x\cap B(y)=B(y)\setminus B(x)\), of size \(s_{xy}\), and its complement in \(C_x\), of size \(r_x-s_{xy}\). Because distinct centers are distinguishable, each child has depth at least one exactly when it has at least two vertices. Thus the negative branch has depth at least two precisely when some \(y\) satisfies \(2\le s_{xy}\le r_x-2\).

At the root of any depth-three tree, both children must have dimension at least two. The preceding two paragraphs therefore give the claimed necessary and sufficient local condition. If the condition fails, \(\operatorname{Ldim}\le2\).

**VC dimension.** Suppose three distinct query vertices \(a,b,c\) were shattered. The all-positive pattern would be realized by some center \(v\), so all three lie in \(B(v)\). At least two of them, say \(a,b\), are distinct neighbors of \(v\). Their closed neighborhoods have intersection exactly \(\{v\}\) by the no-triangle/no-four-cycle assumptions. Therefore any concept labeling \(a,b\) both positive must be centered at \(v\), which necessarily labels the remaining query \(c\) positive. The pattern with just \(a,b\) positive is impossible. Thus \(\operatorname{VCdim}\le2\).

For the reverse inequality, if \(G\) has a vertex \(v\) of degree at least three, take two neighbors \(a,b\) as queries. The centers \(v,a,b,c\), with \(c\) a third neighbor of \(v\), realize respectively \(11,10,01,00\), since the neighbors of \(v\) are pairwise nonadjacent. If the maximum degree is at most two, the connected graph is a path or cycle. On a path of at least five vertices, take the first and third vertices as queries; the second, first, fourth and fifth vertices realize the four traces. On a cycle of at least five vertices, take two adjacent query vertices; their one-step neighbors on the opposing sides and a vertex outside the union of the two balls provide the four traces. Therefore \(\operatorname{VCdim}=2\), and the general inequality \(\operatorname{Ldim}\ge\operatorname{VCdim}\) completes the non-depth-three case.

**Sharp order.** A depth-three tree has eight leaves requiring eight distinct concepts, so a graph with fewer than eight vertices cannot have Littlestone dimension three. The tree with edge set
```
(1,0), (1,2), (1,3), (1,4), (0,5), (5,6), (5,7)
```
has \(\deg(5)=3\), \(V\setminus B(5)=\{1,2,3,4\}\), and \(B(2)\setminus B(5)=\{1,2\}\). Hence \(r_5=4\) and \(s_{5,2}=2\), satisfying the criterion and realizing Littlestone dimension three at the smallest possible graph order. All assertions follow. \(\square\)

## Verification

Run `python verify_closed_balls.py` with NetworkX installed and `python independent_check.py` with Python's standard library. The first program independently computes VC dimension by all fixed-query traces and Littlestone dimension using memoized recursion on complete version spaces, then compares both with the degree/neighborhood criterion. It checks all 35 connected triangle- and four-cycle-free graphs in the NetworkX graph atlas through seven vertices, all 986 unlabelled trees of orders two through twelve, and the eight-vertex witness. The second program represents candidate centers directly, uses a separate recursion and independently decodes Prüfer codes to check every one of the 1,440 labeled trees of orders three through six, 350 deterministic random trees on 7–16 vertices, and 55 cycles with or without leaves. The checks do not replace the all-size proof.

## Relationship to prior work

Benediktsson, Macpherson and Adler (first public arXiv submission July 31, 2020) compute static VC dimension/density for the *open-neighborhood* relation in Johnson and Hamming graphs, and discuss closed neighborhoods there. Their full arXiv text concerns those symmetric graph families and does not state a Littlestone classification of one-step **closed balls in graphs of girth at least five**. Bousquet and Thomassé (2014/2015) study VC dimensions of graph-ball hypergraphs at arbitrary radii, including a general minor-exclusion bound that already implies a static VC upper bound of two for trees; that earlier implication is not asserted as new. Their result does not determine the online dimension or the present exact local criterion. The novelty asserted here is the all-graph online classification, its sharp three-round witness, and the exact criterion for distinguishing the two possible online depths. No comprehensive historical-priority guarantee is implied by search results.

## Limitations

The local classification requires connectedness, no triangles and no four-cycles, and **closed radius-one** balls. It does not claim the bound for arbitrary radii, for all sparse graphs, or for open neighborhoods. The finite enumeration is corroboration rather than a substitute for the proof. Neither a classification of larger girth-free classes nor independent third-party validation is claimed. Although published comparisons and records searches revealed no covering assertion, unindexed literature or alternative terminology may contain prior equivalents.

## References

1. B. G. Benediktsson, D. Macpherson, and I. Adler, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042, first posted 2020-07-31, https://arxiv.org/abs/2007.16042.
2. N. Bousquet and S. Thomassé, *VC-dimension and Erdős–Pósa property*, arXiv:1412.1793, first posted 2014-12-04; published in Discrete Mathematics (2015), https://arxiv.org/abs/1412.1793.
