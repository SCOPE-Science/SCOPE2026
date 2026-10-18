# The rational symmetry character of complete-bipartite Boolean complexes

## Finding

Let \(m,n\geq1\). For the Boolean cell complex \(\mathcal B(K_{m,n})\) formed from commutation classes of injective words on the vertices of the complete bipartite graph, the natural side-preserving action of \(S_m\times S_n\) on top-dimensional rational homology has character
\[
\boxed{\operatorname{tr}\bigl((\sigma,\tau)\mid\widetilde H_{m+n-1}(\mathcal B(K_{m,n});\mathbb Q)\bigr)
=\operatorname{sgn}(\sigma)\operatorname{sgn}(\tau)
\,\beta\bigl(K_{c(\sigma),c(\tau)}\bigr).}
\]
Here \(c(\pi)\) counts **all** cycles, including fixed points, of a permutation, and \(\beta(K_{p,q})\) is the known Boolean number (top Betti number) for the indicated smaller complete bipartite graph. In particular,
\[
\beta(K_{p,q})=\sum_{j=1}^{p}(-1)^{p-j}j!\left\{\begin{matrix}p+1\\j+1\end{matrix}\right\}j^q
\qquad (p,q\geq1),
\]
where braces denote Stirling numbers of the second kind. The complete character therefore depends on a permutation only through the number of cycles and its sign. Further,
\[
\dim_{\mathbb Q}\widetilde H_{m+n-1}(\mathcal B(K_{m,n});\mathbb Q)^{S_m\times S_n}
=\begin{cases}1,&m=n,\\0,&m\ne n.\end{cases}
\]
The existing nonequivariant wedge-of-spheres theorem is assumed, not claimed as new.

## Assumptions and scope

Take two disjoint sets \(L\) and \(R\) of \(m\) and \(n\) distinct labeled vertices. In a word without repeated letters, two *adjacent* letters may be exchanged exactly when they lie in the **same** part. A cell of dimension \(s-1\) corresponds to such a commutation class of words with \(s\) letters; the empty word is the augmented cell of dimension \(-1\). Faces are obtained by deleting a selected set of letters. This is the regular Boolean cell complex of Jonsson and Welker, equivalently the Boolean complex associated to \(K_{m,n}\) studied by Ragnarsson and Tenner. Every face has a Boolean face interval, so its cellular orientation can be set by the increasing order of its labeled vertices, independently of its word representative. A label permutation that fixes a cell acts on its oriented interior with the sign of its permutation of that cell's vertices.

Only permutations preserving \(L\) and \(R\) are included. The homology is reduced rational homology. For \(m,n\geq1\), the preexisting shellability and wedge theorems imply that reduced homology is zero outside degree \(m+n-1\); hence signed cellular Lefschetz numbers recover its actual character. The equality extends across all positive integers \(m,n\) without assuming \(m=n\).

## Proof

**1. Cells and acyclic orientations.** On a fixed vertex subset \(S\) with \(a\) left and \(b\) right vertices, order the vertices according to a word and orient each cross-edge from its earlier endpoint to its later endpoint. This is acyclic. Conversely, an acyclic orientation has a linear extension; all its linear extensions differ by adjacent exchanges of incomparable vertices, which in a complete bipartite graph must lie in the same part. Thus cells on \(S\) are precisely the acyclic orientations of \(K_{a,b}\). This identification also covers \(a=0\) or \(b=0\): there is exactly one orientation on an edgeless graph. Let \(A(a,b)\) be the number of these orientations, with \(A(0,0)=1\).

**2. Fixed orientations collapse permutation cycles.** Fix \(g=(\sigma,\tau)\) and a \(g\)-stable vertex subset \(S\). Every row of a bipartite edge-orientation matrix specifies the set of right vertices toward which a given left vertex points. These sets are linearly ordered by inclusion: two incomparable rows would furnish a directed four-cycle. A longer directed cycle in an oriented complete bipartite graph likewise has a directed four-cycle, by repeatedly shortcutting along chords, so this condition characterizes acyclicity.

Under a \(g\)-fixed orientation, rows belonging to one \(\sigma\)-cycle are permuted together with their right-neighbor sets under \(\tau\); hence their sizes agree. Since the row sets are nested, equal sizes force **equal sets**. For any fixed row, invariance then makes its entries constant along each \(\tau\)-cycle. Consequently each pair consisting of a selected \(\sigma\)-cycle and a selected \(\tau\)-cycle has one uniform orientation, and these quotient edge-orientations form an acyclic complete bipartite orientation. Conversely every acyclic orientation on this quotient lifts to a \(g\)-fixed acyclic orientation on \(S\): a directed cycle in the lift would project to a directed closed walk containing a directed cycle in the quotient. Thus if \(S\) comprises \(a\) complete cycles of \(\sigma\) and \(b\) complete cycles of \(\tau\), precisely \(A(a,b)\) cells supported on \(S\) are fixed.

