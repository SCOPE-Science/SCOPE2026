# Sharp first-cycle component envelope for BiCGSTAB on positive diagonal systems

## Finding
Let
\[
A=\operatorname{diag}(\lambda_1,\ldots,\lambda_n),
\qquad
0<\mu\le \lambda_i\le L,
\]
and let \(b\ge0\). Apply unpreconditioned BiCGSTAB in exact arithmetic to
\[
Ax=b
\]
from \(x_0=0\), with the standard shadow residual \(\widehat r_0=r_0=b\).

Assume the first BiCG half-step does not already terminate exactly. Define
\[
m=\frac{\sum_i b_i^2\lambda_i}{\sum_i b_i^2},
\qquad
n=\frac{\sum_i b_i^2\lambda_i^2(\lambda_i-m)^2}
{\sum_i b_i^2\lambda_i(\lambda_i-m)^2}.
\]
Then
\[
\alpha_1=\frac1m,
\qquad
\omega_1=\frac1n,
\]
and the first completed BiCGSTAB iterate has the exact coordinate formula
\[
x_{1,i}=\frac{m+n-\lambda_i}{mn}\,b_i.
\]
Since the exact solution is \(x_i^\star=b_i/\lambda_i\), every active coordinate obeys
\[
\frac{x_{1,i}}{x_i^\star}
=
\frac{\lambda_i(m+n-\lambda_i)}{mn}.
\]

Writing
\[
\kappa=\frac L\mu,
\]
the sharp dimension-free envelope is
\[
\boxed{
\kappa(2-\kappa)
\le
\frac{x_{1,i}}{x_i^\star}
\le
\frac{(\kappa+1)^2}{4\kappa}
}.
\]
Both constants are sharp as an infimum and supremum over positive diagonal systems and positive right-hand sides.

The lower envelope immediately yields the exact positivity frontier:
\[
\boxed{
\text{all first completed BiCGSTAB iterates are componentwise nonnegative}
\iff
\kappa\le2.
}
\]
In contrast, if there are at most two active eigenvalues, the first completed BiCGSTAB iterate is componentwise positive for every condition number. Thus three active eigenvalues are minimal for first-cycle sign loss.

## Assumptions and scope
The matrix is diagonal positive definite in the coordinate system in which componentwise sign is tested. The start is \(x_0=0\), the shadow residual is chosen as \(\widehat r_0=r_0=b\), and arithmetic is exact.

Coordinates with \(b_i=0\) are inactive and can be omitted. If all active eigenvalues coincide, the first BiCG half-step solves the system exactly and the completed stabilization step is unnecessary; the theorem concerns the nontrivial case in which the intermediate residual is nonzero.

The result describes one completed BiCGSTAB cycle. It does not classify later cycles, preconditioned variants, alternative shadow residuals, finite-precision breakdown, or nondiagonal matrices.

## Proof
Set
\[
r_0=b,
\qquad
p_1=r_0.
\]
The first BiCGSTAB coefficient is
\[
\alpha_1
=
\frac{(r_0,r_0)}{(r_0,Ar_0)}
=
\frac1m,
\]
where
\[
m=\frac{\sum_i b_i^2\lambda_i}{\sum_i b_i^2}.
\]
The intermediate residual is
\[
s_i
=
(1-\alpha_1\lambda_i)b_i
=
\frac{m-\lambda_i}{m}b_i.
\]
Let \(t=As\). The stabilizing coefficient is chosen by residual minimization:
\[
\omega_1
=
\frac{(t,s)}{(t,t)}.
\]
Substituting the diagonal formulas gives
\[
\omega_1
=
\frac{\sum_i b_i^2\lambda_i(\lambda_i-m)^2}
{\sum_i b_i^2\lambda_i^2(\lambda_i-m)^2}
=
\frac1n,
\]
where
\[
n=\frac{\sum_i b_i^2\lambda_i^2(\lambda_i-m)^2}
{\sum_i b_i^2\lambda_i(\lambda_i-m)^2}.
\]
Both \(m\) and \(n\) are weighted means of active eigenvalues, hence
\[
\mu\le m,n\le L.
\]
The first completed iterate is
\[
x_1
=
\alpha_1 b+\omega_1s.
\]
Therefore
\[
x_{1,i}
=
\left(\frac1m+\frac1n-\frac{\lambda_i}{mn}\right)b_i
=
\frac{m+n-\lambda_i}{mn}b_i,
\]
and
\[
\eta_i
:=
\frac{x_{1,i}}{x_i^\star}
=
\frac{\lambda_i(m+n-\lambda_i)}{mn}.
\]

To prove the upper bound, complete the square:
\[
\eta_i
=
\frac{(m+n)^2}{4mn}
-
\frac{\left(\lambda_i-(m+n)/2\right)^2}{mn}
\le
\frac{(m+n)^2}{4mn}.
\]
The last expression is maximized on \([\mu,L]^2\) when the ratio of \(m\) and \(n\) is \(\kappa\), giving the Kantorovich factor
\[
\eta_i
\le
\frac{(\kappa+1)^2}{4\kappa}.
\]

For the lower bound, for fixed \(m,n\) the expression \(\lambda(m+n-\lambda)/(mn)\) is concave in \(\lambda\). Hence its minimum on \([\mu,L]\) is at an endpoint. Scale by \(\mu\), so \(m,n,\lambda\in[1,\kappa]\).

