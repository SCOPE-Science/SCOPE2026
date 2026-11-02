# Review of the ternary-length \(2\)-binomial Cantor spectrum

## Correctness
PASS. At fixed binary word length, the pair (number of ones, scattered-`01` count) determines every subsequence count of length at most two. The length-\(3^k\) block decomposition contains only `00`, `01`, and `10` adjacent substitution-block pairs, so both arithmetic families are exhaustive. Ternary positions, palindrome reversal, and the interval intersection formula reproduce the exact count. The explicit \(3\)-block collision construction produces distinct literal factors and pairwise distinct profiles. Independent rolling-window enumeration was checked for substitution levels 1–7, with collision witnesses at levels 3–7. Limit: finite experiments alone do not prove the unrestricted statement.

## Originality
PASS under accessible priority evidence, not an independent certification. The closest inspected works introduce general binomial complexity and settle Sturmian/Thue–Morse and Tribonacci classes, without the present Cantor-word arithmetic profile family or its explicit linear-collision theorem. The Parikh-constant morphism bound in the 2015 paper does not cover \(1\mapsto101,0\mapsto000\). Targeted semantic-record and primary-source searches did not reveal an equivalent result. Historical priority remains a residual risk.

## Value
PASS. This is a natural complete structural invariant at the substitution lengths of a classical nonprimitive automatic word, not a chosen finite slice: it gives all attainable binomial profiles and an exact compact arithmetic counting formula, while exposing a linear-scale, explicitly witnessed failure of profile injectivity. That behavior contrasts with the published all-length injectivity results for Sturmian and Tribonacci words. A simple closed formula for the summation is intentionally not asserted.

## Closest literature and limitations
Rigo–Salimov (WORDS 2013; TCS 2015), and Lejeune–Rigo–Rosenfeld (Adv. Appl. Math. 2020), as cited in `RESULT.md`. The result is restricted to the specified Cantor fixed point, the \(3^k\) length subsequence counts, and order two. Publication priority has not been independently established.

Self-review: passed. Independent audit: not yet performed.
