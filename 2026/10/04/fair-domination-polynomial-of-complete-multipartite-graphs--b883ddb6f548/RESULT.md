# Fair domination polynomial of complete multipartite graphs

## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), nonempty partite classes \(V_1,\ldots,V_r\), and \(N=\sum_i n_i\). For \(D\subseteq V(G)\), set \(d_i=|D\cap V_i|\) and \(d=|D|\).

A proper set \(D\ne V(G)\) is a fair dominating set if and only if there is an integer \(t\ge0\) such that
\[
d_i=t\qquad\text{for every index }i\text{ with }d_i<n_i,
\]
and
\[
d-t>0.
\]
The full set \(V(G)\) is fair dominating under the standard vacuous convention for fair domination.

Put \(L=\max_i n_i\), and for \(0\le t<L\) define
\[
P_t(x)=x^{\sum_{i:n_i\le t}n_i}\prod_{i:n_i>t}\left(x^{n_i}+\binom{n_i}{t}x^t\right).
\]
Then the fair domination polynomial, whose coefficient of \(x^j\) counts fair dominating sets of cardinality \(j\), is
\[
D_f(G,x)=\sum_{t=0}^{L-1}P_t(x)-(L-1)x^N-1.
\]
As a scalar consequence,
\[
\operatorname{fd}(G)=\min\left\{r,\min_i n_i\right\}.
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. The multipartite representation has \(r\ge2\) nonempty parts, so \(G\) is connected. Fair domination uses the definition of Caro, Hansberg, and Henning: a proper dominating set is fair when every vertex outside it has the same positive number of neighbors in the set; \(V(G)\) is admitted vacuously. The enumerator uses the fair domination polynomial convention of Alikhani and Safazadeh.

The novelty claim is the arbitrary complete-multipartite all-set classification and its closed polynomial. The balanced complete-bipartite case \(K_{n,n}\) is prior-covered and is used as a consistency specialization rather than claimed as new.

## Proof
Let \(D\ne V(G)\). If \(v\in V_i\setminus D\), then every selected vertex outside \(V_i\) is adjacent to \(v\), while no selected vertex in \(V_i\) is adjacent to \(v\). Therefore
\[
|N(v)\cap D|=d-d_i.
\]
Hence if \(D\) is fair, then for any two non-full parts \(V_i,V_j\) we have \(d-d_i=d-d_j\), so \(d_i=d_j\). Thus all non-full parts contain a common number \(t\) of selected vertices. Fair domination also requires the common outside-neighbor count \(d-t\) to be positive.

Conversely, suppose every non-full part contains exactly \(t\) selected vertices and \(d-t>0\). Every vertex outside \(D\) lies in a non-full part and therefore has exactly \(d-t\) neighbors in \(D\). Thus every outside vertex is dominated by the same positive number of selected vertices, so \(D\) is fair dominating. This proves the classification.

For the polynomial, fix \(t\in\{0,\ldots,L-1\}\). A part with \(n_i\le t\) cannot be non-full with exactly \(t\) selected vertices and is therefore forced to be full, contributing \(x^{n_i}\). A part with \(n_i>t\) is either full, contributing \(x^{n_i}\), or is non-full with exactly \(t\) selected vertices, contributing \(\binom{n_i}{t}x^t\). Therefore \(P_t(x)\) counts all selections compatible with common partial occupancy \(t\), including the all-full set.

Every proper fair dominating set has at least one non-full part, so its common occupancy \(t\) is uniquely determined and it occurs in exactly one \(P_t\). The all-full set occurs in every \(P_t\), so after summing the \(L\) products it must be reduced from multiplicity \(L\) to multiplicity one, giving the correction \(-(L-1)x^N\). For \(t=0\), choosing the non-full option in every part also produces the empty set, which is not dominating; subtracting \(1\) removes it. This yields the displayed formula.

Finally let \(m=\min_i n_i\). Taking an entire smallest part gives a fair dominating set of size \(m\), while taking one vertex from every part gives a fair dominating set of size \(r\). Hence \(\operatorname{fd}(G)\le\min\{m,r\}\). Conversely, for any proper fair dominating set with common partial occupancy \(t\), if \(t=0\) then at least one part is full, so \(|D|\ge m\); if \(t\ge1\), every part contributes at least one selected vertex, so \(|D|\ge r\). The full set is larger than both lower bounds. Therefore \(\operatorname{fd}(G)=\min\{m,r\}\).

## Verification
The accompanying checker independently constructs every nondecreasing complete-multipartite profile of total order at most \(9\). It tests every vertex subset against the literal fair-domination definition, compares that result with the structural criterion above, expands the displayed polynomial coefficient-by-coefficient, and checks the formula for \(\operatorname{fd}(G)\). The finite census is a regression check only; the infinite statement is proved symbolically above.

## Relationship to prior work
Caro, Hansberg, and Henning introduced \(k\)-fair and fair domination and explicitly adopt the vacuous convention that \(V(G)\) is \(k\)-fair. Their paper also records \(\operatorname{fd}(K_{m,n})=\gamma(K_{m,n})\), so the scalar complete-bipartite minimum is prior work. The first public arXiv version is dated 2011-09-06 and lists MSC 05C69.

Alikhani and Safazadeh later defined the fair domination polynomial and counted fair dominating sets for several families. Their complete-bipartite treatment is for the balanced family \(K_{n,n}\). Its structural cases agree with the specialization of the theorem here: when neither part is full, the two selected occupancies must coincide; otherwise one part is full and the other may be partially selected. Their inspected full text does not contain an arbitrary complete-multipartite theorem.

The terminology also overlaps with \([k,k]\)-domination: a \(k\)-fair dominating set is a dominating set for which every outside vertex has exactly \(k\) selected neighbors. Searches under that equivalent terminology did not reveal an arbitrary complete-multipartite all-set formula or polynomial.

## Limitations
The literature search cannot exclude a poorly indexed source or a result stated only in an uncommon equivalent terminology. The originality assessment therefore concerns the inspected literature and targeted searches, not a proof of global uniqueness. The computational verification is exhaustive only through order \(9\) and is not used as an infinite proof.

## References
1. Y. Caro, A. Hansberg, M. A. Henning, “Fair Domination in Graphs,” arXiv:1109.1150v1 (2011); later Discrete Mathematics 312 (2012), 2905–2914, DOI 10.1016/j.disc.2012.05.006.
2. S. Alikhani, M. Safazadeh, “On the number of fair dominating sets of graphs,” arXiv:2107.10671v1 (2021).
3. M. Chellali, T. W. Haynes, S. T. Hedetniemi, A. McRae, “[1, 2]-sets in graphs,” Discrete Applied Mathematics 161 (2013), 2885–2893, DOI 10.1016/j.dam.2013.06.012.
