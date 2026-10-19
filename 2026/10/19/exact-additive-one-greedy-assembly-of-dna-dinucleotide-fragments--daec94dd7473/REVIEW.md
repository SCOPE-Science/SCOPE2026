# Review of exact DNA dimer greedy assembly

## Correctness

**PASS.** Lemmas 1–3 in `RESULT.md` prove that the state space contains all ten reverse-complement classes, that the oriented subset recurrence computes the true optimum, and that the component-multiset recurrence enumerates all legal greedy tie breaks. The standalone `verify.py` evaluates every one of the 1023 nonempty subsets, with no inference beyond the finite domain. It establishes the exact tables and the additive-one inequality, and cross-checks the small-input recurrences using separately implemented brute-force methods. The explicit `AA,AC,CA` witness proves global sharpness at ratio \(5/4\).

## Originality

**PASS within inspected evidence.** Closest primary sources are Yamano–Shibuya (arXiv:2601.15814, arXiv:2603.26176), Fici et al. (arXiv:1511.08431), and Orenstein–Shamir (2013, DOI:10.1093/bioinformatics/btt230). Their general approximation, reversal-based compression, and full-coverage constructions do not imply the exact **direct greedy, fixed dimer alphabet, all-subsets, all-ties** profile. Checked mathematical research records included DNA two-letter coverage and ordinary binary shortest-superstring finite cases, which are different settings. Residual risk: an equivalent finite enumeration may exist in unindexed code or literature.

## Value

**PASS.** This is a complete and sharp finite benchmark for the standard direct greedy rule in the smallest strand-aware, four-nucleotide, nontrivial short-read domain. Its exact additive guarantee and full extremal distribution describe all 1023 inputs rather than isolated examples. The restriction to two-letter fragments is substantive and explicitly limits transfer to longer reads.

## Limitations and comparison

The guarantee does not cover cycle-cover algorithms MGREEDY-RC or TGREEDY-RC, other alphabets, or read lengths greater than two. Independent scientific audit has not been conducted; exact exhaustive computations and primary-source comparisons can be examined in the embedded artifacts.

Self-review: passed. Independent audit: not yet performed.
