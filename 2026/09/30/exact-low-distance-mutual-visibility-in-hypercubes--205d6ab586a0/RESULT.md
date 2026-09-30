# Exact \(2\)- and \(3\)-distance mutual visibility in hypercubes
## Finding
Let \(Q_n\) be the \(n\)-dimensional hypercube, with vertices identified with subsets of \([n]\), and let \(\mu_k(Q_n)\) denote the \(k\)-distance mutual-visibility number: a set \(S\) is feasible when every two vertices of \(S\) have a geodesic of length at most \(k\) whose internal vertices avoid \(S\).

For every \(n\ge 2\),
\[
\mu_2(Q_n)=n+1.
\]
For \(k=3\),
\[
\mu_3(Q_n)=
\begin{cases}
3,&n=2,\\
5,&n=3,\\
8,&n=4,\\
2n-1,&n\ge5.
\end{cases}
\]
The exceptional value at \(n=4\) is attained by the eight vertices whose first three coordinates have even parity.

## Assumptions and scope
All graphs are finite, simple, and undirected. Hypercube distance is Hamming distance, equivalently \(d(A,B)=|A\triangle B|\) under the subset model. The result concerns the distance-limited mutual-visibility parameter introduced in arXiv:2408.03976 / DOI:10.1007/s40840-024-01811-3. The upper bounds use the classical bounded-diameter theorem for set families and, for the equality case at diameter three when \(n\ge5\), Frankl's extremal characterization in DOI:10.1017/S0963548316000456.

## Proof
For \(k=2\), any \(2\)-distance mutual-visibility set has Hamming diameter at most \(2\). For \(n\ge3\), Kleitman's diameter theorem gives size at most
\[
\sum_{i=0}^{1}\binom{n}{i}=n+1.
\]
The closed Hamming ball
\[
B_1(\varnothing)=\{\varnothing\}\cup\{\{i\}:i\in[n]\}
\]
has \(n+1\) vertices and is \(2\)-distance mutually visible: \(\varnothing\) is adjacent to each singleton, while for distinct singletons \(\{i\},\{j\}\) the geodesic \(\{i\},\{i,j\},\{j\}\) has its internal vertex outside the ball. For \(n=2\), the same three-vertex construction works and all four vertices of the cycle \(Q_2\) fail because an antipodal pair has both possible geodesic midpoints selected. Hence \(\mu_2(Q_n)=n+1\) for every \(n\ge2\).

Now take \(k=3\). For \(n\ge5\), every feasible set has Hamming diameter at most \(3\), so Kleitman's bound gives \(|S|\le2n\). Frankl's equality characterization applies because \(n\ge3+2\): if \(|S|=2n\), then, after a hypercube translation, \(S\) is
\[
\mathcal K_y=\{A\subseteq[n]:|A\setminus\{y\}|\le1\}.
\]
But \(\varnothing\) and \(\{y,i\}\) belong to \(\mathcal K_y\) for any \(i\ne y\), and their only two geodesic midpoints are \(\{y\}\) and \(\{i\}\), which also belong to \(\mathcal K_y\). Thus \(\mathcal K_y\) is not mutual-visible, and therefore \(|S|\le2n-1\).

This bound is sharp. Fix \(y\in[n]\) and put
\[
S_n=\{\{i\}:i\in[n]\}\cup\{\{y,i\}:i\in[n]\setminus\{y\}\}.
\]
Then \(|S_n|=2n-1\). Distinct singletons see each other through \(\varnothing\), which is outside \(S_n\). A singleton \(\{j\}\), with \(j\notin\{y,i\}\), and a pair \(\{y,i\}\) see each other along
\[
\{j\},\{i,j\},\{y,i,j\},\{y,i\},
\]
whose two internal vertices lie outside \(S_n\). Two distinct pairs \(\{y,i\}\) and \(\{y,j\}\) see each other through \(\{y,i,j\}\), and all remaining pair types are adjacent. Hence \(S_n\) is \(3\)-distance mutually visible, proving \(\mu_3(Q_n)=2n-1\) for \(n\ge5\).

