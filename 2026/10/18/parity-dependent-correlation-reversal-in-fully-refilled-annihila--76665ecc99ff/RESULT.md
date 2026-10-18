# Parity-dependent correlation reversal in fully refilled annihilating complete graphs

## Finding
For every integer \(N\ge 2\) and rate \(r>0\), consider hard-core annihilating random walkers on the complete graph with \(N\) labeled sites and **edge-clock normalization**: each occupied site attempts a jump to each *other* site at rate one. A jump to an empty site moves the particle; a jump to an occupied site removes both particles. Independently, at rate \(r\), the whole configuration is reset to the fully occupied configuration. Let \(K\) be the stationary number of occupied sites.

Put \(m=\lfloor N/2\rfloor\), \(k_j=N-2j\), and \(a_j=k_j(k_j-1)\), for \(0\le j\le m\). Then \(a_m=0\), and the **complete stationary law** is
\[
\Pr(K=k_j)=p_j(r):=\frac{r}{r+a_j}\prod_{h=0}^{j-1}\frac{a_h}{r+a_h}, \quad 0\le j\le m.
\]
Conditional on \(K=k_j\), the occupied set is exactly uniform among all \(\binom{N}{k_j}\) subsets. Therefore any two distinct site indicators \(\eta_u,\eta_v\) have common covariance
\[
C_N(r)=\frac{1}{N(N-1)}\sum_{j=0}^{m}k_j(k_j-1)p_j(r)
-\left(\frac1N\sum_{j=0}^{m}k_jp_j(r)\right)^2.
\]
The covariance obeys the **parity-sensitive weak-reset and parity-insensitive fast-reset laws**
\[
\begin{array}{ll}
C_N(r)=\dfrac{r}{2(N-1)}+O_N(r^2), & N\text{ even},\quad r\downarrow0,\\[4pt]
C_N(r)\longrightarrow-\dfrac1{N^2}, & N\text{ odd},\quad r\downarrow0,\\[4pt]
C_N(r)=\dfrac2r+O_N(r^{-2}), & N\ge2,\quad r\to\infty.
\end{array}
\]
In particular **every odd \(N\ge3\) has at least one positive reset rate at which distinct-site covariance reverses from negative to positive**. The minimal odd system has
\[C_3(r)=\frac{2(r-2)}{(r+6)^2},\]
so its reversal is unique and occurs at \(r=2\). No uniqueness claim is made for general odd \(N\), and no all-rate sign claim is made for even \(N\).

## Assumptions and scope
All jump attempts, particle removals and resets are continuous-time independent Poisson events. The global refill resets *all* sites simultaneously, not independently. The particle number can only decrease by two between refills and preserves the parity of \(N\). Sites are distinguishable, walkers are indistinguishable, and no spontaneous births occur except global refills. The stationary measure is defined for strictly positive \(r\), and asymptotic limits hold for each *fixed* finite \(N\). The jump clock is one per directed pair of distinct sites; choosing unit total rate per walker requires time/rescaling and changes numerical critical rates.

## Proof
**1. Lumped reaction chain.** Given \(K=k\), there are exactly \(k(k-1)\) directed occupied-to-occupied jump attempts per unit time. Every such event removes two particles, so \(K\mapsto K-2\) at rate \(k(k-1)\). All occupied-to-empty jumps leave \(K\) unchanged. Before the next refill, \(K\) is precisely the pure-death chain on \(N,N-2,\ldots,N-2m\) with death rates \(a_j\).

**2. Stationary law.** At any stationary observation time, the age since the last global Poisson refill has the exponential law with rate \(r\), independently of the particle dynamics after that refill. At level \(k_j\), the competing clocks for reset and the next annihilation have rates \(r\) and \(a_j\). Starting from \(k_0=N\), reaching level \(k_j\) without reset has probability \(\prod_{h<j}a_h/(r+a_h)\), and terminating the current age before any further death has probability \(r/(r+a_j)\). This yields the displayed formula, including the terminal \(a_m=0\) case. The probabilities telescope to one. A reset from any configuration reaches full occupancy, and all states reachable from full form one finite irreducible recurrent communicating class (via the reset); hence the stationary distribution is unique. The labeled process and refill are invariant under all site permutations, so uniqueness forces conditional uniformity on each particle-count level.

