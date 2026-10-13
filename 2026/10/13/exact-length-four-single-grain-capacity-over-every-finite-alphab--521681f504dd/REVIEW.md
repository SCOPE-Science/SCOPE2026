# Scientific review

## Correctness — PASS
The one-grain output map preserves the first coordinate. For fixed first letter, splitting by the next two letters bounds codewords with second letter equal to the first by \(t\), those with third equal to the first but second different by \(q-t\), and those with both different by \((q-1)^2\). This gives \(q^2-q+1\) per first letter for every alphabet. An idempotent Latin square exists in each order at least three, and the paper proves that its row/column uniqueness and diagonal guarantee disjoint output sets for the proposed size-matching construction. Six displayed binary words cover the exceptional order two. Separate Python and C++ verifiers enumerate outputs for all packaged sample sizes. No experimental bound is used to infer the universal theorem.

## Originality — PASS, subject to bibliographic risk
Sharov–Roth's 2014 full text defines the general \(q\)-ary overwrite channel and develops asymptotic bounds, but its finite-block constructions and equality discussion are binary rather than an exact all-alphabet length-four formula. Gabrys–Yaakobi–Dolecek treat binary grain-error correction using related nonbinary component codes; that is not the same as a \(q\)-ary grain channel. The standard existence of idempotent Latin squares is acknowledged as prior mathematics. Searches found no assertion of \(M_q(4,1)=q^3-q^2+q\) for all integer \(q\), nor an equivalent complete construction. This conclusion remains subject to the possibility of an unindexed earlier specialization; the 2014 original is the closest prior source.

## Value — PASS
Length four is a natural first finite length at which overwriting at multiple distinct positions produces nontrivial competing error shadows. An exact formula valid for every alphabet size, with a general matching construction, resolves the whole alphabet family rather than supplying isolated small computations. The Latin-square connection yields a simple reusable design mechanism and clarifies precisely why the familiar binary case is exceptional in the construction.

## Boundaries
The exact result concerns one directed adjacent overwrite and length four, not noisy stochastic operation, multi-error correction, or other lengths. The proof relies on the published classical existence theorem for idempotent Latin squares of every order except two; the bundled finite verifiers only test small examples. An earlier equivalent result might be present outside the inspected materials. The review is not independent certification.

Self-review: passed. Independent audit: not yet performed.
