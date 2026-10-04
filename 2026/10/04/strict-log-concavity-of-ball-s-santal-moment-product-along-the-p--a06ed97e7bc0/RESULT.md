# Strict log-concavity of Ball's Santaló moment product along the ℓp scale

## Finding
For an integer \(n\ge2\), write
\[
B_p^n=\left\{x\in\mathbb R^n:\sum_{j=1}^n|x_j|^p\le1\right\},\qquad 1<p<\infty,
\]
and let \(q=p/(p-1)\), so \((B_p^n)^\circ=B_q^n\). Define Ball's quadratic Santaló functional
\[
\mathcal B(K)=\int_K\int_{K^\circ}\langle x,y\rangle^2\,dx\,dy.
\]
With \(t=1/p\in(0,1)\), set
\[
F_n(t)=\frac{\mathcal B(B_{1/t}^n)}{\mathcal B(B_2^n)},
\]
where the polar exponent has reciprocal \(1-t\). Then
\[
\frac{d^2}{dt^2}\log F_n(t)<0\qquad(0<t<1).
\]
Thus \(\log F_n\) is strictly concave. Since polarity gives \(F_n(t)=F_n(1-t)\), the function is strictly increasing on \((0,1/2)\), strictly decreasing on \((1/2,1)\), and has the unique maximum
\[
F_n(1/2)=1.
\]
Equivalently, as \(p\) runs from \(2\) to \(\infty\), the normalized Ball moment product decreases strictly from the Euclidean value to
\[
F_n(\infty)=\frac{2^{2n+1}(n+2)^2\Gamma(n/2+1)^2}{3(n+2)!\,\pi^n}.
\]

## Assumptions and scope
The statement concerns real \(\ell_p^n\) balls in dimensions \(n\ge2\). The strict concavity is asserted in the reciprocal exponent \(t=1/p\), not in \(p\) itself. The endpoint values \(p=1\) and \(p=\infty\) are understood by continuity. No assertion is made that analogous monotonicity holds for arbitrary paths of symmetric convex bodies.

Because \(B_p^n\) is unconditional and invariant under coordinate permutations, its second-moment matrix is scalar. Hence, if
\[
I_n(p)=\int_{B_p^n}x_1^2\,dx,
\]
then
\[
\mathcal B(B_p^n)=nI_n(p)I_n(q).
\]
Therefore it is enough to analyze the coordinate moment product.

## Proof
A beta-integral evaluation gives, for \(1<p<\infty\),
\[
I_n(p)=\frac{2^n}{3}\,
\frac{\Gamma(1+3/p)\Gamma(1+1/p)^{n-1}}
{\Gamma(1+(n+2)/p)}.
\]
Put \(t=1/p\) and, for a positive integer \(a\), define
\[
\Phi_a(t)=\log\Gamma(1+at)+\log\Gamma(1+a(1-t)).
\]
Constants independent of \(t\) disappear after differentiation, and the exact formula above yields
\[
\log F_n(t)=\Phi_3(t)+(n-1)\Phi_1(t)-\Phi_{n+2}(t)+C_n
\]
for a constant \(C_n\).

Let \(\psi_1\) denote the trigamma function and define
\[
G_t(x)=\psi_1(t+x)+\psi_1(1-t+x).
\]
The series representation
\[
\psi_1(z)=\sum_{k=0}^{\infty}\frac{1}{(z+k)^2}
\]
shows directly that \(G_t(x)\) is strictly decreasing for \(x>0\). Differentiating Gauss's multiplication formula for \(\Gamma\) twice gives, for every positive integer \(a\),
\[
\Phi_a''(t)=\sum_{r=1}^{a}G_t\!\left(\frac r a\right).
\]
Set \(N=n+2\), so \(N\ge4\). The \(N\) numbers
\[
\frac1N,\frac2N,\ldots,\frac NN
\]
are coordinatewise no larger, after sorting, than the \(N\)-term multiset
\[
\left\{\frac13,\frac23,\underbrace{1,\ldots,1}_{N-2\text{ copies}}\right\},
\]
and the first comparison is strict. Since \(G_t\) is strictly decreasing,
\[
\Phi_N''(t)>
\Phi_3''(t)+(N-3)\Phi_1''(t)
=
\Phi_3''(t)+(n-1)\Phi_1''(t).
\]
Consequently
\[
(\log F_n)''(t)<0
\]
for every \(0<t<1\). The identity \(F_n(t)=F_n(1-t)\) follows from swapping the polar pair. Strict concavity then forces strict increase to \(t=1/2\), strict decrease afterward, and a unique maximum there.

