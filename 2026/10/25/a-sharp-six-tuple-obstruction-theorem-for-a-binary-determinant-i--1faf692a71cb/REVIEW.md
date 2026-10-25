# Review of the binary-determinant obstruction theorem

## Correctness — PASS

For a split of \(\operatorname{dep}(x,y)\lor\operatorname{dep}(y,z)\), each of two determinant values uses at most one red \(y\)-class; the blue residue must be \(z\)-constant per \(y\)-class. The resulting two-register characterization is equivalent to the original team semantics. Three mixed classes need six tuples; exactly two mixed classes admit two orientations, and the explicit false-orientation normal form proves the exhaustive four- and six-tuple classification. The enumeration weights of local types \(L,R,C\) are respectively \(t,t,2t\), where \(t=\binom{c}{2}\), giving \(N_4=2\binom{b}{2}t^2\) and \(N_6=(4\binom{b}{2}+44\binom{b}{3})t^3\). The six-tuple obstruction exists already on the \(2\times2\times2\) cube. The checker verified 1,450,240 finite subteams on seven benchmark domains, including direct split checks on three small domains, with `ALL_CHECKS_OK 11856`. The universal proof does not rely on those finite tests.

## Originality — PASS on the inspected evidence

Fröhlich–Kolaitis–Meier (arXiv:2508.16146, Theorem 25 and its proof) prove **unrestricted** incoherence of this exact disjunction, using growing first-coordinate alphabets; they do not give a two-valued determinant obstruction classification. Barlag et al. (arXiv:2605.31269, Sections 3 and 5) give general coherence and rewritability results without the restricted-value six-tuple spectrum or its labelled counts. Restricting to the special case \(z=x\) would not cover freely varying independent \(z\)-values in the general three-coordinate formula. Semantic searches for equivalent formulations, dominating results, and exact tables disclosed no matching implication or enumeration. A 2010 thesis on coherence was found, but its full text was not retrieved; this is an acknowledged residual priority risk, not evidence of uniqueness.

## Value — PASS

The two-element determinant domain is a natural Boolean-valued-data restriction. It transforms a known globally incoherent dependency disjunction into a family with a sharp constant forbidden-subteam bound and supplies the complete minimal-obstruction classes and a uniform polynomial labelled census for all remaining domain sizes. Such a complete bounded-domain description supports small-counterexample testing and concrete finite database benchmarks; neither correctness nor counting alone is being used as evidence of significance.

## Limits and independent review

The classification does not extend by assertion to arbitrary determinant alphabets, multisets or unprojected extra attributes. Equivalent older formulations in functional-dependency database decomposition remain possible. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
