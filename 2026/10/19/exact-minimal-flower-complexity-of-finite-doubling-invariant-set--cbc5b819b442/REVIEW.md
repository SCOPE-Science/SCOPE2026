# Scientific review: exact finite-support flower complexity

## Correctness — PASS

The proof fixes the exact flower definition from Harriss--Jenkinson and Brown, records the unique inverse branch forced at each point of a finite invariant set, and reduces the covering optimization to a circular two-sheet transition count. Its seam term follows from the nontrivial monodromy of the doubling covering: ordinary equal branch labels require an additional seam jump. A constructive selector attains all the gapwise lower bounds with every prescribed point in an interior. The fixed-point-grid recurrence and binary necklace/BWT correspondence are proved directly. The verifier passed 1,197 exact rational assertions on 315 finite families and includes small-case exhaustive side-label minimization. These tests are diagnostics; they do not replace the proof.

## Originality — PASS on inspected evidence

Harriss and Jenkinson (arXiv:0711.0802, Section 2) define finite-jump inverse selectors and flowers; Brown (arXiv:2605.06962v1, Sections 2--4) establishes structural complexity bounds and interval-exchange coding. Neither inspected section states the global minimum-petal formula for every finite invariant support or the exponential all-fixed-points obstruction. Kumallagov (arXiv:2606.01267v1, Sections 2 and 8--9) treats BWT run structure; it is credited for the established word-combinatorial background, not for the new geometric identification. The five-petal value for a narrow reflection-paired mechanical-cycle family is treated as prior information and is not claimed independently. A historical equivalent described in other terminology remains possible.

## Value — PASS

The primary object is a geometric optimal covering of a prescribed dynamical invariant set, not an arbitrary sequence statistic. The closed formula classifies the optimum for every finite union of periodic orbits and constructs an optimizer. The sharp growth \(2^n-1\) for all fixed points of the \(n\)-th iterate shows an exponential obstruction invisible from the cardinality of a single periodic orbit. The BWT bridge makes an established combinatorial run statistic an exact geometric invariant, allowing cyclic-word methods to address cover problems. The result does not cover infinite invariant sets, other map degrees, or global maximal-invariant-set equality.

## Sources, comparison, and limits

Primary inspected sources: E. Harriss and O. Jenkinson, *Flattening Functions on Flowers*, arXiv:0711.0802 (Section 2); M. Brown, *Expanding Maps on Flowers, Interval Exchange Transformations, and Ergodic Optimization*, arXiv:2605.06962v1 (Sections 2--4); D. Kumallagov, *An extremal problem for completely unclustered Burrows--Wheeler images*, arXiv:2606.01267v1 (Sections 2, 8--9). No independent bibliographic certification or independent proof audit has been performed.

Self-review: passed. Independent audit: not yet performed.
