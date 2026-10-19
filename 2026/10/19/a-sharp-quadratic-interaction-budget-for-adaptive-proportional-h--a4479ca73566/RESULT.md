# A sharp quadratic interaction budget for adaptive proportional hypergraph voting

## Finding
Let a finite group of \(N\ge2\) binary-opinion agents repeatedly interact through *active* hyperedges (hyperedges containing both opinions). An active hyperedge is selected using any nonanticipating rule, possibly depending on the entire prior history. Each event independently chooses opinion-preserving rewiring with probability \(p\in[0,1)\), or proportional group voting with probability \(1-p\). During proportional group voting, one uniformly sampled member's opinion is assigned simultaneously to all members of the chosen hyperedge. Let \(\tau\) be the number of active-hyperedge events until there is no active hyperedge, and let \(X_0=i\) be the initial number holding opinion A. Suppose every selected active hyperedge has at least \(\ell\ge2\) vertices. Then

\[
\boxed{\mathbb E\tau\le\frac{i(N-i)}{(1-p)(\ell-1)}\le\frac{N^2}{4(1-p)(\ell-1)}.}
\]

The first bound is sharp: for \(p=0\) and any connected fixed graph (two-person hyperedges), \(\mathbb E\tau=i(N-i)\) exactly. For arbitrary \(\ell\), one mixed hyperedge of size \(N=\ell\) with one dissenting voter attains the bound \(\mathbb E\tau=1\). In particular, the quadratic dependence on population size cannot be uniformly improved in the event-count normalization.

More precisely, if \(a_t,b_t\) are the numbers of A and B agents in the hyperedge selected immediately before event \(t<\tau\), then the following exact *discordance-budget identity* holds:

\[
\boxed{(1-p)\,\mathbb E\sum_{t<\tau} a_t b_t
=i(N-i)-\mathbb E\big[X_\tau(N-X_\tau)\big].}
\]

Thus expected cumulative mixed-group pair exposure is determined by the initial and terminal global color imbalances, even when the group topology changes arbitrarily. If \(P\) denotes the number of actual propagation events before absorption, then \(\mathbb EP\le i(N-i)/(\ell-1)\), independently of \(p\).

There is also a uniform finite-population tail: writing \(B=N^2/[4(1-p)(\ell-1)]\) and \(L=\max\{1,\lceil2B\rceil\}\), for every integer \(r\ge1\),

\[
\boxed{\mathbb P\{\tau>rL\}\le2^{-r}.}
\]

Under independent unit-rate Poisson clocks on active hyperedges, the expected physical absorption time is at most the event-count bound. The bound is on *active-hyperedge events*, not on computational time spent searching for or choosing those events.

## Assumptions and scope
The vertex set is fixed and finite, with labels A/B; at each event with at least one active hyperedge, one such hyperedge is chosen using information available before that event. The selector may be random or adversarial but is nonanticipating. Hyperedges have distinct vertices and selected active hyperedges satisfy \(\lvert H_t\rvert\ge\ell\), where \(2\le\ell\le N\). Rewiring never changes any vertex's opinion; it may modify the incidence structure in any admissible manner and is not required to conserve the number of hyperedges. Coin flips choosing rewiring versus propagation have fixed conditional probability \(p\). At a propagation event, a vertex is sampled uniformly from the selected hyperedge and its opinion is assigned to every member simultaneously. If no active hyperedge exists, the process stops. For the complete original class permitting pairwise interactions, choose \(\ell=2\). The condition \(p<1\) is essential: rewiring alone need not terminate.

No connectedness, mean-field closure, bounded degree, hyperedge-size distribution, or independence between rewiring decisions across events is assumed beyond the stated fixed conditional propagation probability. A topology-only operation may be a self-loop. The proof is formulated for an event-indexed process; the continuous-time corollary assumes independent rate-one active-hyperedge clocks and finite waiting-event dynamics.

## Proof
Write \(X_t\) for the number of A agents and \(\Phi_t=X_t(N-X_t)\), and stop all variables at \(\tau\). Conditional on the complete past and a selected mixed hyperedge with \(a\ge1\) A agents and \(b\ge1\) B agents, a propagation event changes \(X\) by \(+b\) with probability \(a/(a+b)\) or by \(-a\) with probability \(b/(a+b)\). The rewiring branch changes it by zero. Consequently,

\[
\mathbb E[\Delta X_t\mid\mathcal F_t]=0,\qquad
\mathbb E[(\Delta X_t)^2\mid\mathcal F_t]=(1-p)ab.
\]

Since \(\Delta\Phi=(N-2X)\Delta X-(\Delta X)^2\),

\[
\mathbb E[\Phi_{t+1}-\Phi_t\mid\mathcal F_t]=-(1-p)a_tb_t
\]

for \(t<\tau\), and zero thereafter. Therefore, for each finite \(m\),

\[
\mathbb E\Phi_{m\wedge\tau}+(1-p)\mathbb E\sum_{t<m\wedge\tau}a_tb_t=i(N-i).
\tag{1}
\]

For positive integers \(a,b\) with \(a+b\ge\ell\), \(ab=(a-1)(b-1)+(a+b-1)\ge\ell-1\). Hence equation (1) and nonnegativity of \(\Phi\) show

\[
(1-p)(\ell-1)\mathbb E[m\wedge\tau]\le i(N-i).
\]

By monotone convergence \(\mathbb E\tau\le i(N-i)/[(1-p)(\ell-1)]<\infty\); therefore absorption is almost sure. Bounded convergence for \(0\le\Phi\le N^2/4\), together with monotone convergence for the nonnegative sum in (1), proves the exact terminal identity. The predictable conditional probability of propagation is \(1-p\), so the same identity yields \(\mathbb EP\le i(N-i)/(\ell-1)\).

