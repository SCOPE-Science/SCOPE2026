# One-crossing covariance law for threshold exceedances in symmetric Dirichlet samples

## Finding
Let \(n\ge3\), \(\alpha>0\), and \(V=(V_1,\ldots,V_n)\sim\operatorname{Dirichlet}(\alpha,\ldots,\alpha)\). For \(0<t<1\), write \(K_t=\sum_{i=1}^n\mathbf1\{V_i>t\}\), \(p(t)=\Pr(V_1>t)\), and \(q(a,b)=\Pr(V_1>a,V_2>b)\). For \(0<a\le b<1\),
\[
\operatorname{Cov}(K_a,K_b)=np(b)\left[1-np(a)+(n-1)\frac{q(a,b)}{p(b)}\right].\tag{1}
\]
There is a unique \(a_*=a_*(n,\alpha)<1/2\) with \(p(a_*)=1/n\). If \(0<a<a_*\), the covariance in (1), as a function of \(b\in[a,1)\), is strictly positive before exactly one zero \(b_*(a)\in(a,1-a)\) and strictly negative afterward. If \(a>a_*\), it is strictly positive everywhere on this domain. At \(a=a_*\), it is positive for \(a\le b<1-a\) and zero for \(1-a\le b<1\). This includes the boundary where two distinct coordinates cannot both exceed the two thresholds.

When \(\alpha=1\) (uniform circle spacings),
\[
p(a)=(1-a)^{n-1},\quad q(a,b)=(1-a-b)_+^{n-1},\quad a_*=1-n^{-1/(n-1)},
\]
and for \(0<a<a_*\),
\[
b_*(a)=1-\frac{a}{1-\left[(n(1-a)^{n-1}-1)/(n-1)\right]^{1/(n-1)}}.\tag{2}
\]
In particular the nested counts \(K_b\le K_a\) can have strictly **negative** covariance, with exactly one transition in the larger threshold.

For fixed \(\alpha>0\) and \(0<x\le y\), let \(G\sim\operatorname{Gamma}(\alpha,1)\), \(p_x=\Pr(G>\alpha x)\), and \(c_x=\alpha x f_G(\alpha x)\). Then
\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(K_{x/n},K_{y/n})}{n}
=p_y(1-p_x)-\frac{c_xc_y}{\alpha}.\tag{3}
\]
For every fixed \(x>0\), the right side is strictly positive at \(y=x\), decreases in sign through exactly one zero on \(y\in(x,\infty)\), and remains negative beyond it. For \(\alpha=1\) the limiting zero is \(y=(e^x-1)/x\).

## Assumptions and scope
The concentration \(\alpha\) is arbitrary positive real; the dimension \(n\) is any integer at least three; thresholds are real with \(0<a\le b<1\). Symmetric Dirichlet components are strictly positive and sum to one almost surely. Strictly greater-than thresholds are used throughout (boundary atoms are absent). In (3), \(\alpha,x,y\) remain fixed while \(n\to\infty\); the zero in (3) concerns the asymptotic covariance **at scale \(n\)**, not a finite-sample independence assertion. The Dirichlet threshold-count problem and the uniform circular-spacing special case are both covered.

## Proof
**1. Mixed moment.** Exchangeability gives \(\mathbb E K_t=np(t)\). In the product \(K_aK_b\), the same-index term is \(np(b)\), while the \(n(n-1)\) different-index terms have probability \(q(a,b)\). Subtract \(n^2p(a)p(b)\) to get (1).

