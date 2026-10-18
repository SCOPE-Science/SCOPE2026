# Adjacent-pair zero forcing excludes higher-particle dark states on quantum cycles

## Finding

**Theorem.** Let \(N\geq5\) and \(3\leq k\leq N\) be integers. In the \(k\)-token graph \(F_k(C_N)\), initially color blue every configuration containing at least one occupied nearest-neighbor bond of the underlying cycle. The usual zero-forcing rule (a blue vertex with exactly one white neighbor colors that neighbor blue) colors **every** configuration.

Equivalently, if \(H\) is any complex matrix indexed by \(k\)-subsets of \(\mathbb Z/N\mathbb Z\), with \(H_{A,B}\ne0\) for every edge \(AB\) of \(F_k(C_N)\), with \(H_{A,B}=0\) for distinct nonadjacent graph vertices, and with arbitrary diagonal, then an eigenvector vanishing on all configurations containing adjacent particles is identically zero. In particular, a hard-core quantum ring with everywhere-nonzero nearest-neighbor particle hopping, arbitrary number-conserving diagonal potentials, and positive pair-loss rates on every nearest-neighbor bond has **no common Hamiltonian eigenvector and pair-loss kernel vector** in any sector with at least three particles.

## Assumptions and scope

The cycle has distinct vertices \(0,1,\ldots,N-1\), indexed modulo \(N\). A configuration is an unordered set \(A\) of exactly \(k\) occupied sites; different configurations are adjacent in \(F_k(C_N)\) precisely when one particle moves one step clockwise or counterclockwise to an unoccupied site. No second-neighbor or simultaneous hopping matrix elements are allowed. Every allowed single-step off-diagonal matrix element is nonzero; its phase and magnitude may otherwise vary by configuration and direction. Neither Hermiticity nor translation invariance is needed for the graph statement. For the physical corollary, \(H\) is Hermitian and number-conserving; pair losses are \(L_j=\sqrt{\gamma_j}\,b_jb_{j+1}\), with \(\gamma_j>0\) for every bond \(j\).

A zero-forcing step means that a blue configuration with exactly one white graph neighbor forces that white configuration to blue. The theorem is finite, for every allowed \(N\) and \(k\), without an asymptotic hypothesis. If every configuration already contains an occupied bond, the conclusion is immediate.

## Proof

Arrange the occupied sites of \(A\) in clockwise order. Define its *minimum cyclic gap* \(g(A)\) as the smallest number of cycle edges between successive occupied sites (including the closing gap). Thus \(g(A)\geq1\), the gaps sum to \(N\), and \(g(A)\leq\lfloor N/k\rfloor\). The initially blue configurations are exactly those with \(g(A)=1\).

We induct over integers \(d\geq2\), showing that all configurations with \(g(A)\leq d\) become blue once all configurations with \(g(A)<d\) are blue. Let \(S\) be any fixed set of \(k-2\) occupied sites. Because \(k\geq3\), this set is **nonempty**. For each \(t\in\mathbb Z/N\mathbb Z\), write

\[A_t=S\cup\{t,t+d\}.\]

Whenever \(A_t\) has fewer than \(k\) distinct sites or has \(g(A_t)<d\), it is either absent or already blue. Consider a remaining white candidate \(A_t\), so \(g(A_t)\geq d\). Define

\[B_t=S\cup\{t,t+d-1\}.\]

This is a legitimate \(k\)-particle configuration: an extra occupation at \(t+d-1\) would create a gap one in \(A_t\), contrary to \(g(A_t)\geq d\). Its displayed pair is separated by \(d-1\) edges, so \(g(B_t)<d\) and \(B_t\) is blue.

Every token move out of \(B_t\) other than shifting \(t\) left or shifting \(t+d-1\) right leaves the displayed close pair at distance at most \(d-1\), or brings it even closer. Consequently **all** such neighbors are already blue. The only potentially white neighbors are

\[A_{t-1}=S\cup\{t-1,t+d-1\},\qquad A_t=S\cup\{t,t+d\}.\]

The second is a valid graph neighbor of \(B_t\); the first is either a valid neighbor or absent/already blue. If \(A_{t-1}\) is blue, the blue vertex \(B_t\) has the unique white neighbor \(A_t\) and forces it.

Fix \(S\) and traverse \(t\) in increasing cyclic order. Because \(S\ne\varnothing\), there is a starting value \(t=s\in S\) for which \(A_s\) is absent. Hence the preceding candidate is initially absent/blue. At every subsequent \(t\), either \(A_t\) is absent/already blue, or the preceding paragraph forces it after \(A_{t-1}\) is blue. After a full circuit, every \(A_t\) is absent or blue.

