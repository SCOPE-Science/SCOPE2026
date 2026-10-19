# Exact fixation and a hyperedge-size selection transition on uniform sunflowers

## Finding

**Theorem (uniform-petal sunflower fixation).** Fix integers \(s,m\geq1\) and a relative mutant fitness \(r>0\). Let a population of \(N=sm+1\) individuals occupy the sunflower hypergraph with one central vertex \(c\) and \(m\) disjoint sets \(P_1,\ldots,P_m\), each of size \(s\), and hyperedges \(\{c\}\cup P_j\). At each discrete step select one parent with probability proportional to fitness (mutants have fitness \(r\), residents fitness \(1\)); the parent chooses one of its incident hyperedges uniformly, and every vertex in that hyperedge adopts the parent's type. There are no mutations after initialization.

Put
\[
q=\frac{r+sm}{r(1+smr)},\qquad
H=\left(1+\frac{sm}{r}\sum_{j=0}^{m-1}q^j\right)^{-1}.
\]
The respective probabilities of eventual mutant fixation from one mutant initially at the center, from one mutant initially at any peripheral vertex, and from one mutant initialized uniformly over all \(N\) vertices are exactly
\[
\boxed{\rho_c=H,\qquad
\rho_p=H\frac{m(r+sm)}{m(r+s-1)+1},\qquad
\rho_{s,m}=H\frac{mr+sm^2-m+1}{mr+m(s-1)+1}.}
\]
These formulas hold for every admissible \(s,m,r\), including \(r=1\). Fixation or extinction occurs almost surely. For \(m>1\), peripheral initialization is strictly better than central initialization at **every** positive fitness:
\[
\frac{\rho_p}{\rho_c}-1=\frac{(m-1)(sm+1)}{m(r+s-1)+1}>0.
\]
At neutrality, the two location-specific probabilities are \(\rho_c=1/(1+sm^2)\) and \(\rho_p=m/(1+sm^2)\), whereas uniform initialization has \(\rho_{s,m}(1)=1/(sm+1)\).

Fix \(s\) and an advantageous fitness \(r>1\). The growing-petal-number limit is
\[
\boxed{\lim_{m\to\infty}\rho_{s,m}(r)=\frac{r^2-1}{r(r+s-1)}.}
\]
The well-mixed Moran baseline with the same \(N\) individuals converges to \(1-1/r\). Thus pairwise star reproduction (\(s=1\)) has a strictly *larger* limit \(1-1/r^2\); three-person group reproduction (\(s=2\)) has exactly the Moran limit; and groups of at least four persons (\(s\geq3\)) have a strictly *smaller* limit. These are statements about limiting fixation probabilities, not a claim of global finite-size amplifier/suppressor ordering for every fitness.

