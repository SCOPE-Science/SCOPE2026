# Balanced non-uniform reset coupon collectors: profile rates and heterogeneity penalties

## Statement

Fix a reset probability \(q\in(0,1)\), write
\[
s=1-q,\qquad c=\frac{q}{s},
\]
and consider \(n\) standard coupon types. Conditional on a non-reset draw, coupon \(i\) has probability
\[
w_{i,n}=\frac{x_{i,n}}{n},
\]
where for fixed constants \(0<m\le 1\le M<\infty\),
\[
m\le x_{i,n}\le M,\qquad \frac1n\sum_{i=1}^n x_{i,n}=1.
\]
Equivalently, on each calendar step a reset occurs with probability \(q\), while standard coupon \(i\) occurs with probability \(s x_{i,n}/n\). A reset erases the current collection, and collection then resumes from empty.

Let \(C_n\) be the ordinary coupon-collector completion time in standard-coupon draws with probabilities \(w_{i,n}\), let
\[
g_n(z)=\mathbb E z^{C_n},
\qquad
p_n=g_n(s),
\]
and let \(T_n\) be the reset-collector completion time. Thus \(p_n\) is the probability that a single reset-free attempt succeeds.

Define
\[
L_n(y)=\frac1n\sum_{i=1}^n \log(1-e^{-x_{i,n}y}),
\qquad
\Phi_n(y)=L_n(y)-cy,\qquad y>0.
\]
There is a unique maximizer \(y_n\in(0,\infty)\), characterized by
\[
c=\frac1n\sum_{i=1}^n\frac{x_{i,n}}{e^{x_{i,n}y_n}-1}.
\]
Set
\[
A_n=-\Phi_n''(y_n)
=
\frac1n\sum_{i=1}^n
\frac{x_{i,n}^2e^{x_{i,n}y_n}}
{(e^{x_{i,n}y_n}-1)^2}.
\]

### Theorem 1: saddle-point success probability and mean completion time

Uniformly over all arrays satisfying the bounds above,
\[
p_n
=
c\sqrt{\frac{2\pi n}{A_n}}\,
e^{\,n\Phi_n(y_n)}(1+o(1)).
\]
Consequently,
\[
\mathbb E T_n
=
\frac{\sqrt{A_n}}
{q\,c\,\sqrt{2\pi n}}\,
e^{-n\Phi_n(y_n)}(1+o(1)).
\]

The saddles stay in a fixed compact interval:
\[
\frac1M\log\!\left(1+\frac{M}{c}\right)
\le y_n\le
\frac1m\log\!\left(1+\frac{m}{c}\right).
\]

For equal standard probabilities (\(x_{i,n}\equiv1\)),
\[
y_n=-\log q,\qquad
\Phi_n(y_n)=\log s+\frac{q}{s}\log q,
\]
and the formula reduces to
\[
p_n
\sim
\sqrt{2\pi qn}\,
\bigl(sq^{q/s}\bigr)^n.
\]
In fact, in the equal case,
\[
p_n=
\frac{\Gamma(n+1)\Gamma(nq/s+1)}
{\Gamma(n/s+1)},
\]
so this recovers the beta/gamma asymptotic already known for the uniform reset collector.

### Theorem 2: a limiting profile-rate functional

Suppose the empirical measures
\[
\nu_n=\frac1n\sum_{i=1}^n\delta_{x_{i,n}}
\]
converge weakly to a probability measure \(\nu\) on \([m,M]\). Since all \(\nu_n\) have mean \(1\), so does \(\nu\).

There is a unique \(y_\nu>0\) solving
\[
c=
\int\frac{x}{e^{xy_\nu}-1}\,d\nu(x).
\]
Define
\[
\Lambda_q(\nu)
=
-cy_\nu
+
\int\log(1-e^{-xy_\nu})\,d\nu(x).
\]
Then
\[
\frac1n\log p_n\longrightarrow \Lambda_q(\nu),
\qquad
\frac1n\log\mathbb E T_n\longrightarrow-\Lambda_q(\nu).
\]
Thus the non-uniform coupon vector enters the fixed-reset asymptotics through a one-dimensional saddle coupled to the limiting empirical profile.

### Theorem 3: explicit sharp exponential-approximation rate