For \(n=4\), Kleitman's diameter-three bound gives \(\mu_3(Q_4)\le8\). Let
\[
P=\{x\in\{0,1\}^4:x_1+x_2+x_3\equiv0\pmod 2\}.
\]
Then \(|P|=8\). Two vertices of \(P\) differ in either zero or two of the first three coordinates, and possibly also in the fourth. At distance \(2\), both geodesic midpoints have odd parity in the first three coordinates and lie outside \(P\). At distance \(3\), toggle one of the differing first-three coordinates, then the fourth coordinate, then the other differing first-three coordinate; both internal vertices have odd first-three parity. Thus \(P\) is \(3\)-distance mutually visible and \(\mu_3(Q_4)=8\).

For \(n=3\), the construction \(S_3\) above has size \(5\). No six-vertex set is feasible. Up to an automorphism of \(Q_3\), the two omitted vertices of a six-set are at distance \(1\), \(2\), or \(3\). If they are \(000,001\), then \(010\) and \(111\) have both geodesic midpoints selected. If they are \(000,011\), then for the antipodal selected pair \(001,110\), the two omitted vertices lie in the same distance layer of the interval and cannot be the two consecutive internal vertices of a geodesic; every geodesic therefore contains a selected internal vertex. If they are \(000,111\), the same selected antipodal pair \(001,110\) has the two omitted vertices nonadjacent inside its interval, so again every geodesic contains a selected internal vertex. Hence \(\mu_3(Q_3)=5\). Finally, \(Q_2\) has mutual-visibility number \(3\), as noted in the \(k=2\) case, so \(\mu_3(Q_2)=3\).

## Verification
The standalone file `verify.py` exhaustively enumerates every vertex subset of \(Q_2\), \(Q_3\), and \(Q_4\) and confirms
\[
(\mu_2(Q_2),\mu_3(Q_2))=(3,3),\quad
(\mu_2(Q_3),\mu_3(Q_3))=(4,5),\quad
(\mu_2(Q_4),\mu_3(Q_4))=(5,8).
\]
It also checks the \(k=2\) constructions through \(n=12\), the parity construction for \(Q_4\), the size-\((2n-1)\) \(k=3\) constructions for \(5\le n\le12\), and the obstruction inside the Frankl extremal family. The replay ends with `VERIFY_OK`.

## Relationship to prior work
The distance-limited mutual-visibility parameter was introduced in arXiv:2408.03976, where exact values were obtained for several graph classes and hypercubes were cited in the surrounding mutual-visibility literature, but the exact \(k=2\) and \(k=3\) hypercube values above were not found in the checked sources. Classical mutual visibility in hypercubes is studied in arXiv:2402.04791, while the bounded-Hamming-diameter extremal structure used here comes from DOI:10.1017/S0963548316000456. The present contribution is the combination of the distance-limited visibility condition with the extremal set-theoretic diameter structure, including the exceptional parity construction in \(Q_4\).

## Limitations
Only the cases \(k=2\) and \(k=3\) are determined. The argument does not claim formulas for larger \(k\), where bounded-diameter extremal families and the internal-geodesic avoidance condition interact more intricately. The literature search establishes originality only to the best of current accessible knowledge; no independent audit, formal proof assistant verification, or expert attestation has been performed.

## References
1. P. Frankl, “A Stability Result for Families with Fixed Diameter,” Combinatorics, Probability and Computing 26 (2017), 506–516. DOI:10.1017/S0963548316000456.
2. M. Cera López, P. García-Vázquez, J. C. Valenzuela-Tripodoro, and I. G. Yero, “The \(k\)-Distance Mutual-Visibility Problem in Graphs.” arXiv:2408.03976; DOI:10.1007/s40840-024-01811-3.
3. M. Axenovich and D. Liu, “Visibility in Hypercubes.” arXiv:2402.04791.
