# Exact real and complex quadratic Hilbert coefficient constants, with an odd-dimensional gap

## Finding
For a field \(\mathbb K\in\{\mathbb R,\mathbb C\}\), an integer \(n\ge1\), and a homogeneous quadratic polynomial
\[
P(z)=\sum_{j=1}^{n}a_jz_j^2+\sum_{1\le i<j\le n}b_{ij}z_i z_j,
\]
write \(E(P)=\sum_j|a_j|^2+\sum_{i<j}|b_{ij}|^2\) and \(\|P\|=\sup_{\|z\|_2\le1}|P(z)|\). Define \(C_n(\mathbb K)=\sup_{P\ne0} E(P)^{1/2}/\|P\|\). **The exact constants in every dimension are**
\[
\boxed{C_n(\mathbb R)^2=\begin{cases}2n,&n\text{ even},\\2n-1/n,&n\text{ odd},\end{cases}}
\qquad
\boxed{C_n(\mathbb C)^2=\begin{cases}1,&n=1,\\17/3,&n=3,\\2n,&n\ge2,\ n\ne3.\end{cases}}
\]
All values are attained by explicitly constructed polynomials. In particular, the two fields agree for dimensions one, two and three, but differ strictly in every odd dimension at least five. At the exceptional complex dimension three, the deficit relative to the general upper bound is exactly \(1/3\) in squared constant.

## Assumptions and scope
The scalar field is real or complex, the Euclidean norm is the standard \(\ell_2\)-norm, and \(n\) is any positive integer. The coefficient norm counts **one copy** of each monomial \(z_i z_j\) for \(i<j\); it is not the Hilbert--Schmidt norm of the associated symmetric matrix, nor the Bombieri coefficient norm. No sparsity or unimodularity restriction is placed on coefficients. Every estimate and extremizer is exact, not asymptotic.

## Proof
**1. Reduction to symmetric isometries.** Associate to \(P\) the symmetric matrix \(A\) with \(A_{ii}=a_i\) and \(A_{ij}=A_{ji}=b_{ij}/2\) for \(i\ne j\). Then \(P(z)=z^T A z\), and direct accounting gives
\[
E(P)=\sum_i|A_{ii}|^2+4\sum_{i<j}|A_{ij}|^2
=2\|A\|_F^2-\sum_i|A_{ii}|^2. \tag{1}
\]
For real symmetric \(A\), the spectral theorem gives \(\|P\|=\|A\|_{\mathrm{op}}\). For complex symmetric \(A\), Takagi factorization \(A=V\operatorname{diag}(s_1,\ldots,s_n)V^T\), with unitary \(V\) and nonnegative singular values \(s_i\), gives the same equality: the triangle bound proves \(\|P\|\le s_1\), and a conjugated Takagi vector attains \(s_1\).

The unit ball of real symmetric matrices is the convex hull of real symmetric orthogonal matrices: diagonalize \(A=Q\operatorname{diag}(\lambda_i)Q^T\) and express every \(\lambda_i\in[-1,1]\) as a convex combination of \(\pm1\). The analogous statement for complex symmetric matrices follows from Takagi factorization and expressing each \(s_i\in[0,1]\) as a convex combination of signs: every \(V\operatorname{diag}(\varepsilon_i)V^T\), \(\varepsilon_i\in\{-1,1\}\), is symmetric unitary. The Euclidean coefficient norm \(E(P)^{1/2}\) is convex in \(A\). Thus its maximum over symmetric contractions is attained at a symmetric orthogonal/unitary matrix, respectively. For such a matrix \(U\), \(\|U\|_F^2=n\), so by (1)
\[
C_n(\mathbb K)^2=2n-\min_{U}\delta(U),\qquad
\delta(U)=\sum_{i=1}^n|U_{ii}|^2, \tag{2}
\]
where \(U\) ranges over symmetric orthogonal matrices if \(\mathbb K=\mathbb R\) and symmetric unitary matrices if \(\mathbb K=\mathbb C\). All minima exist by compactness.

**2. The real field.** When \(n\) is odd, a real symmetric orthogonal \(U\) has eigenvalues \(\pm1\), so its trace is a nonzero odd integer. Cauchy--Schwarz therefore gives
\[
\delta(U)\ge\frac{|\operatorname{tr}U|^2}{n}\ge\frac1n.\tag{3}
\]
This is sharp. Write \(r=(n+1)/2\), index coordinates by \(j=0,\ldots,n-1\), and take an \(r\)-dimensional subspace spanned by \(\lfloor r/2\rfloor\) full real Fourier frequency pairs
\[
\left(\sqrt{2/n}\cos(2\pi kj/n)\right)_j,\qquad
\left(\sqrt{2/n}\sin(2\pi kj/n)\right)_j
\]
for \(k=1,\ldots,\lfloor r/2\rfloor\), together with the constant unit vector \((1/\sqrt n)_j\) if \(r\) is odd. (For \(n=1\), only the constant vector is used.) These vectors are orthonormal. Their orthogonal projection \(Q\) has constant diagonal \(Q_{jj}=r/n\), since each sine--cosine pair contributes \(2/n\) to every diagonal entry. The symmetric orthogonal reflection \(U=2Q-I\) has \(U_{jj}=2r/n-1=1/n\), so \(\delta(U)=1/n\). This proves the odd real formula. When \(n\) is even, take a direct sum of \(2\times2\) transposition matrices \(\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\). It is symmetric orthogonal with zero diagonal, giving \(\delta(U)=0\). Equation (2) proves both real branches.

