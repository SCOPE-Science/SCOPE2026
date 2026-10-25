# An unbounded homotopy–homology interleaving gap under the persistence Quillen–McCord hypothesis

## Finding

For every integer \(m\ge 1\), there are finite-type, integer-indexed persistence posets \(P^{(m)}\) and a fixed finite-type filtration \(Q\), with a map \(f:P^{(m)}\to Q\), for which every lower-set fiber \(f^{-1}(L_v)\) is weakly \(\varepsilon\)-contractible at \(\varepsilon=\lceil m/2\rceil\), but

\[
d_{\mathrm{HC}}(P^{(m)},Q)=m,
\qquad d_{\mathrm I}\bigl(H_*(P^{(m)};\mathbb Z),H_*(Q;\mathbb Z)\bigr)=0.
\]

The target filtration \(Q\) is fixed as \(m\) varies. Thus the homotopy-commutative interleaving distance can be arbitrarily large even when the persistent integral homology modules agree exactly and the lower-fiber hypothesis of the persistence Quillen–McCord theorem holds. Here \(d_{\mathrm{HC}}\) is computed in the homotopy category, and shifts are nonnegative integers.

## Assumptions and scope

Let \(\Sigma=S^3/I^*\) be the Poincaré homology sphere, where \(I^*\) is the binary icosahedral group of order \(120\). It is a closed triangulable integral homology \(3\)-sphere with nontrivial fundamental group; its universal cover is \(S^3\) with covering degree \(120\). Let \(u:\Sigma\to S^3\) be a degree-one map obtained by collapsing the complement of the interior of an embedded closed \(3\)-ball to a point. Choose finite triangulations and, after subdivision, a simplicial approximation \(\phi:K\to L\) to \(u\). The induced map on homology is an isomorphism in every degree, while \(\phi\) is not a homotopy equivalence.

