# Additive bidirectional Gauss-Seidel inverse: exact SPD threshold and quadratic weak-coupling clustering

**Same-model review: passed. Independent audit: not yet performed.**

## Summary

Let a real symmetric positive-definite block matrix be split as
\[
A=D+L+L^T,
\]
where \(D\succ0\) is block diagonal and \(L\) is strictly block lower triangular. Define the forward and backward Gauss-Seidel inverse actions
\[
R_f=(D+L)^{-1},\qquad R_b=(D+L^T)^{-1},
\]
and the diagonal-corrected additive inverse
\[
B:=R_f+R_b-D^{-1}.
\]
Unlike standard symmetric Gauss-Seidel, the two triangular solves in \(B r\) use the same input residual and are independent of one another. The diagonal correction cancels every first-order term in the off-diagonal coupling, but it can also destroy positive definiteness.

Writing
\[
C=D^{-1/2}LD^{-1/2},\qquad H=D^{-1/2}AD^{-1/2}=I+C+C^T,
\]
the following hold.

1. **Exact factorization and exact SPD threshold.**
   \[
   B=(D+L^T)^{-1}\bigl(D-L^TD^{-1}L\bigr)(D+L)^{-1},
   \]
   hence
   \[
   B\succ0\quad\Longleftrightarrow\quad I-C^TC\succ0
   \quad\Longleftrightarrow\quad \|C\|_2<1.
   \]
   Thus \(A\succ0\) alone does not guarantee that this additive inverse is CG-safe.

2. **One-sided spectral location when the threshold holds.** If \(\delta:=\|C\|_2<1\), then
   \[
   0\prec B\preceq A^{-1},
   \]
   and every eigenvalue of \(BA\) lies in \((0,1]\).

3. **Quadratic weak-coupling accuracy.** If \(\delta<1\),
   \[
   \|I-D^{1/2}BD^{1/2}H\|_2
   \le \frac{2\delta^2}{1-\delta}.
   \]
   In particular, if \(\delta<1/2\),
   \[
   \kappa\!\left(B^{1/2}AB^{1/2}\right)
   \le \frac{1-\delta}{1-\delta-2\delta^2}
   =1+2\delta^2+O(\delta^3).
   \]
   By comparison, the elementary Jacobi bound from \(H=I+C+C^T\) is
   \[
   \kappa(H)\le\frac{1+2\delta}{1-2\delta}
   =1+4\delta+O(\delta^2)
   \qquad(\delta<1/2).
   \]
   This comparison is only a worst-case weak-coupling bound; it does not assert that the additive inverse always outperforms Jacobi or symmetric Gauss-Seidel in practice.

4. **Uniqueness of the first-order cancellation within a natural affine family.** For the scaled family \(A(t)=D+t(L+L^T)\), among symmetric affine combinations
   \[
   a\bigl((D+tL)^{-1}+(D+tL^T)^{-1}\bigr)+bD^{-1}
   \]
   with constant \(a,b\), matching \(A(t)^{-1}\) through first order for nonzero coupling forces \(a=1\) and \(b=-1\).

5. **Exact two-block spectrum.** For
   \[
   H=\begin{bmatrix}I&K^T\\K&I\end{bmatrix},
   \]
   the method is SPD exactly when \(H\) is SPD, namely \(\|K\|_2<1\), and
   \[
   (D^{1/2}BD^{1/2})H
   =\operatorname{diag}(I-K^TK,\ I-KK^T).
   \]
   Thus each nonzero singular value \(\sigma_j(K)\) contributes the eigenvalue \(1-\sigma_j(K)^2\) twice, with additional unit eigenvalues from null directions. If \(K=cQ\) with square orthogonal \(Q\), the preconditioned matrix is exactly \((1-c^2)I\).

## Computational model

The matrix is finite-dimensional, real and SPD. The split is a fixed block ordering with an SPD block diagonal \(D\). Applying \(B\) to a residual requires one solve with \(D+L\), one solve with \(D+L^T\), and one block-diagonal solve; the two triangular solves depend only on the same residual and therefore have no data dependence on each other. No claim is made about hardware speedup, communication cost, or floating-point stability.

## Proof

Set
\[
M=D+L,\qquad X=(I+C)^{-1},\qquad \widetilde B=D^{1/2}BD^{1/2}.
\]
Then \(D^{1/2}R_fD^{1/2}=X\) and \(D^{1/2}R_bD^{1/2}=X^T\), so
\[
\widetilde B=X+X^T-I.
\]

### Exact factorization

