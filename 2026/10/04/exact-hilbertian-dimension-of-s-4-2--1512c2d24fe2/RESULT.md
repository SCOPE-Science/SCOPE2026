# Exact Hilbertian dimension of \(S_4^2\)
## Finding
The largest integer \(k\) for which there exists a complex-linear isometric embedding
\[
\ell_2^k(\mathbb C)\longrightarrow S_4^2
\]
is \(k=2\). Consequently, the least integer \(n\) for which
\[
\ell_2^3(\mathbb C)\longrightarrow S_4^n
\]
admits a complex-linear isometric embedding is \(n=3\).

## Assumptions and scope
Here \(S_4^n\) is the space of \(n\times n\) complex matrices with Schatten \(4\)-norm, and all embeddings are complex-linear. The assertion is specific to the exact isometric problem. It does not classify approximately Euclidean subspaces, real-linear embeddings, or Hilbertian subspaces of \(S_p^n\) for general \(p\) and \(n\).

## Proof
Assume for contradiction that an isometry \(T:\ell_2^3(\mathbb C)\to S_4^2\) exists. Put
\[
h(x)=\|Tx\|_2^2=x^*Hx,
\qquad
q(x)=\det(Tx),
\]
where \(H\) is a positive Hermitian \(3\times3\) matrix and \(q\) is a homogeneous holomorphic quadratic polynomial.

For every \(2\times2\) complex matrix \(A\),
\[
\|A\|_4^4=\operatorname{Tr}((A^*A)^2)
=(\operatorname{Tr}A^*A)^2-2\det(A^*A)
=\|A\|_2^4-2|\det A|^2.
\]
Since \(T\) is an isometry,
\[
2|q(x)|^2=(x^*Hx)^2-\|x\|_2^4. \tag{1}
\]
The right side is nonnegative, so \(H\ge I\). After a unitary change of coordinates in the source, write \(H=\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3)\) with every \(\lambda_j\ge1\). Equation (1) becomes
\[
2|q(x)|^2=
\sum_j(\lambda_j^2-1)|x_j|^4
+2\sum_{i<j}(\lambda_i\lambda_j-1)|x_i|^2|x_j|^2. \tag{2}
\]
Hence \(|q|\) is invariant under independent rotations of the coordinates.

A nonzero homogeneous holomorphic polynomial whose modulus is invariant under the coordinate torus must be a single monomial. Indeed, for each torus element \(u\), the polynomials \(q(u\cdot x)\) and \(q(x)\) have the same modulus. On any open ball avoiding the zero set of \(q\), their quotient is holomorphic with constant modulus, hence is constant; polynomial identity then gives \(q(u\cdot x)=\chi(u)q(x)\). Thus \(q\) is a torus weight vector, and a homogeneous weight space is spanned by one monomial.

Since \(q\) has degree two, it is either \(c x_i^2\) or \(c x_i x_j\) if it is nonzero. In the first case, comparison in (2) first forces \(\lambda_j=1\) for \(j
e i\), then the mixed coefficient forces \(\lambda_i=1\), contradicting \(c
e0\). In the second case, the three pure fourth-power coefficients force every \(\lambda_j=1\), and then the mixed coefficient supporting \(|c x_i x_j|^2\) also vanishes, again contradicting \(c
e0\). Therefore \(q=0\).

Equation (1) now gives \(H=I\), and every matrix in \(T(\mathbb C^3)\) is singular. But a complex linear subspace of \(M_2(\mathbb C)\) consisting only of singular matrices has dimension at most two. To see this directly, normalize a nonzero rank-one member to \(E_{11}\) by invertible left and right multiplications. If \(B=(b_{ij})\) belongs to the transformed subspace, then
\[
0=\det(E_{11}+tB)=t b_{22}+t^2\det B
\]
for every \(t\), so \(b_{22}=0\) and \(b_{12}b_{21}=0\). The projection onto \((b_{12},b_{21})\) is a linear subspace contained in the union of the two coordinate axes, hence in one axis. The whole singular subspace therefore has dimension at most two, contradicting injectivity of \(T\).

The lower bounds are attained. The first-row map \((z_1,z_2)\mapsto\begin{pmatrix}z_1&z_2\0&0\end{pmatrix}\) is an isometric embedding \(\ell_2^2(\mathbb C)\to S_4^2\). Likewise, placing \((z_1,z_2,z_3)\) in the first row of a \(3\times3\) matrix gives an isometric embedding \(\ell_2^3(\mathbb C)\to S_4^3\). Thus the two asserted dimensions are exact.

## Verification
The proof uses only exact identities. The Schatten identity follows from the two eigenvalues of \(A^*A\). The torus step is an algebraic consequence of modulus invariance, and the final singular-subspace bound is proved directly by a determinant polynomial. No finite experiment or numerical approximation is used.

## Relationship to prior work
Xu, Zhang, and Liu classify complex-linear isometric embeddings \(\ell_q^2(\mathbb C)\to S_p^n\): they exist exactly for \(q=p\) or \(q=2\). They explicitly state that their theorem does not determine the least target size for a prescribed higher-dimensional Hilbertian source and that the Hilbertian dimension problem lies beyond their scope. The present result addresses the first higher-dimensional Hilbertian target-size instance at \(p=4\), source dimension three, and target size two.

The 2026 survey of Chattopadhyay, Pradhan, and Skripka summarizes the broader Schatten isometric-embedding problem and records canonical Hilbert-to-Schatten embeddings, but it does not state this exact \(S_4^2\) Hilbertian-dimension calculation.

## Limitations
The argument exploits the special quartic identity for \(2\times2\) matrices. It does not by itself determine maximal Hilbertian dimensions in \(S_4^n\) for \(n\ge3\), nor does it extend automatically to other even Schatten exponents. A residual originality risk is that the same low-dimensional fact may appear in older literature under a classification of Euclidean or Hilbertian subspaces of Schatten classes rather than under the target-size language used here.

## References
1. Y. Xu, W. Zhang, Q. Liu, “Further Results on the Isometric Embeddability of \(S_q^m\) into \(S_p^n\),” arXiv:2609.37504v1, 2026.
2. A. Chattopadhyay, C. Pradhan, A. Skripka, “Isometric Embeddability of Schatten Classes Revisited,” arXiv:2603.07359v2, 2026.
3. A. Chattopadhyay, G. Hong, A. Pal, C. Pradhan, S. K. Ray, “Isometric embeddability of \(S_q^m\) into \(S_p^n\),” Journal of Functional Analysis 282 (2022), 109281.
