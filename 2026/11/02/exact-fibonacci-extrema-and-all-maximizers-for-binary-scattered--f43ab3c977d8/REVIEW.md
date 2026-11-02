# Scientific review

## Correctness — PASS

The exact endpoint-symbol decomposition partitions distinct nonempty palindromic subsequence patterns by their common first/last symbol and uses the earliest and latest occurrences to identify the entire admissible middle set, without double counting. The same-endpoint binary case yields the bound \(4+M_{n-2}+M_{n-4}\); the different-endpoint case yields \(4+2M_{n-3}\). Single-letter and singleton-symbol cases are strictly suboptimal for \(n\geq4\). The Fibonacci identities give equality in the first bound at all lengths, equality in the second only at even lengths, and a strictly positive odd-length gap \(F_{m-1}\). All candidate maximizers attain equality in the exact recursion; induction on equality conditions forces no others. Exhaustive and independent-method finite checks corroborate the proof but do not certify arbitrary lengths computationally.

## Originality — PASS (bounded literature comparison)

Mahalingam–Pandoh's 2021 work is the closest direct predecessor. It already prints the first ten binary maxima and gives algorithms and a weaker all-alphabet upper bound; its sharp \(q\)-sensitive theorem applies only to \(q\geq n/2\), and its conclusion explicitly leaves \(q<n/2\) open. For fixed binary alphabet \(q=2\), all \(n\geq5\) lie outside that proved sharp domain. The new claim provides a proof for every such length and an exhaustive structural equality classification. Holub–Saari (2009) instead addresses reconstruction of a word from its palindrome set and related longest-subsequence structures; Müllner–Ryzhikov (2019) instead concerns longest palindromic subsequence length. Semantically close research records about Fibonacci absent subsequences, duplication codes, contiguous palindromes and string attractors have different objects or optimizing parameters. The cited earlier numerical table is credited, not claimed as new. A missed equivalent publication remains possible; absence from search results is not proof of worldwide uniqueness.

## Mathematical value — PASS

This establishes a closed exact capacity for a natural low-alphabet extremal observable, solving the binary instance of the specifically noted \(q<n/2\) gap and classifying **all** attaining words. The parity distinction and forced endpoint structure are mathematically informative independently of verification-code implementation. The result is not claimed to solve the variable-alphabet conjecture.

## Closest sources and limitations

1. Mahalingam and Pandoh, *Counting scattered palindromes in a finite word*, 2021, arXiv:2108.02729; Sections 4–6 and Table 4.
2. Holub and Saari, *On Highly Palindromic Words*, 2009, https://www.karlin.mff.cuni.cz/~holub/soubory/subpal.pdf ; Sections 4–5.
3. Müllner and Ryzhikov, *Palindromic Subsequences in Finite Words*, 2019, arXiv:1901.07502; longest-palindrome problem.

The scope is fixed binary, nonempty distinct scattered palindrome patterns on linear words. No independent scientific audit has been performed and the bounded comparison retains literature-overlap risk.

Self-review: passed. Independent audit: not yet performed.
