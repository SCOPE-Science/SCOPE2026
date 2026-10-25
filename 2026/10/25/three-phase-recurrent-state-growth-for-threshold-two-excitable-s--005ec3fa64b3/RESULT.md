# Three-phase recurrent-state growth for threshold-two excitable split graphs

## Finding

On the labelled complete split graph \(S_{a,b}=K_a\vee\overline{K_b}\), with integers \(a,b\ge1\), use synchronous three-state Greenberg–Hastings updating with states \(0\) (rest), \(1\) (excited), \(2\) (refractory): \(1\mapsto2\mapsto0\), and a resting vertex becomes excited if and only if at least two distinct neighbours are excited. The update \(F\) satisfies, **uniformly in the two graph sizes**,
\[
F^8=F^5.
\]
The five-step entry bound is sharp, as witnessed on \(S_{3,3}\). The only periodic states are the all-zero fixed state and configurations of prime period three in which **every vertex advances at each update**.

For an initial configuration let \(c_j\) be the number of clique vertices in state \(j\), and \(i_j\) the number of independent-set vertices in state \(j\), for \(j\in\{0,1,2\}\), reading indices modulo three. Then a nonzero state is periodic exactly when
\[
\begin{aligned}
 c_j>0&\Longrightarrow c_{j+1}+i_{j+1}\ge2,\\
 i_j>0&\Longrightarrow c_{j+1}\ge2
\end{aligned}\qquad (j=0,1,2).
\]
Hence the exact number of labelled periodic configurations is
\[
R(a,b)=1+\!\!\sum_{\substack{c_0+c_1+c_2=a\\ i_0+i_1+i_2=b\\c_j,i_j\ge0}}
\frac{a!}{c_0!c_1!c_2!}\frac{b!}{i_0!i_1!i_2!}
\prod_{j=0}^2
\mathbf1_{\{c_j=0\ \mathrm{or}\ c_{j+1}+i_{j+1}\ge2\}}
\mathbf1_{\{i_j=0\ \mathrm{or}\ c_{j+1}\ge2\}}.
\]
All \(R(a,b)-1\) nonzero periodic states belong to \((R(a,b)-1)/3\) distinct primitive three-cycles.

There are three sharply different fixed-clique, growing-fringe regimes:
\[
\begin{array}{ll}
1\le a\le3:&R(a,b)=1;\\[2pt]
a=4:&R(4,b)=1+18(2^b-b-1);\\[2pt]
a=5:&R(5,b)=1+150(2^b-1)-60b;\\[2pt]
a\ge6:&R(a,b)=N_a3^b+O_a(2^b),
\end{array}
\]
where, for \(a\ge6\),
\[
N_a=3^a-3(2^a+a2^{a-1})+3(a^2+a+1)>0.
\]
Thus the exponential growth rate \(\lim_{b\to\infty}b^{-1}\log R(a,b)\) jumps from \(0\) to \(\log2\) to \(\log3\) as \(a\) passes from at most three through four–five to at least six.

## Assumptions and scope

Graphs are undirected, simple and labelled. Clique and independent-set sizes are positive integers. All updates are simultaneous, with no external stimulation or stochastic excitations. The excitation threshold counts **distinct neighbours**, not the vertex itself. The initial colour of each vertex is chosen from \(\{0,1,2\}\), and recurrent means periodic under the finite deterministic map. A transient length is the least nonnegative number of updates required to enter a periodic state.

## Proof

**1. Exact six-class reduction.** Split each of the clique and fringe into its three *initial* colour classes. All vertices in an initial class remain in the same state, because class members start identically and each resting clique vertex sees exactly the total number of excited clique vertices plus excited fringe vertices; its own contribution is zero. A resting fringe vertex sees exactly the number of excited clique vertices. For each of the six initial classes retain its common current state, as well as its initial multiplicity. Only whether any excited-neighbour total is zero, one or at least two matters. Consequently replacing each initial multiplicity by its truncation \(\min(2,\text{multiplicity})\) preserves the current state of every nonempty initial class at every update, by induction. There are exactly \(3^6=729\) truncated-multiplicity profiles (including empty parts, which cause no difficulty). The six-class update is fully specified by the preceding two excitation tests and by \(0\mapsto (1\text{ if excited-neighbour total}\ge2,\ 0\text{ otherwise}),1\mapsto2,2\mapsto0\).

**2. Exhaustive finite certificate and uniform bound.** The standalone `verify.py` enumerates all 729 profiles, begins every nonempty initial class at its defining initial phase, performs eight updates using the exact six-class map, and checks equality at updates five and eight for every nonempty class. This is an exhaustive *finite proof after the reduction*, not an inference from samples of graph sizes. It establishes \(F^8=F^5\) for every \(a,b\ge1\). The labelled configuration \((0,0,1\mid1,2,2)\) on \(S_{3,3}\) evolves by
\[
(001\mid122)\to(112\mid200)\to(220\mid011)\to
(001\mid022)\to(002\mid000)\to(000\mid000).
\]
The state at update four is not periodic, so the bound five is attained.

