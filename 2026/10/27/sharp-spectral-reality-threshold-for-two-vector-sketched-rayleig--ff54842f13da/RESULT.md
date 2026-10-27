# Sharp spectral-reality threshold for two-vector sketched Rayleigh–Ritz

## Finding

Let \(A\in\mathbb R^{n\times n}\) be symmetric and \(X\in\mathbb R^{n\times2}\) have orthonormal columns, where \(n\ge4\). Write \(H=X^{\mathsf T}AX\), assume its two real eigenvalues have gap \(\Delta>0\), and let \(R=(I-XX^{\mathsf T})AX\) have \(r=\|R\|_2>0\). Given a real linear sketch \(S\) satisfying the squared-norm embedding condition
\[
(1-\varepsilon)\|z\|_2^2\le\|Sz\|_2^2\le(1+\varepsilon)\|z\|_2^2
\quad(z\in\operatorname{span}\{X,AX\}),\qquad0\le\varepsilon<1,
\]
define the sketched Rayleigh–Ritz extraction \(B=(SX)^\dagger SAX\). The two eigenvalues of \(B\) satisfy the sharp dimension-independent envelope
\[
\max_{\lambda\in\sigma(B)}|\operatorname{Im}\lambda|
\le \left[\max\left\{0,\frac{\varepsilon^2r^2}{1-\varepsilon^2}-\frac{\Delta^2}{4}\right\}\right]^{1/2}.
\]
Consequently both sketched Ritz values are real for **every** admissible problem if and only if the sketch distortion is bounded by
\[
\varepsilon\le\varepsilon_{\mathrm{crit}}:=\frac{\Delta}{\sqrt{\Delta^2+4r^2}}.
\]
The qualifier “for every” is crucial: for each fixed \(\Delta,r>0\) and \(\varepsilon>\varepsilon_{\mathrm{crit}}\), a real **positive-definite** four-dimensional witness has a nonreal conjugate pair and attains the envelope. At equality, an admissible witness has a real repeated defective Ritz value. The envelope remains sharp at and below the transition (its value is zero there).

## Assumptions and scope

All statements are in exact real arithmetic. The tested space \(\mathcal U=\operatorname{span}\{\operatorname{range}(X),\operatorname{range}(AX)\}\) has dimension at most four. The embedding bounds apply on this entire space, not just the column space of \(X\). The sketch can have any number of rows as long as the embedding holds; then \(SX\) has full column rank. The gap \(\Delta\) is the gap between the two **unsketched** Ritz values, and \(r\) is the spectral norm of the unsketched residual matrix. For \(r=0\), the sketched extraction equals \(H\) and has real eigenvalues for every \(\varepsilon<1\); the nontrivial sharp classification assumes \(r>0\). Neither statistical assumptions on \(S\) nor conditioning of \(A\) are imposed.

## Proof

**1. An optimal Gram-block mixing estimate.** Choose an orthonormal basis \(Y\) for the range of \(R\), with \(Y^{\mathsf T}X=0\); write \(R=YC\), so \(\|C\|_2=r\). Relative to the orthonormal basis \([X,Y]\) of \(\mathcal U\), set
\[
G=[X,Y]^{\mathsf T}S^{\mathsf T}S[X,Y]
=\begin{pmatrix}G_{11}&G_{12}\\G_{12}^{\mathsf T}&G_{22}\end{pmatrix}.
\]
The embedding condition is \(\|G-I\|_2\le\varepsilon\) and \(G_{11}\) is positive definite. The identity \(AX=XH+YC\) gives
\[
 B=H+E,\qquad E=G_{11}^{-1}G_{12}C.
\]
We show the dimension-independent sharp estimate
\[
\|G_{11}^{-1}G_{12}\|_2\le\frac{\varepsilon}{\sqrt{1-\varepsilon^2}}.
\]
For a unit vector \(y\) in the residual-coordinate space let \(z=G_{11}^{-1}G_{12}y\). If \(z\ne0\), let \(u=z/\|z\|_2\), \(q=\|z\|_2\), and \(a=u^{\mathsf T}G_{11}u>0\). Then \(u^{\mathsf T}G_{12}y=aq\). Applied to the unit block vector \((u,0)\), the bound \(\|G-I\|_2\le\varepsilon\) implies \((a-1)^2+a^2q^2\le\varepsilon^2\). Completing the square in \(a\) (or minimizing over all real \(a\)) gives \(q^2/(1+q^2)\le\varepsilon^2\). Hence \(q\le\varepsilon/\sqrt{1-\varepsilon^2}\); taking the supremum over \(y\) proves the estimate. This argument also handles rank-one residuals. Therefore
\[
\|E\|_2\le\delta:=\frac{r\varepsilon}{\sqrt{1-\varepsilon^2}}.
\]

