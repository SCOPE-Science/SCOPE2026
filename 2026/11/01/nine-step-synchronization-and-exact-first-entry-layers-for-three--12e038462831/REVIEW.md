# Self-review

## Correctness — PASS

The four-block color-cohort quotient is exact: any two nonbridge vertices starting in the same color see an identical blinking-neighbor condition whenever their current color is 2, because neither can be a blinking vertex at that moment. Exact single-step update rules for the two bridge endpoints and six possible interior cohort coordinates are given in `RESULT.md`. The self-contained Python program tests all \(3^2\cdot7^2=441\) initial cohort supports, finds first global synchrony at time at most nine, and obtains the ten exact coefficient matrices. The explicit four-block trajectory gives a valid nine-step extremizer for every clique-size pair. Inclusion-exclusion gives the exact labelled counts. A different, direct C++ labelled test checks 1,185,921 initial assignments for 25 graph sizes. The correctness proof for arbitrary sizes depends on the finite quotient, not a large-\(n\) extrapolation. Unproved: other graph families and other colors.

## Originality — PASS, with residual risks

The closest full primary texts are Lyu, arXiv:1407.1103 (introduction, model definition, width lemma, path and tree theorems, concluding remarks) and Lyu, arXiv:1610.00837 (introduction, main theorem and tree-local analysis). They establish the model and results for paths and low-degree trees; neither of the inspected portions gives the bridged-clique synchronization-time matrix. The path theorem applies to the single parameter pair corresponding to \(P_4\), not to the infinite cyclic graph family. The prior complete-bipartite and complete-split firefly censuses have non-equivalent edge sets; the Greenberg–Hastings bridge-clique census uses a different local rule and cannot imply this theorem. Equivalent literature could remain unindexed. No claim is made that web or database silence proves novelty.

## Mathematical value — PASS

A single bridge is a natural bottleneck for synchronization between two dense communities, and the assertion that *every* initial three-color configuration synchronizes in a sharp constant nine steps despite arbitrarily large communities is structural, not a parameter renaming. The complete first-entry distribution distinguishes the difficult extremal configurations from the typical two-step regime, and establishes the exact equality of the one-step and three-step layers. These quantities are natural stopping-time invariants and give information not provided by a generic existence-of-synchrony theorem.

## Limitations

The proof relies on a small reproducible exhaustive finite transition and on the proved exactness of its abstraction; the computer check has not undergone an independent external audit. Historical-priority uncertainty remains where relevant articles or unpublished analyses may not be indexed. This review evaluates only the stated theorem and makes no claim about wider graph classes.

Self-review: passed. Independent audit: not yet performed.
