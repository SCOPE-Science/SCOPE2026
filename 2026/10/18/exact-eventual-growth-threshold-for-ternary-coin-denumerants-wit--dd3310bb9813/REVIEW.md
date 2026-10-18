# Review: exact eventual-growth threshold for ternary coin denumerants

**Correctness — PASS.** The proof derives an exact adjacent-difference formula for all indices and parameters, isolates the unique worst six-residue partial run, and determines both last non-increases in coprime cases and an infinite strict-decrease progression in noncoprime cases. Direct exact dynamic programming returns `VERIFY_OK 408502`; it supports but does not substitute for the infinite proof.

**Originality — PASS, with residual risk.** The relevant known theorem of Woods supplies qualitative eventual quasipolynomial growth; Ding investigates general restricted-representation growth; neither inspected theorem material states this exact sharp threshold. Published mathematical-record and prior-theorem comparisons found no covering formulation. An equivalent unstated consequence of general denumerant formulas cannot be ruled out. Related 2026 work by Komatsu, Hyun and Song was only available by abstract, and no full-text noncoverage claim is made for it.

**Mathematical value — PASS.** The claim computes the precise last local-growth obstruction for a natural full infinite one-parameter family of coin-counting functions and gives a contrasting infinite-descent arithmetic class. It resolves a natural quantitative refinement of eventual-monotonicity theory; it is not only a table recomputation.

**Limitations.** The classification is for weights \(2,3,c\) and need not generalize to arbitrary triples. It does not enumerate every earlier plateau/decline. Independent mathematical verification is not available.

Self-review: passed. Independent audit: not yet performed.
