# A second harmonic-index resonance of the nine Hesse lines and its sharp charge-three cutoff

## Finding
Let \(\omega=e^{2\pi i/3}\). For \(a,b\in\{0,1,2\}\), set \(v_{a,b}\) to be the cyclic shift by \(a\) coordinates of \((0,1,-\omega^b)/\sqrt2\). These nine unit vectors represent the Hesse SIC configuration in \(\mathbb C^3\). For every integer \(q\ge0\), let \(\mathcal H_q:=\operatorname{Harm}(q+3,q)\) be the complex bihomogeneous harmonic subspace on \(S^5\), with probability-normalized surface \(L^2\) norm. Write \(E_q f=(f(v_{a,b}))_{a,b}\) and \(m_q=\dim\mathcal H_q\).

Define \(a_q=P_q^{(1,3)}(-1/2)/(q+1)\), where \(P_q^{(1,3)}\) is the classical Jacobi polynomial. The exact normalized Gram matrix and its spectrum are
\[
 m_q^{-1}E_qE_q^*=(1+a_q/8)I_9-(a_q/8)J_9,
 \qquad\operatorname{spec}(m_q^{-1}E_qE_q^*)=\{1-a_q\;(1),\;1+a_q/8\;(8)\}.
\]
The parentheses denote multiplicities. **The rank is eight exactly at \(q=0,2\) and nine at every other \(q\ge0\).** At these two exceptional indices \(a_q=1\), the image is the mean-zero hyperplane in \(\mathbb C^9\), all eight nonzero normalized eigenvalues equal \(9/8\), and the minimum squared norm interpolating such data \(y\) is \(8\|y\|_2^2/(9m_q)\). In particular, \(m_0=10\), \(m_2=81\): the normalized sampling Grams of the holomorphic cubic and the much larger mixed-degree \((5,2)\) sector coincide exactly. For the full-rank indices the displayed spectrum gives both the optimal interpolation cost and an explicit inverse.

## Assumptions and scope
The ambient field is \(\mathbb C\), with the unit sphere \(S^5\subset\mathbb C^3\). The complex Laplacian is \(\sum_{j=1}^3\partial_{z_j}\partial_{\overline z_j}\). Harmonic polynomials are of holomorphic and antiholomorphic bidegree \((q+3,q)\), and the probability measure on the unit sphere fixes the reproducing-kernel normalization. The nine vectors have the stated phases; changing individual phases generally conjugates the Gram by a diagonal unitary, so the rank and spectrum persist, while the literal mean-zero constraint changes to its phase-twisted equivalent. The conclusion is for every nonnegative integer \(q\), not just bounded degree.

## Proof
**1. Exact Hesse overlaps.** Every distinct pair of the given vectors has Hermitian inner product of modulus \(1/2\) and cube \(-1/8\). This follows directly from the three coordinates and \(1+\omega+\omega^2=0\); the checker verifies all 36 pairs in exact integer arithmetic in \(\mathbb Z[\omega]\). Diagonal overlaps are one.

**2. Addition theorem and two eigenvalues.** The reproducing kernel for \(\operatorname{Harm}(q+3,q)\) on the probability-normalized complex sphere is, for \(z,w\in S^5\),
\[
K_q(z,w)=m_q\langle z,w\rangle^3\frac{P_q^{(1,3)}(2|\langle z,w\rangle|^2-1)}{P_q^{(1,3)}(1)}.
\]
Here \(P_q^{(1,3)}(1)=q+1\), and
\[
m_q=\binom{q+5}{2}\binom{q+2}{2}-\binom{q+4}{2}\binom{q+1}{2}.
\]
This is the standard complex-spherical harmonic addition formula, with normalized diagonal \(K_q(z,z)=m_q\). The off-diagonal normalized value is \(-a_q/8\), and the diagonal is one. Therefore \(m_q^{-1}E_qE_q^*=(1+a_q/8)I-(a_q/8)J\). Its eigenvectors are the constants and their orthogonal complement, with eigenvalues \(1-a_q\) and \(1+a_q/8\), respectively.

