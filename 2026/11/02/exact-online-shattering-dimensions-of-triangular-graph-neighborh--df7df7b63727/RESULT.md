# Exact online shattering dimensions of triangular-graph neighborhoods

## Finding

Let \(T_n=J(n,2)\), \(n\ge2\), be the triangular graph whose vertices are unordered pairs from an \(n\)-element set and whose edges join distinct pairs sharing exactly one element. Let \(\mathcal N_n=\{N(e):e\in V(T_n)\}\) be its open-neighborhood concepts, with queried pairs as instances and unknown center pairs as hypotheses. Then
\[
\operatorname{Ldim}(\mathcal N_n)=\begin{cases}
0,&n=2,\\
1,&n=3,4,\\
3,&n=5,6,\\
4,&n\ge7.
\end{cases}
\]
In particular the online shattering dimension of these graphs, and of all their induced subgraphs, is at most four, independent of the graph order. There is a sharp jump from one to three at five underlying labels.

## Assumptions and scope

Neighborhoods are open; a pair is not adjacent to itself. All graphs are the full Johnson rank-two graphs \(J(n,2)\). Littlestone dimension means the maximum depth of a complete binary adaptive membership-query tree in which every answer path is realized by a center pair. The induced-subgraph statement is only an upper bound, not an exact classification for arbitrary subgraphs.

## Proof

Fix a first queried pair \(e=\{a,b\}\). Its positive hypotheses are \(A=N(e)\), consisting of the two classes \(\{\{a,x\}:x\notin e\}\) and \(\{\{b,x\}:x\notin e\}\).

For a second query \(f\), the positive fiber \(B=A\cap N(f)\) is one of three forms. If \(f=e\), then \(B=A\), giving no split. If \(f=\{a,c\}\) intersects \(e\) in one element, then \(B\) consists of all \(\{a,x\}\) with \(x\notin\{a,b,c\}\), together with the one exceptional pair \(\{b,c\}\). If \(f=\{c,d\}\) is disjoint from \(e\), then \(B=\{\{a,c\},\{a,d\},\{b,c\},\{b,d\}\), containing four centers.

In the adjacent-query case, examine any further query \(g\) on the fiber \(B\). When \(g\) contains \(a\), its negative trace on \(B\) has size at most two: only the exceptional pair and, potentially, the one pair equal to \(g\) can fail adjacency. When \(g\) does not contain \(a\), its positive trace on \(B\) has size at most two: it can meet at most two of the star pairs in \(B\), with the excluded \(\{a,c\}\) ensuring that a possible contribution from \(\{b,c\}\) does not raise the count. Therefore every query on \(B\) has a branch with at most two center hypotheses, and \(\operatorname{Ldim}(\mathcal N|_B)\le2\). For disjoint \(f\), the four-center bound also gives \(\operatorname{Ldim}(\mathcal N|_B)\le2\). Thus \(\operatorname{Ldim}(\mathcal N|_A)\le3\), because a depth-four complete tree on \(A\) would require a depth-three subtree in each branch of its first query. A depth-five tree in the full concept class would require a depth-four subtree after its positive first answer, which is impossible. This proves \(\operatorname{Ldim}(\mathcal N_n)\le4\) for every \(n\).

For \(n=2\) there is one hypothesis, so the dimension is zero. For \(n=3\) the graph is \(K_3\), giving dimension one. For \(n=4\), complementary pairs have identical open neighborhoods and there are just three distinct concepts, giving dimension at most one; two distinct concepts give the matching lower bound. For \(n=5,6\), the concept-class cardinalities \(\binom52=10\) and \(\binom62=15\) exclude depth four.

The file `lower_certificates.json` supplies complete depth-three and depth-four query trees for \(T_5\) and \(T_7\), with a different center pair at each of the eight and sixteen leaves. Every edge label is checked by `verify.py`. Restricting both pairs and queries from \(T_n\) to the pairs on a fixed subset of labels gives an induced copy of every smaller triangular graph, so these witnesses embed for all \(n\ge5\) and \(n\ge7\), respectively. All upper and lower bounds match. Restriction of centers and query instances to an induced subgraph cannot increase Littlestone dimension.

## Verification

Run `python verify.py` alongside `lower_certificates.json` using the Python 3 standard library. This checks every path of both lower certificates against an independently computed pair-intersection predicate and obtains the exact Littlestone dimensions by the full finite recurrence for all \(n=2,\ldots,9\). The output is recorded in `verification_output.txt`. The mathematical proof handles every \(n\); no infinite assertion rests on finite enumeration.

## Relationship to prior work

Adler, Benediktsson and Macpherson [1] study this same open-neighborhood relation in the more general Johnson graphs and determine its VC dimension and VC density, including the sharp static rank-two threshold. Their Section 3 establishes intersecting-pair geometry used as background but does not state the adaptive dimension sequence above. The new claim concerns the Littlestone (online) invariant, not a new VC-dimension bound. The graph is also known as the line graph of the complete graph; searches included that equivalent formulation.

## Limitations

The conclusion does not concern higher-rank Johnson graphs, closed neighborhoods, or distance-radius queries beyond adjacency. No claim is made of exhaustive historical-priority verification or independent scientific certification. The explicit finite witnesses and unrestricted upper-bound argument are independently reproducible but do not establish priority by themselves.

## References

[1] I. Adler, B. G. Benediktsson and D. Macpherson, *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042v1 (31 July 2020), especially Section 3; later *Discrete Applied Mathematics* 312 (2022), 29–44. https://arxiv.org/abs/2007.16042
