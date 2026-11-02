# Exact recurrent-orbit census for majority dynamics on bouquets of squares

## Finding

For an integer \(k\ge1\), let \(D_k\) be the one-vertex union of \(k\) labelled four-cycles. Under synchronous binary strict majority of graph neighbors, with ties retaining the current bit, all eventual periods divide two. Denote the numbers of fixed configurations and distinct primitive temporal two-cycle orbits by \(E_k\) and \(Q_k\). The exact formulas are

\[
E_k=4^k+\binom{2k}{k},\qquad
Q_k=\sum_{\substack{a,b,c\ge0\\a+b+c=k\\2c<k<2(b+c)}}\frac{k!}{a!b!c!}.
\]

Each primitive two-cycle flips the common hub. Its phase with hub value zero is uniquely described by assigning to each blade one of the three ordered binary triples \(000\), \(101\), or \(111\), where the order runs along the three noncentral vertices of that four-cycle. The counts \(a,b,c\) in the formula refer to these three triples. A choice gives a two-cycle exactly when \(2c<k<2(b+c)\).

Equivalently,

\[
Q_k=\sum_{j=\lfloor k/2\rfloor+1}^{k}\binom kj
\sum_{c=0}^{\min\{j,\lfloor(k-1)/2\rfloor\}}\binom jc.
\]

The asymptotic laws are \(Q_k/3^k\to1\) and

\[
\frac{2Q_k}{E_k+2Q_k}\sim2\left(\frac34\right)^k.
\]

Thus there are exponentially many oscillatory orbits even though a uniformly selected recurrent *configuration* lies on an oscillatory orbit with a probability tending to zero.

## Assumptions and scope

All graphs are finite, undirected, simple, with no loops. For \(i\in\{1,\ldots,k\}\), the \(i\)-th blade is \(h-a_i-b_i-c_i-h\), and vertices in different blades meet only at \(h\). The graph has \(3k+1\) vertices. Vertices carry bits from \(\{0,1\}\). At an update, vertex \(v\) adopts bit one when strictly more than half of its neighbors are one, bit zero when strictly fewer than half are one, and its existing bit when exactly half are one. All vertices update simultaneously. A primitive two-cycle is an unordered temporal orbit \(\{x,F(x)\}\) with \(F^2(x)=x\) and \(F(x)\ne x\). Vertices and blades are labelled; configurations are not quotiented by graph automorphisms.

## Proof

**1. Eventual periods.** Write spins as \(s_v(t)\in\{-1,+1\}\) and choose any fixed \(0<\varepsilon<1\). Let

\[
H_v(t)=\sum_{u\sim v}s_u(t)+\varepsilon s_v(t),\qquad
W_t=\sum_vs_v(t+1)H_v(t).
\]

The local update is \(s_v(t+1)=\operatorname{sgn}H_v(t)\), with \(H_v(t)\ne0\) because neighbor sums are integers. Therefore \(W_t\ge\sum_vs_v(t-1)H_v(t)=W_{t-1}\), where the equality uses symmetry of adjacency. Equality holds only when every \(s_v(t+1)=s_v(t-1)\). Because the state space is finite, \(W_t\) is bounded and takes finitely many values, so eventually equality holds; all trajectories then have period at most two. The argument also proves this standard fact without an appeal to finite sampling.

**2. Fixed states.** Fix hub bit \(h=0\). On a blade, writing the nonhub triple as \((a,b,c)\), the local update is

\[
F_0(a,b,c)=(a\wedge b,\operatorname{maj}(a,b,c),c\wedge b).
\]

Exactly four triples are locally fixed: \(000,011,110,111\). They contribute respectively \(0,1,1,2\) one-bits to the two neighbors of the hub. Thus the polynomial that records the number of hub-neighbor one-bits per blade is \(1+2z+z^2=(1+z)^2\). Hub zero is fixed if the total number is at most \(k\) (ties retain zero); there are \(\sum_{j=0}^k\binom{2k}{j}\) fixed states with hub zero. Bit complementation gives the same count with hub one. Since \(\sum_{j=0}^k\binom{2k}{j}=2^{2k-1}+\tfrac12\binom{2k}{k}\), the total is exactly \(E_k=4^k+\binom{2k}{k}\).

**3. The hub must change in every primitive two-cycle.** If the hub stays zero during a periodic trajectory, each blade endpoint satisfies \(a(t+1)=a(t)\wedge b(t)\) and \(c(t+1)=c(t)\wedge b(t)\). Such endpoint bits are nonincreasing and therefore constant on a periodic trajectory. With the two endpoint bits constant, the middle bit evolves by \(b(t+1)=\operatorname{maj}(a,b(t),c)\), which is either constant or the identity, never a primitive two-cycle. If the hub stays one, both endpoints are nondecreasing because their update is an OR, and the same conclusion holds. Hence in every nonfixed recurrent orbit the hub flips every time.

