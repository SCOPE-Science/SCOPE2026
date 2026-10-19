# A cubic boundary-layer law for linear \(H^4\) approximation to geometric sums

## Finding

Let \(m\ge1\) be any integer and let \(f_m(z)=1+z+\cdots+z^m\). With normalized Haar measure \(d\theta/(2\pi)\) on the unit circle, let \(q_m\) be the unique complex polynomial of degree at most one that minimizes \(\|1-q f_m\|_{H^4}\). Define

\[
F_m(t)=\frac38(1+t)^4+3m(1+t)^2t^2+2m(m-1)(1+t)t^3+\frac{m(2m^2+1)}3t^4.
\]

There is a unique \(t_m\in(-1,0)\) satisfying \(F_m'(t_m)=0\), and the *global complex-coefficient* minimizer, its zero, and its fourth-power error are exactly

\[
q_m(z)=\frac{1-t_m}{2}-\frac{1+t_m}{2}z,\qquad
w_m=\frac{1-t_m}{1+t_m}>1,\qquad
E_m^4=\|1-q_m f_m\|_{H^4}^4=F_m(t_m).
\]

Let \(c\) be the unique root in \((0,1)\) of

\[
16c^3-36c^2+36c-9=0
\]

and set \(\kappa=-c(4c^3-12c^2+18c-9)/6\). Both constants are explicit and positive, with \(c\approx0.357498368378205\) and \(\kappa\approx0.233323093727595\). As the geometric-sum length grows,

\[
t_m=-\frac{c}{m}+O(m^{-2}),\qquad
w_m=1+\frac{2c}{m}+O(m^{-2}),\qquad
E_m^4=\frac38-\frac{\kappa}{m}+O(m^{-2}).
\]

The reciprocal symmetry used to obtain this result is not limited to the fourth norm: for every real \(1<p<\infty\), the unique degree-one optimal approximant to \(1/f_m\) in \(H^p\) has the form \(q_{m,p}(z)=a_{m,p}+(a_{m,p}-1)z\) with \(a_{m,p}\in\mathbb R\).

## Assumptions and scope

The result holds for every integer \(m\ge1\). The Hardy norm is \(\|P\|_{H^p}^p=(2\pi)^{-1}\int_0^{2\pi}|P(e^{i\theta})|^p\,d\theta\) for polynomials \(P\). Coefficients of candidate approximants are allowed to be *arbitrary complex numbers*. No restriction to real or palindromic candidates is assumed. The approximation degree is fixed at one while \(m\) grows; \(E_m\) is the minimum error in that two-dimensional approximation space, not a claim concerning higher-degree approximants.

## Proof

**1. Uniqueness and reciprocal reduction for every \(p>1\).** Since \(f_m\ne0\), multiplication by \(f_m\) is injective on the polynomials of degree at most one. Its range is finite-dimensional, hence closed. Strict convexity of \(L^p\) for \(1<p<\infty\) gives a unique nearest point to the constant function \(1\), and therefore a unique optimal polynomial. Real coefficients of \(f_m\), complex conjugation of Fourier coefficients, and invariance of the norm force the coefficients of the unique optimizer to be real.

For \(q(z)=a+bz\), put \(R(z)=1-q(z)f_m(z)\). Define its reciprocal conjugate by \(R^\sharp(z)=z^{m+1}\overline{R(1/\overline z)}\). The identities \(z^m f_m(1/z)=f_m(z)\) and \(1-z^{m+1}=(1-z)f_m(z)\) give

\[
R^\sharp(z)=1-f_m(z)\big[1+\overline b+(\overline a-1)z\big].
\]

Because \(|R^\sharp(e^{i\theta})|=|R(e^{i\theta})|\), reciprocal conjugation sends an optimizer to an optimizer. Uniqueness implies \(a=1+\overline b\), and reality then yields \(b=a-1\). This proves the claimed symmetry for all \(p>1\) without presuming real coefficients in the optimization.

**2. The exact fourth-moment polynomial.** Parametrize \(a=(1-t)/2\), \(b=-(1+t)/2\), with real \(t\), and write \(e=(1+t)/2\). The residual \(R=1-qf_m\) has the coefficient vector

\[
(e,\underbrace{t,\ldots,t}_{m\text{ entries}},e).
\]

Its nonnegative-lag autocorrelations are \(r_0=2e^2+mt^2\), \(r_k=2et+(m-k)t^2\) for \(1\le k\le m\), and \(r_{m+1}=e^2\). Parseval applied to \(|R|^2\) gives

\[
\|R\|_{H^4}^4=r_0^2+2\sum_{k=1}^{m+1}r_k^2
=6e^4+12me^2t^2+4m(m-1)et^3+\frac{m(2m^2+1)}3t^4=F_m(t).
\]

**3. Global optimization and zero location.** The fourth-power norm of the residual is strictly convex along the real line of candidates, since distinct candidate residuals differ at almost every boundary point and \(|\cdot|^4\) is strictly convex. Thus \(F_m\) has exactly one global minimizer. Direct differentiation gives

\[
F_m'(-1)=-\frac{2m(m+1)(4m-1)}3<0,
\qquad F_m'(0)=\frac32>0.
\]

The unique critical point \(t_m\) therefore lies strictly between \(-1\) and \(0\). The displayed formula for \(q_m\) and \(w_m\) follows; in particular \(1+t_m>0\) and \(1-t_m>1\), so the zero is strictly outside the closed unit disk.

**4. Uniform asymptotic expansion.** On each bounded interval of \(u\ge0\), substitution \(t=-u/m\) into the explicit polynomial yields uniformly, along with the first derivative,

\[
F_m(-u/m)=\frac38+\frac{Q(u)}m+O(m^{-2}),\qquad
Q(u)=\frac{u}{6}(4u^3-12u^2+18u-9).
\]

The derivative of \(Q\) is

\[
Q'(u)=\frac83u^3-6u^2+6u-\frac32,\qquad
Q''(u)=8u^2-12u+6=2(4u^2-6u+3)>0.
\]

Because \(Q'(0)<0<Q'(1)\), there is exactly one positive critical point \(c\in(0,1)\), and it is the unique root of the stated cubic. Let \(u_m=-mt_m\). Since the derivative with respect to \(u\) of \(m[F_m(-u/m)-3/8]\) tends to \(Q'(u)\) uniformly on bounded intervals, choose fixed points on either side of \(c\); the opposite derivative signs and convexity trap \(u_m\) between them. Shrinking this interval gives \(u_m\to c\). The same uniform derivative expansion with \(Q''(c)>0\) yields \(u_m=c+O(m^{-1})\). Substitution gives

\[
E_m^4=F_m(-u_m/m)=\frac38+\frac{Q(c)}m+O(m^{-2}).
\]

Since \(Q'(0)<0\), \(c\) is the strict minimizer of \(Q\), and \(Q(0)=0\), the value \(\kappa=-Q(c)\) is strictly positive. Finally, \(w_m=(1+u_m/m)/(1-u_m/m)=1+2c/m+O(m^{-2})\), completing the proof.

## Verification

The accompanying standalone `check_h4.py` uses only the Python standard library. It computes the scalar derivative and its unique root by bisection; independently recomputes fourth moments from the full coefficient autocorrelation for nine values of \(m\); compares selected values against direct root-of-unity quadrature of the original boundary integral; and checks numerical stabilization of the constants through \(m=10000\). Its reproduced output is `check_h4_output.txt`.

The proof above, not these finite experiments, establishes the statements for every integer \(m\). The exact autocorrelation formula and the positive quadratic \(Q''(u)\) are the decisive analytic certificates.

## Relationship to prior work

Centner, Cheng, and Felder [1] study degree-zero and degree-one optimal approximants in \(H^p\), including general coefficient and zero-location bounds. Cheng and Felder [2] analyze additional properties and examples, including an occurrence of \(1+z+z^2\) in a *norm comparison*, but do not present the present geometric-sum degree-one fourth-norm minimization or its growing-length asymptotics. A later study [3] provides further general root restrictions and Hardy-space projection properties. These general statements neither specify the unique cubic boundary-layer constant nor the exact fourth-power error correction for this fixed-degree family.

For comparison, the elementary Hilbert-space calculation gives the linear \(H^2\) optimizer \(q_{m,2}(z)=((m+1)-mz)/(2m+1)\), with zero \(1+1/m\). In contrast the sharp \(H^4\) zero displacement is \(2c/m+O(m^{-2})\), with \(2c\approx0.714996736756410\). The explicit nonlinear constant is the point of the comparison; no claim is made that the \(H^2\) benchmark is new.

## Limitations

This theorem concerns the fixed approximant degree one and the geometric-sum generators only. It does not establish all higher-degree optimal approximants, uniform asymptotics as the Hardy exponent varies, numerical stability of computed roots under perturbations of the generator, or a general solution of the Hardy-space zero-location problem. Originality is assessed against the cited accessible published literature and mathematical-results records; no finite search can prove absolute uniqueness in the entire literature.

## References

[1] R. Centner, R. Cheng, and C. Felder, *Optimal Polynomial Approximants in \(H^p\)*, arXiv:2305.16068v1, first public 25 May 2023, https://arxiv.org/html/2305.16068v1.

[2] R. Cheng and C. Felder, *More Properties of Optimal Polynomial Approximants in Hardy Spaces*, arXiv:2310.16010v1, first public 24 October 2023, https://arxiv.org/html/2310.16010v1.

[3] *Metric projections, zeros of optimal polynomial approximants, and some extremal problems in Hardy spaces*, arXiv:2511.08000v1, first public 11 November 2025, https://arxiv.org/html/2511.08000v1.
