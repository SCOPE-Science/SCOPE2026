# Laplacian factorization and an eigenspace transition for rank-two parallel-class matroid polytopes

## Finding
Fix integers \(p\ge2\) and \(q\ge3\). Let \(M_{p,q}\) be the loopless rank-two matroid with one parallel class of size \(p\) and \(q\) further singleton parallel classes. Let \(G_{p,q}\) denote the one-skeleton of its base polytope, and \(L_{p,q}\) the ordinary, unweighted combinatorial graph Laplacian. Put
\[
 E=pq+\binom q2,\qquad T=p+2q-1,\qquad S=p+q-1,\qquad U=2p+2q-2,
\]
\[
 W(t)=t^2-(2p+3q-1)t+q(3p+2q-1).
\]
The **complete characteristic polynomial**, including multiplicities, is
\[
\boxed{\det(tI-L_{p,q})=t(t-2p-q+1)(t-T)^{(p-1)(q-1)}
(t-S)^{p-1}(t-U)^{q(q-3)/2}W(t)^{q-1}.}
\]
In particular, the exact number of undirected spanning trees is
\[
\boxed{\tau(G_{p,q})=\frac{2p+q-1}{E}
T^{(p-1)(q-1)}S^{p-1}U^{q(q-3)/2}
\bigl[q(3p+2q-1)\bigr]^{q-1}.}
\]
Define
\[
\lambda_- =\frac{2p+3q-1-\sqrt{(q-1)^2+4p(p-1)}}2.
\]
Then the algebraic connectivity and the dimension of its eigenspace have a **sharp two-parameter transition**:
\[
 \lambda_2(G_{p,q})=\min\{S,\lambda_-\},\qquad
 \operatorname{mult}(\lambda_2)=
 \begin{cases}
 q-1,&q<p(p-1),\\
 p+q-2,&q=p(p-1),\\
 p-1,&q>p(p-1).
 \end{cases}
\]
(The equality line occurs in the stated domain only for \(p\ge3\).)

## Assumptions and scope
The base set of \(M_{p,q}\) consists of the two-element subsets of a ground set \(I\sqcup C\), where \(|I|=p\), \(|C|=q\), excluding precisely the pairs contained in \(I\). Its base polytope is
\[
 P_{p,q}=\operatorname{conv}\{e_a+e_b:\{a,b\}\text{ is a base of }M_{p,q}\}\subset\mathbb R^{p+q}.
\]
Here the vertex-edge graph is the ordinary basis-exchange graph: two distinct bases are adjacent exactly when their intersection has size one. Equivalently, take the complete split graph \(H_{p,q}=K_q\vee\overline{K_p}\) on vertex parts \(C\) and \(I\): its edges are exactly the bases, and \(G_{p,q}=L(H_{p,q})\), the line graph. No graph edges carry weights. The graph \(G_{p,q}\) has \(E\) vertices, is connected, and the eigenvalues of its combinatorial Laplacian are nonnegative.

## Proof
**1. Laplacian as a signless-incidence Gram perturbation.** Index \(\mathbb R^E\) by the edges of \(H_{p,q}\). Let \(B\) be the unsigned \((p+q)\)-by-\(E\) incidence matrix: each column has a \(1\) at each endpoint. For distinct edges, \((B^{\mathsf T}B)_{ef}\) is \(1\) if the edges share an endpoint and \(0\) otherwise, and the diagonal is \(2\). Hence \(A(G_{p,q})=B^{\mathsf T}B-2I\). Since an edge \(uv\) of \(H_{p,q}\) is adjacent in the line graph to \(d_H(u)+d_H(v)-2\) other edges, the line-graph Laplacian is
\[
 L_{p,q}=D-B^{\mathsf T}B,
\]
where \(D\) is diagonal with value \(T=p+2q-1\) on the \(pq\) edges of type \(I\)-\(C\), and \(U=2p+2q-2\) on the \(\binom q2\) edges of type \(C\)-\(C\). We now give an orthogonal decomposition of the entire edge coordinate space.

**2. Independent-part contrasts.** Regard the \(I\)-\(C\) coordinates as a \(p\)-by-\(q\) matrix. Matrices having every row sum and every column sum equal to zero form a \((p-1)(q-1)\)-dimensional subspace of \(\ker B\) and therefore have Laplacian eigenvalue \(T\). Matrices constant along each row, with row constants summing to zero, form another \((p-1)\)-dimensional subspace. Their \(B^{\mathsf T}B\) eigenvalue is \(q\), so their Laplacian eigenvalue is \(T-q=S\).

**3. Clique-edge kernel.** In the \(C\)-\(C\) edge coordinates, vectors in the kernel of the unsigned incidence matrix of \(K_q\) have eigenvalue \(U\). For \(q\ge3\), this incidence matrix has row rank \(q\): if a row-dependence has coefficients \(a_j\), then \(a_j+a_k=0\) for every distinct pair, and a triangle forces all coefficients zero. Consequently the dimension is \(\binom q2-q=q(q-3)/2\).

**4. Coupled clique contrasts.** For each vector \(v\in\mathbb R^q\) with \(\sum_jv_j=0\), consider \(y_{ij}=v_j\) in the \(I\)-\(C\) block and \(z_{jk}=v_j+v_k\) in the \(C\)-\(C\) block. Their squared norms are \(p\|v\|^2\) and \((q-2)\|v\|^2\), respectively; the vectors associated with orthogonal \(v\)'s are mutually orthogonal. On the two normalized coordinates \(y/\sqrt p\) and \(z/\sqrt{q-2}\), the Gram matrix \(B^{\mathsf T}B\) is
\[
 \begin{pmatrix}p&\sqrt{p(q-2)}\\\sqrt{p(q-2)}&q-2\end{pmatrix}.
\]
Subtracting it from \(D\) gives the symmetric Laplacian block
\[
 M=\begin{pmatrix}2q-1&-\sqrt{p(q-2)}\\-\sqrt{p(q-2)}&2p+q\end{pmatrix}.
\]
Its characteristic polynomial is exactly \(W(t)\), its two eigenvalues are
\[
 \lambda_\pm=\frac{2p+3q-1\pm\sqrt{(q-1)^2+4p(p-1)}}2,
\]
and the block repeats once for each of the \(q-1\) independent clique contrasts.

