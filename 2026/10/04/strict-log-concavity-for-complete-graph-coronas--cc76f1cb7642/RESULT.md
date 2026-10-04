# Strict log-concavity for complete-graph coronas
## Finding
For every integer \(n\ge2\), let \(H_n=K_n\circ K_1\), with core vertices \(v_1,\ldots,v_n\) and pendant mates \(v'_1,\ldots,v'_n\). A set \(S\subseteq V(H_n)\) with \(|S|\ge3\) is in general position if and only if \(|S\cap\{v_i,v'_i\}|\le1\) for every \(i\). Hence its general position polynomial is \[\psi(H_n;x)=(1+2x)^n+n x^2.\] Moreover the coefficient sequence of \(\psi(H_n;x)\) is strictly log-concave, and therefore unimodal. Thus the corona-unimodality question has an affirmative answer for complete-graph bases, and in this family the stronger log-concavity property is preserved.

## Assumptions and scope
All graphs are finite, simple, and undirected. For \(n\ge2\), let \(H_n=K_n\circ K_1\). Write the vertices of the core clique as \(v_1,\ldots,v_n\), and let \(v'_i\) be the unique pendant neighbor of \(v_i\). A vertex set is in general position when no selected vertex lies on a shortest path between two other selected vertices. The general position polynomial \(\psi(H_n;x)\) counts general position sets by cardinality.

## Proof
Every set of at most two vertices is in general position.

Let \(|S|\ge3\). First suppose that both \(v_i\) and \(v'_i\) lie in \(S\). Choose any third vertex \(w\in S\setminus\{v_i,v'_i\}\). Every shortest path from \(v'_i\) to \(w\) starts with the edge \(v'_iv_i\), so \(v_i\) is an internal vertex of a \(v'_i,w\)-geodesic. Hence \(S\) is not in general position. Therefore every general position set of size at least three contains at most one vertex from each pendant pair \(\{v_i,v'_i\}\).

Conversely, suppose that \(S\) contains at most one vertex from every pendant pair. Shortest paths in \(H_n\) have the following forms. Two distinct core vertices are adjacent. A pendant vertex \(v'_i\) and a different core vertex \(v_j\) have the unique geodesic \(v'_i,v_i,v_j\). Two pendant vertices \(v'_i,v'_j\), with \(i\ne j\), have the unique geodesic \(v'_i,v_i,v_j,v'_j\). Thus every internal vertex of a geodesic whose endpoints lie in \(S\) is the core mate of a selected pendant endpoint. Such a mate is absent from \(S\) by hypothesis. Hence no selected vertex lies internally on a geodesic between two other selected vertices, and \(S\) is in general position.

For \(k\ge3\), a general position \(k\)-set is therefore obtained by choosing \(k\) of the \(n\) pendant pairs and then choosing one of the two vertices from each chosen pair. Hence there are \(2^k\binom{n}{k}\) such sets. For \(k=0,1,2\), all subsets are in general position. Therefore
\[
\psi(H_n;x)=1+2nx+\binom{2n}{2}x^2+\sum_{k=3}^n 2^k\binom{n}{k}x^k
=(1+2x)^n+n x^2.
\]

Write \(a_k=[x^k]\psi(H_n;x)\). Then
\[
a_0=1,\qquad a_1=2n,\qquad a_2=n(2n-1),\qquad
a_k=2^k\binom{n}{k}\quad (k\ge3).
\]
For the only indices affected by the extra \(n x^2\) term,
\[
a_1^2-a_0a_2=2n^2+n>0,
\]
\[
a_2^2-a_1a_3=\frac{n^2}3(4n^2+12n-13)>0
\]
whenever the \(a_3\) term is present, and
\[
a_3^2-a_2a_4=
\frac{2n^2(n-1)(n-2)}9(2n^2-3n+7)>0
\]
whenever the \(a_4\) term is present. All remaining log-concavity inequalities are those of the strictly log-concave scaled binomial sequence \(2^k\binom{n}{k}\). The cases \(n=2,3\) are contained in the same coefficient formula and are immediate. Hence the full coefficient sequence is strictly log-concave, and therefore unimodal.

## Verification
The included checker constructs \(H_n\) from its adjacency list, computes all-pairs graph distances by breadth-first search, and identifies forbidden triples solely from the metric equality defining a vertex lying on a geodesic. It then examines every vertex subset for \(2\le n\le10\), compares the complete size distribution with the closed formula, and checks strict log-concavity.

## Relationship to prior work
The 2024 paper introducing general position polynomials asks whether unimodality of \(\psi(G)\) implies unimodality of \(\psi(G\circ K_1)\). It proves the implication for path bases through the comb family. A 2026 follow-up studies the same corona question, proves positive cases for edgeless graphs and paths, and shows that log-concavity is not preserved in general by giving \(C_6\circ K_1\) as a counterexample. The complete-graph base family is not among the positive corona families stated there.

Earlier work on general position numbers proves \(\operatorname{gp}(G\circ H)=|V(G)|\rho(H)\) for connected \(G\) of order at least two. Specializing to \(H=K_1\) gives \(\operatorname{gp}(K_n\circ K_1)=n\), which agrees with the degree of the polynomial above but does not determine its coefficients.

The present result supplies both the exact polynomial and a strict log-concavity proof for complete-graph bases, giving a new positive family for the corona-preservation program.

## Limitations
The result concerns only coronas of complete graphs with one pendant vertex attached to each core vertex. It does not settle the general corona-unimodality problem. The structural characterization is specific to the clique metric; for a general base graph, selected core vertices can lie on geodesics corresponding to geodesics in the base. The exhaustive computation through \(n=10\) is corroborative only; the all-orders theorem follows from the proof.

## References
1. V. Iršič, S. Klavžar, G. Rus, J. Tuite, “General Position Polynomials,” Results in Mathematics 79 (2024), 110, DOI 10.1007/s00025-024-02133-3; arXiv:2401.05696v1.
2. M. Ghorbani, H. R. Maimani, M. Momeni, F. Rahimi Mahid, S. Klavžar, G. Rus, “The General Position Problem on Kneser Graphs and on Some Graph Operations,” Discussiones Mathematicae Graph Theory 41 (2021), 1199–1213, DOI 10.7151/dmgt.2269; arXiv:1903.04286.
3. B. A. Rather, “Explicit Formulas and Unimodality Phenomena for General Position Polynomials,” arXiv:2603.06930v1 (2026).
