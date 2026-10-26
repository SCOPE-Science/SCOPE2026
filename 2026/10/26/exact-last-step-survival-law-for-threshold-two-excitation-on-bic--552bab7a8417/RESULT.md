# Exact last-step survival law for threshold-two excitation on bicliques

## Finding

Let \(a,b\ge1\), and let \(F\) denote the deterministic simultaneous three-state Greenberg–Hastings update on the labelled, simple, loopless complete bipartite graph \(K_{a,b}\), with resting \(0\), excited \(1\), and refractory \(2\). A state \(1\) changes to \(2\), and state \(2\) changes to \(0\). A resting vertex becomes excited exactly when **at least two distinct neighbours are excited**; otherwise it remains resting. Define the first-periodic-entry time \(\tau(x)=\min\{t\ge0:F^t(x)\text{ lies on a periodic orbit}\}\).

For every positive integer \(n\), define
\[
P_n=\sum_{j=2}^{n-2}\binom nj2^{n-j},\qquad
Q_n=\begin{cases}n,&n\ge3,\\0,&n\le2.\end{cases}
\]
Empty sums are zero. The number of labelled initial states entering their eventual periodic orbit **for the first time at update five** is exactly
\[
\boxed{N_5(a,b)=2\bigl(P_aQ_b+Q_aP_b\bigr).}
\]
Equivalently, \(\tau(x)=5\) if and only if, up to exchanging the parts, one part contains at least two excited and at least two nonexcited vertices, and the other contains at least two resting vertices and **exactly one** excited-or-refractory vertex. The two orientations are mutually exclusive. Consequently, \(F^5(x)\) is always periodic, and the sharp maximum of \(\tau\) equals five precisely when \(\min(a,b)\ge3\) and \(\max(a,b)\ge4\). On \(K_{3,4}\), exactly \(144\) of its \(2187\) labelled initial states have this last-step delay, even though all trajectories on this graph eventually extinguish.

For \(n\ge3\), inclusion–exclusion gives
\[
P_n=3^n-2^n-n2^{n-1}-2n-1.
\]
In particular, on balanced graphs the maximal-depth probability is
\[
\frac{N_5(n,n)}{3^{2n}}=\frac{4nP_n}{3^{2n}}\sim\frac{4n}{3^n}.
\]
Thus maximal-delay configurations become exponentially rare even while such configurations continue to exist.

## Assumptions and scope

The bipartite parts are fixed, labelled sets of sizes \(a,b\ge1\). All \(3^{a+b}\) initial colourings are included, with no distributional or genericity assumption. Updates are synchronous; neighbours exclude the vertex itself; the excitation threshold is exactly two. The preperiod \(\tau\) is defined using the full labelled microstate, not merely population counts. No assertion is made for other thresholds, directed edges, asynchronous dynamics or arbitrary graphs.

## Proof

**Step 1: a lossless finite quotient.** In each bipartition part, divide vertices by their *initial* colour. Vertices in the same initial-colour class have identical neighbours and identical starting states. Hence they retain identical states at every time. Write the three initial class sizes as \((r,e,h)\), for resting, excited and refractory. The only graph information needed to update any class is whether the number of excited vertices in the opposite part is at least two. Define the clipping map \(\operatorname{cap}(m)=\min(m,2)\). For any nonnegative class sizes \(m_i\), and any subset of the three initial classes, the sum \(\sum m_i\ge2\) holds if and only if \(\sum\operatorname{cap}(m_i)\ge2\). Thus clipping each of the six class sizes preserves *all* excitation predicates at all times, and preserves the complete itinerary of every nonempty initial class. Empty classes are ignored, not treated as artificial vertices.

Each part's three clipped class sizes range over \(\{0,1,2\}^3\) excluding the all-zero vector, giving exactly \((3^3-1)^2=676\) admissible six-tuples. For every such tuple, initialize the states of nonempty class types at \((0,1,2)\), and update according to the stated rule while treating the fixed clipped sizes as multiplicities. There are at most \(3^6=729\) distinguishable class-state tuples, so exact orbit detection by first repetition is terminating and exhaustive. It yields the first-periodic-entry time of the *original microstate* for any actual class sizes realizing that clip. This is a finite reduction valid for arbitrarily large \(a,b\), not an extrapolation from finitely many graph sizes.

**Step 2: the full certificate and terminal predicate.** The standalone standard-library program `verify_bipartite_ghm.py` enumerates every one of the \(676\) admissible clips and computes the complete class-state orbit from its first appearance until first repetition. The resulting exact table (row = preperiod, column = primitive period; zeros omitted) is

