# Exact finite-dimensional antilinear trace disks and Takagi-spectrum tomography

## Finding
Let \(n\geq2\), and let \(A:\mathbb C^n\to\mathbb C^n\) be any conjugate-linear map, written \(Ax=M\overline{x}\). Define its complex-symmetric matrix \(C=(M+M^{\mathsf T})/2\), and let \(s_1\geq\cdots\geq s_n\geq0\) be the Takagi singular values of \(C\) (equivalently, the usual singular values of \(C\)). For each integer \(1\leq k\leq n\), the normalized trace numerical range, in the terminology of Majumdar--Müller, is
\[
W_{\mathrm{tr},k}(A)=\left\{\frac1k\sum_{j=1}^k\langle Ax_j,x_j\rangle:\langle x_i,x_j\rangle=\delta_{ij}\right\}.
\]
Then **every one of these sets is a closed centered disk**, including the top-rank case:
\[
\boxed{W_{\mathrm{tr},k}(A)=\{z\in\mathbb C:|z|\leq R_k\},\qquad R_k=\frac1k\sum_{j=1}^k s_j.}
\]
In particular, the entire sequence of observable disks recovers the full Takagi singular spectrum by
\[
\boxed{s_k=kR_k-(k-1)R_{k-1},\qquad R_0=0,\quad 1\leq k\leq n.}
\]
Two conjugate-linear maps in the same dimension have equal trace numerical ranges at all ranks if and only if their complex-symmetric coefficient matrices have the same singular values, equivalently are unitarily congruent. Every complex skew-symmetric coefficient perturbation leaves all these ranges unchanged.

## Assumptions and scope
The space has its standard Hermitian inner product, conjugate linear in the first variable. No normality, positivity, invertibility, or symmetry is imposed on \(M\). The statement includes repeated or zero singular values, all ranks through \(k=n\), and the case \(C=0\). The definition averages the diagonal values over an **orthonormal frame**, not the higher-rank compression condition nor the constrained \(q\)-numerical range. The result is specific to conjugate-linear maps; it makes no assertion that real-linear operators containing both linear and conjugate-linear parts have centered-disk ranges.

## Proof
**1. Remove the invisible skew part.** For every column \(w\), the scalar \(w^{\mathsf T}Mw\) equals \(w^{\mathsf T}Cw\), because \(w^{\mathsf T}(M-M^{\mathsf T})w=0\). If \(w_j=\overline{x_j}\) and \(W=[w_1\ \cdots\ w_k]\), then \(W^*W=I_k\) and
\[
\sum_{j=1}^k\langle Ax_j,x_j\rangle
=\overline{\operatorname{tr}(W^{\mathsf T}CW)}.
\]
This also establishes invariance under arbitrary complex skew-symmetric additions to \(M\).

**2. Exact upper bound.** By Takagi factorization choose unitary \(V\) with \(C=VDV^{\mathsf T}\) and \(D=\operatorname{diag}(s_1,\ldots,s_n)\). Put \(W=\overline VZ\), so \(Z^*Z=I_k\). Writing \(z_{ij}\) for the entries of \(Z\),
\[
\operatorname{tr}(W^{\mathsf T}CW)=\sum_{i=1}^n s_i\sum_{j=1}^k z_{ij}^2.
\]
Let \(p_i=\sum_{j=1}^k|z_{ij}|^2\), the diagonal entries of the orthogonal projection \(ZZ^*\). Thus \(0\leq p_i\leq1\) and \(\sum_i p_i=k\). Consequently,
\[
\left|\operatorname{tr}(W^{\mathsf T}CW)\right|
\leq\sum_{i=1}^n s_ip_i\leq\sum_{i=1}^k s_i.
\]
The last inequality is the finite-dimensional decreasing-rearrangement bound: moving mass from any later index to an earlier unfilled index cannot decrease the weighted sum. Equality is attained by \(Z=[e_1\ \cdots\ e_k]\), so the maximal absolute trace is exactly \(\sum_{i=1}^k s_i\).

**3. Explicit zero at every rank.** It suffices to exhibit an orthonormal \(Z\) with \(\operatorname{tr}(Z^{\mathsf T}DZ)=0\). For \(k=1\) (hence \(n\geq2\)), if \(s_1+s_2>0\), take
\[
z=\frac{\sqrt{s_2}\,e_1+i\sqrt{s_1}\,e_2}{\sqrt{s_1+s_2}};
\]
then \(z^*z=1\) and \(z^{\mathsf T}Dz=0\). If \(s_1+s_2=0\), every unit vector works.

For \(k\geq2\), work within the first \(k\) Takagi coordinates. On any pair of coordinates use the unitary
\[
Q=\frac1{\sqrt2}\begin{pmatrix}1&i\\ i&1\end{pmatrix},
\qquad Q Q^{\mathsf T}=\begin{pmatrix}0&i\\i&0\end{pmatrix}.
\]
For even \(k\), place copies of \(Q\) on the diagonal of a \(k\)-by-\(k\) unitary \(U\); then all diagonal entries of \(UU^{\mathsf T}\) vanish and hence \(\operatorname{tr}(U^{\mathsf T}D_kU)=0\), where \(D_k\) is the leading \(k\)-by-\(k\) block of \(D\).

