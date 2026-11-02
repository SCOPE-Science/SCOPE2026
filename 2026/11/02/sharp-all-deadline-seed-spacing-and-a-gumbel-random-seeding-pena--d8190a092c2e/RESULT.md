# Sharp all-deadline seed spacing and a Gumbel random-seeding penalty for SI flooding on cycles

## Finding
On an undirected cycle \(C_N\), \(N\ge3\), put initially infected seeds at a nonempty fixed set \(S\) of \(k\) distinct vertices, and let each infected–susceptible edge transmit at independent exponential rate \(\lambda>0\). Infection is permanent; \(T_S\) is the first time all vertices are infected. If successive seeds enclose \(\ell_1,\dots,\ell_k\) initially healthy vertices, with \(\sum_i\ell_i=N-k\), then the **entire finite-time law**, for every \(t\ge0\), is
\[
\Pr(T_S\le t)=\prod_{i=1}^k Q_{\ell_i}(2\lambda t),\qquad Q_0(z)=1,\qquad Q_m(z)=1-e^{-z}\sum_{r=0}^{m-1}\frac{z^r}{r!}\quad(m\ge1).
\]
For every positive deadline \(t\), this probability is maximized precisely when the gap lengths differ by at most one; every other placement is strictly worse. The optimality therefore holds for the whole completion-time distribution in the usual stochastic order, not merely for its mean.

Now suppose \(k=k_N\to\infty\) and \(d_N=N/k_N\) obey \(d_N/(\log k_N)^2\to\infty\). If the seed set is uniformly drawn among all \(k_N\)-subsets and independent of the transmission clocks, then
\[
\Pr\!\left(\frac{2\lambda T_{\rm random}}{d_N}-\log k_N\le x\right)\longrightarrow \exp(-e^{-x})\qquad(x\in\mathbb R).
\]
By contrast, for every optimally balanced seed set,
\[
\frac{2\lambda T_{\rm balanced}}{d_N}\xrightarrow{\mathbb P}1,
\qquad
\frac{T_{\rm random}}{T_{\rm balanced}\log k_N}\xrightarrow{\mathbb P}1,
\]
where the ratio convergence holds for any coupling of the two experiments. Thus random initial spacing creates a multiplicative logarithmic flooding-time penalty.

## Assumptions and scope
The network is the simple undirected cycle on \(N\ge3\) vertices. One fixed set of \(1\le k\le N\) initially infected vertices is seeded simultaneously at time zero. Every susceptible vertex becomes permanently infected upon an infected neighbor's independent rate-\(\lambda\) contact; equivalently, each susceptible–infected edge carries an independent rate-\(\lambda\) exponential clock while it is active. The process is the continuous-time SI process with no recovery, spontaneous infection, or further seeding. Infection times for different gaps use disjoint edge clocks. The shape-zero Gamma variable is defined to be identically zero.

The finite-size identities and all-deadline optimization hold without any growth assumption. Only the asymptotic statements require \(k_N\to\infty\), \(d_N=N/k_N\), and \(d_N/(\log k_N)^2\to\infty\). Seed locations in the random case are sampled uniformly without replacement; no independence of cyclic gap lengths is assumed.

## Proof
**1. Independent gap clocks.** Order the initial seeds cyclically. A gap containing \(\ell\) uninfected vertices is bordered by infected endpoints (possibly the same seed when \(k=1\)). While at least one vertex in this gap is susceptible, exactly two edges cross the infected/susceptible boundary within the gap. This remains true after each infection because infection advances from an endpoint and never creates an interior island. By independence and exponential memorylessness, successive waiting times to the next infection in the gap are independent \(\operatorname{Exp}(2\lambda)\) variables. Consequently, its clearance time is \(\operatorname{Gamma}(\ell,2\lambda)\); gap clearance times are mutually independent since their edge-clock collections are disjoint. The last cleared gap determines \(T_S\), proving the displayed product formula.

