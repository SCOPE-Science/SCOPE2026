# A spectral Gumbel law for uniform-active collection on slowly switching stars

## Finding

For each integer \(n\ge2\), let a star have center \(o\) and \(n\) labeled leaves. Each spoke independently switches from OFF to ON at continuous-time rate \(a/n\) and from ON to OFF at rate \(b/n\), where \(a,b>0\) are fixed as \(n\to\infty\). Start all links independently in their stationary two-state distributions. At the event times of an independent rate-one Poisson clock, the center contacts one uniformly chosen leaf among the currently ON spokes; when none is ON, nothing happens. Repeated contacts are permitted. Let \(T_n\) be the time of first contact with every leaf.

Put
\[
\pi=\frac{a}{a+b},\quad c=\frac1\pi,\quad
\gamma=\frac{a+b+c-\sqrt{(a+b+c)^2-4ac}}2,\quad
\Gamma=\frac{a+b+c+\sqrt{(a+b+c)^2-4ac}}2,
\quad C=\frac{\Gamma-1}{\Gamma-\gamma}.
\]
Then \(0<\gamma<1<\Gamma\) and \(0<C<1\), and, with \(G\) a standard Gumbel random variable,
\[
\boxed{\frac{\gamma T_n}{n}-\log(nC)\ \xrightarrow{\mathrm d}\ G},
\qquad
\boxed{\mathbb E T_n=\frac n\gamma\bigl(\log n+\log C+\gamma_{\!E}\bigr)+o(n)},
\]
where \(\gamma_{\!E}\) is Euler's constant. In particular, \(T_n/(n\log n)\to1/\gamma\) in probability and in mean.

If the stationary ON fraction \(\pi\in(0,1)\) is fixed and the total switching-speed parameter \(s=a+b\) varies, then \(a=s\pi\), \(b=s(1-\pi)\), and the rate \(\gamma(s)\) is strictly increasing from zero to one. Thus finite persistence imposes the explicit multiplicative coverage penalty \(1/\gamma(s)>1\), despite an unchanged stationary ON fraction. These assertions use fixed positive parameters before the limit \(n\to\infty\).

## Assumptions and scope

The edge chains, their stationary initial states, and the independent hub clock are mutually independent. The rate-one hub clock operates even if no spoke is available. A leaf counts as covered on its first contact, but previously contacted leaves remain eligible for all subsequent choices. The communication graph is exactly a star, not an arbitrary edge-Markovian graph. Time is measured in the original continuous-time units. Every asymptotic statement is for fixed \(a,b\in(0,\infty)\).

## Proof

**1. Uniform concentration of available spokes.** Let \(M(t)\) be the number of ON spokes. Stationarity and edge independence give \(M(t)\sim\operatorname{Binomial}(n,\pi)\) for each deterministic \(t\). Fix any sufficiently large constant \(K\), set \(H_n=K n\log n\), and put \(\epsilon_n=n^{-1/3}\). At integer times \(j\le\lceil H_n\rceil\), Hoeffding's inequality bounds the chance of \(|M(j)/n-\pi|>\epsilon_n/2\) by \(2\exp(-n\epsilon_n^2/2)\). The number of link flips on any interval of length one is stochastically bounded by a Poisson variable of mean \(\max(a,b)\), because the total flip intensity never exceeds \(\max(a,b)\). A union bound over the integer intervals therefore yields an event \(\mathcal E_n\) with
\[
\Pr(\mathcal E_n^c)\le O(n\log n)e^{-\Omega(n^{1/3})},\qquad
\sup_{t\le H_n}|M(t)/n-\pi|\le\epsilon_n\quad\text{on }\mathcal E_n.
\]
The Poisson bound for more than \(n\epsilon_n/2\) flips on a unit interval is smaller than the displayed error. In particular, \(M(t)>0\) on \(\mathcal E_n\) for all sufficiently large \(n\).

