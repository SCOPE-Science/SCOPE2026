# Exact strong-odd chromatic polynomial and cubic threshold zero of sunlet graphs

## Finding
For each integer \(n\geq3\), let \(S_n=C_n\circ K_1\) denote the sunlet graph: a labeled cycle of length \(n\), with one private pendant leaf at each cycle vertex (here \(\circ\) denotes corona, not lexicographic product). Let \(P_n(k)\) be the number of strong-odd proper vertex colorings of \(S_n\) from the labeled palette \([k]\), where unused colors are permitted. A coloring is strong odd when each color occurring among the neighbors of any vertex occurs an odd number of times there.

Define the integer polynomials
\[
q=k-3,\qquad r=4-k,\qquad L=1+(k-3)(k-2),
\]
and define \(U_0=2\), \(U_1=-q\), and
\[
U_j=-qU_{j-1}+rL U_{j-2}\qquad(j\geq2).
\]
Then for all \(n\geq3\) and all nonnegative integers \(k\), the following *polynomial identity* holds:
\[
\boxed{P_n(k)=L^n+(k-1)U_n+\frac{k(k-3)}2r^n+\frac{(k-1)(k-2)}2(-r)^n.}
\]
In particular, as a sequence indexed by \(n\), these polynomials obey the constant-order recurrence whose shift-operator polynomial is
\[
\boxed{(X-L)(X^2+qX-rL)(X^2-r^2).}
\]
This is an annihilating recurrence (possibly of lower minimal order at individual values of \(k\)).

The strong-odd chromatic number, and the exact counts of optimal labeled-palette colorings, have a sharp parity transition:
\[
\boxed{\chi_{\mathrm{so}}(S_n)=\begin{cases}2&n\text{ even},\\4&n\text{ odd};\end{cases}}
\]
there are exactly two optimal colorings when \(n\) is even, while for odd \(n\) the number of optimal \(4\)-colorings is \(3^n-3\).

For every odd \(n\geq3\), the chromatic polynomial has a **zero of precisely order three** at \(k=3\), with exact leading term
\[
\boxed{\left.\frac{P_n(k)}{(k-3)^3}\right|_{k=3}=\frac{n(n^2-1)}4.}
\]
For even \(n\), by contrast, \(P_n(3)=6\).

## Assumptions and scope
All graphs are finite, simple, undirected, and vertex labeled for enumeration. Vertices of the base cycle are \(v_i\) for \(i\in\mathbb Z/n\mathbb Z\), and their pendant leaves are \(w_i\). The graph has \(2n\) vertices and edges \(v_iv_{i+1}\) and \(v_iw_i\). A \(k\)-coloring is a map from all vertices into \([k]\), not necessarily surjective; when \(k=0\), there are no colorings. The polynomial \(P_n\) is understood over \(\mathbb Q[k]\), and its displayed expression takes integer values at nonnegative integers. All vertex-color labels are distinguished, whereas cycle rotations are not identified. The structural statements require \(n\ge3\); no assertion is made for other corona operations.

## Proof
**1. The local leaf rule.** Fix a proper coloring of the base cycle, with \(c_i\) the color at \(v_i\). The three neighbors of \(v_i\) are \(v_{i-1},v_{i+1},w_i\). A multiset of three colors satisfies the strong-odd condition precisely when its entries are all equal or pairwise distinct. Because both cyclic neighbors have colors different from \(c_i\), there is exactly one allowed choice for the color of \(w_i\) if \(c_{i-1}=c_{i+1}\), namely that common neighbor color. If \(c_{i-1}\ne c_{i+1}\), the leaf must avoid those two distinct colors and \(c_i\), giving exactly \(k-3\) choices. The pendant vertex itself has only one neighbor, so its strong-odd condition is automatic. The leaf choices are independent across positions. Thus
\[
P_n(k)=\sum_{\substack{c_0,\ldots,c_{n-1}\in[k]\\c_i\ne c_{i+1}\ \text{for all }i}}
(k-3)^{d(c)},\quad
 d(c)=|\{i:c_{i-1}\ne c_{i+1}\}|.
\]
Here cyclic subscripts are understood. This formula holds for all integers \(k\ge3\); for \(k=1,2\), the same count is given by the direct leaf rule whenever the term is nonzero.