**2. Strict stochastic balancing.** For \(z>0\), let \(p_m=e^{-z}z^m/m!\) be the rate-one Poisson mass and \(Q_m(z)=\Pr\{\operatorname{Poisson}(z)\ge m\}\). The identity
\[
\frac{Q_m(z)}{p_m}=\sum_{j=0}^\infty\frac{z^j}{(m+1)(m+2)\cdots(m+j)}
\]
uses an empty product of one. It decreases strictly with integer \(m\ge0\), so \(p_m/Q_m\) increases strictly. Since \(Q_{m+1}/Q_m=1-p_m/Q_m\), the successive ratios \(Q_{m+1}/Q_m\) strictly decrease: the sequence \(m\mapsto Q_m(z)\) is strictly log-concave, including the boundary \(m=0\). For integers \(a\ge b+2\),
\[
Q_{a-1}(z)Q_{b+1}(z)>Q_a(z)Q_b(z).
\]
Transferring one initially healthy vertex from a larger to a smaller gap therefore strictly increases the finite-time coverage CDF, simultaneously for every \(t>0\). Repeating such transfers reaches and only terminates at the balanced gap vectors with entries \(\lfloor(N-k)/k\rfloor\) or \(\lceil(N-k)/k\rceil\). Every nonbalanced vector admits a strict transfer. Any feasible gap vector corresponds to some seed set on the cycle. This proves the complete optimal-placement characterization; equivalence of different placements having the same gap multiset is intentional.

**3. Uniform random seed spacings and an exact formula.** Select a uniformly random \(k\)-element subset of the \(N\) vertices and select a uniform marked seed from it. Reading clockwise gaps from this marked seed makes \((\ell_1,\ldots,\ell_k)\) uniform over the \(\binom{N-1}{k-1}\) weak compositions of \(N-k\) into \(k\) parts. Indeed, each composition has exactly \(N\) rooted realizations, and \(N\binom{N-1}{k-1}=k\binom Nk\). Hence the exact random-seeding CDF is
\[
\Pr(T_{\rm random}\le t)=\frac{[u^{N-k}]\left(\sum_{m=0}^{N-k}Q_m(2\lambda t)u^m\right)^k}{\binom{N-1}{k-1}}.
\]
Let \(M_N=\max_i\ell_i\). Inclusion–exclusion on weak compositions gives, for any integer \(m\ge1\),
\[
\Pr(M_N<m)=\sum_{j=0}^{k}(-1)^j\binom kj\frac{\binom{N-jm-1}{k-1}}{\binom{N-1}{k-1}},
\]
with a binomial coefficient interpreted as zero if its upper argument is smaller than its nonnegative lower argument. This formula is exact, including finite \(N\) and \(k=1\).

**4. Sharp random-spacing extreme value.** Fix real \(x\), put \(m_N=\lfloor d_N(\log k_N+x)\rfloor+1\), and count \(Z_N=\sum_i\mathbf1\{\ell_i\ge m_N\}\). For each fixed positive integer \(j\), the uniform-composition representation yields
\[
\mathbb E(Z_N)_j=(k_N)_j\frac{\binom{N-jm_N-1}{k_N-1}}{\binom{N-1}{k_N-1}}.
\]
The ratio is \(\prod_{r=0}^{k_N-2}(1-jm_N/(N-1-r))\). Under \(k_N\to\infty\) and \(d_N/(\log k_N)^2\to\infty\), logarithmic expansion shows that this ratio equals \(k_N^{-j}e^{-jx+o(1)}\): its linear term tends to \(-j(\log k_N+x)\), and the quadratic error is \(O(j^2(\log k_N)^2/k_N)=o(1)\), with rounding error \(O(1/d_N)\). Thus every fixed factorial moment of \(Z_N\) tends to that of \(\operatorname{Poisson}(e^{-x})\), proving
\[
\Pr(M_N/d_N-\log k_N\le x)=\Pr(Z_N=0)\longrightarrow e^{-e^{-x}}.
\]
In particular \(M_N=O_{\mathbb P}(d_N\log k_N)\).

