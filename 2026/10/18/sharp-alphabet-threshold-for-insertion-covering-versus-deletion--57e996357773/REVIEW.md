# Scientific assessment

**Correctness — PASS.** The robust-superword lemma turns the covering implication into a universal subsequence statement. Explicit witnesses handle targets of length at most two on any alphabet and length three in binary; direct missing-pattern codes prove attainability, with the binary upper bound obtained by counting consecutive-zero gaps. Every case includes all positive radii. Separate short-range enumeration (`verify.py`) supports the proofs without replacing infinite quantifiers.

**Originality — PASS within examined evidence.** Xie–Sun–Ge, arXiv:2606.15379v1, Section III, give the separation and a binary \(R+4\) counterexample; the present assertion is the sharp *earliest possible* length on each alphabet, and the nonbinary \(R+3\) construction. Lenz–Rashtchian–Siegel–Yaakobi, arXiv:1911.09944, study quantitative covering bounds rather than the all-radii implication threshold. Searches for the threshold, the \(R+3\) ternary onset, and aliases involving missing scattered-subsequence patterns identified no decisive prior theorem. Risk: an equivalent result under a different supersequence/containment terminology or in uninspected portions of the earlier literature.

**Value — PASS.** The recent discovery of non-equivalence raises a natural exact boundary question: what is the first blocklength where the two covering notions can disagree? A complete classification for all radii and alphabet sizes identifies a genuinely alphabet-dependent transition and distinguishes a ternary three-pattern obstruction from the binary four-pattern obstruction. It does not claim new asymptotic code-size bounds.

Self-review: passed. Independent audit: not yet performed.
