# Same-model review

## Correctness

**PASS.** The necessity of unit fixation is forced by testing the defining condition on \(u\cdot u^{-1}=1\): the resulting projection \((u^*)^{-1}u\) is invertible and therefore equals \(1\). For sufficiency, the argument was checked componentwise with respect to the central projection \(p=ab\). Reversibility gives \(ba=p\) and centrality of \(p\); the elements \(pa+(1-p)\) and \(pb+(1-p)\) are mutual units, hence self-adjoint under the assumed unit condition. This identifies the \(p\)-component of \(b^*a\) with \(p\), while \(*\)-reversibility kills its \((1-p)\)-component. Thus the proof gives the stronger identity \(b^*a=ab\), not merely that \(b^*a\) is a projection.

The clean-ring corollary uses two independent ingredients: Fakieh's Proposition 8 that every idempotent in a unital \(*\)-reversible ring is self-adjoint, and the new theorem's fixation of every unit. A clean decomposition then forces every element to be self-adjoint. The example \(\mathbb F_2[x]\) with \(x^*=x+1\) was checked directly: the involution has order two, the ring is a domain, and its only unit is \(1\).

## Originality

**PASS, to the best of our knowledge.** Chen--Wang--Zou, arXiv:2609.20076v1 (submitted 17 September 2026), introduces pro-\(*\)-reversibility, proves pro-\(*\)-reversible \(\Rightarrow\) \(*\)-reversible, asks whether the converse holds, and gives a counterexample. Its HTML text contains no occurrence of “unit” or “invertible”, and it does not state the unit-group criterion proved here. The displayed counterexample is consistent with the criterion: it contains an inverse unit pair with a unit moved by the involution.

Fakieh (2013) supplies the older theory of \(*\)-reversible rings, including self-adjointness of idempotents, but predates the pro-\(*\)-reversible notion. Han--Nicholson (2001) supplies the standard clean-ring background, including semiperfect \(\Rightarrow\) clean. Searches for pro-\(*\)-reversible rings together with unit/self-adjoint/invertible terminology did not locate an equivalent published characterization.

The main residual risk is terminological rather than a known concrete overlap: because the proof is elementary once the new 2026 definition is available, an equivalent characterization could occur in concurrent work, a later version of the source preprint, or under a differently named projection-reversibility condition. No such source was identified in the inspected literature.

## Value

**PASS.** The theorem replaces a one-way implication plus counterexample by an exact structural classification of the missing condition. It also yields immediate restrictions not stated in the source paper: the unit group is abelian, the involution is trivial on the Jacobson radical, and pro-\(*\)-reversibility collapses to the identity involution throughout clean/semiperfect/Artinian/local rings and division rings. The \(\mathbb F_2[x]\) example shows this collapse is not valid for arbitrary rings.

## Scope and limitations

This record concerns unital rings with involution and the projection-based definition of Chen--Wang--Zou. It does not classify nil-\(*\)-reversible rings, nonunital variants, or extension behavior. Originality is asserted only to the best of our knowledge. No independent validation, formal verification, or peer review is claimed.

**Same-model review: passed. Independent audit: not yet performed.**
