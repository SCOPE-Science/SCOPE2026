# A non-Gaussian sharp near-equal-weight law for random quadratic quadrature

## Finding
Let \(X_1,\ldots,X_m\) be independent uniform random points on \([-1,1]\), for each integer \(m\ge3\). Among all real quadrature weights \(w_1,\ldots,w_m\) that integrate every polynomial of degree at most two exactly against the uniform probability measure on \([-1,1]\), let
\[
T_m=\min\max_{1\le i\le m}|mw_i-1|.
\]
The minimum exists almost surely, and the following explicit weak limit holds:
\[
\sqrt m\,T_m\ \Longrightarrow\ W:=2\left(|G_2|+\sqrt{G_1^2+G_2^2}\right),
\]
where \(G_1,G_2\) are independent centered normal random variables with respective variances \(1/3\) and \(4/45\). This limit is non-Gaussian and has a continuous distribution. Consequently, for every fixed \(t>0\), the probability that all exact quadrature weights can be chosen in the interval
\[
\left[\frac{1-t/\sqrt m}{m},\frac{1+t/\sqrt m}{m}\right]
\]
converges to \(\mathbb P(W\le t)\). In particular those feasible weights are strictly positive for sufficiently large \(m\).

The distribution is explicit: for \(t\ge0\), putting \(\sigma_1=1/\sqrt3\) and \(\sigma_2=2/\sqrt{45}\),
\[
\mathbb P(W\le t)=\frac{\sqrt{2/\pi}}{\sigma_2}
\int_0^{t/4}\exp\left(-\frac{v^2}{2\sigma_2^2}\right)
\operatorname{erf}\left(\frac{\sqrt{t^2/4-tv}}{\sqrt2\,\sigma_1}\right)\,dv.
\]
At \(t=0\) the integral is zero.

## Assumptions and scope
The target integration functional is \(I(f)=\frac12\int_{-1}^1 f(x)\,dx\). The nodes are iid uniform with no conditioning. Weight adaptation is performed after the nodes are observed. Feasible weights are initially allowed to be real, and positivity follows asymptotically from the displayed \(t/\sqrt m\) band. Exact integration is required simultaneously for \(1,x,x^2\). The degree remains two as \(m\to\infty\); no growing-degree assertion is made.

## Proof
**1. Finite-sample dual.** Write \(\delta_i=mw_i-1\) and \(h(x)=x^2-1/3\). Exact moment matching is equivalent to
\[
\sum_i\delta_i=0,\quad \sum_i\delta_iX_i=-\sum_iX_i,\quad
\sum_i\delta_i h(X_i)=-\sum_i h(X_i).
\]
With probability one at least three nodes are distinct, so this system has rank three and is solvable. Elementary \(\ell_\infty/\ell_1\) linear programming duality, eliminating the constant multiplier through its sample median, gives the exact identity
\[
T_m=\sup_{(a,b)\ne(0,0)}
\frac{\left|a\sum_iX_i+b\sum_i h(X_i)\right|}
{\inf_{c\in\mathbb R}\sum_i|c+aX_i+b h(X_i)|}.
\]
The denominator is positive whenever \((a,b)\ne(0,0)\), since a quadratic polynomial taking one constant value at three distinct points is itself constant.

**2. Exact population dual norm.** Define
\[
N(a,b)=\inf_{c\in\mathbb R}\frac12\int_{-1}^1|c+ax+b h(x)|\,dx.
\]
Using reflection in \(x\) and negation, this depends only on \(|a|,|b|\). It suffices to assume \(a,b\ge0\). If \(a\ge b\), then \(ax+bx^2=x(a+bx)\) has the sign of \(x\) throughout \([-1,1]\); zero is a median and direct integration of its absolute value gives \(a/2\). If \(0\le a<b\), the sublevel set below the median is the centered interval of length one, namely \([-(1+a/b)/2,(1-a/b)/2]\). Its median is \((b^2-a^2)/(4b)\), and direct integration gives \((a^2+b^2)/(4b)\). Hence
\[
N(a,b)=\begin{cases}|a|/2,&|a|\ge|b|,\\
(a^2+b^2)/(4|b|),&0\le|a|<|b|.
\end{cases}
\]
This is a genuine norm on \(\mathbb R^2\). Its dual norm has the explicit form
\[
N^*(u,v)=\sup_{N(a,b)\le1}(au+bv)
=2\left(|v|+\sqrt{u^2+v^2}\right).
\]
To verify the last equality, take \(u,v,a,b\ge0\) by symmetry. On \(a\ge b\) the feasible region is \(0\le b\le a\le2\), contributing at most \(2(u+v)\). On \(a\le b\) the condition \(N(a,b)\le1\) is the disk \(a^2+(b-2)^2\le4\); its maximizer is \((a,b)=(2u/r,2+2v/r)\), where \(r=\sqrt{u^2+v^2}\), and lies in \(a\le b\). It contributes \(2v+2r\), which dominates \(2(u+v)\). The zero vector case is immediate.

