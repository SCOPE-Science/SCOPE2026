# Scientific review

## Correctness — PASS

A class is determined locally by the multiplicities \(0\), \(1\), and \(\ge2\) of every unary colour because guards contain at most two distinct variables. The proof explicitly constructs a guarded back-and-forth system relating all models of a given class-profile spectrum; the nonempty spectra are separated by rank-three guarded formulas. The canonical model has \(\sum_{v\in S}\sum_t v_t\) elements, and summing over all nonzero profiles proves the universal upper bound \(c3^c\). The all-profile sentence requires pairwise distinct classes with the indicated multiplicities, hence forces exactly that lower bound. This proves exact theory count, quantifier-rank collapse, and optimality for arbitrary domain sizes.

The finite checker independently enumerates all \(1954\) one-unary-predicate equivalence structures through five labelled elements, explicitly tests guarded back-and-forth on \(418\) selected instances, and checks the extremal models for \(c=1,2,4\). It is supporting evidence, not the all-cardinality proof.

## Originality — PASS, qualified

The guarded-bisimulation preservation theorem is classical and explicitly acknowledged. In the inspected primary texts, the broader small-model and canonisation results do not supply the explicit \(0/1/\ge2\) class-profile invariant, the \(c3^c\) best uniform model bound, or the \(2^{3^c-1}-1\) complete GF-theory census for a single equivalence plus unary-only vocabulary. The complete profile theorem and simultaneous sharpness are the contribution assessed here; absolute historical priority is not asserted. Targeted searches of mathematical literature, published research records, and accessible deduplication ledgers revealed no statement equivalent to all three quantitative components. A prior textbook treatment of equality-aware single-role modal/guarded logic remains a residual priority risk.

## Value — PASS

The 2026 work on nested equivalence relations emphasizes how an otherwise benign guarded fragment changes when equality and auxiliary binary relations are present. In the natural *unary-only* boundary regime, the result completely classifies the expressiveness of unrestricted-rank guarded sentences: every sentence reduces to rank three, only finitely many theories remain, and the exact smallest universal witness size is computed. The optimal witness size is doubly exponential in the number of unary predicates even though it does not depend on formula length. These are motivated finite-model and expressive-power invariants, not arbitrary finite enumerations.

## Closest literature and limitations

Fiuk, *The Guarded Fragment with Nested Equivalences* (arXiv:2605.15072), studies more general signatures and proves undecidability with equality and additional guards. Fiuk, *Random Models and Guarded Logic* (arXiv:2601.05247), establishes asymptotically optimal general small-model bounds. Bárány, Gottlob and Otto, *Querying the Guarded Fragment* (LMCS 2014, DOI:10.2168/LMCS-10(2:3)2014), establishes guarded-bisimulation invariance and general canonisation. Their results supply mathematical background but do not state the special-case sharp number or full census in the inspected sections. Further explicit older results on unary-labelled S5-style guarded semantics could reduce originality.

The claim does not extend to added binary predicates, additional equivalences, constants, counting quantifiers, or ordinary two-variable logic. No independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
