# Review of the Fibonacci–Tribonacci cyclic-cover theorem

## Correctness — PASS

The proof establishes a lower bound for **unrestricted** cyclic hosts by subtracting required overlap-graph edges from any covering closed walk. The remaining integral flow has one unit from each vertex ending but not starting with `11` to a vertex starting but not ending with `11`. At each source, any route to a target needs at least as many shifts as the index of the first `11`; forbidden intermediate edges cannot shorten that bound. The explicit source-to-target bijection rotates the first `11` into place and reverses the initial `11`-free prefix, giving a path of precisely the lower-bound length. The augmented graph is balanced and strongly connected, so an Eulerian circuit attains the bound. The prefix/suffix decomposition, Fibonacci counts, Tribonacci generating function and pole ratio were recalculated. Finite graph constructions and independent minimum-cost-flow calculations corroborate the proof; finite tests are not the infinite proof.

## Originality — PASS against inspected evidence

Compeau–Pevzner–Tesler (2011) covers standard unrestricted de Bruijn cycles and their Eulerian interpretation, but not the exact cyclic-cover cost for a regular language forbidding `111`. Burstein–Kitaev (2003) studies unavoidable word-pattern families and pattern-universal cycles, a different mathematical statement. Kapun–Tsarev (2013) addresses paired de Bruijn graph sound-cycle hardness, rather than the present explicit optimal one-graph covering formula. A general directed Chinese postman algorithm explains why finite instances are optimizable but does **not** imply the closed Fibonacci–Tribonacci coefficient law or the explicit reversed-prefix optimal matching. Available topical searches did not identify a dominating closed form. A prior specialized theorem in unindexed or differently named literature remains a residual risk.

## Mathematical value — PASS

The optimal periodic test cycle for the natural no-three-consecutive-ones shift has a sharply determined length at every window size, including when arbitrary forbidden windows are allowed as possible shortcuts. The proof identifies and exactly prices the local overlap imbalance and gives an optimal **valid** periodic cycle without forbidden windows. The positive asymptotic overhead, approaching \(0.617024\ldots\) of the number of required factors, is a structural cost of constrained coverage rather than a small table extension. The work does not count optimal cycles or extend to other forbidden sets.

Self-review: passed. Independent audit: not yet performed.
