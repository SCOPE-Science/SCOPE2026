# The locally identifying coloring polynomial of two cliques joined by a partial matching

## Finding

Fix integers \(n\ge 2\) and \(0\le t\le n\). Let \(H_{n,t}\) have two disjoint labeled cliques \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), together with the \(t\) cross-edges \(a_ib_i\), \(1\le i\le t\), and no other cross-edges. Let \(L_{n,t}(k)\) count proper locally identifying vertex colorings \(f:V(H_{n,t})\to[k]\), where adjacent vertices with unequal closed neighborhoods must see different *sets* of colors in their respective closed neighborhoods. Colors need not all be used. Set \((x)_j=x(x-1)\cdots(x-j+1)\), with \((x)_0=1\).

For every integer \(k\ge0\), the exact enumerator is
\[
L_{n,t}(k)=
\begin{cases}
(k)_n^2,&t=0,\\[2mm]
(k)_n\displaystyle\sum_{r=0}^{n-2}\binom{n-1}{r}^2r!\,(k-n)_{n-r},&t=1,\\[3mm]
(k)_n\displaystyle\sum_{r=0}^{n-t}\binom{n-t}{r}^2r!\,(k-n)_{n-r},&2\le t<n,\\[3mm]
(k)_{2n}+n(n-1)(k)_{2n-1},&t=n.
\end{cases}
\]
All terms are integer-valued at nonnegative \(k\); for \(k<n\), the count is zero by the clique obstruction (evaluate the polynomial by its identity on sufficiently large integers).

More precisely, a proper coloring is locally identifying exactly under these mutually exclusive conditions:

* \(t=0\): any proper coloring works.
* \(1\le t<n\): every color shared by the two clique palettes occurs only at unmatched vertices \(a_i,b_j\) with \(i,j>t\); and, if \(t=1\), at most \(n-2\) colors may be shared.
* \(t=n\): the two clique palettes share at most one color; if one is shared, its two occurrences must lie at different indices, as already required by properness.

Consequently the minimum number of colors is
\[
\chi_{\mathrm{lid}}(H_{n,t})=\begin{cases}
n,&t=0,\\
n+2,&t=1,\\
n+t,&2\le t<n,\\
2n-1,&t=n.
\end{cases}
\]
At this minimum, the number of color partitions of the labeled vertex set, counting two assignments equivalent when they differ only by a bijection of color names, equals
\[
U_{n,t}=\begin{cases}
n!,&t=0,\\
(n-1)^2(n-2)!,&t=1,\\
(n-t)!,&2\le t<n,\\
n(n-1),&t=n.
\end{cases}
\]
For a fixed palette consisting of exactly \(\chi_{\mathrm{lid}}(H_{n,t})\) named colors, the number of optimal colorings is \(U_{n,t}\chi_{\mathrm{lid}}(H_{n,t})!\).

The edge-addition profile has two plateaus when \(n\ge3\): the first two cross-edges both require \(n+2\) colors, and the last edge does not increase the requirement of \(2n-1\). The order-two exception is sharper: \(\chi_{\mathrm{lid}}(H_{2,1})=4\) but \(\chi_{\mathrm{lid}}(H_{2,2})=3\), so adding an edge decreases the parameter.

## Assumptions and scope

All graphs are finite, simple, and labeled. The integers are \(n\ge2\) and \(0\le t\le n\); the partial cross-matching may be any matching of size \(t\), since relabeling makes it the first \(t\) indices. A proper coloring assigns different colors to adjacent vertices. It is locally identifying (lid) if \(f(N[u])\ne f(N[v])\) whenever \(uv\) is an edge and \(N[u]\ne N[v]\), where \(N[u]\) denotes the closed vertex neighborhood and \(f(S)\) means the set (not multiset) of colors present on \(S\). The fully matched endpoint \(H_{n,n}\) is \(K_n\square K_2\), and \(H_{n,0}\) is disconnected. No claim is made about arbitrary cross-edge sets that are not matchings.

## Proof

Write \(P=\{f(a_i):i\in[n]\}\) and \(Q=\{f(b_i):i\in[n]\}\). Properness forces \(|P|=|Q|=n\) and, for \(i\le t\), \(f(a_i)\ne f(b_i)\). For each matched index \(i\le t\), the closed-neighborhood color sets are
\[
f(N[a_i])=P\cup\{f(b_i)\},\qquad f(N[b_i])=Q\cup\{f(a_i)\}.
\]
For unmatched \(i>t\), they are respectively \(P\) and \(Q\). Two distinct unmatched vertices within one clique have identical *vertex* closed neighborhoods, hence do not require separation. Every other pair in a clique has unequal closed neighborhoods when \(t>0\).

First suppose \(1\le t<n\). Comparing each matched \(a_i\) with an unmatched \(a_j\) forces \(f(b_i)\notin P\). Symmetrically, \(f(a_i)\notin Q\). These conditions are equivalent to saying that every shared color appears only among the \(n-t\) unmatched positions in each clique. Under this condition the closed-neighborhood color sets for distinct matched vertices in the same clique are pairwise different, since their additional colors are distinct and lie outside that clique's palette; each is also different from the constant set for unmatched vertices. Thus all same-clique edges satisfy local identification.

