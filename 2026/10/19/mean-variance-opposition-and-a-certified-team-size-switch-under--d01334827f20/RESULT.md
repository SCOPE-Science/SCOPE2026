# Mean–variance opposition and a certified team-size switch under collective Brownian resetting

## Finding

For \(N\in\{7,8,9,10\}\) independent one-dimensional Brownian searchers, simultaneously reset to their common starting position at Poisson rate \(r\), consider the first time at which **any** searcher reaches the absorbing origin. Write \(F_N(r)\) for this random time. For every \(N\in\{7,8,9,10\}\), increasing \(r\) from zero **strictly increases** \(\mathbb E F_N(r)\). Yet for \(N=7,8,9\), the same small positive rate **strictly decreases** \(\operatorname{Var}F_N(r)\); for \(N=10\), it **strictly increases** that variance. For all four sizes the squared coefficient of variation decreases for sufficiently small positive rate. All signs are mathematically certified by exact-rational integral enclosures, not inferred from finite sampling.

In particular, there is a change of sign of the zero-rate variance sensitivity **between nine and ten searchers**, within the initial four integer counts beyond the known common-reset mean-optimality boundary. No classification of larger \(N\) is asserted.

## Assumptions and scope

Let \(N\in\{7,8,9,10\}\), \(D>0\), \(x_0>0\), and \(B_i\), \(1\le i\le N\), be independent standard Brownian motions. Between resets, particle \(i\) follows \(x_0+\sqrt{2D}B_i(t)\). At each time of an independent common Poisson clock of rate \(r\ge0\), every particle is **simultaneously** returned to \(x_0\) and resumes with independent fresh Brownian increments. The search stops at the first hit of zero by any particle. No delays or inter-particle interactions are included.

Scale the search time by \(4D/x_0^2\), writing \(T=(4D/x_0^2)F_N(r)\), and the resetting rate by \(\rho=r x_0^2/(4D)\). Define \(s_N(t)=\operatorname{erf}(t^{-1/2})^N\), and for \(j=0,1,2\), \(m_j(N)=\int_0^\infty t^j s_N(t)\,dt\). These integrals converge for all four sizes since \(s_N(t)=O(t^{-N/2})\) at infinity. Here \(m_j(N)\) denotes the moment integral, not the ordinary \(j\)-th moment of \(T\).

## Proof

**1. Renewal and sensitivities.** Without resetting, independence and reflection at the origin give \(\Pr(T>t)=s_N(t)\). Its Laplace transform is \(h(\rho)=\int_0^\infty e^{-\rho t}s_N(t)\,dt\). Splitting at the first common reset gives the survival-transform identity

\[
\widetilde s_{N,\rho}(z)=\frac{h(z+\rho)}{1-\rho h(z+\rho)}.
\]

Using the first two derivatives in \(z\), the mean and variance of the scaled first-arrival time are