The exact response to weak selection, at finite population size, is
\[
\boxed{\rho'_{s,m}(1)=
\frac{sm^2(sm^2-m+2)}{(sm+1)^2(1+sm^2)}.}
\]
For \(m>1\), the derivative is above the well-mixed Moran derivative when \(s=1\), but for every \(m\geq1\) it is strictly below the Moran derivative when \(s\geq2\). At \(s=1,m=1\), the derivatives agree. In particular, \(\lim_{m\to\infty}\rho'_{s,m}(1)=1/s\), while the Moran derivative tends to \(1/2\). The three-person borderline has the sharper large-\(m\) expansion, for fixed \(r>1\),
\[
\rho_{2,m}(r)=1-\frac1r-\frac{(r-1)(r+3)}{2r(r+1)m}+O_r(m^{-2}).
\]

## Assumptions and scope

Every hyperedge contains precisely \(s+1\) people. Distinct hyperedges share exactly the central individual, and there are no other hyperedges. Parents are chosen from the whole population according to their positive constant fitnesses. A peripheral parent belongs to one hyperedge; the central parent chooses among \(m\) hyperedges. The selected parent replaces **all other members** of its selected hyperedge. The theorem does not cover fitness based on payoffs, majority-gated replacement, selection on death, separate random recipient selection, mutation, or a hyperstar containing every possible pair of leaves.

A fixed initial mutant is at the center or any one peripheral individual; in the uniform case the initial location is chosen uniformly. The theorem quantifies fixation at the all-mutant absorbing state, not expected fixation time. All probabilities are unconditional over subsequent reproduction events. The limit keeps \(s,r\) fixed while \(m\to\infty\), and the weak-selection derivative holds \(s,m\) fixed while differentiating at \(r=1\).

## Proof

**1. Homogeneous petals are permanent.** Whenever a hyperedge is selected, every individual in its petal receives one type. Since the petal's peripheral individuals only interact through that same hyperedge, they remain mutually identical thereafter. The configurations in which every petal is already homogeneous therefore form an invariant state space. Write \((h,j)\) for the state in this space with hub type \(h\in\{0,1\}\) (resident/mutant) and exactly \(j\in\{0,\ldots,m\}\) mutant petals. The two absorbing states are \((0,0)\) and \((1,m)\).

**2. Exact reduced transition rates.** In state \((0,j)\), the only changes are \((0,j)\to(0,j-1)\), with probability proportional to \(j/m\), when the resident hub chooses a mutant petal; and \((0,j)\to(1,j)\), with probability proportional to \(srj\), when a mutant peripheral parent converts the hub. In state \((1,j)\), the only changes are \((1,j)\to(1,j+1)\), proportional to \(r(m-j)/m\), and \((1,j)\to(0,j)\), proportional to \(s(m-j)\). All four rates share the same state-dependent positive denominator equal to the sum of the fitnesses of all individuals. Self-loops do not affect the harmonic fixation equations.

Let \(u_j\) and \(v_j\) be the probabilities of eventual mutant fixation from \((0,j)\) and \((1,j)\), respectively. The boundary conditions are \(u_0=0\), \(v_m=1\). First-step conditioning gives
\[
\frac1m(u_{j-1}-u_j)+sr(v_j-u_j)=0\quad(1\leq j\leq m),
\]
\[
\frac r m(v_{j+1}-v_j)+s(u_j-v_j)=0\quad(0\leq j<m).
\]
Set \(d_j=v_j-u_j\). The equations imply
\[
u_j-u_{j-1}=smr\,d_j,\qquad
v_{j+1}-v_j=\frac{sm}{r}d_j,
\]
so that \((1+smr)d_{j+1}=(1+sm/r)d_j\), or \(d_{j+1}=qd_j\) with the displayed \(q\). From \(u_0=0\) and \(v_m=1\),
\[
1=v_m=v_0+\frac{sm}{r}\sum_{j=0}^{m-1}d_j
=d_0\left(1+\frac{sm}{r}\sum_{j=0}^{m-1}q^j\right).
\]
Hence \(v_0=d_0=H\), proving the hub formula. There are no other closed communicating classes: at every nonabsorbing homogeneous-petal state there is a finite positive-probability path to one of the two unanimous states. Finiteness of the state space therefore implies almost-sure absorption.

**3. The initial peripheral mutant.** Start with a resident hub, one mutant peripheral individual, and all other individuals resident. Until an event selects its petal, the state is unchanged. The first such event is initiated either by that mutant (relative rate \(r\)), by one of its \(s-1\) resident petal-mates (relative rate \(s-1\)), or by the resident hub choosing the petal (relative rate \(1/m\)). The mutant event leads to \((1,1)\); either resident event causes immediate extinction. Thus
\[
\rho_p=\frac{r}{r+s-1+1/m}v_1.
\]
The second reduced equation at \(j=0\) gives \(v_1=H(1+sm/r)\). Substitution proves the leaf formula. Averaging one hub location and \(sm\) peripheral locations proves the formula for \(\rho_{s,m}\). A direct subtraction proves the strict location inequality.

**4. Neutrality and weak selection.** At \(r=1\), \(q=1\) and \(H=1/(1+sm^2)\), giving the claimed probabilities. Differentiating at \(r=1\),
\[
q'(1)=-\frac{2sm}{sm+1},\quad
H'(1)=\frac{sm^2}{(sm+1)(1+sm^2)},\quad
\left(\frac{\rho_p}{H}\right)'\!\!(1)=-\frac{m(m-1)}{sm+1}.
\]
Differentiating the uniform average yields the displayed derivative. The well-mixed Moran derivative at neutrality is \(sm/[2(sm+1)]\); their difference (Moran minus sunflower) is
\[
\frac{sm\bigl(s(s-2)m^3+(s+2)m^2+(s-4)m+1\bigr)}{2(sm+1)^2(1+sm^2)}.
\]
For \(s=1\), the parenthesized term equals \(-(m-1)^3\); for \(s=2\), it is \(4m^2-2m+1>0\); and for \(s\geq3\) it is positive for all \(m\geq1\). This proves the finite-size weak-selection assertions.

**5. Large-population behavior.** For fixed \(r>1\), \(q\to r^{-2}<1\) as \(m\to\infty\), and the finite geometric sum converges to \(r^2/(r^2-1)\). Therefore \(mH\to(r^2-1)/(sr)\) and \(\rho_p/H\sim sm/(r+s-1)\). The uniform average converges to \((r^2-1)/[r(r+s-1)]\). The comparisons with the Moran limit follow by cancellation of \((r-1)/r\). For the \(s=2\) correction, use the exact finite geometric-sum expression, the exponentially small term \(q^m\), and a first-order expansion in \(1/m\); the coefficient simplifies to \(-(r-1)(r+3)/[2r(r+1)]\). No interchange of the limits \(r\downarrow1\) and \(m\to\infty\) is asserted.

## Verification

Two standalone Python files accompany this result. `verify_exact.py` verifies 22,400 exact-rational recurrence, boundary, aggregation, and ordering identities over a grid of positive rational fitnesses and integer petal sizes. `check_general.py` independently builds full binary-configuration chains for small populations and a separate petal-count Markov chain for larger cases. It reports 13,677 numerical checks, requiring agreement within \(10^{-10}\) in those comparisons. The original proof above, not the finite checks, establishes all-size and asymptotic statements. Run with `python verify_exact.py` and `OPENBLAS_NUM_THREADS=1 python check_general.py` (the second script requires NumPy).

## Relationship to prior work

Liu and Masuda (2023) define precisely this parent-selection/group-broadcast mechanism as their *model 1* and study complete, cyclic, and star 3-uniform hypergraphs. Their star uses **every** pair of peripheral vertices with the hub, unlike the present disjoint-petal sunflower; their equations and supporting derivations accordingly have different transitions. The one-petal case and the graph-star case are covered by elementary existing models, and their appearance above serves as consistency and limiting benchmarks, not as independent novelty claims. The contribution is the arbitrary-group-size disjoint-petal reduction, the exact location-specific and uniform fixation probabilities for all \(s,m,r\), and the sharp hyperedge-size transition.

Liu and Masuda (2024) examine two-layer pairwise networks and selection suppression; their model uses coupled layers rather than group-wide adoption on a sunflower. Peña and Rochat (2012) distinguish group-game interaction hypergraphs from replacement graphs, but their update uses pairwise competition/strategy imitation, rather than replacing every member of a selected hyperedge. These results do not by themselves imply the formulas here. Related reductions to weighted pairwise stars can inform the homogeneous-petal part, but do not directly specify the first heterogeneous-petal event or the full group-size comparison.

## Limitations

The result is for a highly symmetric, finite sunflower with positive constant fitness and group-wide copying. It does not imply that every hypergraph with larger hyperedges suppresses selection, or that the finite-size Moran inequality holds globally for all \(r>0\). The large-population comparison assumes a fixed advantageous mutant fitness \(r>1\); neutral and deleterious mutants require separate limits. Similar reductions may have appeared in less easily indexed evolutionary-population literature; independent priority assessment has not been performed. The scripts provide reproducibility checks, not a replacement for the analytical proof.

## References

- R. Liu and N. Masuda, *Fixation dynamics on hypergraphs*, PLOS Computational Biology 19 (2023), e1011494. First public preprint: 13 January 2023, arXiv:2301.05343. https://arxiv.org/abs/2301.05343 ; https://doi.org/10.1371/journal.pcbi.1011494 . Relevant locations: Sections 2, 3.1 and Supporting Text G.
- R. Liu and N. Masuda, *Fixation Dynamics on Multilayer Networks*, SIAM Journal on Applied Mathematics 84 (2024), 2028–2050. https://doi.org/10.1137/23M1620144 . Relevant locations: Sections 2–3.
- J. Peña and Y. Rochat, *Bipartite Graphs as Models of Population Structures in Evolutionary Multiplayer Games*, PLOS ONE 7 (2012), e44514. https://pmc.ncbi.nlm.nih.gov/articles/PMC3438187/ . Relevant locations: interaction versus replacement structure.
