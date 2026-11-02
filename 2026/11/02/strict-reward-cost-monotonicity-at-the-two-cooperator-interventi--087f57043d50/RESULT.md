# Strict reward-cost monotonicity at the two-cooperator intervention threshold

## Finding

Consider the finite-population Fermi imitation process of Duong, Durbac, and Han with an institutional reward paid to each cooperator only when there are one or two cooperators. In a population of any integer size \(N\ge4\), with baseline cooperator-minus-defector payoff difference \(\delta<0\), selection intensity \(\beta>0\), and reward amount \(\theta\ge0\), let \(E_2(\theta)\) be the expected total institutional outlay before absorption, **starting from one cooperator and \(N-1\) defectors**. (The single cooperator represents a mutant introduced into an otherwise all-defector population; no further mutation occurs before absorption.) Then

\[
\boxed{E_2'(\theta)>0\quad\text{for all }\theta\ge0.}
\]

This is a rigorous all-population-size solution of the first threshold beyond one rewarded cooperator for the all-defector-start cost criterion. In particular, for a required limiting cooperation frequency \(0<\omega<1\) under the rare-mutation approximation, the unique least-cost nonnegative uniform per-cooperator reward is

\[
\boxed{\theta_{\mathrm{opt}}=\max\!\left\{0,\frac12\left[\frac1\beta\log\!\frac{\omega}{1-\omega}-(N-1)\delta\right]\right\}.}
\]

The cooperation constraint is the known fixation-probability condition; its combination with the new strict cost monotonicity establishes the optimality statement.

## Assumptions and scope

The states are \(j\in\{0,1,\ldots,N\}\), the number of cooperators, with absorbing \(0,N\). At an interior state, let \(h_j=j(N-j)/N^2\). The Markov transition probabilities are \(P_{j,j+1}=h_j p_j\), \(P_{j,j-1}=h_j(1-p_j)\), and \(P_{j,j}=1-h_j\), with

\[
p_j=\begin{cases}(1+e^{-\beta(\delta+\theta)})^{-1},&j=1,2,\\(1+e^{-\beta\delta})^{-1},&3\le j\le N-1.\end{cases}
\]

The institutional outlay on each visit to \(j\) is \(j\theta\) for \(j\le2\), otherwise zero. The criterion is total expected outlay up to the first absorption, starting at state \(1\). We assume \(N\ge4\), \(\beta>0\), \(\delta<0\), and \(\theta\ge0\). No claim is made for general initial states, higher reward thresholds, persistent mutation, or nonlinear state-dependent payoff differences.

## Proof

Write

\[
R=e^{-\beta\delta}>1,\quad r=e^{-\beta(\delta+\theta)}=Re^{-\beta\theta},\quad T=\sum_{k=0}^{N-3}R^k\ge1+R>2.
\]

For the birth-death chain, set \(\rho_0=1\) and \(\rho_j=\prod_{k=1}^j(1-p_k)/p_k\). Then \(\rho_1=r\), \(\rho_2=r^2\), and \(\rho_j=r^2R^{j-2}\) for \(j\ge2\). Define the scale function \(S_j=\sum_{h=0}^{j-1}\rho_h\), with \(S_0=0\), \(S_1=1\), and \(S_N=1+r+r^2T\). Solving the absorbing birth-death Green-function recurrence, including the unit source at the occupied state, gives the expected number of visits to state \(j\) starting at state \(1\):

\[
G_{1j}=\frac{S_N-S_j}{S_N h_jp_j\rho_j}.
\]

Indeed the expression is harmonic in the initial-state index away from \(j\), vanishes at both absorbing boundaries, and its generator has the required unit jump at \(j\). Consequently

\[
G_{11}=\frac{N^2(1+r)(1+rT)}{(N-1)(1+r+r^2T)},\qquad
G_{12}=\frac{N^2(1+r)T}{2(N-2)(1+r+r^2T)}.
\]

Thus the **exact** expected cost, not a large-population approximation, is

\[
E_2(\theta)=N^2\theta B(r),\qquad
B(r)=\frac{(1+r)\left[A(1+rT)+CT\right]}{1+r+Tr^2},\quad A=\frac1{N-1},\ C=\frac1{N-2}>A.
\]

It remains to establish that multiplying the expected occupation by reward amount cannot reverse the sign of the derivative. Write \(K=A+CT\), \(L=AT\), and \(D(r)=1+r+Tr^2\). Direct differentiation yields

\[
B'(r)=\frac{AT-2CT^2r-(A+C)T^2r^2}{D(r)^2},\qquad
E_2'(\theta)=N^2\left[B(r)-\beta\theta\,r B'(r)\right].
\]

If \(B'(r)\le0\), positivity is immediate. Suppose \(B'(r)>0\). Its explicit numerator implies

