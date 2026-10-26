# Effective resistance separates all two-configuration symmetry types of the Petersen token graph

## Finding

Let \(P=\operatorname{KG}(5,2)\), the Petersen graph on the ten two-element subsets of \(\{0,1,2,3,4\}\), with two vertices adjacent when disjoint. Let \(F=F_2(P)\) be the simple graph of configurations consisting of two *indistinguishable* tokens on distinct vertices of \(P\). A legal move slides one token along a Petersen edge to an unoccupied vertex. Give each of the 120 edges of \(F\) unit electrical resistance, and write \(R_F(A,B)\) for effective resistance between two distinct configurations.

**Theorem.** For any two unordered pairs of distinct configurations \(\{A,B\}\) and \(\{C,D\}\),
\[
 R_F(A,B)=R_F(C,D)
 \quad\Longleftrightarrow\quad
 \{A,B\}\text{ and }\{C,D\}\text{ lie in the same }\operatorname{Aut}(F)\text{-orbit}.
\]
There are exactly **17** such orbits among the 990 unordered configuration pairs, and their 17 resistance values are all distinct. The following table is the complete resistance spectrum with orbit sizes. Each resistance is \(m/95760\). The last column records shortest token-slide distance and the representative is indexed as defined below.

| Representative \((i,j)\) | Multiplicity | Numerator \(m\) | Shortest distance |
| --- | ---: | ---: | ---: |
| (0,4) | 60 | 32257 | 1 |
| (0,38) | 60 | 36730 | 2 |
| (0,8) | 60 | 37967 | 1 |
| (0,36) | 30 | 38189 | 2 |
| (0,3) | 30 | 38756 | 2 |
| (0,1) | 60 | 38981 | 2 |
| (0,23) | 60 | 39584 | 3 |
| (0,19) | 120 | 40483 | 3 |
| (0,17) | 15 | 41562 | 4 |
| (0,37) | 60 | 46283 | 2 |
| (0,6) | 120 | 46801 | 2 |
| (0,34) | 30 | 49083 | 3 |
| (0,20) | 120 | 49447 | 3 |
| (0,18) | 60 | 50441 | 4 |
| (6,7) | 30 | 55076 | 2 |
| (6,13) | 60 | 58156 | 3 |
| (6,12) | 15 | 59360 | 4 |

In particular, the minimum effective resistance is \(32257/95760\) (60 pairs), the maximum is \(106/171\) (15 pairs), and the Kirchhoff index is
\[
 \sum_{\{A,B\}\subset V(F)}R_F(A,B)=\frac{486429}{1064}.
\]
Resistance is **not monotone** with graph distance: representatives \((0,38)\) and \((0,8)\) have distances two and one, respectively, but
\[
 R_F(0,38)=\frac{36730}{95760}<\frac{37967}{95760}=R_F(0,8).
\]
Thus resistance both separates substantially more geometry than shortest-path distance and can order nearby configuration pairs oppositely to that distance.

## Assumptions and scope

All graphs are finite, undirected and simple; all electrical edge resistances equal one. Configurations are unordered two-subsets of Petersen vertices, not configurations of distinguishable tokens. Vertex labels are deterministic: list the ten two-subsets of \(\{0,1,2,3,4\}\) in lexicographic order and give them base-vertex indices \(0,\ldots,9\). Then list the 45 two-subsets of \(\{0,\ldots,9\}\) in lexicographic order and give them configuration-state indices \(0,\ldots,44\). Every table representative \((i,j)\) means the unordered pair of configuration states with these indices. The denominator \(95760\) is an exact common denominator, not a floating-point normalization.

The finding concerns resistance between pairs of vertices of \(F\), not resistance measured directly in \(P\). The group in the theorem is the full automorphism group of \(F\). No assertion concerns more than two tokens, other underlying graphs, or weighted variants.

## Proof

**Construction and completeness.** A configuration is a two-subset of the ten base vertices, so there are \(\binom{10}{2}=45\) states. Every Petersen edge \(uv\) permits a move between the states \(\{u,w\}\) and \(\{v,w\}\) for each of the eight choices \(w\notin\{u,v\}\). Each token edge corresponds to exactly one base edge and one stationary token. Consequently \(|E(F)|=15\cdot8=120\). Fifteen configurations occupy adjacent Petersen vertices and have degree four; the other thirty have degree six.

**Exact electrical calculation.** Let \(L\) be the \(45\times45\) combinatorial Laplacian of \(F\). Ground state \(0\) by deleting its row and column, giving the \(44\times44\) reduced Laplacian \(L_0\). The graph is connected; the exhaustive breadth-first search in `verify.py` visits every state. Set \(B=L_0^{-1}\), and extend \(B\) by a zero row and column at state \(0\). For any distinct states \(i,j\), electrical-network linear algebra gives
\[
 R_F(i,j)=B_{ii}+B_{jj}-2B_{ij}.
\]
Inverting \(L_0\) by exact rational Gauss–Jordan elimination and checking the product \(L_0B=I\) gives the table's exact rational values. The supplied verifier reconstructs the graph, the inverse and *every one* of the 990 resistances, without numerical approximation. Its reduced-inverse formula also covers pairs with state \(0\).

