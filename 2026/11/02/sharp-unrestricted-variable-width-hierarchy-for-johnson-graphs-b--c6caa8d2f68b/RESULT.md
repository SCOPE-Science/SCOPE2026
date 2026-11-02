# Sharp unrestricted variable-width hierarchy for Johnson graphs beyond three variables

## Finding

For integers \(p\ge4\), \(r,s\ge3\), \(n\ge2r\), and \(m\ge2s\), let \(J(n,r)\) be the simple graph on the \(r\)-element subsets of an \(n\)-element set, with two distinct vertices adjacent exactly when their intersection has size \(r-1\). In the pure language of equality and adjacency, with no counting quantifiers and no restriction on quantifier depth,

\[
J(n,r)\equiv_{\mathrm{FO}^{p}}J(m,s)
\quad\Longleftrightarrow\quad
r=s\ \text{ and }\ \min\{n,pr\}=\min\{m,pr\}.
\]

In particular, for every fixed \(r\ge3\), the family \(\{J(n,r):n\ge2r\}\) has precisely \((p-2)r+1\) different unrestricted \(p\)-variable theories: singleton classes for each \(2r\le n<pr\), followed by one stable class of all \(n\ge pr\). Its smallest stable representative has \(\binom{pr}{r}\) vertices. If \(3r\le n<m\), then the least variable width distinguishing \(J(n,r)\) from \(J(m,r)\) is exactly \(\lfloor n/r\rfloor+1\), giving arbitrarily high genuinely distinct levels of the hierarchy in a fixed-rank uniform-matroid basis-graph family.

The novelty claimed here is the exact higher-width assertion \(p\ge4\), \(r\ge3\), not the previously studied three-variable case or the two-element-subset (triangular-graph) case.

## Assumptions and scope

The Johnson graph \(J(n,r)\) uses the usual replacement adjacency: \(E(A,B)\) holds if \(A\ne B\) and \(|A\setminus B|=1\). Every graph is finite, nonempty, undirected, and loopless. The normalization \(r\le n/2\) loses no isomorphism types since complementation of subsets identifies \(J(n,r)\) with \(J(n,n-r)\). The theorem includes all integer \(p\ge4\) simultaneously, all normalized ranks \(r,s\ge3\), and arbitrarily many nested quantifiers using at most \(p\) variable names.

## Proof

**Metric definability.** In any Johnson graph, the shortest-path distance between vertices \(A,B\) is \(d(A,B)=|A\setminus B|=r-|A\cap B|\). For the upper bound, exchange one element of \(A\setminus B\) for one of \(B\setminus A\) per step; for the lower bound, one edge can increase the intersection with \(B\) by at most one. Since \(n\ge2r\), disjoint \(r\)-sets exist and the diameter is exactly \(r\).

For each fixed integer \(h\ge0\), the condition \(d(x,y)\le h\) is definable using only three variable names. Begin with \(R_0(x,y):=(x=y)\) and recursively set

\[
R_{h+1}(x,y):=R_h(x,y)\lor\exists z\,(E(x,z)\wedge R_h(z,y)),
\]

renaming bound variables cyclically among three names in each expansion. Write \(\Delta_0(x,y):=(x=y)\) and \(\Delta_h(x,y):=R_h(x,y)\wedge\neg R_{h-1}(x,y)\) for \(h\ge1\). Thus \(\Delta_h\) defines exact distance \(h\). Any third helper name can be bound locally inside a two-free-variable subformula, even when a surrounding formula already uses that name elsewhere. As \(\exists x\exists y\,\Delta_h(x,y)\) detects the graph diameter, unequal normalized ranks \(r\ne s\) are distinguishable with three variables.

