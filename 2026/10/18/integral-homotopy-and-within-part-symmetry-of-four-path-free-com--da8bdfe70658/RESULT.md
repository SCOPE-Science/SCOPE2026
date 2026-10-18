# Integral homotopy and within-part symmetry of four-path-free complete multipartite complexes

## Finding

Let \(m\ge3\) and \(n_1,\ldots,n_m\ge1\) be arbitrary integers. Put \(G=K_{n_1,\ldots,n_m}\), with labeled vertex classes \(V_1,\ldots,V_m\), and let \(X=\mathrm{PF}_4(G)\) be the simplicial complex whose faces are subsets of graph vertices whose induced graphs contain **no simple (not necessarily induced) path on four distinct vertices**. Set \(N=\sum_i n_i\), \(e_2=\sum_{i<j}n_i n_j\), and \(e_3=\sum_{i<j<k}n_i n_j n_k\).

**Theorem.** There is an integral homotopy equivalence
\[
X\simeq\bigvee^{\beta} S^2,\qquad \beta=(m-1)(1-N)+e_2+e_3.
\]
The convention is that the wedge with zero summands is contractible. Let \(W=\prod_i S_{n_i}\) act by relabeling vertices within the parts; let \(f_i(g)\) count the fixed vertices of the \(i\)-th factor of \(g\). Its complete rational second-homology character is
\[
\chi(g)=(m-1)\left(1-\sum_i f_i(g)\right)+\sum_{i<j}f_i(g)f_j(g)+\sum_{i<j<k}f_i(g)f_j(g)f_k(g).
\]
Writing \(I_i=\mathbb Q^{n_i}/\mathbb Q\) for the augmented natural permutation module of \(S_{n_i}\) (inflated to \(W\)), the full rational representation is
\[
\widetilde H_2(X;\mathbb Q)\cong
\mathbb Q^{\oplus\binom{m-1}{3}}
\oplus\bigoplus_i I_i^{\oplus\binom{m-1}{2}}
\oplus\bigoplus_{i<j}(I_i\otimes I_j)^{\oplus(m-1)}
\oplus\bigoplus_{i<j<k} I_i\otimes I_j\otimes I_k.
\]
All tensor factors are external over distinct direct-product factors. A zero-dimensional \(I_i\) vanishes.

## Assumptions and scope

The graph is finite, simple, undirected, complete multipartite, with at least three nonempty parts; no assumption of equal sizes. A four-vertex path may have additional chords in the graph. The result concerns homotopy over integers and the rational action of the within-part group \(W\), not the potentially larger automorphism group interchanging equal-sized classes. The first-public-date source used for the recent research context is Deshpande–Goyal–Sawant, arXiv:2607.05358 (July 6, 2026), not a claim to its theorem as new.

## Proof

**1. Complete description of allowable faces.** For any nonempty vertex set \(S\), put \(r_i=|S\cap V_i|\) and let \(t\) count its positive \(r_i\). A four-vertex path exists if \(t\ge4\); if \(t=3\) and one of the three \(r_i\) is at least two, choose \(a_1,b,a_2,c\) in the corresponding class order to obtain path \(a_1-b-a_2-c\); or if \(t=2\) with both occupied class sizes at least two, choose alternating vertices. Conversely, no four-vertex path can occur within one class, with exactly two occupied parts of which one contains only one vertex, or with exactly three occupied parts of one vertex each. These are precisely all faces of \(X\).

In particular every vertex triple is a face, so \(X\) contains the complete two-skeleton on its vertex set. Hence \(X\) is simply connected: its one-skeleton is complete, and every triangular loop bounds a simplex; every edge loop decomposes into triangles.

**2. Homology concentrated in degree two.** Write \(U_i=\Delta(V_i)*\mathrm{sk}_0\Delta(V\setminus V_i)\), with the latter zero-skeleton understood to contain the empty face. Each \(U_i\) is contractible. Let \(Z=\bigcup_{i=1}^mU_i\) and \(Z_k=\bigcup_{i=1}^kU_i\). For \(i\neq j\), the intersection \(U_i\cap U_j\) is a one-dimensional subcomplex: it is the complete bipartite graph on \(V_i\sqcup V_j\), together with isolated vertices of the remaining parts. Consequently \(J_k=Z_{k-1}\cap U_k=\bigcup_{i<k}(U_i\cap U_k)\) is a graph (possibly disconnected). Mayer–Vietoris for \(Z_k=Z_{k-1}\cup U_k\), starting from the contractible \(Z_1\), proves \(H_j(Z;\mathbb Z)=0\) for all \(j\ge3\). It also proves by induction that \(H_2(Z;\mathbb Z)\) is free: the exact sequence has \(H_2(Z_{k-1})\) as a subgroup of \(H_2(Z_k)\) and free quotient equal to a subgroup of \(H_1(J_k)\); the short exact sequence splits because the quotient is free.

