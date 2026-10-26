# A two-singular-value law for constrained numerical disks of self-adjoint antilinear matrices

## Finding
For every complex dimension \(n\ge3\), every self-adjoint conjugate-linear map \(Ax=M\overline x\) with \(M=M^{\mathsf T}\), and every \(q\in\mathbb C\) with \(|q|\le1\), the constrained numerical range is the exact centered disk
\[
W_q(A)=\left\{z\in\mathbb C:|z|\le R_A(|q|)\right\},\qquad
R_A(t)=\frac{(1+t)s_1+(1-t)s_2}{2},
\]
where \(s_1\ge s_2\ge0\) are the first two Takagi singular values of \(M\). Therefore \(s_1=R_A(1)\) and \(s_2=2R_A(0)-R_A(1)\): this whole family of constrained disks detects precisely the two largest Takagi singular values, no others.

## Assumptions and scope
The inner product is \(\langle x,y\rangle=\sum_j x_j\overline{y_j}\), linear in its first variable. A map is conjugate-linear if \(A(\lambda x)=\overline\lambda Ax\). Its matrix is symmetric \(M=M^{\mathsf T}\), equivalently the conjugate-linear adjoint equals \(A\). Its Takagi values are the usual singular values of \(M\), counting multiplicities, which are nonnegative. Here \(n\ge3\), \(q\in\mathbb C\), \(|q|\le1\); \(W_q(A)\) uses pairs of unit vectors with \(\langle x,y\rangle=q\). The theorem does not claim the same disk shape in dimension two or for nonsymmetric coefficient matrices.

## Proof
**Reduction.** By Takagi factorization and unitary change of orthonormal coordinates, assume \(M=\operatorname{diag}(s_1,\dots,s_n)\). Multiplying one frame vector by a unimodular scalar reduces the radius problem to the constraint \(\langle x,y\rangle=t=|q|\) without changing absolute values.

**Sharp upper bound.** Write \(S=\operatorname{diag}(s_1,\dots,s_n)\) and \(K=(xy^{\mathsf T}+yx^{\mathsf T})/2\). Symmetry of \(S\) gives \(|\langle Ax,y\rangle|=|\operatorname{tr}(SK)|\). For \(0\le t<1\), the vectors
\[
u=\frac{x+y}{\sqrt{2(1+t)}},\qquad v=\frac{x-y}{\sqrt{2(1-t)}}
\]
are orthonormal. Consequently \(K=\frac{1+t}{2}uu^{\mathsf T}-\frac{1-t}{2}vv^{\mathsf T}\), and its only nonzero singular values are \((1+t)/2\) and \((1-t)/2\). The von Neumann trace inequality then yields
\[
|\operatorname{tr}(SK)|\le\frac{1+t}{2}s_1+\frac{1-t}{2}s_2.
\]
At \(t=1\) the rank-one form \(K=xx^{\mathsf T}\) gives the same inequality.

**Attainment.** In the Takagi basis let \(e_1,e_2\) denote the first two basis vectors, put \(a=\sqrt{(1+t)/2}\), \(b=\sqrt{(1-t)/2}\), and set \(x=ae_1+ib e_2\), \(y=ae_1-ib e_2\). Both vectors have norm one, \(\langle x,y\rangle=t\), and \(|\langle Ax,y\rangle|=a^2s_1+b^2s_2\). Undoing the phase reduction gives an attaining frame for every complex \(q\).

**Disk filling.** The constrained unit-frame space is connected: for \(t<1\) it is parametrized by the complex Stiefel manifold of orthonormal two-frames; for \(t=1\), by the unit sphere. The modulus of the defining value therefore has interval image. This interval contains zero: a homogeneous complex quadratic form in at least two variables has a nonzero isotropic vector, so choose unit \(x\) with \(\langle Ax,x\rangle=0\); for \(t<1\), choose a unit \(z\) orthogonal to both \(x\) and \(Ax\), possible since \(n\ge3\), and put \(y=\overline q x+\sqrt{1-|q|^2}z\). Then \(\langle x,y\rangle=q\) and \(\langle Ax,y\rangle=0\). For \(t=1\), use \(y=\overline q x\). A simultaneous phase rotation of \(x,y\) rotates \(\langle Ax,y\rangle\) through a full circle while preserving \(q\); thus every complex point between the minimum zero and the sharp maximum is attained. Compactness yields the closed disk.

**Spectral extraction.** The displayed radius is affine in \(t\). Evaluating at \(t=0,1\) yields the claimed recovery of the top two singular values. Changing lower singular values cannot change any disk in this family. If \(s_1=s_2\), all radii are equal; otherwise the radius is strictly increasing in \(|q|\).

## Verification
A standalone NumPy checker evaluates the endpoint witness and samples 10,500 admissible complex pairs across dimensions 3, 4, and 6 and five \(q\) values for each of seven random singular spectra. It checks the candidate upper bound and witness within numerical tolerance. Finite checks are corroboration; the Takagi factorization, rank-two singular-value calculation, von Neumann trace bound, and disk-filling argument prove the assertion in all finite dimensions \(n\ge3\).

Run \(python verify_takagi_q.py\) with NumPy. The script is supplied alongside this result.

## Relationship to prior work
Majumdar and Müller introduce constrained \(q\)-numerical ranges for real-linear operators and establish their centered-disk geometry for conjugate-linear operators in dimension at least three (Theorem 6.6). Their result does not supply the disk radius or its two-singular-value spectral reconstruction. Earlier two-dimensional annulus calculations for general conjugate-linear matrices do not by themselves classify the full higher-dimensional radius extremum. Here the new statement is a sharp higher-dimensional spectral formula within the natural self-adjoint conjugate-linear subclass. Takagi factorization and the von Neumann trace inequality are standard inputs and are not claimed as new.

## Limitations
The result concerns finite dimensions at least three and conjugate-linear operators whose coefficient matrices are symmetric. It does not classify general nonsymmetric conjugate-linear maps, does not recover singular values beyond the two largest, and makes no unconditional claim of priority over unindexed formulations. Equality is exhibited but a full characterization of all attaining frames is not asserted.

## References
1. A. Majumdar and V. Müller, *Some Generalized Numerical Ranges of Real-linear Operators on Hilbert Spaces*, arXiv:2610.16823v1, first submitted 12 October 2026, especially Definition 6.1 and Theorem 6.6, https://arxiv.org/abs/2610.16823.
2. Autonne–Takagi diagonal factorization for complex symmetric matrices (classical theorem).
3. Von Neumann's singular-value trace inequality (classical theorem).
