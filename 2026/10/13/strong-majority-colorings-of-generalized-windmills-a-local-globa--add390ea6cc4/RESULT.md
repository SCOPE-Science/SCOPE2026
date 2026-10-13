# Strong majority colorings of generalized windmills: a local-global transition

## Finding

Let \(W_{n,m}=K_1\vee(nK_m)\) be the generalized windmill formed from \(n\ge2\) labeled \(m\)-clique blades, \(m\ge2\), sharing a universal center \(z\). A **strong majority vertex coloring** is any vertex labeling by colors such that, for every vertex \(v\) and color \(\alpha\), at most \(\deg(v)/2\) neighbors of \(v\) have color \(\alpha\). Colors need not be proper, and a coloring with \(q\) available labels may leave some labels unused.

The complete structure depends on the blade size.

**Two-vertex blades.** For \(m=2\), a coloring is strong majority if and only if no blade vertex has the center's color, and each other color occurs at most \(n\) times among the \(2n\) blade vertices. Within any individual two-vertex blade, the colors may coincide.

**Larger clique blades.** For \(m\ge3\), put \(h=\lfloor m/2\rfloor\). A coloring is strong majority if and only if **in each blade separately** the center color appears at most \(h-1\) times and every other color appears at most \(h\) times. These conditions are completely independent between different blades: the center's own majority requirement is automatically satisfied whenever all blade conditions hold.

Consequently, for all \(n\ge2\),
\[
\boxed{\operatorname{Maj}(W_{n,m})=
\begin{cases}4,&m=3,\\3,&m=2\text{ or }m\ge4.\end{cases}}
\]
There is also an exact **all-colorings enumeration**. Let \(A_q(n,m)\) count strong majority maps into a fixed labeled palette of \(q\ge1\) colors, allowing unused labels. For \(s\ge0\), define the truncated exponential polynomial
\[E_s(x)=\sum_{j=0}^s\frac{x^j}{j!}.\]
For \(m\ge3\),
\[
\boxed{A_q(n,m)=q\left(m![x^m]E_{h-1}(x)E_h(x)^{q-1}\right)^n,\qquad h=\lfloor m/2\rfloor.}
\]
For \(m=2\),
\[
\boxed{A_q(n,2)=q
\sum_{\substack{t_1+\cdots+t_{q-1}=2n\\0\le t_j\le n}}
\frac{(2n)!}{t_1!\cdots t_{q-1}!}.}
\]
An empty sum is zero. In particular \(A_1=A_2=0\) for all allowed \(n,m\), and \(A_3(n,3)=0\). The number of surjective colorings onto a fixed \(q\)-color palette is
\[
\boxed{S_q(n,m)=\sum_{j=0}^{q}(-1)^j\binom qj A_{q-j}(n,m),\quad A_0(n,m)=0.}
\]
At the minimum palette size, every coloring is surjective. Several simple optimal-count formulas are
\[
\boxed{S_3(n,2)=3\binom{2n}{n},\quad S_4(n,3)=4\cdot6^n,\quad
S_3(n,4)=S_3(n,5)=3\cdot30^n.}
\]
The feasible numbers of used colors form the whole interval from the stated minimum to \(|V(W_{n,m})|=nm+1\).

## Assumptions and scope

Graphs are finite, simple, undirected. The join \(G\vee H\) adds all possible edges between disjoint copies of its factors; \(nK_m\) is the disjoint union of \(n\) cliques of order \(m\). Each vertex of a blade has degree \(m\). The center has degree \(nm\). A strong majority coloring permits adjacent vertices to share a color; it is **not** ordinary proper coloring, majority C-coloring, or strong majority **edge** coloring. The statement begins at \(n=2\) to avoid treating previously studied complete graphs \(W_{1,m}=K_{m+1}\) as a new scalar family.

## Proof

Fix a color palette with \(q\) labels and write \(\alpha\) for the center color. In a fixed blade \(B\cong K_m\), denote by \(a_\beta\) the number of blade vertices of color \(\beta\). A vertex \(v\in B\) of color \(\gamma\) has precisely
\[
 a_\beta+\mathbf 1_{\{\beta=\alpha\}}-\mathbf 1_{\{\beta=\gamma\}}
\]
neighbors of color \(\beta\): all other blade vertices and the center. Because the vertex degree is \(m\), its strong majority cap is \(h=\lfloor m/2\rfloor\).

