# Self-review

## Correctness — PASS

The quantifiers cover all finite alphabets, all least periods \(p\ge2\), and all purely periodic words with infinitely many palindromic prefixes. A long palindromic prefix extends to a global reflection symmetry. A palindrome of length at least \(p\) therefore has a unique center class modulo \(p\) and can be expanded by \(p\); a palindrome longer than \(p\) can be contracted. Since every prefix has minimum palindromic length at most \(p\), pigeonhole arguments in both directions establish the cutoff \(n>p(p-1)\). Rukavicka's explicitly cited translation lemma prevents an exceptional early maximum; Fischler's residue statement is also directly reproved. The asymptotic counting then follows by congruence classes. The two-run family is proved exactly, not inferred from experiments. A standalone verifier independently checks many finite instances, without treating them as an infinite certificate.

## Originality — PASS (priority risk remains)

Rukavicka (2026) proves a universal finite lower bound and supplies a monotonicity lemma but expressly does not assert an ordinary-limit theorem for arbitrary words. Fischler (2005/2006) already proves the periodic palindrome-prefix residue pattern, so that fact is not new. The new assertion is the uniform effective quadratic threshold for the **minimum palindromic factorization** sequence, from which an exact finite-scan limit follows, together with the sharp period-dependent upper envelope. Bucci–Richomme studies greedy, rather than minimal, lengths; Rukavicka's 2020 repeated-palindrome work treats a different lower-bound problem. Searches of published mathematical findings and accessible prior claims were checked for equivalences, stronger implications, aliases, and the exact cutoff or density. These searches do not establish universal priority; unindexed work and a potentially implicit derivation from cited lemmas are residual risks.

## Value — PASS

The 2026 paper explicitly leaves ordinary-limit behavior unresolved generally. For the full natural class of palindrome-rich periodic words, this result both proves convergence to an integer and supplies a uniform finite stopping rule to compute its exact value, with a sharp family reaching the largest possible value for every period. This is a structural classification of long prefixes and a quantitative boundary to an active palindromic-density question; it is not a parameter substitution or an arbitrarily chosen finite table. The result neither claims a universal limit for aperiodic words nor proves optimality of the cutoff.

## Closest literature and limitations

Directly relevant: Rukavicka, arXiv:2609.15146v1 (Lemma 6.1, Proposition 6.2, Remark 6.3); Fischler, arXiv:math/0501420v3 (Lemma 5.6). Context: Bucci–Richomme, arXiv:1606.05660; Rukavicka, arXiv:2005.01371. The exact cutoff and limit may be implicit in unindexed earlier work; independent publication-priority and proof checks are still outstanding.

Self-review: passed. Independent audit: not yet performed.