\[
\mu_N(\rho)=\frac{h(\rho)}{1-\rho h(\rho)},\qquad
V_N(\rho)=\frac{-2h'(\rho)-h(\rho)^2}{(1-\rho h(\rho))^2}.
\]

Since \(m_2(N)<\infty\), differentiating at the right endpoint \(\rho=0\) is legitimate by dominated convergence. Straight differentiation yields

\[
\mu_N'(0)=m_0^2-m_1,\qquad
V_N'(0)=-2m_2+6m_0m_1-2m_0^3.
\]

The squared coefficient of variation \(C_N(\rho)=V_N(\rho)/\mu_N(\rho)^2\) obeys

\[
C_N'(0)=\frac{2(2m_1^2-m_0m_2)}{m_0^3}.
\]

Thus the signs reduce to three explicit combinations of positive one-dimensional integrals.

**2. Exact-rational certification.** Substitute \(u=t^{-1/2}\). Then

\[
m_j(N)=2\int_0^\infty u^{N-2j-3}\bigl[\operatorname{erf}(u)/u\bigr]^N\,du.
\]

The quotient \(E(u)=\operatorname{erf}(u)/u\) is positive and strictly decreasing, with \(E(0)=2/\sqrt\pi\). On \(0\le u\le4\), divide the range into 2000 equal rational cells. The integral over each cell is bounded below by the polynomial weight integral times \(E\) at its **right** endpoint and above by the same weight integral times \(E\) at its **left** endpoint. For every endpoint, the identity

\[
E(u)=\frac2{\sqrt\pi}\int_0^1e^{-u^2v^2}\,dv
\]

and the globally valid alternating Taylor bounds \(P_{71}(-z)\le e^{-z}\le P_{70}(-z)\) for \(z\ge0\) produce **rational** bounds. The factor \(2/\sqrt\pi\) is itself bounded by rational numbers using Machin's arctangent identity and alternating-series inequalities. On the tail \(u\ge4\), the inequalities \(\operatorname{erf}(4)\le\operatorname{erf}(u)\le1\) reduce the remaining integral to rational powers of four. Exact integer/fraction operations combine all bounds.

The supplied standalone program `certify_sensitivity.py`, with input sizes `7`, `8`, `9`, or `10`, asserts the strict signs using exact fractions. The four `certified_intervals_*.json` files report human-readable decimal **enclosures only**; the assertions in the program, not decimal rounding, determine the signs. Selected displayed enclosures for \(\mu_N'(0)\) and \(V_N'(0)\) are:

| \(N\) | Mean derivative enclosure | Variance derivative enclosure |
| --- | --- | --- |
| 7 | \([0.07770,0.09306]\) | \([-2.97232,-2.87064]\) |
| 8 | \([0.12503,0.13907]\) | \([-0.57840,-0.50057]\) |
| 9 | \([0.13655,0.14970]\) | \([-0.12376,-0.05950]\) |
| 10 | \([0.13634,0.14886]\) | \([0.00462,0.06012]\) |

For each of these four sizes, the certified enclosure of \(2m_1^2-m_0m_2\) is strictly negative. The positive conversion factors between \(\rho\) and \(r\), and between scaled and physical mean/variance, preserve all sign conclusions.

**3. Positive small-rate interval.** The first two moments are right-differentiable at zero. Every displayed derivative is strictly separated from zero, so its sign persists for a (possibly size-dependent) nonempty interval \(0<r<\varepsilon_N(D,x_0)\), completing the claimed local comparison.

## Verification

Execute `python certify_sensitivity.py 7`, and repeat for `8`, `9`, and `10`, with Python 3 standard library only. Each invocation constructs an exact rational interval enclosing all three \(m_j\), propagates it through the sensitivity polynomials, and checks required strict inequalities. The four supplied JSON reports were generated this way. The argument establishes all four signs for infinite continuous-time processes; no simulation-to-proof extrapolation is involved.

## Relationship to prior work

Biroli, Majumdar and Schehr (2023) introduce exactly this simultaneous-reset protocol, provide the common-reset renewal formula, and establish the mean-based transition: zero resetting minimizes the mean when the number of walkers is at least seven. Their published mean and renewal results are **premises**, not claimed discoveries. Reuveni (2016) obtains a generic unit coefficient of variation at a **nonzero mean-optimal restart rate**; it does not settle the present zero-rate, team-size-resolved fluctuation signs. General restart second-moment identities algebraically imply the above sensitivity expressions after specialization, but the certified contrary signs for the four consecutive sizes and the nine-to-ten variance switch require the Brownian moment comparison proved here.

## Limitations

The theorem covers only the four stated integers, infinitesimal positive common resetting, unbiased homogeneous one-dimensional Brownian motion, and a first-arrival target. It neither establishes a sharp global variance threshold for all team sizes nor says whether intermediate/large resetting rates reverse their effects. The general renewal equation predates this result, and a previously published equivalent evaluated Brownian specialization cannot be ruled out without independent priority review. No independent audit has been performed.

## References

- Marco Biroli, Satya N. Majumdar and Grégory Schehr, *Critical number of walkers for diffusive search processes with resetting*, arXiv:2303.18012 (first publicly posted 31 March 2023); Physical Review E 107, 064141 (2023).
- Shlomi Reuveni, *Optimal stochastic restart renders fluctuations in first passage times universal*, arXiv:1512.01600 (2015); Physical Review Letters 116, 170601 (2016).
- Sergey Belan, *Median and mode in first passage under restart*, arXiv:1906.05619 (2019); related discussion of fluctuation-focused restart objectives.
