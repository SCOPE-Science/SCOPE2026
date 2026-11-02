# Exact singleton two-rainbow domination of rectangular rook graphs

## Finding

**Theorem.** Let \(2\le m\le n\) be integers, and let \(R_{m,n}=K_m\square K_n\) be the graph with vertex set \([m]\times[n]\), where distinct vertices are adjacent if they share one coordinate. A *singleton two-rainbow dominating function* is a map \(f:V(R_{m,n})\to\{0,1,2\}\) such that every vertex labelled \(0\) has a neighbor labelled \(1\) and a neighbor labelled \(2\). Its weight is the number of nonzero labels. Then

\[
\widetilde\gamma_2(R_{m,n})=\min\{2m,m+n-2\}.
\]

In particular, the minimum is \(2m-2\) on square boards, \(2m-1\) for width \(m+1\), and \(2m\) for every width at least \(m+2\). The theorem also determines the dual-server domination number of \(R_{m,n}\), since a dual-server dominating set is precisely the union of the two nonzero color classes.

## Assumptions and scope

Graphs are finite, simple, and undirected. The two colors are mutually distinguishable, and each vertex receives **at most one** color, rather than an arbitrary subset of colors. A colored vertex is exempt from the two-neighbor requirement. We assume \(2\le m\le n\); transposition gives the formula for any two dimensions at least two. This is not the classical set-valued rainbow domination parameter or proper rainbow domination.

## Proof

Let \(f\) be a feasible function with \(w\) colored vertices. An empty row (a row with no colored vertices) forces **each column** to contain a vertex of each color: an uncolored cell in that row can see colored neighbors only in its column. Thus \(w\ge2n\ge2m\). Symmetrically an empty column forces each row to contain both colors, giving \(w\ge2m\). Hence if \(w<2m\), every row and column contains at least one color.

Assume henceforth that \(w<2m\). Classify rows by their sets of colors: \(a\) rows contain only color \(1\), \(b\) contain only color \(2\), and \(c\) contain both, so \(a+b+c=m\). Likewise let \(p,q,r\) be the counts of columns containing respectively only \(1\), only \(2\), or both; then \(p+q+r=n\). Write \(x\) and \(y\) for the numbers of vertices labelled \(1\) and \(2\), with \(w=x+y\).

When \(a,p>0\), every cell at the intersection of a color-\(1\)-only row and color-\(1\)-only column must be colored \(1\): if uncolored, its row and column together contain no color \(2\). These \(ap\) forced cells lie in neither a both-color row nor a both-color column. Every one of the \(c\) both-color rows and \(r\) both-color columns needs at least one **additional** \(1\), so

\[
x\ge ap+\max\{c,r\}\quad(a,p>0).
\]

Without the simultaneous positivity assumption, every row containing color \(1\) and every column containing color \(1\) must be met by a \(1\)-cell, yielding the universally valid inequality

\[
x\ge\max\{a+c,p+r\}.
\]

By exchanging colors, if \(b,q>0\) then \(y\ge bq+\max\{c,r\}\), and always \(y\ge\max\{b+c,q+r\}\).

If both \(a,p>0\) and \(b,q>0\), use \(ap\ge a+p-1\) and \(bq\ge b+q-1\) to obtain

\[
\begin{aligned}
w&\ge ap+bq+2\max\{c,r\}\\
&\ge m+n-2+|c-r|\ge m+n-2.
\end{aligned}
\]

Suppose exactly one of the pairs \((a,p)\), \((b,q)\) is simultaneously positive. By symmetry suppose \(a,p>0\). Either \(b=0\) or \(q=0\). In the first case, the lower bounds above give

\[
w\ge(ap+c)+(q+r)\ge(a+p-1+c)+(q+r)=m+n-1.
\]

In the second case they give

\[
w\ge(ap+r)+(b+c)\ge(a+p-1+r)+(b+c)=m+n-1.
\]

Finally suppose neither pair is simultaneously positive. If \(a=b=0\), all rows contain both colors, giving \(w\ge2m\). If \(a,b>0\), then \(p=q=0\), so all columns contain both colors and \(w\ge2n\ge2m\). Otherwise, exactly one of \(a,b\) is positive. If \(a>0,b=0\), every row contains color \(1\) and \(p=0\) ensures every column contains color \(2\), so \(w\ge m+n\); the case \(b>0,a=0\) is symmetric. In every case \(w\ge\min\{2m,m+n-2\}\), contradicting \(w<\min\{2m,m+n-2\}\). This establishes the lower bound.

