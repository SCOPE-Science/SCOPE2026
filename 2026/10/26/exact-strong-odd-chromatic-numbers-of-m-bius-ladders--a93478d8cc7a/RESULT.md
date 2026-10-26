# Exact strong odd chromatic numbers of Möbius ladders

## Finding
For every integer \(n\ge 3\), let \(M_{2n}\) be the cubic Möbius ladder with vertex set \(\mathbb Z/(2n)\), cycle edges \(\{i,i+1\}\), and antipodal edges \(\{i,i+n\}\), with indices modulo \(2n\). A **strong odd coloring** is a proper vertex coloring in which each color that occurs in the open neighborhood of any vertex occurs there an odd number of times. Then
\[
\chi_{\mathrm{so}}(M_{2n})=\begin{cases}
2,&n\text{ odd},\\
4,&n\equiv2\pmod4,\\
8,&n=4,\\
6,&n=8,\\
5,&n\equiv0\pmod4,\quad n\ge12.
\end{cases}
\]
Furthermore, **for every even \(n\ge4\)**, the strong odd vertex colorings of \(M_{2n}\) are exactly the proper colorings of its graph square \(M_{2n}^2\), with identical color classes. In particular the equality \(\chi_{\mathrm{so}}(M_{2n})=\chi(M_{2n}^2)\) holds throughout this even-index family.

## Assumptions and scope
All graphs are finite, simple and undirected; color names have no mathematical significance. The square of a graph joins two distinct vertices whenever their graph distance is at most two. Every open neighborhood in \(M_{2n}\) has exactly three vertices. Write each of the \(n\) rungs as a pair \((x_i,y_i)\), where \(0\le i<n\), with rung edge \(x_iy_i\), horizontal edges \(x_ix_{i+1}\), \(y_iy_{i+1}\) for \(0\le i<n-1\), and twisted closing edges \(x_{n-1}y_0\), \(y_{n-1}x_0\). This representation is isomorphic to the Cayley graph in the finding. The theorem concerns strong odd **vertex** colorings, not odd edge colorings, neighborhood-parity colorings without properness, or two-tone colorings.

## Proof
**1. Adjacent-rung exclusion when \(n\) is even.** Fix a color \(c\) in a strong odd coloring. An adjacent pair of rungs cannot both contain \(c\). If they did, properness forces the occurrences into opposite rows: after shifting the rung labels and possibly exchanging rows and reversing their order, suppose \(x_0\) and \(y_1\) receive \(c\). Extend the notation through the twisted seam by \(x_{i+n}=y_i\) and \(y_{i+n}=x_i\). The three neighbors of \(x_1\) are \(x_0,y_1,x_2\); exactly two already receive \(c\), so the parity condition forces \(x_2\) to receive \(c\). Similarly, \(y_2\) has neighbors \(y_1,x_2,y_3\), forcing \(y_3\) to receive \(c\). Repeating proves that \(x_{2j}\) and \(y_{2j+1}\) have color \(c\) for every admissible step. Because \(n\) is even, this eventually forces both \(x_0\) and \(x_n=y_0\) to receive \(c\), contradicting their rung edge. The same proof applies to an adjacent-rung pair crossing the seam by twisted cyclic symmetry. Thus the rung indices occupied by any color form an independent set of the ordinary cycle \(C_n\); in particular each rung contains at most one occurrence and each color class has size at most \(n/2\).

**2. Strong odd is equivalent to square coloring.** At any vertex \(v\), three neighbors share three colors, whose multiplicities are all odd. They are either all distinct or all of one color. The latter possibility would put one color on two adjacent rungs (indeed on the rung neighbor of \(v\) and on a row neighbor), which step 1 excludes. Hence all three neighbors of each vertex have pairwise different colors. Together with properness, this says precisely that every pair of vertices at graph distance at most two have different colors: the coloring is proper on \(M_{2n}^2\). Conversely a proper square coloring has three differently colored neighbors at each vertex, so it is strong odd.

**3. Lower bounds.** Since every color class of the square coloring occupies nonconsecutive rungs, step 1 gives \(\chi_{\mathrm{so}}\ge4\) for all even \(n\). If \(4\mid n\), no color class can occupy all \(n/2\) rungs of an alternating maximal independent set of \(C_n\). Indeed, any two vertices of the same color in rungs two steps apart must lie in opposite rows: otherwise they have the intervening row vertex as a common neighbor, contrary to the square-coloring property. Hence, along all the \(n/2\) selected alternating rungs, the chosen row switches at each step. Since \(n/2\) is even, the first and last selected rungs have opposite rows; however the twisted closing edges make these opposite-row choices at distance two, a contradiction. The alternative alternating independent set is symmetric. Thus every color class has size at most \(n/2-1\) when \(4\mid n\), and
\[
\chi_{\mathrm{so}}(M_{2n})\ge\left\lceil\frac{2n}{n/2-1}\right\rceil.
\]
This is \(8\) when \(n=4\), \(6\) when \(n=8\), and \(5\) for all multiples of four \(n\ge12\).

