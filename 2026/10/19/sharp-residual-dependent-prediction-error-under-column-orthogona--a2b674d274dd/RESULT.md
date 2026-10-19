# Sharp residual-dependent prediction error under column-orthogonal least-squares perturbations

## Finding
Let \(A\in\mathbb R^{m\times n}\) have full column rank, with \(m>n\ge1\), and let \(x_*=A^\dagger b\ne0\) be the unique least-squares solution for \(b\in\mathbb R^m\). Put \(r=b-Ax_*\), \(\rho=\|r\|_2/\|Ax_*\|_2\), and fix a nonnegative perturbation budget \(\delta\). For the class of data-matrix errors
\[
\mathcal E_\delta=\{E\in\mathbb R^{m\times n}:A^\mathsf T E=0,\ \|EA^\dagger\|_2\le\delta\},
\]
define the relative prediction-energy displacement by
\[
\mathcal D(E)=\frac{\|A((A+E)^\dagger b-x_*)\|_2}{\|Ax_*\|_2}.
\]
Its **exact, attained** worst-case envelope is
\[
\boxed{\max_{E\in\mathcal E_\delta}\mathcal D(E)=\frac{s^2+\rho s}{1+s^2},\quad
s=\begin{cases}\delta,&\rho=0,\\\min\{\delta,(1+\sqrt{1+\rho^2})/\rho\},&\rho>0.\end{cases}}
\]
A rank-one perturbation attains equality for every admissible data set and every finite budget. For nonzero residual the envelope **saturates** at
\[
\delta_* =\frac{1+\sqrt{1+\rho^2}}{\rho},\qquad
\max_E\mathcal D(E)=\frac{1+\sqrt{1+\rho^2}}{2}\quad(\delta\ge\delta_*).
\]
For a consistent least-squares system (\(r=0\)), the sharp envelope is \(\delta^2/(1+\delta^2)\), so first-order sensitivity to these structured errors vanishes.

## Assumptions and scope
All matrices and vectors are real and all norms are Euclidean/operator 2-norms. The strict inequality \(m>n\) ensures at least one direction orthogonal to the original column space; \(x_*\ne0\) makes the normalization meaningful. The perturbation condition \(A^\mathsf T E=0\) means every column of \(E\) lies in the orthogonal complement of the *original* column space. The budget \(\|EA^\dagger\|_2\) is a right-invariant, dimensionless relative matrix perturbation; a bound merely on \(\|E\|_2/\|A\|_2\) is a different problem. The prediction displacement is measured using the original matrix \(A\), not \(A+E\), and the right-hand side \(b\) is fixed.

The perturbed matrix always has full column rank, regardless of the size of \(\delta\), because \((A+E)^\mathsf T(A+E)=A^\mathsf TA+E^\mathsf TE\) is positive definite. Therefore the pseudoinverse and maximand are well defined for every admissible \(E\).

## Proof
**1. Reduction to a graph perturbation.** Take a thin QR factorization \(A=QR\), where \(Q^\mathsf TQ=I_n\) and \(R\) is invertible. Write \(u=Rx_*\), so \(\|u\|_2=\|Ax_*\|_2>0\), and \(b=Qu+r\) with \(Q^\mathsf T r=0\). Let \(F=ER^{-1}\). Then \(Q^\mathsf T F=0\), \(E=FR\), and, because \(EA^\dagger=FQ^\mathsf T\),
\[
\|EA^\dagger\|_2=\|F\|_2.
\]
If \(\hat u=R(A+E)^\dagger b\), the normal equations for \(Q+F\) give
\[
(I+F^\mathsf T F)\hat u=u+F^\mathsf Tr.
\]
With \(S=F^\mathsf T F\) and \(T=S(I+S)^{-1}\), the displacement is
\[
\hat u-u=-Tu+(I+S)^{-1}F^\mathsf Tr. \tag{1}
\]
Here \(T\) is positive semidefinite and
\[
0\preceq T\preceq cI,\qquad c=\frac{\delta^2}{1+\delta^2}<1. \tag{2}
\]
The norm in (1) equals \(\|A((A+E)^\dagger b-x_*)\|_2\).

**2. A dimension-free upper bound.** Set \(K=(I+S)^{-1}F^\mathsf T\). The identity
\[
KK^\mathsf T=(I+S)^{-1}S(I+S)^{-1}=T-T^2 \tag{3}
\]
follows by commuting functions of \(S\). For any unit vector \(z\in\mathbb R^n\), the scalar dual pairing of (1), Cauchy–Schwarz, and (3) yield
\[
\langle z,\hat u-u\rangle
\le\|u\|_2\sqrt{z^\mathsf T T^2z}
+\|r\|_2\sqrt{z^\mathsf T(T-T^2)z}.
\]
Let \(a=\sqrt{z^\mathsf T T^2z}\). Since the spectrum of \(T\) lies in \([0,c]\), \(0\le a\le c\). Cauchy–Schwarz also implies \(z^\mathsf T Tz\le a\); thus
\[
0\le z^\mathsf T(T-T^2)z=z^\mathsf T Tz-a^2\le a-a^2.
\]
Taking the supremum over unit \(z\) (the Euclidean dual-norm formula) gives the *exactly one-dimensional upper envelope*
\[
\frac{\|\hat u-u\|_2}{\|u\|_2}
\le\max_{0\le a\le c}\bigl(a+\rho\sqrt{a(1-a)}\bigr). \tag{4}
\]

