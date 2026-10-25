# Exact natural-basis graph spectra of binary rank-one evolution algebras

## Finding

For every integer \(n\ge 3\), the entire family of directed graphs arising from natural bases of every \(n\)-dimensional nondegenerate evolution algebra \(E\) over \(\mathbb F_2\) satisfying \(\dim E^2=1\) is determined exactly. Write \(H_{n,k}\) for the directed graph on \(n\) vertices in which every vertex has an arrow to each vertex of one distinguished \(k\)-element set, and there are no other arrows; loops are retained. Up to graph isomorphism, \(H_{n,k}\) depends only on \(k\).

In any natural basis \(e_1,\ldots,e_n\), the algebra has a unique common nonzero square \(u=e_i^2\), with \(u=\sum_i u_i e_i\) and \(u\ne0\). Set \(h=|\{i:u_i=1\}|\). The **complete graph spectrum** \(\mathcal G(E)\), the set of digraph isomorphism types obtained from *all* natural bases, is

\[
\mathcal G(E)=
\begin{cases}
\{H_{n,n}\},&u=e_1+\cdots+e_n,\\
\{H_{n,k}:1\le k<n,\ k\text{ odd}\},&u\ne e_1+\cdots+e_n,\ h\text{ odd},\\
\{H_{n,k}:2\le k<n,\ k\text{ even}\},&u\ne e_1+\cdots+e_n,\ h\text{ even}.
\end{cases}
\]

These are exactly three nonempty types of graph spectra for each \(n\ge3\). In particular, a finite nonempty collection \(H_{n,k_1},\ldots,H_{n,k_s}\) occurs as the natural-basis graphs of a single such algebra if and only if **either all \(k_j=n\), or all \(k_j<n\) and the \(k_j\) have the same parity**. Thus the simultaneous-realisation problem is decided completely for this natural class, including construction of the algebra and basis for every permitted graph. Strong connectivity is likewise fully determined: an attainable graph is strongly connected precisely in the singleton case \(H_{n,n}\).

## Assumptions and scope

The ground field is exactly \(\mathbb F_2\), and \(n\) is any integer at least \(3\). Evolution algebras are finite-dimensional, commutative, generally nonassociative algebras admitting a *natural basis* whose distinct elements have product zero. We use the standard graph convention: an arrow from \(i\) to \(j\) is present if the coefficient of \(e_j\) in \(e_i^2\) is nonzero. Loops count. Nondegenerate means \(\operatorname{Ann}(E)=0\), equivalent here to all natural-basis squares being nonzero. The square \(E^2\) is the linear span of all products and has dimension exactly one. Natural bases may be changed arbitrarily; graph types are compared up to directed graph isomorphism, not arbitrary graph homomorphism.

## Proof

**1. Normal form.** Choose a natural basis \(e_i\). Because \(E^2\) is one-dimensional and the annihilator is zero, every \(e_i^2\) is a nonzero multiple of the same vector. The only nonzero scalar in \(\mathbb F_2\) is \(1\), so every \(e_i^2=u\ne0\). Identifying \(E\) with \(\mathbb F_2^n\) using this basis, multiplication is
\[
xy=(x\mathbin{\cdot} y)u,
\qquad x\mathbin{\cdot}y=\sum_{i=1}^n x_i y_i.
\]
The bilinear form is nonsingular. Conversely any nonzero \(u\) with this product defines an algebra in the stated class.

**2. All natural bases.** Let \(P\) have the new basis vectors as columns. They are pairwise orthogonal for the dot product if and only if their cross products vanish. Their Gram matrix is diagonal, and because the vectors form a basis, this Gram matrix is nonsingular. Hence every diagonal entry equals \(1\) and \(P^{\mathsf T}P=I_n\). Conversely every such orthogonal matrix gives a natural basis. In this new basis the common square \(u\) has coordinate vector \(P^{-1}u=P^{\mathsf T}u\). Thus the resulting graph is \(H_{n,k}\), where \(k\) is the Hamming weight of \(P^{\mathsf T}u\). Since orthogonal matrices are closed under transpose, the possible weights are exactly the weights in the orthogonal-group orbit of \(u\).

**3. Orthogonal orbits over \(\mathbb F_2\).** Put \(\mathbf1=(1,\ldots,1)\). Because \(x\cdot x=x\cdot\mathbf1\) for every \(x\), every orthogonal matrix \(Q\) fixes \(\mathbf1\): \(x\cdot\mathbf1=(Qx)\cdot\mathbf1=x\cdot Q^{\mathsf T}\mathbf1\) for all \(x\), forcing \(Q^{\mathsf T}\mathbf1=\mathbf1\). Orthogonal matrices also preserve \(x\cdot x\), which is the parity of its weight. Therefore \(0\) and \(\mathbf1\) are singleton orbits, and a noncanonical vector cannot change weight parity.