**2. A weighted closed-arc transfer.** For integer \(k\ge3\), index a matrix \(T\) by directed arcs \((a,b)\) with \(a\ne b\) of the loopless complete graph on \([k]\). From \((a,b)\) to \((b,c)\), where \(c\ne b\), assign transition weight \(1\) if \(c=a\), and weight \(q=k-3\) otherwise; all other transitions have weight zero. The closed walks of length \(n\) are in bijection with proper cyclic sequences \((c_i)\); each transition contributes the local leaf multiplicity. Consequently
\[
P_n(k)=\operatorname{tr}(T^n).
\]
For a function \(f\) on arcs, let \(s_b=\sum_{c\ne b}f(b,c)\), and put \(r=1-q=4-k\). The matrix acts by
\[
(Tf)(a,b)=q s_b+r f(b,a).
\]

**3. Exhaustive invariant-space calculation.** Decompose the \(k(k-1)\)-dimensional arc space (over characteristic zero) into three invariant summands for \(k\ge3\).

The constant functions form a one-dimensional summand with eigenvalue \(L=q(k-2)+1\). The functions \(f(a,b)=\alpha x_a+\beta x_b\), for zero-sum vectors \(x\in\mathbb Q^k\), form a \(2(k-1)\)-dimensional summand. On the coefficient pair \((\alpha,\beta)\), the action is the \(2\)-by-\(2\) matrix
\[
\begin{pmatrix}0&r\\L&-q\end{pmatrix},
\]
whose characteristic polynomial is \(X^2+qX-rL\). The trace of its \(n\)-th power is \(U_n\), as shown directly by Cayley–Hamilton and initial traces \(U_0=2\), \(U_1=-q\).

On the remaining functions, whose outgoing and incoming sums at every color vanish, the first term \(q s_b\) is zero and \(T=rJ\), with \(Jf(a,b)=f(b,a)\). The symmetric zero-row-sum arc functions have dimension \(k(k-3)/2\); the antisymmetric zero-row-sum functions have dimension \((k-1)(k-2)/2\). These dimensions follow by counting unordered pairs with the \(k\) independent row equations in the symmetric case, and by the rank \(k-1\) of the signed incidence matrix of \(K_k\) in the antisymmetric case. The corresponding eigenvalues are \(r\) and \(-r\). Their dimensions, together with \(1+2(k-1)\), sum to \(k(k-1)\), proving exhaustion. Summing the traces yields the boxed formula for every \(k\ge3\).

For fixed \(n\), the displayed expression is a polynomial in \(k\). The right side of the leaf enumeration is also a polynomial in \(k\): for any prescribed equality/inequality pattern among the \(n\) cycle vertices, its realization count is a chromatic polynomial of a quotient graph (or zero, if constraints conflict). Since the two polynomials agree at all integers \(k\ge3\), they agree identically and therefore at \(k=0,1,2\) as well. The five spectral factors establish the asserted recurrence.

**4. Chromatic threshold and odd cubic zero.** If \(n\) is even, the alternating proper two-coloring of the base cycle extends uniquely to the leaves, with precisely two possible labeled assignments, so \(\chi_{\mathrm{so}}(S_n)=2\). For odd \(n\), consider the graph on the \(n\) cycle positions with edges \(\{i-1,i+1\}\). Because \(n\) is odd, this distance-two graph is itself a single cycle. Outside the \(d(c)\) defect sites, the corresponding edges impose equal colors. Removing at most two edges from a cycle leaves at most two connected components, so a proper coloring with at most two defects would use at most two colors on the original odd cycle, an impossibility. Hence every proper coloring has at least three defects, and \(P_n(k)\) has a factor \((k-3)^3\) for odd \(n\).

