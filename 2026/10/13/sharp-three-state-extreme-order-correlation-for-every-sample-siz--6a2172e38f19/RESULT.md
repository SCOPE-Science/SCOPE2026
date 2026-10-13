# Sharp three-state extreme-order correlation for every sample size at least four

## Finding
Let \(n\ge4\) be an integer and let \(X_1,\ldots,X_n\) be independent, identically distributed random variables with probabilities \(1/3\) at each of three distinct real numbers \(x_1<x_2<x_3\). Write \(L_n=\min_iX_i\), \(U_n=\max_iX_i\), and
\[
a_n=3^{-n},\qquad b_n=(2/3)^n.
\]
Then
\[
\operatorname{Corr}(L_n,U_n)\le
R_n:=\frac{(a_n+b_n)^2-a_n}{3a_n+b_n-(a_n+b_n)^2}.
\]
**Equality holds exactly when** \(x_2=(x_1+x_3)/2\), i.e., the three support points form an arithmetic progression. For every \(n\ge4\) the upper bound is attained, so it is sharp. Moreover,
\[
R_n\sim(2/3)^n\qquad(n\to\infty).
\]
For example, \(R_4=104/625\). This establishes the three-point, all-sample-sizes-at-least-four extreme-rank instance of the lattice-optimality question posed in the cited discrete Terrell study. It does **not** optimize over parent probability vectors.

## Assumptions and scope
The sample is with replacement (independent draws), its three parent atoms are strictly ordered and equally likely, and the sample size is any integer \(n\ge4\). The correlation is the ordinary Pearson coefficient, well-defined because both sample extrema have positive variance. No continuity, moment, smoothness, or asymptotic approximation assumptions are needed. A positive affine transformation sets the support to \(\{0,t,1\}\), uniquely with \(0<t<1\); the optimal midpoint is \(t=1/2\).

## Proof
**1. Exact moments.** Fix \(n\ge4\), abbreviate \(a=3^{-n}\), \(b=(2/3)^n\), \(d=b-a\), and \(h=d^2-a\). Counting the events that all observations lie in a given subset of the three atoms gives
\[
\begin{aligned}
\mathbb EL_n&=a+dt,&\mathbb EU_n&=1-b+dt,\\
\mathbb EL_n^2&=a+dt^2,&\mathbb EU_n^2&=1-b+dt^2,\\
\mathbb E(L_nU_n)&=a(1+t^2)+t(b-2a).
\end{aligned}
\]
Consequently, with \(z=t(1-t)\),
\[
C(z):=\operatorname{Cov}(L_n,U_n)=ab+hz,
\]
and
\[
\begin{aligned}
V_L(t)&=a(1-a)-2adt+d(1-d)t^2,\\
V_U(t)&=b(1-b)-2d(1-b)t+d(1-d)t^2.
\end{aligned}
\]
Both variances are positive for \(0<t<1\).

**2. Symmetric reduction.** Set
\[
V_0=\frac{3a+b-(a+b)^2}{4},\qquad
\ell=d(1-a-b),\qquad k=d(1-d).
\]
Direct expansion using \(t=1/2+s\) and \(z=1/4-s^2\) gives
\[
P(z):=V_L(t)V_U(t)
=\bigl(V_0+k(1/4-z)\bigr)^2-\ell^2(1/4-z).
\]
In particular, \(P(z)>0\) throughout \(0\le z\le1/4\), even at the endpoint limits. The squared correlation is \(\rho(z)^2=C(z)^2/P(z)\). Define
\[
H(z)=2hP(z)-(ab+hz)P'(z).
\]
Then
\[
\frac{d}{dz}\rho(z)^2=\frac{(ab+hz)H(z)}{P(z)^2}.
\]
Because \(P\) is quadratic and \(C\) is affine, the quadratic terms cancel in \(H\): **\(H\) is affine in \(z\)**.

**3. Positive endpoint certificates, uniformly in \(n\).** Write
\[
x=d=\frac{2^n-1}{3^n},\qquad
r=\frac{a}{d^2}=\frac{3^n}{(2^n-1)^2}.
\]
These sequences are strictly decreasing for \(n\ge3\), so for every \(n\ge4\),
\[
0<x\le\frac7{27}<\frac13,\qquad
0<r\le\frac{27}{49}<\frac35.
\]
In particular \(h=d^2(1-r)>0\), so \(C(z)>0\).

