# Threshold rigidity for rank-two q-matroid ports

## Finding

Let \(M=(E,\rho)\) be a rank-two \(q\)-matroid over a finite field, with \(\dim E=n\ge3\). For each line \(P_0\le E\) satisfying \(\rho(P_0)=1\) and each complement \(P\) with \(E=P_0\oplus P\), define the reconstructing port

\[
\Gamma(P_0,P)=\{V\le P:\rho(P_0+V)=\rho(V)\}.
\]

If every such port is dimension-threshold, i.e. for each pair \(P_0,P\) there is an integer \(k(P_0,P)\) such that

\[
\Gamma(P_0,P)=\{V\le P:\dim V\ge k(P_0,P)\},
\]

then \(M\) is the uniform rank-two \(q\)-matroid: for every \(V\le E\),

\[
\rho(V)=\min\{\dim V,2\}.
\]

Conversely, the uniform rank-two \(q\)-matroid has every such port threshold at \(k=2\). The theorem therefore gives an exact rank-two classification, in particular for code-induced \(q\)-matroids arising from rank-metric coding.

## Assumptions and scope

A \(q\)-matroid has an integer-valued rank function on the subspaces of \(E\), with \(0\le\rho(V)\le\dim V\), monotonicity, and submodularity. Its total rank is assumed to be \(\rho(E)=2\). A loop is a line \(L\) with \(\rho(L)=0\). The threshold condition is required for every rank-one secret line \(P_0\) and every vector-space complement \(P\); it is not enough to check one port. The statement is about exact threshold behavior, not near-threshold ports.

## Proof

First note two consequences of the rank axioms.

**Loop fact.** If \(L\) is a loop, then for every subspace \(X\), submodularity gives

\[
\rho(X+L)+\rho(X\cap L)\le\rho(X)+\rho(L)=\rho(X).
\]

Monotonicity forces \(\rho(X+L)=\rho(X)\). The sum \(Z\) of all loop lines is a subspace of rank zero, and adding \(Z\) never changes rank.

**Rank-one-line fact.** Fix a line \(P_0\) with \(\rho(P_0)=1\). If every two-dimensional subspace containing \(P_0\) has rank one, then every subspace containing \(P_0\) has rank one. To prove this, use induction on its dimension. The assertion is true in dimensions one and two. For a subspace \(X\) of dimension at least three, choose two distinct hyperplanes \(X_1,X_2\) of \(X\) that contain \(P_0\) and satisfy \(X_1+X_2=X\). Their intersection contains \(P_0\), so the induction hypothesis gives rank one for \(X_1,X_2,X_1\cap X_2\). Submodularity yields \(\rho(X)+1\le1+1\), while monotonicity gives \(\rho(X)\ge\rho(P_0)=1\). Hence \(\rho(X)=1\). In particular, this situation would force \(\rho(E)=1\), contrary to the assumed total rank two.

We now prove the forward implication by ruling out every nonuniform rank-two case.

**Case 1: loops exist.** Let \(Z\ne0\) be the sum of all loop lines. Choose a line \(P_0\) outside \(Z\); it has rank one because the total rank is two. Choose a loop line \(L\le Z\), and choose a complement \(P\) to \(P_0\) that does not contain \(L\). The intersection \(V=P\cap(P_0+L)\) is a line distinct from \(L\). Since \(P_0+L\) meets \(Z\) exactly in \(L\), the line \(V\) is not a loop. Thus \(\rho(V)=1\), while the loop fact gives \(\rho(P_0+V)=\rho(P_0+L)=\rho(P_0)=1\). Consequently \(V\in\Gamma(P_0,P)\).

The zero subspace is not in \(\Gamma(P_0,P)\), since \(\rho(P_0)=1\). A threshold port containing the line \(V\) must therefore have threshold \(k(P_0,P)=1\), so every nonzero subspace of \(P\) must be reconstructing. If \(\dim Z\ge2\), every hyperplane \(P\) intersects \(Z\) in a nonzero subspace, so it contains a loop line \(W\). But \(\rho(P_0+W)-\rho(W)=1\), so \(W\notin\Gamma(P_0,P)\), a contradiction. If \(\dim Z=1\), choose \(P\) disjoint from \(Z\) as well as complementary to \(P_0\). Every line in \(P\) is then non-loop, and threshold one forces every plane through \(P_0\) to have rank one. The rank-one-line fact contradicts \(\rho(E)=2\). Thus loops are impossible under the threshold hypothesis.

**Case 2: no loops.** If \(M\) were nonuniform, some two-dimensional subspace \(C\) would have rank one: all lines have rank one, and any subspace of dimension at least two has rank at most two. Choose a line \(P_0\le C\) and any complement \(P\) to it. Then \(V=C\cap P\) is a line, with \(\rho(V)=\rho(C)=1\), and \(\rho(P_0+V)=\rho(C)=1\). Hence \(V\in\Gamma(P_0,P)\), so the threshold must again be one. Every line \(W\le P\) is then reconstructing, which means every plane \(P_0+W\) has rank one. The rank-one-line fact again contradicts \(\rho(E)=2\).

Therefore there are no loops and every plane has rank two. Every line has rank one; every subspace of dimension at least two contains a plane and hence has rank two. It follows that \(\rho(V)=\min\{\dim V,2\}\) for all \(V\le E\).

For the converse, take the uniform rank-two rank function. Since \(P\cap P_0=0\), we have \(\dim(P_0+V)=\dim V+1\). Therefore

\[
\rho(P_0+V)-\rho(V)=
\begin{cases}
1,&\dim V=0\text{ or }1,\\
0,&\dim V\ge2.
\end{cases}
\]

Thus \(\Gamma(P_0,P)=\{V\le P:\dim V\ge2\}\), as required.

## Verification

The argument uses only the rank axioms and the definition of a port. The loop case and the loop-free dependent-plane case exhaust nonuniform rank-two possibilities. The converse follows by direct substitution of the uniform rank function. No finite enumeration or computational certificate is used.

## Relationship to prior work

Dinesen, Byrne, Freij-Hollanti, and Hollanti introduced q-polymatroid ports and threshold structures in their 2025 paper on secret sharing in the rank metric; its Proposition 6 proves that MRD-code-induced structures are threshold. Their 2026 follow-up proves the uniform-to-threshold direction in Proposition 41 and explicitly identifies classification of q-matroids whose ports are threshold or near-threshold as an open direction. The result here proves the converse in the rank-two case: if all rank-one ports of a rank-two q-matroid are threshold, then the underlying rank function is uniform. This is a low-rank special case, not a classification in higher rank.

## Limitations

The theorem assumes an integer-valued rank-two \(q\)-matroid; a general rational \(q\)-polymatroid is outside its scope. It requires threshold behavior for every rank-one secret line and every complement, and it says nothing about near-threshold structures or ranks three and above. The proof does not classify which uniform rank-two \(q\)-matroids are represented by a specified rank-metric code; it is a structural implication for any code-induced \(q\)-matroid that meets the assumptions.

## References

J. V. Dinesen, E. Byrne, R. Freij-Hollanti, and C. Hollanti, “Secret Sharing in the Rank Metric,” arXiv:2504.18294, first submitted 25 April 2025. https://arxiv.org/abs/2504.18294.

E. Byrne, J. V. Dinesen, R. Freij-Hollanti, and C. Hollanti, “A \(q\)-Polymatroid Framework for Information Leakage in Secure Linear Network Coding,” arXiv:2601.07567, first submitted 12 January 2026. Full text: https://arxiv.org/html/2601.07567v1.
