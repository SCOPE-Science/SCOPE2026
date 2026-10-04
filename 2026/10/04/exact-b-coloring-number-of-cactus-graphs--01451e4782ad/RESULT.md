# Exact \(B\)-coloring number of cactus graphs
## Finding
Let \(G\) be a finite simple connected cactus graph with at least one edge, and let \(q_B(G)\) be the minimum number of colors in a proper edge-coloring in which every \(4\)-cycle is rainbow. Then
\[
q_B(G)=\begin{cases}
\max\{\Delta(G),4\},&\text{if \(G\) contains a \(4\)-cycle},\\
3,&\text{if \(G\) is an odd cycle},\\
\Delta(G),&\text{otherwise}.
\end{cases}
\]
Consequently every cactus with \(\Delta(G)\ge4\) satisfies \(q_B(G)=\Delta(G)\), and the threshold \(4\) is sharp because a \(4\)-cycle with one pendant edge has maximum degree \(3\) but requires four colors.

## Assumptions and scope
A cactus graph is a finite simple connected graph in which every block is either a bridge or a cycle. A \(B\)-coloring is a proper edge-coloring in which every copy of \(C_4\) receives four pairwise distinct colors; \(q_B(G)\) is the least number of colors in such a coloring. The theorem concerns every connected cactus with at least one edge. The isolated one-vertex graph has \(q_B=0\) separately.

The result is an exact formula, not an asymptotic statement. The only obstructions beyond the maximum degree are a \(C_4\), which forces four colors, and the case in which the entire graph is an odd cycle, which requires three colors by ordinary edge-coloring parity.

## Proof
Write \(\Delta=\Delta(G)\). Properness gives \(q_B(G)\ge\Delta\). If \(G\) contains a \(C_4\), the four edges of that cycle must have distinct colors, so \(q_B(G)\ge4\). If \(G\) itself is an odd cycle, then every \(B\)-coloring is a proper edge-coloring of an odd cycle, so \(q_B(G)\ge3\).

It remains to construct a coloring meeting these lower bounds. Let \(K\) be the right-hand side of the displayed formula and fix a palette of \(K\) colors. Root the block-cut tree of \(G\) at an arbitrary block. Every cycle of a cactus is contained in a single block, so every \(4\)-cycle is a \(C_4\)-block.

Color the root block first. A bridge needs one color. A \(C_4\) receives four distinct colors. An even cycle of length other than four is colored alternately with two colors, and an odd cycle is properly colored with three colors. Each of these uses at most \(K\) colors.

Now process the remaining blocks away from the root. Suppose a new block meets the already colored subgraph only in a cut vertex \(x\). If the new block is a bridge, at most \(\deg_G(x)-1\le K-1\) colors have already appeared at \(x\), so an unused color is available for the new edge.

Suppose instead that the new block is a cycle \(xv_1v_2\cdots v_{\ell-1}x\). At most \(\deg_G(x)-2\) colors have already appeared at \(x\). Hence at least
\[
K-(\deg_G(x)-2)\ge2
\]
colors are available there. Choose two distinct available colors \(a\) and \(b\) for the two cycle edges incident with \(x\).

If \(\ell=4\), then \(K\ge4\); choose two further distinct colors outside \(\{a,b\}\) for the other two cycle edges. The block is then rainbow. If \(\ell\ge6\) is even, alternate \(a,b\) around the cycle. If \(\ell\) is odd, then either this cycle was the whole graph, already handled as the root case, or its attachment to the rest of the graph forces \(\Delta\ge3\), hence \(K\ge3\). Choose \(c\notin\{a,b\}\); color the internal path from \(v_1\) toward \(v_{\ell-1}\) alternately by \(b,a\) through the edge preceding the last internal edge, and use \(c\) on that last internal edge before the final \(b\)-colored edge at \(x\). This is proper for every odd \(\ell\), including \(\ell=3\).

