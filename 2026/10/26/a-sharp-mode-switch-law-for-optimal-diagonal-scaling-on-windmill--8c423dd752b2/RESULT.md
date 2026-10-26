# A sharp mode-switch law for optimal diagonal scaling on windmill matrices

## Finding

Let \(k\ge2\) be an integer. Index a real symmetric matrix \(A=A(k,s,t)\) by a hub \(0\) and \(k\) disjoint leaf pairs \(\{a_j,b_j\}\). Define its entries by \(A_{vv}=1\), \(A_{a_j,b_j}=A_{b_j,a_j}=s\), \(A_{0,a_j}=A_{a_j,0}=A_{0,b_j}=A_{b_j,0}=t\), and zero at all other off-diagonal positions. Its sparsity graph is the friendship (windmill) graph formed by \(k\) triangles sharing one hub.

Assume
\[
k\ge2,\qquad 0<s<1,\qquad 0<t,\qquad 2kt^2<1+s.
\]
Then \(A\) is positive definite. Among **all** positive diagonal matrices \(D\), without a symmetry restriction, the optimal spectral condition number
\[
\kappa_*(A)=\min_{D\text{ positive diagonal}}\frac{\lambda_{\max}(DAD)}{\lambda_{\min}(DAD)}
\]
is attained by \(D_* =\operatorname{diag}(\sqrt{q_*},1,\ldots,1)\), possibly multiplied by any positive scalar. Put \(\theta=kt^2\), \(a=1+s\), and \(\theta_c=2s^2/(1+s)\). Then
\[
q_* =\begin{cases}
\dfrac{s(1-s)}{s-\theta},&0<\theta\le\theta_c,\\[5pt]
1+s,&\theta_c\le\theta<(1+s)/2,
\end{cases}
\]
and
\[
\boxed{\displaystyle
\kappa_*(A)=\begin{cases}
\dfrac{2s+s(1-s)/(s-\theta)}{1-s},&0<\theta\le\theta_c,\\[7pt]
\dfrac{1+\sqrt{2\theta/(1+s)}}{1-\sqrt{2\theta/(1+s)}},&\theta_c\le\theta<(1+s)/2.
\end{cases}}
\]
The two formulas coincide at \(\theta=\theta_c\). This \(q_*\) is the unique optimal hub-to-leaf squared scaling ratio within the automorphism-invariant diagonal class. **Jacobi's identity scaling is globally optimal if and only if \(kt^2=s^2\).**

## Assumptions and scope

The spectral condition number is the ratio of largest to smallest eigenvalue of a real symmetric positive-definite matrix. A positive diagonal scaling acts by congruence, not by similarity. The diagonal of \(A\) is already normalized to one; therefore \(D=I\) is the ordinary Jacobi scaling. Every leaf belongs to exactly one pair, and the only nonzero off-diagonal entries are the paired-leaf links of weight \(s\) and hub-leaf links of weight \(t\). No claims are made at \(s=0\), \(t=0\), or the singular boundary \(2kt^2=1+s\).

## Proof

**1. Positive definiteness and spectral reduction.** In each leaf pair, the antisymmetric vector has eigenvalue \(1-s\). The pair-symmetric vectors orthogonal to the sum of all pair-symmetric vectors give eigenvalue \(1+s\), with multiplicity \(k-1\). The remaining hub/leaf-sum block of \(A\) is
\[
\begin{pmatrix}1&\sqrt{2k}\,t\\ \sqrt{2k}\,t&1+s\end{pmatrix}.
\]
Thus \(A\succ0\) exactly when \(s<1\) and \(2kt^2<1+s\), under the stated positivity assumptions.

