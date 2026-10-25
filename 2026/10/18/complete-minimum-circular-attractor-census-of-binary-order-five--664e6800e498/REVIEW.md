# Independent mathematical audit

## correctness

PASS

PASS: Each order-five binary de Bruijn cycle has exactly 32 distinct cyclic length-five windows; a marked position belongs to five of them, so every circular string attractor has at least ceil(32/5)=7 positions. Each cyclic word corresponds uniquely to a 32-vertex Hamilton tour of overlapping five-bit windows rooted at the unique 00000 occurrence; exact DFS counts 2048 such words. A seven-position set hits all unique length-five windows iff all cyclic intermarked gaps are at most five, giving exactly 384 candidates independent of the cycle. Those selected length-five incidences automatically hit any factor of length >=5; for lengths 1..4 the union-of-all-occurrence position masks supply necessary-and-sufficient tests. Independently implemented C++ reconstruction exhausted 2048 tours ×384 complete candidate sets, reproducing minimum 216 (4 words), maximum 368 (2 words), 120 distinct counts, and total 589120. Its deterministically sorted complete 2048-row CSV SHA-256 is 8bb608eb66f3bfac0152475146822a21df2a5ecb9665f2f9193ef22ec4291ea2, exactly matching frozen census.csv. Direct proof of exhaustive object/candidate parametrization converts finite enumeration to an exact finite theorem; no infinite claim made.

## originality

PASS

PASS best of knowledge: actual general-framework primary source text and result-set searches were checked against each exact claim, with the four distinct prior-implication tests documented. A universal over 2048 cyclic classes and every minimum-set multiplicity cannot follow from a theorem about one chosen linear word, nor from general verification or asymptotic bounds. The full finite exhaustive proof is extra mathematical content, subject to unlocated equivalent tables. No failed search is equated to a novelty proof; unaccessed primary material is named explicitly.

## value

PASS

PASS: Circular string attractors are natural factor-cover/hitting-set invariants of cyclic universal words. The known length-five window lower bound is sharp on every one of the 2048 order-five de Bruijn cycles, but numbers of extremal seven-sets vary nontrivially from 216 to 368. Full optimizer multiplicity census of a canonical closed finite family supplies useful optimality/rigidity data not determined by just one benchmark word or the optimum size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