**Case \(m=2\).** Each blade vertex sees exactly the center and its blade mate, so these two neighbors must receive distinct colors. Consequently neither blade vertex may have color \(\alpha\). Conversely, this exclusion ensures the strong majority condition at both blade vertices, irrespective of whether their own two colors are equal. At the center, exactly \(2n\) vertices are neighbors; its cap is \(n\). It is therefore necessary and sufficient that every non-center color appear at most \(n\) times across all leaves. This proves the first structural statement. For counting, choose the center label in \(q\) ways, then distribute the \(2n\) individually distinguished leaf vertices among the remaining \(q-1\) labels with multiplicities at most \(n\). Multinomial counting gives the stated formula for \(A_q(n,2)\).

**Case \(m\ge3\).** No blade can be monochromatic: if the sole blade color is \(\alpha\), each blade vertex sees \(m>h\) neighbors of that color; if the sole blade color differs from \(\alpha\), each vertex sees \(m-1>h\) neighbors of its own color. Thus each blade uses at least two different colors. For every blade color \(\beta\) there is a vertex in the blade whose color differs from \(\beta\), and for every absent blade color any vertex may be used. Hence the displayed neighbor-count formula forces \(a_\alpha+1\le h\) and \(a_\beta\le h\) for all \(\beta\ne\alpha\). These inequalities are therefore necessary.

Conversely, suppose the inequalities hold for a blade. For any vertex color \(\gamma\), its count of neighbors of color \(\beta\) is at most \(a_\beta+\mathbf 1_{\{\beta=\alpha\}}\), which is at most \(h\) by the inequalities. Thus all blade vertices satisfy the condition. Over the entire graph the center sees, for each color, at most \(nh\) vertices because every blade has at most \(h\) vertices of that color (and at most \(h-1\) for \(\alpha\)). But
\[
 nh\le\left\lfloor\frac{nm}{2}\right\rfloor,
\]
so the center also satisfies the strong majority condition. There is no constraint linking different blades. This proves the exact local factorization.

With the center color fixed, a single labeled blade can receive count vector \((a_\alpha,a_2,\ldots,a_q)\) of total \(m\) if and only if \(a_\alpha\le h-1\) and \(a_j\le h\) for all other colors. The number of assignments realizing those counts is the multinomial coefficient \(m!/(a_\alpha!\prod_{j=2}^q a_j!)\). Therefore the number of valid labelings of one blade is
\[
 L_{m,q}=m![x^m]E_{h-1}(x)E_h(x)^{q-1}.
\]
The \(n\) blades are independent and the center has \(q\) possible labels, yielding \(A_q=qL_{m,q}^n\). Inclusion-exclusion over unused palette labels gives the surjective formula \(S_q\).

**Optimal numbers of colors.** One color is impossible because the graph has edges and positive degree, and for \(m=2\) two colors fail because all \(2n\) leaves must then use the sole non-center color, exceeding the center's capacity \(n\). For \(m\ge3\), two colors offer total permitted capacity at most \((h-1)+h=2h-1<m\) in a blade, so are impossible. For \(m=3\), \(h=1\), three colors offer permitted blade capacity only \(0+1+1=2<3\); four colors allow the center color only at the center and three distinct other colors once per blade. This gives a strong majority four-coloring since each color occurs at most \(n\) times among the \(3n\) center-neighbors. For \(m=2\), color the two vertices of each blade with different non-center colors; these two colors each occur exactly \(n\) times among the center-neighbors, yielding three colors.

For \(m\ge4\), set \(h=\lfloor m/2\rfloor\) and color in each blade exactly one vertex with the center color, \(h\) vertices with a second color, and the remaining \(m-h-1\) vertices with a third color. The last number is positive for \(m\ge4\), and both non-center counts are at most \(h\); also \(1\le h-1\). Hence the local criterion holds and three colors suffice. This proves the exact \(\operatorname{Maj}\) formula.

