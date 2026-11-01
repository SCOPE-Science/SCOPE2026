# Scientific review

## Correctness

**PASS.** For every \(n\ge4\), total domination in the line graph of a complete graph is equivalent to an edge-selected graph with at most one isolated vertex and no \(K_2\)-component. The exact lower bound and equality classification follow from the component inequalities \(v_i\le3e_i/2\) and \(c=s-h+\mu\le\lfloor s/3\rfloor\), with \(\mu\ge0\). These show all optimum components are trees and force exactly the stated orders. Unordered labelled component partition counts use the standard values three, sixteen and 125 for trees on three, four and five vertices. The standalone enumerator checks the full candidate space for \(4\le n\le10\), including the numerical multiplicities and structures. It is a finite consistency check, not the infinite proof.

## Originality

**PASS, with historical-priority qualification.** The nearest directly applicable result, Cornet–Dravec–Torres (arXiv:2610.04675, Theorem 14), gives the value of the minimum total domination number and sample minimizing constructions, but its relevant proof does not enumerate or classify every minimizing set. The prior assertion of the minimum value is excluded from the new contribution. The equivalent language is minimum total edge domination of the complete graph; targeted searches under that terminology and searches of mathematical result records found no direct count. Pan–Yang–Li–Xu (arXiv:1910.02431) addresses complexity and trees, but its complete manuscript was not materially inspected and is a residual risk. Missing matches cannot establish universal novelty.

## Mathematical value

**PASS.** Minimum-solution multiplicities are natural refinements of an exact extremal parameter for a prominent strongly regular family. The result is not simply another construction attaining the known minimum: it gives a complete forest characterization and closed counts for all values of \(n\), including the additional order-five-tree and double-order-four-tree families occurring only when \(3\mid n\). These reveal the structure and degeneracy of optimum solutions, useful when enumerating or uniformly sampling optimal total dominating sets.

## Scope and residual risks

The theorem is for labelled two-subsets \(J(n,2)\) and minimum total domination only. It does not settle the historical presence of equivalent formulas in hard-to-index work under other edge-domination terminology and does not treat orbit counts or larger selected sets.

Self-review: passed. Independent audit: not yet performed.
