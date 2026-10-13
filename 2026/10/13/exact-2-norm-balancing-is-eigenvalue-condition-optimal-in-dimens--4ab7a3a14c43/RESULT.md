# Exact 2-norm balancing is eigenvalue-condition optimal in dimension two, but dimension three is already harmful

## Finding
Exact 2-norm matrix balancing has a sharp low-dimensional dichotomy for simple-eigenvalue conditioning.

For an irreducible real matrix \(A\), exact Osborne 2-norm balancing chooses a positive diagonal similarity
\[
\widetilde A=D^{-1}AD
\]
whose \(i\)-th row and \(i\)-th column have equal Euclidean norm. For a simple eigenvalue \(\lambda\), write its absolute condition number as
\[
\chi(\lambda,A)
=
\frac{\|x\|_2\|z\|_2}{|z^{\mathsf T}x|},
\]
where
\[
Ax=\lambda x,
\qquad
z^{\mathsf T}A=\lambda z^{\mathsf T}.
\]

In dimension two, the exact balanced matrix simultaneously minimizes \(\chi\) for every simple eigenvalue over the full positive diagonal-similarity orbit.

In dimension three this universal protection fails. For every \(t>0\), define
\[
B_t=
\begin{pmatrix}
t+1&t&1\\
t&t+1&1\\
1&-1&2t+2
\end{pmatrix},
\qquad
D_t=
\operatorname{diag}
\left(
1,1,\sqrt{2t+1}
\right),
\]
and
\[
A_t=D_tB_tD_t^{-1}.
\]
The matrix \(B_t\) is exactly 2-norm balanced and is the exact balance of \(A_t\). Both matrices have the positive real spectrum
\[
\{1,2t+1,2t+2\}.
\]
For the simple eigenvalue
\[
\lambda_t=2t+2,
\]
one has
\[
\chi(\lambda_t,A_t)
=
\frac{2t+3}{2t+1},
\]
but
\[
\chi(\lambda_t,B_t)
=
\frac{
\sqrt{3(4t^2+4t+3)}
}{
2t+1
}
>
\chi(\lambda_t,A_t).
\]
The damage factor satisfies
\[
\frac{\chi(\lambda_t,B_t)}
{\chi(\lambda_t,A_t)}
=
\frac{
\sqrt{3(4t^2+4t+3)}
}{
2t+3
}
\longrightarrow
\sqrt3.
\]

Meanwhile, balancing genuinely reduces the Frobenius norm:
\[
\|A_t\|_{\mathrm F}^2-\|B_t\|_{\mathrm F}^2
=
\frac{8t^2}{2t+1}>0.
\]
Thus norm improvement and eigenvalue-condition improvement separate already in the smallest possible dimension.

## Assumptions and scope
The balancing operation is exact Osborne balancing in the Euclidean norm, not the practical power-of-two approximation used by some software implementations. The matrix is assumed irreducible so the finite positive balancing similarity exists uniquely up to a scalar multiple.

The eigenvalue condition number is the standard absolute first-order condition number for a simple eigenvalue under unstructured matrix perturbations. The theorem does not concern the spectral condition number of the matrix itself.

The two-dimensional theorem permits real matrices with either real or complex simple eigenvalues. The three-dimensional obstruction has positive real spectrum, so complex-eigenvalue effects are not needed.

No finite-precision claim is made. Practical balancing can include permutations, power-of-two rounding, and stopping heuristics that are outside the exact theorem.

## Proof
Take an irreducible real \(2\times2\) matrix
\[
A=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix},
\qquad
bc\ne0.
\]
Up to an irrelevant scalar multiple, every positive diagonal similarity can be written as
\[
A_s=
\begin{pmatrix}
a&bs\\
c/s&d
\end{pmatrix},
\qquad
s>0.
\]
Let \(\lambda\) be a simple eigenvalue and set
\[
\tau=\lambda-a.
\]
Because \(bc\ne0\), one has \(\tau\ne0\). A right eigenvector and a left eigenvector row are
\[
x_s=
\begin{pmatrix}
bs\\
\tau
\end{pmatrix},
\qquad
z_s^{\mathsf T}
=
\begin{pmatrix}
c/s&\tau
\end{pmatrix}.
\]
Their bilinear product is invariant:
\[
z_s^{\mathsf T}x_s
=
bc+\tau^2.
\]
Therefore
\[
\chi(\lambda,A_s)^2
=
\frac{
\left(|b|^2s^2+|\tau|^2\right)
\left(|c|^2s^{-2}+|\tau|^2\right)
}{
|bc+\tau^2|^2
}.
\]
The only \(s\)-dependent term in the numerator is
\[
|\tau|^2
\left(
|b|^2s^2+|c|^2s^{-2}
\right).
\]
By the arithmetic-geometric mean inequality,
\[
|b|^2s^2+|c|^2s^{-2}
\ge
2|bc|,
\]
with equality uniquely at
\[
s^2=\left|\frac cb\right|.
\]
But this is exactly
\[
|bs|=|c/s|,
\]
which is the \(2\times2\) 2-norm balancing condition. The minimizing scale does not depend on \(\lambda\), so all simple eigenvalues are optimized simultaneously.