To calculate the leading coefficient, fix the palette \([3]\) and identify its colors with \(\mathbb Z/3\mathbb Z\). For a proper cyclic coloring, let \(\epsilon_i=c_{i+1}-c_i\in\{+1,-1\}\). A defect occurs exactly when \(\epsilon_{i-1}=\epsilon_i\). If exactly three defects occur, write \(g_1,g_2,g_3\) for their positive cyclic spacings, summing to odd \(n\). Between successive defects the step signs alternate; a spacing of even length contributes zero to \(\sum_i\epsilon_i\), while an odd spacing contributes one sign. Cyclic closure \(\sum_i\epsilon_i\equiv0\pmod3\) holds exactly when all three spacings are odd. For each such unordered triple of defect sites there are exactly two choices of initial step sign and three choices of initial color, giving six colorings. Writing \(g_j=2a_j+1\), their nonnegative parameters sum to \((n-3)/2\), hence the number of cyclic triples of defect sites is
\[
\frac n3\binom{(n+1)/2}{2}=\frac{n(n^2-1)}{24}.
\]
Therefore there are \(n(n^2-1)/4\) three-color cycle colorings with exactly three defects. The counts of center colorings with exactly \(d\) defects are polynomials in \(k\) by the quotient-graph argument; evaluating the coefficient of \((k-3)^3\) at \(k=3\) proves the exact cubic-zero leading coefficient.

Finally, the transfer formula at \(k=3\) gives \(P_n(3)=3+3(-1)^n\), and at \(k=4\) gives \(P_n(4)=3^n+3(-1)^n\). For odd \(n\), the former vanishes and the latter is positive, proving the optimal value four and its exact multiplicity \(3^n-3\). In all cases an optimal coloring necessarily uses each color of its minimal palette, because otherwise fewer colors would suffice.

## Verification
The included `verify.py` checks the definition directly on every vertex assignment for cycle orders \(3\le n\le5\) and palettes \(1\le k\le4\) (1,185,894 assignments). Separately, it constructs the weighted directed-arc transfer and checks the formula for \(3\le n\le30\), \(1\le k\le8\) (224 comparisons), checks the exact three-defect coefficient for odd orders through \(13\), and tests both parity threshold identities through order \(64\). Run `python3 verify.py` using Python's standard library. These tests check finite instances; the invariant-space decomposition and parity argument establish the unrestricted result.

## Relationship to prior work
Kwon and Park introduced the strong-odd coloring notion and established sparse-graph bounds (first public version, 22 January 2024). Caro, Petruševski, Škrekovski, and Tuza subsequently established a four-color upper bound for connected unicyclic graphs other than the bare five-cycle, and determined strong-odd chromatic numbers of bare cycles (arXiv version, 3 October 2024). A sunlet is unicyclic but not a bare cycle; the present work does not claim the general four-color upper bound or the basic notion as new. Those scalar results do not enumerate sunlet colorings, supply an all-palette polynomial, the five-factor recurrence, or the exact cubic vanishing at three colors. No equivalent polynomial for sunlets was found in the sources and research records inspected; incomplete indexing remains a bibliographic risk.

## Limitations
This is a complete result for a cycle with exactly one private leaf at each cycle vertex, not for arbitrary trees attached to cycle vertices or arbitrary unicyclic graphs. It treats strong-odd proper colorings, not the weaker neighborhood-odd coloring notion. All finite computations are cross-checks, not substitutes for proof. The bibliographic comparison is necessarily limited to accessible sources and search coverage.

## References
1. H. Kwon and B. Park, *Strong odd coloring of sparse graphs*, arXiv:2401.11653, initially public 2024-01-22, https://arxiv.org/abs/2401.11653 ; accessible HTML v2 https://arxiv.org/html/2401.11653v2 .
2. Y. Caro, M. Petruševski, R. Škrekovski, and Z. Tuza, *On strong odd colorings of graphs*, arXiv:2410.02336v1, initially public 2024-10-03, https://arxiv.org/html/2410.02336v1 ; especially Section 2, Proposition 2.2, on unicyclic graphs.