**3. Signed Lefschetz calculation.** Write \(N=m+n\), \(p=c(\sigma)\), \(q=c(\tau)\). On a fixed oriented \((s-1)\)-cell the orientation sign is \(\operatorname{sgn}(g|_S)\). A cycle of length \(\ell\) included in \(S\) contributes \((-1)^{\ell}\) to the sign of the augmented alternating face count and \((-1)^{\ell-1}\) to its orientation sign, so its combined contribution is \(-1\). Let
\[
F_g=\sum_{S:gS=S}(-1)^{|S|}\operatorname{sgn}(g|_S)
\#\{g\text{-fixed acyclic orientations on }S\}.
\]
Because the augmented empty cell has dimension \(-1\), the reduced Lefschetz number is \(-F_g\). Since the homology is concentrated in degree \(N-1\), this gives
\[
\chi_{m,n}(g)=(-1)^N F_g.
\]
By steps 1–2, and because selecting a stable subset means choosing whole permutation cycles,
\[
F_g=\sum_{a=0}^{p}\sum_{b=0}^{q}(-1)^{a+b}
\binom pa\binom qb A(a,b)=F_{\mathrm{id}_{K_{p,q}}}.
\]
Applying exactly the same reduced Euler-characteristic identity to \(\mathcal B(K_{p,q})\), whose reduced homology is only in degree \(p+q-1\), yields \(F_{\mathrm{id}_{K_{p,q}}}=(-1)^{p+q}\beta(K_{p,q})\). Therefore
\[
\chi_{m,n}(g)=(-1)^{m+n+p+q}\beta(K_{p,q})
=\operatorname{sgn}(\sigma)\operatorname{sgn}(\tau)\beta(K_{p,q}),
\]
since a permutation on \(m\) letters with \(p\) cycles has sign \((-1)^{m-p}\), and analogously for \(\tau\). This proves the character formula for every pair of permutations.

**4. Invariant-top-homology corollary.** Over \(\mathbb Q\), averaging over a finite group commutes with homology. For a cell with \(a\) selected left and \(b\) selected right letters, the group orbit of its commutation class is determined by its sequence of maximal monochromatic blocks. If any block has size at least two, a transposition of letters inside that block fixes the cell but reverses its oriented interior; its invariant orbit sum therefore vanishes. Otherwise the color pattern alternates, and its orbit has a nonzero invariant sum. Hence the invariant augmented cellular chain space in degree \(a+b-1\) has one basis element per alternating \(L,R\)-word using \(a\) left and \(b\) right positions, as long as \(a\leq m\) and \(b\leq n\). Such words number two when \(a=b\geq1\), one when \(|a-b|=1\), and zero otherwise (the empty augmented word is counted once in degree \(-1\)).

Their alternating dimensions give the invariant reduced Euler characteristic directly. If \(m=n=k\), the signed augmented sum is \(-1-2k+2k=-1\): there are \(k\) equal-color-count pairs, each contributing \(-2\), and \(2k\) unequal-color-count alternating words, each contributing \(+1\). If \(m>n=k\), the sum is \(-1-2k+(2k+1)=0\), and symmetrically if \(n>m\). Since the homology is concentrated in degree \(N-1\), multiplying the invariant reduced Euler characteristic by \((-1)^{N-1}\) proves the stated dimension formula. For \(m=n\), \(N\) is even and the preceding Euler characteristic is \(-1\), giving dimension one.

## Verification

The supplied `verify_boolean_character.py` is standalone standard-library Python. It exhaustively builds bipartite acyclic orientations as distinct direction matrices of permutations of the vertices, evaluates signed fixed-cell traces on *actual invariant subsets*, and compares to the formula for all conjugacy-class pairs at seven labeled bipartite sizes: \((1,1),(1,2),(2,2),(2,3),(3,3),(2,4),(3,4)\). Exactly 47 class pairs pass. Separate complete permutation averaging checks the invariant dimension claim for all 25 pairs \(1\leq m,n\leq5\). The checks include \(\beta(K_{3,3})=73\) and \(\beta(K_{3,4})=301\). The infinite assertion rests on the proof, not on these finite tests.

To reproduce: run `python3 verify_boolean_character.py`; the script exits unsuccessfully on any failed equality and otherwise reports the exact number of passed tests. Its finite enumerations are exhaustive **within the listed sizes**, not for all sizes.

## Relationship to prior work

Jonsson and Welker developed the regular CW structure and shellability for commutation classes of injective words [1]. Ragnarsson and Tenner proved that Boolean complexes of graphs are wedges of top-dimensional spheres and established the Boolean-number framework [2]. Claesson, Kitaev, Ragnarsson, and Tenner evaluated the nonequivariant Boolean number for Ferrers graphs, including complete bipartite graphs [3]. Ragnarsson and Tenner subsequently studied homology bases [4]. Those results supply the underlying top-homology concentration and known dimensions. The statement here concerns the **entire character under graph automorphisms**, not an alternative proof of those sphere counts or of shellability. The cycle-contraction identity and one-dimensional balanced invariant line yield representation information invisible in any nonequivariant Betti number.

## Limitations

No action that exchanges the two color classes is analyzed, even when \(m=n\); only \(S_m\times S_n\) is covered. The result is rational and makes no assertion about an integral equivariant decomposition, specific cycle representatives, or the other Coxeter graph families. The possibility of an unindexed or inaccessible later equivalent formula is a residual bibliographic uncertainty. No independent external mathematical audit has been performed.

## References

1. J. Jonsson and V. Welker, *Complexes of Injective Words and Their Commutation Classes*, arXiv:0712.2143 (first publicly posted 2007-12-13), especially Lemma 1.1 and Theorem 1.2.
2. K. Ragnarsson and B. E. Tenner, *Homotopy Type of the Boolean Complex of a Coxeter System*, arXiv:0806.0906 (first publicly posted 2008-06-05).
3. A. Claesson, S. Kitaev, K. Ragnarsson, and B. E. Tenner, *Boolean Complexes for Ferrers Graphs*, arXiv:0808.2307 (first publicly posted 2008-08), especially the complete-bipartite Boolean-number formula.
4. K. Ragnarsson and B. E. Tenner, *Homology of the Boolean Complex*, arXiv:1005.4411 (first publicly posted 2010-05).
