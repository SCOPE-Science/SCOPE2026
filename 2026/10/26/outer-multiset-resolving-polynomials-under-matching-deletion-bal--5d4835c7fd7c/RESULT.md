# Outer multiset resolving polynomials under matching deletion: balance-induced gaps

## Finding

Let \(3\le p\le q\) and \(0\le t\le p\) be integers. Form \(G_{p,q,t}\) from the complete bipartite graph \(K_{p,q}\) by deleting the independent edges \(a_i b_i\), for \(1\le i\le t\), where the bipartition classes are \(A=\{a_1,\ldots,a_p\}\) and \(B=\{b_1,\ldots,b_q\}\). Put \(N=p+q\). For a landmark set \(S\), write \(m_S(v)\) for the multiset of distances from \(v\) to every vertex of \(S\). Call \(S\) *outer multiset resolving* when \(m_S(u)\ne m_S(v)\) for all distinct \(u,v\notin S\), and define its complete enumerator by

\[
\mathcal R_{p,q,t}(z)=\sum_{S\text{ outer multiset resolving}}z^{|S|}.
\]

The exact polynomial is

\[
\boxed{\mathcal R_{p,q,t}(z)=z^N+Nz^{N-1}+A_2z^{N-2}+A_3z^{N-3}+A_4z^{N-4}},
\]

where \(\mathbf1_E\) is one when condition \(E\) holds and zero otherwise, and

\[
\begin{aligned}
A_2&=t(p+q-2t)+\begin{cases}pq,&p<q,\\2t(p-t),&p=q,\end{cases}\\[2pt]
A_3&=t(t-1)+t(p-t)(q-1)\\
&\quad+\mathbf1_{\{q\ne p+1\}}\bigl[t(t-1)+t(q-t)(p-1)\bigr],\\[2pt]
A_4&=\mathbf1_{\{p<q\}}\,t(t-1)\bigl[t-2+(p-t)(q-t)\bigr].
\end{aligned}
\]

All other coefficients are zero. Consequently the outer multiset dimension, the minimum cardinality of such an \(S\), is

\[
\boxed{\operatorname{odim}(G_{p,q,t})=\begin{cases}
N-1,&t=0,\ p=q,\\
N-2,&t=0,\ p<q,\\
N-3,&t=1\text{ or }(t\ge1\text{ and }p=q),\\
N-4,&t\ge2,\ p<q.
\end{cases}}
\]

In the crown-graph endpoint \(p=q=t=n\ge3\), the polynomial simplifies to

\[
\boxed{\mathcal R_{n,n,n}(z)=z^{2n}+2nz^{2n-1}+2n(n-1)z^{2n-3}}.
\]

Thus every minimum outer multiset basis of a crown graph omits exactly three vertices, there are exactly \(2n(n-1)\) bases, and **no** outer multiset resolving set has \(2n-2\) vertices. In particular, the family of outer multiset resolving sets is not upward-closed: adding any one vertex to any minimum basis in this case destroys the outer multiset resolving property. These support gaps disappear when \(p=q\) but \(1\le t<p\).

## Assumptions and scope

Graphs are finite, simple, undirected, connected and labeled as described. The condition \(p\ge3\) ensures every two vertices in one bipartition class have a common neighbor, even after the matching is removed. A missing matched edge has distance three; all other opposite-class pairs have distance one. Every same-class pair has distance two. The zero-deletion case \(t=0\) is included only to show the sharp transition from the previously known complete-bipartite boundary, not as a new result in isolation. The parameter \(\operatorname{odim}\) is the *outer multiset* dimension, not ordinary metric dimension, edge metric dimension, or local multiset dimension.

## Proof

**Distance-signature lemma.** Let \(I=\{i:a_i\notin S\}\subseteq[p]\), \(J=\{j:b_j\notin S\}\subseteq[q]\), \(x=|I|\), \(y=|J|\), and \(T=[t]\). Define

\[
P=I\cap(T\setminus J),\qquad Q=J\cap(T\setminus I).
\]

For each \(i\in I\), the multiplicities of distances two and three in \(m_S(a_i)\) are, respectively,

\[
\bigl(p-x,\ \mathbf1_{\{i\in P\}}\bigr).
\]

For each \(j\in J\), the corresponding multiplicities in \(m_S(b_j)\) are

\[
\bigl(q-y,\ \mathbf1_{\{j\in Q\}}\bigr).
\]

Every remaining landmark lies at distance one. The first count follows because every selected vertex on the same bipartition side is at distance two, while the unique possibly missing cross-edge is \(a_i b_i\). The same argument applies to the other side. Since the number of selected landmarks is fixed, the two displayed multiplicities determine the entire multiset.

Consequently, if \(S\) resolves its complement, then \(x,y\le2\). When \(x=2\), exactly one member of \(I\) belongs to \(P\); when \(y=2\), exactly one member of \(J\) belongs to \(Q\). If \(p-x=q-y\), signatures across the two sides have the same number of distance-two entries; at most two outside vertices can then be distinguished, using the two possible distance-three indicators. This proves that no resolving set can have four or more omitted vertices unless \(x=y=2\) and \(p<q\). These are necessary and sufficient conditions, together with distinct cross-side indicators when exactly one vertex of each side is omitted and \(p=q\).

**Zero and one omitted vertex.** The complement of every set of size \(N\) or \(N-1\) has at most one vertex, so contributes \(1\) and \(N\), respectively.