**2. Monotone conditional tail.** Fix \(a\in(0,1)\). By Dirichlet conditioning, given \(V_2=y\),
\[
V_1=(1-y)B,\qquad B\sim\operatorname{Beta}(\alpha,(n-2)\alpha),
\]
where the conditional law of \(B\) does not depend on \(y\). Hence \(g_a(y):=\Pr(V_1>a\mid V_2=y)=\Pr(B>a/(1-y))\) decreases strictly on \(0<y<1-a\) and is identically zero on \(y\ge1-a\). As \(V_2\) has a strictly positive density, \(r_a(b):=q(a,b)/p(b)=\mathbb E[g_a(V_2)\mid V_2>b]\) is continuous, strictly decreasing as \(b\) runs through \((0,1-a)\), and zero for \(b\ge1-a\). Strictness follows, for two truncated-tail levels, by splitting the lower truncation interval from its upper tail and noting that \(g_a\) is strictly decreasing on a set of positive measure. Thus the bracket in (1) strictly decreases to \(1-np(a)\) and then remains constant.

**3. Starting sign and classification.** At \(b=a\), equation (1) is \(\operatorname{Var}(K_a)>0\). Indeed, for every \(a\in(0,1)\), the open simplex contains configurations with one dominant coordinate and configurations with a different number of coordinates exceeding \(a\); the Dirichlet density is positive on both regions. The continuous strictly decreasing survival function \(p\) runs from \(1\) to \(0\), giving the unique \(a_*\). Because at most one coordinate can exceed \(1/2\) and there is positive probability that none exceeds \(1/2\), \(p(1/2)<1/n\), whence \(a_*<1/2\). If \(p(a)>1/n\), the bracket in (1) begins positive and ends negative, with a unique zero before \(1-a\). If \(p(a)<1/n\), it is everywhere positive. Equality makes the bracket positive until \(1-a\), where it becomes zero. This proves all finite-dimensional assertions.

**4. Uniform-spacing explicit formulas.** At \(\alpha=1\), the Dirichlet distribution is uniform on the simplex. Directly scaling one coordinate, or two coordinates simultaneously, gives the displayed powers for \(p\) and \(q\). Substitution into (1) and solving the one-root equation yields (2).

**5. Joint Gamma expansion.** Set \(m=n\alpha\) and \(T_i=mV_i\). Write \(f(t)=t^{\alpha-1}e^{-t}/\Gamma(\alpha)\). Uniformly on compact positive \(t\)-sets, the one- and two-coordinate densities satisfy
\[
\begin{aligned}
f_{T_1}(t)&=f(t)\left[1+\frac{h_1(t)}m+O(m^{-2})\right],\\
f_{T_1,T_2}(t,s)&=f(t)f(s)\left[1+\frac{h_2(t,s)}m+O(m^{-2})\right],
\end{aligned}
\]
where
\[
\begin{aligned}
h_1(t)&=-\frac{\alpha(\alpha+1)}2+(\alpha+1)t-\frac{t^2}2,\\
h_2(t,s)&=-\alpha(2\alpha+1)+(2\alpha+1)(t+s)-\frac{(t+s)^2}2.
\end{aligned}
\]
This follows by writing the exact Beta/Dirichlet densities, applying \(\Gamma(m)/\Gamma(m-k\alpha)=m^{k\alpha}[1-k\alpha(k\alpha+1)/(2m)+O(m^{-2})]\) for \(k=1,2\), and expanding \((1-u/m)^{m-c}\). The key cancellation is
\[
h_2(t,s)-h_1(t)-h_1(s)=-(t-\alpha)(s-\alpha).\tag{4}
\]
For the fixed tail sets \(t>\alpha x\) and \(s>\alpha y\), the expansions can be integrated: first truncate to a fixed large rectangle, then bound its complement by the exact densities using the exponential factor \((1-(t+s)/m)^{m-2\alpha-1}\) (and the analogous marginal factor). For fixed \(\alpha,x,y\), choosing a rectangle growing slowly with \(m\) yields an integrated remainder \(o(m^{-1})\) and exponentially negligible outside; the same conclusion follows by dominated differentiation of the normalized gamma-ratio densities. Thus
\[
n\operatorname{Cov}(\mathbf1\{V_1>x/n\},\mathbf1\{V_2>y/n\})
\longrightarrow-\frac1\alpha\prod_{z\in\{x,y\}}\mathbb E[(G-\alpha)\mathbf1\{G>\alpha z\}].
\]
Gamma integration by parts yields \(\mathbb E[(G-\alpha)\mathbf1\{G>t\}]=tf(t)\). The same-coordinate contribution to the covariance of the full sums, divided by \(n\), tends to \(p_y(1-p_x)\), proving (3).