| Preperiod | Period 1 | Period 3 | Period 4 |
|---:|---:|---:|---:|
| 0 | 4 | 1 | 2 |
| 1 | 60 | 0 | 10 |
| 2 | 324 | 0 | 30 |
| 3 | 160 | 0 | 8 |
| 4 | 51 | 0 | 2 |
| 5 | 24 | 0 | 0 |

The entries count **clipped class-size types**, not numbers of labelled configurations. The checker verifies separately for all \(676\) types that preperiod five occurs exactly for two mutually exclusive cases: a *thin* part with \(\operatorname{cap}(r)=2\) and either \((\operatorname{cap}(e),\operatorname{cap}(h))=(1,0)\) or \((0,1)\); and a *fat* opposite part with \(\operatorname{cap}(e)=2\) and \(\operatorname{cap}(r)+\operatorname{cap}(h)\ge2\). Their orientations may be exchanged. Because the checker explores the entire finite quotient with exact integers and tests this structural condition for every type, its successful result proves both necessity and sufficiency, along with the uniform five-update bound. The entire enumeration, including transition and class-empty handling, appears in the embedded code and may be replayed.

**Step 3: exact labelled count.** Fix an orientation. For a fat part of size \(a\), choose \(j\ge2\) excited vertices and require at least two remaining vertices; assign each remaining vertex state zero or two. This gives
\[
P_a=\sum_{j=2}^{a-2}\binom aj2^{a-j}.
\]
For the thin part of size \(b\), select its unique nonrest vertex in \(b\) ways and choose its state \(1\) or \(2\), giving \(2Q_b\). Hence this orientation contributes \(2P_aQ_b\). The reverse contributes \(2Q_aP_b\), without double counting because a thin part has at most one excited vertex and a fat part has at least two. This proves the claimed formula.

**Step 4: sharpness and asymptotics.** The fat condition is realizable exactly for part size at least four; the thin condition exactly for size at least three, proving the iff threshold. The finite quotient table ensures no preperiod greater than five. For \(n\ge3\), subtract from the \(3^n\) three-colour assignments those having fewer than two excited vertices and those having fewer than two nonexcited vertices; these excluded events are disjoint when \(n\ge3\), giving the displayed expression for \(P_n\). Since \(P_n/3^n\to1\), the balanced probability is asymptotic to \(4n/3^n\), as asserted.

## Verification

Run `python3 verify_bipartite_ghm.py`. The executable independently checks the 676 exact capped signatures, the terminal predicate for all of them, the complete preperiod/primitive-period table and size-dependent sharpness for 36 ordered part-size pairs up to six. An independent vertex-labelled implementation then enumerates all \(560124\) configurations across the six part-size pairs \((1,1),(2,3),(3,4),(4,4),(4,5),(6,6)\), reproducing the last-step formula and periodic-state counts. The output is included verbatim as `ghm_verification_output.txt`.

These labelled finite examples are corroboration. The all-parameter proof is the exact finite clipped-class reduction and complete 676-state-type certificate, plus the combinatorial counting argument.

## Relationship to prior work

Threshold-two finite excitation belongs to the Greenberg–Hastings class studied by Durrett and Griffeath (1993), whose focus is planar lattices and spiral-core phase behaviour. Doba (2018) and Gravner–Lyu–Sivakoff (2018) analyze three-state excitation on arbitrary finite graphs under **one-excited-neighbour contact**, not the two-neighbour rule of this result. An earlier analysis of the same two-threshold complete-bipartite model already established the five-update global bound, sharpness when both parts have size at least four, and a period-\(1,3,4\) recurrent-state count. Those results are retained as prior context, not claimed as new here. The contribution is the precise classification and labelled count of **which initial states require all five updates**, including sharpness at the previously unresolved asymmetric \((3,4)\) boundary and exponential rarity on balanced graphs. Neither period counts nor a maximum-time bound alone determines this initial-state stratum.

## Limitations

The originality comparison is bounded by the inspected sources and accessible records; an unindexed equivalent maximal-depth formula is possible. The proof concerns a deterministic complete-bipartite graph, exactly three states and threshold two. Finite verification is not independent mathematical review. The incidence of a rare maximal-depth configuration need not predict stochastic excitation with noise, external forcing or a different network topology.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, first submitted 1993-03-22. https://arxiv.org/abs/patt-sol/9303002
2. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems 27 (2018), 101–126. https://wpmedia.wolfram.com/sites/13/2018/09/27-2-1.pdf
3. J. Gravner, H. Lyu and D. Sivakoff, *Limiting Behavior of 3-Color Excitable Media on Arbitrary Graphs*, Annals of Applied Probability 28 (2018), 3324–3357. https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf
