# A sharp \(n=2q\) spectral crossover for coordinate Fourier sampling on invertible finite-field matrices

## Finding
Let \(q\ge2\) be any prime power, \(n\ge2\) an integer and \(F=\mathbb F_q\). Select any nontrivial unitary additive character \(\psi:F\to\mathbb C\). On the uniform-probability space \(X=\operatorname{GL}_n(F)\), take the constant function and all nontrivial one-coordinate additive characters
\[
\phi_0(M)=1,\qquad
\phi_{ij,a}(M)=\psi(aM_{ij}),
\quad 1\le i,j\le n,\quad a\in F^\times.
\]
Their probability-normalized Gram matrix has size \(1+n^2(q-1)\). Put
\[
r=q-1,\quad u=\frac1{q^n-1},\quad t=\frac1{q^{n-1}-1},\quad v=ut,
\]
\[
A=1+u,\quad R=A-r(n-1)(u+v),\quad I=A+r(u+v),
\]
\[
T=A+r\bigl(-(2n-1)u+(n-1)^2v\bigr),\quad C=-n\sqrt r\,u,
\]
\[
\lambda_\pm=\frac{1+T\pm\sqrt{(1-T)^2+4C^2}}2.
\]
The **complete spectrum**, with multiplicities, is
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
A&n^2(q-2)\\
R&2(n-1)\\
I&(n-1)^2\\
\lambda_-&1\\
\lambda_+&1.
\end{array}
\]
Zero multiplicities are omitted; any numerical coincidences are combined. All eigenvalues of positive multiplicity are strictly positive. Consequently these characters remain linearly independent after restriction to invertible matrices.

**The sharp endpoint changes exactly at the dimension \(n=2q\):**
\[
\boxed{\lambda_{\min}=\lambda_-,\qquad
\lambda_{\max}=\begin{cases}I,&2\le n<2q,\\\lambda_+,&n\ge2q.\end{cases}}
\]
Both inequalities distinguishing the two upper sectors are strict (there is no transition tie). The sharp squared Riesz condition number is therefore
\[
\boxed{\kappa(q,n)^2=\frac{\lambda_{\max}}{\lambda_-}.}
\]
For every fixed finite-field order \(q\), the condition number approaches one **exponentially fast**:
\[
\boxed{\kappa(q,n)^2
=1+2n\sqrt{q(q-1)}\,q^{-n}+O_q(q^{-n})
\quad (n\longrightarrow\infty).}
\]
At fixed \(q\), the invertible matrices nevertheless occupy the nonvanishing asymptotic proportion \(\prod_{j=1}^\infty(1-q^{-j})\) of the ambient matrix space. Thus near-tightness is not a consequence of removing a vanishing proportion of ambient sampling points.

## Assumptions and scope
The ambient additive group is \(V=M_n(F)\), endowed with normalized counting measure. The displayed functions are restrictions of distinct ambient additive characters indexed by
\[
\Omega=\{0\}\cup\{aE_{ij}:a\in F^\times,\ 1\le i,j\le n\}.
\]
Here \(E_{ij}\) is a matrix unit, and all elements of \(\Omega\) are distinct. The inner product on \(X\) is \(\langle f,g\rangle_X=|X|^{-1}\sum_{M\in X}\overline{f(M)}g(M)\). Unlike representation-theoretic Fourier analysis of the nonabelian group \(\operatorname{GL}_n(F)\), these are **ambient additive** Fourier characters. No assumption that \(q\) is prime or odd is made. The eigenvalues refer to the squared singular values of the probability-normalized restriction map \(\mathbb C^\Omega\to L^2(X)\).

