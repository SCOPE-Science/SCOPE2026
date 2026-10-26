# Minimal forts, zero-forcing polynomials, and a threefold integrality gap in crown graphs

## Finding
For every integer \(n\ge3\), let \(C_n^\star=K_{n,n}-M\) be the crown graph with vertex classes \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\) and edges \(a_i b_j\) precisely for \(i\ne j\). Its entire inclusion-minimal-fort hypergraph consists of

\[
\{\{a_i,a_j,a_k\}:i<j<k\}\;\cup\;\{\{b_i,b_j,b_k\}:i<j<k\}\;\cup\;\{\{a_i,a_j,b_i,b_j\}:i<j\}.
\]

Consequently there are \(2\binom n3\) three-vertex minimal forts and \(\binom n2\) four-vertex minimal forts. Its full zero-forcing polynomial, counting initial black sets according to cardinality, is

\[
\mathcal Z(C_n^\star;z)=\sum_{i=0}^{2}\sum_{j=0}^{2}\binom ni\binom nj z^{2n-i-j}-\binom n2 z^{2n-4}.
\]

In particular, \(Z(C_n^\star)=2n-4\), with exactly \(\binom n2(\binom n2-1)\) distinct minimum zero-forcing sets. For the fractional *fort-cover* relaxation introduced by Cameron–Hogben–Kenter–Mojallal–Schuerger,

\[
Z^*(C_n^\star)=\frac{2n}{3},\qquad \frac{Z(C_n^\star)}{Z^*(C_n^\star)}=3-\frac6n\longrightarrow3.
\]

The fractional optimum is uniquely the constant weight \(1/3\) at every vertex for \(n\ge4\); uniqueness does not hold at \(n=3\). Relative to \(K_{n,n}\), whose fractional and ordinary values are \(n\) and \(2n-2\), deleting one perfect matching decreases the fractional optimum by one third and produces an integrality ratio tending to three rather than two.

## Assumptions and scope
All graphs are finite, undirected, and simple. A *fort* is a nonempty vertex subset \(F\) such that no vertex outside \(F\) has exactly one neighbor in \(F\). Inclusion-minimality refers to nonempty proper subsets, not just single-vertex deletions. An initial vertex set is *zero forcing* if repeated application of the rule that a black vertex with exactly one white neighbor turns that neighbor black eventually colors every vertex black. The polynomial has one monomial for each distinct subset, not each forcing chronology. Fractional zero forcing \(Z^*\) means the LP on minimal forts \(\min\sum_v w_v\) subject to \(w_v\ge0\) and \(\sum_{v\in F}w_v\ge1\) for all minimal forts; it is **not** the alternative three-color-game fractional variant.

## Proof
Write \(P=\{i:a_i\in F\}\) and \(Q=\{i:b_i\in F\}\), with \(p=|P|\), \(q=|Q|\). For \(a_i\notin F\), the number of its neighbors in \(F\) is \(q-\mathbf1_{i\in Q}\); for \(b_i\notin F\), it is \(p-\mathbf1_{i\in P}\). These are the exact fort inequalities.

Every three vertices contained in one vertex class constitute a fort: each external opposite-class vertex has either two or three neighbors in the triple, while same-class vertices have zero. Every paired four-set \(\{a_i,a_j,b_i,b_j\}\) is also a fort: external vertices outside these two index positions have two neighbors in the opposite side. These forts are inclusion-minimal. A triple has no fort subset of smaller order because a 1- or 2-subset on one side leaves some opposite-side vertex with exactly one neighbor (using \(n\ge3\)); a paired four-set has no smaller fort subset as seen directly from the neighbor-count equations.

Conversely, if \(p\ge3\) or \(q\ge3\), then \(F\) contains a same-side triple and is inclusion-minimal only if it is that triple. Suppose \(p,q\le2\). If \(p=0\) and \(q\in\{1,2\}\), an outside \(a_i\) with \(i\in Q\) has \(q-1\in\{0,1\}\) opposite neighbors, and when \(q=1\) any outside \(a_j\) with \(j\ne i\) has one; when \(q=2\) the outside \(a_i\) above has one. Thus no such fort exists, and symmetrically for \(q=0\). If \(p=1\) and \(q\ge1\), any external \(b_i\) not paired with the unique selected \(a\) would have one selected neighbor, so all external \(B\)-vertices would need to be that one matched vertex. This forces \(q=n-1\le2\), hence \(n=3\), \(q=2\) and \(Q\) is the complement of \(P\); but then an outside \(a_i\) with \(i\in Q\) has exactly one neighbor in \(F\), contradiction. The symmetric argument rules out \(q=1\). Finally, \(p=q=2\): whenever \(i\in Q\setminus P\), the outside vertex \(a_i\) has exactly one selected neighbor; hence \(Q\subseteq P\), and equality follows from their equal sizes. This establishes the complete list.

