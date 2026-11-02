# Periodic leaching minimizes stationary salt mass: a renewal convex-risk law

## Finding

For constant salt deposition, fixed fractional salt removal per leaching event, and independent renewal intervals of a specified mean, regularly spaced events uniquely minimize the stationary **time-sampled mean salt mass**. This holds with or without continuous first-order salt uptake. Without uptake, the conclusion strengthens to *every increasing convex risk functional* of stationary salt mass; it does **not** strengthen to first-order stochastic dominance.

More precisely, fix deposition rate \(a>0\), pulse retention \(0<r<1\), mean interevent time \(\mu>0\), and continuous uptake rate \(b\ge0\). For positive i.i.d. intervals \(L\) of mean \(\mu\), let \(M_L\) denote the salt mass observed at a stationary uniformly sampled time. Let \(M_0\) denote its counterpart for intervals exactly \(\mu\), with stationary uniformly random phase.

If \(b>0\), write \(q=\mathbb E[e^{-bL}]\) and \(q_0=e^{-b\mu}\). Then

\[
\mathbb EM_L=\frac{a}{b}\left(1-\frac{(1-r)(1-q)}{b\mu(1-rq)}\right),
\qquad
\mathbb EM_L-\mathbb EM_0=\frac{a(1-r)^2(q-q_0)}{b^2\mu(1-rq)(1-rq_0)}.
\]

The difference is nonnegative, with equality **if and only if** \(L=\mu\) almost surely. If \(b=0\), with possibly infinite second moment,

\[
\mathbb EM_L=a\left(\frac{r\mu}{1-r}+\frac{\mathbb E L^2}{2\mu}\right),\quad
\mathbb EM_0=a\mu\left(\frac{r}{1-r}+\frac12\right),\quad
\mathbb EM_L-\mathbb EM_0=\frac{a\operatorname{Var}(L)}{2\mu},
\]

with extended nonnegative expectations if \(\mathbb E L^2=\infty\). Moreover, for every nondecreasing convex \(\phi:[0,\infty)\to\mathbb R\),

\[
\boxed{\mathbb E\phi(M_0)\le\mathbb E\phi(M_L)}
\]

in the extended-expectation sense. For a nondegenerate renewal law the inequality is strict for \(\phi(x)=x\) whenever \(\mathbb E L^2<\infty\), and the random model has infinite mean if that second moment is infinite. A convex increasing penalty need not be strictly improved for every \(\phi\), such as a constant penalty.

## Assumptions and scope

The soil root zone is represented by one nonnegative salt mass \(M(t)\). Between leaching events it obeys \(\dot M(t)=a-bM(t)\); at every event it jumps from \(M(t^-)\) to \(rM(t^-)\). There is no coupled soil-water, concentration, salinity-dependent hydraulic conductivity, random event efficiency, or dependence of event timing on mass. Interevent times are independent, identically distributed, and strictly positive, with finite mean \(\mu\). Their two-sided renewal process is taken in stationary equilibrium. Intervals and the deterministic pulse-retention factor are not conditioned on the salt state. The performance quantity is the stationary **calendar-time** distribution, not the event-sampled distribution.

For \(b=0\), the stationary mass is almost surely finite when \(\mathbb E L<\infty\), although its expectation can be infinite if \(\mathbb E L^2=\infty\). For \(b>0\), the stationary mass lies in \([0,a/b]\). The equality statement assumes \(a>0\) and \(0<r<1\); the degenerate cases \(a=0\), \(r=0\), and \(r=1\) are not asserted to have strict uniqueness. Results concern one-patch salt mass, not irrigation water use, yield, or an optimal-control policy under a water-budget constraint.

## Proof

**1. Existence and stationary renewal decomposition.** At pulse epochs, the post-pulse mass \(Y_n\) satisfies, for \(b>0\),

\[
Y_n=r\left(e^{-bL_n}Y_{n-1}+\frac{a}{b}(1-e^{-bL_n})\right).
\]

