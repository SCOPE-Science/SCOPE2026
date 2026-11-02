# Scientific review

## Correctness — PASS

A direct least-significant-bit multiplication by three has carry states \(0,1,2\). The input/output parity product reduces to one sign per starting carry, giving the exact \(3\times3\) matrix formula; the terminal vector includes every high carry bit. Rational resolvents and the characteristic polynomial give the all-index recurrence and spectral formula. The joint counts follow by an exact sign-indicator identity and a separately evaluated marginal transfer matrix. An algebraic-integer obstruction makes the spectral angle irrational and proves infinitely many positive and negative values with sharp scale. `verify.py` passed complete enumeration of 262143 dyadic-prefix input evaluations through level 17, with all four joint cells. Direct enumeration is a cross-check, not an infinite proof. No unproved hypotheses are invoked.

## Originality — PASS within inspected evidence

The first principal relevant primary work, Shallit (2023, arXiv:2302.09436), treats the single-coordinate bias \(\tau(3n)\) and Newman-type bounds, not the mixed product \(\tau(n)\tau(3n)\). The full Shallit text was checked in the relevant introduction and main results. Baake–Coons (2022, arXiv:2209.07102), also read in its main definitions and theorems, treats constant-shift correlations, which do not yield an exact dyadic multiplier-index correlation. Charlier–Cisternino–Massuir (2019, arXiv:1910.08543) gives a multiplication automaton and state-complexity results rather than the four sign-cell counts. The accessible full publisher rendering of a 2011 weighted rarefied-sum article concerns one-coordinate sums with position-weighted digits. Searches for equivalences, joint parity, transfer recurrences, and direct named formulas did not produce a covering theorem. Those negative searches are limited evidence; broad published digit-sum methods may imply a short rederivation, and complete bibliographic uniqueness is not certified.

## Mathematical value — PASS

The Newman bias alone determines the parity of \(3n\), not whether the two digit parities agree; that conditional arithmetic question is natural and distinct from ordinary adjacent-symbol correlations. The exact two-coordinate law exhibits two genuinely different spectral scales and an infinitely sign-changing correction at the smaller scale. It provides complete integer counts rather than just a normality statement or numerical trend. The new contribution is a meaningful exact arithmetic-correlation refinement, not a claim of a new generic automaton method.

## Scope and limits

Only dyadic prefixes and multiplication by three are included. One potentially relevant older weighted-digit article was not obtained as a complete offline file; implicit stronger published formulas remain the principal originality risk. The finite checker is not independent scientific certification.

Self-review: passed. Independent audit: not yet performed.
