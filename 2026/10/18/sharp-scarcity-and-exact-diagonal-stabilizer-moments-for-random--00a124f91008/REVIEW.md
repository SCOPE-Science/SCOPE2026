# Review of sharp scarcity and exact diagonal stabilizer moments

## Correctness

**PASS — self-review.** The claim fixes a labelled, uniform \(\mathrm{GL}_n(\mathbb F_q)\) probability space and defines diagonal automorphisms by the literal coefficient equation \(M_{ij}(d_j-d_i^2)=0\). An invertible minor supplies a permutation whose cycles force all coordinates into the odd-order field subgroup. Equal color multiplicities under squaring are both necessary and sufficient for invertible block choices, giving formula (1). The finite support threshold is the smallest order of two modulo an odd prime factor of \(q-1\). All minimal-support symmetries are isolated directed cycles; intersections of distinct cycle events and all larger supports are negligible by explicit counts and a uniform quadratic exponent bound. This proves the sharp probability, conditional group order, and moment asymptotic, without extrapolation from finite computations. `verify.py` exhaustively checks six small ensembles and a separate binary-extension-field example. No checks establish the entire asymptotic by computation alone.

## Originality

**PASS — self-review, subject to bibliographic residual risk.** Elduque–Labra establish that diagonal groups depend on the support graph, and Sriwongsa–Zou establish the odd-order root constraints and the full-cycle extremal case. These results are essential known ingredients, not claimed as new. Wei–Zou give general monomial-group Burnside isomorphism counts (and thus an implicit finite fixed-point framework), but neither its explicit low-dimensional enumerations nor its statement computes the sharp large-dimension probability of **nonidentity diagonal** stabilizers in uniform labelled invertible structure matrices. Rodiño Montoya–Viana Bedoya–Henao consider particular graph-associated evolution algebras rather than the uniform \(\mathrm{GL}_n(\mathbb F_q)\) ensemble. Searches for equivalent probabilistic, directed-cycle, and exact group-moment formulations found no covering statement. Residual risk: the exact first moment may be extractable from general Burnside formulas and equivalent asymptotic estimates may be in unindexed combinatorial literature.

## Value

**PASS.** The derived event is an intrinsic symmetry statistic of a widely studied algebra family, and the theorem gives a field-arithmetic onset dimension, an exact expectation for every dimension, a sharp fixed-field large-dimension rarity constant and exponent, and the asymptotically forced stabilizer order. The numerical asymptotic is a substantive rare-event statement not supplied merely by the root-of-unity graph criterion or by a finite enumeration. It distinguishes fields with \(q-1\) a power of two, for which symmetries are impossible, from other fields, for which they exist but have sharply quantified rarity.

## Closest literature and limitations

The closest sources are Elduque–Labra, arXiv:1902.02191, Section 2; Sriwongsa–Zou, arXiv:2202.01333, Theorem 2.2 and Section 4; Wei–Zou, arXiv:2310.12368, Section 2; and Rodiño Montoya–Viana Bedoya–Henao, arXiv:2505.15604, Sections 1–2. The model is uniform in labelled invertible matrices, not isomorphism classes. Only rational diagonal automorphisms are assessed; permutation symmetries and automorphism group schemes are out of scope. The limit fixes \(q\). An equivalent unnoticed probabilistic formula remains possible; independent auditing would be useful.

Self-review: passed. Independent audit: not yet performed.