**2. Independent upper and lower contact clocks.** For each leaf independently, construct a Poisson point process on \((t,u)\in[0,\infty)\times[0,\infty)\) of intensity \(dt\,du/n\), independent of all spoke chains. At time \(t\), select a leaf bearing a point with \(u\le n/M(t)\), provided its spoke is ON and \(M(t)>0\). The aggregate selection intensity is exactly one and the selected active leaf is uniform, so this construction has the required law. Let \(c_n^-=1/(\pi+\epsilon_n)\) and \(c_n^+=1/(\pi-\epsilon_n)\). On \(\mathcal E_n\) and up to time \(H_n\), a mark with \(u\le c_n^-\) is always accepted when its link is ON, and every accepted mark has \(u\le c_n^+\). For \(c'>0\), denote by \(Z_{i,n}^{c'}\) the first point of leaf \(i\) with \(u\le c'\) occurring while its own spoke is ON. Then \(Z_{i,n}^{c'}\) are independent and identically distributed over \(i\), and their maxima \(B_n^{c'}=\max_i Z_{i,n}^{c'}\) satisfy the truncated sandwich
\[
 B_n^{c_n^+}\wedge H_n\le T_n\wedge H_n\le B_n^{c_n^-}\wedge H_n
\quad\text{on }\mathcal E_n.
\]
This comparison holds pathwise using the *same* spoke and Poisson-point realizations, not a heuristic independence approximation.

