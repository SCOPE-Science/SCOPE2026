# Scientific review

**Correctness — PASS.** The proof establishes the precise minimal-cover degree-one condition, derives the maximum-edge restriction, excludes shattering at that maximum by separate two-star configurations, and constructs an explicit minimal cover for every trace on an \(a+b-3\)-edge support. The construction's cases have been checked by their endpoint degrees and by a standalone exhaustive verifier. The verifier confirms all \(7{,}688\) instances of the proposed construction for \(3\le a,b\le7\) and independent full finite VC computations for ten parameter pairs. Computational confirmation is supplementary, not a substitute for the general proof.

**Originality — PASS with historical-priority risk.** Kunjwal, Theorem 7, already determines the star-forest structure and maximum size of minimal edge covers of complete bipartite graphs, and the 2018 upper-edge-cover optimization paper invokes the general star-forest equivalence. Those results do not imply the new exact edge-query VC dimension without the upper nonshattering obstruction and all-traces construction. Focused searches for minimum/minimal edge-cover shattering, VC dimension, and spanning-star-forest concept classes yielded no directly covering theorem. Terminological variants and unindexed literature remain a residual risk.

**Value — PASS.** The exact VC dimension of a natural graph-theoretic concept class is determined uniformly over an infinite two-parameter family, including a sharp structural one-edge loss compared to the largest hypothesis size. The proof gives reusable trace realizations through a canonical three-star support, rather than merely a small finite table or a change of notation.

**Scope and residual risks.** No claim is made for general bipartite graphs or exact online dimensions. Historical priority may be affected by work phrased through nonblockers, star factors, maximal solutions, or incidence set systems. Finite verification has not been independently audited.

Self-review: passed. Independent audit: not yet performed.
