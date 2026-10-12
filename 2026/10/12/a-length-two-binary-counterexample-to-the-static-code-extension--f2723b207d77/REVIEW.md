# Review

## Correctness

PASS. The hypotheses are reconstructed directly. With \(R=M=V=\mathbb F_2\), the defining evaluation map \(\operatorname{Hom}_R(M,V)\otimes_D M\to V\) is the usual multiplication isomorphism, and the same calculation applies to the one-dimensional code \(C\). Thus staticity does not depend on any contested proposition in the source. The map \(f(a,0)=(a,a)\) is linear and injective, but \(\operatorname{wt}(1,0)=1\) while \(\operatorname{wt}(1,1)=2\). Every monomial transformation preserves Hamming weight, so neither conclusion of Corollary 3.1.5 can hold for this embedding. The bundled verifier exhausts the three possible embeddings and the two binary length-two monomial maps.

## Originality

PASS. The target full text was inspected at the definition of static code, Proposition 3.1.2, Corollary 3.1.5, and the later theorem that cites the corollary. Exact-title, corollary-number, counterexample, erratum/corrigendum, and semantic searches found the source and general MacWilliams-extension literature but no published correction or same counterexample. The classical extension theorem has a strictly different premise: it assumes the map is already a Hamming isometry, whereas the source corollary asserts that arbitrary embeddings under staticity become isometries. The closest semantic-search results concern unrelated counterexamples in other coding problems and do not imply this statement.

## Value

PASS. The counterexample targets a universal extension corollary in a recent paper and uses the smallest standard coding alphabet and a length-two coordinate code, so it exposes a structural missing hypothesis rather than an exotic edge case. The same corollary is explicitly invoked in the paper's proof of a later Morita-invariance theorem, making the defect mathematically consequential while still allowing that later theorem might admit another proof.

## Closest literature and limitations

Standard MacWilliams extension theory says that an injective Hamming isometry extends under suitable alphabet hypotheses; it does not say that every injective linear map is an isometry. The present counterexample only refutes the stronger statement actually written in Corollary 3.1.5. No claim is made that the downstream theorem is itself false. An unindexed correction or earlier dissemination remains a residual literature risk.

Self-review: passed. Independent audit: not yet performed.
