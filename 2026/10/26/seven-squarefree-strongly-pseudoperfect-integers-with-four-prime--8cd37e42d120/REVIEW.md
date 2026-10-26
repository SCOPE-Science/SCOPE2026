# Scientific review of the seven-number classification

**Correctness — PASS.** Every squarefree four-prime integer either has insufficient abundancy, belongs to the eliminated \(2\cdot7\cdot11\cdot13\) boundary case, or falls into one of ten explicitly enumerated three-prime cores. The complementary-pair equation is exact and separates the last prime linearly. The attached standard-library checker exhausts all 256 omission subsets for each core, excludes the zero-coefficient identity case, verifies all seven unique omission witnesses, and independently checks all qualifying integers up to 5000. The infinite reduction is analytic/elementary and is not inferred from the finite census.

**Originality — PASS, subject to bibliographic risk.** The 2026 Wang–Zelinsky paper lists individual small examples and studies structural restrictions and power constructions; these do not imply a complete bound-free classification at squarefree prime-support four. The closest indexed existing result establishes the \(\Omega(n)\le3\) layer (only 6 and 28), strictly weaker in multiplicity scope. OEIS A334405 supplies initial data only. Searches for the seven-number set, four-prime squarefree restriction, and complementary-pair representations did not locate a theorem with equivalent coverage. An unindexed or implicit stronger theorem remains possible.

**Mathematical value — PASS.** The first squarefree multiplicity layer past the previously classified three-factor obstruction is natural, and its behavior is unexpectedly finite: precisely seven integers, with no hidden larger examples and a unique representation for each. The proof gives an effective, completely reproducible finite cutoff using structural inequalities rather than an arbitrary search bound. This classification is not a general theorem about all strongly pseudoperfect numbers.

**Limitations.** No claim beyond exactly four distinct prime factors in squarefree integers; no new assertion of priority or independent validation. Source comparisons are limited to the inspected available literature and published indexed summaries for inaccessible records.

Self-review: passed. Independent audit: not yet performed.
