# All restrained dominating sets and the restrained domination polynomial of chain graphs

## Finding
Let \(G\) be a connected chain graph with bipartition \(A\cup B\). Merge vertices with equal open neighborhoods into nonempty canonical twin classes
\[
A_1,\ldots,A_p,\qquad B_1,\ldots,B_p,
\]
ordered so that a vertex of \(A_i\) is adjacent to a vertex of \(B_j\) exactly when \(j\le i\). Put \(\alpha_i=|A_i|\), \(\beta_i=|B_i|\), and \(N=|V(G)|\).

For a restrained dominating set \(S\), write \(T=V(G)\setminus S\). If \(T\ne\varnothing\), then \(T\) is the complement of a restrained dominating set if and only if it meets both sides and, for the uniquely determined indices
\[
a=\min\{i:T\cap A_i\ne\varnothing\},\qquad b=\max\{j:T\cap B_j\ne\varnothing\},
\]
both of the following hold:
\[
0<|T\cap(B_1\cup\cdots\cup B_a)|<|B_1\cup\cdots\cup B_a|,
\]
\[
0<|T\cap(A_b\cup\cdots\cup A_p)|<|A_b\cup\cdots\cup A_p|.
\]

Define
\[
E_m(y)=(1+y)^m-1,\qquad P_m(y)=(1+y)^m-1-y^m.
\]
Also write
\[
\alpha_{>a}=\sum_{i>a}\alpha_i,\quad \alpha_{\ge b}=\sum_{i\ge b}\alpha_i,\quad \alpha_{(a,b)}=\sum_{a<i<b}\alpha_i,
\]
and analogously
\[
\beta_{<b}=\sum_{j<b}\beta_j,\quad \beta_{\le a}=\sum_{j\le a}\beta_j,\quad \beta_{(a,b)}=\sum_{a<j<b}\beta_j.
\]
For \(1\le a,b\le p\), define
\[
F^A_{a,b}(y)=
\begin{cases}
E_{\alpha_a}(y)(1+y)^{\alpha_{>a}},&b<a,\\
E_{\alpha_a}(y)(1+y)^{\alpha_{>a}}-y^{\alpha_{\ge a}},&b=a,\\
E_{\alpha_a}(y)(1+y)^{\alpha_{(a,b)}}P_{\alpha_{\ge b}}(y),&a<b,
\end{cases}
\]
and
\[
F^B_{a,b}(y)=
\begin{cases}
(1+y)^{\beta_{<b}}E_{\beta_b}(y),&b<a,\\
(1+y)^{\beta_{<b}}E_{\beta_b}(y)-y^{\beta_{\le b}},&b=a,\\
P_{\beta_{\le a}}(y)(1+y)^{\beta_{(a,b)}}E_{\beta_b}(y),&a<b.
\end{cases}
\]
Then the exact complement enumerator is
\[
Q_G(y)=1+\sum_{a=1}^{p}\sum_{b=1}^{p}F^A_{a,b}(y)F^B_{a,b}(y),
\]
and therefore the restrained domination polynomial is
\[
D_r(G;x)=x^NQ_G(x^{-1}).
\]
In particular, \(\gamma_r(G)=N-\deg Q_G\), and the number of minimum restrained dominating sets is the coefficient of \(y^{\deg Q_G}\) in \(Q_G(y)\).

## Assumptions and scope
All graphs are finite, simple, and undirected. The graph is assumed connected; hence every canonical twin class above is nonempty and the displayed staircase adjacency describes the full graph. A restrained dominating set \(S\subseteq V(G)\) means that every vertex of \(V(G)\setminus S\) has at least one neighbor in \(S\) and at least one neighbor in \(V(G)\setminus S\). The empty complement \(T=\varnothing\), corresponding to \(S=V(G)\), is valid and contributes the initial \(1\) to \(Q_G\).

The theorem concerns enumeration of all restrained dominating sets. The already known minimum restrained domination number of chain graphs is not presented as new; it is recovered as the least degree of \(D_r(G;x)\).

## Proof
Fix \(S\subseteq V(G)\) and put \(T=V(G)\setminus S\). The restrained condition says exactly that every vertex of \(T\) has a neighbor in \(S\) and a neighbor in \(T\). If \(T\ne\varnothing\), the second requirement forces \(T\) to meet both bipartition sides.

Assume therefore that \(T\cap A\ne\varnothing\) and \(T\cap B\ne\varnothing\), and define \(a\) and \(b\) as in the finding. Every vertex of \(T\cap A_i\) has \(i\ge a\), and its neighborhood is \(B_1\cup\cdots\cup B_i\). Hence, if the prefix \(B_1\cup\cdots\cup B_a\) contains at least one vertex of \(T\) and at least one vertex of \(S\), then every vertex of \(T\cap A\) has both a \(T\)-neighbor and an \(S\)-neighbor. Conversely, a vertex of \(T\cap A_a\) can have both kinds of neighbors only if this same prefix contains at least one vertex of each kind. Thus the restrained condition on all vertices of \(T\cap A\) is equivalent to
\[
0<|T\cap(B_1\cup\cdots\cup B_a)|<|B_1\cup\cdots\cup B_a|.
\]

