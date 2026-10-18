# Maximal midpoint instability of an extreme numerical-radius unitary

## Finding

Let \(H=\ell_2(\mathbb N;\mathbb C)\), let \(\mathcal B(H)\) be its bounded operators, and endow \(\mathcal B(H)\) with the complex numerical-radius norm
\[
w(T)=\sup_{\|x\|_2=1}|\langle Tx,x\rangle|.
\]
For a diagonal unitary \(Ue_j=\lambda_j e_j\), with \(|\lambda_j|=1\), the following assertions hold.

**Exact versus approximate antipodality.** The operator \(U\) is an extreme point of the numerical-radius unit ball if and only if \(\lambda_j+\lambda_k\ne0\) for every distinct pair of indices \(j,k\). If these inequalities hold but
\[
\inf_{j\ne k}|\lambda_j+\lambda_k|=0,
\]
then, for **every** \(\varepsilon>0\),
\[
\sup\left\{w(X-Y): w(X),w(Y)\le1,\quad
 w\!\left(\frac{X+Y}{2}-U\right)<\varepsilon\right\}=2.
\]
In particular, \(U\) is extreme but not strongly extreme (equivalently, it is not a midpoint locally uniformly rotund point).

An explicit operator with this property is
\[
U=\bigoplus_{n\ge1}\begin{pmatrix}1&0\\0&-e^{i/(n+2)}\end{pmatrix}
\quad\text{on}\quad \ell_2(\mathbb N;\mathbb C^2).
\]
The supremal diameter \(2\) is the maximum permitted by the triangle inequality; the striking point is that it occurs at arbitrarily small neighborhoods of the midpoint of an extreme point.

## Assumptions and scope

All Hilbert spaces and operators are **complex**. The spectrum in the main criterion is a diagonal pure-point spectrum with a fixed orthonormal eigenbasis; no assertion about arbitrary continuous-spectrum normal operators is made. The index set is countably infinite, with at least two indices. Distinct indices may have the same unimodular eigenvalue. A point \(U\) of a norm-one ball is *strongly extreme* if sequences \(X_n,Y_n\) in the ball with \((X_n+Y_n)/2\to U\) in norm necessarily satisfy \(X_n-Y_n\to0\). The numerical radius is an equivalent norm on \(\mathcal B(H)\), and \(w(V\oplus W)=\max\{w(V),w(W)\}\) for orthogonal block sums.

## Proof

**Step 1: the two-dimensional criterion.** Let \(D=\operatorname{diag}(\lambda,\mu)\) with \(|\lambda|=|\mu|=1\). Suppose \(w(D\pm A)\le1\). Testing the two coordinate unit vectors gives
\[
|\lambda\pm A_{11}|\le1,\qquad |\mu\pm A_{22}|\le1,
\]
so \(A_{11}=A_{22}=0\), since a boundary point of the closed complex disk cannot be the midpoint of two distinct disk points. For a unit vector \(e_j\), the positive-semidefinite matrix
\[
I-\operatorname{Re}\bigl(\overline{\lambda_j}(D+A)\bigr)
\]
has zero \((j,j)\) entry, and hence a zero \(j\)-th row and column. Applying this for \(j=1,2\) gives
\[
A_{21}=-\lambda^2\overline{A_{12}},\qquad
A_{12}=-\mu^2\overline{A_{21}}.
\]
Consequently \(A_{12}=(\mu/\lambda)^2 A_{12}\). If \(\mu\ne\pm\lambda\), then \(A=0\). If \(\mu=\lambda\), then \(D=\lambda I\) and, for every unit vector \(x\), the same midpoint argument applied to \(\lambda\pm\langle Ax,x\rangle\) yields \(\langle Ax,x\rangle=0\). Complex polarization gives \(A=0\). Thus \(D\) is extreme whenever \(\mu\ne-\lambda\).

Conversely, when \(\mu=-\lambda\), let
\[
J=\begin{pmatrix}0&i\\i&0\end{pmatrix},\qquad
W_\pm=\begin{pmatrix}1&\pm i\\\pm i&-1\end{pmatrix}.
\]
Both \(W_\pm\) are nonzero rank-one square-zero matrices with operator norm \(2\), whence their numerical radii are \(1\): a rank-one square-zero operator is unitarily similar to \(\begin{psmallmatrix}0&2\\0&0\end{psmallmatrix}\), whose numerical radius is \(1\). As \(D=(\lambda W_++\lambda W_-)/2\) with distinct numerical-radius contractions \(\lambda W_\pm\), \(D\) is not extreme.

**Step 2: the diagonal criterion in infinite dimension.** If \(\lambda_j=-\lambda_k\) for some distinct indices, the above nontrivial decomposition on their two-dimensional span, extended by \(U\) on the orthogonal complement, proves that \(U\) is not extreme: the direct-sum formula preserves the unit-ball condition. Conversely, suppose no exact antipodal pair exists and that \(U=(X+Y)/2\) with \(w(X),w(Y)\le1\). Compress to the span of any two distinct basis vectors. Numerical radius cannot increase under orthogonal compression, so the two-dimensional criterion forces the compression of each summand to equal the corresponding compression of \(U\). Every matrix entry of \(X-U\) and \(Y-U\) is therefore zero. Density of finite linear combinations of basis vectors implies \(X=Y=U\).

