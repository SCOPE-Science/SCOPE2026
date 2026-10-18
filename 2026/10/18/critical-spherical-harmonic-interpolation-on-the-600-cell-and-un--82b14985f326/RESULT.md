# Critical spherical-harmonic interpolation on the 600-cell and uniquely optimal sampling weights

## Finding

Let \(X\) be the \(120\) vertices of the regular 600-cell on the probability-normalized sphere \(S^3\). Let \(\mathcal H_{<L}\) be the direct sum of spherical harmonics of degrees \(0,1,\ldots,L-1\), with the probability-surface \(L^2\) inner product. Let \(R_L:\mathcal H_{<L}\to\mathbb C^X\) be evaluation, with probability counting measure on \(X\). For \(L=1,\ldots,8\), its exact ranks are
\[
\bigl(1,5,14,30,55,91,116,120\bigr).
\]
Thus \(L=8\) (degree at most seven) is the **first** cutoff with surjective point sampling. Its complete squared singular-value spectrum, with multiplicities, is
\[
\operatorname{spec}(R_8R_8^*)
=\left\{1^{[55]},\ \left(\tfrac74\right)^{[16]},\ \left(\tfrac73\right)^{[45]},\ 4^{[4]}\right\}.
\]
Consequently, the smallest squared singular value is exactly \(1\), the largest is exactly \(4\), and the sharp condition number of the surjective restriction operator is \(2\). For comparison, at the preceding cutoff, \(L=7\), the complete spectrum on the \(120\)-dimensional sample space is
\[
\left\{0^{[4]},\ 1^{[91]},\ \left(\tfrac74\right)^{[16]},\ \left(\tfrac73\right)^{[9]}\right\}.
\]

For every strictly positive vertex-weight family \(w=(w_x)_{x\in X}\), define weighted sampling by \((R_{8,w}f)(x)=\sqrt{w_x}\,f(x)\), with the same probability-counting norm. Then
\[
\boxed{\ \kappa(R_{8,w})\ge 2,\quad\text{with equality if and only if all }w_x\text{ are equal}.\ }
\]
The statement is invariant under a common scaling of all weights. The minimum-norm interpolant of arbitrary data \(g\in\mathbb C^X\) is given explicitly below.

## Assumptions and scope

Write \(\varphi=(1+\sqrt5)/2\). Define \(X\subset S^3\subset\mathbb R^4\) as the union of (a) the eight signed coordinate vectors, (b) the sixteen vectors \((\pm1,\pm1,\pm1,\pm1)/2\), and (c) the ninety-six vectors obtained by the twelve even permutations of
\[
\left(0,\ \frac{\pm1}{2},\ \frac{\pm\varphi}{2},\ \frac{\pm(\varphi-1)}{2}\right),
\]
with three independent signs. The terms are disjoint and all have Euclidean norm one. The definition fixes every vertex explicitly; no orientation or labelling choice affects the findings.

Here \(\mathcal H_n\) denotes all complex spherical harmonics of exact degree \(n\) on \(S^3\), including their natural multiplicities \(\dim\mathcal H_n=(n+1)^2\). The continuous inner product uses normalized surface measure. The target \(\mathbb C^X\) is equipped with \(\langle u,v\rangle_X=120^{-1}\sum_{x\in X}u(x)\overline{v(x)}\). Singular values are those between these specified Hilbert spaces; zero singular values in the stated sample-space spectrum count the codimension of the sample image. The rank table concerns \(1\le L\le8\); no spectrum is asserted for higher cutoffs.

## Proof

**Step 1: Exact reproducing kernel.** On the probability sphere \(S^3\), the addition theorem for any continuous orthonormal basis of \(\mathcal H_n\) reads
\[
\sum_{j=1}^{(n+1)^2}Y_{n,j}(x)\overline{Y_{n,j}(y)}
=(n+1)U_n(\langle x,y\rangle),
\]
where \(U_0(t)=1\), \(U_1(t)=2t\), and \(U_{n+1}(t)=2tU_n(t)-U_{n-1}(t)\) are Chebyshev polynomials of the second kind. In particular, the sample-space Gram matrix \(B_L=R_LR_L^*\) is
\[
(B_L)_{xy}=\frac1{120}\sum_{n=0}^{L-1}(n+1)U_n(\langle x,y\rangle).
\]
We will also use the integer-scaled matrix \(C_L=120B_L\).

