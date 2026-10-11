# Exact Fourier-algebra norm from induced edges in symmetric rank-three actions

## Finding
Let a finite group \(G\) act transitively with symmetric permutation rank three on a set \(\Omega\) of size \(n\), fix \(\alpha\in\Omega\), and let \(X\) be either nontrivial undirected orbital graph. Write \(k\) for the valency of \(X\), \(\theta>\tau\) for its two nontrivial adjacency eigenvalues, and \(d_\theta,d_\tau\) for their multiplicities. For \(J\subseteq\Omega\), put \(r=|J|\), let \(e_X(J)\) be the number of edges of \(X\) induced by \(J\), and define \(A_J=\{g\in G:g\alpha\in J\}\). With normalized counting measure and Fourier-algebra norm equal to the sum of the singular values of the normalized left-convolution operator, one has
\[
\|1_{A_J}\|_{A(G)}=\frac r n+\sqrt{\frac{d_\theta q_\theta}{n}}+\sqrt{\frac{d_\tau q_\tau}{n}},
\]
where
\[
q_\theta=\frac{2e_X(J)-\tau r-(k-\tau)r^2/n}{\theta-\tau},\qquad
q_\tau=\frac{\theta r-2e_X(J)+(k-\theta)r^2/n}{\theta-\tau}.
\]
Consequently the Fourier-algebra norm of a union of point-stabilizer cosets in any symmetric rank-three action depends on the chosen cosets only through \((r,e_X(J))\).

## Assumptions and scope
The action is finite, transitive, and of symmetric permutation rank three. Thus the stabilizer \(H=G_\alpha\) has three orbits on \(\Omega\): \(\{\alpha}\), the neighbors of \(\alpha\) in \(X\), and the nonneighbors of \(\alpha\). The nontrivial orbital is assumed self-paired, so \(X\) is an undirected strongly regular graph. The function \(1_{A_J}\) is the indicator of the union of the \(r\) right cosets of \(H\) corresponding to \(J\). Convolution uses Haar probability measure on \(G\).

## Proof
Let \(\pi\) be the permutation representation of \(G\) on \(\mathbb C^\Omega\). Rank three means that the commutant of \(\pi(G)\) has dimension three. Because the two nontrivial orbitals are self-paired, this commutant is the commutative algebra spanned by the identity, the adjacency matrix \(B\) of \(X\), and the all-ones matrix. Hence
\[
\mathbb C^\Omega=\mathbf 1\oplus V_\theta\oplus V_\tau
\]
with \(V_\theta,V_\tau\) irreducible, inequivalent, and of dimensions \(d_\theta,d_\tau\); the adjacency matrix acts there by \(\theta\) and \(\tau\).

For an irreducible unitary representation \(\rho\), write
\[
\widehat f(\rho)=\frac1{|G|}\sum_{g\in G}f(g)\rho(g).
\]
The regular representation decomposition gives
\[
\|f\|_{A(G)}=\sum_{\rho\in\widehat G}d_\rho\|\widehat f(\rho)\|_{S_1}.
\]
Choose representatives \(g_\omega\) with \(g_\omega\alpha=\omega\). Since \(|H|/|G|=1/n\),
\[
\widehat{1_{A_J}}(\rho)=\frac1n\sum_{\omega\in J}\rho(g_\omega)P_{\rho,H},
\]
where \(P_{\rho,H}\) is the orthogonal projection onto the \(H\)-fixed vectors. Frobenius reciprocity and the displayed permutation-module decomposition show that only \(\mathbf1,V_\theta,V_\tau\) contribute and that each relevant \(H\)-fixed space is one-dimensional.

Let \(P_\theta,P_\tau\) be the orthogonal projectors in \(\mathbb C^\Omega\). Transitivity gives \(\|P_\theta e_\omega\|^2=d_\theta/n\) and \(\|P_\tau e_\omega\|^2=d_\tau/n\). Therefore the normalized spherical orbit vectors are
\[
u_{\theta,\omega}=\sqrt{n/d_\theta}P_\theta e_\omega,\qquad
u_{\tau,\omega}=\sqrt{n/d_\tau}P_\tau e_\omega.
\]
Each nontrivial Fourier block is rank one, so its trace norm is the Euclidean norm of the appropriate spherical-vector sum divided by \(n\). Consequently the two nontrivial contributions to \(\|1_{A_J}\|_{A(G)}\) are
\[
\sqrt{\frac{d_\theta}{n}\,1_J^*P_\theta1_J},\qquad
\sqrt{\frac{d_\tau}{n}\,1_J^*P_\tau1_J}.
\]
The trivial block contributes \(r/n\).

The spectral projectors are
\[
P_\theta=\frac{B-\tau I-(k-\tau)P_0}{\theta-\tau},\qquad
P_\tau=\frac{\theta I-B+(k-\theta)P_0}{\theta-\tau},
\]
where \(P_0=n^{-1}\mathbf1\mathbf1^*\). Since \(1_J^*B1_J=2e_X(J)\), \(1_J^*1_J=r\), and \(1_J^*P_01_J=r^2/n\), these quadratic forms are exactly \(q_\theta\) and \(q_\tau\), proving the formula. Their nonnegativity is automatic because they are squared projection norms.

## Verification
The accompanying `verify.py` performs an exhaustive exact-rational check on the rank-three action of \(S_4\) on its six two-element subsets. For all \(64\) choices of \(J\), it constructs the actual \(24\times24\) unnormalized convolution matrix, forms its Gram matrix, and verifies the complete nonzero spectrum by exact Gaussian elimination. It then compares the resulting nuclear norm with the displayed formula. The replay result is `VERIFY_OK exact_convolution_cases=64 max_numeric_error=2.220e-16`.

The computation is corroborative. The proof above is uniform in \(G\), \(n\), and \(J\), and does not infer an infinite statement from the finite check.

## Relationship to prior work
Sanders defines the same finite-group Fourier-algebra norm through singular values of normalized convolution and proves that a single subgroup coset has norm \(1\); his quantitative non-abelian idempotent theorem gives structural control for general small-norm indicators. Those results do not evaluate the norm of a prescribed union of point-stabilizer cosets, and their triangle-inequality consequence gives only a coarse bound by the number of cosets. Forrest, Samei, and Spronk develop Fourier algebras on coset spaces and their operator-space and amenability properties, but the inspected full text does not give this finite rank-three indicator formula. Sanders's later coset-decision-tree work gives general structural bounds, not an exact rank-three trace norm.

The new point is the exact reduction of the nonabelian algebra norm to the two strongly-regular spectral projections, after which the entire dependence on \(J\) collapses to its cardinality and one induced-edge statistic.

## Limitations
The result requires a symmetric rank-three action. It does not assert a corresponding two-parameter collapse for nonsymmetric rank-three actions or for higher-rank actions. The literature comparison found no statement of this exact norm identity, but an equivalent calculation could exist in older Gelfand-pair, association-scheme, or spherical-function terminology; that residual terminology risk is retained explicitly.

## References
1. T. Sanders, *A quantitative version of the non-abelian idempotent theorem*, arXiv:0912.0308v1 (first public 2009-12-02); Geom. Funct. Anal. 21 (2011), 141–221, DOI 10.1007/s00039-010-0107-2.
2. B. E. Forrest, E. Samei, N. Spronk, *Convolutions on compact groups and Fourier algebras of coset spaces*, arXiv:0705.4277 (2007); Studia Math. 196 (2010), 223–249.
3. T. Sanders, *Coset decision trees and the Fourier algebra*, arXiv:1805.02168v1 (2018); J. Anal. Math. 144 (2021), 227–259.