For any coefficients \(c_\alpha\in\mathbb C\), ambient Parseval and the theorem yield the simultaneously sharp bounds
\[
\lambda_-\sum_{\alpha\in\Omega}|c_\alpha|^2
\ \le\ \left\|\sum_{\alpha\in\Omega}c_\alpha\phi_\alpha\right\|_{L^2(X)}^2
\ \le\ \lambda_{\max}\sum_{\alpha\in\Omega}|c_\alpha|^2.
\]
The lower equality space is always one-dimensional. The upper equality space has dimension \((n-1)^2\) for \(n<2q\) and one dimension for \(n\ge2q\), as given constructively in the proof.

## Proof
**1. Exact additive Fourier correlations.** For any nonzero matrix \(D\) of rank one, the first column of a uniformly chosen invertible matrix is uniform on \(F^n\setminus\{0\}\). Left-right invariance reduces the character average to a nontrivial additive character of the first coordinate. Orthogonality gives
\[
\mathbb E_{M\in X}\psi(\operatorname{tr}(D^\mathsf T M))=-\frac1{q^n-1}=-u.
\]
For a rank-two \(D\), invariance reduces the average to \(\mathbb E\psi(M_{11}+M_{22})\). The first two columns \(x,y\) range uniformly over linearly independent ordered pairs. For each fixed \(x\ne0\), summing \(\psi(y_2)\) over \(y\notin\operatorname{span}(x)\) gives \(-q\mathbf1_{\{x_2=0\}}\). The remaining sum over \(x\ne0\) of \(\psi(x_1)\mathbf1_{\{x_2=0\}}\) equals \(-1\). The total numerator is therefore \(q\), giving
\[
\mathbb E_{M\in X}\psi(\operatorname{tr}(D^\mathsf T M))
=\frac q{(q^n-1)(q^n-q)}=\frac1{(q^n-1)(q^{n-1}-1)}=v.
\]
This is a low-rank specialization of the general matrix-group Gauss sums previously computed by Li and Hu (2011, Theorem 2.1). The rank-one and rank-two character sums themselves are **not claimed as new**.

**2. An exact rook-geometry Gram decomposition.** Distinct frequencies \(aE_{ij}\) and \(bE_{kl}\) differ by rank one precisely when \(i=k\) or \(j=l\), including distinct labels in one cell; otherwise their difference has rank two. Index the nonzero frequencies by \((i,j,a)\) with \(r=q-1\) labels per cell. Define the \(n^2\)-by-\(n^2\) rook matrix
\[
P=I_n\otimes J_n+J_n\otimes I_n-I_{n^2},
\]
where \(J_s\) is the all-ones matrix of order \(s\). In the frequency-label coordinates, the nonzero-frequency Gram block is exactly
\[
D=(1+u)I_{rn^2}-(u+v)(P\otimes J_r)+vJ_{rn^2}.
\]
The constant-to-nonzero-frequency block equals \(-u\mathbf1_{rn^2}^\mathsf T\). These identities include the diagonal entries: \((1+u)-(u+v)+v=1\).

**3. Exhaustive orthogonal spectral decomposition.** First, at each cell, the \(r-1\) Fourier-label directions of zero coordinate sum are eigenvectors of \(D\) with eigenvalue \(A\). Their total multiplicity is \(n^2(r-1)\). The remaining label-constant vectors identify with \(\mathbb C^n\otimes\mathbb C^n\). Since the rook matrix has eigenvalues \(2n-1\), \(n-1\), and \(-1\) on, respectively,
\[
\langle\mathbf1_n\rangle\otimes\langle\mathbf1_n\rangle,\qquad
(\mathbf1_n^\perp\otimes\langle\mathbf1_n\rangle)
\oplus(\langle\mathbf1_n\rangle\otimes\mathbf1_n^\perp),\qquad
\mathbf1_n^\perp\otimes\mathbf1_n^\perp,
\]
we obtain the eigenvalues \(R\) with multiplicity \(2(n-1)\) and \(I\) with multiplicity \((n-1)^2\). Each of these coefficient sectors has zero overall sum, so neither couples to the constant character. On the normalized all-ones nonzero-frequency vector \(w=(rn^2)^{-1/2}\mathbf1_{rn^2}\), the diagonal entry is \(T\). The two remaining directions, the constant-frequency coefficient vector \(e_0\) and \(w\), have matrix
\[
\begin{pmatrix}1&C\\C&T\end{pmatrix}.
\]
Its eigenvalues are exactly \(\lambda_-\) and \(\lambda_+\). For either eigenvalue \(\lambda\), a coefficient eigenvector is \(C e_0+(\lambda-1)w\). The multiplicities sum to \(1+rn^2\), and these sectors are mutually orthogonal. The decomposition therefore gives every eigenvalue and equality space.

