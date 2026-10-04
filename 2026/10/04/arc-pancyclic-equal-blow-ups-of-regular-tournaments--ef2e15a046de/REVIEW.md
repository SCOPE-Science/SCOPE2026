# Same-model review

## Correctness
**PASS.** The proof reduces the claim to two ingredients. First, Alspach's theorem gives, for the prescribed base arc \(u\to v\), a base cycle of every length \(t\in\{3,\ldots,c\}\). Second, every target \(\ell\in\{3,\ldots,c\alpha\}\) can be written as a sum of at most \(\alpha\) such admissible lengths because the intervals \([3k,ck]\) cover the full integer range when \(c\ge5\). Lifting the \(j\)-th selected base cycle into the \(j\)-th clone layer and linking its final vertex to the next \(u\)-clone gives a simple directed cycle of length \(\ell\) through the prescribed lifted arc. Distinct layers prevent repeated vertices. The excluded case \(c=3\) genuinely fails for nontrivial blow-ups.

## Originality
**PASS.** The closest recent source, arXiv:2609.12372, proves \(4\)-arc-pancyclicity for arbitrary regular multipartite tournaments only when \(c\ge93\), together with weaker distinct-length guarantees outside that range. Alspach treats only the unblown tournament. Pan--Zhang's classical multipartite theorem fixes the number of partite sets met by a cycle, not every total cycle length, and vertex-pancyclicity results do not prescribe an arc. Searches under blow-up, composition, lexicographic-product, cyclic-tournament, and regular-multipartite aliases found no statement implying the equal-blow-up theorem. The main residual risk is older composition literature under terminology not indexed by the searches.

## Value
**PASS.** Equal independent-set blow-ups are a canonical way to pass from tournaments to regular multipartite tournaments. Showing that they preserve the full prescribed-arc cycle spectrum gives a structurally motivated infinite family satisfying a conclusion stronger than the recent large-\(c\) theorem, and the proof exposes a simple additive cycle-splicing mechanism potentially useful in related composition problems.

## Closest literature and limitations
The initiating 2026 paper is the closest current result on the same invariant. The theorem here is a sufficient-condition result, not a classification of all arc-pancyclic regular multipartite tournaments; unequal blow-ups remain outside its scope. The result uses the classical Alspach theorem as an essential base input.

Same-model review: passed. Independent audit: not yet performed.