**2. Why an asymmetric diagonal cannot beat a symmetric one.** Let \(D\succ0\) be any positive diagonal matrix, and let \(\alpha>0\), \(\beta>0\) be the smallest and largest eigenvalues of \(DAD\). With \(W=\alpha D^{-2}\), congruence gives
\[
W\preceq A\preceq (\beta/\alpha)W.
\]
The automorphism group permutes the \(k\) pairs and swaps the two leaves within each pair. Conjugating both inequalities by each corresponding permutation matrix and averaging gives a positive diagonal \(\overline W\), constant on all leaves, satisfying the **same** inequalities. The associated symmetric diagonal scaling \(\overline W^{-1/2}\) therefore has condition number at most \(\beta/\alpha\). Consequently a globally optimal diagonal scaling can be sought among scalings with one hub value and a common leaf value. A common positive factor does not alter the condition number, so write this class as \(D(q)=\operatorname{diag}(\sqrt q,1,\ldots,1)\), \(q>0\). This argument proves global optimality of a symmetric candidate; it does not assume that every optimizer is symmetric.

**3. The three relevant eigenvalue levels.** For \(D(q)AD(q)\), the eigenvalues outside the hub/leaf-sum block remain \(\nu=1-s\) (multiplicity \(k\)) and \(a=1+s\) (multiplicity \(k-1\)). The remaining two are
\[
\lambda_{\pm}(q)=\frac{q+a\pm\sqrt{(q-a)^2+8\theta q}}{2}.
\]
Since \(0<2\theta<a\), both are positive. The strict inequalities \(\lambda_+(q)>a>\nu\) hold for all \(q>0\). Since \(\lambda_-(q)<a\), the complete condition number is exactly
\[
K(q)=\frac{\lambda_+(q)}{\min\{\lambda_-(q),\nu\}}.
\]
The larger eigenvalue \(\lambda_+(q)\) is strictly increasing in \(q\): differentiating its quadratic characteristic equation yields
\[
\lambda_+'(q)=\frac{\lambda_+(q)-(a-2\theta)}{\lambda_+(q)-\lambda_-(q)}>0.
\]
Evaluating the quadratic characteristic polynomial at \(a-2\theta\) gives \(-2\theta(a-2\theta)<0\), so \(0<\lambda_-(q)<a-2\theta<\lambda_+(q)\). The same differentiation identity now shows \(\lambda_-\) strictly increases from zero toward \(a-2\theta\), because its numerator and denominator are both negative. The condition number of the two-by-two block alone, \(\lambda_+/\lambda_-\), has a **unique** minimum at \(q=a\): the squared eigenvalue-sum divided by their product is
\[
\frac{(a+q)^2}{q(a-2\theta)},
\]
which is strictly decreasing for \(q<a\) and increasing for \(q>a\), by the arithmetic-geometric mean inequality (or differentiation). The ratio \(\lambda_+/\lambda_-\) has the same ordering as this expression.

**4. The active-mode switch.** The equation \(\lambda_-(q)=\nu\) is equivalent to
\[
2s\bigl(q-(1-s)\bigr)=2\theta q.
\]
When \(\theta<s\), it has the positive solution \(q_0=s(1-s)/(s-\theta)\); otherwise the two eigenvalue levels never cross. Moreover
\[
q_0\le a\quad\Longleftrightarrow\quad\theta\le\theta_c=\frac{2s^2}{1+s}.
\]
Notice \(\theta_c<s\) for \(0<s<1\). If \(\theta\le\theta_c\), the block condition number decreases up to \(q_0\) (where \(\lambda_-\le\nu\)), whereas beyond \(q_0\) the full condition number becomes \(\lambda_+(q)/\nu\), which strictly increases. Therefore the unique invariant minimizer is \(q_*=q_0\). At that point the upper block eigenvalue equals \(a+q_0-\nu=2s+q_0\), proving the first formula.

If \(\theta\ge\theta_c\), one has \(\lambda_-(a)\le\nu\). For \(q\le a\) the block condition number decreases toward \(a\) on the part where it controls the denominator; for \(q>a\), the block condition number increases until any crossing, after which \(\lambda_+(q)/\nu\) increases. Thus \(q_*=a\) is the unique invariant minimizer. Its block eigenvalues are \(a\pm\sqrt{2a\theta}\), proving the second formula. At equality, \(q_0=a\), so both branches match. Unrestricted optimality follows from Step 2.