\[
0<r<\frac{A}{2CT}<\frac1{2T}.
\]

Moreover, using \(K-L=A+(C-A)T>0\),

\[
\frac{B'(r)}{B(r)}=\frac1{1+r}+\frac{L}{K+Lr}-\frac{1+2Tr}{1+r+Tr^2}<\frac1{1+r},
\]

because \((K+Lr)(1+2Tr)-L(1+r+Tr^2)=(K-L)+2KTr+LTr^2>0\).

Set \(z=\beta\theta=\log(R/r)\ge0\). The function \(u\mapsto u\log(R/u)\) is increasing on \((0,R/e)\). Since \(r<1/(2T)\le1/4<R/e\),

\[
zr<\frac{\log(2RT)}{2T}\le\frac{\log(2T^2)}{2T}<1.
\]

The last strict inequality holds for \(T\ge2\), since \(2T-\log(2T^2)\) is positive at \(T=2\) and has derivative \(2-2/T>0\) thereon. Hence

\[
0\le zr\frac{B'(r)}{B(r)}<\frac{zr}{1+r}<1,
\]

and therefore \(E_2'(\theta)>0\). This also covers \(\theta=0\), where \(E_2'(0)=N^2B(R)>0\). The cooperation-target corollary follows by taking the smallest nonnegative reward satisfying the known fixation-ratio constraint \(\beta[(N-1)\delta+2\theta]\ge\log(\omega/(1-\omega))\).

## Verification

Run `python3 check.py` with Python 3.10 or later. The program constructs the exact rational transition matrix, solves the absorbing-chain linear system independently of the closed formula, and compares all entries with the scale-function expression in 182 rational cases over \(4\le N\le10\). It also tests 10,000 random valid numerical configurations for derivative positivity and checks the inequalities used in the analytic positive-derivative case. Its output is `PASS: 182 exact-rational Green-kernel cases; 10000 positive-derivative numerical cases; analytic intermediate bounds.` The universal positivity statement is proved above, not inferred from these finite tests.

For the illustration \(N=4\), \(\beta=1\), \(\delta=-1\), \(\theta=1\), the exact expected outlay is \(16(7+5e)/(3(3+e))\approx19.2052179402\).

## Relationship to prior work

Duong, Durbac, and Han (2024), initially posted February 12, 2024, define the two-cooperator reward cost, derive its expression through tridiagonal inverses, and prove monotonicity only for the single-cooperator threshold; they treat larger thresholds numerically and explicitly identify an unresolved threshold-dependent monotonicity conjecture. The present theorem proves strict monotonicity at threshold two, for all finite population sizes \(N\ge4\), under the all-defector-start convention.

Han and Tran-Thanh (2018) introduce composition-dependent intervention and study its efficiency analytically and numerically, without an all-size two-cooperator cost-monotonicity theorem in the material inspected. Duong and Han (2021) and Duong, Durbac, and Han (2023) establish nonmonotone-cost regimes for full-investment and mixed-incentive models; those statements concern different incentive policies. The method here is a scale-function/Green-kernel reduction followed by a sharp derivative sign analysis, not merely the known closed cost expression or a finite-state numerical observation.

## Limitations

Strict monotonicity is shown only for expected cost when a single mutant cooperator is introduced into an all-defector population, under rare mutation, the uniform Fermi rule, two rewarded states, constant payoff disadvantage, and a finite population of size at least four. The equally likely initial-state mixture, arbitrary initial distributions, heterogeneous costs, stochastic mutation during the fixation excursion, and thresholds at least three are not settled. The proof does not establish a universal threshold boundary for all policies, and independent verification has not been conducted. Residual prior-art risk: an equivalent theorem may occur outside indexed publications or under a different Green-function formulation.

## References

1. M. H. Duong, C. M. Durbac, and T. A. Han, *Cost Optimisation of Individual-Based Institutional Reward Incentives for Promoting Cooperation in Finite Populations*, arXiv:2402.07663 (first posted 2024-02-12); *Bulletin of Mathematical Biology* 86, 115 (2024). https://arxiv.org/abs/2402.07663
2. T. A. Han and L. Tran-Thanh, *Cost-effective external interference for promoting the evolution of cooperation*, *Scientific Reports* 8, 15997 (2018). https://doi.org/10.1038/s41598-018-34435-2
3. M. H. Duong and T. A. Han, *Cost efficiency of institutional incentives for promoting cooperation in finite populations*, *Proceedings of the Royal Society A* 477, 20210568 (2021). https://doi.org/10.1098/rspa.2021.0568
4. M. H. Duong, C. M. Durbac, and T. A. Han, *Cost optimisation of hybrid institutional incentives for promoting cooperation in finite populations*, *Journal of Mathematical Biology* 87, 77 (2023). https://doi.org/10.1007/s00285-023-02011-6