**Step 2: A fully finite exact distance-algebra certificate.** The pairwise inner products of \(X\) take exactly nine values, ordered as
\[
T=\bigl(-1,-\varphi/2,-1/2,-(\varphi-1)/2,0,(\varphi-1)/2,1/2,\varphi/2,1\bigr),
\]
with row multiplicities \((1,12,20,12,30,12,20,12,1)\). For the distance matrix \(A_i\), put \((A_i)_{xy}=1\) exactly when \(\langle x,y\rangle=T_i\). Direct enumeration from the displayed \(120\) algebraic coordinates gives nonnegative integers \(p_{ij}^k\) satisfying
\[
 A_iA_j=\sum_{k=1}^{9}p_{ij}^k A_k,
\qquad
p_{ij}^k=\#\{z\in X:\langle x,z\rangle=T_i,\ \langle z,y\rangle=T_j\}
\]
for every ordered pair \((x,y)\) at level \(T_k\). This identity is checked for **every** such pair, not inferred from random examples or assumed from a group-action slogan. The accompanying `CHECKER.py` constructs the coordinates exactly in \(\mathbb Z[\varphi]\), verifies the complete \(120^2\)-pair closure, and works entirely in the resulting nine-dimensional algebra. It proves the following exact matrix polynomial identities:
\[
 C_L(C_L-120I)=0\quad(1\le L\le6),
\]
\[
 C_7(C_7-120I)(C_7-210I)(C_7-280I)=0,
\]
\[
 (C_8-120I)(C_8-210I)(C_8-280I)(C_8-480I)=0.
\]
Here the second-kind polynomial recurrence is applied at all nine algebraic levels; multiplication of the resulting class vectors uses the exhaustive integer intersection counts. This is an exact finite proof of the displayed identities, not a floating-point estimate.

**Step 3: Exact eigenvalue multiplicities.** Each \(C_L\) is a real symmetric positive semidefinite Gram matrix and therefore diagonalizable; its eigenvalues belong to the finite root sets in Step 2. For a class vector \(c\), its matrix trace equals \(120\) times the coefficient of the identity level \(T=1\). At \(L=7\), the traces of powers \(0,1,2,3\) of \(C_7\) are, respectively,
\[
(120,16800,2721600,502992000).
\]
The associated Vandermonde system at roots \((0,120,210,280)\) gives multiplicities \((4,91,16,9)\). At \(L=8\), the corresponding traces are
\[
(120,24480,5947200,1673424000),
\]
and the roots \((120,210,280,480)\) have multiplicities \((55,16,45,4)\). At each \(L\le6\), the projection identity in Step 2 makes the nonzero \(C_L\)-eigenvalue exactly \(120\); its multiplicity, determined by the trace, is \(\sum_{j=1}^{L}j^2\). Dividing eigenvalues by \(120\) establishes both spectra and the entire rank table. The first surjective cutoff is \(L=8\), since \(L=7\) has sample codimension four and \(L=8\) has no zero eigenvalue.

**Step 4: Unique optimality of equal positive weights.** Let \(B=B_8\), which is positive definite by Step 3. Scale weights to satisfy \(120^{-1}\sum_xw_x=1\) (this does not affect conditioning), and let \(W=\operatorname{diag}(w_x)\). The nonzero singular-value squares of \(R_{8,w}\) are the eigenvalues of \(B^{1/2}WB^{1/2}\). The 600-cell vertices constitute the binary icosahedral subgroup of the unit quaternions, so its left translations act transitively on \(X\) by orthogonal transformations preserving \(B\). The average of the conjugates of \(W\) under these permutations is \(I\). Therefore the convexity of the maximum eigenvalue and concavity of the minimum eigenvalue imply
\[
\lambda_{\max}(B^{1/2}WB^{1/2})\ge\lambda_{\max}(B)=4,
\quad
\lambda_{\min}(B^{1/2}WB^{1/2})\le\lambda_{\min}(B)=1.
\]
Thus \(\kappa(R_{8,w})\ge2\). The exact certificate also gives \(B\mathbf1=\mathbf1\). The Rayleigh quotient of \(B^{1/2}WB^{1/2}\) at \(\mathbf1\) is \(1\). If equality holds in the condition bound, both preceding inequalities must be equalities and the minimum eigenvalue must be \(1\). Consequently \(\mathbf1\) is a minimum eigenvector. Because \(B^{1/2}\mathbf1=\mathbf1\) and \(B^{1/2}\) is invertible, the resulting eigenvector equation forces \(W\mathbf1=\mathbf1\). Hence every normalized weight is exactly \(1\); undoing common normalization proves uniqueness up to scale.