**3. Exact one-link survival distribution.** On the rescaled clock \(x=t/n\), one spoke evolves from OFF to ON at rate \(a\) and back at rate \(b\), and is killed at rate \(c'\) while ON by the independent contact marks. Its transient generator, with states ordered OFF and ON, is
\[
Q_{c'}=\begin{pmatrix}-a&a\\b&-b-c'\end{pmatrix}.
\]
Writing \(\gamma_{c'}<\Gamma_{c'}\) for the two positive roots of
\[
z^2-(a+b+c')z+ac'=0,
\]
and \(A_{c'}=(\Gamma_{c'}-\pi c')/(\Gamma_{c'}-\gamma_{c'})\), the stationary-start survival probability is exactly
\[
S_{c'}(x)=(1-\pi,\pi)e^{xQ_{c'}}\binom11
=A_{c'}e^{-\gamma_{c'}x}+(1-A_{c'})e^{-\Gamma_{c'}x}.
\]
Indeed, the right side has value one and derivative \(-\pi c'\) at zero, and obeys the second-order equation with the characteristic polynomial just displayed. At \(c'=c=1/\pi\), the polynomial evaluated at one is \(1-c<0\); its roots therefore obey \(0<\gamma<1<\Gamma\), and the leading coefficient is precisely \(A_c=C\in(0,1)\). Thus for every \(c'>0\),
\[
\Pr(B_n^{c'}\le nx)=[1-S_{c'}(x)]^n\qquad(x\ge0).
\]

**4. Sharp Gumbel centering.** Set \(x_n(y)=(\log(nC)+y)/\gamma\) for fixed real \(y\). Since \(c_n^\pm=c+O(\epsilon_n)\), the roots and leading coefficients vary smoothly and \(\epsilon_n\log n\to0\), so
\[
 nS_{c_n^\pm}(x_n(y))\longrightarrow e^{-y},
 \qquad \Pr(B_n^{c_n^\pm}\le nx_n(y))\longrightarrow\exp(-e^{-y}).
\]
Take \(K>2/\gamma\). For fixed \(y\), the evaluation time \(nx_n(y)\) precedes \(H_n\) for large \(n\). Applying the pathwise sandwich and \(\Pr(\mathcal E_n^c)\to0\) gives the asserted Gumbel distributional limit.

**5. Expectation, including the order-\(n\) constant.** For \(c'\) in a compact neighborhood of \(c\), the positive two-exponential survival formula and tail integration of the maximum give, uniformly in that neighborhood,
\[
\mathbb E B_n^{c'}=\frac n{\gamma_{c'}}\bigl(\log(n A_{c'})+\gamma_{\!E}\bigr)+o(n).
\]
Uniformity follows either by integrating the explicit maximum distribution or by exponential tail bounds on both sides of its centering. Independently of \(\mathcal E_n\), any ON leaf has actual contact intensity \(1/M(t)\ge1/n\). Using the same marked Poisson processes gives \(T_n\le B_n^1\) on every realization. The two-exponential formula implies \(\mathbb E[(B_n^1)^2]=O(n^2\log^2 n)\). Choose \(K\) larger if necessary so that \(\Pr(B_n^1>H_n)=O(n^{-10})\); the same estimate holds for \(B_n^{c_n^\pm}\) with this \(K\). Cauchy–Schwarz and the exponentially small probability of \(\mathcal E_n^c\) make all removed exceptional and post-horizon contributions \(o(n)\). The expectation sandwich then applies to the full maxima. As \(\gamma_{c_n^\pm}-\gamma=O(\epsilon_n)\), \(A_{c_n^\pm}-C=O(\epsilon_n)\), and \(\epsilon_n\log n\to0\), both bounds yield the claimed expansion.

**6. Persistence penalty.** At fixed \(\pi\), write \(s=a+b\) and substitute \(a=s\pi\), \(b=s(1-\pi)\). The smaller root obeys
\[
\gamma(s)^2-(s+1/\pi)\gamma(s)+s=0,
\qquad \gamma'(s)=\frac{1-\gamma(s)}{s+1/\pi-2\gamma(s)}>0.
\]
The root formula gives \(\gamma(s)\sim s\pi\) as \(s\downarrow0\) and \(\gamma(s)\to1\) as \(s\to\infty\). These limits are statements about the coefficient after the fixed-parameter \(n\to\infty\) theorem; joint parameter-size limits are not asserted.

## Verification

Run `python checks/check_temporal.py` using Python 3 and its standard library. It reconstructs the killed-generator survival by an independent numerical ODE method, verifies the spectral polynomial and extreme-value distribution for several parameters, computes a separate exact finite-state continuous-time Markov generator, and simulates the original graph dynamics by Gillespie events. In the benchmark \(a=b=1,n=2\), the finite-state expected cover time is exactly \(268/45\); the independent simulation corroborates it. The delivered code reports 195 checks passed. Simulations and finite-state calculations are supporting diagnostics, not infinite-size proofs.

## Relationship to prior work

Cai, Sauerwald, and Zanetti (arXiv:2006.10589v1, first posted 2020-06-18) study random-walk mixing on edge-Markovian evolving graphs, motivating the slowly changing independent-link model; their main statements do not give a star hub's one-contact coverage Gumbel law or its spectral constant. Lamprou, Martin, and Spirakis (arXiv:1702.05412, first posted 2017-02-17) give bounds and a finite-state cover-time framework for walkers on evolving graphs. Their walker changes location and cannot simply be identified with the present center-only repeated-contact process. Athreya, Mukherjee, and Mukherjee (arXiv:2304.01145v1, posted 2023-04-03) prove Gumbel results for independent group coupon samples and study a different fixed-size subset-swap dependence; their sharp law has no independently flickering ON/OFF gates. Earlier edge-Markovian flooding bounds concern all-edge broadcast, not a hub making one uniform-active contact per unit time. These distinctions are about statement implication, not titles; no historical exhaustiveness or independent novelty certification is asserted.

## Limitations

The claim does not cover nonstationary link initialization, other update-time scales, simultaneous broadcast to every available leaf, contact strategies that avoid previously visited leaves, or arbitrary underlying graphs. Its full distributional and expectation formulas depend on fixed positive \(a,b\) and independent exponential edge switching. The O(n) term is an asymptotic statement, not a finite-size error bound. The literature comparison is not an exhaustive historical-priority search.

## References

1. L. Cai, T. Sauerwald, L. Zanetti, *Random walks on randomly evolving graphs*, arXiv:2006.10589v1 (2020-06-18), https://arxiv.org/abs/2006.10589.
2. I. Lamprou, R. Martin, P. Spirakis, *Cover Time in Edge-Uniform Stochastically-Evolving Graphs*, arXiv:1702.05412 (2017), https://arxiv.org/abs/1702.05412.
3. S. Athreya, S. Mukherjee, S. S. Mukherjee, *On a generalisation of the coupon collector problem*, arXiv:2304.01145v1 (2023-04-03), https://arxiv.org/abs/2304.01145.
4. A. E. F. Clementi, C. Macci, A. Monti, F. Pasquale, R. Silvestri, *Flooding Time of Edge-Markovian Evolving Graphs*, SIAM Journal on Discrete Mathematics 24 (2010), 1694–1712, https://doi.org/10.1137/090756053.
