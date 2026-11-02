# Isolated period-30 excitation on crown graphs at threshold two

## Finding
Consider the synchronous three-state Greenberg–Hastings model with excitation threshold two on the labelled crown graph \(\operatorname{Cr}_n=K_{n,n}\setminus M\), for every integer \(n\ge1\). Each matched pair consists of vertices \(a_i,b_i\); the edge \(a_i b_i\) is deleted, and all other cross-shore edges are present. States are resting \(0\), excited \(1\), and refractory \(2\). Every excited site advances \(1\mapsto2\), every refractory site advances \(2\mapsto0\), and a resting site advances \(0\mapsto1\) exactly when at least two of its neighbors are excited.

For the full labelled update map \(F_n\),
\[
F_n^{69}=F_n^9\qquad(n\ge1).
\]
Consequently every trajectory enters a periodic orbit after at most nine updates. Nine is sharp: a configuration on \(\operatorname{Cr}_9\) first becomes periodic at update nine. Across the entire graph family, the set of possible eventual *least* periods is exactly
\[
\{1,3,4,6,10,12,30\}.
\]
The long-period resonance is size-isolated: primitive 30-cycles occur **if and only if** \(n=8\). On the labelled graph \(\operatorname{Cr}_8\), there are exactly
\[
\boxed{2688}\quad\text{distinct primitive 30-cycle orbits},
\]
comprising \(80640\) periodic configurations. These are genuine microscopic periods, not merely periods of a population histogram.

## Assumptions and scope
The graph has two labelled shores of equal size \(n\), with one specified perfect matching removed. All updates are simultaneous. Each neighbor is counted once, and excitation requires at least two *distinct* excited neighbors. The result concerns all \(3^{2n}\) initial configurations, without a probabilistic or invariant-measure assumption. The period statement is a family-wise spectrum, not the claim that every size realizes every period.

## Proof
Let \(h_{ab}\) count matched indices \(i\) such that the paired states are \((a_i,b_i)=(a,b)\), for \(a,b\in\{0,1,2\}\). Define the saturated nine-type population vector
\[
c_{ab}=\min\{3,h_{ab}\}\in\{0,1,2,3\}.
\]
For a vertex with paired state \((a,b)\), the number of excited neighbors on its opposite shore is \(E_B-\mathbf1_{\{b=1\}}\) or \(E_A-\mathbf1_{\{a=1\}}\), where \(E_A=\sum_bh_{1b}\) and \(E_B=\sum_a h_{a1}\). The truth of the threshold-two inequality depends only on whether these excited populations are \(0,1,2\), or at least \(3\). Therefore the update of each paired state is a deterministic function of its current state and the saturated vector \(c\).

For each one of the nine initial paired-state types that is actually occupied, attach an *origin tag* tracking the current paired state of every index originally in that type. Identical pairs always evolve identically. The exact next tagged vector is obtained from the current saturated populations and the per-type local update. Each new saturated count is the minimum of three and the sum of the old counts of types mapping to that new type; this is exact because
\[
\min\!\left(3,\sum_j h_j\right)=\min\!\left(3,\sum_j\min(3,h_j)\right).
\]
Hence the finite tagged system exactly preserves microscopic equality for every possible original multiplicity: two successive full configurations agree precisely when every initially occupied origin tag has returned to the same paired state. The nine saturated coordinates range over \(4^9-1=262143\) nonempty possibilities. The tags are *not* identified merely because their population vectors agree; this is essential for distinguishing the least periods \(10\) and \(30\).

The standalone integer verifier `verify.cpp` enumerates every one of these \(262143\) saturated vectors. For each vector it traces the uniquely determined tagged transitions until the complete signature (saturated counts and occupied-origin states) repeats. This is a finite exhaustive proof because the saturation lemma transfers every labelled initial configuration, of any size, to an enumerated signature with exactly the same preperiod and least period. The verified maximum preperiod is nine, and the only detected least periods are \(1,3,4,6,10,12,30\); all seven periods appear. They all divide \(60\), proving \(F_n^{69}=F_n^9\).

