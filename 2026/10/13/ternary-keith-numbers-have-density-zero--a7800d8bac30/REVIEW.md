# Review

## Correctness
PASS. The proof reconstructs the base-\(3\) specialization of the Klazar--Luca recurrence comparison. Choosing \(\alpha=7/20\) gives two strict, independently checked inequalities: \(\alpha>1/3\), which makes the class with at least \(\alpha n\) zeros exponentially sparse by a binomial large-deviation bound, and \(3^\alpha<3/2\), which makes the suffix-comparability contradiction work. For zero-poor strings, the published recurrence asymptotic forces \(2^{m-n}n\asymp3^n\), hence only \(O(1)\) possible recurrence indices. Fixing such an index and a long prefix leaves an antichain of suffixes, giving \(O(3^n/\sqrt n)\) candidates per digit length and therefore \(O(x/\sqrt{\log x})\) globally. No finite search is used to prove the infinite statement.

## Originality
PASS. The closest primary paper explicitly proves the density estimate for decimal Keith numbers and notes that its modifications cover bases \(b\ge4\), while stating that base \(3\) is not covered because its two crude parameter inequalities are incompatible. The present proof changes exactly that bottleneck using the sharp zero-frequency threshold \(1/3\). Targeted searches for “ternary Keith numbers”, “base 3 Keith numbers”, and density formulations found no later theorem covering the case. The inspected exact databases likewise do not state it.

The residual originality risk is an unindexed recreational or unpublished note on ternary Keith numbers.

## Value
PASS. This resolves a concrete base case explicitly isolated in the foundational density paper, with the same quantitative upper bound as in the already-settled bases. The repair is structural rather than computational: it identifies that the failure comes from a crude combinatorial estimate and replaces it by the correct binomial large-deviation threshold. The method also explains sharply why base \(3\), unlike base \(2\), still lies on the density-zero side of this argument.

Self-review: passed. Independent audit: not yet performed.