**Orbit computation.** The full permutation group \(S_5\) acts on the underlying five labels, hence on Petersen vertices and on token states, preserving every edge of \(F\). Enumerate its \(5!=120\) permutations. Applied to unordered distinct pairs of the 45 states, this action partitions the 990 pairs into the 17 orbits listed in the table. For each orbit the exact resistance formula gives its displayed rational value; an exhaustive check verifies constancy on every member. The multiplicities sum to 990, proving exhaustiveness. The 17 numerators are distinct, proving distinctness of resistance values.

Every graph automorphism preserves the electrical resistance function. Thus two pairs in one \(\operatorname{Aut}(F)\)-orbit have equal resistance. Conversely, pairs of equal resistance belong to the same \(S_5\)-orbit by the 17-value calculation, and therefore to the same full automorphism orbit. This proves both directions of the theorem without needing an a priori classification of all automorphisms of \(F\).

**Distance and Kirchhoff consequences.** Exhaustive breadth-first search on \(F\) gives respectively 120, 390, 390 and 90 unordered pairs at token-slide distances one through four. The table contains 60 pairs with numerator 36730 at distance two, and 60 with numerator 37967 at distance one, proving the stated inversion. Summing the resistance numerators with their multiplicities gives the Kirchhoff index \(486429/1064\); the exact sum is checked independently of table presentation in the verifier.

## Verification

Run `python3 verify.py` in the same directory. The script uses only the Python standard library (`fractions`, `itertools`, and `collections`) and prints `VERIFY_OK` after checking the theorem. It independently constructs the Petersen graph from both Kneser's disjointness rule and the \(\operatorname{GP}(5,2)\) cycle-and-spoke model, verifying equality of their edge sets. It constructs all 45 configurations and 120 moves, computes the exact 44-by-44 grounded inverse, checks the matrix product, checks the entire \(S_5\)-orbit partition, and checks all 17 exact resistance values and shortest distances.

As an additional spectral checksum, an exact characteristic-polynomial calculation for the same combinatorial Laplacian gives
\[
 \chi_L(x)=x(x-2)^5(x-3)^5(x-5)^4(x-6)^6(x-7)^6
 (x^2-13x+32)^4(x^2-13x+38)^5.
\]
The standard spectral Kirchhoff identity \(\sum_{\{A,B\}}R_F(A,B)=45\sum_{\lambda>0}\lambda^{-1}\) then yields \(486429/1064\), agreeing with the entrywise exact calculation. This polynomial is a consistency check, not a replacement for the pair-resistance computation.

## Relationship to prior work

Audenaert, Godsil, Royle and Rudolph introduced and analyzed symmetric graph powers and proved cospectrality principles for symmetric squares of strongly regular graphs (public arXiv version dated 2005-07-12). Fabila-Monroy and coauthors treated token graphs and general connectivity and diameter (public version dated 2009-10-25). Dalfó and coauthors developed Laplacian-spectral inclusion for token graphs, while Fabila-Monroy and Trujillo-Negrete established automorphism reconstruction for connected \((C_4,\mathrm{diamond})\)-free graphs, a class containing the Petersen graph. Reyes, Dalfó and Fiol supplied additional spectral-radius and distance-regular quotient tools.

The cited spectral theorems concern eigenvalues and quotient matrices, not the *entrywise* pseudoinverse or the 17 different effective resistances. The cited automorphism theorem identifies a group but does not imply that a scalar electrical invariant distinguishes every pair orbit. The present finding is exactly that distinction and its table, not the previously known graph definition, symmetry group or general resistance formula. Searches for two-token Petersen resistance spectra and their pair-orbit equivalences revealed no directly covering published computation, but such searches cannot establish absolute novelty.

## Limitations

This is a complete finite calculation for one canonical 45-state exclusion graph, not an infinite-family resistance theorem. It uses exact rational linear algebra and an exhaustive orbit census whose completeness depends on the transparent finite indexing and loops in the supplied program. The link from unit-resistor networks to random-walk commute times uses the standard simple-random-walk normalization \(2|E(F)|=240\); alternative weighted or continuous-time normalizations are not part of the finding. An unpublished or unindexed equivalent table could predate this calculation. Independent external auditing and validation have not been performed.

## References

1. K. Audenaert, C. Godsil, G. Royle, T. Rudolph, *Symmetric Squares of Graphs*, arXiv:math/0507251 (first public version 2005-07-12), https://arxiv.org/abs/math/0507251.
2. R. Fabila-Monroy, D. Flores-Peñaloza, C. Huemer, F. Hurtado, J. Urrutia, D. R. Wood, *Token Graphs*, arXiv:0910.4774 (first public version 2009-10-25), https://arxiv.org/abs/0910.4774.
3. C. Dalfó, F. Duque, R. Fabila-Monroy, M. A. Fiol, C. Huemer, A. L. Trujillo-Negrete, F. J. Zaragoza Martínez, *On the Laplacian spectra of token graphs*, arXiv:2012.00808 (2020-12-01), https://arxiv.org/abs/2012.00808.
4. R. Fabila-Monroy, A. L. Trujillo-Negrete, *Connected (C4,Diamond)-free Graphs Are Uniquely Reconstructible from Their Token Graphs*, arXiv:2207.12336 (2022-07-25), https://arxiv.org/abs/2207.12336.
5. M. A. Reyes, C. Dalfó, M. A. Fiol, *On the spectra and spectral radii of token graphs*, arXiv:2310.16929 (2023-10-25), https://arxiv.org/abs/2310.16929.