Precisely two recurrent saturated vectors have microscopic least period \(30\). In paired-state order
\[
(00,01,02,10,11,12,20,21,22),
\]
their coordinates are \((1,1,1,1,1,1,1,0,1)\) and \((1,1,1,1,1,0,1,1,1)\). Every occupied coordinate equals one. Thus both patterns require exactly eight matched pairs and cannot occur at any other \(n\). Each pattern admits \(8!\) assignments of the eight distinguishable paired-state types to the eight labelled matched indices. These patterns consist exclusively of primitive 30-periodic microscopic states, giving \(2\cdot8!=80640\) periodic states and \(80640/30=2688\) distinct orbits.

A sharp preperiod-nine witness is the capped vector \((0,2,2,2,0,1,0,1,1)\), corresponding to integer encoding \(83112\) in base four, with exactly nine matched pairs. Direct vertex-level simulation gives first-entry time nine and least period four. The verifier's exhaustive preperiod bound proves sharpness.

## Verification
Compile and execute the self-contained standard C++17 program `verify.cpp` with \(`g++ -O3 -std=c++17 -o verify verify.cpp && ./verify`\). Its integer-only exhaustive state traversal checks all \(262143\) saturation profiles, their fully tagged microscopic recurrence, the sharp preperiod, the complete period spectrum, and the exceptional period-30 population profiles. The expected marker is `CROWN_GHM2_VERIFY_OK`; the full run output is in `verify_output.txt`.

Separately run `python3 direct_check.py` to reproduce independent unsaturated, vertex-by-vertex enumeration for \(n=1,2,3,4,5\) (a total of \(66429\) labelled states), and explicit microscopic representatives of the period-30 and preperiod-nine phenomena. The output is in `direct_output.txt`. These finite tests supplement; they are not the reason an all-size claim holds. The saturation lemma and complete tagged enumeration establish the infinite graph family.

## Relationship to prior work
The Greenberg–Hastings threshold family appears in the early work of Durrett–Griffeath (1993) and Fisch–Gravner–Griffeath (1993). The latter work motivates threshold-dependent self-sustaining excitation, but studies spatial lattices and scaling, not the exact crown-graph cycle census. Gravner–Lyu–Sivakoff (2016) proves broad qualitative properties for **threshold one**, which does not imply threshold-two crown counts. Known complete-bipartite threshold-two classifications admit primitive periods \(1,3,4\) and maximum preperiod five; deleting the matching changes the possible periods and yields a primitive period 30 at a unique shore size. The earlier complete-tripartite threshold-two result includes period 12, but neither graph family contains all crown-graph edges as the same dynamics. These are scientific implication comparisons, not merely title comparisons.

## Limitations
The result is an exact computer-assisted finite reduction whose final finite case distinction is supplied as inspectable source rather than a hand-listed table of all \(262143\) cases. It does not establish stability under perturbation, noisy excitation, other thresholds, or arbitrary graph families. No claim is made that all possible related historical manuscripts were accessible. The full texts of the two cited 1993 historical articles were not available in this run, so a possible unindexed exact treatment remains a residual novelty risk.

## References
- R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, first public preprint 1993-03-22, arXiv:patt-sol/9303002, https://arxiv.org/abs/patt-sol/9303002.
- R. Fisch, J. Gravner and D. Griffeath, *Threshold-Range Scaling of Excitable Cellular Automata*, first public preprint 1993-04-02, arXiv:patt-sol/9304001, https://arxiv.org/abs/patt-sol/9304001.
- J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, first public preprint 2016-10-24, arXiv:1610.07320, https://arxiv.org/abs/1610.07320. Its studied rule has one-neighbor excitation, unlike the present threshold-two rule.