At \(\lambda=\kappa\), the quantity increases with both \(m\) and \(n\), so its minimum is at \(m=n=1\):
\[
\eta\ge \kappa(2-\kappa).
\]
At \(\lambda=1\), the quantity decreases with both \(m\) and \(n\), so its minimum is
\[
\frac{2\kappa-1}{\kappa^2}.
\]
The difference from the claimed lower constant is
\[
\frac{2\kappa-1}{\kappa^2}-\kappa(2-\kappa)
=
\frac{(\kappa-1)^3(\kappa+1)}{\kappa^2}
\ge0.
\]
Thus
\[
\eta_i\ge\kappa(2-\kappa).
\]

Both constants are sharp. For the lower envelope, scale \(\mu=1\) and use three active eigenvalues
\[
1,
\qquad
1+\delta,
\qquad
\kappa,
\]
with a fixed positive split between the first two weights and a positive high-mode weight that tends to zero faster than \(\delta^2\). Then \(m,n\to1\) while the high mode remains active, so
\[
\eta_{\mathrm{high}}\to\kappa(2-\kappa).
\]
For the upper envelope, use eigenvalues
\[
1,
\qquad
\frac{1+\kappa}{2},
\qquad
\kappa,
\]
with high-mode squared weight \(\varepsilon\), midpoint squared weight \(\varepsilon^2\), and the remaining weight at \(1\). Then
\[
m\to1,
\qquad
n\to\kappa,
\]
and the active midpoint coordinate tends to
\[
\frac{(\kappa+1)^2}{4\kappa}.
\]

The positivity frontier follows because the sharp lower constant is nonnegative exactly when \(\kappa\le2\). For every \(\kappa>2\), the lower-envelope construction gives an actual negative high-mode coordinate for sufficiently small positive parameters.

It remains to establish the two-mode exception. Let the two active eigenvalues be \(a<c\), with squared-residual weights \(p\) and \(q=1-p\). Then
\[
m=pa+qc.
\]
A direct substitution into the definition of \(n\) yields
\[
n
=
\frac{qa^2+pc^2}{qa+pc}.
\]
Consequently
\[
m+n-c
=
a+\frac{pq(c-a)^2}{qa+pc}>0.
\]
The high-mode coordinate is therefore positive, and the low-mode coordinate is automatically positive because \(m+n>a\). Dimension one terminates exactly, so three active eigenvalues are minimal for a first-cycle sign failure.

## Verification
The embedded `verify.py` uses exact rational arithmetic.

For
\[
A=\operatorname{diag}(1,2,4),
\qquad
b=(1,1/2,1/11)^{\mathsf T},
\]
it reconstructs
\[
\alpha_1=\frac{87}{106},
\qquad
\omega_1=\frac{4609}{12729},
\]
and verifies
\[
(x_1)_3=-\frac{7955}{14842014}<0.
\]
It also checks the closed coordinate formula against the algorithm, verifies the exact two-mode positivity identity on rational instances, and tests the component envelope on a deterministic family of rational spectra and right-hand sides.

Those finite checks replay algebraic consequences and witnesses. The universal bounds and sharpness statements are proved analytically above.

## Relationship to prior work
Van der Vorst introduced BiCGSTAB as a smoother-converging product-type Krylov method. The original paper derives the residual factorization
\[
r_i=Q_i(A)P_i(A)r_0,
\]
chooses each scalar stabilizing factor to minimize the current residual norm, and gives the unpreconditioned algorithm used here. It emphasizes residual smoothness, finite termination, and numerical behavior, including symmetric positive-definite test problems, but it does not state a componentwise sign theorem or a condition-number envelope for the first completed iterate.

Gutknecht's early variants and the later induced-dimension-reduction interpretation analyze polynomial structure and generalizations of BiCGSTAB. Those frameworks explain the method's residual-polynomial architecture but do not imply the coordinate formula above, because the new statement uses positivity of a diagonal spectral measure and tracks a single solution coordinate rather than only residual norms or polynomial degree.

Targeted searches for BiCGSTAB together with positive orthants, nonnegative iterates, M-matrices, componentwise monotonicity, two-eigenvalue safety, and first-cycle sign changes did not locate an implication-equivalent theorem.

## Limitations
The theorem is deliberately first-cycle and diagonal. Later BiCGSTAB cycles depend on the evolving Bi-CG recurrence and are not covered by the two weighted means \(m,n\) used here.

The standard choice \(\widehat r_0=r_0\) is part of the statement. Different shadow residuals can change the first Bi-CG coefficient and therefore the sign geometry.

The sharp constants are dimension-free infimum and supremum constants. The lower and upper sharpness constructions approach their endpoints; they need not attain them at finite positive spectral weights.

Nondiagonal positive-definite systems, nonsymmetric M-matrices, preconditioning, finite precision, and breakdown handling are outside scope.

Residual originality risk remains that older Krylov or orthogonal-polynomial literature may encode the same first-cycle component formula under a different parametrization. The full original BiCGSTAB paper inspected for this review contains the algorithmic ingredients but not this componentwise envelope.

## References
1. H. A. van der Vorst, “Bi-CGSTAB: A Fast and Smoothly Converging Variant of Bi-CG for the Solution of Nonsymmetric Linear Systems,” SIAM Journal on Scientific and Statistical Computing 13 (1992), 631–644, DOI 10.1137/0913035. The journal issue is dated 1992-03-01 and lists AMS classification 65F10.
2. M. H. Gutknecht, “Variants of BICGSTAB for Matrices with Complex Spectrum,” SIAM Journal on Scientific Computing 14 (1993), 1020–1033, DOI 10.1137/0914062.
3. G. L. G. Sleijpen, P. Sonneveld, and M. B. van Gijzen, “Bi-CGSTAB as an induced dimension reduction method,” Applied Numerical Mathematics 60 (2010), 1100–1114.
