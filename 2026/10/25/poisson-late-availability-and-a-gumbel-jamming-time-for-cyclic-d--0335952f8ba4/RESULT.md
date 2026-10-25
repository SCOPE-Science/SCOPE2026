# Poisson late-availability and a Gumbel jamming time for cyclic dimer adsorption

## Finding
Consider continuous-time random sequential adsorption of dimers on the cycle of \(n\) vertices. Each of the \(n\) edges attempts deposition at rate one; a deposition succeeds exactly when its two endpoints are vacant, and accepted dimers never move or desorb. Let \(X_{n,e}(t)\) indicate that both endpoints of edge \(e\) remain vacant at time \(t\), let \(N_n(t)=\sum_e X_{n,e}(t)\), and let \(T_n\) be the final successful deposition time. Identify edge \(e\) with \(e/n\) on the unit circle.

**Theorem.** For any fixed real \(x\), as \(n\to\infty\), at the late time \(t_n(x)=\log n+x\), the spatial point process of still-available edges satisfies
\[
\Xi_n(x)=\sum_{e=0}^{n-1}X_{n,e}(t_n(x))\delta_{e/n}
\ \Longrightarrow\ \operatorname{PPP}(e^{-2-x}\,dy)
\]
on the unit circle. In particular, \(N_n(t_n(x))\) converges to a Poisson variable of mean \(e^{-2-x}\). Uniformly on every fixed bounded interval \(|x|\le L\), there is a finite constant \(C_L\) such that for all sufficiently large \(n\),
\[
d_{\mathrm{TV}}\!\left(\mathcal L(N_n(\log n+x)),\operatorname{Pois}(e^{-2-x})\right)
\le C_L\frac{\log n}{n}.
\]
Consequently,
\[
\Pr(T_n\le\log n+x)=\exp(-e^{-2-x})+O_L(\log n/n),
\]
and \(T_n-\log n+2\) converges in distribution to the standard Gumbel law with cumulative distribution function \(\exp(-e^{-z})\).

## Assumptions and scope
The cycle has \(n\ge3\) vertices, initially all vacant. Each edge carries an independent rate-one Poisson attempt process. Every successful attempt occupies its two endpoints permanently; unsuccessful attempts do not change the state. The jamming time is the last accepted deposition (a.s. finite). Convergence of point processes is weak convergence of finite point measures on the compact unit circle. The asymptotic error is uniform only for a bounded real-valued centering parameter \(x\).

## Proof
**1. First-clock representation and late availability.** Let \(\tau_e\) be the first arrival of the Poisson process assigned to edge \(e\); these variables are independent \(\operatorname{Exp}(1)\). Sorting these clocks and accepting an edge only when both endpoints are unoccupied gives exactly the original process. Indeed, once an edge is blocked it can never become available again, so later attempts on that edge cannot succeed.

On the infinite path, let \(u(t)\) denote the probability that the terminal vertex of a semi-infinite path is vacant at time \(t\). The only edge incident to the terminal vertex attempts for the first time during \((t,t+dt)\) with probability \(e^{-t}dt+o(dt)\). Conditional on its absence before that time, the vertex at its other end is vacant with probability \(u(t)\), by independence of the remaining half-line. Thus
\[
u'(t)=-e^{-t}u(t),\qquad u(0)=1,\qquad
u(t)=\exp(-(1-e^{-t})).
\]
For a specified interior edge to have both endpoints vacant at \(t\), its own first clock must exceed \(t\). Conditional on this event, the two half-lines obtained by removing the edge evolve independently. Hence the exact infinite-line vacant-pair probability is
\[
p_\infty(t)=e^{-t}u(t)^2
=\exp[-t-2(1-e^{-t})].
\]
This is the classical empty-interval probability for one-dimensional dimer adsorption, used here as an input to a late-time finite-cycle limit.

**2. Uniform spatial localization.** The accepted/rejected status of an edge is determined by its own first clock and earlier neighboring edge clocks, iterated backward in strictly decreasing clock order. Coupling a tagged edge to the dynamics on a finite edge neighborhood of radius \(R\) fails only if there is a strictly decreasing chain of first clocks of length at least \(R\) linking that edge to outside its neighborhood. There are at most \(2^{R+2}\) nearest-neighbor walks of the relevant length, and any specified sequence of \(R\) distinct independent continuous clocks has strictly decreasing order with probability \(1/R!\). Therefore a coupling error bound valid for all times is
\[
\varepsilon_R\le \frac{2^{R+2}}{R!}.
\]
Take \(R=\lceil4\log n\rceil\). For all sufficiently large \(n\), disjoint neighborhoods of radius \(R\) embed identically in the infinite path and in the cycle. The union probability of any discrepancy among the \(n\) tagged edges is at most \(n\varepsilon_R=o(n^{-k})\) for each fixed positive integer \(k\).

Write \(Y_{n,e}(t)\) for the vacant-pair indicator computed with only the clocks in the radius-\(R\) neighborhood of \(e\). Such indicators are independent when their centers are separated by more than \(2R+2\) cycle edges, and \(\Pr(Y_{n,e}(t)=1,\,Y_{n,f}(t)=1)\le e^{-2t}\) for distinct \(e,f\): availability of each edge implies that its own first clock exceeds \(t\). The one-point coupling gives
\[
\Pr(Y_{n,e}(t_n(x))=1)
=p_\infty(t_n(x))+O(\varepsilon_R)
=\frac{e^{-2-x}}{n}+O_L(n^{-2})+O(\varepsilon_R).
\]
In particular \(\lambda_n=\sum_e\Pr(Y_{n,e}(t_n(x))=1)=e^{-2-x}+O_L(n^{-1})\).

