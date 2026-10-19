# Selection intensity strictly orders stationary polarization in balanced nonlinear public-goods games

## Finding

**Theorem (strict finite-population polarization ordering).** Fix integers \(N\ge3\) and \(2\le n\le N-1\), contribution cost \(c>0\), exploration probability \(0<\mu<1\), and positive single- and all-contributor multipliers \(r_1,r_n>0\) on the **balance surface**
\[
r_n=\frac{n(N-1)}{N-n}.
\]
Consider the nonlinear \(n\)-person public-goods game, sampled uniformly without replacement from \(N\) players, with the payoff and Fermi imitation/exploration rules defined below. Let \(\pi_w\) be its unique stationary distribution of the number \(X_w\) of cooperators at selection intensity \(w\ge0\), and write \(D_w=|2X_w-N|\).

For any \(w_2>w_1\ge0\), when \(r_n>r_1\) (economies of scale), the law of \(D_{w_2}\) **strictly dominates** that of \(D_{w_1}\) in monotone likelihood-ratio order: for every pair of attainable deviations \(d_2>d_1\),
\[
\frac{\Pr(D_{w_2}=d_2)}{\Pr(D_{w_1}=d_2)}
>
\frac{\Pr(D_{w_2}=d_1)}{\Pr(D_{w_1}=d_1)}.
\]
For \(r_n<r_1\) (diminishing returns), this strict inequality is reversed. For \(r_n=r_1\), the stationary distribution is independent of \(w\). In every case, \(\pi_w(i)=\pi_w(N-i)\), and \(\mathbb E[X_w]=N/2\). Hence the stationary variance strictly **increases** with \(w\) under economies of scale and strictly **decreases** under diminishing returns; the stationary mean heterozygosity \(\mathbb E[X_w(N-X_w)]\) varies in the opposite direction. The statement is valid at **every** positive exploration rate and for **all** finite pairs of selection intensities, not only in weak-selection limits.

## Assumptions and scope

For a group with \(k\) contributors, set the common benefit per member to
\[
B(k)=\frac{ck}{n}r(k),\qquad
r(k)=r_1+\frac{k-1}{n-1}(r_n-r_1)\quad(1\le k\le n),\qquad B(0)=0.
\]
A cooperator receives \(B(k)-c\) and a defector receives \(B(k)\). When there are \(i\in\{1,\ldots,N-1\}\) cooperators, the conditional expected payoffs \(u_C(i)\) and \(u_D(i)\) average independent uniform samples of \(n-1\) distinct co-players from the other \(N-1\) players; write \(\Delta_i=u_C(i)-u_D(i)\).

Write \(\sigma(z)=(1+e^{-z})^{-1}\). For every \(i\in\{0,\ldots,N\}\), use the discrete-time birth-death transition probabilities
\[
q_i^+(w)=(1-\mu)\frac{i(N-i)}{N^2}\sigma(w\Delta_i)+\mu\frac{N-i}{N},
\qquad
q_i^-(w)=(1-\mu)\frac{i(N-i)}{N^2}\sigma(-w\Delta_i)+\mu\frac{i}{N},
\]
where imitation terms vanish at \(i=0,N\) and \(q_i^0=1-q_i^+-q_i^-\). The imitation event samples focal and model individuals independently with replacement. Conditional on selecting exploration (probability \(\mu\)), the focal individual flips strategy; this is **uniform exploration**, not fitness-dependent mutation. The ordinary expected-payoff rule is used, not independently realized noisy payoffs. Positive exploration makes every neighboring transition possible, including at the boundary; therefore the chain is irreducible and has a unique positive stationary distribution.

The allowed values of \(r_1\) at fixed balanced \(r_n\) are any positive values. The result makes no statements for \(\mu=0\), \(\mu=1\), \(n=N\), asymmetric payoff structures, Moran reproduction, or nonlinear payoff-to-fitness comparisons other than the specified Fermi rule.

## Proof

