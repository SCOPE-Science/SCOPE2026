# Integral second off-diagonal magnitude homology of the Tutte–Coxeter graph
## Finding
Let \(T\) be the Tutte–Coxeter graph with shortest-path metric. Its integral magnitude homology in bidegree \((3,5)\) is
\[
\boxed{\operatorname{MH}_{3,5}(T;\mathbb Z)\cong\mathbb Z^{1440}.}
\]
For ordered endpoints \((x,y)\) in opposite bipartition classes, the endpoint-localized group is
\[
\operatorname{MH}^{x,y}_{3,5}(T;\mathbb Z)\cong
\begin{cases}
0,&d(x,y)=1,\\
\mathbb Z^4,&d(x,y)=3.
\end{cases}
\]
Every same-side summand is zero. In particular no primary torsion survives; this strengthens the previously published dimension \(1440\) over \(\mathbb F_2\).

## Assumptions and scope
The graph \(T\) is the bipartite incidence graph with one class the \(15\) two-element subsets of \(\{0,1,2,3,4,5\}\), and the other class the \(15\) partitions of these six symbols into three unordered pairs (perfect matchings). Incidence means that an edge belongs to a matching. There are \(30\) vertices and \(45\) graph edges; the graph is connected, cubic, has girth \(8\) and diameter \(4\).

For a finite metric graph \(G\), the magnitude chain group \(\operatorname{MC}_{k,l}(G)\) is the free abelian group on tuples \((v_0,\ldots,v_k)\) of vertices with consecutive entries unequal and \(\sum_i d(v_{i-1},v_i)=l\). The differential in degree \(k\) deletes an interior vertex \(v_i\) with coefficient \((-1)^i\) if \(d(v_{i-1},v_i)+d(v_i,v_{i+1})=d(v_{i-1},v_{i+1})\); other deletions contribute zero. All calculations use these integral, signed boundaries. The differential preserves initial and final endpoints, giving a direct sum of endpoint-localized chain complexes. This result concerns only \(k=3\) and \(l=5\).

## Proof
**Endpoint types and reduction.** Bipartiteness implies \(d(a,b)\) has the parity of the change in part. Consequently any chain of odd total metric length, including length \(5\), has endpoints in opposite parts. An \(S_6\) permutation of the underlying six symbols acts by incidence-graph automorphisms. It is transitive on ordered point-to-matching incident pairs and on nonincident pairs separately: fixing a chosen two-element subset, it acts transitively on matchings containing it and on matchings avoiding it. These have \(45\) and \(180\) ordered point-to-matching pairs, respectively, and graph distances \(1\) and \(3\). Reversing tuples identifies the two opposite endpoint orders, with the degree-\(k\) differential changed only by an overall sign \((-1)^k\). Thus there are exactly two integral chain types to compute.

**Exact localized chain reductions.** For one representative of each type, enumerate every tuple in \(\operatorname{MC}_{k,5}^{x,y}\) for \(k=2,3,4\) by all possible positive step lengths summing to \(5\). Construct the signed integer matrices \(B_3=\partial_3\) and \(B_4=\partial_4\) using the displayed metric-deletion rule. Direct integer Smith reduction gives:

| Endpoint distance | \(\dim C_2\) | \(\dim C_3\) | \(\dim C_4\) | \(\operatorname{rank}B_3\) | Nonzero Smith factors of \(B_4\) |
|---:|---:|---:|---:|---:|---|
| \(1\) | \(8\) | \(36\) | \(56\) | \(8\) | \(1\) repeated \(28\) times |
| \(3\) | \(14\) | \(45\) | \(40\) | \(14\) | \(1\) repeated \(27\) times |

The same enumeration verifies \(B_3B_4=0\). All the nonzero Smith factors of \(B_4\) are units, hence \(\operatorname{im}B_4\) is a primitive subgroup of the free group \(C_3\). Therefore \(C_3/\operatorname{im}B_4\) is free abelian, and its subgroup \(\ker B_3/\operatorname{im}B_4\) is also free abelian. The localized homology ranks are exactly \(36-8-28=0\) for incident endpoints and \(45-14-27=4\) for nonincident endpoints. This proves the asserted integral groups, rather than only dimensions in characteristic two.

**Global sum.** There are \(180\) ordered nonincident point-to-matching pairs and \(180\) reversed pairs. Each contributes a free rank-four group, giving \(360\cdot4=1440\). All remaining endpoint summands vanish.

## Verification
The accompanying `check_tutte_integral.py` is a standalone reproducible exact-integer checker (Python 3 and SymPy). It reconstructs the incidence graph from the \(15\) edges and \(15\) perfect matchings of a six-element set, verifies the graph invariants and both \(S_6\) orbit sizes, generates the two complete endpoint-localized magnitude chain complexes, checks \(B_3B_4=0\), obtains exact integer Smith forms of both boundaries and verifies all displayed counts. Its checks make no assumption that a finite-field rank determines integral torsion. The checker completes with the statement `PASS: integral MH_(3,5) = Z^1440; all relevant Smith factors are units`.

## Relationship to prior work
Asao, Hiraoka and Kanazawa established girth-dependent vanishing of magnitude homology near the diagonal (arXiv:2101.09044, first available January 2021). For a girth-eight graph, their second-off-diagonal vanishing criterion does not cover bidegree \((3,5)\). A previously published computation entitled *Second off-diagonal magnitude homology of the Tutte–Coxeter graph* determined the dimension in this same bidegree over \(\mathbb F_2\), together with endpoint counts and ranks, but explicitly made no integral assertion. The present result is the stronger integral assertion, including exclusion of every prime torsion subgroup: neither a characteristic-two rank nor the girth theorem implies it. General graph magnitude-homology definitions trace to Hepworth and Willerton.

## Limitations
This is an exact finite-graph, one-bidegree computation. It does not classify higher magnitude homology, symmetry modules or all generalized quadrangles. Its computer-assisted integral certificates rely on exact Smith reductions from fully enumerated signed boundary matrices, supplied as executable code, not on sampled graphs or probabilistic rank checks. The original modular result already fixes the characteristic-two dimension; the independent mathematical information here is the integral freeness and consequent rational and all-characteristic dimensions.

## References
1. Y. Asao, Y. Hiraoka, S. Kanazawa, *Girth, magnitude homology, and phase transition of diagonality*, arXiv:2101.09044, initially submitted 2021-01-22. https://arxiv.org/abs/2101.09044
2. R. Hepworth, S. Willerton, *Categorifying the magnitude of a graph*, arXiv:1505.04125. https://arxiv.org/abs/1505.04125
3. *Second off-diagonal magnitude homology of the Tutte–Coxeter graph*, published published-finding corpus research record, 2026-10-11. https://github.com/published-finding corpus/2026
