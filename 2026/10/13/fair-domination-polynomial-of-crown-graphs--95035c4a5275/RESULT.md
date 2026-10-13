# Fair-domination polynomial of crown graphs
## Finding
For every integer \(n\ge 3\), let \(\operatorname{Cr}_n\) be the crown graph with bipartition classes \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), where \(a_i b_j\) is an edge exactly when \(i\ne j\). For a vertex set \(S\), put
\[
I=\{i:a_i\in S\},\qquad J=\{i:b_i\in S\}.
\]
Then \(S\) is a fair dominating set if and only if at least one of the following mutually compatible structural conditions holds:

1. \(I=[n]\) or \(J=[n]\);
2. \(I=J\ne\varnothing\);
3. \(I\cup J=[n]\) and \(|I|=|J|\).

The full vertex set is included under the standard vacuous convention. After separating overlaps, the fair-domination polynomial is
\[
D_f(\operatorname{Cr}_n,x)
=2x^n(1+x)^n-x^{2n}
+\sum_{m=1}^{n-1}\binom{n}{m}x^{2m}
+\sum_{m=\lceil n/2\rceil}^{n-1}\binom{n}{m}\binom{m}{n-m}x^{2m}.
\]
Consequently,
\[
\operatorname{fd}(\operatorname{Cr}_n)=2,
\]
and the minimum fair dominating sets are exactly the \(n\) deleted-matching pairs \(\{a_i,b_i\}\).