Wang and Lu's memoryless-catastrophe theory uses
\[
\alpha_n
=
\frac{s\bigl(p_n-qg_n'(s)\bigr)}
{1-p_n}
\]
and proves, for fixed \(q\), a two-sided Kolmogorov estimate
\[
d_K\!\left(\frac{T_n}{\mathbb E T_n},\operatorname{Exp}(1)\right)
\asymp_q p_n+|\alpha_n|
\]
whenever \(p_n+|\alpha_n|\) is sufficiently small.

For the balanced non-uniform coupon collector above, let \(\mu_n\) be the probability law on \((0,\infty)\) with density proportional to \(e^{n\Phi_n(y)}\), and write
\[
\bar y_n=\int y\,d\mu_n(y).
\]
Then the exact derivative identity is
\[
\frac{g_n'(s)}{p_n}
=
\frac{n\bar y_n-1/c}{s^2},
\]
hence
\[
\alpha_n
=
\frac{p_n}{1-p_n}
\bigl(1+s-cn\bar y_n\bigr).
\]
Laplace concentration gives
\[
\bar y_n=y_n+O(n^{-1/2})
\]
uniformly in the balanced class. Therefore
\[
\alpha_n
=
-cn y_n p_n\bigl(1+O(n^{-1/2})\bigr),
\]
and in particular
\[
d_K\!\left(\frac{T_n}{\mathbb E T_n},\operatorname{Exp}(1)\right)
=
\Theta_{q,m,M}(n p_n).
\]
Combining with Theorem 1,
\[
d_K\!\left(\frac{T_n}{\mathbb E T_n},\operatorname{Exp}(1)\right)
=
\Theta_{q,m,M}\!\left(
n^{3/2}e^{\,n\Phi_n(y_n)}
\right).
\]
If \(\nu_n\Rightarrow\nu\), this gives the logarithmic convergence rate
\[
\frac1n\log
d_K\!\left(\frac{T_n}{\mathbb E T_n},\operatorname{Exp}(1)\right)
\longrightarrow
\Lambda_q(\nu).
\]

Thus the same profile functional controls three quantities: the single-attempt success probability, the exponential growth of the mean completion time, and the exponential decay rate of the normalized completion-time error.

### Theorem 4: exact uniform extremality and a quantitative heterogeneity penalty

For fixed \(n\), \(q\), and \(\sum_i x_i=n\), the success probability
\[
(x_1,\ldots,x_n)\longmapsto p_n
\]
is strictly Schur-concave on the positive orthant. Hence the uniform vector maximizes \(p_n\) and minimizes \(\mathbb E T_n\).

The balanced regime also gives a quantitative exponential penalty. Let
\[
a_*=\frac1M\log\!\left(1+\frac{M}{c}\right),
\qquad
b_*=\frac1m\log\!\left(1+\frac{m}{c}\right),
\]
and
\[
\kappa_*=
\min_{\substack{x\in[m,M]\\y\in[a_*,b_*]}}
\frac{y^2e^{xy}}{(e^{xy}-1)^2}>0.
\]
Write
\[
V_n=\frac1n\sum_{i=1}^n(x_{i,n}-1)^2.
\]
Then
\[
\Phi_n(y_n)
\le
\log s+\frac{q}{s}\log q
-\frac{\kappa_*}{2}V_n.
\]
Consequently, if \(\liminf_nV_n\ge v>0\),
\[
\liminf_{n\to\infty}
\frac1n\log
\frac{\mathbb E T_n}
{\mathbb E T_n^{\rm unif}}
\ge
\frac{\kappa_*v}{2}.
\]
Persistent balanced heterogeneity therefore incurs an exponential, not merely polynomial, delay under fixed resetting.

## Proof

### 1. Exact Poisson-race representation

Introduce independent continuous-time Poisson processes: reset events have rate \(q\), while coupon \(i\) has rate \(s w_{i,n}\). Their superposition has rate \(1\), and its sequence of event labels is exactly the original discrete-time sampling scheme.

A reset-free attempt succeeds precisely when every coupon process has fired before the first reset. If \(R\sim\operatorname{Exp}(q)\) is the first reset time, independence gives
\[
p_n
=
\int_0^\infty q e^{-qt}
\prod_{i=1}^n
\bigl(1-e^{-s w_{i,n}t}\bigr)\,dt.
\]
After \(u=st\), and then \(u=ny\),
\[
p_n
=
c\int_0^\infty e^{-cu}
\prod_{i=1}^n(1-e^{-w_{i,n}u})\,du
=
nc\int_0^\infty e^{n\Phi_n(y)}\,dy.
\]
This also proves directly that the integral equals \(g_n(s)=\mathbb E s^{C_n}\).

### 2. Unique saddle and compactness

For \(y>0\),
\[
\Phi_n'(y)
=
\frac1n\sum_i
\frac{x_{i,n}}{e^{x_{i,n}y}-1}
-c,
\]
and
\[
\Phi_n''(y)
=
-\frac1n\sum_i
\frac{x_{i,n}^2e^{x_{i,n}y}}
{(e^{x_{i,n}y}-1)^2}<0.
\]
Also \(\Phi_n'(y)\to+\infty\) as \(y\downarrow0\) and \(\Phi_n'(y)\to-c\) as \(y\to\infty\). Hence there is a unique maximizer \(y_n\).

For fixed \(y\), the function
\[
x\mapsto\frac{x}{e^{xy}-1}
\]
is decreasing. Applying this to the saddle equation gives the stated lower and upper bounds on \(y_n\).

On the resulting common compact saddle interval, \(A_n\) is bounded above and bounded away from zero uniformly in the balanced class. All higher derivatives needed in a fixed neighborhood of the saddle are also uniformly bounded. Strict concavity supplies a uniform quadratic local bound, while away from the saddle the exponent loses a fixed positive amount. Standard one-dimensional Laplace asymptotics therefore give
\[
nc\int_0^\infty e^{n\Phi_n(y)}\,dy
=
c\sqrt{\frac{2\pi n}{A_n}}\,
e^{n\Phi_n(y_n)}(1+o(1)),
\]
uniformly over the balanced arrays.

Memoryless reset gives the exact renewal identity
\[
\mathbb E T_n=\frac{1-p_n}{qp_n}.
\]
The uniform-vector bound below implies \(p_n\) is exponentially small, so substitution yields the displayed mean asymptotic.

### 3. Profile limit

Because \(x\in[m,M]\) and \(y_n\in[a_*,b_*]\), weak convergence \(\nu_n\Rightarrow\nu\) implies uniform convergence on compact \(y\)-sets of
\[
\int\log(1-e^{-xy})\,d\nu_n(x)
\]
and of its first derivative. Strict concavity gives \(y_n\to y_\nu\), and therefore
\[
\Phi_n(y_n)\to\Lambda_q(\nu).
\]
The polynomial Laplace prefactor contributes only \(o(n)\) to logarithms, proving the rate limits.

### 4. Evaluation of \(g_n'(s)\) and \(\alpha_n\)

For \(z\in(0,1)\), put \(c_z=(1-z)/z\). The same Poisson-race calculation gives
\[
g_n(z)
=
nc_z
\int_0^\infty
\exp\left\{
n\left[L_n(y)-c_zy\right]
\right\}\,dy.
\]
Differentiating its logarithm is legitimate because the integrand has exponential tails. Since \(c_z'=-z^{-2}\),
\[
\frac{g_n'(z)}{g_n(z)}
=
\frac{n\bar y_{n,z}-1/c_z}{z^2},
\]
where \(\bar y_{n,z}\) is the mean of \(y\) under the normalized integrand. At \(z=s\), this is the displayed exact derivative formula.

The same local quadratic estimate used for Laplace's method gives
\[
\mathbb E_{\mu_n}|Y-y_n|=O(n^{-1/2}),
\]
hence \(\bar y_n=y_n+O(n^{-1/2})\). Substitution into Wang and Lu's definition of \(\alpha_n\) gives
\[
\alpha_n
=
\frac{p_n}{1-p_n}
(1+s-cn\bar y_n)
=
-cn y_np_n(1+O(n^{-1/2})).
\]
Because \(y_n\) is bounded above and away from zero, \(|\alpha_n|\asymp n p_n\), while \(p_n=o(np_n)\). Wang and Lu's two-sided theorem then yields the claimed sharp order for \(d_K\).

This calculation also verifies the qualitative unequal-probability rare-success condition used by Long: the relevant derivative is \(O(np_n)\), while \(p_n\) decays exponentially.

### 5. Schur extremality and quantitative penalty

For every fixed \(y>0\),
\[
\varphi_y(x)=\log(1-e^{-xy})
\]
is strictly concave:
\[
\varphi_y''(x)
=
-\frac{y^2e^{xy}}{(e^{xy}-1)^2}<0.
\]
Therefore
\[
\sum_i\varphi_y(x_i)
\]
is strictly Schur-concave. Exponentiation and integration preserve the corresponding ordering, so \(p_n\) is strictly Schur-concave. The uniform vector is majorized by every vector with the same sum, hence it maximizes \(p_n\). Since \((1-p)/(qp)\) is strictly decreasing in \(p\), it minimizes the mean reset completion time.

For \(x\in[m,M]\) and \(y\in[a_*,b_*]\), \(\varphi_y''(x)\le-\kappa_*\). Strong concavity about \(x=1\), followed by averaging and using \(\frac1n\sum_i(x_i-1)=0\), gives
\[
L_n(y)
\le
\log(1-e^{-y})
-\frac{\kappa_*}{2}V_n.
\]
At \(y=y_n\),
\[
\Phi_n(y_n)
\le
\left[\log(1-e^{-y_n})-cy_n\right]
-\frac{\kappa_*}{2}V_n.
\]
The bracket is at most its maximum over \(y>0\), attained at \(y=-\log q\), and equals
\[
\log s+\frac{q}{s}\log q.
\]
This proves the quantitative exponent gap and, after using the Laplace mean asymptotics, the ratio bound.

## Context and significance

Jocković and Todić introduced the reset-button coupon collector and obtained the finite waiting-time distribution for unequal standard probabilities; their asymptotic analysis of the mean focuses on equal probabilities. Li, Dai and Kim subsequently gave an explicit expected-waiting-time formula for arbitrary standard probabilities.

Long's regenerative formulation identifies the unequal reset collector through
\[
p_n=\mathbb E s^{C_n}
\]
and proves a qualitative exponential limit under rare-success derivative conditions, but leaves the ordinary unequal collector transform to be estimated.

Wang and Lu give a general sharp theorem
\[
d_K(T/\mathbb ET,\operatorname{Exp}(1))\asymp p+|\alpha|
\]
and explicitly identify non-uniform coupon probabilities as a further direction: the remaining challenge is to evaluate the coupon-specific \(D_1=g'(s)\) and \(\alpha\), and to determine how the asymptotics depend on the coupon probability vector.

The results above perform that evaluation in a broad balanced non-uniform regime. They produce an explicit saddle functional for the full probability profile, identify the exponential scale of the mean, convert the general \(p+|\alpha|\) theorem into a sharp \(np_n\) rate, and quantify the exponential cost of heterogeneity.

## Limitations

- The reset probability \(q\) is fixed in \((0,1)\). Regimes where \(q=q_n\to0\) or \(q_n\to1\) require a separate moving-saddle analysis.
- The balance condition \(m/n\le w_{i,n}\le M/n\) excludes very rare coupon types, Zipf-like tails, and profiles with probabilities on multiple asymptotic scales.
- The Kolmogorov estimate uses Wang and Lu's general fixed-\(q\) sharp theorem; the new content here is the non-uniform coupon evaluation of \(p_n\), \(g_n'(s)\), \(\alpha_n\), and the resulting rate.
- The Laplace approximation is first-order. No second-order saddle correction is claimed.
- The heterogeneity penalty is explicit but not claimed optimal as a function of \(V_n\).
- Originality is to the best of our knowledge. General saddle-point, majorization, or unequal-coupon transform results under different terminology could imply parts of the analysis; the closest reset-specific results located are listed below.

## References

1. S. Wang and Z. Lu, "On Completion Times under Memoryless Catastrophe," arXiv:2609.16566 (2026). https://arxiv.org/abs/2609.16566
2. C. D. Long, "Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors," arXiv:2605.14511 (2026). https://arxiv.org/abs/2605.14511
3. J. Jocković and B. Todić, "Coupon Collector Problem with Reset Button," Mathematics 12(2), 239 (2024). https://doi.org/10.3390/math12020239
4. Y. Li, C. Dai and D. Kim, "Generalized analysis of the coupon collector problem with reset button," AIMS Mathematics 11(7), 19739-19748 (2026). https://doi.org/10.3934/math.2026800
5. P. Flajolet, D. Gardy and L. Thimonier, "Birthday paradox, coupon collectors, caching algorithms and self-organizing search," Discrete Applied Mathematics 39 (1992), 207-229.
6. N. Zoroa, E. Lesigne, M.-J. Fernández-Sáez, P. Zoroa and J. Casas, "The coupon collector urn model with unequal probabilities in ecology and evolution," Journal of the Royal Society Interface 14 (2017), 20170258. https://doi.org/10.1098/rsif.2017.0258