For a finite simplicial complex \(A\), write \(\mathcal F(A)\) for its poset of nonempty faces ordered by inclusion, and write \(B(P)\) for the order complex realization of a finite poset \(P\). Set \(P_0=\mathcal F(K)\), \(Q=\mathcal F(L)\), and let \(\phi_\#:P_0\to Q\) send each nonempty face to its image face. The order complexes \(B(P_0)\) and \(B(Q)\) realize the barycentric subdivisions of \(K\) and \(L\), respectively. All homology groups below use integral coefficients.

## Proof

Fix \(m\ge1\). Define a persistence poset \(P^{(m)}\) by

\[
P_i^{(m)}=\begin{cases}P_0,&0\le i<m,\\Q,&i\ge m,\end{cases}
\]

with identity structure maps before time \(m\), the map \(\phi_\#\) from time \(m-1\) to time \(m\), and identity maps thereafter. Let \(Q_i=Q\) with identity structure maps for every \(i\). Define \(f_i:P_i^{(m)}\to Q_i\) to be \(\phi_\#\) for \(i<m\) and the identity for \(i\ge m\). These maps are order-preserving and natural; both persistence posets are finite type, and \(Q\) is a constant filtration.

**Homology distance.** The map \(\phi\) has degree one between integral homology spheres. It induces an isomorphism on \(H_0\) and \(H_3\), and all other reduced homology groups of both spaces vanish. Consequently the one transition map in \(H_*(P^{(m)};\mathbb Z)\) is an isomorphism. This persistence module is naturally isomorphic to the constant module \(H_*(Q;\mathbb Z)\), so its interleaving distance from that module is zero.

**Upper bound for the homotopy distance.** There is an \(m\)-interleaving in the homotopy category: from \(P_i^{(m)}\) to \(Q_{i+m}=Q\), use \(\phi_\#\) when \(i<m\) and the identity when \(i\ge m\); from \(Q_i\) to \(P_{i+m}^{(m)}=Q\), use the identity at every index. The two composites are precisely the structure maps shifted by \(2m\). Hence \(d_{\mathrm{HC}}(P^{(m)},Q)\le m\).

**Lower bound.** Suppose an \(\varepsilon\)-interleaving existed for an integer \(0\le\varepsilon<m\). Write its maps as \(a_i:P_i^{(m)}\to Q_{i+\varepsilon}\) and \(b_i:Q_i\to P_{i+\varepsilon}^{(m)}\) in the homotopy category. Since all structure maps of \(P^{(m)}\) through index \(\varepsilon\) are identities, naturality gives \(a_\varepsilon=a_0\). The interleaving identity on the constant target gives

\[
a_0\circ b_0=a_\varepsilon\circ b_0\simeq\operatorname{id}_{S^3}.
\]

Thus \(b_0:S^3\to\Sigma\) would have a homotopy right inverse and therefore degree \(\pm1\). This is impossible: every map \(S^3\to\Sigma\) lifts to the universal cover \(S^3\), so its degree as a map to \(\Sigma=S^3/I^*\) is divisible by \(120\). No such interleaving exists for \(\varepsilon<m\), proving \(d_{\mathrm{HC}}(P^{(m)},Q)=m\).

**Lower-set fibers.** For \(v\in Q=\mathcal F(L)\), let \(L_v=\{w\in Q:w\le v\}\). This poset has maximum \(v\), so \(B(L_v)\) is contractible. Put \(F_v=f^{-1}(L_v)\) as a persistence subposet. At indices below \(m\), it is the preimage of \(L_v\) under \(\phi_\#\); from index \(m\) onward it equals \(L_v\). Let \(\varepsilon=\lceil m/2\rceil\), so \(2\varepsilon\ge m\). For every index \(i\), the structure map \(F_{v,i}\to F_{v,i+2\varepsilon}\) has contractible target: if \(i<m\), the target is \(L_v\); if \(i\ge m\), it is again \(L_v\). Every such map is null-homotopic. Choosing a point in the first nonempty fiber stage and propagating it by the structure maps gives a compatible map from the point persistence space at that threshold. These maps and the unique maps to a point exhibit a homotopy-commutative \(\varepsilon\)-interleaving. Hence each lower-set fiber is weakly \(\varepsilon\)-contractible, as required.

The construction proves an unbounded gap between the two distances; it does not establish sharpness of the coefficient in the published upper bound \(d_{\mathrm{HC}}\le2\varepsilon|Q|\). ∎

## Verification

The distance calculations are exact and use integer shifts. The homology calculation follows from the degree-one map between integral homology spheres. The lower bound uses the covering degree \(120\) and the homotopy-interleaving identity on the constant target; the upper bound is given by explicit structure-compatible interleaving maps. The fiber check verifies the required null-homotopies after a shift of \(2\varepsilon\) and the compatible choice of a point at each fiber's threshold. No numerical experiment or finite enumeration is used as a substitute for proof.

## Relationship to prior work

Guzeev and Tanaka prove a persistence Quillen–McCord theorem: weakly \(\varepsilon\)-contractible lower or upper fibers imply \(d_{\mathrm{HC}}(P,Q)\le2\varepsilon|Q|\), and their Corollary 3.10 gives the corresponding homological bound. Their concluding remarks explicitly identify the difference between homology interleaving distance and homotopy-commutative interleaving distance as a direction for further investigation. The present family addresses that comparison with an exact, unbounded separation while keeping the target fixed. Guzeev's earlier persistent homological version studies homology interleavings, not this exact homotopy-distance gap.

## Limitations

The construction is an existence family based on finite triangulations and simplicial approximation; it does not provide a minimal face-list realization or optimize the size of the fixed target. The gap grows because the non-homotopy-equivalent initial space is held for an arbitrarily long initial segment before the degree-one map reaches \(S^3\). This does not improve the general upper bound or prove its coefficient sharp. The novelty assessment is literature-based and cannot exclude every unpublished or unindexed equivalent construction.

## References

1. V. Guzeev and K. Tanaka, “Quillen-McCord theorem for persistence finite posets,” arXiv:2605.11615 (first public version 12 May 2026), especially Theorem 3.8, Corollary 3.10, and the concluding remarks.
2. V. Guzeev, “Persistent homological Quillen-McCord theorem,” arXiv:2307.00177 (1 July 2023).
3. J. W. Cannon et al., “What is a topological manifold?” survey discussion of the Poincaré homology sphere as the quotient of \(S^3\) by the binary icosahedral group of order \(120\).
