# Exact global reset-benefit thresholds and spatial nesting on finite cycles

## Finding
For a simple symmetric nearest-neighbor walk on the cycle of \(m\ge3\) vertices, started at \(0\) with target at cyclic distance \(1\le d\le\lfloor m/2\rfloor\), let \(T_q(d)\) be its first hitting time when every update independently resets the position to \(0\) with probability \(q\), consuming an update, and otherwise takes one unbiased nearest-neighbor step. Define \(\mu_d=d(m-d)\) and \(\kappa_d=m^2-5\mu_d-5\). The reset probability ranges over \(0\le q<1\).

**Complete sign classification.** If \(\kappa_d\le0\), resetting is strictly detrimental at *every* \(q\in(0,1)\): \(\mathbb E T_q(d)>\mu_d\). If \(\kappa_d>0\), there is exactly one threshold \(q_c(m,d)\in(0,1)\), with strict speedup precisely for \(0<q<q_c(m,d)\), equality at \(q=q_c(m,d)\), and strict slowdown above this threshold. In particular, the local improvement criterion is also necessary for *any* improvement: no disconnected, reentrant regions of beneficial resetting exist.

**Spatial nesting.** For every fixed \(q\in(0,1)\), the normalized ratio \(\mathbb ET_q(d)/\mu_d\) strictly increases with the integer distance \(d\). Consequently, benefiting distances constitute an initial interval of distances starting at one, and the positive thresholds \(q_c(m,d)\) strictly decrease as \(d\) increases. For \(m\le5\), no nontrivial target distance ever benefits; for \(m\ge6\), distance one benefits at sufficiently small positive reset rates. When \(d/m\to\alpha\in(0,1/2]\), the strict limiting benefit region is \(\alpha<(5-\sqrt5)/10\), away from the boundary.

## Assumptions and scope
The graph has vertices \(\{0,1,\ldots,m-1\}\) with addition modulo \(m\). The target may be taken as vertex \(d\); the walker stops immediately upon landing there. At a reset update, no walk step is also performed; reset updates count as elapsed time. For \(q=0\), gambler's ruin on the two directed arcs gives \(\mathbb ET_0(d)=\mu_d\). The theorem does not address heterogeneous reset rates, simultaneous reset-and-hop conventions, directed or non-nearest-neighbor walks, or stochastic ordering of the entire first-passage distribution.

For \(q\in(0,1)\), let \(r\in(0,1)\) be the unique value satisfying \(1-q=2r/(1+r^2)\), or \(q=(1-r)^2/(1+r^2)\), and let \(S_j(r)=\sum_{k=0}^{j-1}r^k\). The exact finite-size mean is
\[
\mathbb ET_q(d)=\frac{(1+r^2)S_d(r)S_{m-d}(r)}{r^d+r^{m-d}}.
\]
If \(\kappa_d>0\), its threshold is computable as \(q_c=(1-r_c)^2/(1+r_c^2)\), where \(r_c\) is the unique root in \((0,1)\) of the explicit polynomial \(P_{m,d}\) constructed below.

## Proof
**1. First-passage transform and renewal.** Without resetting, take the target to be the two absorbing endpoints of a linear interval of length \(m\), with the starting point at distance \(d\) from the left endpoint. With \(z=1-q\), let \(F_d(z)=\mathbb E[z^{T_0(d)}]\). Solving the standard two-boundary recurrence \(u_j=z(u_{j-1}+u_{j+1})/2\), with boundary values one, yields
\[
F_d(z)=\frac{r^d+r^{m-d}}{1+r^m}=\frac{\cosh((m/2-d)\theta)}{\cosh(m\theta/2)},
\quad z=\frac{2r}{1+r^2}=\operatorname{sech}\theta.
\]
A run without any reset completes with probability \(F_d(z)\); the expected duration up to the first reset or hit is \((1-F_d(z))/q\). The renewal identity therefore gives
\[
M_q(d):=\mathbb ET_q(d)=\frac{1-F_d(1-q)}{qF_d(1-q)}=\frac{\cosh(m\theta/2)/\cosh((m/2-d)\theta)-1}{q}.
\]
Since \(1+r^m-r^d-r^{m-d}=(1-r^d)(1-r^{m-d})\), the displayed polynomial/rational mean formula follows.