**2. An optimal two-by-two real perturbation estimate.** Let \(K\) be any symmetric real \(2\times2\) matrix with eigenvalue gap \(2h>0\), and let \(E\) be real with \(\|E\|_2\le\delta\). Orthogonally diagonalize and subtract the scalar center so that \(K=\operatorname{diag}(-h,h)\). Write without loss of generality
\[
E=\begin{pmatrix}\alpha+u&v+w\\v-w&\alpha-u\end{pmatrix},
\qquad q=\sqrt{u^2+v^2}.
\]
A direct calculation of \(E^{\mathsf T}E\) yields the exact operator norm \(\|E\|_2=\sqrt{\alpha^2+w^2}+q\), hence \(|w|+q\le\delta\). The squared half-gap of the eigenvalues of \(K+E\) is \((u-h)^2+v^2-w^2\). If the eigenvalues are nonreal, their common imaginary-part magnitude \(\gamma>0\) obeys
\[
 \gamma^2=w^2-(u-h)^2-v^2
 \le(\delta-q)^2-(h-q)^2
 =\delta^2-h^2-2q(\delta-h).
\]
If \(\delta\le h\), the simpler inequality \(\sqrt{(u-h)^2+v^2}\ge h-q\ge\delta-q\ge|w|\) shows that nonreal eigenvalues are impossible (in this chain \(q\le\delta\le h\)). If \(\delta>h\), the displayed bound gives \(\gamma^2\le\delta^2-h^2\). Equality for \(\delta>h\) is attained when \(E\) is the skew rotation \(\delta\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\) in the eigenbasis of \(K\). This proves the claimed imaginary envelope upon setting \(h=\Delta/2\).

