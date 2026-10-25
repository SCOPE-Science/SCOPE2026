# Sharp parity-dependent stabilization and critical-bridge counts for majority dynamics on barbell graphs

## Finding

Let \(B_{a,b}\) consist of cliques \(K_a\) and \(K_b\), \(a,b\ge3\), joined by exactly one edge between distinguished vertices \(u\) and \(v\). Apply synchronous binary open-neighbour majority: a vertex adopts the strict majority bit of its neighbours, and keeps its bit at a tie. For any initial labelled state \(z\), let \(\tau(z)\) be the smallest \(t\ge0\) for which \(F^{t+2}(z)=F^t(z)\). The following exact statements hold.

**Sharp stabilization times and final transient strata.** Put \(T(a,b)=\max_z\tau(z)\), and let \(N_T(a,b)=|\{z:\tau(z)=T(a,b)\}|\). Then

\[
T(a,b)=\begin{cases}2,&a,b\text{ odd},\\4,&a,b\text{ even},\\5,&a,b\text{ of opposite parity}.
\end{cases}
\]

For odd \(a=2p+1\), odd \(b=2q+1\), set \(C_a=\binom{2p}{p}\), \(C_b=\binom{2q}{q}\). The terminal population is
\[
N_2(a,b)=2^b C_a+2^a C_b-2C_aC_b.
\]
For even \(a=2p\), even \(b=2q\), set \(D_a=\binom{a-1}{p-1}\), \(D_b=\binom{b-1}{q-1}\). Then
\[
N_4(a,b)=2\left[D_a(2^{b-2}-D_b)+D_b(2^{a-2}-D_a)\right].
\]
For odd \(a=2p+1\) and even \(b=2q\),
\[
N_5(a,b)=\binom{a-1}{p}\binom{b}{q};
\]
the swapped formula applies when \(a\) is even and \(b\) odd. All these terminal populations are strictly positive at the stated sizes.

**All recurrent configurations.** There are exactly four fixed configurations, obtained by assigning a constant bit separately to each clique. A primitive two-cycle exists precisely when both clique sizes are even; in that case every two-cycle consists of a state and its bitwise complement, each clique is exactly half ones, and the bridge bits are opposite. With even \(a,b\), there are precisely \(D_aD_b\) primitive two-cycles, or \(2D_aD_b\) nonfixed periodic configurations. No configuration enters a two-cycle strictly after time zero; every nonperiodic initial configuration eventually reaches a fixed point.

For odd \(a\) and even \(b\) both tending to infinity, the exact terminal count implies the asymptotic probability
\[
\Pr_{z\text{ uniform}}(\tau(z)=5)\sim \frac{1}{\pi\sqrt{ab}}.
\]

## Assumptions and scope

The graph is simple and undirected. Each clique has at least three vertices, and the only interclique edge is \(uv\). Vertices are distinctly labelled, so \(N_T\) counts individual binary configurations, not orbits under automorphisms. Every update is simultaneous and compares **open** neighbours, with the current bit retained at exact ties. Periodicity begins at the smallest \(t\) satisfying \(F^{t+2}(z)=F^t(z)\), which is valid because all eventual periods here are one or two. The theorem makes no assertion for clique sizes below three, weighted edges, stochastic updates, or changed tie policies.

## Proof

**1. One-clique update rule.** Write \(n\) for a clique size, \(w\) for its bridge bit and \(e\) for the opposite bridge bit. Let \(x\) of the other \(n-1\) clique vertices be one, and put \(s=x+w\). Those \(n-1\) vertices have no neighbour outside their clique; the bridge vertex sees those \(n-1\) vertices together with \(e\).

If \(n=2p+1\) is odd, every nondistinguished vertex changes in one update to the common clique-majority bit \(\mu=\mathbf1_{\{s\ge p+1\}}\). This includes the possible tie for an individual nonbridge vertex because a tie retains that vertex's bit. The bridge bit after this update differs from \(\mu\) **only** in the following two pivotal cases:

