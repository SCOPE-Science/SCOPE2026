# Maximal square-zero ranks and exact extremizer counts in wheel partial-isometry monoids

## Finding
Let \(n\ge4\). The wheel \(W_n\) has vertices \(\{0,1,\ldots,n\}\), with hub \(0\), rim cycle \(C_n\), and all spokes from the hub. Let \(\mathcal D(W_n)\) be the inverse monoid of partial bijections preserving graph distance. For \(f\in\mathcal D(W_n)\), write \(\operatorname{rk}(f)=|\operatorname{dom}f|\). A square-zero element satisfies \(f^2=\varnothing\), where \(\varnothing\) is the empty partial map.

The maximum rank of a square-zero element is exactly
\[
\boxed{\rho_n=\left\lfloor\frac n2\right\rfloor.}
\]
Every rank \(0,1,\ldots,\rho_n\) occurs. In particular, for every odd \(n\ge5\), the ambient symmetric inverse monoid on \(n+1\) vertices admits a square-zero rank \((n+1)/2\), but the wheel partial-isometry monoid does not.

Put \(k=\lfloor n/2\rfloor\) and define the formal series
\[
B(z)=z+2z^2+2z^3+\cdots=\frac{z(1+z)}{1-z}.
\]
For the number \(M_n\) of square-zero elements of maximum rank \(k\), put
\[
H_n=\begin{cases}
 n\displaystyle\sum_{r=1}^k(r-1)!\,[z^k]B(z)^r,&n=2k,\\[3pt]
 2n\displaystyle\sum_{r=1}^k r!\,[z^k]B(z)^r,&n=2k+1.
\end{cases}
\]
Then the complete exact extremal enumeration is
\[
\boxed{M_n=H_n+E_n,\qquad
E_n=\begin{cases}
4n(n-2),&n\in\{4,5\},\\
2n(n-4)(n-5),&n\in\{6,7\},\\
0,&n\ge8.
\end{cases}}
\]
The term \(H_n\) counts maps with both domain and image on the rim; \(E_n\) counts those using the hub on exactly one side. In particular \(M_4=44\), \(M_5=100\), \(M_6=72\), \(M_7=308\), \(M_8=224\), \(M_9=1404\), \(M_{10}=1220\), \(M_{11}=9812\), and \(M_{12}=7752\).

## Assumptions and scope
This is a statement for every integer \(n\ge4\), about the graph-distance-preserving partial bijections of the wheel with a rim of \(n\) vertices (hence \(n+1\) total vertices). Graph distance between distinct rim vertices is \(1\) exactly for adjacent rim vertices and \(2\) otherwise, including through the hub. Rank here is the image/domain cardinality of an individual partial map, **not** the size of a smallest generating set of the monoid. Formal coefficient extraction is over the integers, and all sums are finite at each coefficient.

## Proof
**Square-zero and the maximum.** For any partial injection \(f\), the identity \(f^2=\varnothing\) is equivalent to \(\operatorname{dom}f\cap\operatorname{im}f=\varnothing\). Hence \(2\operatorname{rk}f\le n+1\). Suppose the hub belongs to exactly one of these disjoint sets; by inversion, assume it is in the domain. Its image must be a rim vertex \(v\). The other domain vertices are all rim vertices at distance \(1\) from the hub, so their images must be rim neighbors of \(v\), of which there are only two. Consequently any square-zero partial isometry involving the hub has rank at most \(3\).

For odd \(n\ge7\), a hypothetical rank \((n+1)/2\ge4\) uses all vertices, hence the hub, contradicting the preceding bound. For \(n=5\), hypothetical rank \(3\) also uses every vertex. The image of the hub would be \(v\), and the two other image vertices would be \(v-1,v+1\) modulo \(5\). The remaining two rim vertices \(v-2,v+2\) are adjacent, while \(v-1,v+1\) have distance \(2\), contradicting isometry. Therefore rank is at most \(\lfloor n/2\rfloor\) in every case. It is attained by mapping any selected \(\lfloor n/2\rfloor\) alternating rim vertices bijectively to the next \(\lfloor n/2\rfloor\) alternating rim vertices: both selected induced rim graphs are edgeless and the two sets are disjoint. Restricting such a map to arbitrary smaller domains realizes every intermediate rank.

