# Research review

## Correctness — PASS

The linear update decomposes exactly as \(F=D+U\) on vertex basis vectors. For every nonleaf the number of children is divisible by the field characteristic, so \(UD=0\). Height gives \(D^{h+1}=U^{h+1}=0\), yielding a noncommutative word expansion with precisely one term per pair of exponents. The terminal powers are exactly \(F^{2h}=D^hU^h\), of rank one, and \(F^{2h-1}=D^hU^{h-1}+D^{h-1}U^h\), of rank two; each rank is witnessed by inputs on appropriate depth levels. The general extinction bound follows, as do all last-shell probabilities by rank-nullity over \(\mathbb F_q\). Nonextinction for complete trees with mismatched characteristic is proven by an invariant difference of two child subtrees and induction from the star case. The attached verifier reruns small complete and irregular cases over characteristics two and three. The proof covers all sizes without relying on these checks.

## Originality — PASS, qualified

Rojo (DOI:10.1016/j.laa.2005.09.019), including the adjacency-polynomial theorem, treats root-tree spectra over the usual real/complex setting. Rojo–Robbiano (DOI:10.1016/j.laa.2007.06.024) and Fritscher–Trevisan (DOI:10.1137/15M1013262) treat eigenvalue structure, while Aledo–Martínez–Valverde (DOI:10.1155/2015/594294) surveys general parallel-dynamics orbit questions. The available material shows no exact characteristic-divisible irregular-tree extinction index together with shape-independent terminal-shell distribution. Finite-field nilpotency can in some balanced special cases be inferred from specialized determinant identities, but that does not establish the sharp penultimate ranks, irregular branching coverage or final probability law. Targeted searches for equivalent terminology and general results yielded no decisive implication. Residual risk remains from unindexed work or parts of less-accessible prior full texts; this is a qualified, self-review originality assessment, not a proof of global uniqueness.

## Value — PASS

The natural invariant is first entry into the only periodic state of a network-wide additive finite-field dynamical system. The theorem gives a sharp height-only extinction time on a broad class of irregular graphs, with a universal three-way terminal distribution independent of topology and branching magnitudes. It also identifies a sharp characteristic-versus-branching bifurcation in the complete rooted-tree family. The noncommutative up/down factorization explains the mechanism rather than merely tabulating small cases, and the exact law has potential use in finite-field network dynamics and algebraic combinatorics. It does not purport to characterize every earlier shell.

## Closest literature and limits

Rojo's 2005 online paper was examined in its introduction and main adjacency-characteristic polynomial statement (Theorem 4); its spectral quantities are distinct from the finite-field dynamical stopping-time quantities here. The Aledo survey's available abstract and introductory sections supply a broader context, and abstracts of the Rojo–Robbiano and Fritscher–Trevisan studies were compared. No independent proof inspection by another researcher has taken place. The novelty conclusion is subject to limitations from full-text access to some relevant papers.

Self-review: passed. Independent audit: not yet performed.
