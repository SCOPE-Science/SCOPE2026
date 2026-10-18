# Zero-forcing polynomials of complements of paths and cycles

## Finding

For each integer \(n\ge5\), write \(P_n\) and \(C_n\) for the simple path and cycle on \(n\) vertices, and \(\overline{H}\) for the complement of a graph \(H\). The ordinary zero-forcing polynomial is
\[
\mathcal Z(G;z)=\sum_{B\subseteq V(G),\ B\text{ zero forcing}}z^{|B|}.
\]
Both complementary families have ordinary zero-forcing number \(n-3\), but their complete polynomials differ:
\[
\boxed{\mathcal Z(\overline{P_n};z)=(n^2-6n+10)z^{n-3}+\binom n2z^{n-2}+nz^{n-1}+z^n,}
\]
\[
\boxed{\mathcal Z(\overline{C_n};z)=(n(n-4)+2\mathbf 1_{\{n=6\}})z^{n-3}+\binom n2z^{n-2}+nz^{n-1}+z^n.}
\]
In particular, completing the path to a cycle removes one edge from its complement and changes precisely the minimum-degree coefficient:
\[
\boxed{\mathcal Z(\overline{C_n};z)-\mathcal Z(\overline{P_n};z)=(2n-10+2\mathbf 1_{\{n=6\}})z^{n-3}.}
\]
This difference is zero at \(n=5\) and strictly positive for every \(n\ge6\).

A complete description of the minimum forcing sets accompanies the formulas: a subset \(B\) of order \(n-3\) is zero forcing in \(\overline H\), with \(H\in\{P_n,C_n\}\), **if and only if** its three-vertex complement \(W=V(H)\setminus B\) contains both neighbors in \(H\) of some degree-two vertex \(v\notin W\). Moreover, every subset of order at least \(n-2\) is zero forcing; no subset of order at most \(n-4\) is zero forcing.

## Assumptions and scope

All graphs are finite, simple, and undirected. A vertex initially colored blue can force its unique white neighbor to become blue; blue vertices remain blue. A blue set is zero forcing if a sequence of such color changes makes all vertices blue. The polynomial counts labeled vertex subsets, not forcing sequences. In the cycle case indices are taken modulo \(n\). The assertions concern precisely \(n\ge5\); smaller orders have different boundary behavior. In the path case the endpoint vertices have one path neighbor, all other vertices have two.

## Proof

**Initial-force obstruction.** Fix \(H=P_n\) or \(C_n\), put \(G=\overline H\), and let \(W\) be the initial white set of cardinality \(r\). For any initially blue vertex \(v\),
\[
|N_G(v)\cap W|=r-|N_H(v)\cap W|\ge r-2.
\]
If \(r\ge4\), no blue vertex has exactly one white neighbor. Thus no forcing is possible, proving that every forcing set contains at least \(n-3\) vertices.

**Pairs of whites.** For distinct vertices \(u,w\) of either \(P_n\) or \(C_n\), with \(n\ge5\), there is a vertex \(v\notin\{u,w\}\) adjacent in \(H\) to exactly one of \(u,w\). Indeed, the two sets \(N_H(u)\setminus\{w\}\) and \(N_H(w)\setminus\{u\}\) are distinct: this follows by comparing endpoint versus interior neighborhoods in a path, or the two distinct cyclic predecessor/successor neighborhoods in a cycle of order at least five. Therefore \(v\) is adjacent in \(G\) to exactly the other member of \(\{u,w\}\), and forces it. The final white vertex has a blue neighbor because \(G\) has minimum degree at least two for \(n\ge5\), hence is forced. Thus every initial set with exactly two white vertices succeeds. The cases with one or zero white vertices also succeed.

**Three whites.** If \(|W|=3\), an initially blue vertex can force if and only if it has exactly two neighbors inside \(W\) in \(H\). Such a vertex has degree two in \(H\), and its *entire* path/cycle neighborhood lies in \(W\). Conversely, if some \(v\notin W\) has \(N_H(v)\subseteq W\) and \(|N_H(v)|=2\), it forces the unique third white vertex in \(G\); exactly two white vertices remain, and the preceding paragraph completes the process. If there is no such center, no initial force can occur. This proves the necessary and sufficient structural classification.

