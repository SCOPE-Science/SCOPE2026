# The complete spectral edge-exchange profile of double stars

## Finding

For integers \(k\ge m\ge1\), let \(D_{k,m}\) have adjacent hubs \(u,v\), with \(k\) pendant leaves at \(u\) (the \(A\)-leaves) and \(m\) pendant leaves at \(v\) (the \(B\)-leaves). A *valid exchange* replaces an edge \(e\) with a different nonedge \(f\) so that the resulting graph is connected. Call the exchange *improving*, *neutral*, or *decreasing* according as the adjacency spectral radius increases, stays constant, or decreases. Distinct pairs \((e,f)\) are counted separately on the labelled graph.

**Theorem.** Every improving or neutral valid exchange is in the following exhaustive list.

1. If \(m\ge2\), the hub edge \(uv\) has no improving or neutral replacement. If \(m=1\), reconnecting \(u\) to the sole \(B\)-leaf after removing \(uv\) is neutral; when \(k=m=1\), the other two replacements of \(uv\) are neutral as well. No hub-edge replacement is improving.
2. For any \(B\)-leaf \(b\), removing \(vb\) and inserting \(ub\) is strictly improving. If \(m=1\), there are additionally exactly \(k\) neutral exchanges of \(vb\), reconnecting \(b\) to any one of the \(A\)-leaves. If \(m\ge2\), there are no additional nondecreasing exchanges of \(vb\).
3. For any \(A\)-leaf \(a\), removing \(ua\) and inserting \(va\) is strictly improving if \(k=m\), neutral if \(k=m+1\), and decreasing if \(k\ge m+2\). All other replacements of \(ua\) are decreasing, except that \(k=m=1\) has one additional neutral replacement, namely inserting the edge from \(a\) to the sole \(B\)-leaf.

In particular, if \(I(k,m)\) and \(N(k,m)\) denote the numbers of improving and neutral valid exchanges, respectively, then

\[
(I(k,m),N(k,m))=\begin{cases}
(2k,0),&m\ge2,\ k=m,\\
(m,k),&m\ge2,\ k=m+1,\\
(m,0),&m\ge2,\ k\ge m+2,\\
(2,5),&(k,m)=(1,1),\\
(1,5),&(k,m)=(2,1),\\
(1,k+1),&m=1,\ k\ge3.
\end{cases}
\]

Thus, among proper double stars \(m\ge2\), the only non-sustainable edge in the balanced and one-off-balanced cases is the hub edge; for \(k\ge m+2\), exactly the hub edge and all \(k\) edges incident to the larger hub's leaves are non-sustainable. The edgewise conclusion is stronger than non-sustainability of the whole tree.

## Assumptions and scope

All graphs are finite, undirected, unweighted, and simple. The spectral radius \(\rho(G)\) is the largest eigenvalue of the symmetric adjacency matrix. Exchange edges must be absent from the original graph, different from the removed edge, and reconnect the two components after removal. An edge is *sustainable* if at least one of its valid replacements is improving or neutral. The labelled counts do not quotient by graph automorphisms or count the identity operation.

## Proof

**1. Spectral polynomial.** For the double star \(D_{a,b}\) with \(a,b\ge1\), hub eigenvector coordinates \(U,V>0\), and Perron eigenvalue \(\lambda\), elimination of each pendant coordinate gives

\[
(\lambda^2-a)U=\lambda V,\qquad
(\lambda^2-b)V=\lambda U.
\]

Hence \(x=\lambda^2\) is the largest root of

\[
F_{a,b}(x)=(x-a)(x-b)-x
=x^2-(a+b+1)x+ab.
\]

The full characteristic polynomial is \(\lambda^{a+b-2}F_{a,b}(\lambda^2)\). With \(a+b\) fixed, a smaller product \(ab\) strictly increases the largest root. As \(D_{k,m}\) properly contains the two stars centered at the hubs, its squared spectral radius \(x_0\) satisfies \(x_0>\max\{k,m\}\).

**2. Exchanges of the hub edge.** Removing \(uv\) leaves \(K_{1,k}\) and \(K_{1,m}\). Up to permutations of leaves, the three replacements different from \(uv\) join: a hub to an opposite leaf, a leaf to an opposite hub, or a leaf to a leaf. Let \(F=F_{k,m}\), \(x=\lambda^2\), and \(n=k+m+2\). The characteristic polynomials, written for \(\lambda>0\), are respectively

\[
\lambda^{n-4}\bigl(F(x)+m-1\bigr),\qquad
\lambda^{n-4}\bigl(F(x)+k-1\bigr),
\]

and

\[
\lambda^{n-4}\left(F(x)+(k+m-2)-\frac{(k-1)(m-1)}x\right).
\]

These identities follow by eliminating the pendant coordinates, or by the matching-polynomial recurrence for a forest. The correction terms are nonnegative for every \(x\ge x_0\). The third is strictly positive if \(k+m\ge3\), since \(x_0>\max\{k,m\}\); it vanishes identically only when \(k=m=1\). The first two corrections vanish precisely when \(m=1\) or \(k=1\), respectively. Moreover \(F(x)\ge0\) for \(x\ge x_0\). Thus a candidate with positive correction has no adjacency eigenvalue at or above the original Perron root, whereas zero correction gives equality. These are exactly the hub-edge cases stated in the theorem.

**3. Why no other pendant reconnection works when both hub leaf counts of the remaining base are positive.** Let \(H=D_{p,q}\) for \(p,q\ge1\), and let \(\lambda>\rho(H)\), \(x=\lambda^2\), and \(F=F_{p,q}(x)>0\). Put \(R_w(\lambda)=((\lambda I-A(H))^{-1})_{ww}\). Eliminating the leaves gives the following diagonal resolvent values for the hubs \(u,v\) and representative leaves \(y\) at \(u\), \(z\) at \(v\):