**Rim extremizers for even \(n=2k\).** A rank-\(k\) square-zero map avoiding the hub has a domain and an image partitioning all \(2k\) rim vertices. Color these vertices red (domain) and blue (image). The metric restrictions are equivalent to the red and blue induced subgraphs of the rim cycle being isomorphic. Each is a disjoint union of paths, whose component sizes are the lengths of its monochromatic circular runs. Thus the red and blue multisets of run lengths must agree. They have some common run count \(r\), with red runs \((a_1,\ldots,a_r)\), an ordered composition of \(k\). For each part of size \(j\), a path component has \(b_j\) internal automorphisms, where \(b_1=1\) and \(b_j=2\) for \(j\ge2\). Once the red ordered composition is specified, summing over all blue rearrangements with the same multiset and over bijections between matching components gives exactly
\[
r!\prod_{i=1}^r b_{a_i}.
\]
Indeed, if \(m_j\) runs have length \(j\), there are \(r!/\prod_jm_j!\) distinct blue orders and \(\prod_jm_j!\,\prod_jb_j^{m_j}\) isomorphisms for each. A marked start of the first red run has \(n\) possible labeled locations, whereas each cyclic coloring is counted \(r\) times by choosing the marked red run. Consequently the number is
\[
n\sum_{r=1}^k(r-1)!\sum_{a_1+\cdots+a_r=k}\prod_i b_{a_i}
=n\sum_{r=1}^k(r-1)![z^k]B(z)^r.
\]

**Rim extremizers for odd \(n=2k+1\).** A rank-\(k\) rim-only map leaves exactly one rim vertex unused. There are \(n\) choices for this vertex; its deletion cuts the occupied rim into a linear path of \(2k\) positions colored red/blue. Equality of the red and blue component-length multisets forces the number \(r\) of red and blue runs to be equal. Hence the ends have opposite colors, with two choices for the initial color. For a fixed starting color, an ordered red composition of \(k\) into \(r\) parts again contributes \(r!\prod b_{a_i}\) from blue rearrangements and path-component bijections. Therefore the number is
\[
2n\sum_{r=1}^kr![z^k]B(z)^r.
\]

**Hub corrections.** As proved above, hub-using square-zero partial isometries have rank at most three. For \(n=4,5\), maximum rank is two. If the hub is in the domain, its other domain vertex may be any of the \(n\) rim vertices; the two ordered image vertices must form a directed rim edge avoiding that domain vertex. There are \(2(n-2)\) such edges for each choice, giving \(2n(n-2)\) maps; inversion doubles this to \(4n(n-2)\).

For \(n=6,7\), maximum rank is three. If the hub maps to rim vertex \(v\), the other two image vertices must be \(v-1\) and \(v+1\); the two other domain vertices must be a nonadjacent pair among the \(n-3\) rim vertices outside \(\{v-1,v,v+1\}\). These remaining vertices form a path, giving \(\binom{n-3}{2}-(n-4)=(n-4)(n-5)/2\) eligible unordered pairs. There are two bijections of each such pair to \(\{v-1,v+1\}\). Multiplying by \(n\) hub-image choices and by two for inversion gives \(2n(n-4)(n-5)\). For \(n\ge8\), the maximum rank is at least four, so no hub-using map is extremal. This completes the enumeration.

## Verification
Run `python wheel_squarezero_checker.py` in the directory containing that standalone script. It enumerates all disjoint domain/image \(k\)-subsets and all bijections between them, checking pairwise wheel distances directly and independently of the run decomposition. For \(n=4,\ldots,12\), every maximum-rank count, including the hub/rim split, matches the formula. It also tests the impossibility of the larger rank in the two small odd cases \(n=5,7\). The output is included in `wheel_squarezero_check_output.txt`.

## Relationship to prior work
Fernandes introduced and analyzed the wheel partial-isometry monoid, its Green relations, submonoids and **generating** ranks [1]. The present result instead concerns the maximal **element** rank under square-zero multiplication and the exact number of extremizers. The full text of [1] describes hub-mapping restrictions and generators but gives no extremal square-zero enumeration. General partial graph-automorphism inverse-monoid structure and induced-subgraph isomorphism classes are developed in [2]; those results motivate the graph-isomorphism step but do not imply this wheel-specific run formula or hub correction. The cycle partial-isometry presentation and cardinality in [3] concern the stricter intrinsic cycle metric, not the diameter-two metric that rim vertices inherit from a wheel.

## Limitations
This result counts only the maximum-rank square-zero elements, together with the set of attainable square-zero ranks; it does not provide the full rank enumerator or classify all nilpotency indices. The general proof is independent of the finite checks. The closest relevant wheel paper was read as available open full text; specialist enumeration not indexed by the searches remains a possible priority risk. No independent mathematical audit has been performed.

## References
1. V. H. Fernandes, *On the monoid of partial isometries of a wheel graph*, arXiv:2307.16257v1, first posted 30 July 2023; later Asian-European Journal of Mathematics 17 (2024), 2350238. https://arxiv.org/abs/2307.16257
2. R. Jajcay, T. Jajcayová, N. Szakács, M. B. Szendrei, *Inverse monoids of partial graph automorphisms*, arXiv:1809.04422, first posted 12 September 2018. https://arxiv.org/abs/1809.04422
3. V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a cycle graph*, Turkish Journal of Mathematics 47 (2023), 1746–1760, DOI 10.55730/1300-0098.3460. https://journals.tubitak.gov.tr/math/vol47/iss6/10/
