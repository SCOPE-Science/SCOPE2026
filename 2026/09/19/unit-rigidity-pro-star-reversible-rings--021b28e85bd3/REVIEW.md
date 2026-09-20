# Scientific review

## Correctness: PASS

The main equivalence has a direct two-sided proof.

For necessity, the 2026 source proves that pro-\(*\)-reversibility implies \(*\)-reversibility. Applying the defining projection condition to
\[
u^{-1}u=1
\]
shows that \(u^*u^{-1}\) is a projection. It is also a unit, hence equals \(1\), so every unit satisfies \(u^*=u\).

For sufficiency, let \(p=ab\) be a projection in a \(*\)-reversible ring whose units are all fixed. Reversibility makes \(p\) central and gives \(ba=p\). With \(q=1-p\), the zero product \((qa)(qb)=0\) yields \(qb^*a=0\) by \(*\)-reversibility. In the corner \(pRp\), \(A=pa\) and \(B=pb\) are inverse units. Therefore \(B+q\) is a unit of \(R\), so it is fixed by the involution; hence \(B^*=B\), and
\[
pb^*a=B^*A=BA=p.
\]
Adding the two corner components gives \(b^*a=p\), a projection.

The local, division, and clean corollaries follow from the main criterion together with standard facts. The noncommutative free-algebra example is also consistent: a free associative algebra is a domain, its only units are nonzero scalars, and word reversal fixes those units.

Potential hidden-hypothesis checks were made for the use of centrality, corner units, and the anti-multiplicative involution. No commutativity, characteristic, finiteness, or semiperfectness assumption is used in the main theorem.

## Originality: PASS, qualified to the best of our knowledge

Chen--Wang--Zou, arXiv:2609.20076v1, introduce pro-\(*\)-reversible rings, prove pro-\(*\)-reversible implies \(*\)-reversible, and give a counterexample to the converse. Their full HTML text was inspected. Searches within that text found no occurrence of “unit” or “invertible”, and the paper does not state the pointwise-unit criterion.

Fakieh (2013) is prior art for \(*\)-reversible rings, including reversibility and the fact that idempotents are fixed by the involution. These ingredients are not claimed as new.

Targeted literature searches for “pro-\(*\)-reversible” together with units, fixed/self-adjoint units, and equivalent projection formulations located the 2026 source but no earlier or concurrent statement of
\[
\text{pro-}*\text{-reversible}
\iff
(*\text{-reversible and }u^*=u\text{ for every }u\in U(R)).
\]

Because the notion itself is new and the proof becomes short after the substitution \(u^{-1}u=1\), concurrent discovery or an unindexed equivalent observation remains the main originality risk. The originality claim is therefore limited to the exact unit-fixed characterization and the stated consequences, to the best of our knowledge.

## Value: PASS

The theorem supplies a sharp missing-hypothesis criterion for the failed converse in Question 3.7 of the source paper: the gap between \(*\)-reversible and pro-\(*\)-reversible rings is exactly pointwise fixation of the unit group. It also turns the new projection condition into a familiar structural test and yields complete classifications for local rings, clean rings, and division rings while retaining genuinely noncommutative examples outside the clean setting.

Same-model review: passed. Independent audit: not yet performed.
