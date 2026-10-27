# Exact basin spectrum and sharp four-step relaxation for excitation on friendship graphs

## Finding

Let \(r\geq1\) be an integer and let \(G_r\) be the friendship graph formed by identifying one vertex (the hub) of \(r\) disjoint triangles. The two nonhub vertices of blade \(i\) are ordered and denoted \(a_i,b_i\). Equip every vertex with a state in \(\{0,1,2\}\) and update synchronously by the three-state Greenberg–Hastings rule: \(1\mapsto2\), \(2\mapsto0\), and \(0\mapsto1\) exactly when at least one neighbor has state \(1\); otherwise \(0\mapsto0\). Write \(F_r\) for this map.

A blade is **active** in an initial configuration if its three vertices have pairwise distinct states (a *rainbow triangle*). Its orientation is the order of the two nonhub states relative to the hub. Activity and orientation remain invariant under the dynamics. For each \(k=1,\ldots,r\), exactly
\[
\binom rk 2^k
\]
primitive three-cycles have exactly \(k\) active blades, and **each such cycle has exactly**
\[
3\,7^{r-k}
\]
initial configurations in its full basin. There is exactly one fixed point, the all-zero configuration, whose basin has exactly \(3\,7^r\) configurations. No other periodic orbits exist. In particular, the total number of primitive three-cycles is \(3^r-1\).

All configurations enter their eventual periodic orbit in at most four synchronous updates: \(F_r^7=F_r^4\). The sharp maximum first-entry time is \(3\) for \(r=1\) and \(4\) for every \(r\ge2\). With independent uniform initial states, the number of active blades is binomial with parameters \(r\) and \(2/9\); the exact extinction probability is \((7/9)^r\). The active-blade count determines the basin-size level but not the orientation of the selected attractor.

## Assumptions and scope

Vertices and blades are labelled. A state is a vector \(x=(h,a_1,b_1,\ldots,a_r,b_r)\in\{0,1,2\}^{2r+1}\). The hub is adjacent to both vertices of every blade, and there is one edge joining the two vertices of each blade. There are no edges between distinct peripheral blades. The rule is deterministic, synchronous, threshold one, with exactly three states, no self-loop and no stochastic forcing. The basin of a periodic orbit consists of *all* initial configurations whose forward trajectory eventually reaches any state on that orbit. The first-entry time is the least nonnegative \(t\) for which \(F_r^t(x)\) lies on a periodic orbit.

A fixed active blade's orientation is preserved as the three states rotate; the \(k\) active blades and their two possible orientations therefore label distinct eventual three-cycles. For each phase of the hub, each inactive blade has seven possible initial ordered peripheral pairs and each active blade has one initial ordered pair of its assigned orientation.

## Proof

**Step 1: triangle preservation.** If one blade begins with states \(0,1,2\) in some order, then its three vertices all increase by one modulo three in the next update. In particular, if the hub is at \(0\), it has a neighbor at \(1\); if a peripheral vertex is at \(0\), it similarly has a neighbor at \(1\). The remaining updates \(1\mapsto2\) and \(2\mapsto0\) are automatic. This argument repeats indefinitely: an active blade keeps its orientation and forces the hub along \(0\to1\to2\to0\). Other blades cannot affect this forced rotation.

**Step 2: local driven-wing classification.** For a fixed hub state \(h\), the update of one ordered wing pair is \(U_h(a,b)=(f_h(a,b),f_h(b,a))\), where
\[
f_h(a,b)=\begin{cases}(a+1)\bmod3,&a\in\{1,2\},\\ \mathbf1_{\{h=1\text{ or }b=1\}},&a=0.\end{cases}
\]
With a rotating hub \(h_t=(h_0+t)\bmod3\), the three permissible periodic wing pairs at hub phase \(1\) are \((0,0),(0,2),(2,0)\). They rotate respectively to \((1,1),(1,0),(0,1)\) at hub phase \(2\), and to \((2,2),(2,1),(1,2)\) at hub phase \(0\), before returning. The first pair at each phase is passive, and the other two have the two rainbow orientations.

For completeness, the local update can be checked for the \(3\times9=27\) choices of initial hub state and ordered wing pair. After four updates with the rotating hub, every nonrainbow initial pair has reached the *passive* pair for the current hub phase, whereas each rainbow pair retains its original orientation. Three further updates return each pair exactly. These are local, finite identities, independent of the number of blades; `verify.py` exhausts their twenty-seven input cases. Thus if at least one initial blade is rainbow, the entire configuration is on a primitive three-cycle by time four. Primitive period one is impossible in this case because the hub rotates.

**Step 3: absence of active blades.** There are six unordered peripheral-pair types \((0,0),(0,1),(0,2),(1,1),(1,2),(2,2)\), and for any fixed hub value exactly five are nonrainbow. If no blade is rainbow initially, the set of present unordered pair types has one of \(2^5-1=31\) nonempty supports. Its future is completely determined by that support and the hub: multiplicities do not affect whether the hub sees a state \(1\), and each individual pair evolves by \(U_h\). Thus only \(3(2^5-1)=93\) support cases require checking, independently of \(r\).

The hub sequences in these cases, for times zero through four, are exactly
\[
(0,0,0,0,0),\quad(0,1,2,0,0),\quad(1,2,0,0,0),\quad(2,0,0,0,0).
\]
The first occurs when the hub begins at zero and no peripheral vertex is excited; the second when it begins at zero and some peripheral vertex is excited; the last two correspond to initial hub states one and two. Direct substitution in the five permitted pair types for each initial hub state shows that in every case the hub and all pairs are zero at time four. The certificate in `verify.py` iterates all ninety-three supports and checks this exact conclusion, independently of any full-graph search. Hence \(F_r^4(x)=0\) for every configuration with no active blade.

