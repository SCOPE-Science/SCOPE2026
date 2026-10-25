# Alternating-chain census and a sharp nilpotency-index phase transition for \(\mathrm{DP}(K_{a,b})\)

## Finding

Let \(a,b\geq 2\) be integers. The inverse monoid \(\mathrm{DP}(K_{a,b})\) consists of partial distance-preserving bijections of the complete bipartite graph with labeled part sets \(A,B\), \(|A|=a\) and \(|B|=b\). An element \(f\) is nilpotent if some positive power is the empty partial map; its index \(\nu(f)\) is the least such positive power, and its rank is \(|\operatorname{dom}f|\). In particular, the empty map has index one and rank zero.

For an integer \(L\geq1\), define the following finite polynomials (in the appropriate formal power-series truncations):
\[
P_L(x,u)=\sum_{j=1}^{L}x^ju^{j-1},
\]
\[
Q_L(x,y,u)=
\sum_{\substack{r\geq0\\2r+1\leq L}}
\bigl(x^{r+1}y^r+x^ry^{r+1}\bigr)u^{2r}
+2\sum_{\substack{r\geq1\\2r\leq L}}(xy)^ru^{2r-1}.
\]
The polynomial counting nilpotent partial isometries by rank, with index at most \(L\), is exactly
\[
H_L^{a,b}(u)=a!b![x^ay^b]
\left(\exp(P_L(x,u)+P_L(y,u))
+\exp(Q_L(x,y,u))\right)-1.
\tag{1}
\]
Here the exponential is a formal power series; extraction at the indicated finite bidegree makes this a finite, effective formula. Set \(H_0^{a,b}(u)=0\). The **complete joint rank–index polynomial** is therefore
\[
\boxed{\mathcal N_{a,b}(u,v)=\sum_{L=1}^{a+b}v^L
\bigl(H_L^{a,b}(u)-H_{L-1}^{a,b}(u)\bigr).}
\tag{2}
\]
The coefficient of \(u^rv^L\) counts *exactly* those nilpotent elements with rank \(r\) and index \(L\).

In particular, the total nilpotent count is
\[
\boxed{\mathcal N_{a,b}(1,1)=
L_aL_b+a!b![x^ay^b]\exp\!\left(\frac{x+y+2xy}{1-xy}\right)-1,}
\tag{3}
\]
where \(L_j=j![t^j]\exp(t/(1-t))\) is the number of nilpotent partial injections on a labeled set of size \(j\), including the empty map.

There is also a sharp **extremal phase transition**. Suppose \(a\geq b\geq2\). The largest possible nilpotency index \(M_{a,b}\), and the number \(E_{a,b}\) of elements attaining it, are
\[
\boxed{
(M_{a,b},E_{a,b})=
\begin{cases}
(2b,\;2(b!)^2),&a=b,\\[2pt]
(2b+1,\;a!b!/(a-b-1)!),&b<a<2b+1,\\[2pt]
(a,\;a!(L_b+1)),&a=2b+1,\\[2pt]
(a,\;a!L_b),&a>2b+1.
\end{cases}}
\tag{4}
\]
The switch occurs precisely at the side-size ratio \(a=2b+1\): the longest nilpotent chains switch from **alternating between** the sides to **remaining within** the larger side. At the boundary both mechanisms coexist, and their extremizer counts add.

For example, for \(K_{2,2}\) the index distribution (indexes one through four) is \((1,24,8,8)\). For \(K_{3,2}\) it is \((1,56,60,24,12)\), and for \(K_{4,2}\) it is \((1,138,224,120,48)\).

## Assumptions and scope

All graphs are finite, simple and connected, with every edge between different bipartition parts. Their graph metric takes value one on different-part pairs and value two on distinct same-part pairs. Partial isometries have arbitrary domains and are injective because distance zero is preserved. Multiplication is ordinary composition of partial maps, and the zero element is the empty partial map.

The new classification, formulas (1)–(4), and all proof assertions are stated for \(a,b\geq2\). The underlying counting expressions remain valid when one part has size one, but that star specialization is not asserted to be new. Formula (4) uses \(a\geq b\) solely to avoid duplicating symmetric cases. The parameter \(u\) marks the number of directed arrows (domain elements), and \(v\) marks the least positive nilpotency exponent.

## Proof

**1. The two-orientation decomposition.** Let \(f\) be a nonempty partial isometry. Any distinct vertices in one side have distance two and their images must again occupy one side; two vertices from opposite sides have distance one and their images must occupy opposite sides. If the domain meets both sides, it follows that the entire map either preserves each side or exchanges the sides. The same conclusion holds if the domain meets only one side: all its images lie in one side, uniquely determining whether the map preserves or exchanges side labels. Even a singleton-domain map determines one of these two orientations from its source and target sides. Thus every nonempty partial isometry has a **unique** orientation, either side-preserving or side-exchanging. Conversely, any partial injection with either of these uniform orientations preserves the two-valued graph distance. The two orientation families meet only at the empty map.

**2. Nilpotent partial injections are path assemblies.** The directed graph of a partial injection consists of disjoint directed paths and directed cycles, with isolated vertices regarded as one-vertex paths. It is nilpotent exactly when no directed cycle occurs. A path with \(j\) vertices contributes \(j-1\) arrows to the rank and has nilpotency index \(j\). The index of a disjoint union is the maximum path length.

