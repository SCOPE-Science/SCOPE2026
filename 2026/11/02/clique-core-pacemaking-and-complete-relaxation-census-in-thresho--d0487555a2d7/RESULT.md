# Clique-core pacemaking and complete relaxation census in threshold-two excitable split graphs

## Finding
Let \(G_{a,b}=K_a\vee\overline K_b\), the simple graph consisting of a clique of \(a\ge1\) vertices, an independent set of \(b\ge1\) vertices, and all cross-edges. Run synchronous three-state Greenberg–Hastings dynamics with excitation threshold two: a resting vertex (state \(0\)) changes to excited (state \(1\)) if and only if at least two of its neighbors are excited, while states \(1\) and \(2\) always change to \(2\) and \(0\), respectively.

**Theorem.** Every initial labelled configuration first enters a periodic orbit after at most five updates; every primitive period is \(1\) or \(3\), and the all-resting state is the sole fixed point. A primitive three-cycle exists **if and only if**
\[
(a\ge4\ \text{and}\ b\ge2)\quad\text{or}\quad a\ge5.
\]
The bound five is attained already for \((a,b)=(3,3)\), and at every pair \(a\ge3,b\ge3\). More strongly, the complete first-entry/period population \(N_{t,p}(a,b)\) has the finite coefficient formula below for all positive integers \(a,b\). Every three-cycle consists exclusively of configurations that rotate *every* vertex through \(0\to1\to2\to0\).

A particularly strong consequence is **one-sided pacemaking**. Under independent uniform initial colors, for every \(b\ge1\),
\[
\Pr\{T=0,\ p=3\}\ \ge\ 1-3(2/3)^a-a(2/3)^{a-1}.
\]
Consequently, as \(a\to\infty\), the probability of immediate collective three-periodic motion converges to one **uniformly over every positive independent-set size \(b\)**. Filling in clique edges therefore suppresses period four while enabling period three with just one independent vertex, in sharp contrast with the two-large-shores requirement in the threshold-two biclique model.

## Assumptions and scope
All graphs are finite, labelled, simple and undirected. The vertex set is the disjoint union of a clique \(C\) with \(|C|=a\) and an independent set \(I\) with \(|I|=b\). There are no self-loops. The update is simultaneous, deterministic and exactly three-state, with threshold exactly two (not threshold one). A trajectory's **first-periodic-entry time** \(T(x)\) is the least nonnegative integer \(t\) such that \(F^t(x)\) is periodic. Its **eventual least period** \(p(x)\) is the least positive period of that entered orbit. Uniform initialization means independent probability \(1/3\) for each state at each labelled vertex. Counts below are counts of labelled configurations, not quotient states.

## Proof
**1. Exact finite cohort reduction.** Partition the initial vertices into six cohorts \(C_j=\{v\in C:X_0(v)=j\}\), \(I_j=\{v\in I:X_0(v)=j\}\) for \(j\in\{0,1,2\}\). At every future time each cohort remains monochromatic: every vertex of the same cohort starts with the same state, and all resting clique vertices see exactly the total number of excited vertices in \(C\cup I\), while all resting independent vertices see exactly the number of excited vertices in \(C\). For a resting clique vertex, the exclusion of its own vertex has no effect because its state is \(0\), not \(1\). Hence cohorts evolve synchronously even when distinct cohorts subsequently merge.

Let \(m=(m_0,\ldots,m_5)\in\{0,1,2\}^6\) be the **fixed initial cohort capacities**, with \(m_j=\min(2,|C_j|)\) and \(m_{3+j}=\min(2,|I_j|)\). For each side the capacity triple must not be identically zero. There are exactly \(26^2=676\) possible capacity vectors across all positive graph sizes. At time \(t\), let \(w_j(t)\in\{-1,0,1,2\}\) record that cohort's state, with sentinel \(-1\) reserved for empty cohorts. Initially \(w(0)=(0,1,2,0,1,2)\), replacing entries with \(-1\) when their capacities vanish.

