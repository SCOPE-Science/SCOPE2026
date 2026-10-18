# Scientific review: factorial-square triple multiplicity

## Correctness

**PASS.** The squarefree-factorial collision classification follows from the classical Erdős--Selfridge consecutive-product theorem. The exact count of doubled consecutive-largest representations uses disjoint squarefree classes \(b_t\), and the \(O(\sqrt{\log(2X)})\) remainder follows from the published exponential growth of squarefree factorial parts evaluated at square indices. The passage from endpoint counts to a count of *all triples* requires, and explicitly invokes, Yudin's exceptional-endpoint bound together with the uniform \(X^\eta\) bounds on both nonconsecutive parameters. These estimates give the required multiplicity-weighted \(O_\varepsilon(X^{2/5+\varepsilon})\) error. The finite verification program executed successfully; it is not treated as an infinite proof.

## Originality

**PASS, with stated residual risk.** Tao's March 2026 paper already states that repeated squarefree factorial parts occur exactly at square indices. That fact is therefore acknowledged as classical/prior, not presented as a new lemma. Tao nevertheless proposes the distinct-endpoint constant \(C_0\) for the number of three-factor **solutions**. Yudin's October 2026 result counts eligible endpoints, with each squarefree part counted once, and controls exceptional nonconsecutive solutions by a separate theorem. These statements do not themselves give the multiplicity-corrected leading constant \(C_0+K\), which is larger. Comparison included the full relevant passages of both preprints and the entire accessible 2014 three-factor paper. Searches for triple counts, duplicate factorial squarefree parts, the conjectured coefficient, and equivalent formulations found no prior corrected asymptotic statement. Residual risk: a direct derivation using these existing tools is short; an uncatalogued note may already have pointed out the correction.

## Mathematical value

**PASS.** The contribution addresses an explicit, numerically testable asymptotic conjecture for the number of factorial-square triples, determines its correct leading coefficient and its positive excess, and explains the excess via an exact two-representation classification with a logarithmic-scale counting error. The question is meaningful because counting distinct endpoints and counting triples are different natural invariants. This is not merely a second expression for the already-known endpoint constant. It also yields a positive limiting fraction of three-factorable nonsquare endpoints having exactly two representations, while higher multiplicity is asymptotically negligible.

## Sources and limitations

F. Yudin, arXiv:2610.01899v1, Sections 1 and 3, supplies the endpoint asymptotic, exponential squarefree-part bound, and exceptional-representation estimates. T. Tao, arXiv:2603.27990v1, Section 1.3, contains the earlier explicit square-index observation and proposed coefficient. A. Dujella, F. Najman, N. Saradha and T. N. Shorey, *Products of three factorials* (2014), supplies historical examples without a general multiplicity asymptotic. The original Erdős--Selfridge theorem was checked through these literature statements rather than via its 1975 full text. The precise decimal of the infinite correction constant is not independently certified here. The theorem is conditional on no conjectures, but rests on the validity of the published analytic estimates.

Self-review: passed. Independent audit: not yet performed.
