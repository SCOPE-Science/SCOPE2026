# Scientific review

## Correctness
PASS. For each initial configuration on a complete bipartite graph, the update of a vertex depends only on its own color and the set of colors used in the opposite class. This produces an exact \(49\)-state quotient, valid for every choice of positive part sizes. The enumerated \(10\) periodic support pairs and the three depth matrices cover all \(49\) nonempty support pairs. Return permutations on the two-color cycles distinguish true period four from support period two. Onto-function counting gives every coefficient, with independent direct labeled-state checks for \(22\) part-size pairs. Nonstandard steps and the enumeration are reproducible from `verify.py`.

## Originality
PASS within available evidence. Durrett–Griffeath introduces the dynamics in a lattice setting; Gravner–Lyu–Sivakoff proves a general finite-graph synchronization and activity criterion. The latter does not, as stated, enumerate labeled period-three/period-four attractors and their individual first-entry-depth distribution on bicliques. Searches for equivalent cyclic-competition formulas and graph-specific CCA orbit censuses did not identify a covering statement. The closest mathematical-record result treats binary parity updates on complete multipartite graphs, a different operator. Possible unindexed exact work is an acknowledged residual risk rather than a novelty certificate.

## Mathematical value
PASS. The full primitive-period and transient-depth distribution is a natural finite-volume dynamical invariant and demonstrates a nonobvious phenomenon: a three-color cyclic consumption rule supports genuine primitive four-cycles, yet every state is periodic after at most two steps. The two-color/four-cycle and three-color/three-cycle thresholds occur at different part sizes, and the complete exact counts allow finite-network phase frequencies and zeta functions to be computed without simulation. This is substantially beyond a renaming of a general convergence theorem.

## Closest prior literature and limitations
R. Durrett and D. Griffeath (1993), arXiv:patt-sol/9303002; J. Gravner, H. Lyu and D. Sivakoff (2016), arXiv:1610.07320; M. Matamala and E. Moreno (2004), DOI 10.1016/j.tcs.2004.03.018. The source comparison is bounded and does not prove uniqueness. No conclusions are extended to Greenberg–Hastings, higher alphabets or asynchronous rules.

Self-review: passed. Independent audit: not yet performed.
