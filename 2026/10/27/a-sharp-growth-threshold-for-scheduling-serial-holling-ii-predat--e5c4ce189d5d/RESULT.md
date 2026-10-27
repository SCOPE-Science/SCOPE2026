# A sharp growth threshold for scheduling serial Holling-II predator treatments

## Finding
Fix any integer \(m\ge2\). Under a finite sequence of non-overlapping predator treatments, prey density in treatment \(i\) follows
\[
\dot N=f_i(N)=rN-\frac{a_iN}{1+b_iN},\qquad b_i=a_i h_i,
\]
where \(r\ge0\), \(a_i,h_i>0\), and every treatment \(i\) lasts a fixed duration \(t_i>0\). Each treatment is used once; only chronological order changes. Assume the saturation coefficients are distinct, and relabel the treatments so that \(b_1<\cdots<b_m\). The initial density is any \(N_0>0\).

For every \(i<j\), set
\[
S_{ij}(x)=a_jb_j(1+b_ix)^2-a_ib_i(1+b_jx)^2,\quad
M_{ij}=\max\{0,\sup_{x>0}S_{ij}(x)\}.
\]
The extended nonnegative number \(M_{ij}\) is computable from a quadratic. Define
\[
R_{ij}=\frac{a_ia_j(b_j-b_i)}{M_{ij}},\qquad
R_*=\min_{i<j}R_{ij},
\]
with \(c/0=+\infty\) and \(c/(+\infty)=0\) for \(c>0\).

**Sharp universal-order theorem.** For every initial density and every choice of positive treatment durations, chronological order \((1,2,\dots,m)\) minimizes terminal prey density and the reverse order maximizes it **if and only if** \(0\le r\le R_*\). Here “if and only if” means that when \(r>R_*\), at least one choice of initial density and positive durations defeats the ascending order; it does not assert that the descending order is optimal above threshold.

At \(r=0\), ascending saturation order is always optimal. Positive prey growth can destroy this universal scheduling law, even when both treatments cause net prey decline throughout the density interval used in a comparison. The threshold is exact, not merely sufficient.

## Assumptions and scope
The model treats prey as one homogeneous well-mixed population; intrinsic per-capita birth rate \(r\) is common to every stage. The effective attack coefficient \(a_i\) incorporates a constant predator density, and \(h_i\) is the handling-time parameter of the Holling-II intake relation. The predator density, model coefficients, and treatment durations remain fixed within each phase. There is no prey carrying-capacity term, predator reproduction, predator interference, or switching cost. All treatments are finite and contiguous without overlapping predator types; changing the order does not change the amount of time allotted to any predator type. Solutions exist globally forward in time because \(\dot N\le rN\) for \(N>0\) and cannot cross zero. Their phase maps are strictly increasing in initial density by ODE uniqueness.

The condition that \(b_i\) be distinct is material: under positive growth, equal saturation coefficients but different attack coefficients do not generally define commuting flows. No tie-ordering claim is made.