**3. Exact covariance.** Conditional exchangeability gives \(\mathbb E[\eta_u\mid K]=K/N\) and \(\mathbb E[\eta_u\eta_v\mid K]=K(K-1)/(N(N-1))\) for \(u\ne v\). Averaging over the exact \(p_j\) gives the formula.

**4. Weak reset.** When \(r\downarrow0\), every product factor \(a_h/(r+a_h)\) with \(a_h>0\) tends to one; hence \(K\) converges to the terminal state \(0\) for even \(N\) and \(1\) for odd \(N\). For odd \(N\), the terminal state is uniformly a singleton, so the covariance limit is \(-1/N^2\). For even \(N\), for every nonterminal \(k_j>0\), \(p_j(r)=r/a_j+O_N(r^2)\). There are \(N/2\) such levels and \(k_j(k_j-1)/a_j=1\), hence \(\mathbb E[K(K-1)]=(N/2)r+O_N(r^2)\), while \(\mathbb E[K]=O_N(r)\). The covariance is \(r/[2(N-1)]+O_N(r^2)\).

**5. Fast reset.** As \(r\to\infty\), the chance of at least two annihilation events within one renewal age is \(O_N(r^{-2})\); the probabilities of \(K=N\) and \(K=N-2\) are \(1-N(N-1)/r+O_N(r^{-2})\) and \(N(N-1)/r+O_N(r^{-2})\). Writing vacancies as \(1-\eta\), any specified pair is vacant with probability \((N(N-1)/r)/\binom N2+O_N(r^{-2})=2/r+O_N(r^{-2})\), whereas both single-site vacancy means are \(O_N(r^{-1})\). Therefore the occupancy covariance (equal to vacancy covariance) is \(2/r+O_N(r^{-2})\). The exact rational formula is continuous on \(r>0\), proving the odd-size existence result by the intermediate-value theorem.

**6. Three sites.** With \(N=3\), the only count levels are \(3\) and \(1\), with probabilities \(r/(r+6)\) and \(6/(r+6)\). Substitution and simplification yield \(2(r-2)/(r+6)^2\).

## Verification
A standalone numerical checker (`verify_annihilation.py`) independently constructs the full \(2^N\)-state Markov generator, including occupied-to-empty hops and directed-pair annihilations, then solves its stationary linear system without using the pure-death reduction. For \(2\le N\le7\) and four positive rates it checked 1,008 state probabilities and 24 independent pair-covariance comparisons against the closed formulas. Execute `python verify_annihilation.py` with NumPy and SciPy. The proof of the infinite family is analytic; these finite checks cannot establish it by themselves.

## Relationship to prior work
Evans and Majumdar, *Diffusion with Stochastic Resetting* (arXiv:1102.2704, 2011), establish the classical Poisson renewal approach for a reset diffusive particle. Krapivsky and Ben-Naim, *Irreversible Reactions and Diffusive Escape: Stationary Properties* (arXiv:1503.04236, 2015), study annihilation and coalescence on an inhomogeneous one-dimensional half-line. Those works motivate renewal resetting and parity-preserving annihilation but do not derive a complete-graph, globally refilled particle-count law or pair-covariance parity reversal in the examined materials. The renewal principle itself is prior work; the explicit all-size particle-level solution, covariance and parity/fast-reset limits are the specific claimed result.

## Limitations
Only complete graphs, initially full global refills, symmetric unit-rate directed hopping and instantaneous pair annihilation are addressed. No general uniqueness of odd-rate zero crossings, even-size all-rate positive correlation, joint thermodynamic \(N,r\) scaling, multi-site higher-order association, or spatial lattice result is claimed. The bibliographic overlap check is necessarily incomplete: an unindexed equivalent result in finite-population annihilation with catastrophes or refill could subsume the formula. Independent validation has not been performed.

## References
- M. R. Evans and S. N. Majumdar, *Diffusion with Stochastic Resetting*, arXiv:1102.2704v1, first public 2011-02-14, https://arxiv.org/abs/1102.2704.
- P. L. Krapivsky and E. Ben-Naim, *Irreversible Reactions and Diffusive Escape: Stationary Properties*, arXiv:1503.04236v1, first public 2015-03-13, https://arxiv.org/abs/1503.04236.
