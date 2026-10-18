# Seven strong edge colors and ten extremal induced matchings of the Tutte–Coxeter graph

## Finding

Let \(T\) be the thirty-vertex Tutte–Coxeter graph, equivalently the Levi graph of the duads and synthemes of a six-element set. Its strong chromatic index is exactly
\[
\chi'_s(T)=7.
\]
Its maximum induced matching has nine edges, and there are exactly ten maximum induced matchings. Every edge of \(T\) lies in exactly two of these ten matchings; every two distinct maximum induced matchings share exactly one edge. Consequently, their ten-by-forty-five edge-incidence structure is the vertex–edge incidence structure of \(K_{10}\): the forty-five graph edges correspond bijectively to unordered pairs of maximum induced matchings.

The previously published failure of strong six-edge coloring is acknowledged. The retained exactness contribution is a checkable strong seven-coloring, independently accompanied by a complete finite six-color exclusion and the structural induced-matching census.

## Assumptions and scope

An induced matching of a simple graph is an edge set whose endpoints induce a disjoint union of single edges. A strong \(k\)-edge coloring partitions all edges into \(k\) induced matchings; \(\chi'_s\) is the smallest such \(k\).

Use the following canonical model. Let \(U\) be the fifteen unordered pairs of \(\{0,1,2,3,4,5\}\) in lexicographic order. Let \(V\) be the fifteen partitions of this six-set into three unordered pairs, ordered lexicographically by their sorted constituent pairs. The vertices of \(T\) are the fifteen elements of \(U\) followed by the fifteen elements of \(V\); a pair vertex is joined to a partition vertex precisely when the pair belongs to that partition. The forty-five graph edges are indexed \(0,\ldots,44\) by iterating over \(U\) and then over \(V\) in the stated orders and retaining incidences. This fully specifies the graph and the index order used in the certificate.

## Proof

For two distinct graph edges, call them *compatible* if they have disjoint endpoints and no graph edge connects an endpoint of the first to an endpoint of the second. Form the forty-five-vertex compatibility graph \(H\). Induced matchings of \(T\) are precisely cliques of \(H\), and a strong edge coloring is precisely a partition of \(V(H)\) into cliques.

**Complete clique census.** The explicitly included `verify_exact.py` visits every clique exactly once by maintaining a strictly increasing available-index set. Its checked clique counts, for clique sizes \(1,\ldots,9\), are
\[
(45,720,5160,16920,22680,8520,720,90,10),
\]
with no cliques of size at least ten. Its enumeration establishes ten maximum nine-cliques, pairwise sharing one vertex, and that every vertex of \(H\) belongs to exactly two maximum nine-cliques. Independently, `verify_independent.py` uses a Bron–Kerbosch maximal-clique search followed by subset enumeration; it obtains the same full census. The maximal-clique size distribution is \(3060\) of size five, \(5520\) of size six, \(360\) of size seven and \(10\) of size nine.

**Six colors are impossible.** Every eight-clique lies in a unique nine-clique because the ten nine-cliques pairwise meet in just one vertex. Three eight-cliques cannot be pairwise disjoint: for their distinct parent nine-cliques, the intersections of one parent with the other two are two different vertices, whereas its eight-clique omits only one vertex. Nor can two nine-cliques be disjoint. If a partition of forty-five vertices into six cliques used no nine-clique, it could contain at most two eight-cliques and therefore cover at most \(2\cdot8+4\cdot7=44\) vertices. If it used a nine-clique, it could contain at most one disjoint eight-clique and would have to consist of class sizes \(9,8,7,7,7,7\). For each of the \(10\cdot9=90\) ordered choices of a nine-clique and a distinct parent nine-clique for the eight-clique, the latter must omit the single vertex shared with the former. The remaining twenty-eight vertices admit exactly thirty-two candidate seven-cliques, and in every one of the ninety cases **no four of these seven-cliques cover all twenty-eight vertices**. This last finite assertion is verified exhaustively by two separate algorithms in the included standalone programs, the first a constrained exact-cover recursion and the second a direct four-subset census. Both programs construct the graph and compatible edge pairs independently. Hence a six-coloring is impossible; fewer colors would also give a six-coloring by leaving some colors unused.

**Seven colors suffice.** The following explicit assignment gives the color, from zero through six, of graph edges \(0,\ldots,44\) in the canonical order:

```text
0,6,1,3,6,4,0,1,4,6,2,0,5,2,0,
2,3,4,0,5,4,2,5,3,1,6,5,2,4,6,
5,3,1,4,6,3,2,0,6,4,0,1,5,1,6
```

The `verify_exact.py` checker tests every pair of incompatible edges and verifies their colors differ; all seven colors occur. Therefore \(\chi'_s(T)\le7\), which combines with the lower bound to prove equality.

The incidence conclusion follows from the ten-by-forty-five census: each graph edge corresponds to the two maxima containing it, and different graph edges yield distinct pairs because two maxima share exactly one edge. There are \(\binom{10}{2}=45\) pairs, so this is a bijection.

## Verification

Run `python3 verify_exact.py` and `python3 verify_independent.py` in any Python 3.10 or later. Both use only the Python standard library. Each rebuilds the thirty-vertex incidence graph from its duad–syntheme definition and independently enumerates its induced matchings and the ninety residual four-class cases. The first also checks the displayed coloring. The local `CERTIFICATE.json` gives the ordered incidence edges, the seven colors and the ten maximum-matchings in machine-readable form; both verification programs check it against independently generated data. See `VERIFICATION.md` and their recorded outputs for the complete exact checks. A finite search here is a complete proof because its recursion covers every clique of the explicitly finite graph, not an extrapolation to larger graphs.

## Relationship to prior work

Hudák, Lužar, Soták and Škrekovski (arXiv:1303.4580, first posted March 19, 2013) study strong edge coloring for *planar* graphs. Their theorems do not apply as strong seven-color upper bounds to this nonplanar cage. Lužar, Máčajová, Škoviera and Soták (arXiv:2101.04768, Section 5) specifically report that the Tutte eight-cage is not strongly six-edge-colorable. They state a broader seven-color conjecture and give numerical evidence for other bounded graph orders, but do not give a seven-color certificate for this thirty-vertex cage or the ten-matching intersection design. The known six-color obstruction is not claimed as new. General bounds on induced matchings of cubic graphs and on numbers of maximal induced matchings do not imply this exact census.

## Limitations

The result concerns only the stated finite graph and the ordinary, not list, strong chromatic index. The lower-bound certificate is computational but complete and executable; no theorem for all cubic graphs of given girth is asserted. Searches cannot exclude unindexed calculations, unpublished programs or supplements. Independent external audit has not been performed. The computationally asserted census is checked by two distinct finite algorithms, not by a short structural classification of the ten matchings.

## References

1. D. Hudák, B. Lužar, R. Soták, R. Škrekovski, *Strong edge coloring of planar graphs*, arXiv:1303.4580 (initial public version 2013-03-19), doi:10.1016/j.disc.2014.02.002.
2. B. Lužar, E. Máčajová, M. Škoviera, R. Soták, *Strong edge colorings of graphs and the covers of Kneser graphs*, arXiv:2101.04768 (2021), doi:10.1002/jgt.22802, especially Section 5.
3. P. Horák, H. Qing, W. T. Trotter, *Induced matchings in cubic graphs*, Journal of Graph Theory 17 (1993), 151–160, doi:10.1002/jgt.3190170204.
4. B.-J. Yuan, Z.-Y. Yang, L. Zheng, S.-C. Gong, *Maximal and maximum induced matchings in connected graphs*, arXiv:2410.11288 (2024).