**Upper bound for equal ranks.** Fix \(r\ge3\), \(p\ge4\) and two orders \(n,m\ge pr\). Duplicator maintains the following stronger invariant in a \(p\)-pebble game: for the currently selected ordered \(r\)-subsets, the cardinality of every **nonempty** Venn cell (a ground-set element's membership pattern in at least one selected subset) is the same on the two sides. A ground element belonging to none of the selected subsets need not be matched. This invariant entails equality and all pairwise intersection sizes, hence preserves adjacency and nonadjacency of pebbled vertices.

On any move, discard the subset formerly carrying the moved pebble, leaving at most \(p-1\) selected subsets. Their union contains at most \((p-1)r\) ground elements. The invariant identifies each nonempty Venn cell bijectively with its counterpart. Given Spoiler's new \(r\)-subset, copy the number of its elements chosen from each existing nonempty cell; all these choices are possible on the other side. If \(a\) elements of the new subset lie in the old union, choose the remaining \(r-a\) elements outside that union on the other side. There are at least \(pr-(p-1)r=r\) unused ground elements on either side. The complete nonempty Venn profile is therefore preserved after the move. This argument is symmetric, works when vertices coincide, and never decreases any auxiliary resource. Duplicator wins for arbitrarily many moves; consequently all \(n,m\ge pr\) are \(\mathrm{FO}^{p}\)-equivalent.

**Every smaller order is separately visible.** Fix an integer threshold \(t\) with \(2r<t\le pr\). Write \(t=jr+i\), uniquely with \(j=\lfloor(t-1)/r\rfloor\) and \(1\le i\le r\); then \(2\le j\le p-1\). Consider the existential sentence asserting the existence of \(j\) mutually distance-\(r\) vertices \(A_1,\ldots,A_j\) and one additional vertex \(C\), subject to

\[
\Delta_i(A_1,C),\qquad \Delta_r(A_h,C)\quad(2\le h\le j).
\]

Every pair of base sets is disjoint because their graph distance is \(r\). The additional set intersects \(A_1\) in exactly \(r-i\) ground elements and is disjoint from each other base set. Hence the union of all selected subsets has exactly \(jr+i=t\) ground elements. Such a configuration exists if and only if the ground order is at least \(t\): for sufficiency choose \(j\) disjoint \(r\)-sets, take \(r-i\) elements from the first, and take \(i\) elements outside their union. The sentence uses only \(j+1\le p\) variable names, since each distance test is a three-variable formula and its helper quantifiers can locally shadow names of other outer witnesses.

If \(2r\le n<m\) and \(n<pr\), the sentence for \(t=n+1\) holds in \(J(m,r)\) but not \(J(n,r)\). This proves the claimed equivalence criterion together with the upper bound.

**Sharp hierarchy and sizes.** At width \(p\), distinct normalized ranks separate by diameter, and for each rank the preceding threshold criterion leaves \((p-2)r\) singleton orders followed by one stable class. For \(3r\le n<m\), all widths \(h\le\lfloor n/r\rfloor\) with \(h\ge3\) fail to distinguish by the same upper-bound strategy with \(hr\le n\), whereas width \(\lfloor n/r\rfloor+1\) does distinguish using the threshold sentence. The least stable ground order is \(pr\), and \(\binom nr\) strictly increases with \(n\), so the smallest representative has \(\binom{pr}{r}\) vertices.

## Verification

The accompanying standalone programs use Python's standard library only. Run `python verify_venn.py` and `python verify_logic.py` in the extracted file directory. `verify_venn.py` enumerates actual distance-extension supports for ranks two and three; it independently enumerates all nonempty ordered Venn-cell profiles and fourth/fifth-set extensions, checking equality at the predicted cutoff and a discrepancy immediately below. It also constructs 60 exact threshold witnesses. `verify_logic.py` independently applies **noncounting** color refinement (sets of extension colors, not multiplicity-weighted multisets) to small Johnson graphs and reproduces the expected three-variable classes for ranks two and three. The exact recorded outputs are stored in `verify_venn.out` and `verify_logic.out`. These finite checks corroborate, but do not replace, the infinite \(p\)-pebble proof.

## Relationship to prior work

Chepoi's 2015 study characterizes distance-preserving embeddings into Johnson graphs and gives the subset metric; it does not classify unrestricted finite-variable theories. The classical Johnson-scheme literature, including work on merged Johnson graphs, describes adjacency orbitals, distances, and automorphism groups rather than exact higher-variable equivalences. Grohe and Otto's 2012 preprint (later revisions) treats general pebble-game and boolean-equation equivalences, not the precise \(pr\) boundary for these graphs. Adler, Benediktsson, and Macpherson study VC-dimension and VC-density of the adjacency relation on Johnson and Hamming graphs, which are different invariants.

Earlier special-case logical results already cover the three-variable support characterization for distance-regular graphs, the rank-three Johnson-graph classification, and the all-width classification of triangular graphs \(J(n,2)\). Earlier counting color-refinement results on individually marked Johnson vertices determine pointwise stabilizer orbit partitions, but do not determine the present plain unrestricted higher-width equivalence classes. The present theorem does **not** claim those cases anew. Neither earlier result alone implies the higher-width, higher-rank classification: three-variable equivalence can collapse orders that four or more variables separate, and the rank-two endpoint argument does not supply the multiway Venn-cell invariant required when \(r\ge3\). Exact logical width is the new object.

## Limitations

The result is relative to the family of ordinary Johnson graphs with normalized ranks at least three. It is not an identification theorem among all finite graphs. It does not cover counting quantifiers, arbitrary merged Johnson graphs, Grassmann graphs, general matroid basis graphs, or a quantifier-rank bound equal to the variable-width bound. The proof uses the ability to vary quantifier depth without limit. Historical priority remains subject to the possibility of an unlocated stronger general theorem on finite set-system interpretations; no independent mathematical audit has been performed.

## References

1. V. Chepoi, *Distance-preserving subgraphs of Johnson graphs*, arXiv:1503.04047, first submitted 2015-03-13, https://arxiv.org/abs/1503.04047.
2. *Automorphisms and regular embeddings of merged Johnson graphs*, *European Journal of Combinatorics* 26 (2005), 417–435, doi:10.1016/j.ejc.2004.01.012.
3. M. Grohe and M. Otto, *Pebble Games and Linear Equations*, arXiv:1204.1990, first submitted 2012-04-09, https://arxiv.org/abs/1204.1990.
4. I. Adler, B. G. Benediktsson and D. Macpherson, *Vapnik–Chervonenkis dimension and density on Johnson and Hamming graphs*, *Discrete Applied Mathematics* 312 (2022), 29–44, doi:10.1016/j.dam.2021.09.017; accepted manuscript https://eprints.whiterose.ac.uk/id/eprint/178584/.
