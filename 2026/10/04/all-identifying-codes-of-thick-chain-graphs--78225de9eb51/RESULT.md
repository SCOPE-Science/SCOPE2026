# All identifying codes of thick chain graphs
## Finding
Let \(G\) be a finite connected chain graph with canonical nonempty open-neighborhood twin classes \(A_1,\ldots,A_p,B_1,\ldots,B_p\), where a vertex of \(A_i\) is adjacent to a vertex of \(B_j\) exactly when \(j\le i\), and suppose every canonical class has size at least \(2\). Then, unless \(G\cong K_{2,2}\), a set \(C\subseteq V(G)\) is an identifying code if and only if it omits at most one vertex from every canonical class. Consequently, writing \(\alpha_i=|A_i|\), \(\beta_i=|B_i|\), and \(N=|V(G)|\), its identifying-code polynomial \(I_G(x)=\sum_C x^{|C|}\) is \[I_G(x)=\prod_{i=1}^p\bigl(x^{\alpha_i}+\alpha_i x^{\alpha_i-1}\bigr)\bigl(x^{\beta_i}+\beta_i x^{\beta_i-1}\bigr).\] Thus \(\gamma_{ID}(G)=N-2p\) and the number of minimum identifying codes is \(\prod_{i=1}^p\alpha_i\beta_i\). For the unique exception \(K_{2,2}\), the four two-vertex cross-part sets fail to separate their endpoints, so \(I_G(x)=x^4+4x^3\) and \(\gamma_{ID}(G)=3\).

Here an identifying code is a set \(C\subseteq V(G)\) for which every closed-neighborhood trace \(N[v]\cap C\) is nonempty and the traces are pairwise distinct. The qualifier “thick” is shorthand only for the explicit hypothesis that every canonical open-neighborhood twin class has size at least \(2\).

## Assumptions and scope
The graph is finite, simple, connected, and bipartite. Its chain ordering is encoded by nonempty classes \(A_1,\ldots,A_p\) and \(B_1,\ldots,B_p\), with adjacency \(A_iB_j\) exactly for \(j\le i\). Each class has size at least \(2\). No assertion is made for chain graphs having singleton canonical classes.

The enumerator is defined by
\[
I_G(x)=\sum_{C\subseteq V(G):\ C\text{ is an identifying code}}x^{|C|}.
\]

## Proof
Vertices inside a fixed canonical class are false twins: they are nonadjacent and have the same open neighborhood. If distinct vertices \(u,v\) of one class were both omitted from an identifying code \(C\), then
\[
N[u]\cap C=N(u)\cap C=N(v)\cap C=N[v]\cap C,
\]
so they would not be separated. Hence every identifying code omits at most one vertex from each canonical class.

Conversely, suppose \(C\) omits at most one vertex from every canonical class. Since every class has size at least \(2\), every class contains a code vertex. Thus every \(A\)-vertex is dominated from \(B_1\), and every \(B\)-vertex is dominated from \(A_p\).

Two vertices in the same class are separated because at least one lies in \(C\). If \(i<k\), any code vertex in \(B_k\) separates \(A_i\) from \(A_k\). If \(j<\ell\), any code vertex in \(A_j\) separates \(B_j\) from \(B_\ell\).

For \(a\in A_i\) and \(b\in B_j\), if \(j>i\), a code vertex of \(B_1\) is adjacent to \(a\) and not to \(b\). If \(j\le i\) and \(j>1\), the same choice works. If \(j=1\) and \(i<p\), a code vertex of \(A_p\) is adjacent to \(b\) and not to \(a\). If \(j=1\), \(i=p\), and \(p>1\), a code vertex of \(B_2\) is adjacent to \(a\) and not to \(b\).

The only remaining case is \(p=1\), so \(G\cong K_{\alpha_1,\beta_1}\). Equality of the traces of a cross-part pair \(a,b\) can occur only when \(C\cap A_1=\{a\}\) and \(C\cap B_1=\{b\}\). Under the all-but-one condition and \(\alpha_1,\beta_1\ge2\), this forces \(\alpha_1=\beta_1=2\). Hence the only failures are the four two-vertex cross-part sets in \(K_{2,2}\).

For a nonexceptional graph, a class of size \(s\) contributes either all \(s\) vertices, with weight \(x^s\), or all but one, with \(s\) choices and weight \(s x^{s-1}\). Multiplying over all \(2p\) classes gives the formula. The least degree is \(N-2p\) with coefficient \(\prod_i\alpha_i\beta_i\). For \(K_{2,2}\), subtracting the four forbidden degree-two sets from \((x^2+2x)^2\) gives \(x^4+4x^3\).

## Verification
The accompanying `verify.py` constructs all canonical chain profiles with \(p\le3\), class sizes in \(\{2,3\}\), and order at most \(14\), and checks every vertex subset against the closed-neighborhood definition and the theorem. It also checks complete-bipartite profiles \(K_{a,b}\) with \(2\le a,b\le5\) and order at most \(12\). Exact replay output:

`VERIFY_OK profiles=58 subset_checks=323488 coefficient_checks=650 max_order=14`

This finite computation is corroborative only; the proof above establishes the infinite statement.

## Relationship to prior work
Karpovsky, Chakrabarty, and Levitin introduced identifying codes in 1998. Foucaud, Mertzios, Naserasr, Parreau, and Valicov use the same closed-neighborhood definition and, in their conclusion, say that the complexity on bipartite permutation graphs is not known and specifically point to chain graphs as a class where the metric-dimension approach might also work for Identifying Code. Their paper was published online on 14 July 2016 and does not state the all-code classification or enumerator proved here.

Targeted searches also used the aliases “Ferrers graph,” “2K2-free bipartite graph,” and “bipartite permutation graph,” together with identifying-code polynomial/enumerator terminology. No located source implied the stated theorem; search failure is not treated as novelty proof, and residual indexing risk is recorded in the review.

## Limitations
The theorem excludes canonical singleton classes. The factorization relies on every class retaining a selected witness after one omission, so it does not automatically extend to arbitrary chain graphs. The finite verifier is not an exhaustive proof over all orders.

## References
1. M. G. Karpovsky, K. Chakrabarty, and L. B. Levitin, “On a New Class of Codes for Identifying Vertices in Graphs,” *IEEE Transactions on Information Theory* 44(2), 599–611 (1998), DOI 10.1109/18.661507.
2. F. Foucaud, G. B. Mertzios, R. Naserasr, A. Parreau, and P. Valicov, “Identification, Location-Domination and Metric Dimension on Interval and Permutation Graphs. II. Algorithms and Complexity,” *Algorithmica* 78, 914–944 (2017), published online 14 July 2016, DOI 10.1007/s00453-016-0184-1.