**3. Simultaneous sharpness, including positive definiteness.** For arbitrary \(\Delta,r>0\), pick \(a>0\), put \(b=a+\Delta\), and choose \(d>r^2/a\). On \(\mathbb R^4\) take
\[
 A=\begin{pmatrix}a&0&r&0\\0&b&0&r\\r&0&d&0\\0&r&0&d\end{pmatrix},
 \qquad X=[e_1,e_2],\qquad
 J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
The Schur complement \(\operatorname{diag}(a,b)-r^2d^{-1}I\) is positive definite, so \(A\) is positive definite. We have \(H=\operatorname{diag}(a,b)\), \(R=r[e_3,e_4]\) and \(\|R\|_2=r\). For any \(0\le\varepsilon<1\), define the positive-definite sketch Gram matrix
\[
 G=\begin{pmatrix}(1-\varepsilon^2)I_2&\varepsilon\sqrt{1-\varepsilon^2}\,J\\ -\varepsilon\sqrt{1-\varepsilon^2}\,J&(1+\varepsilon^2)I_2\end{pmatrix}.
\]
The exact identity \((G-I_4)^2=\varepsilon^2I_4\) shows its spectrum is contained in \(\{1-\varepsilon,1+\varepsilon\}\), and its least eigenvalue is positive. Choose \(S=G^{1/2}\) (positive matrix square root), so the squared-norm embedding is exactly \(\varepsilon\). Substitution in the sketched extraction gives
\[
 B=\begin{pmatrix}a&-\delta\\\delta&b\end{pmatrix},
 \qquad \delta=\frac{r\varepsilon}{\sqrt{1-\varepsilon^2}},
 \qquad \sigma(B)=\left\{\frac{a+b}{2}\pm\sqrt{\frac{\Delta^2}{4}-\delta^2}\right\}.
\]
For \(\delta>\Delta/2\) the eigenvalues are nonreal and attain the upper envelope; for equality the matrix has a single real eigenvalue and a nonzero nilpotent traceless part, so its repeated eigenvalue is defective. The condition \(\delta\le\Delta/2\) is algebraically equivalent to \(\varepsilon\le\varepsilon_{\mathrm{crit}}\). For every larger ambient dimension, append an arbitrary positive-definite direct-sum block to \(A\), extend \(X\) by zero rows, and take \(S=[G^{1/2},0]\) with four rows; the same bound remains attained with a genuinely dimension-reducing sketch.

## Verification

The standalone `verify.py` uses only Python's standard library. It checks the rational positive-definite witness \(a=2\), \(b=3\), \(r=1\), \(d=2\), \(\varepsilon=3/5\):
\[
 G_{11}=\frac{16}{25}I_2,\quad G_{12}=\frac{12}{25}J,\quad
 B=\begin{pmatrix}2&-3/4\\3/4&3\end{pmatrix},\quad
 \sigma(B)=\left\{\frac52\pm\frac{\sqrt5}{4}i\right\}.
\]
The checker verifies \((G-I_4)^2=(9/25)I_4\) and the characteristic identity in rational arithmetic, and stress-tests both matrix inequalities with 20,000 seeded finite cases. These finite checks corroborate the algebra; the universal statements are established by the preceding proof, not enumeration.

To reproduce, run `python3 verify.py` in a Python 3 environment with no third-party dependencies. Expected final output begins `VERIFICATION_OK`.

## Relationship to prior work

Liu and Liu (2026) examine real-arithmetic sketched eigensolvers for symmetric matrices, note that ordinary sketched Rayleigh–Ritz may return complex eigenvalues, and develop real-Schur-based and local subspace-gap analysis. Nakatsukasa and Tropp (2021) introduce the sketched Rayleigh–Ritz framework, including the symmetric-input warning that sketched eigenvalues need not be real. Neither inspected treatment states the exact universally sharp gap–residual–embedding threshold above or the attained imaginary-part envelope. Gubler and collaborators (2026) instead use a Hermitian generalized eigenproblem with a different projection that retains real spectra; this is not the nonsymmetric sketched extraction studied here. The classical two-by-two distance-to-defectivity mechanism underlies one of the proof's lemmas, but does not alone determine the sharp embedding-to-obliqueness constant or its joint realizability for a positive-definite input.

## Limitations

This theorem applies to precisely two trial vectors and the indicated least-squares sketched Rayleigh–Ritz extraction. It does not imply that all sketched eigensolvers have complex Ritz values, nor does it replace the Hermitian generalized formulation. A sketch embedding only \(\operatorname{range}(X)\), without controlling \(\operatorname{span}\{X,AX\}\), need not satisfy the stated guarantee. The sharp worst-case witness does not estimate the probability of a nonreal pair under a particular random sketch distribution. Prior exact specializations in unindexed literature cannot be excluded by bibliographic search alone.

## References

- X. Liu and Y. Liu, *Real-Arithmetic Sketched Eigensolvers for Symmetric Matrices* (2026), arXiv:2610.22261v1, first publicly available 2026-10-15. https://arxiv.org/html/2610.22261v1
- Y. Nakatsukasa and J. A. Tropp, *Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems* (2021), arXiv:2111.00113. https://arxiv.org/abs/2111.00113
- M. Gubler et al., *Randomized Block Davidson Eigensolvers for Plane-Wave Density-Functional Theory* (2026), arXiv:2608.24529. https://arxiv.org/abs/2608.24529