## Proof
Write \(\Phi_i^t(x)\) for the flow under \(f_i\). The decisive exact two-phase commutator is the scalar Lie bracket
\[
W_{ij}(x)=f_i(x)f_j'(x)-f_j(x)f_i'(x)
=\frac{x^2\big[-a_ia_j(b_j-b_i)+rS_{ij}(x)\big]}{(1+b_ix)^2(1+b_jx)^2}.
\]
This follows by differentiation of \(f_i'(x)=r-a_i/(1+b_ix)^2\), expansion, and cancellation of all higher terms except those inside the displayed quadratic \(S_{ij}\). The denominator is positive for every \(x>0\).

We use the following scalar-flow comparison lemma. If two \(C^1\) vector fields \(f,g\) have positive forward solutions and \(W=fg'-gf'\le0\) everywhere on the positive half-line, then for every \(s,t\ge0\),
\[
\Psi_s(\Phi_t(x))\le\Phi_t(\Psi_s(x)),
\]
where \(\Phi,\Psi\) are the respective flows. To verify this without a backward-flow assumption, define
\[
Q_t(y)=(\partial_y\Phi_t(y))g(y)-g(\Phi_t(y)).
\]
Autonomous flow differentiation gives
\[
\partial_tQ_t=f'(\Phi_t)Q_t-W(\Phi_t),\qquad Q_0=0.
\]
Hence \(W\le0\) implies \(Q_t\ge0\). Compare \(u(s)=\Phi_t(\Psi_s(x))\), which satisfies \(u'=g(u)+Q_t(\Psi_s(x))\), with \(v(s)=\Psi_s(\Phi_t(x))\), satisfying \(v'=g(v)\). Scalar comparison yields \(u(s)\ge v(s)\), as required. Both flow maps are increasing, so a swap improvement is preserved by all subsequent stages.

For \(i<j\), the condition \(W_{ij}(x)\le0\) for every positive \(x\) is exactly
\[
r S_{ij}(x)\le a_ia_j(b_j-b_i)\quad\text{for every }x>0,
\]
which is equivalent to \(r\le R_{ij}\). If \(r\le R_*\), every inversion of ascending saturation order can be removed without increasing terminal prey. Repeated adjacent swaps give the global minimum, while reversing all such comparisons gives the global maximum.

For sharpness, suppose \(r>R_*\). Some \(i<j\) then have \(W_{ij}(x_0)>0\) at a positive density \(x_0\) (the definition of the supremum covers infinite, finite, and zero cases). The Taylor expansion for equal, sufficiently short durations \(\varepsilon>0\) is
\[
\Phi_j^\varepsilon(\Phi_i^\varepsilon(x_0))-
\Phi_i^\varepsilon(\Phi_j^\varepsilon(x_0))
=\varepsilon^2W_{ij}(x_0)+O(\varepsilon^3)>0.
\]
Thus placing the lower-saturation treatment first is now **worse** for that pair. If other phases exist, assign each a positive duration small enough that continuity retains this strict reversal after swapping the two chosen phases in the full schedule. Therefore ascending order cannot be a uniform minimizer beyond \(R_*\).

For explicit computation, the polynomial is
\[
S_{ij}(x)=\underbrace{(a_jb_j-a_ib_i)}_{s_0}
+\underbrace{2b_ib_j(a_j-a_i)}_{s_1}x
+\underbrace{b_ib_j(a_jb_i-a_ib_j)}_{s_2}x^2.
\]
If \(s_2>0\), or \(s_2=0<s_1\), its supremum is infinite. Otherwise its supremum is \(s_0\) unless \(s_2<0\) and \(-s_1/(2s_2)>0\), in which case it is the value at that vertex. Taking the positive part gives \(M_{ij}\). This is an exact elementary algorithm requiring no time integration.

## Verification
The standalone `verify.py` is Python-standard-library code. Executing `python3 verify.py` in a directory containing that file checks 1,500 independent rational evaluations of the exact Lie-bracket identity; 6,558 rational sign comparisons under the computed universal-order threshold; the exact finite-threshold and reversal examples below; and 25 exhaustive three-treatment permutation comparisons by fourth-order Runge–Kutta integration in the zero-growth limit. The finite computations check identities and examples, not the all-parameter theorem, which follows from the proof.

An exact finite threshold occurs at \((a_1,b_1,a_2,b_2)=(2,1/2,3,3/2)\): \(S(x)=7/2+(3/2)x-(9/8)x^2\), with unique maximum \(4\) at \(x=2/3\), so \(R_*=3/2\). At \(r=8/5\), the bracket is positive at \(x=2/3\), where \(W_{12}=1/40\), but negative at \(x=4\), where \(W_{12}=-32/45\). Therefore short-treatment order preferences reverse across initial stocks.

To show the reversal does not depend on population growth during an individual treatment, take \((a_1,b_1,a_2,b_2,r)=(2,1,4,2,4/5)\). For every \(0<x<1\), both \(f_1(x)\) and \(f_2(x)\) are negative. Nonetheless,
\[
W_{12}(x)=\frac{(16/5)x^2(2x-1)}{(1+x)^2(1+2x)^2}.
\]
Thus, as treatment durations decrease together, order \((1,2)\) leaves less prey at initial stock \(1/4\), but order \((2,1)\) leaves less prey at initial stock \(3/4\). The exact bracket values are \(-32/1125\) and \(288/6125\), respectively.

## Relationship to prior work
The Holling-II intake law and handling-time interpretation are classical; the full-text papers of Van der Meer and Smallegange (2008) and Heath et al. (2013) explain its mechanistic ecological role. Pei et al. (2005) treat multi-predator impulsive biological control and extinction/permanence. Wang et al. (2016) treat an impulsive food-web model with periodic controls and stability/bifurcation analysis. Those formulations, observables and objectives differ from the present finite-order permutation question. The full text of the first two accessible articles and the 2016 article was materially inspected. The full text of Pei et al. could not be retrieved, so implication by that source remains a residual risk.

General one-dimensional flow comparison and Lie-bracket reasoning are standard antecedents, not asserted as new. The specific all-population sharp growth threshold, its exact quadratic finite algorithm, and the demonstration that prey growth can reverse serial-treatment ranking even along declining trajectories are the mathematical claim. A published general rearrangement theorem explicitly characterizing this family might subsume it; historical priority is not certified.

## Limitations
No statement about empirical efficacy, stochastic populations, logistics, simultaneous predator releases, variable predator abundance, long-term pest eradication, or optimal control with switching costs follows. The threshold is for a universal ranking over **all** initial densities and duration assignments, not a necessary condition for a particular fixed experiment's optimal order. At or below threshold there may be ties at certain parameter-dependent stationary densities; uniqueness of the optimum is not asserted. The short-duration reverse-order construction beyond threshold does not establish that the reverse order wins at every duration.

## References
1. Pei, Y., Chen, L., Zhang, Q., and Li, C. (2005), *Extinction and permanence of one-prey multi-predators of Holling type II function response system with impulsive biological control*, Journal of Theoretical Biology, 235, 495–503. DOI: 10.1016/j.jtbi.2005.02.003. Initial online publication indexed 2005-04-29, OpenAlex W2084281749. Full text unavailable in this review.
2. Van der Meer, J. and Smallegange, I. M. (2009 issue; first online 2008-12-11), *A stochastic version of the Beddington–DeAngelis functional response: modelling interference for a finite number of predators*, Journal of Animal Ecology. DOI: 10.1111/j.1365-2656.2008.01480.x. Full HTML examined.
3. Heath, M. R., Speirs, D. C., Steele, J. H., and Lafferty, K. (first online 2013-10-27), *Understanding patterns and processes in models of trophic cascades*, Ecology Letters. DOI: 10.1111/ele.12200. PMCID: PMC4237542. Full HTML examined.
4. Wang, Z., Shao, Y., and Fang, X. et al. (2016), *An Impulsive Three-Species Model with Square Root Functional Response and Mutual Interference of Predator*, Discrete Dynamics in Nature and Society. DOI: 10.1155/2016/3897234. Full HTML examined.
