# A better largest Lanczos Ritz value can have an arbitrarily worse residual at condition number two

## Finding
Consider
\[
A_\varepsilon
=
\operatorname{diag}(1,1+\varepsilon,2),
\qquad
0<\varepsilon<1,
\]
and start exact symmetric Lanczos from
\[
v_\varepsilon
=
\frac{(1,1,\varepsilon)^{\mathsf T}}
{\sqrt{2+\varepsilon^2}}.
\]
Every matrix in the family is positive definite and has the fixed spectral condition number
\[
\kappa_2(A_\varepsilon)=2.
\]

At Krylov dimension one, the only Ritz value is the Rayleigh quotient
\[
\rho_\varepsilon
=
\frac{2\varepsilon^2+\varepsilon+2}
{\varepsilon^2+2},
\]
and the exact Ritz residual norm is
\[
\boxed{
\|r^{(1)}_\varepsilon\|_2
=
\frac{
\varepsilon\sqrt{\varepsilon^2-2\varepsilon+3}
}{
\varepsilon^2+2
}.
}
\]

At Krylov dimension two, let
\[
\theta_\varepsilon
=
\max_{\substack{z\in\mathcal K_2\\z\ne0}}
\frac{z^{\mathsf T}A_\varepsilon z}{z^{\mathsf T}z},
\qquad
\mathcal K_2
=
\operatorname{span}
\{v_\varepsilon,A_\varepsilon v_\varepsilon\},
\]
and let \(y_\varepsilon\) be the associated unit Ritz vector. Then
\[
\rho_\varepsilon<\theta_\varepsilon<2.
\]
Thus the largest Ritz value moves strictly toward the desired largest eigenvalue.

The residual diagnostic moves in the opposite direction. As
\[
\varepsilon\downarrow0,
\]
one has
\[
\theta_\varepsilon\longrightarrow\frac53,
\qquad
y_\varepsilon\longrightarrow
\frac{(-1,1,2)^{\mathsf T}}{\sqrt6},
\]
and hence
\[
\|A_\varepsilon y_\varepsilon-\theta_\varepsilon y_\varepsilon\|_2
\longrightarrow
\frac{\sqrt2}{3}.
\]
Since
\[
\frac{\|r^{(1)}_\varepsilon\|_2}{\varepsilon}
\longrightarrow
\frac{\sqrt3}{2},
\]
the exact asymptotic residual amplification law is
\[
\boxed{
\frac{
\|A_\varepsilon y_\varepsilon-\theta_\varepsilon y_\varepsilon\|_2
}{
\|r^{(1)}_\varepsilon\|_2
}
\sim
\frac{2\sqrt6}{9\varepsilon}.
}
\]
It is therefore unbounded even though the matrices remain uniformly well conditioned.

Meanwhile,
\[
\boxed{
\frac{2-\theta_\varepsilon}{2-\rho_\varepsilon}
\longrightarrow
\frac13.
}
\]
The same step that improves the largest-eigenvalue approximation by an asymptotic factor of three can make the associated Ritz residual arbitrarily worse relative to the previous one.

Dimension three is minimal. In dimension at most two, a nontrivial second Krylov step spans the whole space, so the second-step Ritz residual is zero.

## Assumptions and scope
The statement is in exact arithmetic and concerns the standard Hermitian Lanczos/Rayleigh--Ritz process for the largest eigenvalue.

The residual at each Krylov dimension is the Euclidean eigenpair residual
\[
A y-\theta y.
\]
The comparison is between the largest Ritz pair at dimensions one and two. At dimension one there is only one Ritz pair.

The family is deliberately diagonal and has fixed condition number two. This removes nonnormality and ill conditioning as explanations for the spike. The singular feature is instead near-breakdown of the first Lanczos recurrence caused by a nearly repeated low spectral cluster.

No claim is made that the second residual itself becomes unbounded in absolute value; it tends to \(\sqrt2/3\). The unbounded quantity is the ratio to a preceding residual that tends to zero.

Finite precision is outside the theorem. When \(\varepsilon\) is comparable with rounding scales, a practical Lanczos implementation may treat the small first subdiagonal as breakdown or near-breakdown.

## Proof
It is convenient to use the unnormalized starting vector
\[
u_\varepsilon=(1,1,\varepsilon)^{\mathsf T}.
\]
Its squared norm is
\[
u_\varepsilon^{\mathsf T}u_\varepsilon
=
2+\varepsilon^2.
\]
A direct calculation gives
\[
\rho_\varepsilon
=
\frac{
u_\varepsilon^{\mathsf T}A_\varepsilon u_\varepsilon
}{
u_\varepsilon^{\mathsf T}u_\varepsilon
}
=
\frac{2\varepsilon^2+\varepsilon+2}
{\varepsilon^2+2}.
\]
The normalized residual therefore satisfies
\[
\|r^{(1)}_\varepsilon\|_2^2
=
\frac{
\varepsilon^2(\varepsilon^2-2\varepsilon+3)
}{
(\varepsilon^2+2)^2
},
\]
which proves the first formula and
\[
\frac{\|r^{(1)}_\varepsilon\|_2}{\varepsilon}
\longrightarrow
\frac{\sqrt3}{2}.
\]