**Step 3: approximate antipodes create maximal instability.** Assume additionally \(\inf_{j\ne k}|\lambda_j+\lambda_k|=0\). Choose distinct pairs \((j_n,k_n)\) such that
\[
\delta_n=|\lambda_{j_n}+\lambda_{k_n}|\longrightarrow0.
\]
Let \(H_n\) vanish off the span of \(e_{j_n},e_{k_n}\) and have there the matrix \(\lambda_{j_n}J\). Then \(w(H_n)=1\). Replace the actual two-dimensional diagonal block \(\operatorname{diag}(\lambda_{j_n},\lambda_{k_n})\) by the antipodal one \(\lambda_{j_n}\operatorname{diag}(1,-1)\). Their operator-norm (hence numerical-radius) distance is exactly \(\delta_n\). Since \(w(\lambda_{j_n}W_\pm)=1\), the triangle inequality and the orthogonal direct-sum formula show
\[
w(U\pm H_n)\le1+\delta_n.
\]
Set \(X_n=(U+H_n)/(1+\delta_n)\) and \(Y_n=(U-H_n)/(1+\delta_n)\). Both are in the numerical-radius unit ball, and
\[
w\!\left(\frac{X_n+Y_n}{2}-U\right)=\frac{\delta_n}{1+\delta_n}\to0,
\qquad
w(X_n-Y_n)=\frac{2}{1+\delta_n}\to2.
\]
For every fixed \(\varepsilon>0\) these pairs, for sufficiently large \(n\), lie in the prescribed midpoint neighborhood and have separation arbitrarily close to \(2\). The reverse bound \(w(X-Y)\le w(X)+w(Y)\le2\) is universal, proving the stated exact supremum.

**Step 4: explicit instance.** Put \(\lambda_{2n-1}=1\) and \(\lambda_{2n}=-e^{i/(n+2)}\) for \(n\ge1\). None of these eigenvalues are exactly antipodal (the small positive angles lie in \((0,1/3]\)), whereas \(|1-e^{i/(n+2)}|\to0\). Steps 2 and 3 apply.

## Verification

The argument is analytic and applies to infinite-dimensional operator spaces; finite computations are not substituted for the infinite proof. The standalone `VERIFY.py` checks the algebra of the square-zero witness, the exact numerical-radius value of its \(2\)-by-\(2\) corner, the quantitative scaling identities, and finite-dimensional numerical-radius sanity checks on a list of angles. Run `python VERIFY.py` using Python 3 and NumPy; the script prints the number of successful checks. These tests supplement, but do not replace, the matrix-compression and limit arguments above.

## Relationship to prior work

Mal, *Numerical radius norm and extreme contractions of* \(\mathcal L(H)\), arXiv:2210.09734v1 (18 October 2022), Theorems 2.7–2.9, gives the finite-dimensional two-coordinate extremality classification, while Theorem 2.11 excludes compact normal numerical-radius extreme contractions on infinite-dimensional Hilbert spaces. The direct extension of the two-coordinate criterion to diagonal operators is elementary; **the contribution here is the simultaneous full extremality and maximal failure of strong extremality in a noncompact infinite-dimensional unitary**, obtained from approximate but never exact antipodes. The earlier results do not state that instability conclusion.

Kadets, Martín, Merí, Pérez, and Quero, *On the numerical index with respect to an operator* (2019), Lemma 2.3, gives general definitions and criteria for strong extremality of norm-ball points, but does not analyze these diagonal numerical-radius unitaries. The exact-midpoint/approximate-midpoint separation in this result is not a corollary of the cited finite-dimensional classification without the explicit quantitative construction.

## Limitations

This result addresses complex numerical radius, not the usual operator norm and not arbitrary continuous-spectrum normal operators. The criterion for exact extremality of diagonal unitaries is an infinite-basis extension of the earlier finite-dimensional compression theorem; no independent priority is claimed for that elementary ingredient. The new claim concerns the *maximal* local approximate-midpoint diameter under approximate antipodality. It does not characterize strongly extreme diagonal unitaries whose spectra have a uniform antipodal separation, nor does it assert the same phenomenon in real Hilbert spaces. An unindexed equivalent theorem under convex-geometric terminology remains a bibliographic risk. No independent scientific validation has been performed.

## References

1. A. Mal, *Numerical radius norm and extreme contractions of* \(\mathcal L(H)\), arXiv:2210.09734v1, 18 October 2022, https://arxiv.org/abs/2210.09734 (Theorems 2.7–2.11 and Lemma 2.4).
2. V. Kadets, M. Martín, J. Merí, A. Pérez, A. Quero, *On the numerical index with respect to an operator*, arXiv:1905.12257v1, https://arxiv.org/abs/1905.12257 (Lemma 2.3, strongly extreme points).