**1. Hypergeometric payoff reduction.** Let \(K\) be the number of cooperative co-players of a focal individual, whose other \(N-1\) population members contain \(S\) cooperators. Drawing \(n-1\) co-players gives
\[
\mathbb E K=\frac{(n-1)S}{N-1},\qquad
\mathbb E[K(K-1)]=\frac{(n-1)(n-2)S(S-1)}{(N-1)(N-2)}.
\]
Because \(B(k)=\frac c n\big[r_1k+(r_n-r_1)k(k-1)/(n-1)\big]\), the cooperator sees \(S=i-1\) and payoff \(\mathbb E[B(K+1)]-c\), whereas the defector sees \(S=i\) and payoff \(\mathbb E[B(K)]\). Substituting both factorial moments and cancelling terms yields, with no asymptotic approximation,
\[
\Delta_i=c\left[\frac{N-n}{n(N-1)}
\left(r_1+\frac{2(i-1)}{N-2}(r_n-r_1)\right)-1\right].
\]
The balance equation \(r_n=n(N-1)/(N-n)\) simplifies this to
\[
\Delta_i=\kappa(2i-N),\qquad
\kappa=\frac{c(N-n)(r_n-r_1)}{n(N-1)(N-2)}.
\]
All denominators are nonzero in the stipulated integer range. In particular, \(\kappa\) has the sign of \(r_n-r_1\), and \(\Delta_{N-i}=-\Delta_i\).

**2. Symmetry and detailed balance.** The identity \(\sigma(-z)=1-\sigma(z)\) and the reflected payoff difference imply \(q_{N-i}^+(w)=q_i^-(w)\). Therefore reflection \(i\mapsto N-i\) leaves the finite irreducible transition matrix invariant. Uniqueness gives \(\pi_w(i)=\pi_w(N-i)\), and in particular \(\mathbb E[X_w]=N/2\). The birth-death chain is reversible: its stationary law is determined by
\[
\frac{\pi_w(i+1)}{\pi_w(i)}=
\frac{q_i^+(w)}{q_{i+1}^-(w)}\qquad(0\le i<N),
\]
with positive normalizing constant. These equations are also valid for the two boundary edges because the exploration contributions remain positive.

**3. Strict likelihood-ratio comparison.** Suppose \(\kappa>0\). For each edge \(i\to i+1\) wholly on the upper half of the state space (\(i\ge\lceil N/2\rceil\)), the payoff difference at its lower endpoint obeys \(\Delta_i\ge0\), and at the upper endpoint \(\Delta_{i+1}>0\). Hence \(q_i^+(w)\) is nondecreasing in \(w\), while \(q_{i+1}^-(w)\) is strictly decreasing. At an upper boundary edge, \(q_N^-=\mu\) is independent of \(w\), but \(q_{N-1}^+\) is strictly increasing because \(N-1>N/2\) for \(N\ge3\). Thus **every** consecutive upper-half stationary ratio \(\pi_w(i+1)/\pi_w(i)\) is strictly increasing in \(w\), including the one adjoining the center when \(N\) is even. If \(N\) is odd, the central edge joins the two equally distant states and has ratio one by symmetry; it is deliberately excluded from comparisons of distinct deviations.