For the two-dimensional Krylov space, subtract a multiple of the first basis vector:
\[
\frac{
(A_\varepsilon-(1+\varepsilon)I)u_\varepsilon
}{
\varepsilon
}
=
w_\varepsilon
=
(-1,0,1-\varepsilon)^{\mathsf T}.
\]
Hence
\[
\mathcal K_2
=
\operatorname{span}\{u_\varepsilon,w_\varepsilon\}.
\]
The basis matrix
\[
V_\varepsilon=
\begin{pmatrix}
1&-1\\
1&0\\
\varepsilon&1-\varepsilon
\end{pmatrix}
\]
has Gram matrix
\[
G_\varepsilon
=
V_\varepsilon^{\mathsf T}V_\varepsilon
=
\begin{pmatrix}
\varepsilon^2+2&-\varepsilon^2+\varepsilon-1\\
-\varepsilon^2+\varepsilon-1&(1-\varepsilon)^2+1
\end{pmatrix},
\]
and projected quadratic form
\[
H_\varepsilon
=
V_\varepsilon^{\mathsf T}A_\varepsilon V_\varepsilon
=
\begin{pmatrix}
2\varepsilon^2+\varepsilon+2&
-2\varepsilon(\varepsilon-1)-1\\
-2\varepsilon(\varepsilon-1)-1&
2(1-\varepsilon)^2+1
\end{pmatrix}.
\]
The Ritz values are the generalized eigenvalues of
\[
H_\varepsilon c
=
\theta G_\varepsilon c.
\]
Their characteristic polynomial is
\[
\begin{aligned}
p_\varepsilon(\theta)
={}&
(\varepsilon^2-2\varepsilon+3)\theta^2\\
&+
(-\varepsilon^3-\varepsilon^2+4\varepsilon-8)\theta\\
&+
2\varepsilon^3-2\varepsilon^2-\varepsilon+5.
\end{aligned}
\]

As \(\varepsilon\downarrow0\),
\[
G_\varepsilon\longrightarrow
G_0=
\begin{pmatrix}
2&-1\\
-1&2
\end{pmatrix},
\qquad
H_\varepsilon\longrightarrow
H_0=
\begin{pmatrix}
2&-1\\
-1&3
\end{pmatrix}.
\]
The limiting generalized characteristic polynomial is
\[
\det(H_0-\theta G_0)
=
(\theta-1)(3\theta-5).
\]
The larger limiting Ritz value is therefore
\[
\frac53.
\]
It is simple. A corresponding generalized eigenvector is
\[
c_0=(1,2)^{\mathsf T},
\]
which reconstructs the physical vector
\[
V_0c_0=(-1,1,2)^{\mathsf T}.
\]
By continuity of a simple eigenpair of a real symmetric definite pencil,
\[
\theta_\varepsilon\longrightarrow\frac53,
\qquad
y_\varepsilon\longrightarrow
\frac{(-1,1,2)^{\mathsf T}}{\sqrt6}
\]
after fixing the harmless sign of \(y_\varepsilon\).

With
\[
A_0=\operatorname{diag}(1,1,2),
\qquad
y_0=\frac{(-1,1,2)^{\mathsf T}}{\sqrt6},
\]
one finds
\[
A_0y_0-\frac53y_0
=
\frac{(2,-2,2)^{\mathsf T}}{3\sqrt6},
\]
so
\[
\left\|
A_0y_0-\frac53y_0
\right\|_2
=
\frac{\sqrt2}{3}.
\]
Continuity gives the claimed second-residual limit.

Combining the two residual limits yields
\[
\varepsilon
\frac{
\|A_\varepsilon y_\varepsilon-\theta_\varepsilon y_\varepsilon\|_2
}{
\|r^{(1)}_\varepsilon\|_2
}
\longrightarrow
\frac{\sqrt2/3}{\sqrt3/2}
=
\frac{2\sqrt6}{9}.
\]

It remains to compare Ritz values. The largest Ritz value is the maximum Rayleigh quotient over
\[
\mathcal K_2.
\]
Since \(v_\varepsilon\in\mathcal K_2\),
\[
\theta_\varepsilon\ge\rho_\varepsilon.
\]
Equality would make \(v_\varepsilon\) a maximizing Ritz vector and force its residual to be orthogonal to all of \(\mathcal K_2\). But
\[
(r^{(1)}_\varepsilon)^{\mathsf T}
A_\varepsilon v_\varepsilon
=
\|r^{(1)}_\varepsilon\|_2^2
>0,
\]
so equality is impossible. Thus
\[
\theta_\varepsilon>\rho_\varepsilon.
\]
Also \(e_3\notin\mathcal K_2\) for \(0<\varepsilon<1\), so the maximum Ritz value is strictly below the simple top eigenvalue:
\[
\theta_\varepsilon<2.
\]
Therefore the largest-eigenvalue error strictly decreases. Taking limits gives
\[
\frac{2-\theta_\varepsilon}{2-\rho_\varepsilon}
\longrightarrow
\frac{2-5/3}{2-1}
=
\frac13.
\]