Multiplying the unscaled \(B\) on the left by \(M^T\) and on the right by \(M\) gives
\[
\begin{aligned}
M^TBM
&=M^T+M-M^TD^{-1}M\\
&=D-L^TD^{-1}L.
\end{aligned}
\]
Therefore
\[
B=M^{-T}(D-L^TD^{-1}L)M^{-1}.
\]
Equivalently,
\[
\widetilde B=X^T(I-C^TC)X.
\]
Congruence by invertible matrices preserves inertia, so
\[
B\succ0\iff I-C^TC\succ0\iff\|C\|_2<1.
\]
At \(\|C\|_2=1\), \(B\) is singular; above it, \(B\) is indefinite.

### Inverse dominance and spectrum

Assume \(\delta=\|C\|_2<1\). From the factorization,
\[
\widetilde B^{-1}=(I+C)(I-C^TC)^{-1}(I+C^T).
\]
Let
\[
R=C^TC(I-C^TC)^{-1}\succeq0,
\]
so \((I-C^TC)^{-1}=I+R\). Since
\[
(I+C)(I+C^T)=H+CC^T,
\]
we obtain
\[
\widetilde B^{-1}-H
=CC^T+(I+C)R(I+C^T)\succeq0.
\]
Hence \(\widetilde B\preceq H^{-1}\), equivalently \(B\preceq A^{-1}\). The symmetric matrix \(H^{1/2}\widetilde B H^{1/2}\) is therefore SPD and bounded above by \(I\), and it is similar to \(\widetilde B H\), which in turn has the same eigenvalues as \(BA\). Thus
\[
0<\lambda(BA)\le1.
\]

### Quadratic error identity

Using \(X(I+C)=I\) and \(X^T(I+C^T)=I\),
\[
XH=I+XC^T,\qquad X^TH=I+X^TC.
\]
Consequently,
\[
\begin{aligned}
\widetilde B H-I
&=(X+X^T-I)H-I\\
&=-XCC^T-X^TC^TC.
\end{aligned}
\]
Because \(\|X\|_2\le(1-\delta)^{-1}\),
\[
\|I-\widetilde B H\|_2
\le \frac{2\delta^2}{1-\delta}=:q.
\]
The eigenvalues of \(\widetilde B H\) are real and in \((0,1]\). Hence every eigenvalue satisfies \(1-q\le\lambda\le1\). If \(q<1\), equivalently \(\delta<1/2\), this yields
\[
\kappa(B^{1/2}AB^{1/2})
\le\frac1{1-q}
=\frac{1-\delta}{1-\delta-2\delta^2}.
\]

For the scaled coupling \(tC\), the identity also shows directly that the preconditioned error is \(O(t^2)\), with leading term
\[
-t^2(CC^T+C^TC).
\]

### Uniqueness in the symmetric affine family

With \(C\) replaced by \(tC\),
\[
(I+tC)^{-1}=I-tC+O(t^2),
\]
so the normalized affine family expands as
\[
a\bigl((I+tC)^{-1}+(I+tC^T)^{-1}\bigr)+bI
=(2a+b)I-at(C+C^T)+O(t^2).
\]
Meanwhile
\[
(I+t(C+C^T))^{-1}=I-t(C+C^T)+O(t^2).
\]
Matching the constant and first-order coefficients gives \(a=1\), \(b=-1\).

### Relation to standard symmetric Gauss-Seidel

The standard SGS inverse is
\[
B_{\rm SGS}=(D+L^T)^{-1}D(D+L)^{-1},
\]
whose normalized form is \(X^TX\). Therefore
\[
B_{\rm SGS}-B
=(D+L^T)^{-1}L^TD^{-1}L(D+L)^{-1}\succeq0.
\]
Standard SGS remains SPD whenever \(D\succ0\), while the diagonal-corrected additive inverse requires \(\|C\|_2<1\). The structural distinction is multiplicative versus additive: in SGS, the backward correction uses the result of the forward sweep, whereas the two triangular actions in \(B\) can be formed independently from the same residual.

### Exact SPD counterexample

Take \(D=I\) and
\[
C=\begin{bmatrix}
0&0&0\\[2pt]
4/5&0&0\\[2pt]
-3/5&-3/5&0
\end{bmatrix}.
\]
Then
\[
H=I+C+C^T=
\begin{bmatrix}
1&4/5&-3/5\\
4/5&1&-3/5\\
-3/5&-3/5&1
\end{bmatrix}.
\]
Its leading principal minors are
\[
1,\qquad \frac9{25},\qquad \frac{27}{125},
\]
so \(H\succ0\) by Sylvester's criterion. However,
\[
C^TC=
\begin{bmatrix}
1&9/25&0\\
9/25&9/25&0\\
0&0&0
\end{bmatrix}
\]
has largest eigenvalue
\[
\frac{17+\sqrt{145}}{25}>1.
\]
Thus \(\|C\|_2>1\) and \(B\) is indefinite. Explicitly,
\[
\widetilde B=
\begin{bmatrix}
1&-4/5&3/25\\
-4/5&1&3/5\\
3/25&3/5&1
\end{bmatrix},
\qquad
\det\widetilde B=-\frac{81}{625}<0.
\]
This proves that SPD of \(A\) does not by itself certify the additive construction.