For a side-preserving map, each path is entirely in \(A\) or entirely in \(B\). A directed path on a specified \(j\)-element labeled set has \(j!\) possible vertex orders; after the two-sort exponential-generating-function normalization, its contribution is \(x^ju^{j-1}\) or \(y^ju^{j-1}\). Truncating path lengths at \(L\) and forming unordered sets of components yields \(\exp(P_L(x,u)+P_L(y,u))\).

For a side-exchanging map, every directed path alternates colors. If its length is \(2r+1\), it has either \(r+1\) vertices in \(A\) and \(r\) in \(B\), or the reverse. In either case the ordering of labels gives \((r+1)!r!\) paths, giving the first sum in \(Q_L\). If its length is \(2r\), it has \(r\) vertices of each color and may start in either color; its count on a specified pair of label sets is \(2(r!)^2\), producing the second sum in \(Q_L\). The labeled exponential formula for unordered path components yields \(\exp(Q_L(x,y,u))\).

Extracting \([x^ay^b]\) and multiplying by \(a!b!\) gives the two cumulative enumerators. The empty map belongs to both orientations and to no other overlap, so subtracting one gives (1). The longest directed path has at most \(a+b\) vertices. Taking successive index cutoffs gives (2). For unrestricted lengths, the one-color component sum is \(t/(1-t)\) and the alternating component sum is
\[
\frac{x+y}{1-xy}+\frac{2xy}{1-xy}=\frac{x+y+2xy}{1-xy};
\]
this proves (3).

**3. The sharp extremal transition.** Assume \(a\geq b\). In a side-preserving map, a path cannot be longer than \(a\) vertices, and this bound is attainable. If \(a>b\), attaining it requires all \(a\) vertices of \(A\) to form a single directed path, with \(a!\) choices; the nilpotent partial injection on \(B\) is arbitrary and has \(L_b\) choices. Thus exactly \(a!L_b\) side-preserving maps attain index \(a\).

In a side-exchanging map, a path must alternate sides. If \(a=b\), its maximum length is \(2b\), attained by a Hamiltonian alternating path. There are two starting-side choices and \((b!)^2\) orders of the labeled vertices, yielding \(2(b!)^2\) extremizers. Because the side-preserving maximum is only \(b\), these are precisely the global extremizers.

If \(a>b\), an alternating path has length at most \(2b+1\); achieving equality uses all \(b\) vertices of the smaller side and \(b+1\) of the larger side. All remaining vertices of \(A\) are forced to be isolated, since all \(B\)-vertices lie in the long path. Choosing and ordering the vertices of the long path gives
\[
\binom{a}{b+1}(b+1)!b!=\frac{a!b!}{(a-b-1)!}
\]
side-exchanging extremizers. Comparison of the two possible maxima, \(a\) and \(2b+1\), yields all four cases of (4), including addition of disjoint orientation classes at equality. This proves the theorem.

## Verification

The accompanying `verify.py` evaluates each truncated labeled-component exponential over exact rational coefficients, extracts every rank/index cell, and independently enumerates all partial injections on the vertex set. The brute-force routine checks pairwise graph distances and detects directed cycles by explicit orbit following. The two complete tables agree for **15** pairs \((a,b)\) with \(1\leq a,b\leq4\) and \(a+b\leq7\), including all nonstar instances in that range. The sharp maximal index and extremizer formulas agree with the same direct enumeration. The code uses Python's standard library only; run `python verify.py`.

## Relationship to prior work

Fernandes and Paulista [1] study partial isometries of star graphs (the one-vertex-side case), giving their structural decomposition, cardinalities, ranks, Green relations and presentation. The star nilpotent rank/index spectrum is also previously recorded. Those one-side-size-one cases are deliberately excluded from the asserted new theorem; no star-only consequences are claimed as novel. Fernandes and Paulista [2] describe the partial-isometry monoid of cycle graphs; the square \(K_{2,2}\) is the four-cycle. Their published results address cardinality, rank, Green relations and presentation. An earlier complete rank/index census of partial isometries of every cycle already covers the instance \(K_{2,2}=C_4\); that instance is included here as a consistency specialization, not an independently new discovery. FitzGerald [3] develops a general representation theory of inverse semigroups in partial automorphism settings, without this concrete enumeration.

The present counting is not a replacement for these structural monoid descriptions or the complete earlier cycle enumeration. It concerns the complete nilpotent rank/index spectrum for **both parts of size at least two**, and its sharp side-imbalance phase boundary, which requires the two-color alternating path assembly absent from the star specialization.

## Limitations

The theorem does not classify nonnilpotent elements, multiplication tables, automorphism groups, or all regularity classes. The proof gives exact finite formulas and extremal counts, not an asymptotic law for random nilpotent elements. The component-exponential method is standard combinatorial technology; the novelty assessment concerns its exact application to this monoid, the two-orientation decomposition, and the resulting phase transition. Equivalent formulations may exist under colored partial permutations or partial automorphism terminology, so exhaustive publication priority is not asserted. The computational tests are finite corroboration rather than a substitute for the unrestricted proof.

## References

[1] V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a finite star graph*, arXiv:2203.05504, first posted 2022-03-10, https://arxiv.org/abs/2203.05504 .

[2] V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a cycle graph*, arXiv:2205.02196, first posted 2022-05-04, https://arxiv.org/abs/2205.02196 .

[3] D. G. FitzGerald, *Representations of inverse semigroups in complete atomistic inverse meet-semigroups*, arXiv:1906.06415, first posted 2019-06-14, https://arxiv.org/abs/1906.06415 .