**3. The complex field in dimensions one and three.** For \(n=1\), any unitary has squared diagonal modulus one, so \(C_1(\mathbb C)^2=1\). For \(n=3\), let \(U\) be any complex symmetric unitary and put \(d_i=|U_{ii}|\), \(\delta=\sum_i d_i^2\). Its diagonal cofactor identity, from \(\operatorname{adj} U=(\det U)U^*\), reads
\[
U_{jj}U_{kk}-U_{jk}^{2}=(\det U)\overline{U_{ii}}
\]
for each permutation \((i,j,k)\) of \((1,2,3)\). Consequently \(|U_{jk}|^2\le d_jd_k+d_i\). Summing over the three off-diagonal positions and using orthonormal rows yields
\[
\frac{3-\delta}{2}=\sum_{i<j}|U_{ij}|^2
\le\sum_i d_i+\sum_{i<j}d_i d_j
\le\sqrt{3\delta}+\delta.\tag{4}
\]
The last inequalities use Cauchy--Schwarz and \(\sum_{i<j}d_i d_j\le\delta\). The right-minus-left difference is strictly increasing as a function of \(\delta\ge0\), and vanishes at \(\delta=1/3\); hence \(\delta\ge1/3\). Equality holds for
\[
U=I_3-\frac23\mathbf 1\mathbf 1^T,
\]
a real symmetric orthogonal Householder matrix with all diagonal entries \(1/3\). Thus by (2), \(C_3(\mathbb C)^2=6-1/3=17/3\). This also rules out a zero-diagonal complex symmetric unitary in dimension three.

**4. Complex zero-diagonal constructions in every other dimension.** Even dimensions have the symmetric transposition-block examples from Step 2. In dimension five let \(\zeta=e^{2\pi i/5}\) and \(F=(5^{-1/2}\zeta^{jk})_{j,k=0}^4\), the unitary Fourier matrix. Choose \(\theta\) with \(\cos\theta=-1/4\) and define
\[
D=\operatorname{diag}(1,e^{i\theta},e^{-i\theta},e^{-i\theta},e^{i\theta}),\qquad U_5=F^*DF.
\]
The five diagonal entries of \(D\) are unimodular and invariant under the index reflection \(k\mapsto5-k\). Therefore \(U_5\) is both unitary and symmetric (the reflected Fourier coefficients coincide). Every diagonal entry of \(U_5\) equals \((1+4\cos\theta)/5=0\). For any odd \(n\ge5\), adjoining \((n-5)/2\) transposition blocks yields a symmetric zero-diagonal unitary of size \(n\). Hence \(\delta(U)=0\), which with (2) gives the stated \(2n\) branch. The explicit matrices, mapped back to polynomials via Step 1, attain every asserted constant.

## Verification
All critical nonstandard points are proved above: the coefficient normalization (1); reduction to symmetric unitaries (2); the odd real trace obstruction and constant-diagonal Fourier projection (3); and the three-dimensional cofactor inequality (4). For a symmetric orthogonal/unitary extremizer with \(\delta(U)\), direct coefficient evaluation gives \(E(P)=2n-\delta(U)\) and \(\|P\|=1\). Therefore the examples attain the constants and are not merely lower-bound witnesses. The five-dimensional construction uses the exact identities \(\cos\theta=-1/4\) and \(\sum\operatorname{diag}D=0\), not numerical approximation. Supplementary floating-point checks of unitary/symmetry identities in dimensions two through nine are consistent but are unnecessary for the infinite family proof.

## Relationship to prior work
Barbosa, Núñez-Alarcón, Raposo and Santos (arXiv:2610.01500v1) investigate sparse Kahane--Salem--Zygmund forms and critical weighted Hardy--Littlewood polynomial coefficient problems; their public abstract identifies **sharp powers of dimension** in the diagonal polynomial coefficient-versus-supremum-norm setting including the Hilbert endpoint. The present theorem instead treats the natural quadratic exponent-two coefficient norm and computes **all finite-dimensional exact constants**, including a real/complex distinction and a three-dimensional complex obstruction. The arXiv full text could not be inspected, so implicit coverage in its main text or appendices is a specific unresolved literature risk. Raposo and Serrano-Rodríguez, *Coefficients of Multilinear Forms on Sequence Spaces* (2023), give optimal exponents for multilinear norms under separate exponent hypotheses; the inspected full open-access text does not provide the stated finite quadratic coefficient constants. Classical spectral/Takagi and Fourier facts are used as ingredients and are not claimed as new.

## Limitations
The claim concerns degree two, the Euclidean unit ball, and the unweighted \(\ell_2\)-norm of **distinct monomial** coefficients. It does not transfer unchanged to Bombieri coefficients, multilinear tensor coefficients, arbitrary degrees or unequal \(\ell_p\) norms. Literature searches and one accessible full-text comparison do not constitute a uniqueness proof, and the inaccessible full text of arXiv:2610.01500 leaves a concrete originality risk. No independent audit has been performed.

## References
1. A. Barbosa, D. Núñez-Alarcón, A. Raposo, J. Santos, *Sparse Kahane--Salem--Zygmund Forms and Weighted Hardy--Littlewood Inequalities Across the Critical Endpoint*, arXiv:2610.01500v1 (first publicly submitted 2026-10-01).
2. A. Raposo Jr. and D. M. Serrano-Rodríguez, *Coefficients of Multilinear Forms on Sequence Spaces*, Bulletin of the Brazilian Mathematical Society, New Series **54** (2023), article 43, DOI: 10.1007/s00574-023-00359-3.
3. D. M. Pellegrino and A. Raposo, *Hilbertian Kahane--Salem--Zygmund Inequalities: Extremizers and Quantitative Gaps*, arXiv:2608.08246 (related sign-form setting).
