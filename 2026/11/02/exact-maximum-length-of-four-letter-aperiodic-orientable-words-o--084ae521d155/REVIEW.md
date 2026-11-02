# Scientific review

## Correctness
The displayed length-113 witness is checked factor by factor. The bound is the optimum of a completely specified 368-variable binary integer program: every finite admissible word maps to a feasible selection of its consecutive four-gram edges plus one initial and terminal vertex. Connectivity is not assumed in the optimization, so its optimum upper-bounds any realizable word. Exact program construction, independent witness validation and solver-output replay are included in `verify.py`, which reports primal and dual bounds both equal to 110 and checks the returned integer assignment. Residual limitation: the upper certificate uses HiGHS' zero-gap MIP computation; an independently formalized rational cutting-plane or unsatisfiability certificate is not supplied.

## Originality
The main comparison is Mitchell's October 2026 exhaustive binary aperiodic study, which does not determine quaternary finite lengths. The 2026 Mitchell–Wild period results and Gabrić–Sawada's 2024 cyclic constructions do not logically imply an aperiodic maximum: periodic constructions provide lower-bound examples by unwrapping, but do not establish finite maxima. Related de Bruijn-flow and reversal-pair formulations were compared, including published mathematical search records. Searches returned no statement implying the exact 113 bound. This is a best-knowledge priority conclusion, not proof that no unpublished equivalent computation exists.

## Value
This is a natural small nonbinary instance of the exact finite orientable-length problem directly motivated by the contemporary binary classification. It distinguishes finite and cyclic construction limits, provides an exact value where the strongest compared published methods primarily treat cyclic sequences, and offers both an explicit word and a compact reproducible optimization problem. It is not a mere reparameterization of the cyclic result.

## Limits and sources
The finding does not classify optimal words or settle the problem at other alphabets or spans. Sources inspected: the De Bruijn Sequences and Universal Cycles acyclic-orientable overview (binary tables); Mitchell, arXiv:2610.33601v1 (complete HTML, definitions and exhaustive-search sections); Mitchell and Wild, arXiv:2507.02526 and 2026 Acta Informatica open full text (periodic setting); Gabrić and Sawada, arXiv:2407.07029v1 (complete HTML, cyclic construction and bounds). The exact finite certificate is reproducible but not solver-independent.

Self-review: passed. Independent audit: not yet performed.
