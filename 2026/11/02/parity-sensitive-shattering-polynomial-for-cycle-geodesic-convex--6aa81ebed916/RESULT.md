# Parity-sensitive shattering polynomial for cycle geodesic convexity

## Finding

For the simple unweighted cycle \(C_n\), \(n\ge3\), let \(\mathcal C_n\) be all geodesically convex vertex subsets, including the empty set and the whole vertex set. A concept labels a queried vertex by membership. Put \(L=\lfloor(n-1)/2\rfloor\).

**Theorem.** Every nonempty proper member of \(\mathcal C_n\) is a cyclic interval of length at most \(L\) edges, and every such interval is a member. Consequently
\[
|\mathcal C_n|=n(L+1)+2.
\]
Every one- or two-point vertex support is VC-shattered. A three-point support, whose successive positive cyclic gaps are \(a,b,c\) with \(a+b+c=n\), is VC-shattered if and only if
\[
\max\{a,b,c\}\le L.
\]
No four-point support is shattered. In particular, the **complete shattered-support polynomial** is
\[
\Phi_n(z)=1+nz+\binom n2z^2+T_nz^3,
\qquad
T_n=\begin{cases}
\frac{n(n^2-1)}{24},&n\text{ odd},\\
\frac{n(n-2)(n-4)}{24},&n\text{ even}.
\end{cases}
\]
Here \(\Phi_n\) counts shattered supports by cardinality. Thus \(\operatorname{VCdim}(\mathcal C_4)=2\), while the dimension equals three for \(n=3\) or \(n\ge5\).

The proper convex sets alone have VC dimension two for every \(n\ge3\); adjoining the whole-cycle concept is exactly what permits the shattered triples. The Littlestone dimension satisfies, for \(p=\lfloor L/2\rfloor\), \(q=L-p\),
\[
\lfloor\log_2(p+1)\rfloor+\lfloor\log_2(q+1)\rfloor
\ \le\ \operatorname{Ldim}(\mathcal C_n)\ \le\
\lfloor\log_2(n(L+1)+2)\rfloor.
\]
Consequently \(\operatorname{Ldim}(\mathcal C_n)=2\log_2n+O(1)\) for increasing cycle order, whereas its VC dimension stays at most three. The adaptive-minus-static gap is unbounded. No exact finite-order formula for Littlestone dimension is asserted.

## Assumptions and scope

The cycle has distinct vertices \(0,1,\ldots,n-1\) in cyclic order and unit edges. A vertex set is **geodesically convex** when, for every pair of its vertices, it contains **all** vertices on **every** shortest path between the pair. This convention matters for antipodal pairs in even cycles. Cyclic-interval length is the number of edges, so a length-zero interval is a singleton. Shattering means that for each label pattern on a finite support some member of the concept family induces exactly that pattern; a complete online binary query tree defines Littlestone dimension.

## Proof

**Convex sets.** Any nonempty convex set induces a connected subgraph: all shortest paths between two of its vertices lie in the set. A connected proper induced subgraph of a cycle is a cyclic interval. If its edge length \(t\) is at least \(n/2\), its endpoints have an outside shortest path (when \(t=n/2\)) or a strictly shorter outside path (when \(t>n/2\)); either contradicts geodesic convexity. Thus \(t<n/2\), equivalently \(t\le L\). Conversely, every subinterval of a cyclic interval of length below \(n/2\) is the unique shortest path between its endpoints, so every interval of length at most \(L\) is convex. The empty and full sets are convex. There are exactly \(n\) distinct intervals of each length \(0,1,\ldots,L\), proving the cardinality formula.

**Supports of sizes at most three.** Empty, singleton and full concepts realize all four label patterns on any two distinct vertices. For a three-point support \(\{u,v,w\}\) in cyclic order, the trace containing exactly \(u,v\) must come from a proper interval avoiding \(w\); the sole contiguous route from \(u\) to \(v\) that avoids \(w\) spans their successive gap \(a\). Such a trace therefore exists exactly when \(a\le L\). Cycling the roles gives the conditions \(b,c\le L\). These conditions suffice: use those three corresponding gap intervals for the pair traces, singleton intervals for singleton traces, the empty concept for the all-negative trace and the full-cycle concept for the all-positive trace. Hence the triple criterion is necessary and sufficient.

**No four-point support.** Suppose four vertices occur in cyclic order with positive gaps \(g_1,g_2,g_3,g_4\), whose sum is \(n\). Shattering would realize each trace containing three vertices and excluding the fourth. Since the full-cycle concept cannot realize such a trace, a proper interval must include the three selected consecutive vertices, implying \(g_i+g_{i+1}\le L\) for each of the four cyclic values of \(i\). Summation gives \(2n\le4L\), but \(4L<2n\), contradiction. Shattering is hereditary, so no larger support is shattered either.

