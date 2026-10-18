# Scientific assessment

## Correctness — PASS

For all 16 selected closure-rule sets, the unrestricted finite-support proof is based on the conjunction-tree extension of a finite saturated set, not an assumed bound on derivation length. The proof explicitly handles the interaction of `M`, `C`, `N`, and `K`, nested modalities, and arbitrary bracketed conjunctions. The one-world NP certificate is sound and complete by leastness of syntactic closure; plain propositional SAT and TAUT give the lower bounds. A separately implemented finite checker exercises 394 bounded-closure comparisons and 391 exhaustive Horn-set enumerations, without treating them as an infinite proof.

## Originality — PASS, with residual historical risk

Nishimura (2026, arXiv:2610.01433), Sections 2–3, already proves one-world completeness and primitive-recursive decidability, and explicitly mentions finite-subformula restriction; neither property is claimed as new here. The precise NP/coNP completeness conclusion is not stated in the inspected source. Dalmonte–Mazzullo (2023, DOI 10.1007/978-3-031-43513-3_17) studies logics including replacement of equivalents and therefore does not imply the noncongruential result; in that literature the agglomeration axiom can instead cause PSPACE-completeness. Targeted semantic search did not find an equivalent claim. Older syntactic/noncongruential modal complexity literature remains a plausible priority risk.

## Value — PASS

The source identifies computational complexity as an unresolved line of development and establishes only a primitive-recursive decision bound. The new result makes this exact for the entire natural rule-free modal-axiom lattice with a uniform small certificate. Its sharp treatment of the conjunction-aggregation case explains an informative boundary between purely syntactic modal consequence and ordinary congruential non-normal modal reasoning.

Self-review: passed. Independent audit: not yet performed.
