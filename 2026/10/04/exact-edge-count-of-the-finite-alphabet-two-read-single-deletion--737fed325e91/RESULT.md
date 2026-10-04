# Exact edge count of the finite-alphabet two-read single-deletion reconstruction graph
## Finding
Let \(\Sigma_q\) be an alphabet of size \(q\ge2\). For \(x\in\Sigma_q^n\), let \(D_1(x)\) be the set of distinct length-\(n-1\) words obtainable by deleting one coordinate. Define the two-read single-deletion reconstruction graph \(G^{\mathrm D}_{q,n}\) on \(\Sigma_q^n\) by joining distinct \(x,y\) exactly when
\[
|D_1(x)\cap D_1(y)|=2.
\]
For every \(n\ge2\),
\[
|E(G^{\mathrm D}_{q,n})|
=\binom q2\sum_{L=2}^{n}(n-L+1)q^{n-L}
=\frac{q\bigl(1-nq^{n-1}+(n-1)q^n\bigr)}{2(q-1)}.
\]
Every edge has a unique canonical alternating-interval representation. Consequently,
\[
\overline d(G^{\mathrm D}_{q,n})
=\frac{2|E(G^{\mathrm D}_{q,n})|}{q^n}
=n-\frac{q}{q-1}+\frac{q^{1-n}}{q-1}.
\]
For the binary alphabet this reduces to
\[
|E(G^{\mathrm D}_{2,n})|=1+(n-2)2^{n-1},
\qquad
\overline d(G^{\mathrm D}_{2,n})=n-2+2^{1-n}.
\]

## Assumptions and scope
Deletion balls are sets of distinct descendants, so deleting two different coordinates that yield the same descendant contributes only once. The graph concerns exactly two reads: adjacency is the forbidden relation for a code whose distinct codewords must satisfy \(|D_1(x)\cap D_1(y)|<2\). The statement holds for every finite alphabet size \(q\ge2\) and every blocklength \(n\ge2\).

The result is an edge-enumeration theorem for the reconstruction graph. It does not determine the independence number of that graph and therefore does not by itself determine optimal two-read reconstruction-code cardinalities.

## Proof
Cai, Kiah, Nguyen, and Yaakobi prove for equal-length distinct words that a one-deletion-ball intersection has size at most two. Their Type-A characterization says that an intersection of size two occurs exactly when the two source words agree outside one interval and, on that interval, are opposite phases of an alternating word over two distinct symbols. The Hamming-distance-one case has intersection size one, so the interval relevant here has length at least two.

Take an edge \(\{x,y\}\), and let \(i\) be the first coordinate where \(x\) and \(y\) differ and \(j\) the last. Put \(L=j-i+1\). The Type-A characterization forces \(L\ge2\), forces equality outside \([i,j]\), and forces the restrictions to \([i,j]\) to be the two alternating phases over a unique unordered symbol pair \(\{\alpha,\beta\}\). Thus the data
\[
([i,j],\;x_{[1,n]\setminus[i,j]},\;\{\alpha,\beta\})
\]
are uniquely determined by the edge.

Conversely, choose an interval of length \(L\ge2\), choose an arbitrary common outside word, and choose an unordered pair \(\{\alpha,\beta\}\) of distinct alphabet symbols. Filling the interval with the two opposite alternating phases produces two words whose one-deletion balls have exactly two common descendants, hence an edge. The first and last coordinates of that interval differ, so the interval is the first-to-last differing interval and no edge is counted twice.

For fixed \(L\), there are \(n-L+1\) interval positions, \(q^{n-L}\) common outside words, and \(\binom q2\) unordered symbol pairs. Therefore
\[
|E(G^{\mathrm D}_{q,n})|
=\binom q2\sum_{L=2}^{n}(n-L+1)q^{n-L}.
\]
With \(k=n-L\),
\[
\sum_{L=2}^{n}(n-L+1)q^{n-L}
=\sum_{k=0}^{n-2}(k+1)q^k
=\frac{1-nq^{n-1}+(n-1)q^n}{(q-1)^2}.
\]
Multiplying by \(\binom q2=q(q-1)/2\) gives the closed form. The average-degree formula follows from the handshaking identity on the \(q^n\) vertices.

## Verification
The accompanying verifier independently constructs every distinct one-deletion ball and, separately, tests the canonical alternating-interval condition. It exhaustively checks that these two definitions of adjacency agree and that no pair has more than two common descendants for the following parameter ranges:
\[
(q,n)\in\{(2,2),\ldots,(2,9)\}\cup\{(3,2),\ldots,(3,6)\}\cup\{(4,2),\ldots,(4,5)\}\cup\{(5,2),\ldots,(5,4)\}.
\]
For every tested pair, the brute-force edge count agrees with both the interval sum and the closed formula. The binary counts for \(n=2,\ldots,10\) are
\[
1,5,17,49,129,321,769,1793,4097.
\]
The computation is a finite corroboration only; the universal claim rests on the Type-A characterization and the counting proof above.

## Relationship to prior work
Cai, Kiah, Nguyen, and Yaakobi characterize exactly when two equal-length source words have two common one-deletion descendants, introducing the Type-A alternating form. That pairwise theorem supplies the structural premise used here. Their reconstruction results optimize code redundancy and intersection thresholds rather than enumerate all forbidden source pairs.

Ye, Liu, Zhang, and Ge use the same Type-A phenomenon in insertion reconstruction. Abu-Sini and Yaakobi study extremal intersections of multiple insertion or deletion balls. Abbasian, Mirmohseni, and Nasiri Kenari count related local Type-A configurations among descendants of a fixed word when analyzing error-ball sizes. These are different statistics from the total number of source-word pairs in \(G^{\mathrm D}_{q,n}\).

A previously recorded exact binary length-seven two-read reconstruction optimum determines \(\alpha(G^{\mathrm D}_{2,7})=70\). The present result instead gives \(|E(G^{\mathrm D}_{2,7})|=321\) and an all-\(q\), all-\(n\) formula. Neither graph invariant determines the other.

## Limitations
The formula counts edges and yields average degree but does not give the degree distribution, independence number, chromatic number, or optimal reconstruction code for general parameters. The literature comparison did not find this global enumeration, but a differently indexed or differently named enumeration in older synchronization literature remains possible. The proof relies on the published Type-A characterization; the verifier does not replace that general theorem.

## References
1. K. Cai, H. M. Kiah, T. T. Nguyen, and E. Yaakobi, “Coding for Sequence Reconstruction for Single Edits,” arXiv:2001.01376v1, 2020; IEEE Transactions on Information Theory, 2022, DOI 10.1109/TIT.2021.3122798.
2. Z. Ye, X. Liu, X. Zhang, and G. Ge, “Reconstruction of Sequences Distorted by Two Insertions,” arXiv:2302.09798v1, 2023; IEEE Transactions on Information Theory 69(8), 2023.
3. M. Abu-Sini and E. Yaakobi, “On the Intersection of Multiple Insertion (or Deletion) Balls and its Application to List Decoding Under the Reconstruction Model,” IEEE Transactions on Information Theory 70(5), 2024, DOI 10.1109/TIT.2023.3319608.
4. A. Abbasian, M. Mirmohseni, and M. Nasiri Kenari, “On the size of error ball in DNA storage channels,” arXiv:2410.15290v1, 2024.
