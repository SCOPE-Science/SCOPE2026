# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The construction was checked at the level of the finite-index subgroup $\Lambda\le K_0$ rather than by analogy with parity alone. Euler classes are additive on degreewise split conflations, so $\mathcal A_\Lambda$ is extension closed and weakly idempotent complete. Shifts preserve membership up to sign and contractible complexes have zero Euler class, which gives the Frobenius structure. The exponent $e$ of $G=K_0/\Lambda$ guarantees that $e$ copies of every cohomological summand lie in $\mathcal A_\Lambda$; this is exactly what is needed in the object-ideal factorizations and in the special ideal approximation cone sequences.

The extension bifunctor reduces to the usual cohomological formula because the underlying module category is semisimple and an extension of two objects with Euler classes in $\Lambda$ again has Euler class in $\Lambda$. The reverse Ext-orthogonality was checked using stalk complexes on $e$ copies of a simple module, which always have Euler class in $\Lambda$ and detect any nonzero cohomology map.

The object-level criterion follows from the long exact cohomology sequence: a special $\mathcal F_\Lambda$-precover forces the middle term to have exactly the nonpositive cohomology of the target, hence forces the corresponding truncated Euler class to vanish in $G$; the one-copy cone gives the converse. The dual statement is identical. Direct sums multiply the defect class, so the stabilization index is exactly its group-theoretic order. The explicit complex $L\oplus L[-3]$ realizes every class in $G$.

Potential edge cases were checked: a proper finite-index subgroup omits at least one simple basis class of $K_0$, the quotient exponent is finite and at least two, characteristic of the field plays no role, and nonsplit semisimple $k$-algebras are allowed because the argument only uses semisimplicity and the simple-module basis of $K_0$.

## Originality

**PASS, to the best of our knowledge.** Ren--Wang arXiv:2609.18681v1 was inspected in full around its construction, factorization, completeness, parity obstruction, and idempotent-completion arguments. It treats the even-total-cohomology case, equivalently the single quotient $\mathbb Z/2\mathbb Z$, and uses doubles throughout. Its current text does not formulate the construction through $K_0$, finite-index subgroups, general congruence quotients, or finite abelian obstruction groups.

Targeted searches for cotorsion pairs combined with Euler-class congruences, finite-index subgroups of $K_0$, Grothendieck-group obstructions, and finite abelian obstruction groups did not locate the theorem stated here. The earlier Wang--Wang--Zhu counterexample uses an additive integer-valued function with an inequality condition and is explicitly not weakly idempotent complete; it does not supply this finite-quotient Frobenius family. The Frobenius ideal-approximation results of Sun--Tan--Wang--Zhu provide general background and positive criteria but not this construction.

The main residual originality risk is conceptual simplicity: once the recent parity proof is recast in Grothendieck-group language, replacing doubling by the exponent of a finite quotient is natural. An older exact-category or ideal-approximation source could contain an equivalent finite-index-subgroup observation under different terminology, and a concurrent or later revision of the recent parity preprint may independently make the same abstraction. The originality claim is therefore limited to the best of our knowledge and does not claim priority over inaccessible or unindexed equivalent formulations.

## Value

**PASS.** This is more than a modulus parameter change. It identifies the structural invariant behind the parity example and shows that the obstruction can be an arbitrary finite abelian group. It also gives an object-by-object complete criterion and a quantitative invariant: the exact number of direct-sum copies required to repair a failed special object approximation is the order of the defect element. Thus the construction distinguishes ideal completeness from object completeness with a full finite-group spectrum rather than a binary parity obstruction.

## Limitations

The result is an abstract structural extension of a very recent construction, not a new solution of the original completeness question, which the source already answered negatively under the same broad categorical hypotheses. No exhaustive bibliographic search can rule out an equivalent finite-$K_0$ formulation hidden in older exact-category literature. No independent, formal, or peer-reviewed validation is claimed.
