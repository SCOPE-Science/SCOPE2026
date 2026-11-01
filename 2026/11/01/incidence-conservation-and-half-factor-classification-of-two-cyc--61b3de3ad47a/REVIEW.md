# Scientific review

## Correctness — PASS

The claimed all-graph result is established by a direct proof, not by interpolation from enumerated graphs. For a line-graph site corresponding to \(uv\), the exact active-neighbor count is \(h_u+h_v-2x_{uv}\); parity compatibility makes the strict majority threshold integral. This yields the three-branch update formula in the result. In a two-cycle, the update inequalities imply \(\delta_{uv}(\Delta_u+\Delta_v)\le0\). Summing gives the decisive nonnegative sum of squares \(\sum_v\Delta_v^2\), forcing all vertex incidence-count changes to vanish. The classification then follows in both directions: high edges stay one, low edges stay zero and equality edges complement with exactly half of their incidences active. The coefficient formula counts distinct half-factors, and the division by two pairs the two states of each nontrivial orbit. The Eulerian and bridge consequences are valid for any finite simple graph satisfying the stated parity condition.

Both programs replayed successfully from their packaged source. The Python program exhausts every labelled graph of at most five vertices, checking all 154 eligible graphs and their 4,909 edge states. The independently written C++ program checks complete-graph bases through seven vertices and three additional graph families. The 1980 period-two theorem is used only for the statement that all eventual recurrent orbits have period at most two; the new incidence and classification claims are proved directly. A three-vertex path demonstrates that the parity condition cannot be discarded without qualification.

## Originality — PASS, with limitations

The closest general antecedent is Goles and Olivos (1980), which establishes periods one and two for finite symmetric threshold dynamics. The full-text material available from Benjamini et al., arXiv:1405.2486v1 (May 11, 2014), restates this theorem and studies random and unimodular graphs, including regular-graph disagreement; it does not state a line-graph vertex-incidence conservation law or a half-factor orbit classification. Targeted searches for line-graph majority two-cycles, oscillating edge incidence, Eulerian supports, and half-factor equivalences did not locate the latter. The available historical research ledger contains a result on neighbor-XOR on line graphs of Boolean cubes, which is a different update rule; other majority records concern particular graph families and do not imply this general parity-compatible classification.

The original Goles–Olivos full text could not be inspected through available authorized channels, although its bibliographic record and abstract were checked. The 1995 Moran article on majority period-two properties in infinite graphs was available at abstract level. Consequently an unindexed graph-dynamical specialization is a genuine residual originality risk; absence of search hits is not treated as proof of uniqueness. The standard half-factor counting coefficient itself is not claimed as novel independently of its dynamical application.

## Mathematical value — PASS

A general period-two bound leaves the geometry of oscillating sites unspecified. This result gives an **exact structural description for every finite parity-compatible line graph**: a conserved vector of edge incidences, an Eulerian alternating support, bridge exclusion, a necessary-and-sufficient half-factor construction, and a precise recurrent-orbit enumerator. It replaces arbitrary recurrent-state searches with classical graph-factor questions and sharply distinguishes genuine oscillation on two joined odd cycles from a mere union-of-even-cycles description. The proof covers both regular and nonregular base graphs and remains meaningful even when evaluating the resulting factor coefficient is computationally difficult. The fact is not a renaming of the period-two property and has clear use in identifying and counting oscillations on line graphs.

## Limits of the assessment

No polynomial-time evaluation of the factor count, transient-bound theorem, or general attraction-basin formula is asserted. The oldest general threshold-function source was not read in full; a hidden stronger statement remains possible. The finite checks only cross-check the proof, and no independent external validation has occurred.

Self-review: passed. Independent audit: not yet performed.
