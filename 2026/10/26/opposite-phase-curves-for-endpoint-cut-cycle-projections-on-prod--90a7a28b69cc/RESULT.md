# Opposite phase curves for endpoint cut–cycle projections on products of two stars

## Finding
For every pair of integers \(m,n\ge2\), put \(S_m=K_{1,m}\) and \(G_{m,n}=S_m\mathbin{\square}S_n\), with every edge given unit conductance. Let \(D\) be any signed vertex–edge incidence matrix, and define the real Euclidean-orthogonal projections on the edge-coordinate space by
\[
Q=D^{\mathsf T}(DD^{\mathsf T})^+D,\qquad P=I-Q.
\]
Here \(Q\) projects onto the cut space and \(P\) onto the cycle space. Define
\[
A(m,n)=\frac{5mn+2m+3n^2+4n+4}{(n+2)(m+n+2)},\qquad
U(m,n)=\frac{2n(3m+2n+1)}{(n+2)(m+n+2)}.
\]
Then both the real \(\ell_1\) and \(\ell_\infty\) induced norms are exactly
\[
\boxed{\|Q\|=\max\{A(m,n),A(n,m)\},\qquad
\|P\|=\max\{U(m,n),U(n,m)\}.}
\]
The maximizing column for each projection lies on one of the two kinds of *hub-layer edges*: an edge of \(S_m\) above the center of \(S_n\), or an edge of \(S_n\) above the center of \(S_m\). No leaf-layer edge maximizes either norm.

The difference between these candidate columns is governed by **two different exact phase curves**. With \(\Delta=(m+2)(n+2)(m+n+2)\),
\[
A(m,n)-A(n,m)=\frac{2(m-n)(mn-2m-2n)}{\Delta},
\]
\[
U(m,n)-U(n,m)=\frac{2(m-n)(mn-4m-4n-2)}{\Delta}.
\]
Thus the first-direction hub-layer edges maximize the cut norm exactly when \((m-n)(mn-2m-2n)\ge0\), and maximize the cycle norm exactly when \((m-n)(mn-4m-4n-2)\ge0\). Reverse strict inequalities favor the second-direction hub-layer edges; equality yields both types. For every integer \(n\ge7\), the graph \(G_{3,n}\) has **opposite maximizing directions** for \(Q\) and \(P\). For example, at \((m,n)=(3,10)\), the cut maximum is \(71/25\) on the second-direction hub-layer edges, while the cycle maximum is \(10/3\) on the first-direction hub-layer edges.

The two sharp global suprema over all integer \(m,n\ge2\) are
\[
\boxed{\sup_{m,n\ge2}\|Q\|=5,\qquad\sup_{m,n\ge2}\|P\|=6.}
\]
Neither is attained at finite parameters. Both are approached by \(m=r\), \(n=r^2\), as \(r\to\infty\). Along the balanced diagonal \(m=n=r\to\infty\), the respective limits are instead \(4\) and \(5\).

## Assumptions and scope
The graph is the **Cartesian**, not categorical, product: two vertices \((a,b)\), \((a',b')\) are adjacent when exactly one coordinate changes along an edge of its star and the other coordinate is unchanged. The first star has one center and \(m\) leaves, the second one center and \(n\) leaves, and \(m,n\ge2\). There are \((m+1)(n+1)\) vertices and \(2mn+m+n\) unoriented edges. All edge-space and operator norms are over the reals. The Moore–Penrose inverse in the definition of \(Q\) is the standard Laplacian pseudoinverse; the graph is connected, so the defining current is unique.

There are four edge orbits. Call an edge \(A_0\) if its first coordinate moves and its second coordinate is the second-star center, \(A_1\) if its first coordinate moves and its second coordinate is a leaf, and define \(B_0,B_1\) analogously by interchanging the factors. Each orbit is nonempty. An edge orientation changes column signs but not absolute column sums.

## Proof
Let \(e=uv\) be an oriented edge and solve \(L\phi=\mathbf1_v-\mathbf1_u\), with \(L=DD^{\mathsf T}\). The column \(Q\mathbf1_e\) consists of the oriented potential differences \(\phi(b)-\phi(a)\) on all edges \(ab\). Therefore its absolute column sum is the total absolute current. The corresponding column of \(P=I-Q\) has absolute sum
\[
\|Q\mathbf1_e\|_1+1-2R_e,
\]
where \(R_e=\phi(v)-\phi(u)=\langle Q\mathbf1_e,\mathbf1_e\rangle\) is the effective resistance of \(e\). Indeed \(0<R_e\le1\), so the diagonal term of \(I-Q\) has nonnegative sign. Because \(Q\) and \(P\) are symmetric, their maximum absolute column sums are also their maximum absolute row sums.