Write \(E_C(t)=\sum_{j=0}^2m_j\mathbf 1_{\{w_j(t)=1\}}\) and \(E_I(t)=\sum_{j=3}^5m_j\mathbf 1_{\{w_j(t)=1\}}\). For each occupied cohort, its state at time \(t+1\) is \(2\) when presently \(1\), \(0\) when presently \(2\), and, when presently \(0\), the indicator of \(E_C(t)+E_I(t)\ge2\) for clique cohorts or of \(E_C(t)\ge2\) for independent cohorts. Empty cohorts remain \(-1\). Threshold comparisons are unchanged when each initial cohort population exceeding two is replaced by two, even after cohorts merge, because excitation totals are sums of nonnegative cohort populations and only their comparison with two matters. Thus this recurrence reproduces the **actual state of every labelled vertex at every update**. Its first repeat time and primitive period are exactly those of the microscopic trajectory; the argument does not assume eventual periodicity in advance.

**2. Exhaustive finite reduction certificate, covering all sizes.** The attached `certificate.json` explicitly stores the first-repeat trajectory for every one of the \(676\) capacity vectors, and `verify.py` recreates each state using the recurrence just stated. It independently enumerates the microscopic vertex-neighbor update rule on \(221{,}436\) small configurations. Its exact enumeration yields the following **signature-count** pairs \((T,p)\), where counts count *capacity signatures* rather than labelled states:

| \((T,p)\) | \((0,1)\) | \((0,3)\) | \((1,1)\) | \((1,3)\) | \((2,1)\) | \((2,3)\) | \((3,1)\) | \((3,3)\) | \((4,1)\) | \((5,1)\) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Signatures | 4 | 53 | 60 | 18 | 240 | 18 | 170 | 18 | 67 | 28 |

All \(676\) capacity vectors are covered exactly once, with no other \((T,p)\) combination. Since the cohort recurrence is exactly the microscopic recurrence up to relabelling identical initial states, this is an exhaustive proof for **all** \(a,b\), not an extrapolation from finitely many vertex sizes. The capacity vector \((2,1,0;0,1,2)\), realized by three clique vertices and three independent vertices, first becomes fixed at update five. Increasing either capacity-two cohort's actual population preserves that five-update trajectory, proving sharpness at every \(a\ge3,b\ge3\).

**3. Sharp onset of collective three-cycles.** On a period-three orbit, each vertex is either constantly in state zero or executes the full rotation \(0\to1\to2\to0\): the automatic excited/refractory updates preclude any other three-step return. If any clique vertex rotates while another clique vertex were constantly zero, the latter would also ignite at a time when the rotating clique vertex ignites, a contradiction. Thus all clique vertices rotate. An independent vertex constantly zero alongside any rotating independent vertex would ignite at that rotating vertex's first excitation, another contradiction. If every independent vertex were constantly zero, the clique could not excite its resting vertices without exciting those constant independent vertices. Hence every vertex rotates.

For a proposed immediately periodic rotating configuration, write \(u_j\) and \(v_j\) for the numbers initially in color \(j\) on the clique and independent side. The rotation occurs exactly when for each \(j\in\{0,1,2\}\) (indices modulo three),
\[
(u_j=0\ \text{or}\ u_{j+1}+v_{j+1}\ge2),\qquad
(v_j=0\ \text{or}\ u_{j+1}\ge2).
\tag{*}
\]
These are precisely the excited-neighbor conditions at the time a cohort is resting. They remain sufficient for all subsequent steps by phase rotation. Checking the capped versions of \((*)\) over the \(676\) allowed signatures, independently confirmed by `verify.py`, yields \(u_0+u_1+u_2\ge4\), and when this total equals four it forces \(v_0+v_1+v_2\ge2\). The constraints have explicit sharp witnesses: \(u=(0,a-2,2)\), \(v=(b,0,0)\) when \(a\ge4,b\ge2\); and \(u=(a-4,2,2)\), \(v=(b,0,0)\) when \(a\ge5,b\ge1\). These witnesses satisfy \((*)\) and therefore produce primitive three-cycles. The all-zero configuration is the unique fixed point because every excited and refractory vertex must change state.

