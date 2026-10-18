# Scientific review: integral five-cube theta homology

## Correctness

**PASS.** A complete enumeration of \(254475\) independence faces yields an explicit acyclic discrete-Morse matching with \(127231\) disjoint pairs and precisely \(12\) unmatched nonempty simplices in dimensions \(0,5,7\). The gradient graph has \(127231\) matched-pair nodes and \(99497\) directed transitions; the standalone verifier finds a topological ordering covering every node. No unverified assumption of acyclicity is used. Integral Morse differentials vanish since there are no consecutive critical dimensions. The precise integral Alexander-duality degree shift on \(32\) vertices is \(29-i\). A second exact independence-polynomial algorithm and Euler characteristic checks agree. The claim makes no inference from limited sampling or from rational ranks alone.

## Originality

**PASS on the examined evidence; literature-completeness risk remains.** Conant and Thistlethwaite's full-text Section 5.2, Theorem 5 gives only rational ranks for this exact theta complex and notes that the integer groups are undetermined. Their Alexander-duality result and ranks are treated as previous knowledge, not as new. A complete acyclic matching establishes the torsion-free integral groups, which do **not** follow logically from rational homology. Their other cube parameters and Okura's grid graph simple-homotopy formulas do not imply the precise result. Searches also compared the ordinary five-cube with separate indexed four-cube and folded-five-cube independence complex results; both have \(16\), rather than \(32\), vertices, and cannot be substituted. An unindexed later solution to the same 2008–2010 question cannot be categorically excluded.

## Mathematical value

**PASS.** The 2010 primary text explicitly identified the integral homology of this named, naturally occurring cube theta complex as unknown, while computing its rational groups. Integral homology detects torsion not visible to that calculation. The constructive finite acyclic matching resolves precisely the missing invariant, and Alexander duality gives the same answer for a natural simplicial space of satisfiable formulae. The result does not depend on an arbitrary parameter slice: \(\operatorname{Cube}(5,1)\) is the first unresolved edge-cube case in the historical table. No paper-scale or infinite-family classification is asserted.

## Closest literature, limitations and residual risks

The closest directly relevant primary source is Conant–Thistlethwaite, arXiv:0808.0739v2, Section 5.2, Theorem 5; the authors did not settle integral torsion. Okura, arXiv:1908.09356v1, concerns grid graph replacements and different graph families. Indexed public results on the four-cube and the folded five-cube were checked for object identity and implication; neither gives the five-cube answer. Residual risk: independently published later work using an alternative name for the same cubical theta/Boolean-formula space may have been missed. Mathematical limitation: the homotopy attaching maps of the critical seven-cells are not determined. The finite certificate remains independently auditable using the packaged verifier.

Self-review: passed. Independent audit: not yet performed.
