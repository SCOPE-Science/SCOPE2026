# Independent mathematical audit

## correctness

PASS

In the displayed model, the diamond operation sends every set to an upset because the only strict comparison is a<b and R[a] is contained in R[b]. The box operation preserves the three sets empty, {b,c}, W, which also form a Heyting subalgebra: in particular the negation of {b,c} is empty. Thus the fragments are persistent at all depths. Direct evaluation gives {b}, {a,b}, and {a,c} for Diamond p, p→Diamond p, and Box(p→Diamond p), respectively; the last is not an upset. At two worlds the discrete case is automatic. In the chain and equivalent-points cases, the complementary upsets Box bottom and Diamond top force uniform successor-row emptiness. The modals then preserve the constant truth sets. On the chain the only other upset is {b}; if any letter denotes it, its two unimodal images are persistent by hypothesis, and otherwise the constant sets suffice for induction. Independently, any modal-headed subformula at depth one has a propositional argument, so both fragment hypotheses and closure under the intuitionistic connectives prove the depth bound.

## originality

PASS

The exact published question concerns one fixed f-model, and the checked version poses it without the answer given here. The closest indexed three-world result separates operators across frames rather than proving any mixed failure inside one model. Neither it nor the checked relation-condensation result establishes this countermodel or its two minima. This is a bounded comparison, not a priority certification.

## value

PASS

The example answers an explicit fixed-model problem and gives exact bounds on two natural complexity measures. It pinpoints why verifying whole single-operator fragments separately is insufficient: a mixed operator can receive an upset never produced by its own fragment. The separation is useful independently of a larger classification of fusion models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
