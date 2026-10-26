# Self-review

**Correctness — PASS.** Trimming preserves the accepted language and the graph restriction. All accepting paths have length two, forcing three disjoint state layers. Middle states are a Cartesian-rectangle cover. In a cactus, three middle states cannot share an accepting successor because two four-cycles would share multiple vertices. Pairing middle states proves tightness. The proof covers all nonempty relations and all finite alphabets. The attached exact verifier tests all nonempty relations over alphabets of sizes two and three, checks words through length four, and validates the inequality construction for alphabet sizes two through fourteen.

**Originality — PASS, with source-access risk.** The 2014 biclique correspondence is explicitly acknowledged and concerns transition minimization; the new characterization counts **states** subject to a cactus restriction. The 2026 existence result is broader in language class but does not, in its accessible abstract, provide the exact minimization formula. A previously studied diagonal-relation special case is subsumed by this general result, not the reverse. The 2026 paper's complete text was inaccessible; it could contain a closer special argument, and external human literature verification remains necessary. The Sperner/crown biclique number is prior art and not claimed independently.

**Value — PASS.** The result completely characterizes a natural family of finite languages under a graph-topological automaton constraint. It converts an entire state minimization problem to the classical biclique-cover rank with an exact surcharge, and it exhibits a logarithmic-state inequality-language family as distinct from linear-size diagonal relations. The bound and construction are uniform for every nonempty binary relation rather than a small-instance calculation.

**Scientific limits.** This is for epsilon-free NFAs with a single initial state; no transition-minimization or longer-language claim is made. Full-text access to the motivating 2026 paper was not obtained. Finite tests supplement rather than establish the infinite theorem.

Self-review: passed. Independent audit: not yet performed.
