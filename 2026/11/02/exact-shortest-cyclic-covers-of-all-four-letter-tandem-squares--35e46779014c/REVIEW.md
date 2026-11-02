# Self-review

## Correctness — PASS

The proof selects one occurrence of each of the \(q^2\) targets, converts the cyclic covering length to a lower bound on a target Hamiltonian tour, and classifies all distinct-square overlaps as shifts one, three or four. The nonstandard step is the letter-connectivity inequality \(2s+z\ge q\): used reverse-square transitions contract into loops, unused reverse-square pairs can connect at most \(s\) distinct letter pairs, and nonoverlapping jumps connect at most \(z\) more. A connected letter graph must visit all \(q\) constant-square blocks. In the all-loop case the closed walk requires at least \(q\) jumps. This proves the lower bound, and the explicit construction meets it for every \(q\ge2\). Independent finite enumeration of small target-order tours and exhaustive binary cyclic strings corroborate, but are not used as the infinite proof. The overlap-graph reduction and all boundary cases were checked directly.

## Originality — PASS (qualified)

The inspected general universal-cycle and superstring papers [1]–[4] concern exact-once cycle existence, other restricted word families, or general shortest-superstring bounds. They do not, in the material inspected, imply the exact single-cycle all-tandem-square formula. Direct comparisons with analogous exact four-letter ordinary-palindrome and reverse-complement-palindrome covers find different target families: \(abba\) and \(ab\bar b\bar a\) do not give an \(abab\) cover, nor does either published formula imply this one. Searches of related computational research records and full-text literature produced no covering formula. The residual risk is a difficult-to-index equivalent in motif-cover or periodic-word literature, particularly a generalized theorem whose stated parameters subsume this case. The search is evidence against immediate coverage, not a proof of uniqueness.

## Mathematical value — PASS

All two-letter-root tandem squares form a canonical family of \(q^2\) motifs. A shortest single cyclic test word covering all such motifs is a natural finite exact optimization problem in constrained superstring design. The all-alphabet capacity \(2q(q+1)\) is not a small numerical improvement or an arbitrary slice. The sharp connectivity obstruction, unlike a brute-force calculation, explains the additional cost of integrating the otherwise maximally-overlapping reverse-square pairs into one circular sequence. The construction gives a direct generator for optimal covers of any alphabet size.

## Closest literature and limitations

[1] Chen, Kitaev and Sun, arXiv:1908.01116; [2] Gardner and Godbole, arXiv:1711.07029; [3] Sawada, Sears, Trautrim and Williams, arXiv:2308.12405; [4] Cazaux, Juhel and Rivals, DOI:10.4230/LIPIcs.SEA.2018.18. General universal-cycle and superstring methods are background rather than direct closed-form coverage. Longer-root squares, linear covers and target-exact universal cycles are not established here. Search-index incompleteness remains a novelty limitation.

Self-review: passed. Independent audit: not yet performed.
