# Sharp large-parameter second Hankel law for Mocanu-convex functions

## Finding
Let \(\mathbb D\) be the open unit disk. For every real \(\alpha>0\), let \(\mathcal M_\alpha\) consist of normalized holomorphic functions \(f(z)=z+a_2z^2+a_3z^3+a_4z^4+\cdots\) satisfying
\[
\operatorname{Re}\left[(1-\alpha)\frac{zf'(z)}{f(z)}+\alpha\left(1+\frac{zf''(z)}{f'(z)}\right)\right]>0 \quad(z\in\mathbb D).
\]
Define the sharp second-Hankel constant
\[
H(\alpha)=\sup_{f\in\mathcal M_\alpha}|a_2a_4-a_3^2|.
\]
Then the following **sharp asymptotic** holds:
\[
\boxed{H(\alpha)=\frac{2}{7\alpha^2}+O(\alpha^{-3})\quad(\alpha\to+\infty).}
\]
An auxiliary exact moment theorem is established: if \(p(z)=1+2\sum_{k\ge1}c_kz^k\) has positive real part in \(\mathbb D\), then
\[
\boxed{|16c_1c_3-9c_2^2|\le\frac{72}{7},}
\]
with equality precisely at rotations of the symmetric two-point Herglotz measure with equal masses at \(e^{\pm i\theta_0}\), where \(\cos\theta_0=\sqrt{3/14}\). The moment extremizers produce an explicit admissible family establishing the lower asymptotic bound. This statement **does not** assert a sharp formula for finite \(\alpha\).