**5. Transfer to infection time.** Conditional on all gaps, let \(H_{i,N}=2\lambda\,G_{i,N}\) denote the scaled gap clearance time, with \(G_{i,N}\sim\operatorname{Gamma}(\ell_i,2\lambda)\). Then \(H_{i,N}\) is a sum of \(\ell_i\) independent unit exponentials, and \(\mathbb EH_{i,N}=\ell_i\). On the high-probability event \(M_N\le 2d_N\log k_N\), elementary exponential-sum Chernoff bounds give, for fixed \(\varepsilon>0\) and a constant \(c_\varepsilon>0\),
\[
\Pr\bigl(\max_i|H_{i,N}-\ell_i|>\varepsilon d_N\mid(\ell_i)_i\bigr)
\le2k_N\exp\left(-c_\varepsilon\frac{d_N}{\log k_N}\right)=o(1),
\]
because \(d_N/(\log k_N)^2\to\infty\). Therefore \(|2\lambda T_{\rm random}-M_N|/d_N\to0\) in probability and the asserted Gumbel limit follows by Slutsky's theorem.

For a balanced placement, each gap length equals \(d_N+O(1)\) (with \(d_N=N/k_N\) and \(k_N\to\infty\)); the same union bound proves \(\max_i|H_{i,N}-\ell_i|/d_N\to0\), whence \(2\lambda T_{\rm balanced}/d_N\to1\). Meanwhile the random limit implies \(2\lambda T_{\rm random}/(d_N\log k_N)\to1\). Since both converge in probability to constants, their ratio converges to one under any coupling, completing the proof.

## Verification
A standalone Python checker (`check_cycle.py`, Python 3 plus `mpmath`) performs three independent finite calculations: rational-valued Laplace transforms of the complete SI continuous-time Markov chain on all infected subsets for cycles through nine vertices, matched against the independently derived product-of-Gamma maximum law; comparisons of the balanced seed configuration against every seed subset for cycles through eleven vertices at several positive deadlines; and direct exact counting of all cyclic gap configurations versus the inclusion–exclusion formula for cycles through twelve vertices. The checker completed 15,742 successful deterministic assertions. These finite checks test algebraic identities and boundary conditions; they do not certify the infinite asymptotic theorem, which is proved analytically above.

## Relationship to prior work
Leskelä and Ngo [1] analyze exponential first-passage/flooding times on random sparse configuration graphs with limiting minimum degree at least three, principally with one source. Their main theorem does not apply to deterministic degree-two cycles with chosen simultaneous multiple sources, and does not supply the deadline-wise seed placement or discrete random-seed comparison. Jankowski and collaborators [2] study sequential versus simultaneous **activation placement** for a discrete independent-cascade model, focusing on eventual coverage, not continuous-time exact completion-time distributions on cycles. Schlemm [3] proves the classical Gumbel law for maximum **continuous** uniform circular spacings; that Gumbel phenomenon is prior literature, not a novelty claim here. The distinctive combined claim is the SI gap-clearance identity, sharp all-deadline balancing on a discrete cycle, and transfer of extreme discrete seed gaps to a quantitative infection-time penalty. Broader first-passage-percolation and graph-spreading literature may contain a prior equivalent statement; historical priority is not independently certified.

## Limitations
All results are restricted to the continuous-time permanent-infection SI process with independent equal-rate exponential edge transmissions on undirected simple cycles. They do not cover general graphs, recovery, heterogeneity, nonexponential transmission, adaptive seeding, or arbitrary numbers of seeds near full occupancy in the stated asymptotic limit. The random-seeding Gumbel theorem assumes \(d_N/(\log k_N)^2\to\infty\); no claim is made about its optimal necessity or other sparse/dense regimes. The result has not undergone independent mathematical audit.

## References
1. L. Leskelä and H. Ngo, *First passage percolation in sparse random graphs with boundary weights*, first public June 25, 2018, arXiv:1806.09568, https://arxiv.org/abs/1806.09568.
2. J. Jankowski, B. K. Szymanski, P. Kazienko, R. Michalski, and P. Bródka, *Probing Limits of Information Spread with Sequential Seeding*, first public September 18, 2018, arXiv:1809.06656, https://arxiv.org/abs/1809.06656.
3. E. Schlemm, *Limiting distribution of the maximal distance between random points on a circle: A moments approach*, first public May 23, 2014, arXiv:1405.6114, https://arxiv.org/abs/1405.6114.
