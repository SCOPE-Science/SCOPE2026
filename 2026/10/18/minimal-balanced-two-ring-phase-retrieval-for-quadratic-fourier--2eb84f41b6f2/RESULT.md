# Minimal balanced two-ring phase retrieval for quadratic Fourier polynomials

## Finding
For a complex polynomial \(f(z)=a+bz+cz^2\), choose positive radii \(r,s\) and real angular offsets \(\phi,\psi\). Measure the eight squared moduli
\[
|f(r e^{i(\phi+j\pi/2)})|^2,\qquad
|f(s e^{i(\psi+j\pi/2)})|^2,\qquad j=0,1,2,3.
\]
These measurements determine **every** quadratic polynomial (including those with zero coefficients) up to multiplication by one unimodular scalar **if and only if**
\[
\boxed{r\ne s\quad\text{and}\quad\sin(2(\psi-\phi))\ne0.}
\]
At most seven arbitrary point-evaluation magnitudes can never achieve this universal uniqueness property on the three-dimensional complex coefficient space. Thus eight is the minimum possible count, and the two-ring square design attains it in precisely the stated parameter region.

The real linear subsystem that recovers the second-order complex coefficient product, after dividing its two measurements by their natural radial factors, has singular values
\[
\boxed{\sqrt{1+|\cos(2(\psi-\phi))|},\quad
\sqrt{1-|\cos(2(\psi-\phi))|}.}
\]
It is optimally conditioned, with condition number one, exactly when \(\psi-\phi\equiv\pi/4\pmod{\pi/2}\). This conditioning statement concerns the indicated linear demixing subsystem, not uniform stability of the nonlinear coefficient reconstruction near vanishing coefficients.

## Assumptions and scope
The coefficient vector is arbitrary in \(\mathbb C^3\); the zero polynomial is allowed. Two vectors are phase equivalent when one is a common unimodular multiple of the other. Radii are strictly positive; coincident or repeated sampling sites count as repeated measurements rather than additional information. Fourier modulus data are exact. No genericity, sparsity or minimum-amplitude assumption is imposed.

Let \(v(z)=(1,z,z^2)^T\) and let \(\mathcal H_3\) be the nine-dimensional real space of Hermitian \(3\times3\) matrices. The linearized measurement at \(z\) is
\[
\mathcal L_z(H)=\sum_{j,k=0}^2h_{jk}z^j\overline z^{\,k}.
\]
For a coefficient vector \(x=(a,b,c)^T\), the intensity at \(z\) equals \(\mathcal L_z(xx^*)\) under this convention. The general Hermitian lifting is used to prove injectivity, not to assert that an arbitrary Hermitian matrix represents a physical signal.

## Proof
**1. Exact four-angle demixing.** Set \(z_j=\rho e^{i(\vartheta+j\pi/2)}\) and \(Y_j=\mathcal L_{z_j}(H)\), with \(H\in\mathcal H_3\). Finite Fourier orthogonality gives
\[
\begin{aligned}
A_\rho&=\tfrac14\sum_{j=0}^3Y_j=h_{00}+\rho^2h_{11}+\rho^4h_{22},\\
B_\rho&=\tfrac14\sum_{j=0}^3Y_j e^{-i(\vartheta+j\pi/2)}=\rho h_{10}+\rho^3h_{21},\\
C_\rho&=\tfrac14\sum_{j=0}^3(-1)^jY_j=2\rho^2\operatorname{Re}(e^{2i\vartheta}h_{20}).
\end{aligned}
\]
The quantities \(A_\rho,C_\rho\) are real and \(B_\rho\) is complex. These are exactly the four independent real Fourier components of a real four-sample vector; hence their vanishing is equivalent to the four samples vanishing.

**2. The complete Hermitian kernel.** Suppose \(r\ne s\) and \(\sin(2(\psi-\phi))\ne0\). The two equations \(B_r=B_s=0\) force \(h_{10}=h_{21}=0\), because their determinant is \(rs(s^2-r^2)\ne0\). The two equations \(C_r=C_s=0\) force \(h_{20}=0\), because their real coefficient matrix has determinant of absolute value \(|\sin(2(\psi-\phi))|\ne0\). The remaining equations \(A_r=A_s=0\) leave exactly the one-dimensional real diagonal space
\[
\ker\mathcal L_Z=\mathbb R D_{r,s},\qquad
D_{r,s}=\operatorname{diag}(r^2s^2,-(r^2+s^2),1).
\]
All three diagonal entries are nonzero. Therefore every nonzero matrix in the kernel has rank three (its inertia is two positive eigenvalues and one negative, or the reversed inertia).

**3. Phase-retrieval sufficiency.** If two coefficient vectors \(x,y\) produce the same eight intensities, their difference of Hermitian rank-one lifts \(xx^*-yy^*\) lies in \(\ker\mathcal L_Z\). Its rank is at most two; a nonzero multiple of \(D_{r,s}\) has rank three. Consequently \(xx^*=yy^*\), which is equivalent to phase equivalence, including when one vector vanishes. This proves universal sufficiency.

