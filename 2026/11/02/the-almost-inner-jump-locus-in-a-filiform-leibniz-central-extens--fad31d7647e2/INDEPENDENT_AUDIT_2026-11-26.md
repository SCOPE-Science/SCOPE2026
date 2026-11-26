# Independent mathematical audit

## correctness

PASS

With θ=0 the multiplication is a Lie bracket: the subspace spanned by e2,...,en is abelian and the bracket with e1 acts by a linear shift. The three modifications take values in the center and vanish when either input is in the span of e3,...,en, so they do not change the nested terms in the right Leibniz identity. This check uses no assumption on characteristic. Every right multiplication is therefore a derivation. Normalize an almost-inner D by subtracting a right multiplication so that D'(e1)=0. Its value on e2 must be t e3+s en, with s=0 if θ3=0, and the iterated brackets with e1 force all the other values. The inner R_(e1+θ1 e_(n−1)) fixes e1 in the sense that its value there is zero, and agrees with the shift on e2,...,e_(n−1). Subtracting t times this map leaves sE. The map E kills the derived subspace and has central image, hence is a derivation. When θ3=0, testing at e2 shows E is not almost inner. When θ3≠0, [x,e_(n−1)]=−x1 en works if x1≠0, and [x,e2]=x2θ3 en works if x1=0; these supply pointwise witnesses for E. For a right multiplication equaling E, testing on e2 would force the right coefficient of e1 to vanish and that of e2 to be θ3^−1, which gives a forbidden e3 component on e1. For a right multiplication equaling zero, test at e2 to kill the coefficient of e1, then at e1 to kill the coefficients of e2,...,e_(n−1), leaving just Ken. Thus Inn has dimension n−1 and E contributes exactly one dimension on the open stratum. In n=4, e3 and en are still distinct and e_(n−1)=e3, so the same tests apply; all divisions are by assumed nonzero field elements. The finite counts follow from the vector-space dimensions.

## originality

PASS

Adashev–Kurbanbaev already give the broader F3 presentation and a normal form; their unconditional extra-summand assertion does not give the correct classification at θ3=0. Even over C, the β=0, (θ1,θ2,θ3)=(1,0,0) member is non-Lie and has [e2,L]=Ce3, which cannot contain E(e2)=en. The new content supported by the matched primary literature and bounded search is the exact criterion for this subfamily, with its arbitrary-field proof, not the upper bound or the extra direction in known cases.

## value

PASS

This resolves a wrong universal membership assertion for a natural three-parameter subfamily and gives the exact boundary for every dimension and characteristic in scope. The distinction between a central derivation and a pointwise almost-inner derivation changes the quotient AID/Inn, so a user of the published normal form needs the corrected condition, not just a single counterexample. The finite cardinalities are useful consequences rather than the justification for the result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
