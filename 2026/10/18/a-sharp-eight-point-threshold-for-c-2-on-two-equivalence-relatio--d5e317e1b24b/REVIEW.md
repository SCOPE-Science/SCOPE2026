# Review of a sharp eight-point \(C^2\) threshold

## Correctness — PASS

The scope fixes two named equivalence relations on a nonempty finite universe. The orbit encoding by intersection matrices is bijective on isomorphism types; the four one-point extensions are exhaustive by deletion, and the canonical representative fixes invariant column-sum order and minimizes over the remaining row/column freedoms. The logical characterization is global, synchronized one-dimensional colour refinement including every joint \(E,F\) relation value, with equality accounted for on the diagonal. The extracted standalone exact verifier computes 3,017 types, 3,016 stable-colour signatures and one two-member class at eight, with no earlier collisions. The witnesses are analytically nonisomorphic (different incidence-component counts) and indistinguishable (each point has the same four relation-category counts). The table also agrees with OEIS A007716's independently known isomorphism totals. Risk: as with any finite exhaustive classification, the proof depends on the supplied generator/canonicalization argument and code implementing it correctly; the labelled-partition cross-check independently tests the small orders.

## Originality — PASS, qualified

Kiefer–Schweitzer–Selman, arXiv:1503.08792v1 (2015), give the general characterization of structures identified by \(C^2\), not the explicitly evaluated two-equivalence cutoff and first ambiguity layer. Pratt-Hartmann, DOI:10.1002/malq.201400102 (2015), addresses (un)decidability of satisfiability in the presence of equivalences, not the 3,016-class census. OEIS A007716 already contains the *3,017 isomorphism count*; novelty does not include that total. Focused mathematical searches yielded no source stating the unique eight-element pair or threshold. The general characterization is the most important stronger antecedent, so the contribution should be described specifically as a restricted exact specialization. Risk: small-order colour-refinement computations not indexed under these keywords may have appeared earlier; priority has not been independently audited.

## Value — PASS

Two interacting partitions are a basic minimal setting for finite relational structures, epistemic equivalence frames, and \(C^2\) identification. The exact first loss of reconstructibility and unique obstruction identify the smallest way locally identical intersection behaviour can conceal globally different incidence connectivity. Enumerating the complete first layer is a natural benchmark rather than an arbitrary graph slice, and the 3,017-to-3,016 distinction is a logical statistic not provided by the pre-existing matrix count. The result is finite and deliberately limited; no downstream general theorem is asserted.

## Sources and limitations

The primary historical texts were inspected in their relevant sections: Kiefer–Schweitzer–Selman, introductory logic correspondence and relational-structure classification (Theorem 27 and Corollary 29); Pratt-Hartmann, Sections 1–2 and 7; OEIS A007716, enumerator definition, formula and values. This is a self-review, not a substitute for outside priority or code inspection. Only new work was assessed.

Self-review: passed. Independent audit: not yet performed.
