# Proper conflict-free chromatic number of crown graphs

## Finding
For an integer \(n\ge 2\), let \(\operatorname{Cr}_n\) be the crown graph obtained from \(K_{n,n}\) by deleting a perfect matching \(\{a_i b_i:1\le i\le n\}\). Then the proper conflict-free chromatic number with respect to open neighborhoods is
\[
\chi_{\mathrm{pcf}}(\operatorname{Cr}_n)=
\begin{cases}
2,&n=2,\\
3,&n=3,\\
4,&n\ge4.
\end{cases}
\]
In particular, the family has unbounded maximum degree \(n-1\) but constant proper conflict-free chromatic number from \(n=4\) onward.

## Assumptions and scope
All graphs are finite and simple. A proper coloring is proper conflict-free when every non-isolated vertex has a color that occurs exactly once in its open neighborhood. The two bipartition classes of \(\operatorname{Cr}_n\) are \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), with \(a_i\) adjacent to \(b_j\) exactly when \(i\ne j\).

A structural fact used below is that if a color occurs on both sides of a proper coloring of \(\operatorname{Cr}_n\), then it occurs exactly on one deleted matched pair \(\{a_i,b_i\}\), and hence is a singleton color on each side. Indeed, if the same color occurs on \(a_i\) and \(b_j\), properness forces \(i=j\); any additional occurrence on either side would then be adjacent to the occurrence on the other side.

## Proof
For \(n=2\), \(\operatorname{Cr}_2\) is two disjoint edges. Two colors give a proper conflict-free coloring, while one color is impossible because edges are present.

For \(n=3\), assign color \(i\) to both \(a_i\) and \(b_i\), for \(i\in\{1,2,3\}\). Every monochromatic pair is a deleted matching edge, so the coloring is proper. Every vertex has two neighbors of two distinct colors, hence both neighborhood colors occur uniquely. Thus \(\chi_{\mathrm{pcf}}(\operatorname{Cr}_3)\le3\). A proper two-coloring of the connected bipartite graph \(\operatorname{Cr}_3\cong C_6\) colors each side monochromatically, so every vertex sees its two neighbors in the same color; therefore two colors are not proper conflict-free.

Now let \(n\ge4\). A four-coloring is obtained by setting
\[
\varphi(a_1)=\varphi(b_1)=1,\qquad
\varphi(a_2)=\varphi(b_2)=2,
\]
\[
\varphi(a_i)=3,\qquad \varphi(b_i)=4\qquad(3\le i\le n).
\]
The only colors used on both sides are \(1\) and \(2\), each on its deleted matched pair, so the coloring is proper. Every vertex is adjacent to at least one of the two singleton-colored vertices on the opposite side: a vertex with index \(1\) sees the singleton of color \(2\), one with index \(2\) sees the singleton of color \(1\), and every other vertex sees both. Hence the coloring is proper conflict-free and \(\chi_{\mathrm{pcf}}(\operatorname{Cr}_n)\le4\).

It remains to exclude colorings with at most three colors. Consider any proper coloring using at most three colors, and call a color *shared* if it occurs on both \(A\) and \(B\). By the structural fact above, every shared color is confined to one deleted matched pair and is a singleton on each side.

If there is no shared color, the palettes used on \(A\) and \(B\) are disjoint. With at most three colors, one side therefore uses only one color. Every vertex on the opposite side has degree \(n-1\ge3\) and sees that color repeated \(n-1\) times, so no neighborhood color is unique.

If there is exactly one shared color, say on \(\{a_i,b_i\}\), then each side must also use a side-exclusive color because it has \(n\ge4\) vertices and a shared color can occur only once on that side. With at most three colors the two palettes are therefore \(\{c,x\}\) and \(\{c,y\}\), where \(c\) is shared and \(x,y\) are side-exclusive. The vertex \(a_i\) does not see \(b_i\); all \(n-1\) vertices in its neighborhood then have color \(y\), so its neighborhood has no unique color.

Exactly two shared colors are impossible: after their two forced singleton matched pairs, each side still contains at least two vertices, so each side needs the only remaining color; that would make the third color shared as well. If all three colors are shared, each side contains only the three singleton occurrences of those colors, contradicting \(n\ge4\). Thus no proper conflict-free coloring with at most three colors exists, proving the formula.

## Verification
The proof above is uniform in \(n\). The accompanying `verify.py` independently checks the constructions for \(2\le n\le12\) and exhaustively excludes colorings below the claimed minimum for \(n=2,3,4,5\), using restricted-growth canonicalization of color names and direct testing of properness and the conflict-free neighborhood condition.

## Relationship to prior work
Proper conflict-free coloring with respect to open neighborhoods was introduced in the proper setting by Fabrici, Lužar, Rindošová, and Soták. Caro, Petruševski, and Škrekovski developed the parameter on basic graph classes, and subsequent work established complexity results and general maximum-degree bounds. The crown graphs form a classical dense bipartite family; the theorem above gives their exact values and a side-sharing lemma tailored to the deleted perfect matching.

## Limitations
The result concerns ordinary proper conflict-free coloring, not list coloring, fractional variants, unique-maximum coloring, or \(h\)-conflict-free coloring for \(h>1\). It does not characterize all optimal four-colorings when \(n\ge4\). The finite replay is a sanity check rather than a formal proof and does not replace the uniform argument.

## References
1. I. Fabrici, B. Lužar, S. Rindošová, R. Soták, “Proper conflict-free and unique-maximum colorings of planar graphs with respect to neighborhoods,” arXiv:2202.02570, first public version 2022-02-05; Discrete Applied Mathematics 324 (2023), 80–92.
2. Y. Caro, M. Petruševski, R. Škrekovski, “Remarks on proper conflict-free colorings of graphs,” arXiv:2203.01088; Discrete Mathematics 346 (2023), 113221.
3. J. Ahn, S. Im, S.-i. Oum, “The proper conflict-free \(k\)-coloring problem and the odd \(k\)-coloring problem are NP-complete on bipartite graphs,” arXiv:2208.08330.
4. D. W. Cranston, C.-H. Liu, “Proper Conflict-Free Coloring of Graphs with Large Maximum Degree,” arXiv:2211.02818; SIAM Journal on Discrete Mathematics 38 (2024), 3004–3027.
5. C.-H. Liu, B. Reed, “Asymptotically Optimal Proper Conflict-Free Coloring,” Random Structures & Algorithms 66 (2025), e21285.
