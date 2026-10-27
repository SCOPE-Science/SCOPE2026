# Sharp preperiod cutoff for three-state Greenberg–Hastings dynamics on cyclic rings

## Finding
For every integer \(n\ge3\), equip the cycle \(C_n\) with states \(0\) (rest), \(1\) (excitation), and \(2\) (refractory). Let \(F_n\) act synchronously by
\[
(F_nx)_i=\begin{cases}2,&x_i=1,\\0,&x_i=2,\\1,&x_i=0\text{ and }(x_{i-1}=1\text{ or }x_{i+1}=1),\\0,&\text{otherwise}.
\end{cases}
\]
Indices are taken modulo \(n\). For \(x\in\{0,1,2\}^n\), let \(\tau_n(x)\) be the smallest nonnegative integer such that \(F_n^{\tau_n(x)}(x)\) belongs to a periodic orbit (the least preperiod). Then
\[
\boxed{\max_{x\in\{0,1,2\}^n}\tau_n(x)=\lfloor n/2\rfloor+2.}
\]
One excited cell with all remaining cells resting attains equality. Every eventual periodic orbit is either the all-resting fixed configuration or a wave train shifting one site per time step, so its period divides \(n\).

## Assumptions and scope
The graph is exactly the undirected cycle with \(n\ge3\), nearest-neighbor threshold one, three states, and parallel updates. The bound concerns the entire finite state space, not merely randomly chosen states or synchronizing initial conditions. It does not classify the number of states at each preperiod or the attraction basins.

## Proof
Write a configuration at time \(t\) as \(X_t\). For \(t\ge1\), every site colored \(1\) has a neighbor colored \(2\): that site was excited from a neighboring \(1\) at time \(t-1\), and the latter automatically became \(2\). Define an R-particle with head at \(i\) when \((X_t(i-1),X_t(i))=(2,1)\), and an L-particle with head at \(i\) when \((X_t(i),X_t(i+1))=(1,2)\). Every excitation is the head of at least one particle. A head can carry both orientations, corresponding to local pattern \(212\).

**No new particle creation after time one.** If an R-particle has its head at \(j\) at time \(t+1\ge2\), then its old head at \(j-1\) was \(1\), its old target at \(j\) was \(0\), and the old head's requisite neighboring \(2\) must have been at \(j-2\). Thus an R-particle existed at \(j-1\) at time \(t\), moving one step right. Conversely an R-particle at \(j-1\) survives to head \(j\) precisely when its target at \(j\) is resting. The same argument, reflected, proves that an L-particle survives only by moving one step left and has an L-ancestor. There is no splitting, creation, reversal, or waiting.

**Opposite orientations collide.** Consider any R and L present at time \(1\), with head positions \(p\) and \(q\); let \(d\in\{0,\ldots,n-1\}\) be the clockwise distance from \(p\) to \(q\). In fact \(d\le n-2\), since \(d=n-1\) would make the L-particle's requisite refractory body coincide with the R-particle's excited head. If both selected particles survive, after \(s\) rounds their heads must occupy \(p+s\) and \(q-s\). For even \(d\), they meet at the same excited site after \(d/2\) rounds; the two refractory bodies on its sides then prevent continuation of either particle. For odd \(d\), after \((d-1)/2\) rounds their excited heads are adjacent, preventing their continuation. Thus the two selected particles cannot both survive past \(\lfloor d/2\rfloor\) further rounds. Any simultaneous surviving R and L at a later time would have ancestors at time one, yielding the same contradiction. Consequently by time \(1+\lfloor(n-2)/2\rfloor+1=\lfloor n/2\rfloor+1\), at most one particle orientation is present globally.

**One extra round reaches a periodic configuration.** If neither orientation remains at any time \(t\ge1\), no site is excited, so after one additional update all refractory sites also disappear. If only R-particles remain, every excited site is preceded by \(2\) and not followed by \(2\). Moreover, the site immediately ahead of each excited head must be resting: it cannot be \(2\), which would define an L-particle, or \(1\), which (by the first paragraph) would need a refractory neighbor on its other side and thus also define an L-particle. All R-particles therefore advance freely one site, with any refractory sites not part of a particle disappearing. The updated configuration is a rigid right-moving wave train, recurrent by rotation; the all-L case is its reflection. This proves \(\tau_n(x)\le\lfloor n/2\rfloor+2\) for every \(x\).

**Sharpness.** Start from one excited site and all other sites resting. Two excitation fronts travel in opposite directions; the R and L heads first appear at time one at clockwise separation \(n-2\). Their intervening resting sites cause them to advance until they meet (if \(n\) is even) or become adjacent (if \(n\) is odd). Their heads then disappear and the final refractory cells vanish exactly one update later. The result is all zeros at time \(\lfloor n/2\rfloor+2\), with nonzero configurations at every preceding time. Such a trajectory cannot enter a nonzero periodic orbit, since its eventual orbit is zero. Equality follows.

## Verification
Run the enclosed standalone `verify.py` with Python 3. It computes the entire functional graph for each \(3\le n\le11\) and checks the exact maximum preperiod, checks the sharp single-excitation witness, exhaustively tests the ancestry conditions for all one-step image states at \(3\le n\le8\), and uses 2,000 reproducible configurations of larger rings to test entry into a fixed or translating wave train. These are finite corroborations, not substitutes for the preceding all-size argument.

## Relationship to prior work
Fisch and Gravner (1995) analyze one-dimensional Greenberg–Hastings fronts and their annihilation on the infinite lattice. Gravner, Lyu, and Sivakoff (2018, Theorem 3) show that *conservative* initial colorings on a finite connected graph synchronize no later than its diameter and give asymptotic activity for nonconservative colorings. On \(C_n\), that theorem supplies a strong pre-existing bound for the synchronizing branch; its stated nonconservative result does not give an entrance-time bound into a traveling wave. Kesseböhmer, Rademacher, and Ulbrich (2020) describe nonwandering dynamics and entropy in the one-dimensional infinite system, without the above sharp worst-case finite-cycle preperiod formula in the material inspected. The present scope is the universal finite-ring cutoff, explicitly including winding/nonconservative states, rather than the already established particle description or synchronization criterion.

## Limitations
The conclusion pertains only to three-state, nearest-neighbor, threshold-one synchronous Greenberg–Hastings dynamics on a cycle. It does not extend as stated to arbitrary graphs, thresholds, refractory lengths, or asynchronous schedules. Historical priority has not been independently certified; a more specialized finite-ring theorem not identified in the inspected literature remains possible. The claim does not count maximally delayed configurations or full transient-depth distributions.

## References
- R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002 (public 1993-03-22), https://arxiv.org/abs/patt-sol/9303002.
- R. Fisch and J. Gravner, *One-dimensional Deterministic Greenberg-Hastings Models*, Complex Systems **9** (1995), 329–348, https://content.wolfram.com/sites/13/2018/02/09-5-1.pdf.
- J. Gravner, H. Lyu, and D. Sivakoff, *Limiting Behavior of 3-Color Excitable Media on Arbitrary Graphs*, Annals of Applied Probability **28** (2018), 3324–3357, https://doi.org/10.1214/17-AAP1350.
- M. Kesseböhmer, M. Rademacher, and T. Ulbrich, *Dynamics and Topological Entropy of 1D Greenberg–Hastings Cellular Automata*, Ergodic Theory and Dynamical Systems (2020), preprint arXiv:1903.02459, https://arxiv.org/abs/1903.02459.
