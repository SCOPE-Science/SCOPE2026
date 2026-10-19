# Scientific review

## Correctness: PASS

The claim has exact integer quantifiers and fixes the ambient alphabet. The proof first establishes, by comparing positions of the unique central symbol, that the borders of a finite Zimin word are precisely the shorter Zimin words. It then proves a right-extension lemma for every prefix and isolates all minimal absent words containing the new central symbol: those with that symbol at one end arise exactly from noninitial extensions of Zimin prefixes, and those with that symbol at both ends arise exactly from borders. Inheritance of all earlier forbidden factors completes a disjoint induction. Independent direct factor enumeration through \(k=8\) confirms the sets and exact length histograms. The finite test is not used as proof of the infinite statement.

## Originality: PASS, subject to residual bibliographic risk

Full primary manuscripts inspected: Conlon–Fox–Sudakov (2017), which studies unavoidable pattern *instances* rather than absent literal contiguous factors; Charalampopoulos et al. (2018), which proves bounds and sequence-comparison algorithms using general minimal absent words; Ayad et al. (2019), which gives output-sensitive antidictionary algorithms; Akagi et al. (2022), which gives run-length-based MAW categories and data structures. No result inspected there gives the complete finite-Zimin set, the dyadic-only forbidden lengths, or the exact cubic total. An output-sensitive algorithm that could compute an instance is not a theorem identifying the displayed formula. Targeted searches for Zimin / ruler / abacaba / antidictionary / forbidden factor combinations did not produce an equivalent theorem. The possibility of an unindexed or differently phrased result remains unresolved; absence from a database is not a proof of novelty.

## Mathematical value: PASS

Canonical Zimin words are foundational recursively generated pattern objects of exponential length. Their **entire** minimal-absent-factor set is a natural negative-information invariant of the corresponding factorial language. The theorem gives a complete infinite-family classification, a dyadic support phenomenon, and polynomially many minimal absent factors despite exponential input length. The two structural lemmas permit symbolic construction without generic suffix indexing, illustrating an exact case of compressed antidictionary determination. This is a structural invariant and complete classification, not a contrived subrange of parameters; no general output-sensitive algorithm improvement is claimed.

## Scope and residual risk

The exact alphabet is essential: adding unused symbols creates new singleton absent words. Ordinary factor occurrence must not be confused with scattered subsequences or variable-instantiated Zimin patterns. The relevance of later generic absent-word data structures was assessed by their available statements, but no full exhaustive search of all specialized or nonindexed material is possible. The independent audit channel has not been performed.

Self-review: passed. Independent audit: not yet performed.

