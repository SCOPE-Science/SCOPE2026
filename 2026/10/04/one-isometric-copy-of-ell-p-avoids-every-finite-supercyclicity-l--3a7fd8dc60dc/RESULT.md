# One isometric copy of \(\ell_p\) avoids every finite supercyclicity level
## Finding
For every \(p>0\), over either \(\mathbb R\) or \(\mathbb C\), there is a linear isometry \(\Phi:\ell_p\to\mathcal L(\ell_p)\) such that every nonzero \(T_\lambda=\Phi(\lambda)\) is injective, has closed range of infinite algebraic codimension, and is not \(N\)-supercyclic for any integer \(N\ge1\). Hence one and the same isometric copy of \(\ell_p\), apart from zero, avoids every finite supercyclicity level.

## Assumptions and scope
Let \(p>0\). For \(p\ge1\), use the usual Banach norm on \(\ell_p\). For \(0<p<1\), use the standard quasi-norm
\[
\|x\|_p=\left(\sum_{i\ge1}|x_i|^p\right)^{1/p},
\]
and the associated quasi-Banach topology. The focal paper uses the equivalent \(p\)-power F-norm in the non-locally-convex case. An operator \(T\) is called \(N\)-supercyclic when there is an \(N\)-dimensional subspace \(W\) for which \(\bigcup_{m\ge0}T^m(W)\) is dense.

Choose a partition \(\{3,4,5,\ldots\}=\bigsqcup_{k\ge1}N_k\) into infinite sets, enumerate \(N_k=\{n_i^{(k)}:i\ge1\}\), and let \(F_k\) copy the input coordinate \(x_i\) to coordinate \(n_i^{(k)}\). For \(\lambda=(\lambda_k)\in\ell_p\), define
\[
T_\lambda=\Phi(\lambda)=\sum_{k\ge1}\lambda_kF_k.
\]
This is exactly the coordinate-replication family used in Theorem 4.1 of the focal source.

## Proof
Because the ranges of the \(F_k\) have disjoint supports,
\[
\|T_\lambda x\|_p^p
=\sum_{k\ge1}\sum_{i\ge1}|\lambda_kx_i|^p
=\|\lambda\|_p^p\,\|x\|_p^p.
\]
Thus \(\Phi\) is an isometry and, when \(\lambda\ne0\), \(T_\lambda\) is bounded below by \(\|\lambda\|_p\). Hence \(T_\lambda\) is injective and its range is closed.

For each \(i\ge1\), put \(M_i=\{n_i^{(k)}:k\ge1\}\). Under the coordinate identification \(\ell_p(M_i)\cong\ell_p\), the restriction of every vector in \(T_\lambda(\ell_p)\) to \(M_i\) is a scalar multiple of \(\lambda\), namely \(x_i\lambda\). Since \(\lambda\ne0\), choose an index \(r\) such that the coordinate vector \(e_r\) is not in \(\operatorname{span}\{\lambda\}\). Define \(z_i=e_{n_i^{(r)}}\). If a finite sum \(\sum_i c_i z_i\) belonged to \(T_\lambda(\ell_p)\), then restriction to each block \(M_i\) would give
\[
c_i e_r=x_i\lambda.
\]
The choice of \(r\) forces \(c_i=0\) for every \(i\). Therefore the cosets \(z_i+T_\lambda(\ell_p)\) are linearly independent, and the closed range has infinite algebraic codimension.

Now fix an integer \(N\ge1\) and let \(q:\ell_p\to\ell_p/T_\lambda(\ell_p)\) be the quotient map. If an \(N\)-dimensional subspace \(W\) had dense orbit under \(T_\lambda\), then
\[
q\left(\bigcup_{m\ge0}T_\lambda^m(W)\right)=q(W),
\]
because \(T_\lambda^m(W)\subseteq T_\lambda(\ell_p)\) whenever \(m\ge1\). Density would force the finite-dimensional space \(q(W)\) to be dense in the infinite-dimensional Hausdorff quotient. Finite-dimensional subspaces of a Hausdorff topological vector space are closed, so this is impossible. Hence \(T_\lambda\) is not \(N\)-supercyclic. Since \(N\) was arbitrary, it avoids every finite supercyclicity class simultaneously.

## Verification
The norm identity is an exact rearrangement of a nonnegative double series. Closedness of the range follows from the resulting lower bound. Infinite codimension is witnessed by the explicit independent quotient classes \(z_i+T_\lambda(\ell_p)\). The dynamical obstruction uses only the quotient map and the inclusion \(T_\lambda^m(W)\subseteq\operatorname{ran}T_\lambda\) for \(m\ge1\). No finite experiment or asymptotic computation is used.

The argument covers both scalar fields and all \(p>0\). For \(0<p<1\), only Hausdorff quasi-Banach/F-space facts are used; local convexity and duality are not needed.

## Relationship to prior work
The focal paper proves that this same \(\Phi\) is an isometric copy of \(\ell_p\) consisting, apart from zero, of injective operators that are non-cyclic and have non-dense range. In a separate section it proves, for each fixed \(N\), spaceability of the complement of the \(N\)-supercyclic operators. It does not state that the Section 4 isometric copy has infinite-codimensional closed ranges or that one fixed isometric copy avoids every finite \(N\) simultaneously.

Bourdon--Feldman--Shapiro prove a general adjoint-eigenvalue restriction for \(N\)-supercyclic operators. That result supplies a broad antecedent for finite-dimensional obstructions but does not produce this isometric \(\ell_p\)-family, and the quotient proof above works directly also in the non-locally-convex range \(0<p<1\). Searches for the simultaneous isometric-copy statement, the infinite-codimensional range formulation, and equivalent finite-supercyclicity formulations did not locate a covering result.

## Limitations
The result concerns the specific coordinate-replication isometric copy and does not classify all operators that fail every finite supercyclicity level. It does not claim maximality of the embedded subspace, optimality among lineability notions, or any statement about infinite-supercyclicity in Feldman's distinct sense.

## References
N. G. Albuquerque, G. Araújo, L. Bernal-González, E. Demétrio Jr., J. Seoane-Sepúlveda, “SOT-large subspaces of non-cyclic operators,” arXiv:2609.27211v1, 2026.

P. S. Bourdon, N. S. Feldman, J. H. Shapiro, “Some properties of \(N\)-supercyclic operators,” Studia Mathematica 165 (2004), 135–157, DOI 10.4064/sm165-2-4.

N. S. Feldman, “\(n\)-supercyclic operators,” Studia Mathematica 151 (2002), 141–159, DOI 10.4064/sm151-2-3.