The first endpoint is explicitly positive:
\[
P(0)=ab(1-a)(1-b),\qquad
P'(0)=-2ad(1-b)(1+d),
\]
\[
H(0)=2ab(1-b)(h+ab)>0.
\]
At \(z=1/4\), exact polynomial expansion and substitution \(a=rx^2\), \(b=x+rx^2\) give
\[
H(1/4)=rx^5B(r,x),
\]
where
\[
\begin{aligned}
B(r,x)={}&1-x-\frac r2(10x^2-11x+3)\\
&-\frac{r^2}{2}(17x^3-15x^2+4x)\\
&-\frac{r^3}{2}(12x^4-8x^3)-2r^4x^5.
\end{aligned}
\]
For \(0<x<1/3\), the first bracket is positive, the second lies between zero and \(4x\), and the third is negative. Further, \(2r^4x^5\le x/4\) for \(0<r<3/5\), \(0<x<1/3\). Therefore
\[
\begin{aligned}
B(r,x)&\ge1-x-\frac3{10}(10x^2-11x+3)
-\frac9{50}(4x)-\frac x4\\
&=\frac1{10}+\frac{133}{100}x-3x^2
\ge\frac1{10}+\frac{33}{100}x>0.
\end{aligned}
\]
Thus \(H(1/4)>0\). Since \(H\) is affine, \(H(z)>0\) for every \(z\in[0,1/4]\).

**4. Sharpness, uniqueness, and asymptotics.** With \(C(z)>0\) and \(P(z)>0\), the displayed derivative is strictly positive. Hence \(\rho(z)\) is strictly increasing in \(z\), whose unique maximum on \(0<t<1\) occurs at \(z=1/4\), equivalently \(t=1/2\). At that midpoint, both variances equal \(V_0\), and
\[
C(1/4)=\frac{(a+b)^2-a}{4};
\]
therefore \(\rho(1/4)=C(1/4)/V_0=R_n\), proving the inequality and its exact equality condition. Finally \(a/b\to0\), \(a/b^2=(3/4)^n\to0\), and \(b\to0\), so \(R_n/b\to1\).

## Verification
Run `python verify.py` in this package after installing the dependencies in `requirements.txt`. The verifier checks all critical symbolic moment, covariance, variance-product, affine-derivative, and endpoint-factorization identities; it also enumerates exact joint distributions for four finite sample sizes and several rational support gaps. The reported finite diagnostics are not an exhaustive proof of the unbounded \(n\) result; the positivity inequalities above supply that missing uniform argument. The code is a reproducibility supplement rather than an independent mathematical certification.

## Relationship to prior work
Papadatos (2022, arXiv:2205.14360v1, Section 3 and concluding discussion) proves a sharp lattice-optimality result for *two* sample observations and all finite uniform support sizes. His concluding formulation asks whether the uniform lattice remains correlation-optimal under common monotone transformations for other extreme ranks and sample sizes. Here the support is fixed to three equiprobable points but the sample size ranges through **every** integer at least four. The existing general Székely–Móri bound gives only \(\operatorname{Corr}(L_n,U_n)\le1/n\), rather than the sharp three-state expression above. A separate published three-point probability-weight optimization concerns two observations on already equally spaced atoms, whereas the present problem holds atom probabilities fixed and optimizes their spacing for larger samples. López-Blázquez and Salamanca-Miño (2021) give an automatic-differentiation method for maximal correlation of order statistics from discrete parents; the accessible first-page preview and abstract indicate a computational method and examples, not this uniform-in-sample-size sharp three-atom geometry theorem. The full 27-page text was not obtainable for inspection, and remains a specific priority risk. None of the inspected claims yields this assertion by a parameter substitution.

## Limitations
This proof does not classify nonuniform weights, four or more parent support points, samples drawn without replacement, or correlations of intermediate ranks. It addresses ordinary Pearson correlation under a *common* strictly increasing transformation, not unrestricted maximal correlation with distinct transforms at the two extrema. The source comparison is based on inspected cited work and targeted literature records; it is not an independent priority certification. Equality uses strictly distinct atoms, and no convergence-rate bound is claimed beyond the displayed asymptotic equivalence.

## References
1. N. Papadatos, *A discrete analogue of Terrell's characterization of rectangular distributions*, arXiv:2205.14360v1 (first public version 2022-05-28), especially Theorem 1.2 and concluding questions. https://arxiv.org/abs/2205.14360
2. G. J. Székely and T. F. Móri, *An extremal property of rectangular distributions*, Statistics & Probability Letters 3 (1985), 107–109 (general order-statistic correlation inequality, as quoted and discussed in reference 1).
3. *Sharp min-max correlation over three-point probability weights*, publicly indexed research note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-uniform-maximizes-three-point-minmax-correlation--92f0f4188ee4 (two-draw, probability-varying comparison, not a source for the new proof).

4. F. López-Blázquez and B. Salamanca-Miño, *Automatic differentiation and maximal correlation of order statistics from discrete parents*, Computational Statistics 36 (2021), 2889–2915, DOI:10.1007/s00180-021-01103-5 (abstract and publisher first-page preview consulted; full text not inspected).