Every configuration with minimum gap exactly \(d\) is some \(A_t\): choose two consecutive occupied sites separated clockwise by \(d\) edges and let \(S\) be the remaining \(k-2\) particles. Therefore the induction colors every configuration of minimum gap \(d\). Since \(d\) need only run through \(\lfloor N/k\rfloor\), all configurations become blue. This proves the zero-forcing theorem.

For the eigenvector consequence, let \(H\psi=\lambda\psi\) and assume that \(\psi\) vanishes on every initially blue configuration. If a blue graph vertex \(B\) has exactly one white neighbor \(A\), its eigenvalue equation reads

\[0=(H\psi)_B-\lambda\psi_B=H_{B,A}\psi_A,\]

because all other off-diagonal neighbors already have zero amplitude. As \(H_{B,A}\ne0\), the amplitude on \(A\) is zero. Follow the forcing sequence to obtain \(\psi=0\).

Finally, for \(L_j=\sqrt{\gamma_j}\,b_jb_{j+1}\), the coefficient of the \((k-2)\)-particle configuration \(S\) in \(L_j\psi\) is (up to an irrelevant nonzero convention-dependent sign) \(\sqrt{\gamma_j}\,\psi(S\cup\{j,j+1\})\), whenever the union has size \(k\). Because distinct source configurations for fixed \(j\) give distinct outputs, \(L_j\psi=0\) for all \(j\) implies each adjacent-pair amplitude vanishes. The preceding paragraph excludes any nonzero Hamiltonian eigenvector with this property. \(\square\)

## Verification

The proof is an explicit finite forcing sequence construction, not an extrapolation from numerical results. Two independently organized Python-standard-library checks accompany it under `artifacts/`. Running `python3 artifacts/verify_zero_forcing.py` performs the actual graph-coloring algorithm for \(N=5,\ldots,16\) and \(k=3,4,5\) whenever \(k<N\): all 35 cases force every vertex. It additionally confirms the distinct two-particle boundary does **not** force all vertices for \(N=5,\ldots,12\). Running `python3 artifacts/verify_induction_boundary.py` checks the local two-neighbor induction identity directly for \(N=6,\ldots,16\) and \(k=3,4,5\) (where \(k\leq N\)): 7,633 local equations pass. These finite checks corroborate, but do not replace, the all-size argument.

## Relationship to prior work

Van Horssen and Garrahan, *Open quantum reaction-diffusion dynamics: absorbing states and relaxation* (original preprint 28 November 2014, arXiv:1411.7913v1), classify the zero- and one-particle sectors and two-particle dark states analytically. In Sec. III.1.3 they investigate the absence of dark states in sectors of three or more particles by **numerical diagonalization** (their Eq. (15) and Fig. 4); the present all-size forcing proof supplies a separate analytic justification for that conclusion and allows arbitrary nonzero bond hopping weights and arbitrary diagonal interactions.

Fabila-Monroy and coauthors, *Token Graphs* (arXiv:0910.4774v1), introduced the configuration-graph language; its general definition does not imply that the adjacent-occupation boundary is zero forcing. Everest, Hush and Lesanovsky, *Many-body out-of-equilibrium dynamics of hard-core lattice bosons with non-local loss* (arXiv:1406.6097v1), study a different strong-dissipation/Zeno projected dynamics, including nonlocal-loss-stabilized complexes. Its projected hopping constraints do not supply the everywhere-nonzero full token-graph edge hypothesis used here.

## Limitations

The result concerns pure Hamiltonian eigenstates in the simultaneous kernel of *all* nearest-neighbor pair-loss operators; it does not, by itself, classify all mixed Lindblad stationary states or determine relaxation rates. Removing any loss bond, allowing zero hopping on a permitted graph edge, including long-range/non-single-particle hopping, or replacing the cycle by a different graph invalidates the hypotheses and may permit dark states. The special two-particle sector is excluded deliberately: a fixed nonempty set \(S\) is essential to the cyclic zero-forcing induction, and two-particle dark states on even cycles are already known. Small-graph enumeration alone is not offered as a proof of any infinite statement.

## References

1. M. van Horssen and J. P. Garrahan, *Open quantum reaction-diffusion dynamics: absorbing states and relaxation*, arXiv:1411.7913v1 (first public 2014-11-28), Secs. III.1.2–III.1.3, App. B; https://arxiv.org/html/1411.7913v1 .
2. R. Fabila-Monroy, D. Flores-Peñaloza, C. Huemer, F. Hurtado, J. Urrutia, D. R. Wood, *Token Graphs*, arXiv:0910.4774v1 (first public 2009-10-25); https://arxiv.org/abs/0910.4774 .
3. B. Everest, M. R. Hush and I. Lesanovsky, *Many-body out-of-equilibrium dynamics of hard-core lattice bosons with non-local loss*, arXiv:1406.6097v1 (first public 2014-06-23); https://arxiv.org/html/1406.6097v1 .
