# Three dimensions are minimal for transient sign loss in convergent Newton–Schulz inversion of Stieltjes matrices
## Finding
Let \(A=A^{\mathsf T}>0\) be a Stieltjes matrix, meaning that \(A\) is symmetric positive definite and every off-diagonal entry is nonpositive. Consider the Newton–Schulz inverse iteration
\[
X_{k+1}=X_k(2I-AX_k),\qquad X_0=\alpha I,
\]
with
\[
0<\alpha<\frac{2}{\lambda_{\max}(A)}.
\]
Then in dimensions one and two every iterate \(X_k\) is entrywise nonnegative. Dimension three is minimal for failure: the explicit matrix
\[
A=\begin{pmatrix}
1&-1/10&0\\
-1/10&8/5&-1/10\\
0&-1/10&8/5
\end{pmatrix}
\]
with \(\alpha=1\) satisfies the convergence condition and has \(A^{-1}>0\) entrywise, but its second Newton–Schulz update has
\[
(X_2)_{13}=(X_2)_{31}=-\frac1{500}<0.
\]
Hence convergence to an inverse-positive target does not force sign preservation of the intermediate approximate inverses, and the first possible dimension for this phenomenon is three.

## Assumptions and scope
The theorem concerns exact-arithmetic Newton–Schulz inversion with a scalar initialization \(X_0=\alpha I\), symmetric positive definite Stieltjes matrices, and the standard spectral convergence range \(0<\alpha<2/\lambda_{\max}(A)\). The conclusion is entrywise nonnegativity of every iterate for dimensions at most two and a sharp three-dimensional counterexample. It does not address nonsymmetric \(M\)-matrices, non-scalar initial approximations, dropping strategies, floating-point rounding, inverse square roots, or matrix-sign iterations.

## Proof
Because \(X_0\) commutes with \(A\), every iterate is a polynomial in \(A\). Put \(R_0=I-\alpha A\). The Newton–Schulz identity gives
\[
I-AX_{k+1}=(I-AX_k)^2,
\]
so
\[
I-AX_k=R_0^{2^k}
\]
and, for \(m=2^k\),
\[
X_k=q_m(A),\qquad
q_m(\lambda)=\frac{1-(1-\alpha\lambda)^m}{\lambda}
=\alpha\sum_{j=0}^{m-1}(1-\alpha\lambda)^j.
\]
The spectral hypothesis puts \(0<\alpha\lambda<2\) for every eigenvalue, hence \(q_m(\lambda)>0\). Therefore every \(X_k\) is positive definite.

For \(k\ge1\), \(m\) is even. Set \(x=\alpha\lambda\in(0,2)\), \(u=1-x\in(-1,1)\), and
\[
f_m(x)=\frac{1-(1-x)^m}{x}=1+u+\cdots+u^{m-1}.
\]
Differentiating with respect to \(u\),
\[
\frac{d}{du}\left(1+u+\cdots+u^{m-1}\right)
=
\frac{1-mu^{m-1}+(m-1)u^m}{(1-u)^2}.
\]
If \(-1<u<0\), the numerator is strictly positive because \(m\) is even. If \(0\le u<1\), its derivative is
\[
m(m-1)u^{m-2}(u-1)\le0
\]
and the numerator decreases to zero at \(u=1\); it is therefore again strictly positive for \(u<1\). Thus \(f_m\) is strictly increasing in \(u\) and strictly decreasing in \(x\), so \(q_m(\lambda)\) is strictly decreasing on \((0,2/\alpha)\).

Now let \(n=2\). If \(A\) has distinct eigenvalues \(\lambda_1<\lambda_2\), functional calculus in dimension two gives
\[
q_m(A)=c_0I+c_1A,
\qquad
c_1=\frac{q_m(\lambda_2)-q_m(\lambda_1)}{\lambda_2-\lambda_1}<0.
\]
Since the off-diagonal entry of a Stieltjes matrix is nonpositive, the off-diagonal entry of \(q_m(A)\) is nonnegative. Its diagonal entries are positive because \(q_m(A)\) is positive definite. If the eigenvalues coincide, symmetry forces \(A\) to be a scalar multiple of the identity, and the conclusion is immediate. The case \(n=1\) is trivial. Together with \(X_0=\alpha I\ge0\), this proves entrywise nonnegativity of every iterate for \(n\le2\).