**5. Jacobi's exact optimality locus.** Because the diagonal of \(A\) is one, Jacobi scaling corresponds to \(q=1\). The invariant minimizer is unique. The strong-coupling branch has \(q_*=1+s>1\), while in the weak-coupling branch \(q_*=1\) is equivalent to \(\theta=s^2\). This value lies strictly below \(\theta_c\) for \(0<s<1\). Since a symmetric optimum exists, Jacobi is globally optimal exactly on the stated curve.

## Verification

Run `python verify_windmill.py` with Python 3, NumPy, SymPy, and SciPy. The code checks the mode decomposition by exact characteristic-polynomial identities for five rational instances, symbolic transition identities, 75 full-matrix spectral identities, 75 independent one-variable minimizations, and 6,000 asymmetric random scaling comparisons. The program prints PASS summaries for each test category. The finite checks corroborate formulas but do not prove the general statement or exhaust asymmetric scalings; Step 2 is the unrestricted optimality proof.

For a concrete rational example, \(k=2\), \(s=1/2\), \(t=1/10\) give \(q_*=25/48\) and \(\kappa_*=73/24\), whereas unscaled Jacobi has strictly larger condition number \(5/2+\sqrt{41}/10\).

## Relationship to prior work

Vandebril, Golub, and Van Barel (dated 6 January 2005) explain why unit-diagonal scaling is optimal on symmetric positive-definite matrices with property A, including tridiagonal matrices and corresponding semiseparable inverses. The friendship sparsity graph contains triangles and is not property A, so this does not imply the claimed formula; indeed the sharp Jacobi-optimality locus generally fails away from \(kt^2=s^2\). Braatz and Morari (1994) give convex optimization procedures for general Euclidean condition-number scaling; this general method encompasses the optimization **problem** but does not state the explicit two-regime windmill solution. Gao, Qu, Udell, and Ye (2023) give general SDP and subspace schemes for diagonal preconditioning; their accessible treatment also does not state this family-level phase boundary. Shapiro (1985) and Kolotilina (2002) present broader optimal-scaling characterizations, but complete relevant comparisons were not possible from accessible text; these remain residual originality risks rather than proven exclusions.

## Limitations

The result concerns spectral condition numbers under positive diagonal **congruences** of this precisely specified two-parameter positive-definite family, not arbitrary preconditioners, different matrix norms, indefinite matrices, nonlinear solvers, or all matrices having friendship-graph sparsity. It establishes existence and uniqueness of an invariant optimum ratio, but does not classify every possible asymmetric optimizer. The literature comparison may miss specialized older equivalent formulas. Independent validation has not been performed.

## References

1. R. Vandebril, G. H. Golub, M. Van Barel, *A small note on the scaling of symmetric positive definite semiseparable matrices* (public full-text HTML dated 2005-01-06), https://people.cs.kuleuven.be/~raf.vandebril/homepage/publications/papers_html/condss/ ; journal DOI: 10.1007/s11075-006-9014-x.
2. R. D. Braatz and M. Morari, *Minimizing the Euclidean Condition Number*, SIAM Journal on Control and Optimization 32 (1994), 1763–1768, https://web.mit.edu/braatzgroup/Minimizing_the_Euclidean_condition_number.pdf .
3. W. Gao, Z. Qu, M. Udell, Y. Ye, *Scalable Approximate Optimal Diagonal Preconditioning* (arXiv:2312.15594, 2023), https://arxiv.org/html/2312.15594v1 .
4. A. Shapiro, *Optimal Block Diagonal l2-Scaling of Matrices*, SIAM Journal on Numerical Analysis 22 (1985), 81–94, DOI: 10.1137/0722005 (abstract inspected; full text not accessed).
5. L. Yu. Kolotilina, *Optimally conditioned block matrices*, Linear Algebra and its Applications 340 (2002), 55–67, DOI: 10.1016/S0024-3795(01)00412-8 (abstract inspected; full text not accessed).
