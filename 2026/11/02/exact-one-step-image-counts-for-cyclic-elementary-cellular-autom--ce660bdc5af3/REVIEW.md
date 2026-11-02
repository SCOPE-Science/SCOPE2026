# Scientific review

**Correctness — PASS.** The local rule, cyclic boundary convention, rooted-output counting, 4-state pair graph and Boolean composition are fully specified. A 75-state finite closure establishes deterministic recognition of all output strings. The exact 75-component identity \(T^2p(T)v=0\), independently recomputable in `verify.py`, proves the recurrence for every length, while initial values give the rational generating function. Root separation proves the displayed exponential asymptotic with leading coefficient one. Direct enumeration through length 16 is a cross-check and not the infinite proof.

**Originality — PASS, with historical priority risk.** The earlier Rule-110 subset-diagram and de Bruijn literature provides the method of checking preimages, not an inspected formula for the number of distinct rooted cyclic outputs at every length. The accessible 2007 primary manuscript's glider-language and forbidden-pattern results do not imply the stated rational series as a recorded theorem. A related specialized earlier article was only partly accessible, so complete historical-priority exclusion is not possible. A concrete series and proof, not the recognition technique itself, is the contribution. Searches and comparisons are documented in `AUDIT.json`.

**Value — PASS.** The exact growth rate of the one-step image of a classical computationally universal local rule is a natural, nontrivial global-state invariant. It quantifies information loss on finite rings and determines the reachability fraction for every ring size, unlike finite small-size tables or local forbidden-pattern tests alone. No multi-step result is asserted.

The closest literature treats preimage calculations, subset diagrams and selected Garden-of-Eden languages. The fully inspected 2007 study is materially different. Partial access to an earlier preimage paper and unindexed prior results are residual historical risks.

Self-review: passed. Independent audit: not yet performed.