**Two omitted vertices.** If both omitted vertices lie in \(A\), one must have a deleted partner and the other an undeleted partner: there are \(t(p-t)\) possibilities. The analogous count in \(B\) is \(t(q-t)\). When one omitted vertex lies on each side, they are automatically distinguished if \(p<q\), contributing \(pq\). If \(p=q\), their distance-two counts agree, and exactly one of them must have an unomitted deleted partner, contributing \(2t(p-t)\). Summing yields \(A_2\).

**Three omitted vertices.** For \(x=2,y=1\), the distance-two counts are \(p-2\) and \(q-1\), which differ. The two omitted \(A\)-vertices must have exactly one member of \(P\). They can both have deleted partners, with the unique omitted \(B\)-vertex sharing exactly one of their indices (\(t(t-1)\) choices); or one can have a deleted partner and the other an undeleted one, while the omitted \(B\)-vertex avoids the first index (\(t(p-t)(q-1)\) choices). Thus their total is \(t(t-1)+t(p-t)(q-1)\). The symmetric \(x=1,y=2\) case has count \(t(t-1)+t(q-t)(p-1)\), but it is impossible when \(q=p+1\) because then \(p-1=q-2\) and three outside vertices offer only two distinct signature types. This proves \(A_3\).

**Four omitted vertices.** Necessarily \(x=y=2\) and \(p<q\); then the two sides have distinct distance-two counts. Each side must have exactly one outside vertex whose deleted partner remains selected. If one deleted index belongs to both omission sets, there are \(t(t-1)(t-2)\) ordered choices of the common index, the exclusive \(A\)-index and the exclusive \(B\)-index. If no deleted index is common to both omission sets, choose two distinct exclusive deleted indices, one ordinary \(A\)-index, and one ordinary \(B\)-index, giving \(t(t-1)(p-t)(q-t)\). Summing gives \(A_4\), and no other four-omission configurations qualify.

**Extremal values and missing layer.** The coefficients are nonnegative counting formulas. For \(t=0\), the first nonzero coefficient after \(z^{N-1}\) occurs at \(z^{N-2}\) precisely if \(p<q\). For \(t=1\), \(A_3>0\) and \(A_4=0\). For \(t\ge2\), \(A_4>0\) exactly when \(p<q\), since \(p\ge3\) guarantees \(t-2+(p-t)(q-t)>0\) whenever \(t\ge2\); if \(p=q\), \(A_3>0\). This proves the dimension formula. Setting \(p=q=t=n\) gives \(A_2=A_4=0\) and \(A_3=2n(n-1)\), proving the crown statement and its support gap.

## Verification

The standalone program `verify.py` constructs each actual graph, computes all-pairs shortest-path distances by breadth-first search, and independently tests *every* landmark subset by directly comparing sorted distance lists. It compares the resulting coefficients against the formulas for every \(3\le p\le5\), \(p\le q\le6\), \(0\le t\le p\), together with three repeated boundary instances: \(46\) tested parameter triples and \(31{,}936\) enumerated subsets. It reports `PASS`. These finite tests are checks of the proof, not substitutes for the all-parameter argument above.

## Relationship to prior work

Gil-Pons, Ramírez-Cruz, Trujillo-Rasua and Yero introduced the outer multiset dimension and established its fundamental properties in 2019; their work includes the exact value for the six-cycle and equal-sized complete multipartite graphs. Klavžar, Kuziak and Yero (first published online in 2022) characterized graphs whose outer multiset dimension equals their order minus one; in particular, the balanced undeleted boundary is already known. A scientific record on complete multipartite graphs provides the entire undeleted \(t=0\) case in wider generality. These results do not imply the present deleted-matching polynomial because the distance-three signatures and their cross-side balance obstruction disappear at \(t=0\). A 2026 paper by Araujo-Pardo and coauthors studies circulant graphs and diameter-based bounds, not this family. The new claim here is the precise \(t\ge1\) classification, the four coefficient formulas, and the zero-coefficient layer at the crown endpoint.

## Limitations

The result is restricted to \(p\ge3\). Two-vertex smaller bipartition classes may have same-class distance four after deleting a matching, so the signature lemma is not asserted there. The general proof is elementary and does not settle arbitrary forbidden-edge patterns, higher graph diameter, or the analogous nonouter multiset dimension. Literature searches and accessible primary full-text comparisons support an originality assessment but do not prove worldwide novelty; unindexed results and an inaccessible recent survey remain a residual priority risk. Independent audit is not asserted.

## References

1. R. Gil-Pons, Y. Ramírez-Cruz, R. Trujillo-Rasua, and I. G. Yero, *Distance-based vertex identification in graphs: the outer multiset dimension* (first public arXiv version February 8, 2019), arXiv:1902.03017, https://arxiv.org/abs/1902.03017.
2. S. Klavžar, D. Kuziak, and I. G. Yero, *Further Contributions on the Outer Multiset Dimension of Graphs*, Results in Mathematics 78 (2023), article 50, first published December 31, 2022, DOI:10.1007/s00025-022-01829-8, https://rodin.uca.es/handle/10498/29371.
3. G. Araujo-Pardo et al., *On the outer multiset dimensions of graphs*, Boletín de la Sociedad Matemática Mexicana 32 (2026), article 142, published October 17, 2026, DOI:10.1007/s40590-026-00973-3, https://link.springer.com/article/10.1007/s40590-026-00973-3.
4. *Outer multiset dimension of arbitrary complete multipartite graphs*, scientific result record, https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-outer-multiset-dimension-complete-multipartite--ea7c8ea4c9fd (contextual comparator for the undeleted boundary only).
