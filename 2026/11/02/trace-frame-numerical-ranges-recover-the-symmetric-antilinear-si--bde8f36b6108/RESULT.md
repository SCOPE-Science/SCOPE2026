# Trace-frame numerical ranges recover the symmetric antilinear singular profile

## Finding
Let \(H\) be a complex Hilbert space with \(\dim H\ge2\), and let \(A:H\to H\) be bounded and antilinear. For every positive integer \(k\le\dim H\), define its normalized trace-frame numerical range by
\[
\mathcal W_k(A)=\left\{\frac1k\sum_{j=1}^k\langle Ax_j,x_j\rangle:\ (x_1,\ldots,x_k)\text{ is an orthonormal frame}\right\}.
\]
The inner product is linear in the first variable. Write \(A^\#\) for the antilinear adjoint and let \(B=(A+A^\#)/2\) be the self-adjoint antilinear part. Set \(Q=(B^2)^{1/2}\), which is positive and complex-linear. For every admissible \(j\), define the generalized singular value
\[
\sigma_j(Q)=\inf_{\substack{F\subset H\\\dim F<j}}\|Q|_{F^\perp}\|,
\qquad R_k=\frac1k\sum_{j=1}^k\sigma_j(Q).
\]
Then \(\mathcal W_k(A)\) is **precisely** the centered disk of radius \(R_k\), including or excluding its boundary as follows:
\[
\boxed{\mathcal W_k(A)=
\begin{cases}
\{z:|z|\le R_k\}, & \dim E_Q([\sigma_k(Q),\infty))\ge k,\\
\{z:|z|<R_k\}, & \dim E_Q([\sigma_k(Q),\infty))<k.
\end{cases}}
\]
Here \(E_Q\) is the spectral projection of \(Q\). In particular every finite-dimensional trace-frame range is a closed disk; for infinite-dimensional spaces the boundary may fail to be attained. The degenerate case \(R_k=0\) always follows the first line and gives \(\{0\}\).

The complete sequence of these disks reconstructs the generalized singular values of the symmetric antilinear part:
\[
\boxed{\sigma_k(Q)=kR_k-(k-1)R_{k-1}},\qquad k\ge1,
\]
with \(R_0=0\). Consequently, in infinite dimension, \(B\) is compact exactly when \(R_k\to0\); for \(1\le p<\infty\), \(B\in\mathcal S_p\) exactly when
\[
\sum_{k\ge1}[kR_k-(k-1)R_{k-1}]^p<\infty.
\]
These assertions concern \(B\), not the skew-adjoint antilinear component \((A-A^\#)/2\), which the trace-frame ranges cannot detect.

## Assumptions and scope
No separability hypothesis is needed. In the finite-dimensional case, \(k\) may equal \(\dim H\). In infinite dimension \(k\) is always finite. The generalized singular values are the Hilbert-space approximation numbers of \(Q\); for compact \(B\) they are its ordinary Takagi singular values, including zeros. The Schatten statements use the singular spectrum of the antilinear operator through its positive modulus \(Q\). Boundary inclusion concerns the actual range, not merely its closure. The one-dimensional exception is deliberately excluded: a nonzero antilinear operator on \(\mathbb C\) has a circular, not disk-shaped, trace-frame range.

## Proof
**1. The symmetric reduction and polar real form.** In any fixed conjugation coordinates write \(Ax=M\overline x\). Then \(A^\#x=M^{\mathsf T}\overline x\), and \(\langle Ax,x\rangle=\langle Bx,x\rangle\), since the skew-symmetric matrix part makes zero quadratic form. The invariant identity also follows by the definition of the antilinear adjoint. Since \(B=B^\#\), the operator \(B^2\) is positive complex-linear, \(B\) commutes with \(Q=(B^2)^{1/2}\), and the polar factor \(J=BQ^{-1}\) on \((\ker Q)^\perp\) is an antilinear isometric involution commuting with \(Q\). Extend \(J\) to any conjugation on \(\ker Q\). Thus \(B=JQ\), \(J^2=I\), and \(JQ=QJ\). By Cauchy–Schwarz applied to \(Q^{1/2}x\),
\[
|\langle Bx,x\rangle|
=|\langle JQ^{1/2}x,Q^{1/2}x\rangle|
\le\langle Qx,x\rangle.
\]
Moreover every \(J\)-fixed unit vector satisfies \(\langle Bx,x\rangle=\langle Qx,x\rangle\ge0\). Each spectral subspace of \(Q\) is \(J\)-invariant and admits orthonormal \(J\)-fixed vectors.

**2. Radius and the boundary criterion.** For any orthonormal \(k\)-frame,
\[
\left|\sum_{j=1}^k\langle Ax_j,x_j\rangle\right|
\le\sum_{j=1}^k\langle Qx_j,x_j\rangle
\le\sum_{j=1}^k\sigma_j(Q).
\]
The last inequality is the positive-operator Ky Fan variational principle (valid for generalized singular values). Conversely, select \(k\) mutually orthogonal \(J\)-fixed vectors in suitable high spectral subspaces of \(Q\). The Ky Fan supremum can be approached by such vectors, proving that the upper bound is sharp. To determine attainment, put \(a=\sigma_k(Q)\). By the min–max definition the spectral subspace \(E_Q((a,\infty))H\) has dimension \(m<k\); its eigenvalues, with multiplicities, are the first \(m\) generalized singular values above \(a\). For any rank-\(k\) orthogonal projection \(P\),
\[
\operatorname{tr}(PQ)=ka+
\operatorname{tr}(P(Q-aI)_+)-\operatorname{tr}(P(aI-Q)_+)
\le ka+\operatorname{tr}((Q-aI)_+).
\]
Here \((Q-aI)_+\) has finite rank \(m\). The right-hand side is \(\sum_{j=1}^k\sigma_j(Q)\). Equality requires \(P\) to contain \(E_Q((a,\infty))H\) and to have its remaining \(k-m\) dimensions inside \(E_Q(\{a\})H\). It exists exactly when \(\dim E_Q([a,\infty))\ge k\). In this case choosing a \(J\)-fixed orthonormal basis of that maximizing invariant subspace also makes the first inequality an equality, proving the asserted disk-boundary condition.

**3. Zero belongs to every range and disks have no holes.** The complex Stiefel space of orthonormal \(k\)-frames is path connected: any two frames lie in a finite-dimensional subspace and are joined by a path of unitaries. The continuous trace-frame functional therefore has connected range. Multiplying every vector in the frame by a common unimodular phase rotates its value by twice that phase, so the range is circularly symmetric.

If \(\dim H=\infty\), recursively choose \(k\) mutually orthogonal unit vectors, each having zero antilinear quadratic form. At each step the orthogonal complement has dimension at least two; the restriction of the quadratic form there has a nonzero isotropic vector because a homogeneous complex quadratic polynomial in two variables has a projective root.

If \(n=\dim H<\infty\), use Takagi coordinates \(\langle Bx,x\rangle=\sum_{j=1}^n s_jy_j^2\), where \(s_1\ge\cdots\ge s_n\ge0\) and \(y\) is related to \(x\) by a unitary transformation. In each selected pair of coordinate directions, the two orthonormal columns \((1,i)/\sqrt2\) and \((i,1)/\sqrt2\) make their *sum* of quadratic values zero. This deals with even \(k\). For odd \(k<n\), pair \(k-1\) columns and choose the last column isotropic in two unused coordinate directions. For odd \(k=n\ge3\), pair \(n-3\) columns, leaving positive coefficients \(a\ge b\ge c\) on a final three-dimensional block. If \(a+b>0\), put \(t=c/(a+b)\in[0,1]\), choose \(\phi\) with \(\cos(2\phi)=t\), use the two columns of
\[
U_2=\begin{pmatrix}\cos\phi&i\sin\phi\\i\sin\phi&\cos\phi\end{pmatrix}
\]
on the first two axes, and the column \(ie_3\) on the third. Their total quadratic sum is \(t(a+b)-c=0\). If \(a+b=0\), all three coefficients vanish. Hence zero belongs to the range for every \(n\ge2\).

A connected, circularly symmetric subset of \(\mathbb C\) containing zero and with supremal radius \(R_k\) is exactly a centered open or closed disk. Step 2 decides which.

**4. Spectral reconstruction and ideal tests.** By definition \(kR_k=\sum_{j=1}^k\sigma_j(Q)\), so consecutive differences recover each \(\sigma_k(Q)\). On an infinite-dimensional Hilbert space these numbers decrease to the essential norm of \(Q\); hence \(R_k\to\|Q\|_{\mathrm{ess}}\). Compactness is equivalent to their limit being zero. Summability of their \(p\)-th powers is precisely Schatten \(\mathcal S_p\) membership. This completes the proof.

## Verification
The standalone `verify_trace_ranges.py` uses random Takagi matrices with an independently generated skew-symmetric part and verifies the sharp radius, explicit zero-frame constructions for all dimension/parity cases, random-frame upper bounds, and inversion of the radius profile for dimensions \(2\) through \(10\). It is supplemental finite evidence only. The infinite-dimensional statements and spectral endpoint criteria are proven in the preceding four steps; no finite experiment is used as an infinite-dimensional certificate. Two diagnostic noncompact examples are \(Q=I\), where every radius is one and the boundary is included, and \(Q=\operatorname{diag}(1-1/(j+1))_{j\ge1}\), where every radius is one but the boundary is excluded because one is not an eigenvalue.

## Relationship to prior work
Majumdar and Müller, arXiv:2610.16823v1 (October 12, 2026), Section 7, introduce these normalized trace-frame numerical ranges and prove disk geometry for infinite-dimensional antilinear operators. That shape theorem alone neither specifies the disk radius, determines whether its boundary belongs, nor reconstructs singular data from the collection of radii. Kołaczek and Müller (2024) establish the disk shape of the ordinary \(k=1\) antilinear numerical range. Classical Ky Fan variational theory and the spectral representation of antilinearly self-adjoint operators supply the background tools. Their combination with the trace-frame definition gives the complete quantitative and attainment classification stated here. In particular the \(k=1\) radius is not presented as independent of standard numerical-radius theory; the distinctive claims involve all \(k\), the exact endpoint test and recovery of the singular sequence.

## Limitations
The output is insensitive to the skew-adjoint antilinear component of \(A\), so it does not determine the whole original operator. In infinite dimensions the generalized singular sequence records essential spectral magnitude but not the full spectral measure. The equality characterization concerns the existence of a maximizing frame, not an explicit parametrization of every maximizing frame. Prior literature on Ky Fan principles or complex-symmetric operator congruence might contain an equivalent formulation, and independent mathematical validation has not been performed.

## References
1. A. Majumdar and V. Müller, *Some Generalized Numerical Ranges of Real-linear Operators on Hilbert Spaces*, arXiv:2610.16823v1, publicly submitted October 12, 2026, Section 7, https://arxiv.org/abs/2610.16823.
2. D. Kołaczek and V. Müller, *Numerical Ranges of Antilinear Operators*, Integral Equations and Operator Theory 96 (2024), article 17, https://doi.org/10.1007/s00020-024-02768-5.
3. S. Ruotsalainen, *On a Weyl-von Neumann-type Theorem for Antilinear Self-adjoint Operators*, arXiv:1203.4670 (2012), https://arxiv.org/abs/1203.4670.
4. M. Marcus and B. N. Moyls, *On the Maximum Principle of Ky Fan*, Canadian Journal of Mathematics, historical Ky Fan variational principle, https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/on-the-maximum-principle-of-ky-fan/664EF49EF49D15CC71888B0E03E18659.
