# Review of Seven atoms suffice for full-NRD failure of right-tail dependence

## Correctness
PASS. The finite-state definition reduces full NRD to conditional stochastic-order comparisons over increasing upper sets. For every comparable pair of conditioning values with positive marginal mass, cross multiplication preserves the inequality. The packaged verifier enumerates all \(74\) formal comparisons, correctly omits the \(10\) comparisons having a zero-probability conditioning value, and checks all \(64\) applicable inequalities exactly. It reports \(57\) strict inequalities, \(7\) equalities, and minimum positive integer slack \(6\). The NRTD failure is independently visible from \(7/24<2/5\), with cross-product slack \(-13\).

Risk: the argument proves only the displayed law. It does not convert a bounded computational search into a universal lower bound on support size.

## Originality
PASS. The closest primary source is Su--Hu, arXiv:2609.23313v1. It proves a full-NRD/non-NRTD counterexample on a strictly positive \(2\times2\times3\) rectangle and minimality of the rectangular state-space product, while its sparsity discussion explicitly does not assert the sparsest number of positive atoms inside that grid. The new claim is therefore not a restatement of the source's rectangular minimality. Focused searches for sparse-support, seven-atom, and support-cardinality formulations did not locate an implication-equivalent published claim. The 2025/2026 Su--Zou--Hu tournament paper concerns structured tournament score vectors, not this generic sparse finite-state construction.

Residual risk: the motivating paper is recent, and an equivalent sparse witness could exist in poorly indexed or unpublished material. No claim of global uniqueness or exact support minimality is made.

## Value
PASS. Support cardinality is a natural structural invariant here because the motivating paper itself separates minimal rectangle size from sparsest support. Reducing the witness from a strictly positive \(12\)-cell table to \(7\) positive cells shows that the failure of NRTD is not an artifact of dense positivity and gives a substantially smaller exact object for future classification or extremal analysis. The result is useful even without closing the remaining lower-bound problem.

Same-model review: passed. Independent audit: not yet performed.