**Step 4: count and identify attractors.** Any periodic state other than zero has an active blade by Step 3; the hub rotates by Step 1. Every such state at hub phase \(1\) therefore has exactly one of \((0,0),(0,2),(2,0)\) on each blade. The all-passive choice has no active blade and hence cannot be periodic with a rotating hub. Every other choice is manifestly a three-cycle, yielding \(3^r-1\) cycles. Exactly \(\binom rk2^k\) choices have \(k\) active blades.

Fix one such cycle. At any prescribed initial hub state, the orientation of each active blade forces the unique ordered pair consisting of the other two states. Each inactive blade can begin in any of the seven pairs *not* completing a rainbow with that hub state. Steps 1–3 show that these are precisely the configurations converging to the selected cycle. The three possible initial hub states contribute equally, giving the basin size \(3\,7^{r-k}\). When there are no active blades, all initial states converge to zero, giving its basin size \(3\,7^r\). Summing all basin sizes yields
\[
3\,7^r+\sum_{k=1}^r\binom rk 2^k\,3\,7^{r-k}=3\,9^r=3^{2r+1},
\]
which independently checks that the basins partition the entire configuration space.

**Step 5: sharp entry-time bound.** Steps 2–3 give \(F_r^7=F_r^4\) for every \(r\). For \(r\ge2\), start with hub zero, first blade \((0,1)\), and all other blades \((0,0)\). After three updates at least one of the other blades is in state \((2,2)\), so the configuration is not on its eventual zero fixed point; after four updates every vertex is zero. Hence the bound four is sharp. When \(r=1\), direct enumeration of the three hub values and nine ordered pairs (also verified in `verify.py`) gives sharp bound three; for example \((h,a_1,b_1)=(0,0,1)\) reaches zero at its third update, not earlier.

## Verification

The standalone standard-library Python program `verify.py` reproduces the proof-critical finite tables (all ninety-three nonrainbow supports and all twenty-seven periodically driven wing pairs). It also independently enumerates **every labelled state** for \(r=1,2,3,4,5\), respectively \(27,243,2187,19683,177147\) states, checking \(F_r^7=F_r^4\), the sharp entry-time maxima, the basin size of every individual cycle, and the total number of cycles at every active-blade count. Run `python3 verify.py`; the captured output is in `verification_output.txt`. The finite table verifications prove the requisite local identities for *all* \(r\); the larger full-state enumerations are independent corroboration, not an extrapolation to untested \(r\).

## Relationship to prior work

The classical Greenberg–Hastings model was studied by Durrett and Steif (1991) and Durrett and Griffeath (1993), primarily for lattice systems. Gravner, Lyu and Sivakoff (first publicly posted 24 October 2016) give a general graph circulation criterion for three-state excitation (Theorem 3), and a bound of \((7/9)^k\) for synchronization from certain systems of cycles (Theorem 5). Doba (2018, Theorem 1) independently provides a general finite-graph criterion in terms of cycle phase differences. Specialized to a bouquet of triangles, the general circulation criterion already distinguishes extinction from persistent excitation. **That binary extinction criterion is not claimed as novel.**

The contribution here is the complete *attractor-resolved* basin spectrum, the exact multiplicity of every basin-size level, and the sharp uniform four-update entrance cutoff, all for shared-hub triangle windmills. In this family the synchronization probability is exactly \((7/9)^r\): equality occurs for triangles sharing a hub under the Greenberg–Hastings rule, whereas the cited general bound notes a sufficient equality case of vertex-disjoint triangles under the cyclic cellular automaton. The sources inspected do not state the joint per-cycle basin formula or the sharp four-step bound for this graph family.

## Limitations

The assertions are limited to deterministic, synchronous, three-state, threshold-one excitation on labelled friendship graphs. They do not extend automatically to longer cycle bouquets, more colors, asynchronous updates, different thresholds, or noisy transmission. No distribution of *individual* preperiod depths beyond the sharp maximum is asserted. General prior graph-circulation results cover part of the extinction/nonextinction dichotomy; novelty is therefore claimed only for the quantified orbit/basin/cutoff refinement. A limited search and inspection cannot exclude an equivalent unindexed finite-state computation. Self-review is not independent validation.

## References

1. R. Durrett and J. E. Steif, “Some Rigorous Results for the Greenberg–Hastings Model,” *Journal of Theoretical Probability* **4** (1991), 669–690, DOI `10.1007/BF01259549`.
2. R. Durrett and D. Griffeath, “Asymptotic Behavior of Excitable Cellular Automata,” first arXiv public submission 22 March 1993, `patt-sol/9303002`; *Experimental Mathematics* **2** (1993), 183–208, DOI `10.1080/10586458.1993.10504277`.
3. J. Gravner, H. Lyu and D. Sivakoff, “Limiting Behavior of 3-Color Excitable Media on Arbitrary Graphs,” arXiv `1610.07320`, version 1 publicly posted 24 October 2016; *Annals of Applied Probability* **28** (2018), 3324–3357, DOI `10.1214/17-AAP1350`.
4. N. Doba, “The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph,” *Complex Systems* **27** (2018), 101–126, DOI `10.25088/ComplexSystems.27.2.101`.
