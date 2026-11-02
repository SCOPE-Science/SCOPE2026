# Scientific review: Sharp cyclic one-step preimage runner-up for elementary Rule 126

## Correctness — PASS

The proof fixes the exact Boolean rule, labeled periodic states, and one-step domain. The trace of the four-state labeled de Bruijn matrices counts indexed cyclic ancestors without boundary overcounting, and complement symmetry gives the two independent second-order recurrences. A complete Fibonacci zero-gap product proves the formula for every non-all-one output. Every output with two or more zero sites is bounded by \(F_{n-3}+1\), strictly below the one-zero value \(F_{n-2}+\tau_{n-1}\) for all \(n\ge7\). The Lucas-plus-period-three all-one value is strictly higher. The standalone verifier checks every output through length 16 and reconstructs transfer-matrix traces through length 10 using exact integers. The argument, not the finite replay, proves the infinite claim.

## Originality — PASS, with historical risk

Jen (1989), Section 4 and Equation (4.11), gives a Fibonacci formula for **linear-block** Rule-126 preimages and Section 5.4 identifies the all-one linear-block maximum; these are explicitly acknowledged rather than presented as new. Her general recurrence machinery does not itself state the cyclic ring's second-largest fiber or its equality class. Martínez et al. (2012 preprint) describe the rule's de Bruijn diagram, while Fukś (2013 preprint) addresses different multistep preimage sequences. The inspected published statements and actual research-record comparisons did not establish the exact \(F_{n-2}+\tau_{n-1}\) runner-up or show it as a corollary of a stronger finite periodic-ring ranking. An older unindexed or uninspected result may still cover it; independence of historical priority has not been certified.

## Value — PASS

The statement gives a sharp infinite classification of the second-most probable outputs of a canonical nonlinear cellular automaton under uniform input. The period-three correction reflects an antisymmetric transfer-matrix eigenspace, and the proof excludes *all* competing cyclic arrangements of multiple zeros by a strict Fibonacci product inequality. This goes beyond the known homogeneous maximum and beyond a numerical finite enumeration.

## Relationship and limitations

Key closest sources: Erica Jen, *Enumeration of Preimages in Cellular Automata*, Complex Systems 3 (1989), 421–456; Erica Jen, *Scaling of Preimages in Cellular Automata*, Complex Systems 1 (1987), 1045–1062; Martínez et al., *How to Make Dull Cellular Automata Complex by Adding Memory: Rule 126 Case Study* (arXiv:1212.0124v1); and Fukś, *Sequences of Preimages in Elementary Cellular Automata* (arXiv:1305.6533v1). The result is limited to one synchronous update on indexed periodic binary rings, and its extremal assertion begins at length seven. No multi-step, arbitrary-rule, or independent-priority claim is made.

Self-review: passed. Independent audit: not yet performed.