For the upper bound, a coloring of weight \(2m\) always exists: in every row color its first cell \(1\) and its second cell \(2\), leaving the other cells empty. Every empty cell sees both colors in its own row.

It remains to construct weight \(m+n-2\) when \(n=m\) or \(n=m+1\). For \(m=2\) or \(m=3\), color all cells \((1,j)\), \(1\le j<n\), with \(1\), and all cells \((i,n)\), \(2\le i\le m\), with \(2\). This has \((n-1)+(m-1)=m+n-2\) colored vertices. Every zero has a color-\(1\) neighbor in its column and a color-\(2\) neighbor in its row (or the other way around as appropriate).

For \(m\ge4\), set \(d=m-2\) and \(p=n-m+1\in\{1,2\}\). Color cells \((1,j)\), \(1\le j\le p\), with \(1\), and cell \((2,p+1)\) with \(2\). Among rows \(3,\ldots,m\) and columns \(p+2,\ldots,n\), which form a \(d\times d\) square, put color \(1\) on the diagonal and color \(2\) on the cyclic superdiagonal; as \(d\ge2\), these diagonals are disjoint. Leave every other cell uncolored. The first row and first \(p\) columns have only color \(1\), the second row and column \(p+1\) have only color \(2\), and all remaining rows/columns contain both colors. Intersections of two only-\(1\) or two only-\(2\) lines are exactly the precolored cells. Thus every uncolored cell sees both colors. The weight equals

\[
p+1+2d=(n-m+1)+1+2(m-2)=m+n-2.
\]

Together with the universal \(2m\) construction, this completes the proof. \(\square\)

## Verification

Run `python3 verify.py` using Python 3 and its standard library, in the same directory as this document. The program checks the explicit construction at \(114\) dimension pairs, from \(2\le m\le20\) and \(m\le n\le m+5\), directly against each uncolored vertex's neighbors, and checks weights. It exhaustively evaluates all assignments smaller than the theorem's bound for eight small dimension pairs, totaling \(308{,}540\) candidate assignments. It also tests palette-count inequalities for \(44\) parameter pairs. Expected terminal output ends in `VERIFY_OK`. These finite checks are not substituted for the all-parameter proof.

## Relationship to prior work

Lange (arXiv:2610.06906, first public 2026-10-01) studies this precise one-color-per-selected-vertex rainbow \(k\)-domination model for regular graphs; the inspected full text gives exact values for cycles, Möbius ladders, prisms, and a generalized Petersen family, not rook graphs. In the equivalent language of dual-server domination, Rao, Udupa, and Prathviraj (arXiv:2608.14690, first public 2026-08-07) give a product theorem about **when every vertex must be selected**. Their Theorem 3.4 states \(\gamma_{ds}(G\square H)=|V(G\square H)|\) exactly when the degree maxima sum to at most one; on rook graphs that theorem only excludes full selection and does not imply the minimum established here. Jose and Sangeetha (2018) study **proper** two-rainbow domination on Cartesian products of complete graphs; their constraints forbid adjacent same-colored vertices and permit set-valued assignments, unlike the present singleton variant, and the inspected product result is a bound, not the present exact classification. These comparisons distinguish actual statements and implications rather than just titles.

## Limitations

The theorem determines the minimum size, not all minimizing functions, their number, or analogous values with three or more colors. It does not cover arbitrary Cartesian products. Priority is provisional: the introductory paper *Dual-server domination in graphs* (Chellali–Haynes–Hedetniemi, 2026) could not be read in full from accessible public sources, and equivalent results under additional terminology may exist.

## References

1. P. Lange, *Complexity, Bounds, and Exact Algorithms for Rainbow \(k\)-Domination in Regular Graphs*, arXiv:2610.06906 (first posted 2026-10-01), https://arxiv.org/abs/2610.06906 .
2. S. L. Rao, S. Udupa N. V. and Prathviraj N., *The Dual-Server Domination Number of Some Graph Operations*, arXiv:2608.14690 (first posted 2026-08-07), https://arxiv.org/abs/2608.14690 .
3. J. Jose and V. Sangeetha, *Bounds on proper 2-rainbow domination in graphs*, 2018, doi:10.13140/RG.2.2.11704.80645, https://www.researchgate.net/publication/327208249_Bounds_on_proper_2-rainbow_domination_in_graphs .
4. M. Chellali, T. W. Haynes and S. T. Hedetniemi, *Dual-server domination in graphs*, Discrete Applied Mathematics 387 (2026), 251–259, doi:10.1016/j.dam.2026.03.017 .
