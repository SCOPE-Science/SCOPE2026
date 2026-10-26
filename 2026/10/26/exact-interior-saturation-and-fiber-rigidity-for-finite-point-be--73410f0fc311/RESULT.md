# Exact interior saturation and fiber rigidity for finite-point Bergman Schwarz–Pick matrices

## Finding
Let \(B:\mathbb D\to\mathbb D\) be a finite Blaschke product of integer degree \(d\ge2\). For pairwise distinct points \(Z=(z_1,\ldots,z_d)\) define the Hermitian matrices
\[
G_Z=\left[\frac1{(1-z_i\overline{z_j})^2}\right]_{i,j=1}^{d},\qquad
H_{B,Z}=\left[\frac{B'(z_i)\overline{B'(z_j)}}{(1-B(z_i)\overline{B(z_j)})^2}\right]_{i,j=1}^{d}.
\]
Suppose \(w\in\mathbb D\) is a regular value, meaning that \(B'(z)\ne0\) whenever \(B(z)=w\). Its inverse fiber consists of \(d\) distinct points. If \(Z=B^{-1}(w)\), the generalized eigenvalues of \((H_{B,Z},G_Z)\) are **exactly**
\[d,0,\ldots,0.\]
Conversely, if each \(B(z_i)\) is a regular value, and \(d\) is a generalized eigenvalue of \((H_{B,Z},G_Z)\), then \(B(z_1)=\cdots=B(z_d)\), so \(Z\) is a complete regular inverse fiber. Thus the sharp finite-point Schwarz–Pick factor \(d\) is attained inside the disk **if and only if** the regular sampling points form one inverse fiber.

The corresponding inverse-Gram identity, valid for every complete regular fiber, is
\[
\sum_{i,j=1}^{d}\overline{B'(z_i)}(G_Z^{-1})_{ij}B'(z_j)=d(1-|w|^2)^2.
\]
In particular, the generalized spectrum has one eigenvalue \(d\) and \(d-1\) zeros, and the other \(d-1\) directions are null directions for the derivative-data matrix.

## Assumptions and scope
The Bergman space \(A^2(\mathbb D)\) uses normalized area measure and reproducing kernel \(k_z(u)=(1-\bar z u)^{-2}\). A finite Blaschke product is a proper holomorphic disk self-map of degree \(d\). We restrict the converse to \(d\) distinct sampling points whose image values are all regular; critical-value fibers and samples of sizes other than \(d\) are not classified. For Hermitian \(G>0\), generalized eigenvalues of \((H,G)\) are eigenvalues of \(G^{-1/2}HG^{-1/2}\).

## Proof
**1. Proper-map isometry and matrix quotient.** Define the weighted pullback
\[ (Uf)(z)=d^{-1/2}B'(z)f(B(z)). \]
The holomorphic area formula for a proper map of degree \(d\) gives \(\|Uf\|_{A^2}=\|f\|_{A^2}\). The reproducing property gives
\[U^*k_z=d^{-1/2}\overline{B'(z)}k_{B(z)}\]
(with the harmless conjugation depending on which inner-product argument is declared linear). Therefore, writing \(S_Z=\operatorname{span}\{k_{z_1},\ldots,k_{z_d}\}\), the matrix quadratic forms imply \(H_{B,Z}\le dG_Z\), with equality in the extremal generalized eigenvalue precisely when \(S_Z\cap\operatorname{ran}U\) contains a nonzero vector. Indeed \(UU^*\) is the orthogonal projection onto the closed range of the isometry \(U\).

**2. Exact attainment on a regular fiber.** Let \(Z=B^{-1}(w)\), all inverse points simple. By change of variables along the \(d\) local inverse branches, for every \(g\in A^2\) and regular \(w\),
\[ (U^*g)(w)=d^{-1/2}\sum_{B(\zeta)=w}\frac{g(\zeta)}{B'(\zeta)}. \]
This follows by substituting \(u=B(z)\) into the Bergman inner product: the factors \(\overline{B'(z)}\) and the area Jacobian \(|B'(z)|^2\) leave precisely \(1/B'(z)\). If \(g\perp S_Z\), then \(g(\zeta)=0\) at every point of the fiber, hence \((U^*g)(w)=0\). Reproducing at \(w\) yields \(\langle g,Uk_w\rangle=0\) for every \(g\perp S_Z\), whence \(Uk_w\in S_Z\). This is nonzero, so the sharp eigenvalue \(d\) is attained. Since all \(B(z_i)=w\), the matrix \(H\) is rank one, which proves the full spectrum. Its one nonzero generalized eigenvalue equals \( (1-|w|^2)^{-2}b^*G^{-1}b\), with \(b=(B'(z_i))\) under the displayed matrix convention; thus the inverse-Gram identity follows.

**3. Rigidity: a full fiber is necessary.** Assume all values \(B(z_i)\) are regular and the sharp generalized eigenvalue \(d\) is attained. By Step 1 there is a nonzero \(g\in S_Z\cap\operatorname{ran}U\). Thus
\[g(z)=\sum_{i=1}^d\frac{c_i}{(1-\overline{z_i}z)^2}=d^{-1/2}B'(z)f(B(z))\]
for some \(f\in A^2\). The left side is rational on the Riemann sphere and its only possible poles are double poles at the reflected sampling points \(z_i^*=1/\overline{z_i}\), with \(z_i=0\) interpreted as the point at infinity. If it has no finite pole, it is constant. But no nonzero constant belongs to \(\operatorname{ran}U\) when \(d\ge2\): a degree-\(d\) finite Blaschke product has at least one critical point inside the disk, so every function \(Uf\) vanishes there. Consequently some coefficient \(c_i\) with \(z_i\ne0\) is nonzero and \(g\) has an actual double pole at \(z_i^*\).

The rational function \(R=g/B'\) agrees on the disk with the holomorphic function \(d^{-1/2}f\circ B\), so it is constant on every fiber of \(B\) over the disk. Rational identity and continuation of inverse branches imply that it is constant on generic fibers on the sphere. Hence it descends to a rational function \(F\) on the sphere: \(R=F\circ B\). One may see the descent directly by defining \(F\) on any simply connected set avoiding the finitely many critical values using an inverse branch; all branches agree by rational continuation, and the singularities at critical values are meromorphic because \(R\) is rational. Thus \(g=B'F(B)\) as rational functions.

Since \(B\) is a finite Blaschke product, reflection across the unit circle gives \(B(1/\bar z)=1/\overline{B(z)}\). In particular, the exterior point \(z_i^*\) lies over the reflected regular value \(\eta=1/\overline{B(z_i)}\), and the complete inverse image of \(\eta\) consists of the \(d\) reflected points \(1/\overline\zeta\) for \(B(\zeta)=B(z_i)\). None of these inverse points is critical. The double pole of \(g=B'F(B)\) at \(z_i^*\) therefore forces a double pole of \(F\) at \(\eta\), and hence double poles of \(g\) at **all** \(d\) inverse points of \(\eta\). The pole list for \(g\) permits only the \(d\) reflections of the original sampling points. It follows that \(Z\) contains the full regular fiber of \(B(z_i)\). As \(Z\) itself has size \(d\), equality of sets follows.

The case \(z_i^*=\infty\) does not affect the argument: at least one nonzero sampling point with a finite pole was chosen. This proves necessity and completes the theorem.

## Verification
A self-contained Python checker evaluates the exact matrices at degree-two Blaschke products \(B(z)=z(z-a)/(1-az)\) for three values of \(a\) and three regular targets, verifies the generalized spectrum \(\{2,0\}\), and checks that perturbing one inverse-fiber node strictly lowers the top generalized eigenvalue. It is supplementary finite evidence; the proof above is valid for all finite degrees and all regular values.

## Relationship to prior work
Tian's finite-point Schwarz–Pick theorem [1] proves the universal estimate \(H_{B,Z}\le\min\{n,d\}G_Z\), obtaining sharpness from sequences of points approaching the boundary. The present result identifies **finite interior equality**, all generalized eigenvalues on complete regular fibers, and a converse rigidity classification among \(d\) regular sampling points. The weighted Bergman isometry and its adjoint formula are classical proper-map tools (compare Bell [2]); the new issue here is the exact equality configuration and its uniqueness under the regular-value hypothesis. No claim is made that the classical pullback identities themselves are new.

## Limitations
Only finite Blaschke products and exactly \(d\) distinct sampling points are treated; the necessity statement excludes critical image values. The theorem does not characterize near-equality, generic overdetermined sampling, or higher-dimensional proper maps. Historical-priority uncertainty persists: older Bergman proper-map transformation formulas might yield equivalent equality statements after specialized analysis. Independent mathematical validation has not been performed.

## References
[1] James Tian, *A finite-Point Schwarz-Pick Inequality*, arXiv:2608.10443v1, first posted 2026-08-11, Theorem 2.1 and its proof.

[2] Steven R. Bell, *The Bergman kernel function and proper holomorphic mappings*, Transactions of the American Mathematical Society (1982), DOI 10.2307/1999869; cited for classical transformation context, not claimed to have been read in full.
