# Scientific review

## Correctness
**PASS.** The edge-support observation is equivalent to a covering directed walk. For three letters, the component analysis gives an Euler trail for every feasible support, including loops. The formula partitions directed edge supports by active-vertex count and by strong-component structure, without double-counting. The direct enumerator gives 328 labeled supports, including the empty set. The directed-cycle argument proves exact-length persistence for the remaining 315 profiles. The four-symbol example has imbalances \((2,-2,0,0)\), excluding a six-transition realization; its seven-transition word is explicit. A separate state-space closure and exhaustive enumeration of all words through length ten agree with the closed formulas.

## Originality
**PASS, with uncertainty.** The closest full text is Bernardini et al., whose central algorithm for shortest strings with specified length-\(k\) substring sets covers individual instances but neither states the complete ternary length-two census nor the sharp alphabet bound for edge-simple realizations and the 13/315 persistence classification. The older conference version is credited. Celikkanat et al. concern k-mer genomic representations; Gabrys and Milenkovic and related binary multispectrum work retain digram multiplicities and so do not determine the presence-only ternary answer. Exact aliases, broader methods and existing finite tables were searched, without finding a statement implying the complete claim. This does not establish universal novelty; an unindexed combinatorial enumeration or a hidden special-case theorem could supersede the result.

## Value
**PASS.** The ternary alphabet is mathematically distinguished as the largest alphabet for which every feasible length-two support can be realized without repeating an edge. At that boundary the exact set-valued reconstruction capacity becomes a finite 328-class census with a sharp uniform length cutoff and a structural 13-versus-315 persistence dichotomy. This supplements rather than merely relabels general shortest-Eulerian-walk algorithms, furnishing precise benchmarks for support-only sequence representations.

## Limitations and nearest literature
The result does not classify higher-order k-mers, four-symbol support counts, or multiset-valued observations. General directed graph covering-walk reduction is known from Bernardini et al.; the contribution is a small-alphabet rigidity and complete finite support classification. The NeurIPS-2024 genome paper motivates the representation problem but makes no claim of mathematical priority for this theorem. Independent validation is outstanding.

Self-review: passed. Independent audit: not yet performed.
