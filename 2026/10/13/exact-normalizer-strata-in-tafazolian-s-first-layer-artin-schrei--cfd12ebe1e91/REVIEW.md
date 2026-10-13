# Self-review

## Correctness
PASS. Tafazolian's Corollary 1.8 identifies the normalizer quotient with the stabilizer of the Artin--Schreier plane under
\[
D_\lambda(a,b)=(\lambda^{-1}a,\lambda b),
\qquad
J(a,b)=(b,a).
\]
For the first normal form, preservation forces \(\lambda^2=1\), so the quotient is exactly \(C_2\times C_2\).

For the second normal form, with \(r=a/b\), the matrix of \(D_\lambda\) in the natural \(\mathbf F_p\)-basis is
\[
\begin{pmatrix}
c&d/r\\
rd&c
\end{pmatrix},
\qquad
c=\frac{\lambda+\lambda^{-1}}2,\quad
d=\frac{\lambda^{-1}-\lambda}2.
\]
A symmetry beyond \(\lambda=\pm1\) forces \(r^2\in\mathbf F_p\). On that locus the diagonal stabilizer is the norm-one subgroup of \(\mathbf F_{p^2}^*\), cyclic of order \(p+1\); the branch-swap involution acts by inversion, so the quotient is dihedral of order \(2(p+1)\). Multiplication by \(|S|=p^2\) gives the stated normalizer orders.

## Originality
PASS. The initiating paper gives the two normal forms, the stabilizer interpretation of the normalizer, and a universal Klein-four subgroup, but it does not state the exact stabilizer stratification. Its relevant remark stops at the lower bound \(4p^2\) and finiteness information in the second normal form. Targeted searches for the exact orders, the dihedral quotient, the square-class criterion, and the norm-one formulation found no covering statement. The inspected older ordinary-curve literature treats bounds and special families rather than this rank-two first-layer moduli problem.

## Value
PASS. The finding completes a natural invariant emphasized by the source and turns the two first-layer normal forms into an exact automorphism-normalizer stratification. In particular, it identifies a genuine enhanced-symmetry locus where the normalizer jumps from the universal minimum \(4p^2\) to \(2p^2(p+1)\), with a conceptual norm-one-torus explanation.

The result concerns the normalizer of the distinguished Sylow \(p\)-subgroup, not necessarily the full automorphism group.

Self-review: passed. Independent audit: not yet performed.
