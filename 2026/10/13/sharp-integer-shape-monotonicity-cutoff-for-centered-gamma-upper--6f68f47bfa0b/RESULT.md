# Sharp integer-shape monotonicity cutoff for centered Gamma upper tails
## Finding
Let \(G_n\sim\operatorname{Gamma}(n,1)\) for integers \(n\ge1\), and for \(c>-1/3\) put
\[
p_n(c)=\Pr\{G_n-n>c\}.
\]
Then \((p_n(c))_{n\ge1}\) is nondecreasing in \(n\) exactly for
\[
c\ge e-3.
\]
It is strictly increasing when \(c>e-3\). At \(c=e-3\), exactly the first increment vanishes:
\[
p_1(e-3)=p_2(e-3),\qquad p_{n+1}(e-3)>p_n(e-3)\quad(n\ge2).
\]
Thus the integer-shape Gamma family has a sharp monotonicity cutoff strictly inside the interval \((-1/3,0)\), even though the corresponding real-shape centered tail is non-monotone throughout that entire interval.
## Assumptions and scope
The Gamma law uses shape \(n\) and scale \(1\), so its density is \(x^{n-1}e^{-x}/\Gamma(n)\) on \((0,\infty)\). Only integer shapes \(n\ge1\) are asserted. The parameter range in the equivalence is \(c>-1/3\); no claim about monotonicity for more negative shifts is needed. The constant \(e\) is the base of the natural logarithm.
## Proof
For integer \(n\), Gamma--Poisson duality gives
\[
p_n(c)=\Pr\{\operatorname{Pois}(n+c)\le n-1\}.
\]
Write \(x=n+c\), and let \(F_n(\lambda)=\Pr\{\operatorname{Pois}(\lambda)\le n\}\). Since
\[
F_n'(\lambda)=-e^{-\lambda}\frac{\lambda^n}{n!},
\]
one obtains the exact adjacent-shape factorization
\[
\begin{aligned}
p_{n+1}(c)-p_n(c)
&=F_n(x+1)-F_{n-1}(x)\\
&=\frac{e^{-x}x^n}{n!}\left[1-I_n(c)\right],
\end{aligned}
\]
where
\[
I_n(c)=\int_0^1 e^{-s}\left(1+\frac{s}{n+c}\right)^n\,ds.
\]
If \(c\ge0\), then the logarithm of the integrand has derivative
\[
\frac{n}{n+c+s}-1\le0,
\]
so \(I_n(c)<1\) and every increment is positive.

It remains to treat \(e-3\le c\le0\). First, every adjacent increment is strictly increasing as a function of \(c\) on \((-1,0]\). Indeed, if \(g_n(y)=e^{-y}y^{n-1}/(n-1)!\), then
\[
\frac{d}{dc}\bigl(p_{n+1}(c)-p_n(c)\bigr)=g_n(n+c)-g_{n+1}(n+1+c).
\]
With \(x=n+c\), the logarithm of the ratio of the second density to the first is
\[
L_n(x)-1,
\qquad
L_n(x)=\log\frac{x+1}{n}+(n-1)\log\left(1+\frac1x\right).
\]
Moreover
\[
L_n'(x)=\frac{x-n+1}{x(x+1)}>0
\]
for \(c>-1\), while
\[
L_n(n)=n\log\left(1+\frac1n\right)<1.
\]
Hence \(g_{n+1}(n+1+c)<g_n(n+c)\) whenever \(-1<c\le0\), proving the asserted strict increase in \(c\).

We therefore only need the boundary \(c_0=e-3\). Put \(d=3-e\), so \(c_0=-d\), and \(x=n-d\). At \(n=1\), direct evaluation gives
\[
p_1(c_0)=e^{-(e-2)}=p_2(c_0).
\]
For \(n\ge2\), define
\[
h_n(s)=n\log\left(1+\frac{s}{x}\right)-s,
\qquad 0\le s\le1.
\]
Then \(I_n(c_0)=\int_0^1 e^{h_n(s)}\,ds\), and
\[
h_n'(s)=\frac{d-s}{x+s}.
\]
For \(n=2\), elementary integration gives
\[
1-I_2(c_0)=\frac{2+2e-e^2}{e(e-1)^2}>0.
\]
The last inequality follows, for example, from the elementary bounds \(e<2.72<1+\sqrt3\).

