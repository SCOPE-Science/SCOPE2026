# Independent \([1,2]\)-dominating sets of generalized Petersen graphs: an exact polynomial and a missing order

## Finding
For each integer \(n\geq5\), let \(P(n,2)\) be the generalized Petersen graph with vertices \(u_i,v_i\) indexed modulo \(n\) and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\). An **independent \([1,2]\)-set** is an independent vertex set \(S\) such that every vertex outside \(S\) has one or two neighbors in \(S\). Let
\[
F_n(z)=\sum_{S\text{ an independent }[1,2]\text{-set of }P(n,2)}z^{|S|}.
\]
Then, as an identity of formal power series over \(\mathbb Z[z]\),
\[
\boxed{\sum_{n\geq5}F_n(z)t^n=
\frac{5z^4t^5+18z^4t^6+7z^5t^7}
 {1-z^4t^5-3z^4t^6-z^5t^7}
+\frac{6z^4t^6}{1-z^2t^3}.}
\]
In particular, \(P(n,2)\) has an independent \([1,2]\)-set if and only if \(n\neq8\). For each admissible order, the least size of such a set is
\[
\boxed{\left\lceil\frac{2n}{3}\right\rceil+
\begin{cases}1,&n\equiv4\pmod6,\\0,&\text{otherwise},\end{cases}}
\qquad(n\geq5,\ n\neq8).
\]
All graph vertices and all independent sets are *labeled*; the polynomial does not quotient by automorphisms.

## Assumptions and scope
Indices are in \(\mathbb Z/n\mathbb Z\); every outer edge, spoke, and inner step-two edge is included once, and \(n\ge5\) avoids small-order graph degeneracies. The neighborhood condition applies only to vertices outside \(S\). No minimum-size or cardinality restriction is assumed in the polynomial. The conclusion does not assert an analogous formula for other generalized Petersen parameters.

## Proof
**Local-state encoding.** Since each spoke joins \(u_i\) to \(v_i\), independence allows exactly three choices in column \(i\): \(0\) (neither selected), \(U\) (only \(u_i\) selected), or \(V\) (only \(v_i\) selected). Write \(a_i=1\) in state \(U\), \(b_i=1\) in state \(V\), and zero otherwise. For each index \(i\), the two neighborhood constraints, together with independence, are equivalent to
\[
\begin{aligned}
a_i=1&\implies a_{i-1}=a_{i+1}=0,\\
b_i=1&\implies b_{i-2}=b_{i+2}=0,\\
a_i=0&\implies 1\le a_{i-1}+a_{i+1}+b_i\le2,\\
b_i=0&\implies 1\le b_{i-2}+b_{i+2}+a_i\le2.
\end{aligned}
\]
These are necessary and sufficient because the neighborhoods of \(u_i\) and \(v_i\) are respectively \(\{u_{i-1},u_{i+1},v_i\}\) and \(\{v_{i-2},v_{i+2},u_i\}\).

**Finite exact transfer.** Use the \(3^4=81\) words of length four over \(\{0,U,V\}\) as states. There is an arc from \((x_0,x_1,x_2,x_3)\) to \((x_1,x_2,x_3,x_4)\) precisely when the four displayed conditions hold at the central column of the five-letter word \((x_0,\ldots,x_4)\). Weight this arc by \(z\) if \(x_4\ne0\), and by \(1\) otherwise. Write \(M(z)\) for the resulting \(81\times81\) weighted adjacency matrix. It has exactly \(89\) arcs. The cyclic trace gives
\[
F_n(z)=\operatorname{tr}(M(z)^n)\qquad(n\ge5).
\]
Indeed, a closed walk determines one cyclic indexed sequence of column symbols, and the arc test at every column enforces exactly the original graph conditions; its weight is \(z^{|S|}\). The converse reconstructs a unique closed walk by taking each four-symbol window.

**Exact determinant certificate.** The only strongly connected components containing cycles have orders \(17,3,3\). The larger component has six directed simple cycles, with (length, number of selected symbols) equal to
\[
(5,4),\ (6,4),\ (6,4),\ (6,4),\ (7,5),\ (12,8),
\]
and each smaller component has one simple cycle of type \((3,2)\). The only pair of vertex-disjoint simple cycles in the larger component consists of two length-six, weight-four cycles. The positive term for this pair cancels the negative contribution of the length-twelve, weight-eight cycle. The directed-cycle expansion of the determinant consequently yields the **exact polynomial identity**
\[
\det(I-tM(z))
=\bigl(1-z^4t^5-3z^4t^6-z^5t^7\bigr)
 \bigl(1-z^2t^3\bigr)^2.
\]
All cycle and disjointness assertions are certified by the exhaustive, self-contained enumeration in `verify.py`; it directly constructs the 81-state graph and enumerates *all* simple cycles in each cyclic strongly connected component. This is a finite exact calculation, not an extrapolation from small values of \(n\).