**4. No hidden kernel.** The scalar levels \(A\) and \(I\) are visibly positive. For \(R\), substituting \(1+t=q^{n-1}/(q^{n-1}-1)\) shows \(R>0\) is equivalent to
\[
q(q^{n-1}-1)>(q-1)(n-1),
\]
which holds because \(q^{n-1}-1=(q-1)\sum_{j=0}^{n-2}q^j\ge(q-1)(n-1)\) and \(q>1\). For the remaining block, the function represented by \(\sqrt{rn^2}\,w\) is
\[
Y(M)=\sum_{i,j}\sum_{a\ne0}\psi(aM_{ij})=qZ(M)-n^2,
\]
where \(Z(M)\) counts zero matrix entries. The identity matrix and its elementary shear \(I+E_{12}\) are both invertible but have different zero-entry counts for all \(n\ge2\). Hence \(Y\) is nonconstant, and the two-dimensional Gram matrix of \(1\) and \(Y/\sqrt{rn^2}\) has strictly positive determinant. Thus \(\lambda_->0\).

**5. The exact upper-sector crossover.** The scalar eigenvalues obey \(R<A<I\). Also
\[
R-T=rn u\bigl(1-(n-1)t\bigr)\ge0,
\]
because \(q^{n-1}-1\ge(q-1)(n-1)\ge n-1\). The off-diagonal coupling \(C\ne0\) gives \(\lambda_-<\min\{1,T\}\le R\). Therefore the bottom eigenvalue is \(\lambda_-\), and the top is either \(I\) or \(\lambda_+\). Since \(I>1>\lambda_-\), the sign of \(I-\lambda_+\) is the sign of the characteristic polynomial of the two-dimensional block at \(I\). Direct factorization gives the **exact** identity
\[
(I-1)(I-T)-C^2=
 nr u^2(1+t)\bigl(2q-n-r(n-2)t\bigr).
\]
If \(2\le n<2q\), then \(2q-n\ge1\), whereas
\[
0\le r(n-2)t=\frac{(q-1)(n-2)}{q^{n-1}-1}
\le\frac{n-2}{n-1}<1.
\]
Thus the characteristic-polynomial value is strictly positive and \(I>\lambda_+\). If \(n\ge2q\), its final factor is strictly negative, giving \(\lambda_+>I\). This proves the sharp crossover without unresolved boundary cases.

**6. Exact conditioning and its asymptotic.** The Rayleigh variational principle on the orthogonal decomposition establishes both sharp constants and the stated equality dimensions. For fixed \(q\) as \(n\to\infty\), \(u=q^{-n}+O_q(q^{-2n})\) and \(t=O_q(q^{-n})\). Consequently
\[
1-T=(2n(q-1)-q)u+O_q(n^2q^{-2n}),\qquad
C=-n\sqrt{q-1}\,u.
\]
The eigenvalue gap of the two-dimensional block is
\[
\lambda_+-\lambda_-
=u\sqrt{\bigl(2n(q-1)-q\bigr)^2+4n^2(q-1)}
+O_q(n^2q^{-2n}).
\]
For all sufficiently large \(n\), these two roots are the sharp endpoints by step 5 and step 4. The square root is \(2n\sqrt{q(q-1)}+O_q(1)\), while \(\lambda_-=1+O_q(nq^{-n})\), proving
\[
\kappa^2=1+2n\sqrt{q(q-1)}\,q^{-n}+O_q(q^{-n}).
\]
Finally, the standard independent-column count gives \(|\operatorname{GL}_n(F)|/q^{n^2}=\prod_{j=1}^n(1-q^{-j})\), which converges to a strictly positive limit for fixed \(q\).