Now let \(n\ge3\). The series for \(e\) gives \(2.718<e<2.72\), hence
\[
0.28<d<0.282.
\]
The standard inequality \(\log(1+u)<u-u^2/[2(1+u)]\) for \(u>0\) shows \(h_n(1)<0\). Since \(h_n'\) changes sign only at \(d\), the range of \(h_n\) has width at most
\[
R_n\le \int_d^1\frac{t-d}{x}\,dt=\frac{(1-d)^2}{2x}.
\]
Let \(U\) be uniform on \([0,1]\), and write \(\mu_n=\mathbb E h_n(U)\). Fubini gives
\[
\mu_n=\int_0^1\frac{(1-t)(d-t)}{x+t}\,dt.
\]
Using
\[
\frac1{x+t}=\frac1x-\frac{t}{x^2}+\frac{t^2}{x^2(x+t)},
\]
and noting that the final remainder is negative, one gets
\[
\mu_n<\frac{A_0}{x}-\frac{A_1}{x^2},
\]
where
\[
A_0=\frac d2-\frac16<0,
\qquad
A_1=\frac d6-\frac1{12}<0.
\]
For completeness, negativity of the remainder follows by writing it as \(x^{-2}(dD-N)\), with
\[
D=\int_0^1\frac{t^2(1-t)}{x+t}\,dt,
\qquad
N=\int_0^1\frac{t^3(1-t)}{x+t}\,dt,
\]
and observing
\[
\frac ND\ge\frac{3x}{5(x+1)}>0.37>d.
\]
Hoeffding's lemma applied to the bounded variable \(h_n(U)\) yields
\[
\log I_n(c_0)\le \mu_n+\frac{R_n^2}{8}
< -\frac{a}{x}+\frac{b}{x^2},
\]
where
\[
a=\frac16-\frac d2,
\qquad
b=\frac1{12}-\frac d6+\frac{(1-d)^4}{32}.
\]
The bounds on \(d\) imply
\[
a>\frac{77}{3000},
\qquad
b<\frac{163}{2400},
\qquad
\frac ba<\frac{815}{308}<2.647.
\]
For \(n\ge3\), \(x=n-d\ge e>2.718\), so the right-hand side is strictly negative. Hence \(I_n(c_0)<1\), and therefore
\[
p_{n+1}(c_0)>p_n(c_0)\qquad(n\ge2).
\]
By the already proved monotonicity of each increment in \(c\), all increments are positive for \(e-3<c\le0\), while the boundary has exactly the first equality.

Finally,
\[
p_2(c)-p_1(c)=e^{-(2+c)}(3+c-e).
\]
Thus for every \(-1/3<c<e-3\) the first increment is negative, so the sequence cannot be nondecreasing. This proves sharpness and the full equivalence.
## Verification
Every universal step above is analytic. The Gamma--Poisson identity fixes the normalization and converts adjacent shapes to a one-dimensional integral with positive prefactor. The derivative comparison is exact and uses only \(c>-1\). At the boundary, the only exceptional increment is evaluated in closed form; all later increments are controlled uniformly by Hoeffding's lemma and explicit rational bounds. Finite numerical experiments are unnecessary for the proof.
## Relationship to prior work
Pinelis proved that for real shape \(a>0\), the centered upper tail \(\Pr\{X_a-a>c\}\) is increasing for \(c>0\), decreasing for \(c\le-1/3\), and non-monotone in real \(a\) for every \(-1/3<c<0\). His proof also establishes eventual positivity of the unit increment in the intermediate regime, but does not give a sharp parameter cutoff for monotonicity on the integer-shape subsequence. Sun, Hu, and Sun study Gamma probabilities relative to the mean and prove, in particular, the mean-threshold result corresponding to \(c=0\); their stated MSC begins with 60E15. The present finding identifies the exact negative shift down to which monotonicity survives after restricting to Erlang/integer shapes.
## Limitations
The theorem concerns only unit-scale Gamma laws with integer shape, though scale changes can of course be absorbed by rescaling the additive shift. It classifies monotonicity of the integer sequence, not the number or location of extrema of the real-shape function. It also does not classify the integer sequence for \(c\le-1/3\), because that lies outside the sharp transition interval addressed here. A residual literature risk is that the same integer-subsequence cutoff may have appeared under Erlang waiting-time or incomplete-Gamma terminology not retrieved by the searches described in the review.
## References
1. I. Pinelis, “Monotonicity properties of the gamma family of distributions,” arXiv:2012.13578v1, 25 December 2020; later published in *Statistics & Probability Letters*.
2. P. Sun, Z.-C. Hu, and W. Sun, “The extreme values of two probability functions for the Gamma distribution,” arXiv:2303.17487v1, 30 March 2023.
