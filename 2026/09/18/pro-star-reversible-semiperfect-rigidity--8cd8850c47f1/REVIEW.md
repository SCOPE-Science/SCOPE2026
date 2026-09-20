# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The main deductions were checked directly from the definition of pro-\(*\)-reversibility rather than relying on unverified structural claims.

For a unit \(u\), applying the defining property to \(u u^{-1}=1\) makes \((u^*)^{-1}u\) an invertible projection, hence \(1\), so \(u^*=u\). This also makes the entire unit group abelian because \((uv)^*=v^*u^*\) while \(uv\) itself is a unit and hence fixed.

For an idempotent \(e\), applying the definition to \((1-e)e=0\) gives \(e^*(1-e)\) as a projection. Equating it with its adjoint immediately yields \(e^*=e\). Reversibility follows by applying the defining condition twice to a zero product: if \(ab=0\), then \(b^*a\) is a projection, hence so is \((ba)^*\); but \((ba)^2=0\), forcing \(ba=0\). Standard semicommutativity of reversible rings then makes all idempotents central.

For a local ring, every element is either a unit or has \(1-x\) a unit, so unit rigidity forces the involution to fix every element. An identity anti-automorphism forces commutativity. Conversely a commutative ring with identity involution is plainly pro-\(*\)-reversible.

For a semiperfect ring, a complete orthogonal family of local idempotents exists. The preceding lemmas make those idempotents central and self-adjoint, so the ring is a finite product of star-stable local factors. Applying the local classification to each factor proves the exact semiperfect equivalence. This covers Artinian rings, finite rings, and finite-dimensional algebras.

The domain criterion was checked separately. A domain has only the projections \(0,1\). Pointwise fixation of units is therefore sufficient as well as necessary: a projected product is either zero, where a factor vanishes, or one, where direct finiteness of a domain gives the reversed product equal to one. The example \(k[x]\), \(x^*=-x\), correctly shows that the semiperfect conclusion cannot be extended to arbitrary domains.

The finite counterexample was checked explicitly in \(\mathbb F_4\): with \(\alpha^2+\alpha+1=0\), Frobenius is an involution, \(a=\alpha\), \(b=\alpha^2\) satisfy \(ab=1\), but \(b^*a=\alpha^2\), which is not a projection. Rings of orders two and three are prime fields with only the identity involution, so order four is minimal.

## Originality

**PASS, to the best of our knowledge.** Chen--Wang--Zou's arXiv:2609.20076v1 was inspected directly. It introduces pro-\(*\)-reversibility, proves implications to reversible and \(*\)-reversible rings, develops equivalent projection conditions, and gives a non-pro example answering the converse question. Those results are prior art. Full-text searches of that source found no occurrence of “unit”, “local”, “semiperfect”, or “finite”, and no classification of the classes treated here.

Targeted literature searches used the exact new terminology and semantic equivalents involving projection products, involutions, self-adjoint units, local rings, semiperfect rings, Artinian rings, and division rings. No prior statement of the unit-rigidity theorem, the local/semiperfect equivalence, the domain criterion, or the minimal \(\mathbb F_4\) separation was located.

The standard decomposition of semiperfect rings into local corners was checked against Lam's treatment and is prior work. Earlier literature on \(*\)-reversible rings, including Fakieh--Nauman, concerns the zero-product notion and does not contain the newly introduced pro-\(*\) property. Viswanathan's 2023 feebly-\(*\)-clean paper gives a related implication from self-adjoint units to trivial involution under additional clean-type assumptions and \(2\in U(R)\); it does not give the semiperfect theorem above.

No specific inaccessible source produced concrete evidence of prior coverage. The main residual risk is terminological: older clean-ring or involution literature may contain an equivalent unit-fixing lemma under different hypotheses, and the new definition is recent enough that contemporaneous observations may not yet be indexed. The originality claim is therefore expressly limited to the best of our knowledge.

## Value

**PASS.** The result gives a structural classification for a large and standard class of rings immediately after the introduction of pro-\(*\)-reversibility. On every semiperfect ring the new notion has no genuinely involutive or noncommutative examples at all: it is exactly commutativity with the trivial involution. This simultaneously settles the property for all finite rings, Artinian rings, and finite-dimensional algebras.

The domain theorem shows that this rigidity is not a tautology of the definition: outside the semiperfect regime nontrivial involutions can survive precisely when they leave the unit group fixed. The order-four Frobenius field gives a minimal finite separation between \(*\)-reversibility and pro-\(*\)-reversibility, substantially simplifying and sharpening the source paper's counterexample to the converse question.

## Review status

No independent validation, formal verification, expert attestation, or journal peer review is asserted.
