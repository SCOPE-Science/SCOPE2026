# Review: minimum overlap-free square-product spectrum

## Correctness

**PASS.** The final mathematical claim is the complete \(k=1,\ldots,9\) vector of minimum lengths and minimizer counts, plus the unique \(k\)-square factorization of every minimizer. The proof gives an exact inductive enumeration of every overlap-free binary word up to the largest asserted minimum length, \(48\). The suffix-square recurrence counts all cuts into nonempty squares. A separate breadth-first search adding whole overlap-free squares reproduces all nine quadruples, including both and only both length-\(48\) minimizers. The included verifier was executed from its actual path; assertions passed. The result is finite, not extrapolated from short experiments, and no infinity claim rests on enumerated samples.

## Originality

**PASS, with residual priority risk.** The closest source is Shallit, *Ten Squares Force an Overlap*, arXiv:2605.28570v1, Theorem 1 and its proof. That paper already proves at most nine squares and supplies a specific nine-square witness of length \(48\). Its Lemma 7 tabulates products from four special square blocks for a different proof purpose. The source does not state the minimum length among all nine-square products, the two-word classification, factorization uniqueness, or the complete minimum-length spectrum. The stated result is not implied by an existence witness, since a shorter product could a priori exist. Searches for exact parameter vectors and alternate terminology identified no direct published coverage; unindexed or implicit prior calculations remain a residual risk. This review does not claim to certify absolute publication priority.

## Value

**PASS.** For the extremal nine-square regime of the original theorem, the new lower bound proves that its \(48\)-letter witness is optimally short and the unique optimum up to bit complementation. The full enumeration shows a sharp jump from length \(24\) at eight squares to length \(48\) at nine, with every minimum word having exactly one factorization. These are natural and exact extremal facts about the recently studied overlap-avoidance problem, not arbitrary subsets or routine restatements of the existence theorem.

## Boundaries and reproducibility

The proof is exact but computer-assisted: it relies on the finite exhaustive search whose completeness is explicitly established in `RESULT.md`; the independent second enumeration checks implementation errors. No theorem about longer nonminimal words, larger alphabets, or unpublished-work priority is asserted. Run `python3 verify.py` and compare `verification_output.txt`.

Self-review: passed. Independent audit: not yet performed.
