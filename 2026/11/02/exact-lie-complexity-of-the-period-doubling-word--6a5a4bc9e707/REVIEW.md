# Scientific review: exact Lie complexity of the period-doubling word

**Correctness — PASS.** The claim is exact for every positive length, with explicit zero-based indexing and an all-rotation definition. All ones lie in odd absolute positions; the fixed point avoids \(11\) and \(0000\). These exclude odd lengths greater than three. The critical doubling step is a class-level bijection: aligned even rotations come from the morphism and odd rotations come from adjoining the guaranteed next zero; conversely any accepted even-length class desubstitutes uniquely because a word with a one has a forced alignment. Direct base enumerations give \(L_p(1)=L_p(2)=L_p(3)=2\). The independent finite verifier returned `VERIFY_OK` but does not replace the proof.

**Originality — PASS, qualified.** Bell–Shallit [1] define Lie complexity and provide a general automaticity result plus examples for other well-known words; no period-doubling formula appears in the inspected examples. Cassaigne et al. [2] derive the weaker *cyclic complexity* value \(c_p(2^a)=2\), which is not the all-rotation Lie condition and leaves other lengths undetermined. Li [3] gives general bounds/extended invariants, while De Luca–Fici [4] specializes to Sturmian words. Published-record searches using the exact invariant, conjugacy aliases, length support and substitution returned no matching statement. The closest published-record result involving period doubling addresses a three-block difference lift, while the closest accessible prior claim involves Burrows–Wheeler transforms. Unindexed equivalents remain possible.

**Value — PASS.** Exact Lie complexity of a specific canonical non-Sturmian automatic word is a motivated complete structural classification. It identifies the full accepted-length language, an exact two-class multiplicity, a lacunary generating function and a simple desubstitution bijection; these are not consequences of the general automaticity theorem alone.

Scientific limitations: the formula applies to the stated morphism only, not all automatic or Toeplitz words; finite tests are not infinite proofs. There is residual novelty risk from unindexed literature. The result has not received independent external validation.

Closest literature: [1] Bell–Shallit, arXiv:2102.03821, Section 7; [2] Cassaigne–Fici–Sciortino–Zamboni, arXiv:1402.5843, Proposition 17 and Example 1; [3] Li, arXiv:2207.05859; [4] De Luca–Fici, arXiv:2206.00995.

Self-review: passed. Independent audit: not yet performed.