**4. Exhaustive local two-cycle table.** In a hub-zero phase followed by hub one, the three nonhub bits satisfy \(F_1(F_0(a,b,c))=(a,b,c)\), where

\[
F_1(a,b,c)=(a\vee b,\operatorname{maj}(a,b,c),c\vee b).
\]

A direct check of the eight possible binary triples leaves exactly these rows:

| Hub-zero triple | Hub-one triple | Hub-zero neighboring one-bits | Hub-one neighboring one-bits |
| --- | --- | ---: | ---: |
| \(000\) | \(000\) | \(0\) | \(0\) |
| \(101\) | \(010\) | \(2\) | \(0\) |
| \(111\) | \(111\) | \(2\) | \(2\) |

Let \(a,b,c\) count these three choices across the \(k\) labelled blades. The hub goes from zero to one precisely if \(2(b+c)>k\), and it goes from one back to zero precisely if \(2c<k\). Both inequalities must be strict because hub ties preserve its current state. For any such choice the local table and hub inequalities ensure a genuine two-cycle. Conversely the preceding arguments show that every two-cycle occurs this way. There are \(k!/(a!b!c!)\) assignments of the three blade types with these counts, and each orbit has exactly one hub-zero phase. Summation proves the formula for \(Q_k\).

The equivalent nested binomial form follows by putting \(j=b+c\), choosing the \(j\) nonzero-endpoint blades and then the \(c\) constant-one blades among those \(j\).

**5. Asymptotics.** For a uniformly random assignment of the three blade types, \(Q_k/3^k\) is the probability that \(2c<k<2(b+c)\), for a multinomial vector with equal probabilities \(1/3\). The law of large numbers gives \(c/k\to1/3\) and \((b+c)/k\to2/3\), hence this probability tends to one. In fact, Hoeffding bounds show its complement has probability at most \(2e^{-k/18}\). Finally \(\binom{2k}{k}=o(4^k)\), so \(E_k\sim4^k\), giving the claimed recurrent-configuration proportion.

## Verification

The included standard-library Python program `verify.py` independently constructs each graph and directly evaluates the simultaneous neighbor-majority update for every binary state of \(D_k\), \(1\le k\le6\). It checks fixed configurations and unordered primitive two-cycles against both binomial forms. This comprises exactly \(599184\) directly evaluated configurations. A separate eight-state local check confirms the fixed/traversing blade tables; formula-equivalence checks continue through \(k=150\). The accompanying `verify_output.txt` contains the actual program output. These finite tests corroborate, but do not establish, the all-size formulas: the proof above supplies that extension.

| Number of squares \(k\) | Fixed configurations \(E_k\) | Primitive two-cycle orbits \(Q_k\) |
| ---: | ---: | ---: |
| 1 | 6 | 1 |
| 2 | 22 | 1 |
| 3 | 84 | 13 |
| 4 | 326 | 21 |
| 5 | 1276 | 141 |
| 6 | 5020 | 283 |

## Relationship to prior work

Tamuz and Tessler (2013 preprint, revised 2014) study majority dynamics, Lyapunov functions, information retention, and synchronous/asynchronous convergence, not the present one-point unions of four-cycles. Benjamini et al. (2014 preprint) record the Goles–Olivos finite period-two theorem and prove broader convergence statements for unimodular networks and random graphs; those results do not count the periodic configurations or distinguish the three blade types here. Kaaser, Mallmann-Trenn and Natale (2016) bound voting time and study graph modules but do not provide a square-bouquet orbit count in their inspected results. The graph family is the quadrilateral Dutch windmill construction. The present proof turns its shared-cutvertex geometry into exact enumerative constraints; it does not claim novelty for the general period-two theorem, binomial coefficients, or standard concentration inequalities.

## Limitations

Only synchronous binary majority with retention on ties is treated, and all square blades must share a *single* hub. The result gives the recurrent census, not an exact basin-size distribution or a sharp global transient maximum. The finite numerical checks do not prove the general theorem, and historical priority cannot be certified against every unindexed or inaccessible source. A different rule (e.g. strict majority with a fixed tie-breaking bit, or asynchronous updates) is outside scope.

## References

1. O. Tamuz and R. J. Tessler, *Majority Dynamics and the Retention of Information*, arXiv:1307.4035, initially submitted 2013-07-15. https://arxiv.org/abs/1307.4035
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486, initially submitted 2014-05-11. https://arxiv.org/abs/1405.2486
3. D. Kaaser, F. Mallmann-Trenn, and E. Natale, *On the Voting Time of the Deterministic Majority Process*, MFCS 2016, DOI:10.4230/LIPIcs.MFCS.2016.55. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2016.55
4. E. W. Weisstein, *Dutch Windmill Graph*, MathWorld, graph-family definition. https://mathworld.wolfram.com/DutchWindmillGraph.html