Finally,
\[
I_n(\infty)=\frac{2^n}{3},\qquad
I_n(1)=\frac{2^{n+1}}{(n+2)!},\qquad
I_n(2)=\frac{\pi^{n/2}}{(n+2)\Gamma(n/2+1)}.
\]
Substitution into \(F_n=I_n(p)I_n(q)/I_n(2)^2\) gives the stated endpoint formula.

## Verification
The accompanying `verify.py` independently checks the beta-integral formula against direct one-dimensional slice quadrature for several dimensions and exponents, evaluates the exact second-derivative formula at separated test points, checks the strict Ball inequality away from \(p=2\), and verifies convergence to the cube--crosspolytope endpoint. Its successful replay prints `VERIFY_OK`.

These finite checks are sanity checks only. The continuum claim follows from the analytic trigamma identity and the coordinatewise grid comparison in the proof.

## Relationship to prior work
Böröczky, Patsalos, and Saroglou proved Ball's 1986 conjectured Santaló-type moment inequality for all symmetric convex bodies and characterized ellipsoids as the equality cases. Their introduction also recalls that Ball had previously proved the inequality in the unconditional case. Since \(\ell_p\) balls are unconditional, those results imply only the pointwise upper bound \(F_n(t)\le1\); they do not compare two non-Euclidean exponents.

The present statement supplies a complete profile on the canonical polar family \(B_p^n\leftrightarrow B_q^n\): strict log-concavity in reciprocal exponent and hence strict monotonicity away from the Euclidean point. Searches for the source identifier, the exact gamma product, reciprocal-exponent log-concavity, second-moment products of dual \(\ell_p\) balls, and related \(\ell_p\)-ball monotonicity results did not locate a statement implying this profile. Literature on monotonicity of hyperplane projection volumes and on gamma-function estimates for \(\ell_p\)-ball sections concerns different functionals and does not imply the moment-product assertion.

## Limitations
The argument exploits the exact Dirichlet integral for \(\ell_p\) balls and the integer multiplication formula for the gamma function. It does not establish geodesic, Minkowski, or Banach--Mazur path concavity for Ball's functional on general convex bodies. The main residual originality risk is that the gamma-function inequality could have appeared independently in special-functions literature or in an unindexed discussion of Ball's unconditional case; no such statement was located in the checked sources.

## References
1. K. J. Böröczky, K. Patsalos, C. Saroglou, *On Ball's conjectured Santaló type inequality*, arXiv:2602.20325v1 (first public 2026-02-23), primary MSC 52A20.
2. K. Ball, *Isometric problems in \(\ell_p\) and sections of convex sets*, PhD dissertation, University of Cambridge, 1986.
3. K. Ball, *Some remarks on the geometry of convex sets*, in *Geometric Aspects of Functional Analysis*, Lecture Notes in Mathematics 1317 (1988), 224--231.
4. F. Barthe, A. Naor, *Hyperplane projections of the unit ball of \(\ell_p^n\)*, Discrete Comput. Geom. 27 (2002), 215--226.
5. H. König, *On maximal hyperplane sections of the unit ball of \(\ell_p^n\) for \(p>2\)*, Adv. Oper. Theory 10 (2025), article 15.
