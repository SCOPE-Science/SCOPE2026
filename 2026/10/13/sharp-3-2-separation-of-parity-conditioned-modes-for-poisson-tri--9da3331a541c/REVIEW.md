# Scientific review: sharp parity-conditioned modal separation

## Correctness — PASS

The theorem covers all finite independent three-outcome sums with both parity probabilities positive and retains *every* tied mode. The strict-interior case follows from a classical Hurwitz-stability/Hermite--Biehler interlacing theorem, followed by a positive-residue partial-fraction expansion proving that the odd conditional law is a convex mixture of single-Bernoulli deletions of the even conditional law. The elementary convolution identity for adding back one Bernoulli then forces every deletion mode into the integer-conditioned modal interval enlarged by one on the left. The mixture cannot attain a maximum outside this envelope. Compact limits of Bernoulli parameters and mixture weights extend the identity and conclusion to zero outcome probabilities without making an invalid continuity assertion about modes. An explicit exact-rational two-trial law attains the \(\frac32\) bound, while one trial has exact gap \(\frac12\). The standalone finite checker ran successfully; its \(52686\) admissible cases corroborate but do not replace the analytical proof. Risk: the result relies on the standard strict form of Hermite--Biehler and on its correct root orientation, both directly checked against Ellard--Šmigoc, Theorem 1.1.

## Originality — PASS, with residual priority risk

Broadie--Petkova (arXiv:2603.09019v1), full nine-page text, Section 3 and Proposition 3, prove a \(\frac52\) cross-parity modal-distance upper bound but not the sharp \(\frac32\) constant, exact two-trial witness, or the unique-even-mode nearest-neighbor statement. The zero-interlacing theorem itself predates the present result and is explicitly acknowledged from Hermite--Biehler and Ellard--Šmigoc (arXiv:1701.07912v1). These facts do **not** by themselves state the positive-deletion mixture and its modal locality. Separate published mathematical-record searches and direct searches for equivalent parity, modal, and interlacing formulations found no statement that covers the claimed sharp constant. Limit: mathematical implication of classical tools makes an overlooked previous corollary conceivable; searches cannot prove universal priority. The related *Ryder Cup Singles Ordering* companion has a potentially relevant application but no accessible full text in the attempted source and is a minor unresolved priority risk.

## Value — PASS

The earlier \(\frac52\) modal gap bound is a central quantitative conclusion for a natural class of score distributions in win/tie/loss competitions and three-state systems. Improving it to the **attained** \(\frac32\), with a complete one-trial versus many-trial boundary, is a non-routine exact quantitative improvement: the largest permitted cross-parity gap drops by forty percent. The stronger neighboring-mode statement for a uniquely modal integer component explains the structure and identifies exactly when large cross-parity separation is possible (only with a tied integer mode). This is motivated by the paper's named parity-decomposition problem, not by an arbitrary parameter slice.

## Sources and limits

Primary: Broadie and Petkova, *On the structure of the Poisson trinomial distribution*, arXiv:2603.09019v1, Theorem 1, Section 3, Proposition 3, full text at https://arxiv.org/pdf/2603.09019. Method: exact comparison of statements and the derivation.

Classical interlacing: Ellard and Šmigoc, *An extension of the Hermite-Biehler theorem with application to polynomials with one positive root*, arXiv:1701.07912v1, especially Theorem 1.1, full text at https://arxiv.org/pdf/1701.07912. The relevant strict interlacing is prior knowledge, not part of the originality claim.

Scientific limitations: independent three-outcome summands and both positive parity masses are essential assumptions; arbitrary dependent sums, more outcome values, and unconditional modes are not covered. External independent audit remains to be done.

Self-review: passed. Independent audit: not yet performed.