## Assumptions and scope
All parameters \(\alpha\) are positive real numbers, tending to infinity in the asymptotic statement. The supremum is taken over the *full* Mocanu \(\alpha\)-convex class, not a finite-parameter family of test functions. Normalization is \(f(0)=0\), \(f'(0)=1\). The second Hankel determinant is \(a_2a_4-a_3^2\), without an absolute value inside the determinant. The error \(O(\alpha^{-3})\) has an absolute constant independent of the function and is asserted only for sufficiently large \(\alpha\).

For the moment theorem, \(p(0)=1\) and \(\operatorname{Re}p(z)>0\). By the Herglotz representation, \(c_k=\int_{|\zeta|=1}\zeta^k\,d\mu(\zeta)\) for a probability measure \(\mu\). Equality may occur for boundary (two-atomic) measures because their Herglotz functions still have strictly positive real part on \(\mathbb D\).

## Proof
**Step 1: uniform coefficient reduction.** Write \(w(z)=zf'(z)/f(z)=1+w_1z+w_2z^2+w_3z^3+\cdots\). Since
\[
1+\frac{zf''(z)}{f'(z)}=w(z)+\frac{zw'(z)}{w(z)},
\]
the defining positive-real-part expression equals \(w+\alpha zw'/w\). Writing this Carathéodory function as \(1+2c_1z+2c_2z^2+2c_3z^3+\cdots\) gives, by coefficient comparison,
\[
\begin{aligned}
(1+\alpha)w_1&=2c_1,\\
(1+2\alpha)w_2-\alpha w_1^2&=2c_2,\\
(1+3\alpha)w_3-3\alpha w_1w_2+\alpha w_1^3&=2c_3.
\end{aligned}
\]
Also \(a_2=w_1\), \(a_3=(w_2+w_1^2)/2\), and \(a_4=(w_3+3a_2a_3-a_2^3)/3\). Carathéodory's coefficient bound \(|c_j|\le1\) and these identities give, **uniformly** over all admissible functions,
\[
\begin{aligned}
a_2&=2c_1/\alpha+O(\alpha^{-2}),\\
a_3&=c_2/(2\alpha)+O(\alpha^{-2}),\\
a_4&=2c_3/(9\alpha)+O(\alpha^{-2}),\\
\alpha^2(a_2a_4-a_3^2)&=(16c_1c_3-9c_2^2)/36+O(\alpha^{-1}).
\end{aligned}
\]
The error constants are absolute because the displayed rational coefficient identities have uniformly bounded numerators whenever \(|c_j|\le1\). It remains to compute the exact maximum of the last polynomial on the Carathéodory moment body.

**Step 2: a sharp three-moment inequality.** Rotation of the variable sends \(c_k\) to \(e^{ik\phi}c_k\), so the modulus of \(16c_1c_3-9c_2^2\) is unchanged. Set \(c_1=r\in[0,1]\), \(u=r^2\), and \(v=1-u\). The Schur coefficient parameters, with \(|x|,|y|\le1\), give
\[
c_2=u+vx,\quad c_3=r^3+2rvx-rvx^2+v(1-|x|^2)y.
\]
Consequently
\[
16c_1c_3-9c_2^2=A+Bx-Cx^2+D(1-|x|^2)y,
\]
where
\[
A=7u^2,\quad B=14uv,\quad C=v(9+7u),\quad D=16\sqrt u\,v.
\]
Crucially \(C\ge D\), since \(9+7r^2-16r=(1-r)(9-7r)\ge0\). For a fixed unit complex number \(\lambda\), the real quadratic
\[
\operatorname{Re}\bigl(\lambda(A+Bx-Cx^2)\bigr)+D(1-|x|^2)
\]
has real Hessian eigenvalues \(-2D+2C\ge0\) and \(-2D-2C\le0\). Along an eigenvector for the nonnegative eigenvalue, its restriction to any line segment in the disk is convex, so every interior value is no larger than a value at the boundary. Maximizing first over \(y\), then over \(\lambda\), proves that an extremum is attained with \(|x|=1\).

Let \(x=e^{it}\), \(\xi=\cos t\). Direct multiplication gives
\[
|A+Bx-Cx^2|^2=(A+C)^2+B^2+2B(A-C)\xi-4AC\xi^2.
\]
This is concave in \(\xi\). If \(0\le u\le2/7\), its derivative at \(\xi=-1\) equals \(28u(1-u)(28u^2+20u-9)\le0\). Hence the maximum is reached at \(\xi=-1\), where
\[
|A-B-C|=|28u^2-12u-9|\le72/7.
\]
Equality on this interval occurs uniquely at \(u=3/14\). If \(2/7\le u<1\), completion of the square in \(\xi\) and the inequality \(|\xi|\le1\) give
\[
|A+Bx-Cx^2|^2\le (A+C)^2\left(1+\frac{B^2}{4AC}\right)
=\frac{16(9-2u)^2}{9+7u}.
\]
The right-hand side strictly decreases for \(u\in[2/7,1)\), and its value at \(u=2/7\) is \(16(59/7)^2/11<(72/7)^2\). At \(u=1\), the original expression has modulus \(7\). Thus the sharp global constant is \(72/7\).

Equality forces \(u=3/14\), \(x=-1\), up to initial rotation. The Schur boundary condition then uniquely fixes the first three moments as \(c_k=\cos(k\theta_0)\), with \(\cos\theta_0=\sqrt{3/14}\). The corresponding representing measure is the equal-weight pair at \(e^{\pm i\theta_0}\), because \(|x|=1\) means the Schur recursion terminates at degree two. This gives the asserted moment extremizers.

**Step 3: sharpness for \(\mathcal M_\alpha\).** Choose the extremal Carathéodory function
\[
p_*(z)=\frac{1-z^2}{1-2\sqrt{3/14}\,z+z^2}.
\]
It has positive real part in \(\mathbb D\). Define \(g\) by \(zg'(z)/g(z)=p_*(z)\), \(g(0)=0\), \(g'(0)=1\); explicitly \(g(z)=z\exp(\int_0^z(p_*(\zeta)-1)/\zeta\,d\zeta)\), which is starlike. For each \(\alpha>0\), let
\[
f_\alpha(z)=\left[\frac1\alpha\int_0^z \zeta^{1/\alpha-1}\left(\frac{g(\zeta)}\zeta\right)^{1/\alpha}d\zeta\right]^\alpha,
\]
with the analytic branch normalized near zero. The standard Mocanu--Todorov integral correspondence (see references) gives \(f_\alpha\in\mathcal M_\alpha\), with \(J_\alpha[f_\alpha]=p_*\). Its moment polynomial equals \(-72/7\), so Step 1 yields \(\alpha^2|a_2a_4-a_3^2|=2/7+O(\alpha^{-1})\). The upper bound from Steps 1--2, together with this lower bound, proves the theorem.

## Verification
A standalone symbolic checker (`check.py`) verifies the coefficient identity through degree four, the exact moment substitution, the Hessian threshold factorization, both branch-polynomial reductions, and the limiting coefficient \(2/7\). Execute `python check.py` with SymPy as specified in `requirements.txt`. Its checks are corroborative finite symbolic algebra; the universal moment maximization, Herglotz representation, and integral correspondence require the analytical reasoning above.

## Relationship to prior work
Bravo, Carrasco, Hernández and Venegas (arXiv:2606.21574, first public 2026-06-19; inspected October revision) conjecture a finite-parameter sharp second-Hankel formula and explicitly do not prove its global extremality. Their conjectural negative-branch trial family has the same leading \(2/7\) coefficient; this result proves the leading coefficient for the **full** admissible class, not the finite-parameter conjecture.

Sokół and Thomas (2018) give parameter-dependent upper bounds for the same determinant. The more recent full-text treatment by Sokół, Majumder, Haldar and Panja (arXiv:2610.21260, theorem 3.1) reproduces a large-parameter upper bound with coefficient \(9/28>2/7\), so that bound does not force this sharp asymptotic. The present proof also identifies the exact Carathéodory three-moment mechanism underlying the asymptotic limit. The complete 2018 original was unavailable, so priority claims remain provisional.

## Limitations
This theorem concerns \(\alpha\to+\infty\), not sharp finite-\(\alpha\) values or negative parameters. The \(O(\alpha^{-3})\) remainder is not optimized to an explicit best coefficient. Earlier equivalent specializations not located in accessible sources remain a historical-priority risk. The result is a self-contained mathematical argument supported by self-review only; no independent mathematical audit has been performed.

## References
1. V. Bravo, P. Carrasco, R. Hernández, and O. Venegas, “Sharp coefficient, logarithmic and Schwarzian estimates for α-convex functions on the real line,” arXiv:2606.21574 (first posted 2026-06-19; inspected version of 2026-10-22), especially pages 1--2 and 12--13. https://arxiv.org/abs/2606.21574
2. J. Sokół and D. F. Thomas, “The second Hankel determinant for alpha-convex functions,” Lithuanian Mathematical Journal 58 (2018), 212--218, DOI:10.1007/s10986-018-9397-0. Abstract and theorem as reproduced in reference 3; original full text not inspected.
3. J. Sokół, S. Majumder, G. Haldar, and S. Panja, “Alpha-convex functions in complex Banach spaces,” arXiv:2610.21260 (first posted 2026-10-15), theorem 3.1 and its proof. https://arxiv.org/abs/2610.21260
4. P. T. Mocanu and collaborators, classical α-convex/starlike integral correspondence, as cited and stated in reference 1, equation (4), and reference 3, Theorem B.
