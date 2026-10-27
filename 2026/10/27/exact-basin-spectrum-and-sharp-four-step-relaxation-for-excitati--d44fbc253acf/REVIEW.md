# Scientific review

## Correctness — PASS
The three-state update is defined at every vertex with simultaneous updates and threshold one. Each rainbow triangle rotates rigidly and forces its shared hub to rotate; all nonrainbow wings relax to a passive three-cycle phase by the fourth update. The 27-case driven-wing table proves the local assertion, while the 93 possible support cases of nonrainbow wing types prove extinction by the fourth update in the complementary branch. These two exhaustive finite reductions hold for arbitrary blade number, not just tested small graphs. The per-attractor basin formulas partition all \(3^{2r+1}\) states exactly. A direct graph-wide exhaustive checker over \(r=1,\ldots,5\) corroborates the analytic classification and the sharp preperiod bound. A completed proof is provided; these computations are independently replayable but not externally certified.

## Originality — PASS
Existing general circulation criteria already characterize eventual extinction versus persistence for three-state excitation and hence include the binary extinction criterion specialized to this graph. The new claim is the attractor-resolved basin formula \(3\,7^{r-k}\), the exact count \(\binom rk2^k\) of cycles at each level, and the sharp uniform four-step cutoff. The 2016 finite-graph theorem gives an upper bound \((7/9)^r\) in a cycle setting, not these per-cycle basin counts or a sharp universal entrance time on shared-hub triangles. A 2018 finite-graph criterion is also qualitative rather than enumerative. Searches for friendship graphs, bouquets, windmills, excitable dynamics, Greenberg–Hastings and equivalent three-state rules, plus inspection of highly relevant accessible primary PDF sections, yielded no implied joint formula. The 1991/1993 lattice-origin source full texts were inaccessible; unindexed enumeration remains a risk.

## Value — PASS
Friendship graphs model many excitable loops coupled through a single vertex, a natural test for how local circulating waves interact through a common hub. The result distinguishes \(3^r-1\) nonzero attractors with exponentially varying exact basins and a strict constant-time transient; it gives a precise equality instance for the classical \((7/9)^r\) extinction bound. Unlike merely asking whether excitation persists, it quantitatively characterizes asymptotic states and the sharp time required to reach them, making it useful for finite excitable-network models and benchmarking general graph criteria.

## Limits
No extensions to larger cycle blocks, different colors, noisy or asynchronous rules. Uninspected full texts and unindexed equivalent computations are residual originality risks. Finite direct enumerations through five blades do not replace the reduction proving every blade count.

Self-review: passed. Independent audit: not yet performed.
