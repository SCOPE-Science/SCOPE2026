# Mathematical review

## Correctness — PASS

For a finite alphabet containing at least two symbols and an integer \(k\ge 2\), a factor is uncompletable for the code with exactly one missing length-\(k\) word if and only if occurrences of the missing block meet all residue classes modulo \(k\). The forward direction follows from the freedom to extend both partial endpoint blocks. Every selection of occurrence representatives gives a spanning path in the residue graph whose inexpensive edges correspond precisely to proper periods. Kruskal's gcd-component calculation gives a lower bound. The recursively translated forward paths realize exactly its weight: at each step, copies lie in distinct cosets; overlapping translates are consistent by period addition. Therefore the formula applies to all words, including bordered ones with several incommensurate proper periods. The independent KMP and factor-NFA searches verify all \(508\) binary cases at lengths 2–8 and \(124\) binary cases at lengths 2–6, respectively; finite checks are corroboration, not a substitute for the infinite proof.

## Originality — PASS, subject to historical-priority risks

Pribavkina (arXiv:0907.4576, Proposition 2) already proves the maximal \(k^2+k-1\) length for unbordered deleted words. Fici–Pribavkina–Sakarovitch (arXiv:1002.1928v2, Sections 2–3) also treats the one-hole boundary under an unbordered assumption. Chandelkar and Chadha (arXiv:2609.30817v1, Proposition 5.1) give an unbordered special example and a different general-code upper bound. The new classification handles arbitrary *bordered* deleted words through all of their periods; the cited results do not state that extension, its exact gcd formula, or the matching spanning-path construction. Indexed theorem and equivalent-formulation searches did not reveal a covering statement. Gusev and Pribavkina's 2011 paper addresses broader incomplete-code bounds; its full text was not inspected, so that source remains a stated priority risk. Absence of a search hit alone does not establish novelty, and further literature may contain equivalent results.

## Value — PASS

The complete one-hole word-code family is a canonical test case in code completeness and automata. The theorem transforms an established maximum for unbordered holes into an exact classification of *every* hole by its entire period structure, including mixed-border cases. The expression provides a reproducible arithmetic answer without enumerating an exponential code, constructs extremal missing factors, and isolates the unbordered/constant extremal boundaries. This is substantive structural information beyond a numerical special case.

## Scope and remaining limitations

The theorem makes no assertion about several missing words, nonuniform code lengths, or all shortest-witness multiplicities. The key proof uses a forward Hamilton-path construction, whose nonconsecutive overlap compatibility is justified by the period-addition lemma. Independent scientific audit and unrestricted historical-priority certification have not occurred.

Self-review: passed. Independent audit: not yet performed.
