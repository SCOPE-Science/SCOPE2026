# Review of exact cyclic-rotation richness

## Correctness

**PASS.** The fixed-point identities and forbidden patterns are elementary consequences of \(\sigma(0)=01\), \(\sigma(1)=00\). The exact even/odd factor decomposition gives a disjoint class-size doubling for source lengths at least two; both exceptional bases are computed directly. At odd length, each circular pattern of ones has exactly one odd separation and an occurring rotation must place this separation across its boundary, leaving at most three cuts because a run of four zeros is forbidden. For every odd length, the explicit even-distance two-one construction produces a factor \(00u00\), and therefore three distinct occurring rotations. Together these prove the exact result for every positive length. `verify.py` checks exact finite factor sets through length 192; this is corroboration rather than an infinite proof.

## Originality

**PASS within the inspected record, with documented residual risk.** Cassaigne et al., arXiv:1402.5843, Section 5.1/Proposition 10, count aggregate cyclic classes at dyadic lengths but do not give the all-length maximum rotation-multiplicity law or full-primitive-orbit support. Charlier et al., arXiv:1505.03848, address group orbit complexity bounds and different constructions. Searches for rotation classes, aliases in Lie complexity, and exact \(2\)-adic length laws disclosed no covering published result. The closest conceptual source is Bell and Shallit, arXiv:2102.03821: its accessible abstract defines the related full-conjugacy Lie complexity and gives general decidability/boundedness, but the full text was inaccessible and might contain a special case not visible in the abstract. This risk does not establish coverage. An unindexed statement is a further residual risk.

## Mathematical value

**PASS.** The occurrence of every cyclic rotation is a motivated refinement of the known cyclic-complexity problem for this classical substitution word. The theorem supplies a sharp all-length extremal function, a sparse arithmetic classification of lengths supporting complete primitive rotation orbits, and a classwise substitution-renormalization mechanism. Its odd-gap obstruction and universal two-one witness make these consequences structural, not merely a restatement of a dyadic class-count computation.

## Closest literature and limitations

Primary comparison: Cassaigne–Fici–Sciortino–Zamboni (2014), arXiv:1402.5843, Section 5.1. Related theory: Bell–Shallit (2021), arXiv:2102.03821, abstract only, with unresolved full-text overlap risk; Charlier–Puzynina–Zamboni (2015), arXiv:1505.03848, group action results. No complete distribution of odd-length conjugacy-class sizes or independent audit is claimed.

Self-review: passed. Independent audit: not yet performed.