For the optimal counts: when \(m=2\), a three-color palette has one center color and two non-center colors; both non-center multiplicities must equal \(n\), giving \(3\binom{2n}{n}\) colorings. When \(m=3\), each blade is a permutation of the three non-center colors, giving \(4(3!)^n\). For \(m=4\) and \(m=5\) a direct coefficient expansion gives respectively
\[
 L_{4,3}=\frac{4!}{0!2!2!}+2\frac{4!}{1!2!1!}=6+24=30,
\quad L_{5,3}=\frac{5!}{1!2!2!}=30.
\]
Therefore both families have \(3\cdot30^n\) optimal labeled colorings.

Finally, any strong majority coloring remains valid when the vertices of an existing color class are split into two colors, since all monochromatic neighborhood counts weakly decrease. Repeating such splits from an optimal coloring reaches every feasible color count up to the number of vertices.

## Verification

The standalone script `artifacts/verify.py` independently constructs graph adjacency and checks every vertex-neighborhood/color-frequency inequality. It compares this direct test with the exact structural criterion and with the multinomial or truncated-exponential counting formula for every tested palette size. It also checks explicit optimal constructions at all pairs \(1\le n\le40\), \(2\le m\le40\). The exhaustive tests include every palette size from \(1\) to \(\min\{4,nm+1\}\) for the parameter profiles within \(1\le n\le4\), \(2\le m\le5\), \(nm+1\le9\). The domain \(n=1\) is included as an additional boundary check though the new theorem is stated for \(n\ge2\).

Replay output:

`ALL CHECKS PASSED; exhaustive_parameter_cases=35; labeled_maps_checked=609960; constructions=1560; exact_special_counts={(1, 2): 6, (1, 3): 24, (1, 4): 90, (1, 5): 90, (2, 2): 18, (2, 3): 144, (2, 4): 2700, (3, 2): 60, (4, 2): 210}`

These finite computations are corroborative, not a proof for unbounded parameters. The analytic proof above establishes the arbitrary-parameter statement.

## Relationship to prior work

Kalinowski, Kamyczura, Pilśniak, and Woźniak introduced strong majority vertex colorings in 2026, along with the minimum-color invariant \(\operatorname{Maj}\). Their paper proves the exact value for complete graphs and cycles and develops general bounds and graph constructions. In particular, their complete-graph observation supplies the \(n=1\) windmill scalar value as prior work. The inspected full text contains no windmill/friendship treatment, and its graph-family results do not state the local-versus-global structural dichotomy or the coloring enumerators here.

Bujtás, Dettlaff, Furmańczyk, and Laskowska considered majority C-colorings and explicitly included Dutch windmill/friendship graphs. That is a different invariant: a majority C-coloring requires a vertex to share its own color with at least half of its neighbors and *maximizes* the number of colors, whereas strong majority requires **each** neighborhood color to occupy at most half of the neighborhood and *minimizes* colors. Their friendship value cannot imply these statements.

A 2026 follow-up on majority coloring games focuses on alternating-player color selection, complexity, and cycles; game thresholds are not the static all-colorings enumeration here. Related published database entries include generalized-windmill general-position polynomials and strong-majority **edge** coloring on bipartite graphs, neither of which is implication-equivalent.

## Limitations

The result is restricted to the equal-size clique-blade graph \(K_1\vee nK_m\), with \(n\ge2\) and \(m\ge2\). For noncomplete blade graphs \(H\), the independent-blade factorization need not hold. The transfer formula counts labeled maps to a palette; unlabeled or automorphism-quotient counts are distinct questions. The visible public literature search does not certify absolute novelty: synonymous “clique bouquet” or “friendship generalization” treatments and concurrent 2026 work remain possible. No independent external validation has been performed.

## References

1. R. Kalinowski, M. Kamyczura, M. Pilśniak, and M. Woźniak, “Strong majority colorings of graphs,” arXiv:2605.23828v1, first public May 22, 2026. First listed subject classification \(05C15\), followed by \(05C70\) in indexed bibliographic metadata.
2. C. Bujtás, M. Dettlaff, H. Furmańczyk, and A. Laskowska, “Majority C-coloring of graphs,” arXiv:2604.20752v1, first public April 22, 2026. (A distinct majority notion.)
3. Y. Chawda, S. G. Nanoti, B. Sankarnarayanan, and E. Srinivasan, “Structural and computational aspects of majority coloring games,” arXiv:2609.37796v1, first public September 29, 2026. (Game variants rather than static enumeration.)