**4. Sharp necessity of both design conditions.** If \(r=s\), the distinct polynomials \(f(z)=r\) and \(g(z)=z\) have identical moduli at all sampled points, no matter how the two squares are oriented. If \(\sin(2(\psi-\phi))=0\), the distinct polynomials
\[
 f_+(z)=1+i e^{-2i\phi}z^2,\qquad
 f_-(z)=1-i e^{-2i\phi}z^2
\]
have equal modulus on both squares: \(e^{-2i\phi}z^2\) is real at every sampling point. They are not related by a common unimodular scalar because both have constant coefficient one. The strict conditions are therefore necessary.

**5. Seven measurements never suffice.** Consider any at most seven complex point evaluations on \(\mathbb C^3\), and their real linear map \(\mathcal L:\mathcal H_3\to\mathbb R^m\). If the evaluation vectors fail to span \(\mathbb C^3\), an unmeasured nonzero coefficient vector and the zero vector have identical data. Otherwise \(\mathcal L\) annihilates no nonzero positive-semidefinite or negative-semidefinite matrix: a sum of nonnegative quadratic forms that vanishes at a spanning family forces that matrix to be zero. Since \(\dim_\mathbb R\mathcal H_3=9\) and \(m\le7\), the kernel contains a real plane with independent matrices \(H,K\). The continuous real function
\[
 t\longmapsto\det(H\cos t+K\sin t)
\]
changes sign upon replacing \(t\) by \(t+\pi\); therefore some nonzero matrix \(T\) in that plane is singular. It cannot be semidefinite, so it has rank two and signature \((1,1)\). Spectral decomposition writes \(T=xx^*-yy^*\) with noncollinear complex vectors \(x,y\). Hence the corresponding two inequivalent polynomials have equal measurements. This proves the universal cardinality lower bound.

**6. Exact angular singular values.** Write \(h_{20}=u+iv\). The two normalized real quantities \(C_r/(2r^2),C_s/(2s^2)\) equal the matrix product
\[
\begin{pmatrix}\cos2\phi&-\sin2\phi\\\cos2\psi&-\sin2\psi\end{pmatrix}
\begin{pmatrix}u\\v\end{pmatrix}.
\]
The row Gram matrix has diagonal entries one and off-diagonal entry \(\cos(2(\psi-\phi))\); its eigenvalues are \(1\pm|\cos(2(\psi-\phi))|\). Taking square roots proves the singular-value formula, the exact failure criterion, and optimal angular offset. No radial normalization is hidden in this comparison.

## Verification
The accompanying standalone script `two_ring_quadratic_verifier.py` uses exact SymPy linear algebra at \(r=1/2\), \(s=1\), \(\phi=0\), \(\psi=\pi/4\). It independently builds the eight Hermitian measurement rows, checks rank eight, and identifies the kernel generator \(\operatorname{diag}(1,-5,4)\). It checks rank loss when radii coincide or when there is no angular offset. It also performs 1,500 deterministic-seed randomized comparisons of the Fourier formulas, inversion of the two nontrivial linear blocks, and angular singular values. Run it with `python two_ring_quadratic_verifier.py` after installing NumPy and SymPy. All printed numerical checks supplement the analytic arguments above; finite tests do not certify the universal theorem on their own.

## Relationship to prior work
Pohl, Li, and Boche (2017) proved an eight-point phase-retrieval theorem for analytic polynomials of degree at most two using five equispaced values on one circle and three on another. That theorem establishes a different, unbalanced sampling design and does not establish the exact necessary-and-sufficient rotation criterion for two sets of four quadrature samples. Bodmann and Hammen (2013) constructed low-redundancy polynomial phase-retrieval frames using points on two intersecting circles; their geometric hypotheses differ from two concentric squares. The first publicly available motivating paper by de Dios Pont, Greilhuber, Liehr, and Taylor (September 23, 2026) concerns Gaussian-window short-time Fourier-transform phase retrieval from a uniformly discrete set rather than this exact finite-dimensional concentric-orbit problem. The shared theme is spatial sparsity of intensity samples, not an assertion that these earlier theorems imply the result here.

## Limitations
Universal uniqueness assumes noiseless exact measurements. The singular-value assertion describes a two-by-two normalized **linear** product-demixing block and should not be construed as a globally uniform inverse-Lipschitz estimate for the **nonlinear** coefficient map, particularly near the zero signal or coefficients of small magnitude. The checker does not replace the proof of the seven-point impossibility theorem. The 2026 motivating preprint was identifiable from its public abstract and metadata, but its complete text was inaccessible during this comparison; an unindexed or inaccessible earlier treatment of the exact balanced concentric design remains a historical-priority risk. The 2017 and 2013 results were inspected for their stated geometric sample configurations.

## References
1. J. de Dios Pont, J. Greilhuber, L. Liehr, and M. A. Taylor, *Phase retrieval from a uniformly discrete point set*, arXiv:2609.28341, first public version September 23, 2026. https://arxiv.org/abs/2609.28341
2. V. Pohl, G. Li, and H. Boche, *Phase retrieval in spaces of analytic functions on the unit disk*, Sampling Theory and Applications (SampTA), 2017, Theorem 7. https://doi.org/10.1109/SAMPTA.2017.8024411
3. B. G. Bodmann and N. Hammen, *Stable phase retrieval with low-redundancy frames*, 2013. https://arxiv.org/abs/1302.5487
4. I. Chalendar and J. R. Partington, *Phase retrieval on circles and lines*, 2024. https://arxiv.org/abs/2403.16255