## Verification
Run `python checker.py` with Python 3 and NumPy; field arithmetic is explicit for prime fields and for \(\mathbb F_4=\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\). The checker independently enumerates **32,274 invertible matrices** in seven direct test cases: \((q,n)=(2,2),(3,2),(5,2),(4,2),(2,3),(3,3),(2,4)\). It evaluates all restricted additive characters, diagonalizes the resulting Gram matrices, and compares their full spectra with the formulas. The worst absolute eigenvalue discrepancy is below \(1.6\times10^{-15}\). It also checks multiplicities and the exact integer sign certificate for the crossover over **138 parameter pairs** with \(q\in\{2,3,4,5,7,11\}\) and \(2\le n\le24\). All checks pass. Finite experiments do not establish the infinite dimension or arbitrary-field theorem; the proof does so algebraically.

## Relationship to prior work
Li and Hu, *Gauss sums over some matrix groups* (arXiv:1105.4513, Theorem 2.1), give additive Fourier transforms of the full general linear group at arbitrary matrix ranks. Their result already supplies the rank-one/rank-two matrix character averages in step 1. It does **not** state, analyze or classify the Gram matrix of the selected coordinate-character band; its sharp spectral-sector crossover and near-tightness rate require the additional rook-space analysis in steps 2–6. The character sums alone are not represented as a new discovery.

Fickus and Mixon, *Numerically erasure-robust frames* (arXiv:1202.4525), address frame conditioning and group-frame constructions, but not the present ambient-additive Fourier restriction on finite invertible matrices, or a field-order-dependent change in its leading singular-value mode.

The published work *Complete first-coordinate Fourier spectrum on finite-field rank-one matrices* treats the **rank-exactly-one** shell, not the invertible (full-rank) shell; its rook-block framework is an informative structural analogy but its moments and resulting spectrum do not specialize to the present sampling set. The published work *Four-level Fourier frame spectrum on determinant-one matrices over finite fields* treats only \(2\)-by-\(2\) determinant-one matrices. The case \((q,n)=(2,2)\) of the present theorem coincides with that known setting and is not separately claimed as new, while determinant-one sampling for general \(q\) has different opposite-coordinate character correlations. None of these inspected statements supplies the unrestricted full-rank theorem, the precise \(n=2q\) upper-sector boundary or the exponential near-tightness law.

## Limitations
The theorem concerns only the complete constant-plus-one-coordinate additive Fourier band, not arbitrary Fourier supports, all ranks, higher interaction degrees, or Fourier representations of the nonabelian group. Its positive spectrum does not imply robustness under arbitrary additional sample erasures. The numerical checks cover selected small fields and dimensions only. Although the quoted literature was compared at the statement and full-text level where available, an older equivalent specialization or an unrecognized representation-theoretic diagonalization may exist. No independent validation or exhaustive historical novelty certification is claimed.

## References
1. Y. Li and S. Hu, *Gauss sums over some matrix groups*, arXiv:1105.4513 (first posted 2011-05-23), Theorem 2.1. https://arxiv.org/abs/1105.4513
2. M. Fickus and D. G. Mixon, *Numerically erasure-robust frames*, arXiv:1202.4525 (first posted 2012-02-21), Sections 1–2. https://arxiv.org/abs/1202.4525
3. *Complete first-coordinate Fourier spectrum on finite-field rank-one matrices* (2026), public research result. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-complete-first-coordinate-fourier-spectrum-on-finite-field-rank--3ad73e3126a7
4. *Four-level Fourier frame spectrum on determinant-one matrices over finite fields* (2026), public research result. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-four-level-fourier-frame-spectrum-on-determinant-one-matrices-ov--a9ad8796111d
