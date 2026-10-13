# Scientific review

## Correctness: PASS

The Kaczmarz map is an orthogonal projector for each unit row. The three distinct chronological locations of the third row give the reshuffling Gram matrix \(S=[(u+u^2)P+uQ]/3\), with \(u=c^2\). Applying the independent-draw Gram channel three times gives \(T=[(8+6u+4u^2)P+(1+6u+2u^2)Q]/27\). The exact difference, its determinant, and the initial-vector witness prove the phase diagram for the full continuum \(0\le u<1\). The rational instance and two-row minimum were checked by a standalone exact enumerator; finite checks are not substituted for the proof. Assumptions include unit rows, three updates, consistent planar full-column-rank equations, uniform labeled sampling, and deterministic initial error.

## Originality: PASS with stated residual risk

The closest primary source is Han and Xie, arXiv:2410.01140, Algorithm 1 and Section 3, which supplies RRK's recurrence and bounds but does not derive the fixed-initial-vector Gram comparison or the coherence threshold. Recht and Ré (2012) and Lai–Lim (2020) analyze operator norms of averaged products: scalar norm comparison does not imply their Gram difference is positive semidefinite. De Sa (2020) gives matrix-product/reshuffling reversals at different factor counts and in different metrics; the present full-column-rank Kaczmarz projector family and exact three-row coherence boundary are not corollaries of those examples. The exact iid-Kaczmarz MSE formula is not new: Agaskar–Wang–Lu (2014) derive it for full-column-rank systems and Bai–Wu (2018, Theorem 2.1) explicitly restate its Kronecker transfer law. This is fully compatible with our iid Gram-channel computation; neither theorem compares the shuffled Gram against that channel or gives the sharp sign boundary. Published related results on shuffled SOR and later metric-aware reshuffling were checked for implication, with inaccessible extended manuscript text recorded as a residual risk. No search result can certify global priority, and independent verification remains outstanding.

## Value: PASS

This is a complete sharp threshold for **every initial direction** on the smallest possible planar epoch size, not merely a chosen numerical counterexample. The identity pinpoints how the protocol's advantage can change sign with row coherence while standard three-factor spectral-norm advantages remain intact. It resolves a concrete ambiguity in interpreting shuffled Kaczmarz guarantees: worst-case convergence bounds and operator-norm inequalities do not rank individual initial conditions by their exact expected squared error. The strict counterexample persists with three distinct rows, so it is not only a duplicate-data artifact. The reversal's numerical size is modest, and no multi-epoch acceleration or general-matrix claim is made.

## Closest literature and limitations

D. Han and J. Xie (arXiv:2410.01140); B. Recht and C. Ré (arXiv:1202.4184); Z. Lai and L.-H. Lim (arXiv:2006.01510); C. De Sa (NeurIPS 2020); P. Oswald and W. Zhou (arXiv:1510.04727); Agaskar–Wang–Lu (IEEE GlobalSIP 2014); Bai–Wu (Linear Algebra Appl. 553, 2018, Theorem 2.1); 2026 Evidence Press metric-aware summary. The published norm inequalities are not refuted by the stronger fixed-vector risk statement. The three-row all-angle classification assumes two rows coincide; an exact distinct-row example is supplied, without claiming its full phase diagram. A later release's secondary dynamics manuscript could not be read in full, leaving a limited overlap risk.

Self-review: passed. Independent audit: not yet performed.