For odd \(k\geq3\), cancel the first \(k-3\) coordinates in such pairs. For the last three weights \(a=s_{k-2},\ b=s_{k-1},\ c=s_k\), note \(0\leq c\leq b\leq a\). If \(a+b>0\), choose \(\theta\) with \(\cos(2\theta)=-c/(a+b)\); if \(a+b=0\), take \(\theta=\pi/4\). Use the unitary \(Q_\theta=\cos\theta I_2+i\sin\theta\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\) on the first two of these three coordinates and identity on the third. Since the first two diagonal entries of \(Q_\theta Q_\theta^{\mathsf T}\) are \(\cos(2\theta)\), the remaining trace is \((a+b)\cos(2\theta)+c=0\). The first \(k\) columns of the resulting block unitary, padded below by zero, form the required \(Z\). This also covers \(k=n\), all singular degeneracies, and \(C=0\).

**4. Fill the disk and recover the spectrum.** The complex Stiefel manifold of orthonormal \(k\)-frames in \(\mathbb C^n\) is path connected: any two frames extend to unitary bases, and the unitary group is path connected. The continuous modulus of the trace therefore takes **every** value between the exhibited zero and the exhibited maximum \(\sum_{j=1}^k s_j\). Multiplying every frame vector by a common unit complex scalar rotates the conjugate-linear quadratic trace by twice its argument; hence every phase occurs at every attained modulus. Dividing by \(k\) gives the asserted closed disk, including its boundary. Finally \(kR_k=\sum_{j=1}^k s_j\), so successive differences recover each \(s_k\). Takagi factorization states that two complex symmetric matrices are unitarily congruent precisely when their singular-value multisets agree. All claims follow.

## Verification
The standalone script `verify_trace_disks.py` checks random Takagi diagonal data and unitary congruences for dimensions \(2\) through \(9\), all ranks, zero and repeated singular values, arbitrary added skew-symmetric parts, exact upper-bound frames, exact zero-trace frames, and random frames. On the recorded run, \(1{,}056\) dimension-rank cases and \(10{,}560\) checked frames passed at stated floating-point tolerances. Its finite checks are diagnostic; Steps 1--4 provide the proof for all finite \(n\).

## Relationship to prior work
Majumdar and Müller, *Some Generalized Numerical Ranges of Real-linear Operators on Hilbert Spaces* (arXiv:2610.16823v1, submitted 12 October 2026), Definition 7.1, introduce the normalized trace numerical range; Theorem 7.2 proves that for antilinear operators on **infinite-dimensional** Hilbert spaces the sets are centered disks. It does not provide the exact radii, the finite-dimensional result at every rank, or inverse singular-spectrum reconstruction. Kołaczek and Müller, *Numerical Ranges of Antilinear Operators* (2024), establish the **ordinary rank-one** centered disk and its degeneracy properties, not the higher-rank trace profiles. Their results are preserved here as prior art. Kołaczek and Müller (arXiv:2508.04347v1) address ordinary numerical ranges of real-linear maps. Chan, Li and Poon (arXiv:2105.04621) study the joint \(k\)-numerical ranges of **complex-linear** operators, whose top-rank trace is a singleton; their formulas do not imply antilinear top-rank disk behavior. The combination of the full normalized trace-disk profile with the exact Takagi-spectrum inverse and skew-invisibility classification is the asserted new contribution.

## Limitations
The disk family recovers singular values of the complex-symmetric coefficient part only, not its Takagi vectors or the skew-symmetric part of the conjugate-linear operator. In dimension \(n=1\), the rank-one trace range is generally a **circle**, not a disk, so \(n\geq2\) is essential. No independent validation or absolute publication-priority certification is claimed. A mathematically equivalent formula may exist outside the indexed and inspected literature; the familiar Takagi and finite-rank Ky Fan inequalities are explicitly treated as classical ingredients rather than new lemmas.

## References
1. A. Majumdar and V. Müller, *Some Generalized Numerical Ranges of Real-linear Operators on Hilbert Spaces*, arXiv:2610.16823v1 (12 October 2026), especially Definition 7.1 and Theorem 7.2. https://arxiv.org/html/2610.16823v1
2. D. Kołaczek and V. Müller, *Numerical Ranges of Antilinear Operators*, Integral Equations and Operator Theory **96**, article 17 (2024), DOI:10.1007/s00020-024-02768-5. https://link.springer.com/article/10.1007/s00020-024-02768-5
3. D. Kołaczek and V. Müller, *Real linear operators and numerical ranges*, arXiv:2508.04347v1 (2025). https://arxiv.org/html/2508.04347v1
4. J.-T. Chan, C.-K. Li and Y.-T. Poon, *Joint \(k\)-numerical ranges of operators*, arXiv:2105.04621 (2021; revised 2022). https://arxiv.org/pdf/2105.04621
5. T. Takagi, classical factorization of complex symmetric matrices into unitary congruences of nonnegative diagonal matrices (used as a standard theorem).