Finally, in dimension two, either
\[
\dim\mathcal K_2=1,
\]
in which case the first Ritz vector is already invariant and the residual is zero, or
\[
\dim\mathcal K_2=2,
\]
in which case Rayleigh--Ritz is performed on the full space and every Ritz residual is zero. This proves the minimal-dimension statement.

## Verification
The embedded `verify.py` uses exact rational arithmetic for the one-step Rayleigh quotient, first residual, Gram matrix, projected quadratic form, and generalized Ritz polynomial.

It verifies exactly that at
\[
\varepsilon=\frac1{10}
\]
the first squared residual is
\[
\frac{281}{40401}.
\]
The larger two-step Ritz value is the larger root of
\[
2810\theta^2-7611\theta+4882=0.
\]
High-precision arithmetic then reconstructs its generalized eigenvector and confirms a second residual near \(0.44990318\), versus a first residual near \(0.08339828\), an amplification above \(5.39\), while the largest-eigenvalue error decreases.

The checker separately verifies the limiting pencil
\[
(G_0,H_0)
\]
exactly, including its Ritz values \(1\) and \(5/3\), the physical limiting Ritz vector \((-1,1,2)^{\mathsf T}\), and limiting residual square \(2/9\).

Finite evaluations corroborate the formulas but are not used to prove the asymptotic or minimal-dimension statements.

## Relationship to prior work
Rayleigh--Ritz and Lanczos extraction are classical. Jia and Stewart give a full Rayleigh--Ritz formulation and emphasize that convergence of a Ritz value does not by itself force convergence of the associated Ritz vector; they use the Ritz residual as an additional convergence diagnostic and motivate refined Ritz vectors by residual minimization.

Paige and Panayotov give the exact Hermitian Lanczos relation
\[
AV_k
=
V_kT_k+\beta_{k+1}v_{k+1}e_k^{\mathsf T}
\]
as the theoretical starting point for their finite-precision analysis, and they discuss the standard Ritz-value, Ritz-vector, and residual machinery. Their paper is classified primarily under MSC \(65F15\).

Those sources motivate the question but do not state stepwise monotonicity of the largest-Ritz residual. The construction here shows a sharp qualitative failure of such intuition: on a \(3\times3\) SPD family with condition number fixed at two, nested Rayleigh--Ritz strictly improves the largest Ritz value while the residual ratio from dimensions one to two diverges.

A nearby published research result gives sharp Rayleigh-residual distortion for applying a prescribed spectral filter to a normal matrix. A Lanczos Ritz vector is indeed a Krylov polynomial applied to the start vector, but its polynomial is selected adaptively by the Rayleigh--Ritz optimization. That filtering result does not imply that the data-dependent largest Ritz extraction selects a filter producing the displayed near-breakdown asymptotic, nor does it give the dimension-three minimality or fixed-condition-number family.

Another nearby Lanczos result concerns whether a finite Ritz estimate can certify convexification in an optimization method. It monitors a Ritz value against a curvature threshold rather than the residual evolution of the extremal Ritz pair.

## Limitations
The theorem concerns a singularly perturbed three-dimensional family and the transition from Krylov dimension one to two. It does not claim that Ritz residuals are typically nonmonotone.

The residual spike is relative: the second residual stays bounded and tends to \(\sqrt2/3\), while the first residual vanishes.

The largest Ritz pair at dimension two is not a continuation of the nearby low-cluster eigenpair represented at dimension one. The point is precisely that extremal Ritz extraction can switch spectral emphasis as the Krylov space expands.

The construction is exact arithmetic. Practical implementations may detect the small first Lanczos subdiagonal and invoke a breakdown or near-breakdown policy.

Older Lanczos and Rayleigh--Ritz literature is extensive, and an equivalent small-dimensional near-breakdown example may exist under different terminology; this remains the principal originality risk.

## References
1. Zhongxiao Jia and G. W. Stewart, “On the Convergence of Ritz Values, Ritz Vectors, and Refined Ritz Vectors,” University of Maryland Institute for Advanced Computer Studies Technical Report UMIACS-TR-99-08 / CS-TR-3986, public repository date 1999-01-29.
2. Christopher C. Paige and Ivo Panayotov, “Hessenberg Matrix Properties and Ritz Vectors in the Finite-Precision Lanczos Tridiagonalization Process,” SIAM Journal on Matrix Analysis and Applications 32 (2011), 1079–1094. DOI 10.1137/100796285.