**Counting triples.** The number of ordered positive compositions \(a+b+c=n\) is \(\binom{n-1}{2}\). If \(a>L\), the number is \(\binom{n-L-1}{2}\); likewise for the other two gaps. Two gaps cannot simultaneously exceed \(L\) because their sum and the third positive gap would exceed \(n\). Thus
\[
Q_n=\binom{n-1}{2}-3\binom{n-L-1}{2}
\]
is the number of ordered cyclic gap triples with all gaps at most \(L\). Each unordered shattered support is represented by three choices of its initial vertex among \(n\) choices, so \(T_n=nQ_n/3\). Substituting \(L=(n-1)/2\) for odd \(n\) and \(L=(n-2)/2\) for even \(n\) yields the parity formulas. For \(n=3\), the unique triple is shattered; \(n=4\) has none; for odd \(n\ge5\) the gaps \((1,L,L)\) work, and for even \(n\ge6\) the gaps \((2,L,L)\) work. The VC-dimension classification follows. Without the full concept, no triple has its all-positive trace together with all pair traces: any proper interval containing all three cannot use any of the three gaps to pass from one selected vertex to another while avoiding the third, and its length would exceed \(L\) if all gap inequalities held. All adjacent pairs are shattered by proper concepts, proving the proper-family VC dimension two.

**Online upper and lower bounds.** The distinct-concept count gives the upper bound, since a complete depth-\(d\) binary query tree requires at least \(2^d\) distinct terminal hypotheses. For the lower bound, fix vertex \(0\) and restrict to intervals consisting of \(\ell\) consecutive steps counterclockwise and \(r\) clockwise from \(0\), where \(0\le\ell\le p\) and \(0\le r\le q\). Because \(\ell+r\le p+q=L\), all such intervals are convex. Querying the vertex at counterclockwise distance \(s\) from zero reports whether \(\ell\ge s\), and clockwise queries similarly report whether \(r\ge s\). Each coordinate is an ordered threshold class on \(p+1\) or \(q+1\) parameter values. Repeated balanced threshold queries on the first coordinate yield a complete binary tree of depth \(\lfloor\log_2(p+1)\rfloor\); repeating them on the second coordinate at each leaf gives an additional \(\lfloor\log_2(q+1)\rfloor\) levels. Every leaf retains a distinct interval witness, proving the lower bound. Since \(p,q=\Theta(n)\), both bounds are \(2\log_2n+O(1)\).

## Verification

The accompanying standalone program `check_cycle_convexity.py` can be executed with Python 3 and its standard library. It independently determines convex subsets by all-pairs geodesic intervals for cycle orders three through thirteen and compares them to the claimed arc classification; exhaustively enumerates all supports of sizes one through four for orders three through seventeen; verifies each triple's gap condition; computes exact online ranks through order fifteen via the complete version-space recurrence; and replays the constructive threshold-splitting lower-bound trees through order one hundred. These finite checks corroborate the formulas; the universal conclusions rest on the mathematical arguments above. The executable output terminates in `ALL_CYCLE_CONVEXITY_CHECKS_PASS`.

## Relationship to prior work

Thiessen and Gärtner's 2020 study initiated an active-learning treatment of geodesically convex graph classes, using a different querying protocol and broad structural bounds. The complete proof of that paper was inspected; its statements do not give this cycle-specific parity-sensitive shattering polynomial or the present online threshold construction. Their 2022 study considers online learning of convex sets on graphs and is the most relevant potential comparison, but the complete article was not accessible for inspection; priority against its detailed special cases has not been established. Chepoi's 2024 paper studies separation properties of geodesic **halfspaces**, a restricted concept family; its results do not imply the shattered-support counts for the family of **all convex subsets** here. The unrestricted circular-interval family is also a larger concept class than geodesically convex cycle intervals, which must be shorter than half a circumference; its usual capacity bounds alone do not determine the present parity-dependent support counts.

## Limitations

This result is restricted to unweighted simple cycles and **all-shortest-path** convexity. It does not establish exact finite-order Littlestone dimensions beyond the stated bounds or characterize other graph classes. The 2022 article identified above was accessible only through bibliographic information and abstract, not through its full proof; this is a material remaining historical-priority risk. No claim of independent validation or exhaustive literature coverage is made.

## References

1. M. Thiessen and T. Gärtner, *Active Learning on Graphs with Geodesically Convex Classes*, Workshop on Mining and Learning with Graphs (2020), DOI `10.34726/3467`, publicly released August 24, 2020. Full text: https://www.mlgworkshop.org/2020/papers/MLG2020_paper_40.pdf.
2. M. Thiessen and T. Gärtner, *Online Learning of Convex Sets on Graphs*, ECML PKDD 2022, DOI `10.1007/978-3-031-26412-2_22` (abstract/bibliographic record consulted; full article not inspected).
3. V. Chepoi, *Separation axiom S3 for geodesic convexity in graphs*, arXiv:2405.07512, first posted May 13, 2024 (full text consulted; addresses geodesic halfspaces).