Fix an \(A_0\) edge whose first-coordinate endpoints are the center \(H\) and a marked leaf \(L_*\). The source is \((L_*,H)\), the sink \((H,H)\), and the potential at \((H,H)\) is normalized to zero. Every other leaf of the first star has a common value, as does every leaf of the second star. In the following table every displayed entry is the potential **multiplied by** \(\delta_0=(n+2)(m+n+2)\):

| First-coordinate class | Second center \(H\) | Second generic leaf |
| --- | ---: | ---: |
| \(H\) | \(0\) | \(n+2\) |
| \(L_*\) | \(2m+3n+4\) | \(m+2n+3\) |
| Other leaf | \(n\) | \(n+1\) |

Substituting these six values in the Laplacian equations, with center-to-leaf neighbor multiplicities \(1,m-1\) and \(n\), verifies \(L\phi=\mathbf1_{(L_*,H)}-\mathbf1_{(H,H)}\). For instance, at the source the numerator of the Laplacian is \((n+1)(2m+3n+4)-n(m+2n+3)=\delta_0\). The other equations are the same elementary substitutions. Differences along the seven distinct orbit-edge types have constant signs for every positive \(m,n\), yielding
\[
\|Q\mathbf1_{A_0}\|_1=A(m,n),\qquad
R_{A_0}=\frac{2m+3n+4}{(n+2)(m+n+2)},\qquad
\|P\mathbf1_{A_0}\|_1=U(m,n).
\]
The \(B_0\) formulas are obtained by interchanging \(m\) and \(n\).

For an \(A_1\) edge, mark one leaf in **each** star, take source \((L_*,L_*)\), sink \((H,L_*)\), and normalize at \((H,H)\). The symmetry orbits now form a \(3\)-by-\(3\) table, with the classes \(H\), \(L_*\), and other leaves in each factor. Put \(\delta_1=2(m+2)(n+2)(m+n+2)\). The entries below are the potentials multiplied by \(\delta_1\):

| First-coordinate class | Second \(H\) | Second \(L_*\) | Second other leaf |
| --- | ---: | ---: | ---: |
| \(H\) | \(0\) | \(-2(n+2)(m+n+1)\) | \(2(n+2)\) |
| \(L_*\) | \(2(m+2)(m+n+1)\) | \(m^2n+3m^2+mn^2+6mn+9m+n^2+7n+8\) | \(m^2+mn+3m+3n+4\) |
| Other leaf | \(-2(m+2)\) | \(-(mn+3m+n^2+3n+4)\) | \(-(m-n)\) |

At an \(H\) coordinate, its neighbors are the one marked leaf and every unmarked leaf, with multiplicities \(1\) and one less than the leaf count. Each leaf has only its center as a neighbor. These rules show by direct substitution in all nine cells that the table solves the dipole Laplacian equation. No unlisted vertices or edges occur. Taking every center–leaf difference, with the multiplicity equal to the product of the sizes of the fixed-coordinate classes and the changing-leaf class, gives these exact sums. Write \(\Delta=(m+2)(n+2)(m+n+2)\):
\[
W(m,n)=\frac{4m^2n+4mn^2+3m^2+3n^2+14mn+7m+7n+12}{\Delta},
\]
\[
Z(m,n)=\frac{2(2m^2n+2mn^2+m^2+n^2+6mn+m+n+4)}{\Delta}.
\]
Then
\[
\|Q\mathbf1_{A_1}\|_1=\|Q\mathbf1_{B_1}\|_1=W(m,n),\qquad
\|P\mathbf1_{A_1}\|_1=\|P\mathbf1_{B_1}\|_1=Z(m,n).
\]
To recover the complementary formula independently, the same table gives
\[
R_{A_1}=R_{B_1}=\frac{m^2n+mn^2+3m^2+3n^2+8mn+13m+13n+12}{2\Delta},
\]
and \(Z=W+1-2R_{A_1}\). All absolute signs follow directly from the potential differences; each is a positive polynomial times \(+1\) or \(-1\), with denominators positive for \(m,n\ge2\). Specifically, in the \(A_0\) table the signed currents along first-direction edges from the center to a marked/unmarked leaf are respectively \((+,+)\) above the second center and \((+,-)\) above any second leaf; the second-direction center-to-leaf current signs at a first center, marked leaf, and other leaf are \((+,-,+)\). In the \(A_1\) table the corresponding first-direction sign pairs are \((+,-)\), \((+,+)\), \((+,-)\) above second-center, marked-leaf, and unmarked-leaf positions, while the second-direction signs for marked/unmarked changing leaves are \((-,+)\) at first center, \((+,-)\) at first marked leaf, and \((-,+)\) at any other first leaf. For example, the unmarked-first-leaf/unmarked-second-leaf first-direction current is \(-(m+n+4)/(2\Delta)\); the corresponding second-direction current is its negative. Thus no case split is hidden in the formulas.

