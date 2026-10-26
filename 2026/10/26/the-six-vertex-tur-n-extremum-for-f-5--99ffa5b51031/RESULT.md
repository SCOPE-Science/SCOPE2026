# The six-vertex Turán extremum for \(F_5\)

## Finding

For the 3-uniform hypergraph \(F_5\) with edges \(\{a,b,c\},\{a,b,d\},\{c,d,e\}\) on five distinct vertices, every \(F_5\)-free 3-uniform hypergraph on six vertices has at most \(10\) edges, with equality if and only if it consists of all triples containing one fixed vertex; hence \(\operatorname{ex}_3(6,F_5)=10\) and the six labeled extremizers form one isomorphism class.

## Assumptions and scope

A 3-uniform hypergraph is a set of distinct 3-element subsets of its vertex set. A copy of \(F_5\) is not required to be induced: it is an injective image of the five vertices and the three specified edges. The statement concerns exactly six vertices and makes no claim for other orders.

## Proof

For the lower bound, fix a vertex \(v\) and take every triple containing \(v\). This star has \(\binom{5}{2}=10\) edges. It is \(F_5\)-free: the first two edges of \(F_5\) share the pair \(\{a,b}\), whereas its third edge \(\{c,d,e}\) is disjoint from that pair. In a star, the common center of the first two edges must be one of \(a,b\), so it cannot lie in the third edge.

For the upper bound and uniqueness, the included verifier enumerates all \(\binom{6}{3}=20\) possible triples and all \(2^{20}=1,048,576\) labeled 3-graphs on \([6]\). For every injection of the five vertices of \(F_5\) into \([6]\), it builds the 3-edge mask of the resulting copy and deduplicates these masks; exactly 180 distinct forbidden masks remain. A graph mask \(h\) is \(F_5\)-free exactly when no forbidden mask \(p\) satisfies \((h\mathbin{\&}p)=p\). The program checks this condition for every mask, records the edge maximum, and canonicalizes each extremizer under all \(6!=720\) vertex permutations. It returns maximum 10, exactly six labeled extremizers, and one isomorphism class. It also verifies that all six stars occur among those extremizers; because there are exactly six in total, these are all the extremizers.

## Verification

Reproduce with a C++17 compiler:

```sh
g++ -std=c++17 -O3 verify_f5_n6.cpp -o verify_f5_n6
./verify_f5_n6
```

Exact output:

```text
checked_hypergraphs=1048576
distinct_forbidden_patterns=180
max_edges=10
labeled_extremizers=6
isomorphism_classes=1
all_extremizers_are_stars=true
edge_count_10_extremizers=6
```

The search is exhaustive over the finite domain. The result is not inferred from a partial search, timeout, or asymptotic theorem.

## Relationship to prior work

The recent literature on the generalized triangle \(F_5\) establishes the eventual balanced complete tripartite extremum. The 2025 preprint *On a hypergraph Mantel theorem* treats the large-order extremal problem, and a 2026 preprint on blow-ups of \(F_5\) records the known threshold \(n\ge 33\) for the unblown-up problem. A 2024 Andrásfai–Erdős–Sós-type result studies a minimum-degree threshold and a cancellative subfamily. None of these inspected statements gives the six-vertex edge maximum or its extremal classification. In particular, the balanced complete tripartite 3-graph on six vertices has 8 edges, whereas the six-vertex extremizer here has 10.

## Limitations

This is an exact finite result only for six vertices; it yields no formula for \(\operatorname{ex}_3(n,F_5)\) at other orders. The exhaustive certificate is reproducible code rather than a short general inequality. The original 1983 article cited for the eventual \(F_5\) result was not available in full text during this check, so an unlocated historical small-order statement cannot be ruled out; the finding makes no absolute priority claim.

## References

1. Xizhi Liu, *On a hypergraph Mantel theorem*, arXiv:2501.19229 (first public version 2025-01-31). The paper states the large-order unique extremal result and discusses the open minimal-forbidden-family question.
2. Xiamiao Zhao, Xin Cheng, Dániel Gerbner, Hilal Hama Karim, Shujing Miao, Yichen Wang, and Junpeng Zhou, *On the Turán number of blow-ups of* \(\mathcal{F}_5\), arXiv:2605.22397 (first public version 2026-05-21). Its introduction records the previously known threshold \(n\ge 33\) for \(F_5\).
3. Xizhi Liu, Sijie Ren, and Jian Wang, *Andrásfai–Erdős–Sós theorem for the generalized triangle*, arXiv:2410.20832 (first public version 2024-10-28). It treats the \(F_5\) minimum-degree threshold and cancellative 3-graphs.
4. P. Frankl and Z. Füredi, *A new generalization of the Erdős–Ko–Rado theorem*, Combinatorica 3 (1983), 341–349, DOI: 10.1007/BF02579190. Later sources cite it for the eventual \(F_5\) Turán result; its full text was not inspected here.