### Two-block corollary

For
\[
H=\begin{bmatrix}I&K^T\\K&I\end{bmatrix},
\qquad
C=\begin{bmatrix}0&0\\K&0\end{bmatrix},
\]
we have \(C^2=0\), hence \(X=I-C\) and
\[
\widetilde B=I-C-C^T.
\]
Direct multiplication yields
\[
\widetilde BH=
\begin{bmatrix}
I-K^TK&0\\0&I-KK^T
\end{bmatrix}.
\]
The Schur complement gives \(H\succ0\iff\|K\|_2<1\), exactly the same condition as \(\widetilde B\succ0\). The spectral statement follows from the singular values of \(K\).

## Reproducibility

`artifacts/verify_abgs.py` numerically checks the factorization, the exact error identity, inverse dominance, spectral location, the norm bound, the SGS ordering relation, the explicit SPD/indefinite counterexample, and the two-block product identity. `artifacts/verification.txt` records its deterministic output.

## Literature context and originality boundary

Classical Gauss-Seidel, backward Gauss-Seidel, SOR/SSOR, symmetric forward-backward sweeps, extrapolated Gauss-Seidel methods, and general additive/multiplicative matrix-splitting frameworks are well established. Koliha (1972) studied accelerated/extrapolated stationary methods for self-adjoint operator equations; Evans, Li and Xue (1987) studied extrapolated Gauss-Seidel variants; Evans and Li (1988) studied a symmetric extrapolated iterative method; Bai (2003) developed a general algebraic theory of additive and multiplicative splitting iterations; modern reviews document classical GS/SSOR preconditioners; and recent work continues to study highly parallel additive and multiplicative smoothers.

Targeted searches did not locate the specific diagonal-corrected inverse
\[
(D+L)^{-1}+(D+L^T)^{-1}-D^{-1}
\]
together with the congruence factorization above, the exact \(\|C\|_2<1\) SPD threshold, an SPD-\(A\)/indefinite-\(B\) counterexample, and the quadratic weak-coupling conditioning bound. The claim is therefore only **to the best of our knowledge**. The full texts of Evans--Li--Xue (1987), Evans--Li (1988), and Bai (2003) were not inspected end-to-end and are the most plausible historical coverage risks. For Saye (2026), only the abstract-level description of additive versus multiplicative cascading smoothers was inspected. No novelty is claimed for generic additive splitting, extrapolation, polynomial preconditioning, or the idea of combining forward and backward sweeps.

## Limitations

- The theory is finite-dimensional and assumes a real SPD matrix with a fixed SPD block diagonal split.
- The additive inverse is SPD only under the exact certificate \(\|D^{-1/2}LD^{-1/2}\|_2<1\); SPD of \(A\) alone is insufficient.
- The condition-number estimate is a worst-case weak-coupling bound and is informative in the stated form only for \(\delta<1/2\).
- No theorem is given for floating-point stability, sparse-triangular-solve scalability, communication cost, or performance.
- No claim is made that this construction generally beats standard SGS/SSOR, incomplete factorizations, multigrid, or other modern preconditioners.
- Estimating the spectral-norm certificate itself may carry nontrivial cost.
- The literature-access limitations described above leave residual originality risk.

## References

1. J. J. Koliha, “On the iterative solution of linear operator equations with self-adjoint operators,” *J. Austral. Math. Soc.* 13 (1972), 241–255. https://doi.org/10.1017/S1446788700011320
2. D. J. Evans, C. Li, Y. Xue, “The extrapolated Gauss-Seidel methods and generally consistently ordered matrices,” *Int. J. Comput. Math.* 23 (1987), 77–97. https://doi.org/10.1080/00207168708803609
3. D. J. Evans, C. Li, “Analysis of a symmetric extrapolated iterative method for solving linear systems,” *Linear Algebra Appl.* 103 (1988), 149–173. https://doi.org/10.1016/0024-3795(88)90226-1
4. Z.-Z. Bai, “On the convergence of additive and multiplicative splitting iterations for systems of linear equations,” *J. Comput. Appl. Math.* 154 (2003), 195–214. https://doi.org/10.1016/S0377-0427(02)00822-1
5. M. Ferronato, “Preconditioning for Sparse Linear Systems at the Dawn of the 21st Century: History, Current Developments, and Future Perspectives,” *ISRN Applied Mathematics* (2012), Article 127647. https://doi.org/10.5402/2012/127647
6. J. W. Pearson, J. Pestana, “Preconditioners for Krylov subspace methods: An overview,” *GAMM-Mitteilungen* 43 (2020), e202000015. https://doi.org/10.1002/gamm.202000015
7. R. I. Saye, “Cascading Smoothers for Multigrid,” arXiv:2606.12577 (2026). https://arxiv.org/abs/2606.12577