**3. Complete Jacobi equality classification.** Put \(p_q=P_q^{(1,3)}(-1/2)\). Directly \(p_0=1\), \(p_1=-5/2\), \(p_2=3\). For \(3\le q\le899\), the exact rational recurrence in `checker.py` establishes exhaustively that \(- (q+1)<p_q<q+1\). The recurrence is the standard Jacobi three-term formula at \(-1/2\):
\[
2(n+1)(n+5)(2n+4)p_{n+1}=(2n+5)\bigl(-(n+3)(2n+4)-8\bigr)p_n-2(n+1)(n+3)(2n+6)p_{n-1}.
\]
For the infinite tail, the Jacobi generating function is
\[
F(z)=\sum_{n\ge0}p_nz^n=\frac{16}{R(z)(1-z+R(z))(1+z+R(z))^3},\qquad R(z)=\sqrt{1+z+z^2},\quad R(0)=1.
\]
It is analytic for \(|z|<1\). Its only square-root branch points on the closed unit circle are \(\omega,\omega^2\). On that boundary, direct substitution \(z=e^{it}\) gives \(|1+z+R(z)|\ge1\) and \(|1-z+R(z)|\ge\sqrt3\): for \(|t|\le2\pi/3\), \(R\) aligns with \(1+z\) and is orthogonal to \(1-z\), with the latter squared modulus exactly three; for \(|t|\ge2\pi/3\), the roles interchange, with the former squared modulus exactly one. Both factors are zero-free in the open unit disk because their products with their conjugate-sign algebraic partners are respectively \(z\) and \(-3z\), and their values at the origin equal two. The minimum modulus principle therefore gives these lower bounds throughout the disk.

If \(|z|=r<1\), then \(|R(z)|^2=|z-\omega|\,|z-\omega^2|\ge(\sqrt3/2)(1-r)\): the two roots are separated by \(\sqrt3\), so at least one factor is at least \(\sqrt3/2\) and both are at least \(1-r\). Consequently \(|F(z)|\le16\sqrt2\,3^{-3/4}(1-r)^{-1/2}<10(1-r)^{-1/2}\). With \(r=n/(n+1)\), Cauchy's coefficient estimate and \((1+1/n)^n<3\) give \(|p_n|<30\sqrt{n+1}<n+1\) whenever \(n\ge900\). Thus \(|a_q|<1\) for all \(q\ge3\). At \(q=1\), \(a_1=-5/4\), so both Gram eigenvalues remain positive. At \(q=0,2\), \(a_q=1\). These are exactly the rank-deficient cases.

**4. Interpolation.** When \(q\in\{0,2\}\), the Gram is \((9m_q/8)(I-J/9)\). Thus its image is exactly \(\{y:\sum y_{a,b}=0\}\), and its Moore–Penrose inverse is \((8/(9m_q))(I-J/9)\). Standard reproducing-kernel interpolation then yields the asserted minimum squared norm. At all other indices the inverse is \(m_q^{-1}((1-a_q)^{-1}J/9+(1+a_q/8)^{-1}(I-J/9))\).

## Verification
The standalone `checker.py` uses only the Python standard library. It tests all 81 Hermitian products of the nine exact \(\mathbb Z[\omega]\) coordinate vectors, confirms the 36 distinct cubic overlap identities, checks the exact Jacobi values at \(q=0,1,2\), and exhaustively verifies the 897 rational inequalities at every integer \(q=3,\ldots,899\). It also checks the normalization identities and dimensions. The infinite range \(q\ge900\) is proved by the generating-function estimate above; no finite test is treated as an infinite proof.

## Relationship to prior work
Roy and Suda (first public 25 April 2011, arXiv:1104.4692, Section 2) provide the general complex-spherical zonal polynomial and addition theorem; the formulas are foundational inputs and are not claimed new. Dang, Blanchfield, Bengtsson, and Appleby (first public 1 November 2012, arXiv:1211.0215, Section 3) give the Hesse SIC coordinates and explain the classical cubic pencil and its nine base points. The holomorphic cubic obstruction is therefore prior mathematics. The present contribution is the complete rank and conditioning classification of **every** pure charge-three mixed bihomogeneous harmonic sector, including the second, nonholomorphic resonance at \(q=2\) and a proof excluding all other resonances. This stronger all-index statement is not given in the inspected relevant portions of either source.

## Limitations
The classification is specific to the displayed phased Hesse configuration and to charge difference three; it is not a classification of every complex harmonic bidegree or every qutrit SIC. The stated originality judgment is based on relevant full-text sections and searched mathematical records and remains subject to undiscovered equivalent work. The proof uses a large but exact finite certificate for its low-index inequality and an explicit analytic bound for the tail. Independent mathematical validation has not been performed.

## References
1. A. Roy and S. Suda, *Complex spherical designs and codes*, arXiv:1104.4692v1, 25 April 2011, especially Section 2 (zonal polynomial and addition theorem), https://arxiv.org/html/1104.4692v1.
2. H. B. Dang, K. Blanchfield, I. Bengtsson, and D. M. Appleby, *Linear Dependencies in Weyl-Heisenberg Orbits*, arXiv:1211.0215v2, original submission 1 November 2012, especially Section 3, https://arxiv.org/html/1211.0215v2.
