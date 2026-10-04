# Critical-damping relaxation for scalar strictly contractive Peaceman–Rachford splitting
## Finding
Consider
\[
\min_{x,y\in\mathbb R}\frac a2x^2+\frac b2y^2
\quad\text{subject to}\quad x-y=0,
\]
with \(a,b>0\). Apply strictly contractive Peaceman–Rachford splitting with penalty \(\beta>0\) and the same relaxation \(\alpha\in(0,1)\) in both multiplier updates. If
\[
\min\{a,b\}<\beta<\max\{a,b\},
\]
then the exact asymptotic spectral radius of the two-dimensional state recurrence has a unique minimizer \(\alpha_*\in(0,1)\). Define
\[
Q=(a+\beta)(b+\beta),\qquad
u=\frac{\beta}{\sqrt Q},\qquad
w=\frac{\beta(a+b+\beta)}{Q}.
\]
Then
\[
\alpha_*=\frac{w+u-\sqrt{(w+u)^2-u^2(1+u)^2}}{u^2},
\qquad
\rho_*=u(1-\alpha_*).
\]
At \(\alpha_*\), the two eigenvalues coalesce at the negative repeated root
\[
\lambda_*=-u(1-\alpha_*).
\]
Thus the rate-optimal strict underrelaxation is exactly the critical-damping point. It is strictly faster asymptotically than the endpoint \(\alpha=1\) whenever \(\beta\) lies strictly between the two curvatures.

## Assumptions and scope
The objective is exactly the scalar two-block strongly convex quadratic above, with equality coupling \(x-y=0\). The penalty is positive and lies strictly between the two positive curvatures. The algorithm uses one common relaxation factor \(\alpha\in(0,1)\) in the two multiplier updates, exactly as in the strictly contractive Peaceman–Rachford scheme introduced by He, Liu, Wang, and Yuan. The state used for the rate calculation is \(v^k=(y^k,\lambda^k)^T\). The unique saddle point is \((x,y,\lambda)=(0,0,0)\).

No assertion is made here about penalties outside the open interval between the two curvatures, about unequal relaxation factors, or about nonquadratic objectives. At the boundary \(\beta=a\) or \(\beta=b\), the interior minimizer moves to the endpoint \(\alpha=1\), so the strict-interior statement intentionally excludes those cases.

## Proof
The scalar first-order conditions give the exact iteration
\[
x^{k+1}=\frac{\lambda^k+\beta y^k}{a+\beta},
\]
\[
\lambda^{k+1/2}=\lambda^k-\alpha\beta(x^{k+1}-y^k),
\]
\[
y^{k+1}=\frac{\beta x^{k+1}-\lambda^{k+1/2}}{b+\beta},
\]
\[
\lambda^{k+1}=\lambda^{k+1/2}-\alpha\beta(x^{k+1}-y^{k+1}).
\]
Hence \(v^{k+1}=M_\alpha v^k\) for a real \(2\times2\) matrix. Direct elimination gives
\[
\det M_\alpha=\frac{\beta^2(1-\alpha)^2}{(a+\beta)(b+\beta)}=u^2(1-\alpha)^2
\]
and
\[
\operatorname{tr}M_\alpha
=u^2\alpha^2-2w\alpha+(1+u^2)=:T(\alpha).
\]
Thus the characteristic polynomial is
\[
p_\alpha(z)=z^2-T(\alpha)z+u^2(1-\alpha)^2.
\]
Because
\[
T(1)=\frac{(\beta-a)(\beta-b)}{(a+\beta)(b+\beta)}<0,
\]
while \(T(0)+2u=(1+u)^2>0\), the function
\[
F(\alpha)=T(\alpha)+2u(1-\alpha)
\]
has a root in \((0,1)\). Moreover
\[
F'(\alpha)=2u^2\alpha-2w-2u<0
\]
throughout \([0,1]\), since \(w-u^2=\beta(a+b)/Q>0\). Therefore the root is unique. Solving \(F(\alpha_*)=0\) gives the stated closed form for \(\alpha_*\). At that point
\[
T(\alpha_*)=-2u(1-\alpha_*),
\]
so the discriminant vanishes and both roots equal \(-u(1-\alpha_*)\).

