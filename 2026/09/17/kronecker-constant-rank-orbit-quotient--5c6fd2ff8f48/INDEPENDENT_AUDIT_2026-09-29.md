# Independent audit — 2026-09-29

Record: `2026/09/17/kronecker-constant-rank-orbit-quotient--5c6fd2ff8f48`  
Assigned and audited source tree: `ff51506faba029bc5ccd15b9ea7c1e4520a2eb80`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **passed**

## Correctness

**supported**. The orbit distinction is correct. With the arrow basis fixed, an isomorphism of K_n representations uses only a source change S and sink change Q; after stacking the n arrow images of a source vector, S merely reparametrizes the x-dimensional image subspace H while Q acts by a common invertible right factor (up to transpose convention). Hence fixed-arrow isomorphism classes are right-GL_y orbits, not left-right GL_n×GL_y orbits. Conversely, choosing an isomorphism k^x→H reconstructs the arrow maps, and changing that parametrization only changes the source basis. The explicit K_3 space A(a,b)=[[a,0],[b,a],[0,b]] has minors a^2,ab,b^2, so every nonzero member has rank 2. Swapping its first two rows preserves the constant-rank property but changes the individual arrow-rank tuple from (1,2,1) to (2,1,1), an invariant of fixed-arrow representation isomorphism; this is therefore a valid counterexample to a literal single-isomorphism-class reading.

## Originality

**qualified_correction**. The 2023 Communications in Algebra abstract explicitly states that when x+y=n+1 an elementary module is iff it is of the form X(x,y), while the 2026 preprint states a correspondence with fixed-rank spaces without specifying the orbit relation in its public abstract. Bissinger's 2025 paper already makes the GL(A_r) arrow-space action distinct from ordinary representation isomorphism. The new contribution is therefore the precise right-GL_y quotient and explicit K_3 counterexample/correction, not the existence of the arrow-space action itself. Searches found no public erratum or prior statement of this exact quotient correction.

## Scientific value

**meaningful_classification_correction**. Confusing fixed-quiver isomorphism with an additional arrow-basis quotient changes the moduli problem and can collapse genuinely nonisomorphic elementary modules. The explicit orbit calculation therefore clarifies both a published 2023 classification claim and the interpretation of a very recent 2026 constant-rank correspondence.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/17/kronecker-constant-rank-orbit-quotient--5c6fd2ff8f48
- https://arxiv.org/abs/2609.14238
- https://doi.org/10.1080/00927872.2023.2203243
- https://doi.org/10.1112/jlms.70122
- https://doi.org/10.1080/03081088708817751

## Limitations

- The correspondence still uses Liu's full-rank criterion in the specified fundamental-domain regime rather than reproving the representation-theoretic criterion from first principles.
- Bissinger 2025 already distinguishes the GL(A_r) arrow-space action, so originality is confined to the precise quotient correction and explicit counterexample.
- The full text of Westwick 1987 was not needed for correctness and was not claimed as inspected; it remains a background prior-literature risk for matrix-space equivalence terminology.
- The 2026 preprint is very recent and may later clarify its intended equivalence relation.