For a polynomial matrix with constant term identity, the standard formal identity
\[
-t\frac{\partial}{\partial t}\log\det(I-tM(z))
=\sum_{n\ge1}\operatorname{tr}(M(z)^n)t^n
\]
follows by differentiating the formal determinant (or using the formal trace-log expansion). Its terms below order five consist only of \(6z^2t^3\), arising from the two three-cycles. Remove that term and differentiate the displayed determinant. The resulting formula is exactly the boxed generating function for \(n\ge5\).

**Exceptional order and minimum cardinalities.** There is no \(t^8\) term, giving nonexistence at \(n=8\). The finite cyclic-component classification implies every positive-length closed walk decomposes into simple cycles whose lengths and cardinalities are from the list above. Every such cycle obeys \(3w-2\ell\ge0\); the excess is two for a five-cycle, one for a seven-cycle, and zero for the others. Hence \(|S|\ge\lceil2n/3\rceil\). For \(n\equiv4\pmod6\), an excess of one would require exactly one seven-cycle and some three-, six-, or twelve-cycles; all these other cycles have lengths divisible by three, and the only even ones of these are six and twelve. More precisely, to achieve the minimal excess one, the decomposition has one seven-cycle and any number of zero-excess cycles of lengths three, six or twelve. Modulo three, \(n\equiv1\), and to have \(n\equiv4\pmod6\), an odd number of three-cycles would be needed. But cycles from the two isolated three-vertex components cannot coexist in a closed walk with a seven-cycle from the seventeen-vertex component. Thus the only available zero-excess companion cycles have even length, and total length remains odd: contradiction. For these even orders the excess is at least four (the excess cannot be two or three because \(3|S|-2n\equiv1\pmod3\)), proving one more than the ceiling is required.

To prove all bounds are attained, the seventeen-vertex component contains length-five, length-six, and length-seven cycles sharing the four-symbol state \((0,U,V,V)\); their explicit words are `U0UVV`, `0U0UVV`, and `U0U0UVV`, respectively (checked in `verify.py`). Concatenation supplies length \(5+6r\), \(7+6r\), \(14+6r\), or \(10+6r\) with selected counts \(4+4r\), \(5+4r\), \(10+4r\), or \(8+4r\). These realize the claimed minima in all residue classes not divisible by three; repetitions of either three-cycle realize exactly \(2n/3\) when \(3\mid n\) and \(n\ge6\). The only excluded order is eight, completing the existence and minimum-size claims.

## Verification
The accompanying standard-library `verify.py` rebuilds the graph and its arcs; extracts its strongly connected components and all directed simple cycles; verifies the exact weighted determinant expansion; compares every polynomial coefficient to direct exhaustive vertex-subset enumeration for \(5\le n\le10\); compares matrix traces with the displayed rational generating function for \(5\le n\le30\); and checks the stated minimum-size formula for \(5\le n\le100\). Its expected final output begins `VERIFY_OK` and includes `brute_subsets=1397760`. The finite order checks corroborate the proof but do not, alone, establish its infinite conclusions.

## Relationship to prior work
Aleid, Cáceres, and Puertas studied independent \([1,2]\)-sets in trees and related sparse graph classes, providing the established definition and motivation; this work addresses a different highly structured cubic graph family. Beggas and coauthors studied (not necessarily independent) \([1,2]\)-domination in generalized Petersen graphs, including the same graph parameters, but their feasibility and minima do not impose independence and therefore do not imply the polynomial or the exceptional order here. Dod studied the independent domination polynomial, which counts all maximal independent sets, whether or not an outside vertex has at most two selected neighbors. An independent \([1,2]\)-set is maximal independent, but the converse generally fails; the resulting refined count cannot be extracted from the unrefined polynomial without additional incidence data. Likewise, a \((2-d)\)-kernel requires at least two neighbors outside the set, not one or two, and is a distinct condition. No independent priority or completeness certification is asserted.

## Limitations
The theorem is restricted to \(P(n,2)\) with \(n\ge5\), and to independent \([1,2]\)-domination. The finite transfer determinant is an exact reproducible calculation; an alternative human-hand enumeration of all cyclic components is not supplied. Literature comparisons do not establish absolute priority: an equivalent older encoding or enumeration under a different name remains possible. No independent mathematical audit has yet been conducted.

## References
1. S. Aleid, J. Cáceres, and M. L. Puertas, *On independent [1,2]-sets in trees* (2015), arXiv:1511.09262, first public 2015-11-30. https://arxiv.org/abs/1511.09262
2. M. Dod, *The Independent Domination Polynomial* (2016), arXiv:1602.08250, first public 2016-02-26. https://arxiv.org/abs/1602.08250
3. F. Beggas and coauthors, *[1,2]-Domination in Generalized Petersen Graphs* (2019), arXiv:1906.11966. https://arxiv.org/abs/1906.11966
4. P. Bednarz and N. Paja, *On (2-d)-Kernels in Two Generalizations of the Petersen Graph* (2021), Symmetry 13, 1948. https://doi.org/10.3390/sym13101948
