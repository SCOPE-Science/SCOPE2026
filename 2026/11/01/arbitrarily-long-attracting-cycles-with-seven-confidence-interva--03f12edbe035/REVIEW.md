# Scientific review

## Correctness — PASS

The claimed domain is all integers \(p\ge2\), three scalar agents with exactly two distinct stubborn opinions, and a single closed symmetric confidence set with at most seven intervals. The proof calculates each trust membership with integer-numerator separation \(\ge3c\) for excluded differences and padding \(c\) for included differences, so all claimed phase-specific affine updates hold in open neighborhoods. The explicit itinerary is least period \(p\), the exact error identity establishes attraction with multiplier \(2^{-p}\), and all cases with fewer than three agents are ruled out. Exact rational code covers a finite sample of periods and perturbations; the general theorem rests on the symbolic proof. Boundary equalities and the special \(p=2\) coinciding intervals are handled explicitly.

## Originality — PASS, with priority risk

The source paper (Zabarianska–Proskurnikov, arXiv:2408.01753v1, Example 4) already exhibits a three-agent symmetric-confidence periodic orbit with two stubborn opinions. That prior existence claim is not new. The contribution assessed here is the **uniform seven-component construction for every least period \(p\ge2\)** together with a strict open attraction basin and least-agent sharpness. The full originating text was read in the relevant model, examples and convergence-theorem sections. The piecewise-increasing-contraction theorem of Gaivão–Nogueira (arXiv:2007.08014) bounds the count of periodic orbits, not an orbit's period, and does not furnish a SCOD embedding. Relevant opinion-dynamics survey sections and actual semantic research records were considered. Residual risk: period-encoding tricks may be known in general interval-map work, and an alternative SCOD construction could be unindexed; there is no independent literature-priority certification.

## Value — PASS

The question of temporal complexity after relaxing equal-stubborn-opinion convergence is central to the initiating SCOD study. Unbounded least period **without increasing the number of agents or confidence-set components** is a structural distinction from an isolated period-three counterexample. The explicit contraction basin shows persistence for an open set of initial opinions rather than a fragile exact orbit, and the construction identifies the smallest possible agent count.

## Limits

The confidence interval endpoints vary with \(p\); the theorem does not claim many long-period cycles coexist for one fixed set. The dynamics are deterministic and synchronous; no finite stochastic-population or convex-confidence conclusions follow. Other formulations of the binary contraction mechanism could predate this construction.

Self-review: passed. Independent audit: not yet performed.
