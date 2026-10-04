# Quasi-total Roman weight enumerator of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\) and \(N=\sum_i n_i\). A quasi-total Roman dominating function \(f:V(G)\to\{0,1,2\}\) belongs to exactly one of three families: (i) no vertex has label \(2\), in which case every vertex has label \(1\); (ii) label \(2\) occurs in exactly one part \(X_i\), in which case \(X_i\) has only labels \(1,2\), contains at least one \(2\), every other part has only labels \(0,1\), and at least one vertex outside \(X_i\) has label \(1\); or (iii) label \(2\) occurs in at least two distinct parts, in which case every ternary labeling with that property is valid. Consequently the weight enumerator is \[\mathcal Q_G(z)=z^N+\sum_i\big((z+z^2)^{n_i}-z^{n_i}\big)\big((1+z)^{N-n_i}-1\big)+(1+z+z^2)^N-(1+z)^N-\sum_i\big((1+z+z^2)^{n_i}-(1+z)^{n_i}\big)(1+z)^{N-n_i}.\] In particular the total number of quasi-total Roman dominating functions is \[1+\sum_i(2^{n_i}-1)(2^{N-n_i}-1)+3^N-2^N-\sum_i(3^{n_i}-2^{n_i})2^{N-n_i},\] and the minimum weight is \(\gamma_{qtR}(G)=\min\{N,\min_i n_i+2,4\}\).

## Assumptions and scope
All graphs are finite and simple. Let \(G=K_{n_1,\ldots,n_r}\) be connected, so \(r\ge2\), with partite classes \(X_1,\ldots,X_r\) and \(N=\sum_i n_i\). A quasi-total Roman dominating function is a function \(f:V(G)\to\{0,1,2\}\) such that every zero-labeled vertex has a neighbor labeled \(2\), and every vertex labeled \(2\) has a neighbor with positive label.

The polynomial \(\mathcal Q_G(z)=\sum_f z^{\omega(f)}\) sums over all quasi-total Roman dominating functions, where \(\omega(f)=\sum_v f(v)\).

## Proof
Let \(J\) be the set of part indices that contain at least one vertex labeled \(2\).

If \(J=\varnothing\), then no vertex may have label \(0\), because a zero would have no neighbor labeled \(2\). Hence every vertex has label \(1\), giving the term \(z^N\).

Suppose \(J=\{i\}\). A zero inside \(X_i\) would have no adjacent \(2\), because vertices of \(X_i\) are pairwise nonadjacent and there is no \(2\) outside \(X_i\). Thus every vertex of \(X_i\) has label \(1\) or \(2\), with at least one \(2\). Every vertex outside \(X_i\) has label \(0\) or \(1\). In addition, every \(2\) in \(X_i\) must have a positive neighbor, so at least one outside vertex must have label \(1\). Conversely these conditions are sufficient: each outside zero sees a \(2\) in \(X_i\), while each \(2\) in \(X_i\) sees the outside \(1\). The contribution of this family is therefore
\[
\big((z+z^2)^{n_i}-z^{n_i}\big)\big((1+z)^{N-n_i}-1\big).
\]

Finally suppose \(|J|\ge2\). Every zero-labeled vertex has a \(2\)-labeled neighbor in a different part, and every \(2\)-labeled vertex has a positive neighbor, indeed a \(2\), in another part. Hence every ternary labeling whose \(2\)-labels occupy at least two parts is valid. All ternary labelings contribute \((1+z+z^2)^N\). Those with no \(2\) contribute \((1+z)^N\). Those whose \(2\)-labels occur in exactly one part \(X_i\) contribute
\[
\big((1+z+z^2)^{n_i}-(1+z)^{n_i}\big)(1+z)^{N-n_i}.
\]
Subtracting these disjoint cases gives the final two terms of the displayed polynomial.

Setting \(z=1\) gives the stated total-function count.

For the minimum weight, the three families have minimum weights \(N\), \(n_i+2\), and \(4\), respectively. Minimizing over the unique-two part \(X_i\) yields
\[
\gamma_{qtR}(G)=\min\{N,\min_i n_i+2,4\}.
\]
For \(N\ge3\), this minimum-value corollary is also consistent with the published general characterization: weight \(3\) occurs exactly when a universal vertex exists, and otherwise a complete multipartite graph with no singleton part has domination and total domination number \(2\), forcing weight \(4\).

## Verification
The included checker reconstructs every complete multipartite graph from its part labels for orders \(2\) through \(9\). For every map to \(\{0,1,2\}\), it tests the quasi-total Roman conditions directly at each zero-labeled and each two-labeled vertex. It independently expands the displayed polynomial and compares every coefficient, the total function count, and the minimum weight.

## Relationship to prior work
The 2019 paper introducing quasi-total Roman domination defines the same function class, proves general bounds and complexity results, and characterizes the minimum values \(3\), \(4\), and \(N\) under broad graph-theoretic conditions. Its full text contains no complete-bipartite or complete-multipartite treatment. Thus the minimum-value corollary above is not the originality claim: for complete multipartite graphs it follows from those general minimum characterizations together with the elementary domination numbers of the family.

A 2021 follow-up develops further bounds and relationships with Roman, total Roman, and classical domination parameters. It likewise studies the minimum parameter rather than the weight distribution of all feasible functions.

Targeted searches for quasi-total Roman domination together with complete multipartite, complete bipartite, polynomial, enumerator, and all-function terminology did not locate the three-family classification or the displayed weight enumerator.

## Limitations
The theorem is restricted to connected complete multipartite graphs. The minimum-weight statement is included as a corollary of the stronger all-function classification and is substantially covered by prior general minimum-value theory. The exhaustive computation through order \(9\) is corroborative only; the theorem for arbitrary part sizes follows from the proof. Search coverage cannot exclude differently phrased or non-indexed prior enumerative work.

## References
1. S. Cabrera-García, A. Cabrera-Martínez, I. G. Yero, “Quasi-total Roman domination in graphs,” Results in Mathematics 74 (2019), 173, DOI 10.1007/s00025-019-1097-5; arXiv:1903.09789v1.
2. A. Cabrera Martínez, J. C. Hernández-Gómez, J. M. Sigarreta, “On the Quasi-Total Roman Domination Number of Graphs,” Mathematics 9 (2021), 2823, DOI 10.3390/math9212823.