**3. Quantitative Poisson approximation.** Give each \(Y_{n,e}\) a dependency neighborhood of size at most \(4R+5\). The standard dependency-neighborhood Stein–Chen bound for sums of Bernoulli variables (Arratia–Goldstein–Gordon) controls total variation from \(\operatorname{Pois}(\lambda_n)\) by a constant times the two sums
\[
b_1=\sum_e\sum_{f\in B_e}\Pr(Y_{n,e}=1)\Pr(Y_{n,f}=1),
\qquad
b_2=\sum_e\sum_{f\in B_e\setminus\{e\}}\Pr(Y_{n,e}=Y_{n,f}=1).
\]
Both are \(O_L(R/n)\), using the one-point and two-point bounds above, while the conditional-dependence term vanishes by construction. Coupling back to the original process costs at most \(n\varepsilon_R\) in total variation. The total-variation distance between two Poisson laws is at most the absolute difference of their means. The claimed bound \(C_L\log n/n\) follows.

**4. Spatial Poisson limit.** For any fixed number \(k\) of distinct tagged edges, the joint availability probability is at most \(e^{-kt_n(x)}\) in the locally truncated process, because all \(k\) independent first clocks must exceed the observation time. There are only \(O_k(n^{k-1}R)\) ordered distinct \(k\)-tuples containing two edges within dependency range. Their total contribution to any mixed factorial moment is \(O_{k,L}(R/n)\). All remaining \(k\)-tuples are independent and have asymptotic probability \((e^{-2-x}/n)^k\). Counting these tuples in arbitrary disjoint arcs yields the mixed factorial moments of independent Poisson counts of means \(e^{-2-x}\) times arc length. Their convergence, together with bounded expected total count and the negligible global coupling error, proves the stated point-process convergence.

**5. Jamming.** Since available pairs can only disappear, the process has completed all successful depositions by time \(t\) if and only if \(N_n(t)=0\) (each still-available edge has an almost surely finite future attempt). The zero probability of the limiting Poisson variable gives the Gumbel formula and its stated uniform error.

## Verification
Run \(\texttt{python verify_cycle_jamming.py}\) with Python 3, NumPy, and SciPy. The program constructs the entire labeled occupancy-state Markov generator for seven cycle sizes and compares the exact finite-time available-pair expectation with its infinite-line benchmark. It also independently sorts edge first-arrival clocks in randomized trials, measuring the late-time jammed proportion and number of available edges. A recorded run passed 71 assertions; for \(n=256\) and \(n=1024\) the observed jammed fractions at \(t=\log n\) were respectively 0.87100 and 0.87714, versus the predicted \(\exp(-e^{-2})\approx0.87342\). These finite tests verify implementation and scaling consistency; the infinite-volume theorem and error estimate rely on the proof above, not on simulation.

## Relationship to prior work
The exact one-dimensional vacant-pair probability and infinite-lattice jamming density are established classical results (Flory; reviewed by Turban). Penrose and Sudbury study graph-based dimer adsorption and finite-time normal approximations of occupied-site counts; their graphical approach supplies relevant established stabilization techniques. Purvis, Reeve, Wattis and Mao analyze near-jamming availability and its relationship to surface coverage, including one-dimensional deposition. Turban derives covering-time extreme-value laws on the **fully connected** lattice, where the geometry and timescales differ. None of those inspected treatments evaluates the joint *late-time spatial rare-event Poisson law*, its \(O(\log n/n)\) rate, and the consequent cyclic-graph Gumbel jamming law as stated here. The Stein–Chen inequality is standard prior methodology, not a new lemma. This comparison is relative to the identified, materially inspected texts; an unlocated specialist late-time theorem or a more general existing stabilization result could cover the claim.

## Limitations
The result is for one-dimensional periodic geometry, identical unit-rate dimer deposition attempts, and observation windows centered at \(\log n\). It does not establish a limiting process jointly in multiple times, an exact finite-size jamming-time distribution, or extensions to general graphs, unequal edge attempt rates, or longer adsorbates. Historical priority has not been independently certified.

## References
1. M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, 2005, arXiv:math/0503519, https://arxiv.org/abs/math/0503519 .
2. B. E. Purvis, L. Reeve, J. A. D. Wattis, and Y. Mao, *Scaling behavior near jamming in random sequential adsorption*, Physical Review E 91, 022118 (2015), https://doi.org/10.1103/PhysRevE.91.022118 .
3. L. Turban, *Random sequential adsorption of k-mers on the fully-connected lattice: probability distributions of the covering time and extreme value statistics*, 2019, arXiv:1908.00940, https://arxiv.org/abs/1908.00940 .
4. R. Arratia, L. Goldstein, and L. Gordon, *Two moments suffice for Poisson approximations: the Chen–Stein method*, Annals of Probability 17 (1989), 9–25, https://doi.org/10.1214/aop/1176991491 .
5. P. J. Flory, *Intramolecular reaction between neighboring substituents of vinyl polymers*, Journal of the American Chemical Society 61 (1939), 1518–1521 (classical one-dimensional irreversible dimer-coverage calculation).