**Path count.** Number incidences \((v,W)\), where \(v\) is an internal path vertex, \(v\notin W\), \(|W|=3\), and \(N_{P_n}(v)\subseteq W\). There are \(n-2\) choices for \(v\) and \(n-3\) choices for the third white vertex, hence \((n-2)(n-3)\) incidences. A triple is counted twice exactly when it has the form \(\{i,i+2,i+4\}\), with \(0\le i\le n-5\); there are \(n-4\) such triples. No triple has three eligible centers. Subtracting this single excess gives
\[
(n-2)(n-3)-(n-4)=n^2-6n+10.
\]

**Cycle count and exceptional order.** For a cycle there are \(n(n-3)\) center/triple incidences. For \(n=5\) and \(n\ge7\), precisely \(n\) triples have two eligible centers, of the cyclic form \(\{i,i+2,i+4\}\), and every other eligible triple has just one; this produces \(n(n-3)-n=n(n-4)\). For \(n=6\), the two alternating triples \(\{0,2,4\}\) and \(\{1,3,5\}\) have *three* eligible centers each; all other eligible triples have one. Consequently the count is \(6(6-3)-2(3-1)=14\), equal to \(n(n-4)+2\) at \(n=6\). The overlap classifications follow because two distinct degree-two cycle vertices have neighbor pairs sharing a vertex only when their cyclic distance is two, and three such centers share a three-vertex set only in the six-cycle alternating configuration.

**Remaining polynomial coefficients.** Every \((n-2)\)-set, every \((n-1)\)-set, and the full vertex set is zero forcing by the pair argument, giving coefficients \(\binom n2\), \(n\), and \(1\), respectively. Lower coefficients vanish by the initial-force obstruction. Substitution yields both displayed polynomials. Their difference simplifies to the third displayed formula. This completes the proof.

## Verification

The accompanying standalone file `verify.py` constructs complements from first principles, simulates ordinary zero forcing independently for every initially blue subset for both graph families and all orders \(5\le n\le14\), and checks every polynomial coefficient and the exact characterization of minimum sets. It tests 65,472 vertex subsets across 20 graph instances. Run `python3 verify.py` in a directory containing the script. The recorded output is in `verification_output.txt`. These computations independently test bounded examples; the unlimited domain is established by the preceding proof.

## Relationship to prior work

Curl, Fallat, Moruzzi, Reinhart, and Young (2022) establish the **scalar zero-forcing number** for complements of nonstar trees and relevant unicyclic graphs, including the two values \(Z(\overline{P_n})=Z(\overline{C_n})=n-3\). Their lower-bound and existence arguments do not count or classify all minimum forcing sets and do not give the two full polynomial formulas. Boyer and collaborators (2018) introduce the zero-forcing polynomial and establish general high-degree coefficients and polynomials for ordinary paths and cycles; results for \(P_n\) and \(C_n\) themselves must not be confused with results for their complements. The present formulas refine the known scalar numbers to complete enumerations, identify the exceptional six-cycle count, and quantify the effect of deleting the closing complementary edge while preserving the minimum number.

## Limitations

The statement applies only to complement graphs of the path and cycle families, not to arbitrary graphs or complements of general trees or unicyclic graphs. No general formula for complements of other bounded-degree graphs is asserted. Bibliographic searches and inspected primary sources have not established priority exhaustively; unindexed or otherwise overlooked equivalent enumeration is possible. The checks described here are finite, and an independent scientific audit has not been performed.

## References

1. E. Curl, S. Fallat, R. Moruzzi Jr, C. Reinhart, and D. Young, *On the zero forcing number of the complement of graphs with forbidden subgraphs*, arXiv:2206.03932, first submitted 8 June 2022. https://arxiv.org/abs/2206.03932
2. K. Boyer, B. Brimkov, S. English, C. Ferrero, A. Keller, A. Kirsch, and others, *The zero forcing polynomial of a graph*, arXiv:1801.08910, first submitted 26 January 2018. https://arxiv.org/abs/1801.08910
3. L. Eroh, C. X. Kang, and E. Yi, *On Zero Forcing Number of Graphs and Their Complements*, arXiv:1402.1962. https://arxiv.org/abs/1402.1962