Now consider the three-dimensional family. Opposite off-diagonal entries of \(B_t\) have equal absolute values:
\[
|b_{12}|=|b_{21}|=t,
\qquad
|b_{13}|=|b_{31}|=1,
\qquad
|b_{23}|=|b_{32}|=1.
\]
Hence every row has the same off-diagonal Euclidean norm as the corresponding column. Adding the identical diagonal contribution on each row-column pair shows that \(B_t\) is exactly balanced.

A direct characteristic-polynomial calculation gives
\[
\det(\lambda I-B_t)
=
(\lambda-1)
(\lambda-(2t+1))
(\lambda-(2t+2)).
\]
For
\[
\lambda_t=2t+2,
\]
choose
\[
x=
(1,1,1)^{\mathsf T}
\]
and
\[
z=
\left(
\frac1{2t+1},
-\frac1{2t+1},
1
\right)^{\mathsf T}.
\]
Then
\[
B_tx=\lambda_t x,
\qquad
z^{\mathsf T}B_t=\lambda_t z^{\mathsf T},
\qquad
z^{\mathsf T}x=1.
\]
Thus
\[
\chi(\lambda_t,B_t)^2
=
3
\left(
1+\frac{2}{(2t+1)^2}
\right)
=
\frac{3(4t^2+4t+3)}{(2t+1)^2}.
\]

Since
\[
A_t=D_tB_tD_t^{-1},
\]
the corresponding right and left eigenvectors are
\[
D_tx
\quad\text{and}\quad
D_t^{-1}z.
\]
Their bilinear product is still \(1\), while
\[
\|D_tx\|_2^2
=
2+(2t+1)
=
2t+3
\]
and
\[
\|D_t^{-1}z\|_2^2
=
\frac{2}{(2t+1)^2}
+
\frac1{2t+1}
=
\frac{2t+3}{(2t+1)^2}.
\]
Hence
\[
\chi(\lambda_t,A_t)
=
\frac{2t+3}{2t+1}.
\]
Finally,
\[
\chi(\lambda_t,B_t)^2
-
\chi(\lambda_t,A_t)^2
=
\frac{8t^2}{(2t+1)^2}>0.
\]
The asymptotic factor follows immediately.

For the Frobenius norm, diagonal similarity leaves the diagonal entries unchanged. Directly comparing the six off-diagonal squares gives
\[
\|A_t\|_{\mathrm F}^2-\|B_t\|_{\mathrm F}^2
=
\frac{8t^2}{2t+1}>0.
\]

## Verification
The embedded `verify.py` uses exact rational arithmetic for the squared condition numbers, characteristic polynomial, and Frobenius-norm difference at several rational values of \(t\). It also reconstructs the concrete \(t=1\) example and verifies the eigenvector identities exactly after adjoining the formal factor \(\sqrt3\) through squared norms.

The two-dimensional optimum is proved analytically by a one-variable arithmetic-geometric mean inequality; finite testing is not used to establish it.

## Relationship to prior work
Osborne introduced exact Euclidean matrix balancing by diagonal similarity, and Parlett and Reinsch developed the practical balancing procedure used in eigenvalue computation.

Watkins gave a classical example where balancing a Hessenberg matrix degrades eigenvalue condition numbers and consequently eigenvalue accuracy. His examples are large numerical matrices and establish that harmful balancing is a genuine phenomenon.

James, Langou, and Lowery revisit matrix balancing and eigenvector computation. They state that exact 2-norm balancing of an irreducible matrix is unique, emphasize that balancing reduces a matrix norm rather than directly optimizing eigenvalue conditioning, and discuss examples in which conditioning or backward error deteriorates.

The result here identifies an exact low-dimensional boundary inside that classical phenomenon. In dimension two, exact 2-norm balancing is not merely harmless: it is the simultaneous optimizer of every simple eigenvalue condition number over all positive diagonal similarities. Dimension three is already enough for strict harm, even with positive real spectrum and while the Frobenius norm strictly decreases.

Targeted searches using exact balancing, diagonal similarity, two-by-two eigenvalue conditioning, minimal dimension, and harmful balancing terminology did not locate the two-dimensional simultaneous-optimality theorem or the displayed three-dimensional one-parameter obstruction.

## Limitations
The theorem concerns exact 2-norm balancing. Practical power-of-two balancing and implementation-specific stopping criteria can behave differently.

The harmful three-dimensional family gives an asymptotic worsening factor \(\sqrt3\); no claim is made that \(\sqrt3\) is the global worst possible factor in dimension three.

The result concerns simple-eigenvalue absolute conditioning, not eigenvector conditioning, backward error, pseudospectral area, or the condition number of the entire eigenvector matrix.

Older scaling literature is extensive. A differently phrased version of the two-dimensional optimality observation or a smaller explicit harmful example may exist outside the inspected sources; this remains the principal originality risk.

## References
1. E. E. Osborne, “On Pre-Conditioning of Matrices,” Journal of the ACM 7 (1960), 338–345.
2. B. N. Parlett and C. Reinsch, “Balancing a Matrix for Calculation of Eigenvalues and Eigenvectors,” Numerische Mathematik 13 (1969), 293–304. DOI 10.1007/BF02165404.
3. D. S. Watkins, “A Case Where Balancing Is Harmful,” Electronic Transactions on Numerical Analysis 23 (2006), 1–4.
4. R. James, J. Langou, and B. R. Lowery, “On Matrix Balancing and Eigenvector Computation,” arXiv:1401.5766v1, submitted 2014-01-22.