Let \(d=|2i-N|\) range over the attainable deviations. Their stationary masses are \(m_w(d)=\pi_w(N/2)\) when \(N\) is even and \(d=0\), and \(m_w(d)=2\pi_w((N+d)/2)\) otherwise. The multiplicity of each deviation does not depend on \(w\). It follows from the upper-half edge comparisons that for every successive attainable deviations \(d<d'\),
\[
\frac{m_{w_2}(d')}{m_{w_2}(d)}>
\frac{m_{w_1}(d')}{m_{w_1}(d)}
\quad\text{whenever }w_2>w_1.
\]
Multiplying consecutive comparisons gives the claimed strict likelihood-ratio inequalities for every pair \(d_2>d_1\). As the two probability mass functions are normalized and positive, a strictly increasing likelihood ratio must cross one once, yielding strict first-order dominance for every proper upper tail. This also strictly increases the expectation of every nonconstant increasing function of \(D\). If \(\kappa<0\), all derivative signs reverse, and the same proof gives strict reverse likelihood-ratio order. If \(\kappa=0\), all imitation probabilities equal \(1/2\), independently of \(w\).

**4. Observables.** Since \(\mathbb E[X_w]=N/2\),
\[
\operatorname{Var}(X_w)=\frac{\mathbb E[D_w^2]}4,\qquad
\mathbb E[X_w(N-X_w)]=\frac{N^2-\mathbb E[D_w^2]}4.
\]
The strict stochastic comparisons yield all variance and heterozygosity assertions.

**5. Exact illustrative witness.** For \((N,n,c,\mu,r_n)=(4,3,1,1/5,9)\), take either \(r_1=3\) (economies of scale) or \(r_1=15\) (diminishing returns), so \(\kappa=\pm1/3\). The zero-intensity law in both cases is
\[
\pi_0=\left(\frac17,\frac8{35},\frac9{35},\frac8{35},\frac17\right),\qquad\operatorname{Var}_0(X)=\frac85.
\]
At \(w=3\log 2\), the economies-of-scale law is
\[
\pi_w=\left(\frac{17}{92},\frac5{23},\frac9{46},\frac5{23},\frac{17}{92}\right),\qquad\operatorname{Var}_w(X)=\frac{44}{23}>\frac85,
\]
and the diminishing-returns law is
\[
\pi_w=\left(\frac8{83},\frac{20}{83},\frac{27}{83},\frac{20}{83},\frac8{83}\right),\qquad\operatorname{Var}_w(X)=\frac{104}{83}<\frac85.
\]
All fractions follow directly from the same detailed-balance equations.

## Verification

Run `python3 verify_stationary.py` with Python 3; the standalone checker uses standard-library exact `fractions.Fraction` and `math.comb`, with no external data or dependencies. It derives the two focal payoffs independently by exhaustive hypergeometric sums, checks the analytical gap, computes the full stationary law by detailed balance and tests stationarity, symmetry, stochastic transition bounds, and the strict likelihood-ratio/tail comparisons at exactly rational logistic factors. It tests \(3\le N\le13\), \(2\le n<N\), three return regimes, three exploration probabilities, and four intensities parameterized by exact exponential factors. The observed output is: 3432 payoff identities; 2376 stationary-distribution checks; 14139 ordering/equality checks, all passed. These finite checks do not substitute for the preceding all-parameter proof.

## Relationship to prior work

Hauert and McAvoy (2024), *Frequency-dependent returns in nonlinear public goods games*, introduce the linearly contributor-dependent multiplier (their Eq. 5), derive finite-population expected payoffs, and specify Fermi pairwise comparisons and uniform mutation/exploration (their Eqs. 9, 12–13). Their dynamical and finite-population investigations motivate the problem. The result here isolates the precisely balanced cost/return surface and establishes a strict **all-intensity, all-mutation-rate stochastic ordering of the entire finite stationary polarization distribution**, not merely the sign of an equilibrium drift or numerical modality plot.

General finite birth-death detailed balance and monotone likelihood-ratio arguments are classical; neither technique is claimed to be new. Sandholm (2010) studies stochastic stability and selection under large-population/small-noise limits of noisy best response, not the same exact finite-population Fermi/exploration family at fixed positive mutation. Ji and Wang (2011) study a generalized **Moran** model with fitness-dependent reproduction, not the specified Fermi comparison rule. Potential related general stochastic-comparison theorems could imply the final ordering once this payoff reduction is supplied; their applicability is a residual priority risk.

## Limitations

The balance equation is an exact codimension-one constraint; the theorem does **not** assert analogous strict polarization ordering for arbitrary return parameters. It compares equilibrium laws of the specified finite birth-death chain, not transient paths, fixation without exploration, modal counts, or empirical game outcomes. The results hold for fixed \(N,n,c,\mu,r_1,r_n\) while varying selection intensity. The source's original model is broader, and no claim of novelty is made for its definition, the general birth-death stationary product formula, or generic likelihood-ratio facts. Independently established publication priority has not been certified. All checks described here are analytical or reproducible exact finite computations; no outside scientific review is asserted.

## References

1. C. Hauert and A. McAvoy (2024), *Frequency-dependent returns in nonlinear public goods games*, Journal of the Royal Society Interface, DOI: 10.1098/rsif.2024.0334. First public preprint arXiv:2404.13728v1, 2024-04-21. https://arxiv.org/abs/2404.13728 ; full accessible text https://arxiv.org/pdf/2404.13728 .
2. W. H. Sandholm (2010), *Orders of limits for stationary distributions, stochastic dominance, and stochastic stability*, Theoretical Economics 5, 1–26, DOI: 10.3982/TE554. https://doi.org/10.3982/TE554 .
3. Q. Ji and X.-J. Wang (2011), *Evolutionary games in a generalized Moran process with arbitrary selection strength and mutation*, Chinese Physics B 20, 030203, DOI: 10.1088/1674-1056/20/3/030203. https://doi.org/10.1088/1674-1056/20/3/030203 .