**4. Upper bounds and explicit colorings.** If \(n\) is odd, coloring each rim vertex \(i\in\mathbb Z/(2n)\) by its parity is proper because the antipodal edges change parity, and is strong odd because each neighborhood has three vertices of the other color. This proves \(2\), with properness excluding \(1\). If \(n\equiv2\pmod4\), color rim vertex \(i\) by \(i\bmod4\). Graph-square distances are represented by offsets \(\pm1,\pm2,n,n\pm1\) modulo \(2n\); none is \(0\pmod4\) under this congruence assumption. This is a four-color square coloring.

For \(n=4\), use eight distinct colors. For \(n=8\), the successive ordered rung colors \((\operatorname{col}(x_i),\operatorname{col}(y_i))\), with colors numbered \(0\) through \(5\), are
\[
(0,2),(3,1),(4,0),(1,3),(2,4),(3,0),(4,2),(5,1).
\]
For every \(n\equiv0\pmod4\), \(n\ge12\), use the first \(n-7\) pairs of the indefinitely repeated four-block
\[
B=((0,1),(2,3),(1,0),(3,2))
\]
followed by the seven-pair tail
\[
T=((2,4),(1,0),(4,3),(0,2),(3,4),(2,1),(4,3)).
\]
Each is a coloring with respectively six or five color names. To check the square constraints, write \((a_i,b_i)\) for each rung pair. It suffices to check: \(a_i\ne b_i\) in each rung; all four entries of any two adjacent rung pairs are pairwise different (with row interchange when crossing the twisted seam); and both rows on rungs two steps apart have different colors, with the appropriate row interchange at the twisted seam. These checks are immediate for the displayed eight-rung word, the repeated four-block, and the seven-tail joining it: the repeated prefix has length \(n-7\equiv1\pmod4\), so the same finite junction checks handle all \(n\ge12\). Consequently the constructions properly color the square, hence are strong odd by step 2. Combining upper and lower bounds proves all assertions.

## Verification
The companion standard-library program `verify.py` directly checks properness, strong-odd neighbor parity, and (for even \(n\)) graph-square properness for every constructed coloring \(3\le n\le300\). It independently enumerates all strong odd independent color classes for \(n=4,6,8,12\), obtaining respectively \(8,40,128,1496\) eligible nonempty classes and maximum class sizes \(1,3,3,5\). These finite checks corroborate the construction and sharpened upper-size bound at representative orders. The theorem for unbounded \(n\) rests on the displayed propagation, parity obstruction, and fixed-block gluing arguments, not on finite extrapolation. Run `python3 verify.py`; the expected last line is `VERIFY_OK`.

## Relationship to prior work
Kwon and Park introduced and studied strong odd coloring of sparse graphs [1], while Caro, Petruševski, Škrekovski and Tuza developed general bounds and graph-product comparisons [2]. Neither of their inspected statements supplies the five-case exact evaluation for a Möbius ladder or the rigidity that every strong odd coloring of this graph, for even \(n\), is a square coloring. The standard circulant identity for its square [3] identifies an equivalent square-coloring formulation, but not the five-case evaluation or the parity-propagation proof. Results for the untwisted two-row ladder concern a different closure: the Möbius seam is exactly what creates the exceptional \(n=4\) and \(n=8\) behavior and the alternating-row obstruction. Two-tone and strong edge-coloring problems on Möbius ladders use different coloring constraints and do not directly imply this theorem.

## Limitations
This is a theorem only for the explicitly defined cubic Möbius ladder family and the specified open-neighborhood definition of strong odd coloring. It does not classify every optimal coloring or assert analogous formulas for general circulants, graph products, or prisms. Related literature on graph-square coloring and circulant colorings may contain previously unnoticed equivalent or stronger results; absence from searched sources does not prove priority. The finite verification is supplementary rather than a substitute for the proof.

## References
[1] H. Kwon and B. Park, *Strong odd coloring of sparse graphs*, arXiv:2401.11653, first publicly posted 2024-01-22, https://arxiv.org/abs/2401.11653.

[2] Y. Caro, M. Petruševski, R. Škrekovski, and Z. Tuza, *On strong odd colorings of graphs*, arXiv:2410.02336, first publicly posted 2024-10-03, https://arxiv.org/abs/2410.02336.

[3] *Möbius Ladder*, Wolfram MathWorld, https://mathworld.wolfram.com/MoebiusLadder.html (graph-square circulant identity).
