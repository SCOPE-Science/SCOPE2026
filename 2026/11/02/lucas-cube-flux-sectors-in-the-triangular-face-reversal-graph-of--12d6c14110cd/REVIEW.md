# Assessment of the antiprism triangular-face reversal classification

## Correctness — PASS
The Eulerian balance equations produce a conserved local flux in \(\{0,1,2,3\}\). Flux zero and three each have exactly one frozen orientation. At flux one, the only forbidden transition among three local edge-state types is \(Y\to Z\), giving a bijection to independent sets of the even cycle. The exact two triangular-face reversal rules toggle its two sites per cell; orientation complementation transfers the construction to flux two. These are all configurations, proving the four-component isomorphism for every \(n\ge3\). The metric and enumerative consequences follow from transparent independent-set arguments. The supplied cyclic-state and independent raw-orientation verifiers corroborate all cases through \(n=9\) and \(n=8\), respectively.

## Originality — PASS with explicit residual risk
The closest established frameworks are Felsner's 2004 planar Eulerian-orientation lattice theory and Creed's 2007 face-reversal Markov chains, which use permitted face moves generally rather than restricting reversals to the triangular antiprism belt and omitting cap faces. Their statements do not identify antiprism flux sectors with Lucas cubes. Munarini, Perelli Cippo and Zagaglia Salvi's 2001 paper already establishes Lucas-cube definitions, edge counts, diameter and extremal pairs; those are not asserted to be new here. Codara and D'Antona's 2014 Lucas-cube extensions do not provide this orientation-bijection claim. No equivalent implication was found in targeted literature and mathematical-research record searches. The possibility of unindexed exact prior work or an alternative ice-model encoding remains.

## Value — PASS
The precise exclusion of cap moves creates topologically meaningful, conserved-flow disconnection that generic all-face orientation lattices do not exhibit. An exact graph isomorphism, rather than an isolated counting identity, classifies every configuration and every legal local move on an infinite family of canonical four-regular planar graphs, gives direct shortest paths, and exposes frozen states. This is a natural boundary of standard face-reversal connectivity and a transferable link between constrained orientations and median configuration graphs.

## Scope and remaining limitations
This result does not cover cap reversals, other graph families, mixing times, or new intrinsic Lucas-cube identities. The exact classification is proved for all integer \(n\ge3\); finite software checks are supplementary. Literature indexing cannot establish uniqueness in all publications.

Self-review: passed. Independent audit: not yet performed.
