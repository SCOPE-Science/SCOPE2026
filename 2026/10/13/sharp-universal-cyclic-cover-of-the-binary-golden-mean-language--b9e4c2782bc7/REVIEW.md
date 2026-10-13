# Scientific review: sharp universal cyclic cover of the binary golden-mean language

## Correctness — PASS

The quantifiers are all integers \(n\ge2\), with the factor family all internally `11`-free binary \(n\)-words and with cyclic repetition required to avoid `11`. The exact graph-to-cover correspondence is established: admissible length-\(n\) words are arcs of the order-\(n-1\) overlap graph. Every closed covering walk gives a nonnegative added integral flow with unit divergences at precisely the vertices starting `0`/ending `1` and starting `1`/ending `0`. The shortest possible source-to-sink path is bounded by the length of the initial zero run, and a zero-shift path achieves it simultaneously for every source. The sink assignment is bijective, so an Eulerian completion exists. The generating-function identity gives exactly \(F_n-1\) extra arcs; adding the \(F_{n+2}\) required arcs yields the stated minimum. Edge cases \(n=2\) and all intermediate boundary cases are included by the same argument.

The supplied `verify.py` independently implements the graph and Euler circuit, directly checks every factor and the exact formula for \(2\le n\le12\), and runs exhaustive shortest closed-walk searches for \(2\le n\le5\). This computational evidence is supplementary to, not a replacement for, the infinite proof.

## Originality — PASS, with stated bibliographic limits

Wang–Shallit (1998, full 16-page primary article inspected) proves a *linear* extremum \(F_n+F_{n+2}\) and constructs open walks; it does not derive the exact closed route-balancing cost. Tan–Shallit (2013, full 12-page preprint inspected) defines the general shortest circular witness problem and gives broad upper bounds and finite tables, not the specialized Fibonacci equality. Moreno–Matamala (2007, full nine-page preprint inspected) proves Eulerian constructions for their **periodically admissible** language and lexicographically minimal labels, where a word such as `101` is excluded as a cyclic building block; our factor target expressly includes `101`. Thus neither direct statements nor the identified reductions cover the theorem. Searches of relevant mathematical results, source/alias variations, and relevant papers produced no stronger equivalent. These searches are not a proof of historical novelty; unindexed prior work and broader as-yet-uninspected universal-cycle surveys remain genuine residual risks.

## Value — PASS

A constrained universal cyclic word is a natural shortest common superstring on the golden-mean shift, and its exact minimum period is an intrinsic invariant. Unlike a finite table or a routine parameter increment, this result supplies a structural proof and constructive optimum for **every** order. The exact \(F_n-1\) repetition penalty measures the obstruction to an Eulerian tour on the full internally admissible factor graph and can benchmark constrained streaming/test-sequence designs. The theorem requires a nontrivial sharp flow lower bound and matching Eulerization, not merely the count of admissible factors. No optimizer enumeration, downstream algorithmic speed claim, or unproved extension is asserted.

## Limits and primary sources

The literature comparison is strongest for the three inspected full-text sources: Wang–Shallit (1998, DOI 10.37236/1373), Tan–Shallit (2013, arXiv:1304.3666), and Moreno–Matamala (2007, arXiv:0711.1695). Source coverage is not exhaustive. The domain is the binary forbidden-adjacent-ones language only, and full optimizer counts are not determined.

Self-review: passed. Independent audit: not yet performed.
