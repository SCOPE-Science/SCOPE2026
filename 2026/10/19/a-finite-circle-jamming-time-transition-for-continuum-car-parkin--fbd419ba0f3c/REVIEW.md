# Scientific review

## Correctness

**PASS.** The claimed physical-time process is specified as unit Poisson proposal intensity on a finite circle with unit rod length. The accepted center-space rate is the exact length of the admissible set. The proof checks all threshold endpoints: one accepted rod jams for \(1\leq L\leq2\), a second jams for \(2<L\leq3\), and a third possibly deposits for \(3<L\leq4\). For the last regime the second center is uniform on an interval of length \(L-2\), which yields the exact third-stage survival integral. Above circumference four, the explicit open cylinder of mutually compatible first proposals creates a single admissible interval of arbitrarily small length. Its next-deposition mean integrates a nonintegrable \(1/\varepsilon\) singularity over a set of positive density. The finite-size checks in `checks.py` pass, but the all-size conclusion rests on the proof.

## Originality

**PASS under the literature comparisons described, with documented residual priority risk.** The closest work of Privman and Yan (2016) uses Pomeau's mechanism for power-law jamming kinetics on patterned substrates; it does not give the exact finite-circle last-deposition-time phase transition and coefficient. Purvis et al. (2015) analyze coverage–availability scaling, Huillet (2003) uses a free-deposition circle process explicitly different from Rényi's sequential exclusion, and the available Kumar (2026) abstract concerns finite *interval* configuration and absorption-count laws. No matching or dominating published statement emerged from the semantic claim, alias, or gap-parameter searches. Some original complete texts were inaccessible, and independent priority verification remains outstanding.

## Value

**PASS.** The result explains a singular distinction between almost-sure completion and expected physical completion time, with a sharp circumference-three cutoff; the threshold boundary is not inferred from infinite-substrate coverage. The exact terminal-time coefficient and logarithmic truncated mean on \(3<L\leq4\) quantify the rare near-jammed sample paths and supply a reproducible finite-volume benchmark for physical-time adsorption simulations. The proof also isolates the geometric near-fitting-gap mechanism responsible for the all-size infinite-mean result.

## Boundaries

The \(1/t\) coefficient is claimed only through circumference four, not for all larger circles. The result does not cover discrete lattices, multiple rod lengths, finite-number trial protocols, or artificially accelerated sampling of successful arrivals. Older general jamming laws are not claimed as new.

Self-review: passed. Independent audit: not yet performed.