Dually, every vertex of \(T\cap B_j\) has \(j\le b\), and its neighborhood is \(A_j\cup\cdots\cup A_p\). A vertex of \(T\cap B_b\) shows necessity, while nesting shows sufficiency, of
\[
0<|T\cap(A_b\cup\cdots\cup A_p)|<|A_b\cup\cdots\cup A_p|.
\]
This proves the structural characterization, including necessity and sufficiency.

It remains to count complements with their unique pair \((a,b)\). The \(A\)- and \(B\)-choices are independent once \((a,b)\) is fixed. For the \(A\)-side, \(T\cap A_a\) must be nonempty. If \(b<a\), the suffix condition is automatically proper because every class \(A_b,\ldots,A_{a-1}\) lies in \(S\), giving \(E_{\alpha_a}(y)(1+y)^{\alpha_{>a}}\). If \(b=a\), the sole forbidden choice is taking all of \(A_a\cup\cdots\cup A_p\), giving the subtraction \(y^{\alpha_{\ge a}}\). If \(a<b\), the classes strictly between \(a\) and \(b\) are arbitrary while the suffix \(A_b\cup\cdots\cup A_p\) must be a nonempty proper subset, giving the third case for \(F^A_{a,b}\).

The \(B\)-side is symmetric. If \(b<a\), the prefix condition is automatically proper because \(B_{b+1},\ldots,B_a\) lies in \(S\); if \(b=a\), exactly the full prefix is forbidden; and if \(a<b\), the prefix \(B_1\cup\cdots\cup B_a\) must be a nonempty proper subset. These are exactly the three displayed cases for \(F^B_{a,b}\).

The pair \((a,b)\) is uniquely determined by every nonempty valid complement, so summing \(F^A_{a,b}F^B_{a,b}\) causes no double counting. Adding the empty complement proves the formula for \(Q_G\). Finally, replacing a complement of size \(k\) by its restrained dominating set of size \(N-k\) gives \(D_r(G;x)=x^NQ_G(x^{-1})\).

## Verification
The standalone verifier constructs every canonical chain graph with \(1\le p\le4\), each twin-class size in \(\{1,2,3\}\), and total order at most \(11\). For every vertex subset it checks the restrained-domination definition directly, independently checks the prefix/suffix characterization, and compares the full complement-size coefficient vector with the closed formula.

Running `python3 verify.py` returns:

`VERIFY_OK profiles=540 subsets=687124 classification_checks=687124 coefficient_checks=5836 max_order=11`

This is a finite stress test, not a substitute for the proof above. It verifies all tested boundary cases, including singleton twin classes and the complete-bipartite case \(p=1\).

## Relationship to prior work
Pandey and Panda, *Some Algorithmic Results on Restrained Domination in Graphs* (arXiv:1606.02340v1, submitted 7 June 2016), devote Section 8 to chain graphs. Their Theorem 8.1 classifies the minimum restrained domination number using pendant vertices, stars, and bi-stars, and Theorem 8.2 gives a linear-time algorithm for one minimum restrained dominating set. That optimization result is prior coverage and is not claimed here.

Kanagavel, Kokilambal, and collaborators introduced/studied the restrained domination polynomial and, according to the accessible abstract of the 2019 paper, determined it for complete graphs, complete bipartite graphs, paths, cycles, and products involving \(K_2\). The complete-bipartite case is exactly the \(p=1\) specialization of the formula above and is therefore also prior coverage, not an originality claim.

Later work gives restrained domination polynomials for cycles and for join/corona constructions. Those statements do not cover arbitrary chain graphs: connected chain graphs can have arbitrarily many distinct nested neighborhood classes, and already \(P_4\) is a chain graph outside a nontrivial join decomposition. The present statement adds an all-set structural classification and an explicit coefficient enumerator for the entire chain-graph class.

## Limitations
The theorem is restricted to connected chain graphs in canonical nested-neighborhood form. It does not enumerate restrained dominating sets in arbitrary bipartite, chordal-bipartite, convex-bipartite, or threshold graphs. The polynomial formula is exact but is presented as a double sum over boundary indices rather than as a claimed irreducible factorization.

The 2019 polynomial paper was not available in full text from the lawful sources inspected here; its accessible abstract explicitly lists complete bipartite graphs but not general chain graphs. A 2020 article titled *A Study on Restrained Domination Polynomial in Graphs* was located only through abstract/search metadata during this review. These access limitations are retained as bibliographic risks rather than used as negative evidence.

## References
1. A. Pandey and B. S. Panda, *Some Algorithmic Results on Restrained Domination in Graphs*, arXiv:1606.02340v1, 2016.
2. K. Kanagavel and G. Kokilambal, *Restrained domination polynomial in graphs*, Journal of Discrete Mathematical Sciences and Cryptography 22(5), 761-775, 2019, DOI:10.1080/09720529.2019.1681693.
3. S. Velmurugan and R. Kala, *Restrained Domination Polynomial of Cycles*, Palestine Journal of Mathematics 12 (Special Issue II), 58-64, 2023.
4. *Restrained domination polynomial of join and corona of graphs*, Discrete Mathematics, Algorithms and Applications, DOI:10.1142/S179383092250118X.