**6. One asymptotic crossing.** Divide (3) by \(p_y>0\); its sign is that of \(1-p_x-(c_x/\alpha)(c_y/p_y)\). Since
\[
\frac{p_y}{c_y}=\int_1^\infty u^{\alpha-1}e^{-\alpha y(u-1)}\,du,
\]
this ratio decreases continuously and strictly from its positive value at \(y=x\) to zero as \(y\to\infty\). Consequently \(c_y/p_y\) increases strictly without bound. At \(y=x\) the covariance in (3) is strictly positive by Cauchy–Schwarz: \(\operatorname{Var}(\mathbf1\{G>\alpha x\})>\operatorname{Cov}(\mathbf1\{G>\alpha x\},G)^2/\operatorname{Var}(G)\), because a nontrivial indicator cannot be affine in a continuously distributed Gamma variable. Hence there is exactly one zero and the sign reversal follows. For \(\alpha=1\), substituting \(p_z=e^{-z}\) and \(c_z=ze^{-z}\) gives \(y=(e^x-1)/x\).

## Verification
The included `verify.py` is a standalone Python 3 standard-library checker. It tests exact rational Beta and Dirichlet tail integration for small integer concentration values, checks the finite one-crossing property for rational threshold grids, checks the density-expansion algebra and tests the explicit \(\alpha=1\) asymptotic curve. Executing `python3 verify.py` produced `VERIFY_OK`. Finite checks are supplementary; steps 1–6 prove the stated real-parameter assertions.

## Relationship to prior work
Mirakhmedov (2024, arXiv:2404.09581) proves central limit theorems for sums of functions of uniform spacings, including a Gaussian variance structure that specializes to the \(\alpha=1\) part of the asymptotic covariance formula. We therefore **do not claim** the general uniform-spacing central limit mechanism or its marginal variance as new. The assessed result instead is a complete **finite-dimensional all-\(\alpha>0\) one-crossing and exact-zero classification**, including its explicit uniform-spacing threshold and Gamma-limit one-crossing boundary. Classical Dirichlet/gamma conditioning and spacings theory provide the probabilistic input; their role is acknowledged. The finite classification does not follow from the sign of a marginal CLT variance without the monotone conditional-tail argument.

## Limitations
The principal historical-priority risk is that classical full distributions or a general result on Dirichlet spacings may contain an equivalent crossing classification in different notation; an inaccessible classical monograph chapter was not treated as proof of noncoverage. The asymptotic covariance formula at \(\alpha=1\) is closely related to published uniform-spacing CLT covariance theory. No independent audit or experimental universality beyond the stated symmetric Dirichlet model is asserted.

## References
1. S. M. Mirakhmedov, *The central limit theorem for sum-functions of m-tuples of spacings*, arXiv:2404.09581, first posted 2024-04-15, https://arxiv.org/abs/2404.09581 .
2. R. Pyke, *Spacings*, Journal of the Royal Statistical Society, Series B **27** (1965), 395–449. (Classical background; not fully inspected.)
3. G. R. Shorack and J. A. Wellner, *Empirical Processes with Applications to Statistics*, Chapter 21, spacings. (Historical-priority context; chapter body not inspected.)
4. S. Frühwirth-Schnatter and G. Malsiner-Walli, *From here to infinity: sparse finite versus Dirichlet process mixtures in model-based clustering*, Advances in Data Analysis and Classification (2019); online 2018. (Modern background on symmetric Dirichlet weights.)
