# Exact small cover-free-family numbers for paths, cycles, and wheels

## Result

Let \(t(G)\) be the minimum ground-set size of a cover-free family on a graph \(G\) in the sense of Parida and Moura: the blocks assigned to the endpoints of every edge are incomparable, and their union contains no third block. Then

\[
\boxed{t(P_n)=7\quad(11\le n\le 15)},
\]

\[
\boxed{t(C_n)=7\quad(10\le n\le 15)},
\]

and

\[
\boxed{t(W_{11})=t(W_{12})=8}.
\]

Here \(W_n\) is the wheel on \(n\) vertices, i.e. a universal vertex joined to \(C_{n-1}\).

These equalities make exact all path, cycle, and wheel entries through \(n=12\) that were left as upper bounds in Table 4 of Parida--Moura. They also improve the general mixed-radix construction bound from \(8\) to \(7\) for \(P_n\) and \(C_n\) at \(n=13,14,15\).

## Explicit seven-point constructions

Write a block such as `156` for \(\{1,5,6\}\subseteq[7]\), and read each row in graph order. The following are cover-free families:

- \(P_{13}\) and \(C_{13}\):
  `12, 34, 156, 157, 137, 367, 236, 235, 257, 245, 246, 467, 147`.
- \(P_{14}\) and \(C_{14}\):
  `12, 34, 356, 156, 145, 457, 245, 246, 467, 167, 137, 357, 237, 236`.
- \(P_{15}\):
  `12, 34, 356, 156, 145, 157, 357, 237, 367, 167, 467, 247, 245, 256, 567`.
- \(C_{15}\):
  `12, 247, 245, 256, 567, 467, 167, 367, 237, 357, 157, 145, 156, 356, 34`.

The verification artifact checks directly that every listed family is an antichain and that the union attached to each graph edge contains no third block.

## Lower bounds and exactness

The remaining lower bounds are finite and exact.

### No six-point family for \(P_{11}\)

An exhaustive search over all nonempty proper subsets of a six-point ground set finds no \(P_{11}\)-CFF. This proves \(t(P_{11})\ge7\). Parida--Moura give \(t(P_{11})\le7\), hence \(t(P_{11})=7\).

Since \(P_{11}\) is a subgraph of every \(P_n\) for \(n\ge11\), monotonicity gives \(t(P_n)\ge7\). The published upper bounds give the cases \(n=12\), and the explicit families above give \(n=13,14,15\). Thus \(t(P_n)=7\) for \(11\le n\le15\).

### No six-point family for \(C_{10}\)

The same exhaustive method finds no \(C_{10}\)-CFF on six points. Together with the known upper bound \(t(C_{10})\le7\), this gives \(t(C_{10})=7\).

For \(n\ge11\), \(C_n\) contains \(P_{11}\) as a subgraph, so \(t(C_n)\ge7\). The known upper bounds cover \(C_{11},C_{12}\), and the explicit seven-point cyclic families above cover \(C_{13},C_{14},C_{15}\). Hence \(t(C_n)=7\) for \(10\le n\le15\).

### Wheels

An exhaustive search over seven-point ground sets finds no \(W_{11}\)-CFF. The known upper bound is \(8\), so \(t(W_{11})=8\).

For \(W_{12}=C_{11}+\{x\}\), we have \(t(C_{11})=7\) and \(t(1,11)=6\). Corollary 4.16 of Parida--Moura states that when \(t(H)=t(1,|V(H)|)+1\), adjoining a universal vertex raises the parameter by one. Therefore \(t(W_{12})=8\).

## Exhaustive-search certificate

For a graph with no isolated vertices, every graph-CFF is globally an antichain: applying the singleton part of the graph-CFF condition to an edge incident with each vertex prevents either of any two blocks from containing the other. Thus the finite searches may restrict to nonempty proper subsets and pairwise incomparable blocks.

The path and cycle search builds the ordered block family from left to right. For every completed edge \(ij\), all subsets contained in \(B_i\cup B_j\), except its two endpoint blocks, are permanently forbidden. When a new endpoint is appended, the search also checks that its new edge-union contains none of the already chosen third blocks. Consequently every surviving leaf is exactly a graph-CFF, and every graph-CFF has a surviving prefix at every depth.

Ground-set permutations give a complete symmetry reduction: for paths and cycles the first block is fixed to \(\{1,\ldots,s\}\) separately for each possible size \(s\). For wheels the center block is fixed by its size, and under its stabilizer the first rim block is fixed by its size and its intersection size with the center. These actions are transitive on the corresponding choices, so no isomorphism class is omitted.

The standalone artifact `artifacts/verify_small_graph_cff.py` exhausts these reduced spaces for \(P_{11}\) on six points, \(C_{10}\) on six points, and \(W_{11}\) on seven points. As positive controls it also finds families for the previously known boundary cases \(P_{10}\) on six points, \(C_9\) on six points, and \(W_{10}\) on seven points.

## Context and originality boundary

Parida and Moura introduced the graph parameter systematically, proved exact small cases through \(P_{10}\), \(C_9\), and \(W_{10}\), tabulated upper bounds through \(n=12\), and explicitly asked whether their six-point \(P_{10}\) construction method could be generalized to improve the path/cycle bounds. Their Theorem 6.12 gives upper bound \(8\) for \(P_n,C_n\) in the range \(13\le n\le18\).

The contribution claimed here is the exact closure above: the finite impossibility certificates for \(P_{11},C_{10},W_{11}\), the deductions for the remaining \(n\le12\) entries, and the explicit seven-point constructions extending exactness to \(n=15\) for paths and cycles. Standard Sperner bounds, graph-subgraph monotonicity, and the universal-vertex lemma are prior results and are not claimed as new.

Targeted searches for the exact parameter values, the source paper identifier, and equivalent graph-CFF terminology did not locate a later source containing these equalities. Originality is therefore asserted only to the best of our knowledge; differently named structured group-testing or hypergraph-CFF literature remains a residual coverage risk.

## Limitations

The nonexistence statements rely on exhaustive finite computation plus the stated symmetry reductions, not on a human-only classification proof. No claim is made here about \(P_n\) or \(C_n\) for \(n\ge16\), or about wheels beyond \(W_{12}\).

## References

1. P. Parida and L. Moura, *Cover-free families on graphs*, arXiv:2605.12634, 2026. https://arxiv.org/abs/2605.12634
2. T. B. Idalino and L. Moura, *Cover-free families on hypergraphs and combinatorial group testing*, Journal of Combinatorial Optimization 51, 55 (2026). https://doi.org/10.1007/s10878-026-01429-0