For sharpness, take
\[
A=\begin{pmatrix}
1&-1/10&0\\
-1/10&8/5&-1/10\\
0&-1/10&8/5
\end{pmatrix},\qquad \alpha=1.
\]
Its leading principal minors are
\[
1,\qquad \frac{159}{100},\qquad \frac{1267}{500},
\]
so \(A>0\). The leading principal minors of \(2I-A\) are
\[
1,\qquad \frac{39}{100},\qquad \frac{73}{500},
\]
so \(2I-A>0\). Therefore every eigenvalue of \(A\) lies strictly between \(0\) and \(2\), equivalently \(\rho(I-A)<1\), and Newton–Schulz converges quadratically. Direct exact arithmetic gives
\[
A^{-1}=\frac1{1267}
\begin{pmatrix}
1275&80&5\\
80&800&50\\
5&50&795
\end{pmatrix}>0,
\]
\[
X_1=2I-A=\begin{pmatrix}
1&1/10&0\\
1/10&2/5&1/10\\
0&1/10&2/5
\end{pmatrix}\ge0,
\]
and
\[
X_2=X_1(2I-AX_1)=
\begin{pmatrix}
251/250&39/500&-1/500\\
39/500&267/500&9/100\\
-1/500&9/100&67/125
\end{pmatrix}.
\]
Thus entrywise nonnegativity fails in dimension three. All inequalities used for positive definiteness and convergence are strict, and the negative entry is strict, so the phenomenon persists under sufficiently small symmetric Stieltjes perturbations of this witness.

## Verification
The bundled `verify.py` uses exact rational arithmetic. It checks the leading principal minors of \(A\) and \(2I-A\), verifies the displayed inverse by exact multiplication, forms \(X_1\) and \(X_2\) from the Newton–Schulz recurrence, verifies the residual-squaring identity through the second update, and checks \((X_2)_{13}=-1/500\). The two-dimensional part is analytic and is not inferred from finite enumeration.

## Relationship to prior work
Newton–Schulz inversion and its residual-squaring convergence mechanism are classical. Hackbusch, Khoromskij, and Tyrtyshnikov study iterative computation of matrix inverses and explicitly emphasize that intermediate matrices can lose computational structures such as hierarchical or tensor structure; their 2005 preprint and 2008 paper classify this work primarily under MSC 65F30. Soleymani, Sharifi, and Shateyi present Schulz-type inverse iterations, explicitly discuss the scalar initialization \(V_0=\alpha I\) under a contraction condition, and motivate approximate inverses as preconditioners for large sparse systems. Those ingredients are prior work.

The present statement concerns a different structure: entrywise nonnegativity for inverse-positive Stieltjes matrices. Searches for Newton–Schulz together with \(M\)-matrix, Stieltjes, nonnegative-iterate, inverse-positive, and dimension-minimality terminology did not locate the dimension-two preservation theorem or the three-dimensional convergent counterexample. A related literature on Schulz iterations for matrix square roots of \(M\)-matrices addresses a different matrix function and does not imply the inverse-iteration claim here.

## Limitations
The proof does not claim that three dimensions are minimal for nonsymmetric \(M\)-matrices, for arbitrary starting matrices, or for other hyperpower inverse iterations. It also does not quantify how long a negative entry can persist before convergence makes all entries close to the positive inverse. Published-index search cannot establish absolute novelty; older matrix-monotonicity literature using different terminology remains a residual risk.

## References
1. W. Hackbusch, B. N. Khoromskij, and E. E. Tyrtyshnikov, *Approximate Iterations for Structured Matrices*, MPI MIS Preprint 112/2005, publicly posted 2005-11-30; later *Numerische Mathematik* 109 (2008), 365–383, DOI 10.1007/s00211-008-0143-0.
2. F. Soleymani, M. Sharifi, and S. Shateyi, *Approximating the Inverse of a Square Matrix with Application in Computation of the Moore–Penrose Inverse*, Journal of Applied Mathematics (2014), Article 731562, DOI 10.1155/2014/731562.
3. G. Schulz, *Iterative Berechung der reziproken Matrix*, ZAMM 13 (1933), 57–59.