\[
R_u=\frac{\lambda(x-q)}F,\quad
R_v=\frac{\lambda(x-p)}F,\quad
R_y=\frac1\lambda+\frac{x-q}{\lambda F},\quad
R_z=\frac1\lambda+\frac{x-p}{\lambda F}.
\]

The four hub-versus-leaf differences, multiplied by the positive denominator \(\lambda F\), equal

\[
\begin{aligned}
\lambda F(R_u-R_y)&=p(x-q)+q,\\
\lambda F(R_u-R_z)&=p(x-q+1),\\
\lambda F(R_v-R_y)&=q(x-p+1),\\
\lambda F(R_v-R_z)&=q(x-p)+p.
\end{aligned}
\]

All are strictly positive because \(x>\rho(H)^2>\max\{p,q\}\). When a fresh leaf is attached at a vertex \(w\), its new spectral radius is the unique \(\lambda>\rho(H)\) satisfying \(\lambda=R_w(\lambda)\), by the Schur-complement identity. Uniqueness follows because \(R_w\) is strictly decreasing above the spectrum while \(\lambda\) increases. Therefore attaching the new leaf to either hub gives a strictly larger spectral radius than attaching it to any existing leaf. In particular, when a pendant edge of \(D_{k,m}\) is removed and the remaining double star has positive leaf counts at both hubs, every replacement to a leaf has spectral radius strictly below the original attachment to its original hub. Only attachment to the *other* hub can be nondecreasing.

**4. Compare the two possible hub attachments.** For an \(A\)-leaf, the base after deletion is \(D_{k-1,m}\) whenever \(k\ge2\). The original and other-hub attachments give \(D_{k,m}\) and \(D_{k-1,m+1}\). Their corresponding products in the quadratic \(F\) differ by

\[
(k-1)(m+1)-km=k-m-1.
\]

Thus the other-hub attachment strictly improves if \(k=m\), is neutral if \(k=m+1\), and decreases otherwise. For a \(B\)-leaf when \(m\ge2\), the base is \(D_{k,m-1}\), and the other-hub attachment gives \(D_{k+1,m-1}\). Here

\[
(k+1)(m-1)-km=m-k-1<0,
\]

so it strictly improves. Step 3 excludes all other pendant reconnections in these cases.

**5. The one-leaf boundary.** If \(m=1\), removing the single edge from \(v\) to its \(B\)-leaf leaves the star \(K_{1,k+1}\) with center \(u\). Reattaching the removed leaf to \(u\) produces the larger star \(K_{1,k+2}\), whose spectral radius is strictly greater than that of \(D_{k,1}\). Reattaching it to any of the \(k\) original \(A\)-leaves instead produces a labelled graph isomorphic to \(D_{k,1}\), hence a neutral exchange. There are no other valid new endpoints. When \(k=m=1\), removing an \(A\)-leaf has the symmetric description: one strictly improving reconnection to \(v\) and one neutral reconnection to its other leaf. The hub-edge cases were established in Step 2. Combining the cases proves the complete list and the counts.

## Verification

Running `python3 verify.py` (NumPy required) on the embedded standalone program gives `EXACT_MATCHING_CHARACTERISTIC_POLYNOMIALS_OK 112`, confirming the central-edge polynomial formulas directly from forest matching counts for every \(1\le m\le k\le7\). It also gives `INDEPENDENT_ALL_EDGE_EXCHANGES_OK 78 19565`, after reconstructing all labelled double stars and all admissible one-edge exchanges for \(1\le m\le k\le12\) and comparing the actual numerical top adjacency eigenvalues with the theorem. A final `VERIFY_OK` is emitted. Numerical eigenvalue tests use a \(10^{-8}\) sign tolerance and cannot prove the infinite theorem; the proof above supplies that argument. The exact polynomial check is independent of the proof's leaf resolvent calculation.

## Relationship to prior work

Bencs, van Dijk, and Guo introduced spectral edge sustainability and proved that the **central edge** of \(D_{k,m}\) is non-sustainable for \(k,m\ge2\) (their Example 3.6). Their broader degree threshold establishes non-sustainability of many trees, and their starlike-tree results cover some small-radius boundary behavior. Those statements are prior work; the new claim is the *complete classification of each valid edge exchange* on all double stars, including strict versus neutral distinctions and exact labelled multiplicities. The hub-edge obstruction is reproved above to keep the classification self-contained; it is not claimed as new. Classical spectral leaf-attachment perturbation results supply background methods, but not this edge-by-edge table in the inspected material.

## Limitations

The result concerns single-edge exchanges only; repeated shifts, arbitrary rewiring sequences, and non-double-star trees are not classified. Neutral cases count distinct labelled edge exchanges even if the resulting trees are isomorphic. The research record establishes a self-review only; no independent mathematical audit has been performed. Historical priority remains provisional, particularly against unindexed spectral-grafting results.

## References

1. F. Bencs, M. van Dijk, K. Guo, *Sustainable trees*, arXiv:2610.17078v1, first posted 2026-10-12. See Sections 2–3, especially Example 3.6 and Proposition 3.8. https://arxiv.org/html/2610.17078
2. C. Dalfó, M. A. Fiol, E. Garriga, *A Differential Approach for Bounding the Index of Graphs under Perturbations*, Electronic Journal of Combinatorics 18(1), P172 (2011), DOI:10.37236/659. (Background perturbation results.)
3. F. Belardo, M. Brunetti, *Infinite families of trees with equal spectral radius*, Examples and Counterexamples 5 (2024), DOI:10.1016/j.exco.2024.100138. (Different multi-edge replacement setting; comparison based on accessible abstract.)