It remains to prove global optimality, not merely stationarity. For every \(\alpha\), the product of the two eigenvalues is \(u^2(1-\alpha)^2\), hence
\[
\rho(M_\alpha)\ge u(1-\alpha).
\]
For \(\alpha<\alpha_*\), this lower bound is strictly larger than \(u(1-\alpha_*)=\rho_*\). For \(\alpha>\alpha_*\), strict decrease of \(T\) gives
\[
T(\alpha)<T(\alpha_*)=-2\rho_*.
\]
For any two complex numbers with sum \(T(\alpha)\), the larger modulus is at least \(|T(\alpha)|/2\); therefore
\[
\rho(M_\alpha)\ge\frac{|T(\alpha)|}{2}>\rho_*.
\]
This proves uniqueness of the minimizer over \((0,1)\). The same formulas at \(\alpha=1\) give eigenvalues \(0\) and \(T(1)\), so the endpoint is also strictly slower.

## Verification
The accompanying `verify.py` independently reconstructs the scalar update matrix from the four update equations, checks the determinant and trace identities over a grid of positive rational parameters, and checks the critical-damping formula numerically for several penalty-between-curvatures examples. It also verifies the concrete instance
\[
a=1,\qquad b=4,\qquad \beta=2,
\]
for which
\[
\alpha_*=0.9462158829301036\ldots,
\qquad
\rho_*=0.0253540759335033\ldots,
\]
whereas the endpoint \(\alpha=1\) has spectral radius \(1/9\). The script is supplementary to the algebraic proof; finite numerical checks are not used as a proof of the quantified theorem.

## Relationship to prior work
He, Liu, Wang, and Yuan introduced the strictly contractive Peaceman–Rachford scheme by shrinking both multiplier updates with a common relaxation factor. Their paper proves global convergence and worst-case iteration-complexity statements and reports that values close to one, particularly roughly \(0.8\) to \(0.9\), worked well empirically on their tests. The paper does not state the scalar quadratic spectral-radius minimizer above.

He, Ma, and Yuan subsequently studied larger admissible step-size regions for the symmetric version of ADMM, emphasizing convergence domains rather than this problem-dependent scalar critical-damping formula. General Douglas–Rachford rate work, including Giselsson's tight global bounds, optimizes related reflected-resolvent iterations under operator regularity assumptions, but it does not imply the two-multiplier-update scalar formula proved here. Later strictly contractive Peaceman–Rachford variants add proximal terms or unequal relaxation factors; those broader algorithm families likewise do not, from the material inspected, provide this exact common-relaxation result.

## Limitations
The theorem is deliberately one-dimensional and exact. It is a calibration result, not a general parameter-selection theorem for arbitrary matrices. The penalty-between-curvatures assumption is essential to the stated interior critical-damping formula. Detailed full-text comparison with every later symmetric-ADMM variant was not possible; a later paper, thesis, or implementation note could conceivably contain an equivalent scalar calculation under different notation. No independent audit has been performed.

## References
1. B. He, H. Liu, Z. Wang, and X. Yuan, “A Strictly Contractive Peaceman–Rachford Splitting Method for Convex Programming,” *SIAM Journal on Optimization* 24(3), 1011–1040, 2014. DOI: 10.1137/13090849X.
2. B. He, F. Ma, and X. Yuan, “Convergence Study on the Symmetric Version of ADMM with Larger Step Sizes,” *SIAM Journal on Imaging Sciences* 9(3), 1467–1501, 2016. DOI: 10.1137/15M1044448.
3. P. Giselsson, “Tight Global Linear Convergence Rate Bounds for Douglas–Rachford Splitting,” arXiv:1506.01556, 2015.
4. Z.-F. Jin, Z. Wan, and Z. Zhang, “Strictly contractive Peaceman–Rachford splitting method to recover the corrupted low rank matrix,” *Journal of Inequalities and Applications* 2019:147. DOI: 10.1186/s13660-019-2091-x.
