# Scientific review

**Correctness — PASS.** For each of the 80 consecutive listed lengths, the included BWT last column has pairwise unequal consecutive symbols, one stable-rank LF cycle, and Hamming distance \(\lceil n/2\rceil\) from its sorted first column. The standalone checker independently reconstructs a primitive necklace, explicitly computes the sorted-rotation BWT, and counts its cyclic runs. The published factor-two lower bound supplies the opposite inequality. The exact range and cyclic-versus-linear normalization are explicit.

**Originality — PASS within examined evidence.** Kumallagov's original paper supplies small values through length 12 and particular primitive-root families; the latter do not imply complete consecutive sharpness over the interval \(81\le n\le160\) (notably at composite-related lengths 128 and 160). Fici and collaborators prove unclustered *existence* without minimizing input runs. Targeted public-literature and mathematical-research-record searches identified no covering consecutive finite theorem. Unindexed computations remain a priority risk.

**Value — PASS.** The result extends a difficult open extremal BWT question by 80 *consecutive* exact-length cases of this conjectured exact extremal property beyond the original paper's tabulated range. It crosses numerous lengths not supplied by the existing arithmetic prime constructions, and provides simple independently replayable objects rather than an unverified search tally. It is a meaningful finite cutoff, not a proof of the full conjecture.

**Scientific limitations.** The result relies on finite explicit certificates and a published general lower bound. It does not prove sharpness for lengths beyond 160, nor count all optimal solutions. The originality search does not guarantee historical priority.

Self-review: passed. Independent audit: not yet performed.