The random affine map contracts by at most \(r<1\), giving a unique stationary post-pulse state; \(Y_{n-1}\) is independent of the next interval \(L_n\). If \(b=0\), the recurrence is \(Y_n=r(Y_{n-1}+aL_n)\), and its unique stationary version is \(Y_n=a\sum_{j\ge0}r^{j+1}L_{n-j}\). This sum is finite almost surely because it has finite expectation \(ar\mu/(1-r)\).

For a stationary renewal process, the age \(A\) of the current interval has tail

\[
\mathbb P(A>t)=\frac{\mathbb E(L-t)_+}{\mu},\qquad t\ge0.
\]

It is independent of all completed past intervals and the post-pulse mass \(Y\) just before the current interval began. In particular, for \(b>0\), \(\mathbb E e^{-bA}=(1-q)/(b\mu)\), and at the sampled time \(M_L=a/b+(Y-a/b)e^{-bA}\).

**2. Uptake-positive exact mean and uniqueness.** Taking expectation in the event recurrence gives

\[
\mathbb EY=\frac{ra}{b}\frac{1-q}{1-rq}.
\]

Independence of \(Y,A\) and the renewal-age Laplace transform then yields the first displayed formula for \(\mathbb EM_L\). Subtracting its deterministic-interval counterpart gives the stated rational difference. Because \(u\mapsto e^{-bu}\) is strictly convex for \(b>0\), Jensen's inequality gives \(q\ge e^{-b\mu}=q_0\), with equality exactly for a degenerate interval law. The positive prefactor and denominators prove sharpness.

**3. No-uptake mean and increasing convex comparison.** For \(b=0\), the calendar-time representation simplifies to

\[
M_L\ \overset{d}=\ a\left(A+S\right),\quad
S=\sum_{j\ge1}r^jL_{-j},\quad
A\perp S,\quad\mathbb ES=\frac{r\mu}{1-r}.
\]

The backward intervals \(L_{-j}\) are independent copies of \(L\). Under deterministic intervals, \(M_0\overset d=a(U+\mathbb ES)\), where \(U\) is uniform on \([0,\mu]\). Since \(u\mapsto(u-t)_+\) is convex, Jensen gives

\[
\mathbb P(A>t)=\frac{\mathbb E(L-t)_+}{\mu}
\ge\frac{(\mu-t)_+}{\mu}=\mathbb P(U>t).
\]

Thus \(A\) first-order stochastically dominates \(U\). For every nondecreasing convex \(\phi\), first apply conditional Jensen to \(S\) given \(A\), and then stochastic monotonicity to \(A\):

\[
\mathbb E\phi(a(A+S))\ge
\mathbb E\phi(a(A+\mathbb ES))\ge
\mathbb E\phi(a(U+\mathbb ES)).
\]

Subtracting \(\phi(0)\) makes all terms nonnegative, justifying the same reasoning for unbounded \(\phi\) with infinite expectation by monotone approximation. The standard renewal-reward identity \(\mathbb EA=\mathbb E L^2/(2\mu)\) proves the exact mean and its variance-of-intervals penalty. It also proves strict uniqueness for the mean, including the infinite-second-moment case.

**4. Sharp limitation of a stronger ordering.** Take \(a=\mu=1\), \(r=1/2\), \(b=0\), and let \(L\) be \(1/2\) or \(3/2\), each with probability \(1/2\). The periodic stationary mass is uniform on \([1,2]\). In the random model, the event that the preceding four gaps are all \(1/2\) and the present age is below \(1/4\) has positive probability; on that event \(S\le9/16\) and \(M_L<13/16<1\). Conversely, four previous gaps all \(3/2\) and the present age above \(3/4\) have positive joint probability and force \(S\ge23/16\) and \(M_L>35/16>2\). Therefore the two distribution functions cross and no first-order stochastic dominance holds in either direction. Nonetheless the random calendar-time mean equals \(13/8\), exceeding the periodic mean \(3/2\) by \(1/8\).

**5. Optional variance certificate.** If \(b=0\) and \(\mathbb EL^3<\infty\), independence gives the additional exact stationary variance identity