At each step, the new colors at \(x\) avoid all colors already incident there, so properness is preserved. Since a cycle in a cactus lies within a single cycle block, no \(4\)-cycle can use edges from two blocks. Therefore every \(C_4\) is rainbow and the construction is a \(B\)-coloring with exactly the claimed upper bound. Together with the lower bounds, this proves the formula.

## Verification
The accompanying standard-library program `verify.py` independently forms the \(B\)-conflict graph whose vertices are edges of \(G\), joining two edges when they are incident or opposite on a \(4\)-cycle. Thus \(q_B(G)\) is the chromatic number of this conflict graph. The program exhaustively enumerates every connected labeled cactus on \(2\) through \(6\) vertices, computes that chromatic number by an exact backtracking search, and compares it with the theorem.

The exhaustive census contains \(6074\) connected labeled cacti: \(1,4,31,362,5676\) at orders \(2,3,4,5,6\), respectively. Every case agrees with the formula. This finite computation is a stress test only; the proof above supplies the infinite statement.

## Relationship to prior work
Hu, Kong, and Wang define \(B\)-coloring through the equivalent conflict graph and prove the general degeneracy-codegree estimate \(q_B(G)\le\Delta(G)+(d-1)\Delta_2(G)\) for \(d\)-degenerate graphs. For cacti this gives only a general upper bound of the form \(\Delta+2\), not the exact formula here.

Kong, Wang, and Zheng prove \(q_B(G)=\Delta(G)\) for outerplanar graphs once \(\Delta(G)\ge7\). Since every cactus is outerplanar, that theorem already covers the high-degree slice of the present statement. The new content is the complete cactus classification in all degrees and the sharp reduction of the degree-optimal threshold from seven to four inside this natural subclass. Gyárfás, Martin, Ruszinkó, and Sárközy give the earlier \(\Delta+1\) outerplanar bound (with explicit small exceptions), while Jiang gives broad \(K_{{2,t}}\)-free and degeneracy bounds; neither inspected statement gives the cactus formula.

The older paper of Khan, Pal, and Pal studies ordinary edge-coloring of cactus graphs, not the additional rainbow-
\(C_4\) constraint. The recent subcubic preprint of Xue, Hu, and Kong gives a global upper bound and characterizes equality at six colors; only its publicly available abstract was accessible during comparison, so an unobserved more detailed low-color classification remains a residual literature risk.

## Limitations
The theorem is specific to cactus graphs. It does not assert an exact formula for general outerplanar graphs, where distinct cycle blocks can interact through chords inside a \(2\)-connected block. The computational check is exhaustive only through six vertices and is not used as a proof of the infinite result. The subcubic comparison noted above was limited to its abstract rather than the full manuscript.

## References
1. X. Hu, J. Kong, and Y. Wang, “Degeneracy bounds, stability, and a sharp gap for \(B\)-colorings,” arXiv:2609.02845v1, 2 September 2026.
2. Z. Jiang, “\(B\)-coloring of \(K_{{2,t}}\)-free planar graphs,” arXiv:2609.12519v1, 11 September 2026.
3. J. Kong, Y. Wang, and M. Zheng, “\(B\)-Coloring of Planar Graphs,” Journal of Graph Theory 113 (2026), 274–285, DOI 10.1002/jgt.70067.
4. A. Gyárfás, R. R. Martin, M. Ruszinkó, and G. N. Sárközy, “Proper edge colorings of planar graphs with rainbow \(C_4\)-s,” arXiv:2408.09059; Journal of Graph Theory 107 (2024), 833–846.
5. Y. Xue, X. Hu, and J. Kong, “Proper edge coloring of subcubic graphs with rainbow \(C_4\)-s,” SSRN 6528922 (2026), abstract inspected.
6. N. Khan, A. Pal, and M. Pal, “Edge Colouring of Cactus Graphs,” Advanced Modeling and Optimization 11(4) (2009), 407–421.
