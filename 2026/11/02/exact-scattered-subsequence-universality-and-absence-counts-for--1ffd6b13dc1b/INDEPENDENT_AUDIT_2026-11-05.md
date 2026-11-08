# Independent mathematical audit

## correctness

PASS

For binary standard Rudin–Shapiro parity r(t)=popcount(t & (t>>1)) mod 2, k>=4, the proof derives the shortest-absent two-choice greedy suffix recurrence; all 12 sixteen-bit block transitions preserve equal option counts with factor 2^(Delta m-4); composition proves |SAS(W)|=2^(iota(W)-4q) for every nonempty word in exactly the four literal blocks. The four-letter morphism and dyadic edge recursion E(2q)=-E(q)-1 yield iota(R_k)=5*2^(k-4)-e_k and |SAS(R_k)|=2^(2^(k-4)-e_k). I independently recomputed all 12 transitions, all 340 block concatenations for q<=4 and full prefixes k=4..12 with a separately written dynamic program; these corroborate the fully described inductive argument.

## originality

PASS

Best-of-knowledge exact claim-vs-prior comparison after this run’s independent Resultary search and primary-source checks. The direct proof uses a block-state invariance plus dyadic parity recurrence not supplied by generic SAS or automatic-word factor results; unrelated factor, lexicographic and extremal theorems do not imply these exact values. Priority qualified: A specialized older automatic-sequence scattered-subword result under another terminology could contain this exact formula.

## value

PASS

A natural automatic sequence has an exact infinite-rank scattered-universality profile and an unexpectedly multiplicative shortest-absence count for an entire four-block concatenation language. The theorem is neither a renaming of a generic absent-subsequence algorithm nor a tiny isolated table; it yields concrete exact dyadic parameters and structural transfer invariance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