It remains to show that no leaf-layer column can maximize. Direct subtraction yields
\[
A(m,n)-W(m,n)=\frac{(n-1)(m^2-mn-m+3n+4)}{\Delta},
\]
\[
A(n,m)-W(m,n)=\frac{(m-1)(n^2-mn-n+3m+4)}{\Delta}.
\]
The two bracketed expressions sum to \((m-n)^2+2(m+n)+8>0\), so at least one of the first two hub-layer cut columns is **strictly** larger than either leaf-layer cut column. For cycle columns the inequalities are both strict:
\[
U(m,n)-Z(m,n)=\frac{2(n-1)(m^2+m+3n+4)}{\Delta}>0,
\]
\[
U(n,m)-Z(m,n)=\frac{2(m-1)(n^2+n+3m+4)}{\Delta}>0.
\]
The displayed phase-curve identities are polynomial simplifications of the two hub-layer differences. This proves the norm and maximizing-orbit assertions for all integer \(m,n\ge2\).

Finally, \(5-A(m,n)=(8m+2n^2+16n+16)/((n+2)(m+n+2))>0\) and \(6-U(m,n)=(12m+2n^2+22n+24)/((n+2)(m+n+2))>0\), and their swapped versions are positive. Along \(m=r\), \(n=r^2\), the dominant \(A(n,m)\) and \(U(n,m)\) tend respectively to \(5\) and \(6\). Along \(m=n=r\to\infty\), substitution gives the claimed limits \(4\) and \(5\). The strict opposite-direction example follows by comparing the signs of the phase curves when \(m=3\), \(n\ge7\).

## Verification
The included self-contained standard-library script `verify_star_product.py` uses exact `fractions.Fraction` arithmetic. It reconstructs the six- and nine-cell grounded Laplacians and their total current norms for all \(225\) ordered pairs \(2\le m,n\le16\) (\(900\) edge-orbit checks). Separately, it constructs eight entire Cartesian-product graphs and computes \(32\) representative edge columns using full grounded Laplacian elimination, without using the orbit formulas to calculate the currents. All comparisons to the formulas are exact. Reproduce using `python3 verify_star_product.py`. These finite tests confirm instances and the software's algebraic implementation; the unbounded-parameter result is proved by the symbolic potential tables and inequalities above.

## Relationship to prior work
Dilworth, Kutzarova and Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost* (first public arXiv version 21 May 2023, arXiv:2305.12582v1), develops the cycle/cut Banach-space framework and obtains exact endpoint norms for the full Hamming cube; its Sections 2.6–2.7 concern Hamming graphs and do not state a two-star Cartesian-product formula. A star is not a complete graph when it has at least two leaves, and the graph here has four distinct edge orbits and different hub-layer optimizers for the two complementary projections. Thus the Hamming theorem does not yield the displayed rational formulas by replacing an alphabet size. This work concerns the *canonical orthogonal* projections, not minimal norms over all nonorthogonal projections.

## Limitations
The result is restricted to two factors that are unweighted stars with at least two leaves each, and to real \(\ell_1\) and \(\ell_\infty\) endpoint norms of canonical Euclidean-orthogonal edge projections. It does not determine general weighted products, intermediate \(\ell_p\) operator norms, or the least norm among arbitrary nonorthogonal projections. The literature comparison does not exclude an equivalent computation in less-indexed electrical-network sources.

## References
Dilworth, S. J., Kutzarova, D., and Ostrovskii, M. I., *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582v1, publicly posted 21 May 2023, especially Sections 1.1 and 2.6–2.7; published version in *Proceedings of Symposia in Pure Mathematics*, vol. 106 (2024), DOI:10.1090/PSPUM/106/01929.