**Step 5: Explicit interpolation.** The spectral polynomial identity also gives
\[
B^{-1}=\frac{441I-342B+109B^2-12B^3}{196},
\]
verified by exact distance-algebra multiplication. For any \(g\in\mathbb C^X\), the unique interpolant of minimum \(L^2(S^3)\) norm in \(\mathcal H_{<8}\) is
\[
 f_{\min}(z)=\frac1{120}\sum_{x\in X}
 \bigl(B^{-1}g\bigr)(x)
 \sum_{n=0}^{7}(n+1)U_n(\langle z,x\rangle).
\]
Indeed this equals \(R_8^*(R_8R_8^*)^{-1}g\), and applying \(R_8\) returns \(g\). The operator norm of the minimum-norm right inverse is \(1\) in the specified probability norms.

## Verification

Run `python CHECKER.py` with Python's standard library. It deterministically constructs all \(120\) vertices with integer-pair coordinates in \(\mathbb Z[\varphi]\), verifies each one has norm one and all are distinct, classifies all pairwise inner products, enumerates the full nine-class intersection algebra, and exhaustively checks its multiplication law on every ordered vertex pair. It then checks the polynomial annihilators, solves exact rational Vandermonde systems for all eigenvalue multiplicities, and checks the constant eigenvector and inverse-polynomial identity. No floating-point numerical rank test, opaque table, external paper, or random search is used for the finite certificate. The proof of weighted uniqueness follows analytically from these checked facts and transitivity; the checker does not enumerate a continuum of weights.

## Relationship to prior work

Dowker's 2009 work on harmonics of factored three-spheres develops binary-icosahedral invariant and equivariant modes; it does not, in the inspected full-text Sections 5–6, give a \(120\)-node evaluation-Gram spectrum, an interpolation cutoff, or a weighted condition-number optimum. Bannai–Okuda–Tagami (2013) discuss exceptional harmonic-index designs including the 600-cell. Hirao–Nozaki–Tasaka (2025) determine the harmonic-strength set of the binary icosahedral group and prove uniqueness/minimality properties; their explicit invariant-harmonic and addition-theorem calculations establish a different kind of moment information. In particular, 11-design exactness alone gives no individual nonzero singular-value multiplicities at a cutoff whose reproducing-kernel products can reach degree fourteen. The present claim is a finite-spectrum and sharp-weighting theorem for evaluation maps, not a new claim about the design strength or the representation-ring decomposition.

The established general Peter–Weyl and spherical-addition-theorem machinery underlies Step 1; the specific spectrum and uniqueness claim are independently reconstructed by the exact distance-algebra certificate rather than treated as consequences of unchecked representation multiplicity tables. A more general group-sampling formula could make the spectral part a special case, which remains an originality risk.

## Limitations

The computed ranks and spectral multiplicities concern precisely the \(120\)-vertex 600-cell and integer cutoffs \(1\le L\le8\), with the normalization stated above. No analogous claim is made for other point sets, for negative or complex sampling weights, or for larger spectral cutoffs. The interpolation norm refers to the minimum-norm right inverse, not uniqueness of the bandlimited interpolating function, since \(\dim\mathcal H_{<8}=204>120\). The finite certificate is exhaustive for this finite configuration; it is not a symbolic proof for all binary polyhedral groups. Related literature was compared in publicly accessible full-text portions and indexed research results, but an undiscovered broader spectral-sampling theorem is possible.

## References

1. J. S. Dowker, *Harmonics on the factored three-sphere and the Hopf map*, arXiv:0909.3380v1, first submitted 18 September 2009. https://arxiv.org/abs/0909.3380
2. E. Bannai, T. Okuda, and M. Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101v1, first submitted 23 August 2013. https://arxiv.org/abs/1308.5101
3. M. Hirao, H. Nozaki, and K. Tasaka, *Spherical designs for finite quaternionic unit groups and their applications to modular forms*, arXiv:2507.01358v1, first submitted 2 July 2025. https://arxiv.org/abs/2507.01358