A subset \(S\) is zero forcing exactly when it intersects every fort: if an unfilled fort remains, no initially black vertex can force its first member; conversely, when forcing stops with a nonempty white set, that white set is a fort. Therefore, the complement \(V\setminus S\) must contain no minimal fort. It can contain at most two vertices of each class; if it has two in each, their index pairs must differ, else it contains a paired four-set. These are sufficient as well. Choosing white sets of class sizes \(i,j\le2\) and subtracting the forbidden \(\binom n2\) aligned two-plus-two sets proves the polynomial. Its lowest degree is \(2n-4\); there are \(\binom n2^2-\binom n2\) admissible sets at that degree, positive for every \(n\ge3\).

For the fractional LP, sum the constraints for all \(\binom n3\) triple forts on side \(A\). Each \(a_i\) occurs \(\binom{n-1}{2}\) times, so \(\sum_i w(a_i)\ge \binom n3/\binom{n-1}{2}=n/3\). The same inequality on side \(B\) yields objective at least \(2n/3\). Constant weights \(w_v=1/3\) satisfy all triple-fort inequalities at equality and each four-set inequality with sum \(4/3\), proving optimality. If \(n\ge4\), at any optimum the sums on both sides must equal \(n/3\), forcing all triple constraints tight. Given any two vertices of one side, one may choose two others (since \(n\ge4\)); subtracting tight triple equations sharing those two vertices shows their weights are equal. Thus the unique optimizer has weights \(1/3\). For \(n=3\), there are nonconstant optimal assignments, e.g. assign weight \(1\) to \(a_1\) and \(b_2\), and zero elsewhere, which meets every minimal-fort constraint. The asymptotic ratio follows.

## Verification
Run `python verify.py` using Python 3.8 or newer. The standalone script enumerates every subset of \(C_n^\star\) for \(3\le n\le7\). Its fort test uses the definition; it verifies the proposed minimal forts have no fort proper subset, that every fort contains one of them, and independently simulates propagation for every potential forcing set against the claimed complement classification. It checks all total forcing-set counts and outputs `ALL CHECKS PASSED`. These finite enumerations corroborate the mathematical argument but are not its infinite proof.

## Relationship to prior work
Boyer et al. (2018) introduce the zero-forcing polynomial and determine it for complete multipartite graphs, cycles and other families, but do not cover matching-deleted complete bipartite graphs in their full-text enumeration. Cameron et al. (first public 2023) introduce the fort-hypergraph fractional relaxation and compute \(Z^*\) for complete bipartite graphs and hypercubes. The crown family is distinct from \(K_{n,n}\); its first two cases are \(C_6\) and the three-dimensional cube, so those isolated scalar values are already covered by their results. Their full article does not state the crown-family fort classification or polynomial. Duong et al. (2019) study selected bipartite circulants; their full text discusses scalar zero forcing but does not enumerate minimal forts or the crown-family fort-cover relaxation. The new scope is the full paired-fort structural classification and joint exact enumerative/integrality-gap statement, not the definitions or known special cases.

## Limitations
The graph family requires \(n\ge3\); for \(n=2\) the crown is disconnected and these formulas do not apply. This is a fort-cover fractional parameter, not skew or game fractional forcing. The claims have a mathematical proof and finite independent checks, but not an independent human audit. Priority overlap with other graph-theory sources not located by keyword or semantic searches cannot be completely excluded; the known \(n=3,4\) special cases and general complete-bipartite values are not claimed as original.

## References
1. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, C. Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910v1, first public 2018-01-26; https://arxiv.org/html/1801.08910v1.
2. T. R. Cameron, L. Hogben, F. H. J. Kenter, S. A. Mojallal, H. Schuerger, *Forts, (fractional) zero forcing, and Cartesian products of graphs*, arXiv:2310.17904v1, first public 2023-10-27; full HTML v3 at https://arxiv.org/html/2310.17904v3.
3. L. Duong, B. K. Kroschel, M. Riddell, K. N. Vander Meulen, A. Van Tuyl, *Maximum nullity and zero forcing of circulant graphs*, arXiv:1906.03079v1, first public 2019-06-07; https://arxiv.org/html/1906.03079v1.