If
\[
T_n=[z^n](1+z+z^2)^n
=\sum_{r=0}^{\lfloor n/2\rfloor}\frac{n!}{r!^2(n-2r)!}
\]
is the central trinomial coefficient, then the total number of fair dominating sets is
\[
D_f(\operatorname{Cr}_n,1)=3\cdot 2^n+T_n-4.
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. A set \(S\) is fair dominating when it dominates every vertex outside \(S\) and every outside vertex has the same positive number of neighbors in \(S\). The full vertex set is admitted vacuously, following the foundational convention. The theorem is stated only for \(n\ge3\), when both \(\operatorname{Cr}_n\) and its complement are connected.

The claimed contribution is the complete all-set classification, the closed fair-domination polynomial, the exact minimum-set multiplicity, and the central-trinomial total count for crown graphs. The already known complete-bipartite results and general complement principle are background, not claimed as new.

## Proof
Write \(p=|I|\) and \(q=|J|\). If \(a_i\notin S\), then its selected neighbors are all selected vertices of \(B\) except possibly its deleted mate \(b_i\), so
\[
|N(a_i)\cap S|=q-\mathbf 1_{i\in J}.
\]
Similarly, if \(b_i\notin S\), then
\[
|N(b_i)\cap S|=p-\mathbf 1_{i\in I}.
\]

Suppose first that \(I=[n]\) or \(J=[n]\). Every outside vertex then has exactly \(n-1\) selected neighbors, so the set is fair dominating. This includes the full vertex set.

Now assume both \(I\) and \(J\) are proper. Equality of the neighbor counts among vertices \(a_i\notin S\) says that the indicator \(\mathbf 1_{i\in J}\) is constant on \([n]\setminus I\). Hence either \([n]\setminus I\subseteq J\), equivalently \(I\cup J=[n]\), or \(([n]\setminus I)\cap J=\varnothing\), equivalently \(J\subseteq I\). The analogous argument on the \(B\)-side gives either \(I\cup J=[n]\) or \(I\subseteq J\). Therefore either \(I\cup J=[n]\) or \(I=J\).

If \(I=J=K\) is proper, every outside vertex has exactly \(|K|\) selected neighbors. This is positive exactly when \(K\ne\varnothing\), giving condition 2.

If \(I\cup J=[n]\) and both index sets are proper, every outside \(A\)-vertex has \(q-1\) selected neighbors and every outside \(B\)-vertex has \(p-1\). Fairness is therefore equivalent to \(p=q\), giving condition 3. Conversely, each of the three listed conditions makes the displayed neighbor counts equal and positive, so the classification is exact.

For the polynomial, sets with one whole side contribute \(2x^n(1+x)^n-x^{2n}\), with the full set subtracted once because it was counted twice. Proper sets with \(I=J\ne\varnothing\) contribute
\[
\sum_{m=1}^{n-1}\binom{n}{m}x^{2m}.
\]
For the remaining sets, let \(|I|=|J|=m\) and \(I\cup J=[n]\). Necessarily \(\lceil n/2\rceil\le m\le n-1\). Choose \(I\) in \(\binom{n}{m}\) ways; then \(J\) must contain the \(n-m\) elements outside \(I\) and choose its remaining \(2m-n\) elements from \(I\), giving \(\binom{m}{n-m}\) choices. These families are disjoint after the stated exclusions, proving the polynomial.

The least exponent is \(2\), arising only from \(I=J=\{i\}\), so the minimum result and its multiplicity follow. At \(x=1\), the whole-side family contributes \(2^{n+1}-1\), the equal-index proper family contributes \(2^n-2\), and the union-full equal-size family contributes \(T_n-1\): setting \(r=n-m\) identifies its summand with \(n!/(r!^2(n-2r)!)\), while the omitted \(m=n\) term is the final \(1\). Summing gives \(3\cdot2^n+T_n-4\).

## Verification
The accompanying standalone checker constructs \(\operatorname{Cr}_n\) directly for every \(3\le n\le9\), tests every vertex subset against the literal fair-domination definition, compares it with the structural classification, and checks every polynomial coefficient, the minimum value and multiplicity, and the central-trinomial total-count identity. For \(3\le n\le8\) it also constructs the complement and verifies set-by-set preservation of fair domination. Its completed output is:

`VERIFY_OK n_range=3..9 subset_checks=349504 fair_sets=7877 classification_checks=349504 coefficient_checks=91 minimum_total_checks=21 complement_checks=87360 max_order=18`

The finite census is a regression check. The theorem for all \(n\ge3\) follows from the symbolic argument above.

## Relationship to prior work
Caro, Hansberg, and Henning define fair domination and prove the complement principle: when a graph and its complement are connected, a fair dominating set of one is also fair dominating in the other, with the outside-neighbor count complemented inside the selected set. They also record \(\operatorname{fd}(K_{m,n})=\gamma(K_{m,n})\). Their first arXiv version is dated 2011-09-06 and records MSC 05C69. This supplies the parameter definition and the useful equivalent formulation through \(\overline{\operatorname{Cr}_n}\cong K_n\square K_2\), but it does not give the crown classification or polynomial.

Alikhani and Safazadeh define the fair-domination polynomial and determine cardinality counts for the balanced complete bipartite graph \(K_{n,n}\). Their inspected full text contains no occurrence of “crown” or “matching.” The complete-bipartite theorem is not strong enough to imply the result here: deleting the matching changes an outside neighbor count from a part occupancy to an index-sensitive quantity such as \(q-\mathbf 1_{i\in J}\).

A published published-finding corpus record, identifier `b883ddb6f548`, gives the fair-domination polynomial for arbitrary complete multipartite graphs. Crown graphs with \(n\ge3\) are not complete multipartite graphs, and the index-sensitive missing edges are precisely what create the two nontrivial crown conditions \(I=J\) and \(I\cup J=[n]\) with equal sizes. Thus that broader-looking family theorem does not cover the present statement.

The contrast with \(K_{n,n}\) is structural: both families have fair domination number \(2\), but \(K_{n,n}\) has \(n^2\) minimum fair dominating sets, whereas \(\operatorname{Cr}_n\) has only \(n\), exactly the deleted-matching pairs.

## Limitations
A 2010 thesis repository entry explicitly lists fair domination among its topics, but the repository exposes only a graduation year and not a verified public-posting day. No day was inferred from the thesis approval date; the exact-date source anchor used here is therefore the 2011-09-06 arXiv record. This date uncertainty does not affect archive eligibility.

Targeted searches under “crown graph,” “complete bipartite graph minus a perfect matching,” “bipartite Kneser \(H(n,1)\),” the complement description “two cliques joined by a perfect matching,” and \(K_n\square K_2\) did not reveal an equivalent published all-set classification. Such searches cannot exclude a poorly indexed source or a result stated in an uncommon terminology. The originality assessment is therefore relative to the inspected literature and databases, not a claim of exhaustive global uniqueness.

## References
1. Y. Caro, A. Hansberg, M. A. Henning, “Fair Domination in Graphs,” arXiv:1109.1150v1, 2011-09-06; later *Discrete Mathematics* 312 (2012), 2905–2914, DOI 10.1016/j.disc.2012.05.006.
2. S. Alikhani, M. Safazadeh, “On the number of fair dominating sets of graphs,” arXiv:2107.10671v1, 2021-07-21.
3. J. M. Tarr, “Domination in Graphs,” M.A. thesis, University of South Florida, 2010; public repository record 1786 gives graduation year only.
4. published-finding corpus record `b883ddb6f548`, “Fair domination polynomial of complete multipartite graphs.”
