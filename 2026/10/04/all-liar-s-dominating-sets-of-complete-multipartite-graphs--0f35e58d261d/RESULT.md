# All liar's dominating sets of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with nonempty parts \(V_1,\ldots,V_r\), where \(r\ge2\) and \(N=\sum_{i=1}^r n_i\ge3\). For a set \(S\subseteq V(G)\), write \(s=|S|\) and \(s_i=|S\cap V_i|\).

A set \(S\) is liar's dominating if and only if
\[
s\ge3
\quad\text{and}\quad
n_i\ge s\Longrightarrow s_i\le s-3\qquad(1\le i\le r).
\]
Equivalently, for \(3\le s\le N\), define
\[
c_i(s)=\begin{cases}
n_i,&n_i<s,\\
s-3,&n_i\ge s.
\end{cases}
\]
Then the liar's dominating sets of cardinality \(s\) are exactly the vertex sets with profile \((s_1,\ldots,s_r)\) satisfying \(0\le s_i\le c_i(s)\) and \(\sum_i s_i=s\).

Therefore the exact cardinality enumerator is
\[
L_G(x)=\sum_{s=3}^N
\left([y^s]\prod_{i=1}^r\sum_{j=0}^{c_i(s)}\binom{n_i}{j}y^j\right)x^s.
\]
In particular,
\[
\gamma_{LR}(G)=\min\left\{s\in\{3,\ldots,N\}:\sum_{i=1}^r c_i(s)\ge s}\right\},
\]
and, if \(g=\gamma_{LR}(G)\), the number of minimum liar's dominating sets is
\[
[y^g]\prod_{i=1}^r\sum_{j=0}^{c_i(g)}\binom{n_i}{j}y^j.
\]

## Assumptions and scope
A liar's dominating set \(S\) satisfies two conditions: \(|N[v]\cap S|\ge2\) for every vertex \(v\), and \(|(N[u]\cup N[v])\cap S|\ge3\) for every two distinct vertices \(u,v\). The graph is simple and complete multipartite, every part is nonempty, and \(N\ge3\). No claim is made for disconnected graphs or for generalized distance-\(d\) liar domination.

The scalar complete-bipartite liar's domination number is prior work. The finding here is the all-set characterization for arbitrary complete multipartite graphs and the resulting exact enumerator; the scalar formula above is included as a consequence and specializes to the previously reported complete-bipartite cases.

## Proof
For \(v\in V_i\),
\[
N[v]=(V(G)\setminus V_i)\cup\{v\}.
\]
Put \(q_i=s-s_i=|S\setminus V_i|\) and \(t_i=n_i-s_i=|V_i\setminus S|\). The condition \(|N[v]\cap S|\ge2\) says \(q_i\ge2\) when \(v\notin S\), and \(q_i\ge1\) when \(v\in S\).

If \(u\) and \(v\) lie in different parts, then \(N[u]\cup N[v]=V(G)\), so the pair condition is exactly \(s\ge3\). If two distinct vertices lie in the same part \(V_i\), then
\[
N[u]\cup N[v]=(V(G)\setminus V_i)\cup\{u,v\}.
\]
Thus the pair condition requires \(q_i\ge3\) when two omitted vertices in \(V_i\) exist, \(q_i\ge2\) when one omitted and one selected vertex exist, and \(q_i\ge1\) when two selected vertices exist.

Now assume \(s\ge3\). If \(n_i<s\), then every possible profile in \(V_i\) automatically meets these local inequalities. Indeed, \(s-n_i\ge1\); if \(t_i=0\), then \(q_i=s-n_i\ge1\); if \(t_i=1\), then \(q_i=s-n_i+1\ge2\); and if \(t_i\ge2\), then \(q_i=s-n_i+t_i\ge3\).

If instead \(n_i\ge s\), liar domination forces \(q_i\ge3\). For \(q_i=0\), a selected vertex would have only itself from \(S\) in its closed neighborhood. For \(q_i=1\), at least one omitted vertex exists and its closed neighborhood meets \(S\) only once. For \(q_i=2\), at least two omitted vertices exist and the union of their closed neighborhoods meets \(S\) only twice. Conversely \(q_i\ge3\) satisfies every one-vertex and same-part pair inequality. Since \(q_i=s-s_i\), this is precisely \(s_i\le s-3\).

This proves the structural criterion. For fixed \(s\), choosing \(j\) vertices from part \(V_i\) contributes \(\binom{n_i}{j}y^j\), and the criterion allows exactly \(0\le j\le c_i(s)\). Multiplication over the parts and extraction of \([y^s]\) therefore gives the coefficient of \(x^s\) in \(L_G(x)\).

Finally, a profile with total \(s\) and bounds \(0\le s_i\le c_i(s)\) exists if and only if \(\sum_i c_i(s)\ge s\): necessity is immediate, and sufficiency follows by greedily distributing \(s\) indistinguishable profile units among the integral capacities. Taking the least feasible \(s\) proves the formula for \(\gamma_{LR}(G)\), and the coefficient formula at \(s=g\) counts all minimum sets.

## Verification
The accompanying `verify.py` constructs every ordered positive complete-multipartite profile of total order from \(3\) through \(9\). For every vertex subset it checks the literal two defining liar-domination conditions using closed neighborhoods and independently checks the capacity criterion above. It also reconstructs every polynomial coefficient from the capacity products and compares the resulting minimum cardinality.

A replay from the packaged artifact returns `VERIFY_OK profiles=501 subset_checks=173736 coefficient_checks=4551 gamma_checks=501 max_order=9`.

This finite replay is a stress test of the proof, not a proof of the infinite theorem.

## Relationship to prior work
Slater introduced liar's domination and motivated the fault-tolerant location model; the publisher record gives a first-publication date of 13 February 2009. Roden and Slater subsequently studied the parameter and obtained scalar formulas for complete bipartite graphs. A later generalized-liar paper explicitly summarizes those complete-bipartite scalar cases. The present scalar formula is therefore not asserted as new on the bipartite subfamily.

Canoy and Balandra give a full characterization for liar's dominating sets in the join of two nontrivial connected graphs. Their theorem is broader in one direction but does not directly cover the multipartite decomposition into independent parts of size greater than one, because those factors are disconnected. Their full text also records primary MSC 05C69 for this topic.

The new content retained here is the direct complete-multipartite all-set criterion, its exact cardinality enumerator, and the induced minimum-set count for arbitrary numbers and sizes of parts.

## Limitations
The primary full text of Roden and Slater's 2009 paper was not available in the inspected lawful sources. Later full-text literature reports its complete-bipartite scalar formulas, which are treated as prior-covered; it does not report an arbitrary complete-multipartite all-set enumerator. This access gap remains a bibliographic residual risk.

The finding concerns ordinary distance-one liar domination only. It does not classify generalized \((m,\ell)\)-liar domination, connected liar domination, total liar domination, or other fault-tolerant domination variants.

## References
P. J. Slater, “Liar's domination,” *Networks* 54 (2009), 70–74. DOI: 10.1002/net.20295. First published 13 February 2009.

M. L. Roden and P. J. Slater, “Liar's domination in graphs,” *Discrete Mathematics* 309 (2009), 5884–5890. DOI: 10.1016/j.disc.2008.07.019.

S. R. Canoy Jr. and C. B. Balandra, “Liar's domination in graphs under some operations,” *Tamkang Journal of Mathematics* 48 (2017), 49–59. DOI: 10.5556/j.tkjm.48.2017.2188.

S. K. Jena, R. K. Jallu, and G. K. Das, “Generalized Liar's Dominating Set in Graphs,” arXiv:1907.11416 (2019).
