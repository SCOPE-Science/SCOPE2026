# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The universal unit statements are direct consequences of the defining projection-transfer implications. In a pro-star-reversible ring, applying the definition to \(u u^{-1}=1\) makes \((u^*)^{-1}u\) an invertible projection, hence \(1\), so every unit is self-adjoint. Closure of the unit group then forces its commutativity. In a pro-symmetric ring, applying the definition to \((uv)^{-1}uv=1\) makes \((uv)^{-1}vu\) an invertible projection, hence \(1\), so again the unit group is abelian.

The clean-ring conclusions were checked against the required decomposition. The recent pro-star-reversible paper gives self-adjoint central idempotents; the pro-symmetric paper gives symmetry and hence reversibility, so its idempotents are central. A clean decomposition \(x=e+u\) therefore reduces every commutator to one between units. In the pro-star case both summands are fixed by the involution, making the involution the identity on the whole ring and hence forcing commutativity. Nicholson's classical theorem that idempotent-central exchange rings are clean justifies the exchange extension.

For domains, the proof uses only three elementary facts: the only projections are \(0,1\); domains are directly finite; and a product equal to \(1\) has unit factors. The two converses were checked separately at projection value \(0\) and projection value \(1\). The free-algebra example is valid because a highest-degree argument shows that the only units of \(k\langle x,y\rangle\) are nonzero scalars, while word reversal is a nontrivial involution and the free algebra is a domain.

No computational experiment is needed for the general proof.

## Originality

**PASS, to the best of our knowledge.** Chen–Wang–Zou introduce pro-star-reversibility in arXiv:2609.20076v1 and pro-symmetry in arXiv:2609.20084v1. Their papers establish the basic projection implications, reversibility/symmetry consequences, centrality of idempotents in the relevant settings, and examples separating neighboring classes. Full-text checks found no discussion of units, clean rings, or exchange rings in either preprint.

The closest older literature found concerns unit groups and stronger symmetry notions rather than the two new projection classes. Nicholson's 1973 work analyzes semiperfect rings with abelian unit groups, and Nicholson's exchange-ring theorem supplies the clean reduction for idempotent-central exchange rings. Han–Lee–Lee (2023) prove that for an idempotent-central semiperfect ring, their I-symmetry condition is equivalent to having an abelian unit group and to commutativity. That is important neighboring prior art, but it does not state the present unit consequences of pro-symmetry, does not address pro-star-reversibility, and does not give the clean/exchange plus exact-domain dichotomy established here.

Targeted searches for the new terminology together with “unit group,” “clean,” “exchange,” “domain,” and equivalent formulations did not locate the universal unit-rigidity statements, the exchange-ring classifications, or the exact domain criteria with the free-algebra example. Because the motivating preprints are extremely recent and the deductions are elementary, concurrent discovery is a realistic residual risk.

## Value

**PASS.** The result sharply locates where the two new projection-transfer notions have genuine room to be noncommutative. In the finite-dimensional/Artinian/semiperfect setting, pro-symmetry collapses completely to commutativity, while pro-star-reversibility additionally forces the involution to be trivial. Conversely, the domain theorem shows that the same notions can hold in a highly noncommutative algebra whenever projections and units are sparse. The free associative algebra provides a concrete boundary example, and the unit tests give immediate obstructions for future examples.

## Scope and limitations

No novelty is claimed for the definitions of pro-star-reversible or pro-symmetric rings, their basic implications proved by Chen–Wang–Zou, classical clean/exchange theory, classical results on semiperfect rings with abelian unit groups, or standard facts about free associative algebras. The novelty claim is restricted to the unit-rigidity consequences, the clean/exchange and finite-dimensional classifications, the exact domain criteria, and the resulting boundary example.

The theorem does not classify arbitrary nonclean rings with zero divisors. The literature assessment is not exhaustive, and older equivalent statements may use terminology unrelated to the two new names.
