# Scientific review: Sharp quasi-total Roman domination and exact optimizers of rook graphs

## Correctness — PASS

The proof derives the forced-label bound \(\omega(f)\ge 2k+(m-a)(n-b)\), checks all integer defender counts and classifies every possible equality case. The mandatory label-\(1\) cells lie outside every occupied row and column and therefore cannot support any defender. That observation rules out false equality cases. Exact counts follow from a block-partition bijection, with explicit separate counts on the \(2\times2\) and \(3\times3\) boards. The included graph-based exhaustive checker corroborates eleven finite instances, while an independent defender-map checker covers five additional instances. Finite tests are not treated as a proof of the universal theorem.

## Originality — PASS, with bibliographic limitations

The foundational definition in Cabrera-García, Cabrera-Martínez and Yero (arxiv:1903.09789, March 2019) and the bounds developed in Cabrera Martínez et al. (*Mathematics* 9 (2021) 2823) do not furnish the exact optimal rook classification or count. The closest same-object result, Mertens (*Domination Polynomial of the Rook Graph*, arxiv:2401.00716), counts ordinary dominating sets; it does not test whether a defender has a positive-labeled neighbor or count the label-\(1\) exceptions. A related equivalence with minimum total edge-dominating sets of complete bipartite graphs was searched explicitly. Potential unindexed matching enumeration remains a residual risk.

## Value — PASS

This is a complete, motivated, all-size classification of optimum quasi-total Roman functions, not an isolated numerical improvement. The associated-Stirling formula explains the exact multiplicities, and the square boards of orders \(2\) and \(3\) exhibit additional configurations that disappear at order \(4\). This specifies a natural extremal coefficient in an established graph-defense invariant.

## Scope and limitations

The count covers every optimum function but not functions of nonoptimal weight. No literature search proves absolute uniqueness. The published texts were independently compared for mathematical implication, and no independent external mathematical validation of this theorem is claimed.

Self-review: passed. Independent audit: not yet performed.