For a matched cross-edge \(a_ib_i\), the two color sets are \(P\cup\{f(b_i)\}\) and \(Q\cup\{f(a_i)\}\). Here \(f(a_i)\in P\setminus Q\) and \(f(b_i)\in Q\setminus P\). Equality holds if and only if \(P\setminus Q=\{f(a_i)\}\) and \(Q\setminus P=\{f(b_i)\}\), equivalently \(|P\cap Q|=n-1\). There are at most \(n-t\) shared colors. For \(t\ge2\) such equality is impossible; for \(t=1\), it occurs precisely when all \(n-1\) unmatched colors are shared, and must be excluded. This proves the characterization for partial nonempty matchings.

When \(t=n\), all vertices are matched. Since colors in each clique are distinct, the sets \(P\cup\{f(b_i)\}\) for different \(i\) are pairwise distinct exactly when at most one \(f(b_i)\) lies in \(P\). The analogous condition in the other clique is the same inequality \(|P\cap Q|\le1\). Properness prohibits a shared color at equal indices. With disjoint palettes, cross-edge neighborhoods cannot have equal color sets. With one shared color and \(n\ge3\), at least two colors of \(P\setminus Q\) are present in the first endpoint's set but at most one in the second, again forbidding equality. For \(n=2\), the two instances of the shared color lie at unequal indices, so on each matched cross-edge exactly one endpoint's closed-neighborhood color set uses two colors and the other uses three. Thus no cross-edge equality occurs, proving the last case. For \(t=0\), the two clique components have true-twin vertices and all proper colorings are lid.

To count, first order the \(n\) distinct colors of clique \(A\) in \((k)_n\) ways. For \(1\le t<n\), choose \(r\) unmatched positions in each clique, bijectively pair their shared colors in \(\binom{n-t}{r}^2r!\) ways, then injectively color the remaining \(n-r\) vertices of clique \(B\) with colors outside \(P\), in \((k-n)_{n-r}\) ways. The preceding characterization gives \(r\le n-2\) when \(t=1\), and \(r\le n-t\) when \(t\ge2\). For \(t=0\) the two injections are unrestricted, yielding \((k)_n^2\). For \(t=n\), either all \(2n\) colors are distinct, in \((k)_{2n}\) ways, or exactly one color repeats on a nonmatched ordered pair \((a_i,b_j)\), \(i\ne j\), in \(n(n-1)(k)_{2n-1}\) ways. These are all the colorings, proving the polynomial.

The maximum permissible number of shared colors is \(n,\ n-2,\ n-t,\ 1\) in the respective cases. As exactly \(2n-r\) distinct colors are then used, the minimum formulas follow. At the minimum, the repeated-color pairs form respectively: an arbitrary bijection of all \(n\) positions; a bijection of chosen \(n-2\) positions among the \(n-1\) unmatched positions on each side; a bijection of all \(n-t\) unmatched positions; or one nonmatched ordered pair of positions. Their counts are the stated \(U_{n,t}\). Relabeling the colors gives the named optimal counts.

## Verification

The bundled standalone `check_matching_join.py` constructs every graph edge and closed neighborhood directly and evaluates the original lid definition without using the structural characterization in its predicate. For every \(2\le n\le5\), every \(0\le t\le n\), and palettes from \(n\) through \(2n+1\), it tests every injective coloring of the second clique after canonically fixing the first clique's colors. In total it checks 697,320 bottom-layer assignments across 104 parameter cases, comparing each to the claimed structural criterion and each exact count to the polynomial. Fourteen additional small cases enumerate *both* clique colorings with named colors. Every check passed. The analytic proof, not this finite computation, establishes the result for all parameters.

To reproduce after extracting the standalone script, execute `python check_matching_join.py` with Python 3; no third-party packages, data files, or special permissions are required.

## Relationship to prior work

Esperet, Gravier, Montassier, Ochem, and Parreau introduced locally identifying colorings. Bhyravarapu, Kumari, and Reddy studied such colorings on Cartesian and tensor graph products and proved a general Cartesian-product upper bound; their preprint first appeared 2023-05-27. Oliveira's 2026 thesis proves the already-known scalar equality \(\chi_{\mathrm{lid}}(K_n\square P_m)=2n-1\) for \(n\ge3\) and \(m\ge2\). In particular the \(t=n\) scalar value above is *not* asserted to be new. The contribution here is the exact all-palette counting polynomial and complete coloring classification for the whole partial-matching family, including the changes at one and at full matching. Neither of those inspected primary sources states or implies these enumerators; the previously known scalar equality alone does not determine any of their coefficients.

## Limitations

The result is specific to two equally sized cliques with cross-edges forming a matching; it does not address arbitrary links or three or more clique layers. Its originality is assessed against the accessible source material and mathematical indexes; unindexed literature or differently worded equivalent formulations remain possible. The finite verifier tests only small instances and is not a substitute for the proof. Independent mathematical audit has not been performed.

## References

1. L. Esperet, S. Gravier, M. Montassier, P. Ochem, A. Parreau, *Locally Identifying Coloring of Graphs*, Electronic Journal of Combinatorics 19(2), P40 (2012), DOI 10.37236/2417; first arXiv posting 2010-10-27, arXiv:1010.5624.
2. S. Bhyravarapu, S. Kumari, I. V. Reddy, *On Locally Identifying Coloring of Cartesian Product and Tensor Product of Graphs*, arXiv:2305.17536 (first posted 2023-05-27); Discrete Applied Mathematics, DOI 10.1016/j.dam.2024.07.046.
3. R. M. de Oliveira, *Coloração de Identificação Local em Algumas Classes de Grafos*, PhD thesis, Universidade Federal de Goiás (2026), §6.3, Theorem 6.4 and §4.3, Lemma 4.8. Accessible at https://repositorio.bc.ufg.br/tede/handle/tede/15368.
