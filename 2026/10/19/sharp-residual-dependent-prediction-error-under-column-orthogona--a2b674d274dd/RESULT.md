# Sharp residual-dependent prediction error under column-orthogonal least-squares perturbations

## Finding
Let \(A\in\mathbb R^{m\times n}\) have full column rank, with \(m>n\ge1\), and let \(x_*=A^\dagger b\ne0\) be the unique least-squares solution for \(b\in\mathbb R^m\). Put \(r=b-Ax_*\), \(\rho=\|r\|_2/\|Ax_*\|_2\), and fix a nonnegative finite perturbation budget \(\delta\). For the class of data-matrix errors
\[
\mathcal E_\delta=\{E\in\mathbb R^{m\times n}:A^\mathsf T E=0,\ \|EA^\dagger\|_2\le\delta\},
\]
define the relative prediction displacement by
\[
\mathcal D(E)=\frac{\|A((A+E)^\dagger b-x_*)\|_2}{\|Ax_*\|_2}.
\]
Its exact, attained worst-case envelope is
\[
\boxed{\max_{E\in\mathcal E_\delta}\mathcal D(E)=\frac{s^2+\rho s}{1+s^2},\quad
s=\begin{cases}\delta,&\rho=0,\\\min\{\delta,(1+\sqrt{1+\rho^2})/\rho\},&\rho>0.\end{cases}}
\]
For every \(\delta>0\), a rank-one perturbation attains equality for every admissible data set. For \(\delta=0\), the only admissible perturbation is \(E=0\), attaining the value zero. For nonzero residual the envelope saturates at
\[
\delta_* =\frac{1+\sqrt{1+\rho^2}}{\rho},\qquad
\max_E\mathcal D(E)=\frac{1+\sqrt{1+\rho^2}}{2}\quad(\delta\ge\delta_*).
\]
For a consistent least-squares system (\(r=0\)), the sharp envelope is \(\delta^2/(1+\delta^2)\), so first-order sensitivity to these structured errors vanishes.

## Assumptions and scope
All matrices and vectors are real and all norms are Euclidean/operator 2-norms. The strict inequality \(m>n\) ensures at least one direction orthogonal to the original column space; \(x_*\ne0\) makes the normalization meaningful. The perturbation condition \(A^\mathsf T E=0\) means every column of \(E\) lies in the orthogonal complement of the original column space. The budget \(\|EA^\dagger\|_2\) is a right-invariant, dimensionless relative matrix perturbation; a bound merely on \(\|E\|_2/\|A\|_2\) is a different problem. The prediction displacement is measured using the original matrix \(A\), not \(A+E\), and the right-hand side \(b\) is fixed.

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
Taking the supremum over unit \(z\) gives
\[
\frac{\|\hat u-u\|_2}{\|u\|_2}
\le\max_{0\le a\le c}\bigl(a+\rho\sqrt{a(1-a)}\bigr). \tag{4}
\]

**3. Scalar optimization and finite saturation.** If \(\rho=0\), the right side of (4) is \(c\). If \(\rho>0\), the function \(g(a)=a+\rho\sqrt{a(1-a)}\) is strictly concave on \((0,1)\), and its unique maximum on \([0,1]\) occurs at
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

**4. Equality in every dimension.** Let \(v=u/\|u\|_2\). Choose a unit vector \(w\) orthogonal to the columns of \(Q\), aligned with \(r\) when \(r\ne0\), and arbitrary otherwise. For the value of \(s\) in the finding, take
\[
F=-s\,wv^\mathsf T,\qquad E=FR.
\]
It satisfies \(Q^\mathsf T F=0\) and \(\|EA^\dagger\|_2=\|F\|_2=s\le\delta\). It has rank one if \(\delta>0\), since then \(s>0\), \(v,w\) are unit vectors, and \(R\) is invertible. If \(\delta=0\), (2)'s underlying budget \(\|F\|_2\le\delta\) forces \(F=0\), and hence \(E=0\). Substituting into (1) gives
\[
\hat u-u=-\frac{s^2\|u\|_2+s\|r\|_2}{1+s^2}\,v,
\]
so the relative norm matches the upper envelope, including the zero-budget case.

## Verification
An exact scalar replay is \(A=(1,0)^\mathsf T\), \(b=(1,\rho)^\mathsf T\), \(E=(0,-s)^\mathsf T\). Then \((A+E)^\dagger b=(1-\rho s)/(1+s^2)\), the prediction displacement is \((s^2+\rho s)/(1+s^2)\), and \(E\) has rank zero for \(s=0\) and rank one for \(s>0\). The full proof gives both the all-dimensional upper bound and its attainment. The companion numerical script `checks/verify.py` exercises 48 scalar extremizer examples (42 rank-one and six zero-budget cases) and 1,200 randomly generated feasible graph perturbations. These finite cases are stress tests, not a proof of the infinite class.

## Relationship to prior work
Garrison and Ipsen, *Perturbation Analysis for Preconditioned Normal Equations in Mixed Precision* (arXiv:2603.16644v1), Theorems 4 and 6, analyze preconditioned normal/half-normal equations and provide forward-error upper bounds normalized by computed coefficients. Ipsen, *Solution of Least Squares Problems with Randomized Preconditioned Normal Equations* (arXiv:2507.18466, Appendix A), derives residual-sensitive upper bounds for general perturbations. Those results use different hypotheses and error normalizations; they do not state this exact, attained envelope for fixed data, column-orthogonal perturbations, the multiplicative budget, and displacement measured in the original prediction norm.

Classical work by Stewart on pseudoinverses and projections and by Castro-González, Dopico, and Molera on multiplicative perturbations covers broader perturbation models. A related geometric viewpoint appears in Ding's work on projecting onto linear manifolds. Detailed comparison with those older sources remains limited by incomplete full-text access; an equivalent consequence in those sources has not been ruled out.

## Limitations
The theorem is about structured, column-orthogonal data-matrix perturbations and the original prediction norm. It does not give a sharp bound for arbitrary \(E\), simultaneous perturbations of \(b\), a Euclidean-coefficient error when \(A\) is ill-conditioned, or backward error for a numerical algorithm. The curvature of the envelope is not a performance claim for a particular random sketch or floating-point implementation.

## References
1. J. E. Garrison and I. C. F. Ipsen, *Perturbation Analysis for Preconditioned Normal Equations in Mixed Precision*, arXiv:2603.16644v1, https://arxiv.org/html/2603.16644v1.
2. I. C. F. Ipsen, *Solution of Least Squares Problems with Randomized Preconditioned Normal Equations*, arXiv:2507.18466v2, https://arxiv.org/html/2507.18466v2.
3. N. Castro-González, F. M. Dopico, and J. M. Molera, *Multiplicative perturbation theory of the Moore–Penrose inverse and the least squares problem*, Linear Algebra Appl. 503 (2016), 1–25, https://doi.org/10.1016/j.laa.2016.03.027.
4. G. W. Stewart, *On the perturbation of pseudo-inverses, projections and linear least squares problems*, SIAM Rev. 19 (1977), 634–662, https://doi.org/10.1137/1019104.
5. J. Ding, *Perturbation results for projecting a point onto a linear manifold*, SIAM J. Matrix Anal. Appl. 19 (1998), 696–700, https://doi.org/10.1137/S0895479896306604.