**5. Constant coordinates.** The normalized all-ones vector in the \(I\)-\(C\) coordinates and that in the \(C\)-\(C\) coordinates span the two remaining invariant directions. Their Laplacian block is
\[
 M_0=\begin{pmatrix}q-1&-\sqrt{2p(q-1)}\\-\sqrt{2p(q-1)}&2p\end{pmatrix}.
\]
Its characteristic polynomial is \(t(t-2p-q+1)\). The subspace dimensions sum to
\[
 (p-1)(q-1)+(p-1)+\frac{q(q-3)}2+2(q-1)+2=E,
\]
so the decomposition is exhaustive and proves the displayed characteristic polynomial, including all multiplicities.

**6. Spanning trees.** Since \(G_{p,q}\) is connected, the matrix-tree theorem says its number of spanning trees is the product of the \(E-1\) nonzero Laplacian eigenvalues divided by \(E\). The roots of \(W\) have product \(q(3p+2q-1)\). Multiplying the nonzero factors yields the stated integer product formula without any assumptions about simple roots or integrality of individual eigenvalues.

**7. Sharp gap transition and multiplicity.** For \(p\ge2\), \(q\ge3\), the eigenvalues \(T,U,2p+q-1\) are each strictly larger than \(S\); and \(\lambda_+>S\). Thus only \(S\) and \(\lambda_-\) can be smallest positive. A direct identity is
\[
 W(S)=q-p(p-1).
\]
As \(S<\lambda_+\), the sign of \(W(S)=(S-\lambda_-)(S-\lambda_+)\) shows \(\lambda_-<S\) exactly when \(q<p(p-1)\), with equality on \(q=p(p-1)\). The spectral blocks supply the claimed multiplicities; no other block has this eigenvalue.

## Verification
The standalone script `VERIFY.py` independently constructs the exchange graph from its allowed two-element bases, forms its exact integer Laplacian, and checks its characteristic polynomial and a Kirchhoff cofactor against the formulas for \((p,q)=(2,3),(3,3),(2,4),(3,4),(4,3),(2,5),(3,5)\). All seven comparisons passed. It also checks the critical symbolic identities for the discriminant and \(W(S)\), and exact equality examples on \(q=p(p-1)\) for \(3\le p\le14\). These are **finite checks only**; the uniform theorem follows from Steps 1–7 rather than a finite experimental extrapolation. Run `python3 VERIFY.py` with SymPy installed.

## Relationship to prior work
Pineda-Villavicencio and Schröter [1] show the geometric significance of basis exchange graphs and exhibit, in their Example 22, the initial \((p,q)=(2,3)\) parallel-pair polytope with nine vertices. They establish reconstructibility properties, not the Laplacian factorization or the two-parameter connectivity transition. The general line-graph spanning-tree formulas of Dong and Yan [2], Dong [3], and Gong and Jin [4] cover spanning-tree enumeration of any connected line graph **implicitly**. The expression above is therefore **not** asserted as the first possible derivation of the tree count from a general identity: its distinction is the explicitly evaluated two-parameter product together with the full polytope-graph spectrum and exact eigenmode phase boundary. Related published spectral formulas [5,6] for the *underlying* complete split graph do not determine the nonregular line graph's Laplacian merely by a regular-line-graph shift. A mathematically equivalent specialized evaluation under alternate graph terminology remains a literature-search risk.

## Limitations
The claims concern only one nontrivial parallel class and \(q\) singleton classes, with \(p\ge2\), \(q\ge3\); they do not classify all rank-two matroids. The characteristic polynomial is for the **unweighted combinatorial Laplacian**, not the normalized or signless Laplacian. The existence of general spanning-tree formulas for arbitrary line graphs is acknowledged and limits what can be claimed about originality of the count alone. The computations support, but cannot establish, statements for arbitrarily large parameters.

## References
1. G. Pineda-Villavicencio and B. Schröter, *Reconstructibility of Matroid Polytopes*, arXiv:2010.10227 (first posted 2020-10-20), especially Example 22; primary MSC2020 52B11.
2. F. Dong and W. Yan, *Expression for the Number of Spanning Trees of Line Graphs of Arbitrary Connected Graphs*, arXiv:1507.08022 (2017 version), particularly Theorem 1.1 and equation (1.5).
3. F. Dong, *Formulas counting spanning trees in line graphs and their extensions*, arXiv:1907.07376 (2019), especially Corollary 1.1.
4. H. Gong and X. Jin, *A simple formula for the number of spanning trees of line graphs*, Journal of Graph Theory, DOI:10.1002/jgt.22212 (2018).
5. Pinheiro and Trevisan, *Maximality of the signless Laplacian energy*, Discrete Mathematics, DOI:10.1016/j.disc.2017.06.021 (2017), for the related but different signless Laplacian of complete split graphs.
6. K. C. Das and M. Liu, *Complete split graph determined by its (signless) Laplacian spectrum*, Discrete Applied Mathematics 205 (2016), 45–51, DOI:10.1016/j.dam.2016.01.003; this is the underlying graph, not its line graph.