The same mean-time estimate is valid conditionally after every finite preabsorption history, with the initial remaining potential replaced by the current \(X_t(N-X_t)\le N^2/4\). Set \(B=N^2/[4(1-p)(\ell-1)]\) and \(L=\max\{1,\lceil2B\rceil\}\). Markov's inequality gives conditional probability at most \(B/L\le1/2\) of surviving another \(L\) events. Iterating at integer multiples of \(L\) establishes the geometric tail without any Markov assumption on the selector's use of past history.

For sharpness on a connected fixed graph with no rewiring, every selected active hyperedge has \(a=b=1\). The only absorbing configurations are the two global consensuses; the preceding argument gives almost-sure absorption and \(\Phi_\tau=0\). The terminal identity reduces to \(\mathbb E\tau=i(N-i)\). For every \(\ell\ge2\), a single hyperedge on \(N=\ell\) vertices and one dissenter reaches unanimity on its first propagation event, so for \(p=0\) equality holds with \(i(N-i)/(\ell-1)=1\). Finally, under unit-rate Poisson clocks, the total clock rate before absorption is the positive integer number of active hyperedges, at least one. The expected holding time before each active event is consequently at most one; conditioning and summing give \(\mathbb E T_{\mathrm{physical}}\le\mathbb E\tau\). No claim is made that the two times have equal distribution.

## Verification
A standalone exact-rational program, `verify.py`, evaluates the local conditional drift for every pair \(1\le a,b\le14\) and five rewiring probabilities. It also exactly solves small finite-state chains using Gaussian elimination for fixed and topology-switching hypergraphs with up to four agents, checking the full stopped potential identity, event bound, and connected-graph equality. It reports **4888 exact rational assertions passed** when executed with Python 3 (`python verify.py`). These are finite checks; the proof above, rather than enumeration, establishes arbitrary finite population size and arbitrary nonanticipating rewiring. The expected physical-time corollary follows from exponential holding times rather than the finite-state checker.

## Relationship to prior work
Golovin, Mölter and Kuehn [1] define the precise adaptive hypergraph propagation rule and show *conservation of expected magnetization* under proportional voting (their section on magnetization). They investigate slow stochastic evolution and fragmentation primarily with mean-field equations and simulations. The theorem here goes beyond conserved first moments: it gives a *second-moment stopping identity*, a sharp topology-independent bound on the total number of active interactions to termination, and a uniform geometric tail, applicable to both rewiring schemes and history-dependent variants. These new bounds are not asserted for their *majority-voting* rule; that rule fails the zero-drift premise.

Papanikolaou et al. [2] study a different majority-biased group-influence process and group-size-dependent convergence, rather than proportional unanimous propagation. Horstmeyer and Kuehn [3] include triadic peer pressure with majority persuasion. Rogers and Gross [4] derive a diffusion/slow-manifold approximation for pairwise adaptive consensus times, not the exact all-finite-size hypergraph event-count stopping identity. Kim et al. [5] analyze a group-driven voter model with one focal vertex changing per step after a group-constrained sampling rule. Their mean-field consensus times on annealed uniform hypergraphs do not apply to the simultaneous *whole-hyperedge* unanimity operation in the present theorem. Classical bounded-martingale and quadratic-variation techniques underlie the proof and are not claimed as new. The exact topology-independent hypergraph consequence is the claimed contribution; possible prior derivation in another framework remains a priority risk.

## Limitations
The result does not claim consensus: absorption can occur at a fragmented mixed-opinion state, and that possibility appears in the terminal correction \(\mathbb E[X_\tau(N-X_\tau)]\). The result does not apply to majority group voting, zealot biases, irreversible external opinions, rewiring that changes opinions, or conditional propagation probabilities tending to zero. It controls the number of *active interactions*; a simulation that samples arbitrary inactive groups may use many more attempted updates. For physical clock time, it presupposes the event-rate convention. The exponential tail is a conservative bound, not an exact lifetime law. The dependence on \(1/(1-p)\) is sufficient but not claimed optimal for every rewiring policy, and no numerical claim about a fragmentation critical threshold is made.

## References
1. A. Golovin, J. Mölter, C. Kuehn, *Polyadic Opinion Formation: The Adaptive Voter Model on a Hypergraph*, arXiv:2308.03640 (first publicly posted 2023-08-07); Annalen der Physik **536** (2024), 2300342, DOI:10.1002/andp.202300342. https://arxiv.org/abs/2308.03640
2. N. Papanikolaou, G. Vaccario, E. Hormann, R. Lambiotte, F. Schweitzer, *Consensus from group interactions: An adaptive voter model on hypergraphs*, Physical Review E **105** (2022), 054307, DOI:10.1103/PhysRevE.105.054307. https://www.sg.ethz.ch/publications/2022/papanikolaou2022consensus-from-group/PhysRevE.105.054307.pdf
3. L. Horstmeyer, C. Kuehn, *An adaptive voter model on simplicial complexes*, arXiv:1909.05812; Physical Review E **101** (2020), 022305. https://arxiv.org/abs/1909.05812
4. T. Rogers, T. Gross, *Consensus time and conformity in the adaptive voter model*, arXiv:1304.4742; Physical Review E **88** (2013), 030102. https://arxiv.org/abs/1304.4742
5. J. Kim, D.-S. Lee, B. Min, M. A. Porter, M. San Miguel, K.-I. Goh, *Competition between group interactions and nonlinearity in voter dynamics on hypergraphs*, arXiv:2407.11261 (first publicly posted 2024-07-15); Physical Review E **111** (2025), L052301. https://arxiv.org/abs/2407.11261