For the converse, coordinate permutations are orthogonal. For every four-element coordinate set \(J\), let \(w_J\) be its indicator and let \(T_J=I_n+w_Jw_J^{\mathsf T}\). Since \(w_J\cdot w_J=0\) and the characteristic is two, direct multiplication gives \(T_J^{\mathsf T}T_J=I_n\). Acting on a binary vector, \(T_J\) toggles the four coordinates in \(J\) exactly when their sum is odd. A vector of weight \(r\), with \(3\le r<n\), has three one-coordinates and one zero-coordinate. Choosing them as \(J\) lowers its weight from \(r\) to \(r-2\). Iterating, every noncanonical odd-weight vector reaches a unit vector, and every nonzero noncanonical even-weight vector reaches a weight-two vector; permutations are transitive on unit vectors and weight-two vectors respectively. Thus, among nonzero vectors, the orthogonal orbits are precisely \(\{\mathbf1\}\), all odd-weight vectors other than \(\mathbf1\), and all nonzero even-weight vectors other than \(\mathbf1\). This proof also supplies explicit orthogonal transformations between any two vectors in the same orbit.

**4. Graph spectrum and simultaneous realisation.** Combining Steps 2 and 3 proves the three formula branches. For \(n\ge3\), all three orbit types occur: choose \(u=\mathbf1\), \(u=e_1\), or \(u=e_1+e_2\). Orthogonal transformations from Step 3 produce natural bases realizing every permitted support size. The vertices of \(H_{n,k}\) having positive indegree are precisely the distinguished \(k\) target vertices (each with indegree \(n\)); thus graphs with distinct \(k\) are not isomorphic. One algebra can realize several given \(H_{n,k}\) precisely when all desired weight sizes belong to the same orbit spectrum, which is equivalent to the stated parity criterion. No algebra outside this normal form can occur in the specified class, by Step 1.

Finally, if \(k<n\), vertices outside the target set have indegree zero, so the graph is not strongly connected. For \(k=n\), every directed edge including every loop is present, so it is strongly connected. This completes the proof. \(\square\)

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. It exhaustively enumerates **every** ordered orthonormal basis in dimensions \(3\) and \(4\), respectively \(6\) and \(48\) bases, and directly checks the attainable graph support weights for every nonzero defining vector. Separately it generates the orbits under coordinate swaps and all four-coordinate orthogonal transvections for dimensions \(3\) through \(9\), checks each orbit against the complete parity-and-canonical classification, and checks preservation of its basic invariants. The resulting output ends in `VERIFY_OK`. The finite checks are independent tests, not the proof for arbitrary dimension: arbitrary \(n\) is covered by Step 3.

Reproduce with `python verify.py` in the extracted package directory.

## Relationship to prior work

Kaygorodov, Martín González and Viruel (2026, arXiv:2610.22248v1) pose simultaneous graphical realisation as Question 30 and seek basis-independent graph invariants for nondegenerate evolution algebras in Question 27. Their Proposition 14 provides a related but different orthogonal-symmetry algebra and establishes its automorphism group; Remark 22 gives an example of basis-dependent strong connectivity over fields of characteristic other than two. The present theorem provides the full simultaneous realisation answer **only in the specified nondegenerate one-dimensional-square class over \(\mathbb F_2\)**, not a solution for arbitrary evolution algebras or arbitrary graphs.

Martín Barquero, Martín González and Sánchez-Ortega (2025) give a more general pointed-bilinear-form treatment and isomorphism theory for algebras with one-dimensional square. That formalism provides the natural algebraic setting but does not explicitly classify all natural-basis graph isomorphism types, all reachable support sizes, or simultaneous graphical realisability in this binary class. Boudi, Cabrera Casado and Siles Molina (2020) provide general natural-family and natural-basis change theory, without the present exact graph-spectrum result. The simple three-orbit orthogonal calculation should be interpreted in light of those known frameworks, not as a new general classification of one-dimensional-square algebras.

## Limitations

The theorem requires the exact field \(\mathbb F_2\); arbitrary characteristic-two extensions have nontrivial square scalars and are not addressed. The dimension bound \(n\ge3\) ensures all three graph-spectrum classes are nonempty; dimensions \(1\) and \(2\) are not part of the classification as stated. The conclusion concerns graphs of the specific form \(H_{n,k}\), not all digraphs from arbitrary evolution algebras. The work does not establish priority against every inaccessible preprint or independently validate the results. Computational enumeration is exhaustive only for natural bases in dimensions \(3,4\); orbit generator checks for larger tested dimensions do not replace the all-dimension proof.

## References

1. I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (15 October 2026), especially Proposition 14, Remark 22, Questions 27 and 30. https://arxiv.org/html/2610.22248v1
2. D. Martín Barquero, C. Martín González and J. Sánchez-Ortega, *Commutative Algebras with One-Dimensional Square*, Mediterranean Journal of Mathematics **22**, article 48 (26 February 2025), DOI:10.1007/s00009-025-02812-7. https://doi.org/10.1007/s00009-025-02812-7
3. N. Boudi, J. M. Cabrera Casado and M. Siles Molina, *Natural Families in Evolution Algebras*, arXiv:2006.14460v1 (2020), especially Theorem 2.11 and Corollary 2.13. https://arxiv.org/abs/2006.14460