By Step 1, \(X\) is obtained from \(Z\) by adjoining *only* those two-simplices with vertices in three distinct parts. All their edges already lie in \(Z\). Thus the relative cellular chain complex \(C_*(X,Z;\mathbb Z)\) is free in degree two and zero in all other degrees. The relative long exact sequence proves \(H_j(X;\mathbb Z)=0\) for all \(j\ge3\), and \(H_2(X;\mathbb Z)\) is an extension of the free group \(H_2(Z;\mathbb Z)\) by a subgroup of the free group \(H_2(X,Z;\mathbb Z)\), hence is free. Simple connectivity gives \(H_1(X;\mathbb Z)=0\). Its rank is determined in Step 3. A map from the indicated wedge of two-spheres representing a basis of \(\pi_2(X)\cong H_2(X;\mathbb Z)\) is an integral homology equivalence, hence is a homotopy equivalence by the homology form of Whitehead's theorem for simply connected CW complexes.

**3. Exact sphere count.** With the empty set included, the face enumerator \(F(z)=\sum_{S\in X}z^{|S|}\) is
\[
F(z)=1+\sum_i((1+z)^{n_i}-1)
+\sum_{i<j}\{n_j z((1+z)^{n_i}-1)+n_i z((1+z)^{n_j}-1)-n_in_j z^2\}
+e_3 z^3.
\]
The three terms enumerate sets occupying one, two and three parts; in the two-part expression the double-counted two-vertex set is removed. Since each \(n_i\ge1\), evaluating at \(z=-1\) gives \(F(-1)=1-m+(m-1)N-e_2-e_3\). Therefore \(\widetilde\chi(X)=-F(-1)=(m-1)(1-N)+e_2+e_3\), which equals the free rank of the unique possibly nonzero reduced homology \(\widetilde H_2\).

**4. Complete symmetry character.** For \(g\in W\) and a simplex \(S\) invariant as a vertex set, let \(c_g(S)\) be the number of vertex-permutation cycles included in \(S\). On the oriented simplex basis the alternating signed trace is \((-1)^{c_g(S)-1}\), including the augmented empty-face convention. The reduced Lefschetz number therefore equals \(-\sum_{S\in X,\;gS=S}(-1)^{c_g(S)}\). For each part, the signed sum over all its nonempty invariant subsets equals \(-1\), since its whole collection of permutation cycles has generating product \((1-1)^{c_i}=0\). The signed sum over its invariant singleton subsets equals \(-f_i(g)\). Counting the four mutually exclusive face types from Step 1 gives
\[
\sum_{S\in X,\;gS=S}(-1)^{c_g(S)}
=1-m+\sum_{i<j}\big(f_i(g)+f_j(g)-f_i(g)f_j(g)\big)-\sum_{i<j<k}f_i(g)f_j(g)f_k(g).
\]
The two-part summand counts a nonempty invariant subset in one part and an invariant singleton in the other, subtracting the duplicate singleton pair. Since rational reduced homology is concentrated in degree two, its character is the reduced Lefschetz number. Substitute \(f_i=1+(f_i-1)\) to obtain constant coefficient \(\binom{m-1}{3}\), singleton coefficient \(\binom{m-1}{2}\), double coefficient \(m-1\) and triple coefficient one. The character of \(I_i\) is \(f_i-1\), so the displayed direct-sum representation has this complete character. Over characteristic zero representations of finite groups are semisimple and determined by characters. This finishes the proof.

## Verification

The standalone program `verify_pathfree4.py` independently enumerates actual four-vertex paths on 64 graph-size tuples, checks all faces against the independent occupancy classification, computes boundary ranks over the field of two elements and tests the stated Betti ranks. It includes sample sizes \((3,3,3)\), with \(\beta=38\), and \((2,2,2,2)\), with \(\beta=35\). The standalone program `verify_equivariant.py` constructs representatives of all within-part conjugacy classes for nine sample tuples, performs 123 orientation-sensitive augmented chain-trace calculations and checks the character formula. Both require Python 3 standard library only; their exact printed outputs are included as text artifacts. Finite tests corroborate but do not replace Steps 1–4.

## Relationship to prior work

Deshpande, Goyal and Sawant, arXiv:2607.05358, develop the general structural decomposition of path-free complexes on complete multipartite graphs and report complete homotopy classifications for the bipartite case. Their decomposition is a related starting point; it is **not** presented here as a new construction. The above proof specializes to forbidden four-vertex paths, supplies a full integral sphere-wedge formula for all numbers of multipartite classes at least three, and gives an explicit within-part rational homology representation. The paper's abstract and available secondary technical summary were reviewed; the full manuscript was not available for theorem-by-theorem comparison. The possibility of a more detailed overlapping special case in its body is a meaningful bibliographic uncertainty. The different edge-subset path-free complexes of Grinberg, Katthän and Lewis (2021) concern directed paths between designated vertices and do not imply this vertex-subset claim.

## Limitations

No claim is made for general forbidden path size \(t\neq4\), integral representation lattices, or actions that permute equal-sized parts. No assertion of independent verification or uniqueness in unpublished literature is made. The primary source arXiv:2607.05358 could not be inspected in full; an overlapping special case in the inaccessible text has not been ruled out. The computational checks are exhaustive only for their declared finite input sets; the all-parameter proof is the argument above.

## References

1. P. Deshpande, S. Goyal and R. Sawant, *On a complete characterization of path-free complexes associated with complete multipartite graphs*, arXiv:2607.05358 (first submitted July 6, 2026), https://arxiv.org/abs/2607.05358.
2. D. Grinberg, L. Katthän and J. B. Lewis, *The path-missing and path-free complexes of a directed graph*, arXiv:2102.07894 (2021), https://arxiv.org/abs/2102.07894. This is a different edge-subset construction.