\[
(x,w,e)=(p,0,1)\quad(\mu=0,\ w'=1),
\qquad
(x,w,e)=(p,1,0)\quad(\mu=1,\ w'=0).
\]

At the next update the entire odd clique becomes constant \(\mu\), regardless of its neighbour across the bridge, because its \(2p\ge2\) nondistinguished vertices already agree. This constant configuration remains stable thereafter, irrespective of the other clique's behaviour.

If \(n=2p\) is even, the exact update is instead:

- \(s<p\): the entire clique becomes zero;
- \(s>p\): the entire clique becomes one;
- \(s=p\): each nondistinguished bit is complemented, and the bridge bit becomes \(e\).

The first two cases produce permanently stable clique consensus. In the third case, the next total one-count is \(s'=p-1+w+e\). Thus a balanced even clique remains balanced through that step **if and only if** its current bridge bit differs from the other bridge bit. A balanced clique ceases to be balanced when those bits agree, and becomes fully constant one additional update later. The critical update consists of a bitwise complement of the clique exactly when its bridge bits are opposite.

These rules follow by comparing, for a nondistinguished vertex of bit \(c\), the \(s-c\) one-neighbours among its \(n-1\) neighbours, and for the bridge vertex, the \(x+e\) one-neighbours among its \(n\) neighbours, applying tie retention in either case. They are exact for every admissible \(n\), not asymptotic approximations.

**2. Recurrent configurations.** A constant clique is permanently stable because at least two same-bit internal neighbours overwhelm the single opposite-bridge neighbour. If both clique sizes are odd, the preceding lemma makes both cliques constant by time two, hence only the four pairs of clique consensuses can recur. If at least one clique is even, any nonconstant state on that even clique must be balanced at every time on a recurrent orbit; otherwise it collapses permanently into consensus. Its bridge bit must therefore always differ from the opposite bridge bit. If the other clique is odd, the latter becomes constant by time two; an even balanced clique then cannot persist indefinitely. If both are even, both must be balanced and the bridge bits must be opposite, so the entire state is complemented on each update and yields a primitive two-cycle. Conversely, every such balanced, opposite-bridge state is manifestly a two-cycle from its initial time. The central binomial coefficients \(D_a,D_b\) count possible nondistinguished assignments for each of the two opposite bridge-bit choices, giving \(2D_aD_b\) two-periodic states and \(D_aD_b\) cycles. The same argument shows no trajectory can first *enter* a two-cycle at positive time.

**3. Both sides odd: sharp time two and its count.** Each clique is constant by time two. It fails to be constant at time one precisely when its bridge is in one of the two pivotal states in step 1. Call these events \(A\) and \(B\). For odd \(a=2p+1\), \(b=2q+1\), the number of initial configurations satisfying \(A\) is \(2^b C_a\): two choices for the left bridge and matching opposite bridge, \(C_a\) assignments of the left nondistinguished bits, and \(2^{b-1}\) unrestricted assignments on the other nondistinguished vertices. Similarly \(|B|=2^a C_b\), and \(|A\cap B|=2C_aC_b\). Since all states at time two are fixed, \(\tau=2\) holds exactly on \(A\cup B\). Inclusion-exclusion gives the displayed \(N_2\), positive for all odd sizes at least three.

**4. Both sides even: sharp time four and its count.** Let \(a=2p\), \(b=2q\). If the initial bridge bits agree, a balanced initial clique becomes unbalanced after one update and constant after two; a nonbalanced initial clique becomes constant after one. Hence stabilization takes at most two. If the initial bridge bits differ, each initially balanced clique remains balanced at time one, while every initially unbalanced clique becomes constant. When both cliques are balanced, the state is already in a two-cycle. When only one is balanced, the other is fixed after time one. A balanced clique then becomes constant no later than time four, with **exact** entry time four if and only if it is still balanced at time one and its time-one bridge bit opposes the other clique's time-one consensus bit. This occurs precisely when one initial clique is balanced and the other initially has a strict clique-majority bit equal to the initial bridge bit on the balanced side.

Count first the case where the size-\(a\) clique is initially balanced. Its two possible initial bridge bits both allow \(D_a\) assignments of its \(a-1\) nondistinguished bits. For each choice, the opposite bridge bit is forced, and the size-\(b\) clique must have a strict initial majority equal to the balanced-side bridge bit. The number of its nondistinguished assignments is \(2^{b-2}-D_b\), using the binomial-sum identity \(\sum_{j=0}^{q-2}\binom{2q-1}{j}=2^{2q-2}-\binom{2q-1}{q-1}\); the symmetric upper-tail count is the same. Hence this case contributes \(2D_a(2^{b-2}-D_b)\). Exchanging the two cliques adds \(2D_b(2^{a-2}-D_a)\). These cases are disjoint, and give exactly \(N_4\). Because \(b\ge4\), \(2^{b-2}>D_b\), proving sharpness.

**5. Opposite parities: sharp time five and its count.** Assume the odd clique has size \(a=2p+1\), the even clique size \(b=2q\). The odd clique is permanently constant with bit \(\mu\) from time two. A balanced even clique may persist to time three only when it sees first an exceptional odd bridge at time one and then the opposite fixed odd bridge at time two. At time three the even bridge copies \(\mu\), so its own bridge agrees with the odd bridge thereafter; it loses balance at time four and becomes constant at time five. Thus \(\tau\le5\), with equality exactly under the following initial conditions:

\[
\begin{gathered}
\text{odd nondistinguished vertices: exactly }p\text{ ones},\\
\text{odd bridge bit }\mu,\quad\text{even bridge bit }1-\mu,\\
\text{even clique: exactly }q\text{ total ones}.
\end{gathered}
\]

Indeed, the odd bridge then makes its unique pivotal deviation to \(1-\mu\) at time one, and reverts to \(\mu\) at time two. Meanwhile the even clique remains balanced through times one, two and three, leaves the balanced regime at time four and becomes constant at time five. Conversely, to survive until time five the even clique must be balanced at time one and still balanced at times two and three. The balance criterion in step 1 forces the odd bridge to change its bit between times one and two; that can occur only in the two pivotal cases above, and their bridge constraints force the displayed initial pattern.

For either \(\mu\in\{0,1\}\), there are \(\binom{2p}{p}\) choices on the odd nondistinguished vertices and \(\binom{2q-1}{q-1}\) on the even nondistinguished vertices; the second binomial is the same for the two possible bridge bits. Thus
\[
N_5=2\binom{2p}{p}\binom{2q-1}{q-1}
=\binom{a-1}{(a-1)/2}\binom{b}{b/2}>0.
\]
The argument is symmetric when the even clique is on the other side. Stirling's central-binomial estimate yields \(N_5/2^{a+b}\sim1/(\pi\sqrt{ab})\) as both sizes tend to infinity through their respective parity classes.

This completes the proof of all claims.

## Verification

The bundled `barbell_verify.py` independently constructs every labelled graph \(B_{a,b}\) for \(3\le a,b\le8\) and updates states directly by bit-mask neighbour counts, without relying on the proof's clique-summary transition rule. It enumerates all \(254016\) labelled initial configurations over these \(36\) graphs and checks their first periodic entry time, primitive period, recurrent-state count and the relevant displayed terminal-depth count. Every state satisfies the stated upper bound; every sharp bound and terminal count matches. The verifier reports `BARBELL_MAJORITY_VERIFY_OK cases=36 labelled_states=254016 nonzero_strata=189`. Run `python3 barbell_verify.py` with Python 3.9 or newer. The recorded output is in `barbell_verify.out`.

These finite computations corroborate the symbolic argument; the proof, not the enumeration, establishes the theorem for unbounded clique sizes.

## Relationship to prior work

Goles and Olivos established the period-two property for synchronous symmetric-threshold systems, including majority voting. Benjamini, Chan, O'Donnell, Tamuz and Tan studied convergence and opinion retention for majority dynamics on random and infinite unimodular graphs. Kaaser, Mallmann-Trenn and Natale studied general voting-time bounds and graph-module contraction and illustrated how dense clique modules speed convergence. None of these general conclusions implies the exact parity-dependent optimum \(2,4,5\), the complete barbell attractor classification, or the terminal binomial counts without the present bridge-resonance analysis. The contraction idea of the last paper is conceptually related but supplies bounds rather than this sharp state census.

A published zero-forcing polynomial of bridge barbells concerns the same underlying graphs but studies propagation under a different, monotone forcing rule; it does not imply synchronous majority trajectories. Published majority classifications on complete split graphs and clique windmills treat different edge sets and have different recurrent populations. The exact bridge-lag mechanism and counts are distinct mathematical statements, although generic period-two convergence and clique-majority facts are pre-existing.

## Limitations

This result only covers two complete cliques with one bridge, sizes at least three, synchronous open-neighbour binary majority and lazy ties. It gives the terminal transient stratum for each parity regime and counts all recurrent states; it does **not** give a closed expression for every intermediate basin-depth stratum or the four fixed-point basin sizes. Exact historical uniqueness has not been established; relevant general threshold-network papers may contain unlocated equivalent specializations. The mathematical proof is finite and self-contained but has not received an independent external audit.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, DOI: 10.1016/0012-365X(80)90121-1.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, first posted 2014-05-11, https://arxiv.org/abs/1405.2486.
3. D. Kaaser, F. Mallmann-Trenn and E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519v1, first posted 2015-08-14, https://arxiv.org/abs/1508.03519.