**3. Periodic-state classification.** Because \(F^8=F^5\), restriction of \(F^3\) to the eventual recurrent image is the identity: every prime period divides three. A vertex on a period-three orbit is either forever resting or passes through \(0\to1\to2\to0\) at each three-step cycle, because every excitation forces a two-step refractory sequence. If any clique vertex rotates, no clique vertex can remain forever resting: at a time when the rotating vertex is resting and becomes excited, the same global excitation threshold is satisfied at every resting clique vertex. Some clique vertex must rotate whenever activity persists; otherwise no fringe vertex could be excited. If a fringe vertex rotates, the same shared threshold implies that no other fringe vertex can remain forever resting. If instead all fringe vertices remained forever resting, then a rotating clique vertex would need at least two excited clique neighbours at one of its resting-to-excited steps, which would also excite the resting fringe vertices, a contradiction. Thus a nonzero recurrent configuration consists entirely of rotating vertices. Following the three global phases gives precisely the displayed inequalities, which are also sufficient. Every nonzero periodic orbit therefore has least period three.

**4. Enumeration and asymptotics.** For prescribed two triples of phase counts, there are \(a!/(c_0!c_1!c_2!)\) labelled clique states and \(b!/(i_0!i_1!i_2!)\) labelled fringe states. Summing exactly over the inequalities proves the formula. If \(a\le3\), no three-phase assignment satisfies them. If \(a=4\), the clique counts must be a rotation of \((0,2,2)\); for each such pattern the fringe may use two prescribed phases, with at least two vertices in one phase, giving \(18(2^b-b-1)\). If \(a=5\), the admissible clique patterns are rotations of \((1,2,2)\), contributing \(90(2^b-1)\), and rotations of \((0,2,3)\) or \((0,3,2)\), contributing \(60(2^b-b-1)\). For \(a\ge6\), core assignments with each colour represented at least twice permit every fringe assignment, giving \(N_a3^b\). All other core assignments allow at most two fringe colours, and hence contribute at most \(O_a(2^b)\). Inclusion–exclusion over the three colours gives the displayed formula for \(N_a\). This proves the growth-rate trichotomy.

## Verification

Running `python verify.py` (standard library only) returns `VERIFY_OK`. It checks every one of the 729 truncated six-class profiles, checks the recurrent-state condition on the same finite reduction, independently iterates 29,169 labelled states for eleven small graph pairs, compares each with the multinomial sum, tests the small-clique formulas for fringe sizes through eleven, and checks the five-step witness. The recorded result is `verify_output.txt`. This direct small-graph enumeration is corroboration; the all-size theorem relies on the proved exact reduction and its exhaustive finite certificate.

## Relationship to prior work

Greenberg–Hastings cellular automata and contact-threshold wave dynamics are classical [1,2]. The classical notion of stable periodic objects anticipates sufficient rotating-phase support constraints [2]; the new assertions are that these constraints classify **all** recurrent states on every complete split graph at threshold two, that the transient bound is universally five and sharp, and that exact labelled counts have three fringe-growth regimes. Work on excitation in scale-free networks [3] uses an external-stimulus/stochastic activation model and does not imply these deterministic finite-graph counts. Graph-wide deterministic GH analysis with threshold one [4] and threshold-two results on infinite regular trees [5] likewise use different assumptions and do not provide the split-graph census. Complete bipartite and complete split graphs must not be conflated: adding all clique edges changes the excitation tests.

## Limitations

The theorem concerns exactly three states, threshold two, and complete split graphs; it does not assert a corresponding result for higher thresholds, other graph joins, asynchronous updates or stochastic forcing. The finite certificate checks a mathematically complete reduction but is not an independently formalized machine proof. Originality is assessed against the accessible literature and mathematical research records; an unindexed equivalent treatment cannot be excluded. There has been no independent audit.

## References

1. R. Durrett and J. E. Steif, *Some rigorous results for the Greenberg–Hastings model*, Journal of Theoretical Probability 4 (1991), 669–690, DOI: 10.1007/BF01259549.
2. R. Fisch, J. Gravner and D. Griffeath, *Threshold-range scaling of excitable cellular automata*, Statistics and Computing 1 (1991), 23–39; arXiv:patt-sol/9304001v1 (posted 1993-04-02); accessible journal copy: https://www.stat.cmu.edu/~cshalizi/462/readings/fgg.pdf, DOI: 10.1007/BF01890834.
3. A.-C. Wu, X.-J. Xu and Y.-H. Wang, *Excitable Greenberg–Hastings cellular automaton model on scale-free networks*, arXiv:cond-mat/0701248v1 (first submitted 2007-01-11), DOI: 10.1103/PhysRevE.75.032901.
4. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems 27 (2018), 101–126, DOI: 10.25088/ComplexSystems.27.2.101.
5. J. Bello and D. Sivakoff, *Cyclic Cellular Automata and Greenberg–Hastings Models on Regular Trees*, arXiv:2108.06404 (2021).