**3. Uniform convergence and Gaussian limit.** For each \((a,b)\), define the empirical norm
\[
N_m(a,b)=\inf_{c\in\mathbb R}\frac1m\sum_{i=1}^m|c+aX_i+b h(X_i)|.
\]
On the Euclidean unit circle in \((a,b)\), all scalar minimizers \(c\) lie in a common deterministic compact interval: a median lies between the minimum and maximum of the bounded sample values. The class of absolute-value functions indexed by this compact triple of parameters is uniformly Lipschitz and bounded. A finite covering argument plus the strong law therefore yields almost surely uniform convergence \(N_m\to N\) on the unit circle. Since \(N\) is continuous and strictly positive there, \(N_m\) is uniformly bounded away from zero for all sufficiently large \(m\).

The two-vector
\[
Z_m=\frac1{\sqrt m}\left(\sum_iX_i,\ \sum_i(X_i^2-1/3)\right)
\]
converges in law, by the bivariate central limit theorem, to independent Gaussian coordinates \((G_1,G_2)\). Indeed \(\mathbb E X^2=1/3\), \(\mathbb E(X^2-1/3)^2=4/45\), and \(\mathbb E[X(X^2-1/3)]=0\). The exact finite dual and the uniform denominator convergence imply
\[
\sqrt m\,T_m=\sup_{(a,b)\ne(0,0)}
\frac{|aZ_{m,1}+bZ_{m,2}|}{N_m(a,b)}
\Longrightarrow N^*(G_1,G_2)=W,
\]
by Slutsky's theorem and the continuous mapping theorem. The Gaussian density is absolutely continuous and the displayed dual-norm function has no positive-measure level sets, so the law of \(W\) is continuous.

**4. Distribution and positivity.** Set \(U=|G_1|\), \(V=|G_2|\). The event \(W\le t\) is \(0\le V\le t/4\) together with \(0\le U\le\sqrt{t^2/4-tV}\). Integrating the folded-normal densities gives the stated formula. The finite-sample optimality band is exactly \(T_m\le t/\sqrt m\); for fixed \(t\) its lower endpoint is strictly positive when \(m>t^2\). This proves the probability claim with no additional positivity assumption.

## Verification
The included `verify.py` numerically checks the piecewise exact population norm against direct integration, its explicit support norm against attaining coefficients, and finite random-sample linear programs against feasible exact-moment correction vectors. It also checks the Gaussian-limit expression on generated Gaussian coordinates. Run `python verify.py` after installing the versions listed in `REQUIREMENTS.txt`. These finite tests check formula consistency; the weak limit follows from the analytic proof above, not from simulation.

## Relationship to prior work
Neumayer, Schäfer, and Ullrich (arXiv:2610.32699, first public October 23, 2026) establish random-node positive quadrature and finite-dimensional \(L_1\) duality for weight adaptation, including high-probability near-equal-weight bounds. The finite-dimensional dual in step 1 is a specialization of this established approach, **not** a new claim. The contribution here is the explicit sharp fixed-degree random-scale law obtained by evaluating the quadratic population-median norm and its nonelliptic dual. Their general concentration result does not state this limiting law or its integral CDF. Bělík, Narayan, and Turnage (arXiv:2609.09506) study a specific randomized least-squares quadrature construction, rather than the minimum possible \(\ell_\infty\) correction. Hayakawa, Lyons, and Oberhauser (arXiv:2101.04250) study random convex-hull inclusion, which concerns existence of positive weights rather than the optimal narrow symmetric band about uniform weights.

## Limitations
The asymptotic result holds for iid uniform nodes on the one-dimensional interval and fixed quadratic exactness only. It does not give a finite-sample distribution, an optimized rule for higher polynomial degree, or a rate of convergence in distribution. The result describes existence of adapted weights, not a numerically stable algorithm for computing them in finite precision. Because general optimal balancing-weight asymptotics are a substantial literature, possible equivalent uncatalogued specializations remain a scientific priority risk.

## References
- S. Neumayer, M. Schäfer, and T. Ullrich, *Random nodes with positive weights: Richter-Tchakaloff rules and optimal positive quadrature*, arXiv:2610.32699 (2026), https://arxiv.org/abs/2610.32699.
- L. Bělík, A. Narayan, and P. Turnage, *Constructive Tchakaloff results and well-conditioned quadrature through randomized least squares*, arXiv:2609.09506 (2026), https://arxiv.org/abs/2609.09506.
- M. Hayakawa, T. Lyons, and H. Oberhauser, *Estimating the probability that a given vector is in the convex hull of a random sample*, arXiv:2101.04250 (2021), https://arxiv.org/abs/2101.04250.