**4. Exact labelled census.** Put
\[
\Phi_0(z)=1,\qquad\Phi_1(z)=z,\qquad\Phi_2(z)=e^z-1-z.
\]
For each capacity signature \(m\), let \((\tau(m),\pi(m))\) be its first-entry time and least period as listed in `certificate.json`. For all \(a,b\ge1\), \(0\le t\le5\), and \(p\in\{1,3\}\),
\[
\boxed{N_{t,p}(a,b)=a!b!\,[x^a y^b]\!
\sum_{\substack{m\in\{0,1,2\}^6\\m_{0:3}\ne0,\ m_{3:6}\ne0\\\tau(m)=t,\ \pi(m)=p}}
\prod_{j=0}^{2}\Phi_{m_j}(x)\Phi_{m_{3+j}}(y).}
\]
Here \(m_{0:3}\ne0\) denotes the nonzero first triple, and similarly for the last. The exponential generating factors enumerate the exact labelled sizes of the six initial-color cohorts (size zero, one or at least two), and the exact cohort dynamics provide the indicated \((t,p)\). All other \(N_{t,p}\) vanish. In particular \(N_{0,1}=1\), and the number of distinct primitive three-cycles is \(N_{0,3}(a,b)/3\). The independent `verify.py` checks the coefficient sum against direct labelled dynamics for six nontrivial graph sizes, but the formula itself follows exactly from the partition into initial cohorts.

**5. Pacemaker probability.** If the clique initially contains at least two vertices of *each* of its three colors, then the excited population inside the clique is at least two at every step of pure phase rotation. Every resting vertex in either graph side therefore excites, regardless of the independent side's initial colors. For independent uniform colors the chance that a specified clique color appears at most once is \((2/3)^a+a(1/3)(2/3)^{a-1}\). A union bound over the three colors yields the stated bound, independent of \(b\).

## Verification
Run `python3 verify.py` next to `certificate.json`. The script recomputes all \(676\) complete cohort paths, proves the reported histogram, checks the global transient bound, the rotation characterization and the two sharp period-three witnesses. It separately implements explicit vertex-neighbor updates and exhaustively compares first entry and eventual period on \(221{,}436\) labelled configurations; exact multinomial-count checks are run for six selected size pairs. The included `verification_output.txt` records the result `SPLIT_GHM_THRESHOLD_TWO_ALL_CHECKS_PASSED`. This is a finite exhaustive proof *because* the above capacity reduction rigorously covers all positive sizes. No unexamined larger-size simulation is used as a substitute for that reduction.

## Relationship to prior work
Greenberg and Hastings introduced the three-state excitation/refractory mechanism. Fisch, Gravner and Griffeath studied threshold excitation principally on spatial lattices, and Gravner, Lyu and Sivakoff (arXiv:1610.07320v1) proved broad limiting-behavior statements on graphs at the **one-neighbor** excitation rule; their finite-graph irrotationality characterization does not imply the present **two-neighbor** orbit/entry census. A pre-existing threshold-two complete-bipartite classification requires both shores to be at least six for period three and also permits period four when each shore is at least four; its results do not imply what happens after inserting every edge within one shore. A threshold-two tripartite analysis additionally finds primitive twelve-cycles for other graphs, likewise neither a consequence nor a generalization of the split-graph statement. Comparisons based solely on titles or search absence cannot prove novelty, and unindexed historical equivalents remain possible.

## Limitations
The theorem concerns only complete split graphs, exactly three states and synchronous threshold-two excitation. It makes no assertions for general split graphs, other thresholds, noise or asynchronous updating. The coefficient formula is exact but not a closed elementary expression for every parameter pair. The novelty assessment depends on accessible literature and comparison records and has not undergone independent audit. The historical threshold-range paper's complete original text was not available in the consulted materials; its available abstract and the later paper's full text were used without claiming an exhaustive negative literature proof.

## References
1. J. M. Greenberg and S. P. Hastings, “Spatial patterns for discrete models of diffusion in excitable media,” *SIAM J. Applied Mathematics* **34** (1978), 515–523. DOI: `10.1137/0134040`.
2. R. Fisch, J. Gravner and D. Griffeath, “Threshold-Range Scaling of Excitable Cellular Automata,” original preprint `arXiv:patt-sol/9304001`, submitted 1993-04-02; published in *Statistics and Computing* **1** (1991), 23–39, DOI: `10.1007/BF01890834`.
3. J. Gravner, H. Lyu and D. Sivakoff, “Limiting behavior of 3-color excitable media on arbitrary graphs,” `arXiv:1610.07320v1`, first submitted 2016-10-24, especially equations (1) and (5), Theorem 3 and Section 4.