**2. Palindromic sign certificate.** Write \(a=d\), \(b=m-d\), so \(1\le a\le b\). Define
\[
H(r)=(1+r^2)S_a(r)S_b(r)-ab(r^a+r^b).
\]
Then \(M_q(d)-ab=H(r)/(r^a+r^b)\). Directly from \(r^{j-1}S_j(1/r)=S_j(r)\), the polynomial \(H\) is reciprocal of degree \(m\); also \(H(1)=H'(1)=0\). Thus \(H(r)=(1-r)^2P(r)\), where \(P\) is reciprocal of degree \(m-2\), with constant and leading coefficients one.

Put \(h=\lfloor(m-2)/2\rfloor\), and let \(p_k\) denote the coefficient of \(r^k\) in \(P\). By expanding \(H\) and using division by \((1-r)^2\), one obtains, for \(0\le k\le h\),
\[
p_k=\begin{cases}
\bigl((k+1)^3+2(k+1)\bigr)/3,&0\le k<a,\\
a\bigl[t^2+(a-b)t+(a^2+2)/3\bigr],& a\le k\le h,\quad t=k-a+1.
\end{cases}
\]
For \(a\le k<h\), the second-branch successive difference is \(a(2t+1+a-b)<0\), since \(t\le h-a\le(b-a-2)/2\). The first-branch coefficients are strictly positive. Thus the coefficient sequence up to its midpoint has at most one positive-to-negative sign change; reciprocity implies that the *full* coefficient sequence has at most two sign changes (zeros omitted). Descartes's rule therefore gives at most two positive real roots of \(P\), with multiplicities.

A direct differentiation or summation of the coefficients gives
\[
P(1)=-\frac{ab}{6}(m^2-5ab-5)=-\frac{ab\kappa_d}{6}.
\]
As \(P(0)=1\), when \(\kappa_d>0\) there is a root \(r_c\in(0,1)\). Reciprocal symmetry supplies the distinct root \(1/r_c>1\); Descartes rules out all other positive roots. These roots are simple, so \(P\) is positive below \(r_c\) and negative between \(r_c\) and one. Because increasing \(q\) decreases \(r\), resetting improves the mean precisely when \(0<q<q_c\). If \(\kappa_d<0\), a root in \((0,1)\) would need even multiplicity (the endpoint values of \(P\) are both positive), and its reciprocal would provide at least four positive roots; impossible. At \(\kappa_d=0\), the reciprocal identity forces \(P'(1)=(m-2)P(1)/2=0\), so one already counts a root of multiplicity at least two at one, excluding any other positive roots. Thus \(P(r)>0\) throughout \((0,1)\) when \(\kappa_d\le0\).

**3. Strict ordering by distance.** Put \(L=m/2\), \(y=(L-d)^2\), \(Y=L^2\), and \(f(v)=\operatorname{sech}(\theta\sqrt v)\). If \(\tau\) is the exit time of standard Brownian motion from \((-1,1)\) started at zero, solving \(u''/2=su\) with \(u(\pm1)=1\) gives \(f(v)=\mathbb E\exp(-\theta^2v\tau/2)\). Since \(\tau>0\) almost surely, \(f\) is strictly convex on \([0,\infty)\). Formula 1 now rearranges to
\[
\frac{M_q(d)}{d(m-d)}=\frac{\cosh(L\theta)}{q}\frac{f(y)-f(Y)}{Y-y}.
\]
Strict convexity means the negative secant slope \((f(y)-f(Y))/(Y-y)\) strictly *decreases* as \(y\) increases. Hence the ratio increases strictly as \(d\) increases. Comparing at the common benchmark one proves the nested benefit sets; continuity and the unique-crossing result prove strict decrease of positive critical reset probabilities with distance.

**4. Boundaries and small-reset expansion.** Since \(\kappa_d>0\) is \(d(m-d)<(m^2-5)/5\), the smallest possible product \(m-1\) is below this bound precisely for \(m\ge6\). For proportional distances the strict limiting inequality is \(\alpha(1-\alpha)<1/5\). Expanding the renewal formula at \(q=0\) gives \(M_q(d)=ab-(ab\kappa_d/6)q+O(q^2)\); the equality case of the linear term is covered by the global polynomial argument and is still strictly detrimental for every positive \(q\).

## Verification
A standalone `verify.py` uses exact rational polynomial arithmetic to check the coefficient identities and the sign certificate for every \(3\le m\le35\), independently recomputes the means through finite absorbing-chain linear systems for sample graph sizes and rational reset probabilities, and checks the root classification on selected parameter pairs. These finite checks are corroboration, **not** the proof for unbounded \(m\). The preceding recurrence, reciprocal-coefficient argument, Descartes count, and strict convexity furnish the infinite-parameter proof.

## Relationship to prior work
Pal and Prasad (arXiv:1812.03009) derive the continuous-time Brownian interval first-passage law and the limiting spatial criterion. Riascos et al. (arXiv:1910.13568), especially Section III, give an exact finite-ring spectral formula for the reset mean, including numerical efficiency illustrations; thus the pointwise mean formula itself is **not claimed as novel**. Lauber Bonomo and Pal (arXiv:2102.00895), Sections II.2 and III.1, provide the general small-reset variance criterion and confined discrete-walk first-passage generating functions. The present claim is the exact **all-reset-probability** finite-size sign classification, non-reentrance and strict distance nesting, obtained from a two-sign-change palindromic certificate and a strict convexity argument. These structural implications are not stated in the inspected primary texts, despite their formulas implying the underlying pointwise means.

## Limitations
Priority cannot be guaranteed by semantic retrieval: the finite-ring spectral theory is already well established, and an unlocated equivalent argument might exist. This claim establishes neither uniqueness of the *minimizing* reset rate nor a general stochastic-order comparison. It is restricted to unbiased nearest-neighbor cycles with fixed-root, update-consuming geometric resets. All claimed proof steps are mathematical deductions independent of numerical experiments. Independent expert review is not available here.

## References
1. A. Pal and V. V. Prasad, *First passage under stochastic resetting in an interval* (2018), arXiv:1812.03009, https://arxiv.org/html/1812.03009v2 (first public 2018-12-07).
2. A. P. Riascos, D. Boyer, P. Herringer and J. L. Mateos, *Random walks on networks with stochastic resetting* (2019), arXiv:1910.13568, https://arxiv.org/html/1910.13568v2 (first public 2019-10-29).
3. O. Lauber Bonomo and A. Pal, *First passage under restart for discrete space and time: application to one dimensional confined lattice random walks* (2021), arXiv:2102.00895, https://arxiv.org/html/2102.00895v1 (first public 2021-02-01).
