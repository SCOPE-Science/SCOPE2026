# Self-review

## Correctness — PASS

The map is an actual involution because \(\Delta=xz+yt\) is fixed and \(2=0\). The two quadratic generators are fixed and satisfy the displayed relation. The candidate invariant hypersurface has dimension \(4\) and injects into the polynomial coordinate ring: the polynomial relation is primitive linear in \(U,V\), and the source polynomial ring is integral over the generated invariants. Over its function field, the extension has degree exactly \(2\), with the nontrivial involution as Galois generator. The hypersurface is normal by the singular-plane codimension \(2\) and Serre \(R_1+S_2\), so its integral elements in the invariant field are already inside it. This proves equality of rings without relying on a computer package.

In the quotient, partial derivatives and the exact relation give the Jacobian ideal \((z^2,t^2,D^2)\), leaving a free rank-eight module over the singular plane. The reduced fixed locus in the original affine space is a singular determinant quadric; since a linear involution has a smooth reduced linear fixed locus, polynomial linearization is impossible. The extracted `verify.py` passed all its GF(2) polynomial identities and small-field checks. No finite test is treated as a proof of the invariant-field or normality assertions.

## Originality — PASS with bounded literature risk

The originating source (Miasnikov--Shestakov, arXiv:2610.11013v1, Sections 1--5) explicitly assumes characteristic different from \(2\), uses denominators \(1/2\), and does not give the characteristic-two invariant ring, normal quotient singularities, or non-linearizability. The semantically closest older sources concern the free associative Anick automorphism (Drensky--Yu, arXiv:math/0406207) and a three-variable finite-field permutation calculation (Hakuta, DOI:10.5539/jmr.v9n4p23). Their claims do not imply the explicit four-variable characteristic-two quotient. Searches for the defining equation, order-two action, alias, and invariant-ring relation in mathematical literature and published research records did not identify equivalent or stronger coverage. Similar results on unrelated characteristic-two automorphism schemes and singular hypersurfaces concern different objects. An unindexed computation or an unpublished formulation remains possible; novelty is not inferred simply from unsuccessful searches.

## Mathematical value — PASS

The October 2026 four-variable factorization paper leaves characteristic \(2\) explicitly outside its hypotheses. At this boundary the map changes from the situation treated in the paper to an involution of affine four-space. Determining its complete invariant ring and scheme-theoretic quotient singularities is an intrinsic modular invariant-theory question rather than a chosen auxiliary numerical statistic. The explicit normal singular quotient, rank-eight Jacobian thickening, and polynomial non-linearizability exhibit geometric behavior not accessible from the characteristic-\(\ne2\) factorization and provide a natural concrete test example for wild cyclic group actions. The answer does not resolve the separate polynomial tameness question.

## Sources and residual limitations

Primary full-text inspection: Miasnikov--Shestakov, arXiv:2610.11013v1, Sections 1--5. Relevant comparisons: Drensky--Yu, arXiv:math/0406207 (different free associative setting), and Hakuta (2017), DOI:10.5539/jmr.v9n4p23 (different three-variable action and permutation-sign invariant). Mathematical records were compared by exact objects and conclusions; no assertion of exhaustive worldwide priority is made.

The field is algebraically closed of characteristic \(2\). The result does not assert geometric quotient smoothness, polynomial tameness, a complete wild-action classification, or independent expert verification.

Self-review: passed. Independent audit: not yet performed.