**3. Scalar optimization and finite saturation.** If \(\rho=0\), the right side of (4) is \(c\). If \(\rho>0\), the function \(g(a)=a+\rho\sqrt{a(1-a)}\) is strictly concave in the open interval \((0,1)\). Its unique maximum on \([0,1]\) occurs at
\[
a_*=\tfrac12\Bigl(1+\frac1{\sqrt{1+\rho^2}}\Bigr),
\quad g(a_*)=\tfrac12\bigl(1+\sqrt{1+\rho^2}\bigr).
\]
The budget cap \(c=\delta^2/(1+\delta^2)\) reaches \(a_*\) exactly at
\[
\delta=\sqrt{\frac{a_*}{1-a_*}}=
\frac{1+\sqrt{1+\rho^2}}\rho=\delta_*.
\]
Consequently (4) is \(g(c)=(\delta^2+\rho\delta)/(1+\delta^2)\) when \(\delta\le\delta_*\), and \(g(a_*)\) otherwise. In the zero-residual case \(g(c)=c\) for all \(\delta\).

**4. Equality in every dimension.** Let \(v=u/\|u\|_2\). Choose a unit vector \(w\) orthogonal to the columns of \(Q\), aligned with \(r\) when \(r\ne0\), and arbitrary otherwise. Put \(s=\delta\) if \(r=0\), or \(s=\min\{\delta,\delta_*\}\) otherwise, and take the rank-one perturbation
\[
F=-s\,wv^\mathsf T,\qquad E=FR.
\]
It satisfies \(Q^\mathsf T F=0\) and \(\|EA^\dagger\|_2=\|F\|_2=s\le\delta\). Substituting in (1) shows
\[
\hat u-u=-\frac{s^2\|u\|_2+s\|r\|_2}{1+s^2}\,v,
\]
so its relative norm is exactly \((s^2+\rho s)/(1+s^2)\). This attains the upper bound, proves all quantifiers, and establishes the claimed saturation and consistent-data cases.

## Verification
The algebraic proof is complete; finite checks are supporting evidence, not a substitute for the inequality. The standalone standard-library script `checks/verify.py` tests 48 rank-one extremizers spanning zero and nonzero residual, perturbation budgets below and beyond saturation, plus 1,200 randomly generated feasible graph perturbations for dimensions up to five. Its recorded output was `PASS: 48 sharp rank-one cases; 1200 randomized feasible matrices`. Separately, a higher-dimensional numerical implementation checked 120 extremizer cases and 1,200 random perturbations for rectangular matrices with original condition numbers up to one million. The latter numerical experiment is not needed for reproduction of the proof.

## Relationship to prior work
Garrison and Ipsen, *Perturbation Analysis for Preconditioned Normal Equations in Mixed Precision* (arXiv:2603.16644v1, first public March 17, 2026), emphasize the dependence of least-squares perturbation sensitivity on the residual. Their Theorems 4 and 6 analyze preconditioned normal/half-normal equations and provide forward-error upper bounds normalized by computed coefficients. Ipsen, *Solution of Least Squares Problems with Randomized Preconditioned Normal Equations* (arXiv:2507.18466, particularly Appendix A), derives residual-sensitive upper bounds for general perturbations. Neither examined source states an exact uniform sharp envelope for the column-orthogonal class with the relative multiplicative budget above, fixed original prediction norm, rank-one attainment for every input, and finite-budget saturation.

Classical work by Stewart on pseudoinverses and projections and by Castro-González, Dopico, and Molera on multiplicative perturbations covers significantly broader perturbation models, but a general perturbation inequality does not directly imply an equality or an optimal structured threshold. A related geometric viewpoint appears in Ding's work on projecting onto linear manifolds. The detailed comparison with the latter older sources remains limited by incomplete access to their full texts; no assertion is made that an unavailable appendix fails to cover a related formulation.

## Limitations
This is a theorem about *structured*, column-orthogonal data-matrix perturbations and the original prediction norm. It does not give a sharp bound for arbitrary \(E\), simultaneous perturbations of \(b\), a Euclidean-coefficient error when \(A\) is ill-conditioned, or backward error for a numerical algorithm. The curvature of the envelope is not a performance claim for a particular random sketch or floating-point implementation. Some classical full texts were inaccessible and are an unresolved prior-art risk; independent validation has not occurred.

## References
1. J. E. Garrison and I. C. F. Ipsen, *Perturbation Analysis for Preconditioned Normal Equations in Mixed Precision*, arXiv:2603.16644v1 (2026-03-17), https://arxiv.org/html/2603.16644v1.
2. I. C. F. Ipsen, *Solution of Least Squares Problems with Randomized Preconditioned Normal Equations*, arXiv:2507.18466, https://arxiv.org/html/2507.18466v2.
3. N. Castro-González, F. M. Dopico, and J. M. Molera, *Multiplicative perturbation theory of the Moore–Penrose inverse and the least squares problem*, Linear Algebra Appl. 503 (2016), 1–25, https://doi.org/10.1016/j.laa.2016.03.027.
4. G. W. Stewart, *On the perturbation of pseudo-inverses, projections and linear least squares problems*, SIAM Rev. 19 (1977), 634–662, https://doi.org/10.1137/1019104.
5. J. Ding, *Perturbation results for projecting a point onto a linear manifold*, SIAM J. Matrix Anal. Appl. 19 (1998), 696–700, https://doi.org/10.1137/S0895479896306604.