\[
\operatorname{Var}(M_L)=a^2\left[
\frac{\mathbb EL^3}{3\mu}
-\left(\frac{\mathbb EL^2}{2\mu}\right)^2
+\frac{r^2\operatorname{Var}(L)}{1-r^2}
\right].
\]

The periodic value is \(a^2\mu^2/12\). No finite empirical calculation is used to justify these universal claims.

## Verification

The accompanying `CHECK.py` rederives the stationary renewal-reward moments for \(b=0\), symbolically checks the \(b>0\) rational mean and difference, and tests multiple exact-rational two-point laws. It additionally performs seeded time-integral Monte Carlo checks for four uptake settings. This checks algebra and implementation only; the infinite-dimensional statements follow from the proof above. Run `python CHECK.py` with Python 3 and SymPy installed. For \(a=\mu=1\), \(r=1/2\), and equal two-point gaps \(1/2,3/2\), the excess mean at \(b=0\) is exactly \(1/8\). At \(b=\log2\), the exact positive penalty is obtained by substituting \(q=3/(4\sqrt2)\) and \(q_0=1/2\) into the formula above.

## Relationship to prior work

Suweis et al. (2010) formulate root-zone salt accumulation with approximately constant deposition and rainfall-induced multiplicative leaching, but derive stationary distributions under Poisson forcing, not a universal comparison across fixed-mean renewal schedules. Mau, Feng and Porporato (2014) study multiplicative Poisson jump noise with exponentially distributed marks, moment equations and threshold crossings; their full text's assumptions do not imply the arbitrary-renewal deterministic-optimality and convex-risk statements. Mau and Porporato (2015) study deterministic coupled salinity–sodicity dynamics, a different state/control structure. Vico and Porporato (2010) address stochastic soil moisture in irrigation rather than the salt-mass ordering. The 2010 seasonal dry–wet sodicity work by van der Zee et al. has a related application but employs a different, coupled physicochemical model; its full text could not be obtained for a decisive exhaustive comparison. The contribution here is the explicit renewal law, its distribution-free sharp minimizer, and the precise distinction between convex risk and exceedance probabilities. Novelty is assessed relative to the inspected literature, not certified exhaustively.

## Limitations

The renewal intervals are i.i.d. and independent of the salt state; leaching efficiency is fixed and identical across schedules. Salt precipitation, salt transport with varying moisture, correlated meteorological events, irrigation costs, rainfall volumes and nonlinear uptake are not modeled. The all-convex-risk ordering is proved only for \(b=0\); when \(b>0\), the theorem claims only stationary-mean optimality. Mean optimality cannot justify lower probability at every fixed salinity threshold. Prior-art comparisons are based on the specifically inspected sources and remain subject to independent scholarly verification.

## References

1. S. Suweis et al., *Stochastic modeling of soil salinity*, Geophysical Research Letters **37**, L07404 (first published 7 April 2010), https://doi.org/10.1029/2010GL042495.
2. Y. Mau, X. Feng and A. Porporato, *Multiplicative jump processes and applications to leaching of salt and contaminants in the soil*, Physical Review E **90**, 052128 (2014), https://doi.org/10.1103/PhysRevE.90.052128. Author manuscript: https://yairmau.com/archive/papers/mau-2014-Multiplicative%20jump%20processes%20and%20applications%20to%20leaching%20of%20salt%20and%20contaminants%20in%20the%20soil.pdf.
3. Y. Mau and A. Porporato, *A dynamical system approach to soil salinity and sodicity*, Advances in Water Resources **83**, 68–76 (2015), https://doi.org/10.1016/j.advwatres.2015.05.010.
4. G. Vico and A. Porporato, *Traditional and microirrigation with stochastic soil moisture*, Water Resources Research **46**, W03509 (2010), https://doi.org/10.1029/2009WR008130.
5. S. E. A. T. M. van der Zee et al., *Soil sodicity as a result of periodical drought*, Agricultural Water Management **97**, 41–49 (2010), https://doi.org/10.1016/j.agwat.2009.08.009.
