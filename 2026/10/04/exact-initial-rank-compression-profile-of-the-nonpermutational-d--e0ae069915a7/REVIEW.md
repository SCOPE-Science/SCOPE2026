# Review of Exact initial rank-compression profile of the nonpermutational \(D^{\prime\prime}_n\) automata

## Correctness
PASS. Both letters have exactly one collision pair and rank \(n-1\). The image after a nonempty suffix letter always omits one member of the collision pair needed for an effective \(b\), so only the initial \(b\) can reduce rank. Effective occurrences of \(a\) after the first drop must be separated by \(b\). This yields the lower bound \(2s-2\), and equality forces \((ba)^{s-1}\). The explicit hole induction
\[
Q\setminus Q(ba)^k=\{2,4,\ldots,2k\}\cup\{n\}
\]
proves attainability precisely through \(k=\lceil n/2\rceil-1\). Exhaustive power-automaton breadth-first search for \(4\le n\le18\) verifies all claimed thresholds, uniqueness, and the strict next boundary; direct replay verifies the hole formula for \(4\le n\le200\).

Risk: the finite checks cannot prove the infinite statement, but the infinite statement has an independent symbolic proof.

## Originality
PASS with residual bibliographic risk. The 2010 source introducing the family and the 2013 extended treatment both state the reset threshold \(n^2-3n+2\) and describe the coloring; inspection did not find the intermediate-rank profile, its unique shortest words, or the saturation boundary. Searches combining the family name with “rank”, “deficiency”, “compression”, “shortest word”, and “intermediate rank” did not locate an equivalent result. General minimum-rank and compression results do not imply these exact family-specific thresholds.

Risk: failed searches do not establish novelty, and an older unindexed source may use different terminology.

## Value
PASS. The family is a classical slowly synchronizing example whose two letters are both nonpermutations. The theorem separates its early behavior from its final quadratic synchronization: rank falls to about one half at the locally minimal linear cost, then the same mechanism saturates. The exact boundary and unique optimal words give a reusable structural benchmark for rank-compression questions in slowly synchronizing automata.

Risk: the result is deliberately local to the initial profile and does not solve the remaining thresholds.

## Closest literature and limitations
The closest sources are Ananichev–Gusev–Volkov (2010) and their 2013 extended treatment. They prove the complete reset threshold and discuss the family’s extremal reset behavior, while the present statement resolves a different invariant: shortest length as a function of target rank over the initial deficiency range. No implication from the cited reset-threshold theorem to the present profile was found.

Same-model review: passed. Independent audit: not yet performed.
