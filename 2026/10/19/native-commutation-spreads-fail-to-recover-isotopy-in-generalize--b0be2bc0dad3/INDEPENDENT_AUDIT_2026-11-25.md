# Independent mathematical audit

## correctness

PASS

For nonzero x and y, a vanishing product forces c=x^(1-q^r)y^(1-q^s), of norm one. For x nonzero, writing y=xt cancels the xy term and leaves t^(q^r)=t^(q^s); the solutions, including t=0, form the fixed field F_(q^g). Zero commutes with all elements. The H-lines partition K minus zero; any commuting set with a nonzero element lies in one line. This gives the maximal additive subspaces, the disjoint cliques, and the count by placing every tuple except the all-zero tuple in a unique line. For n=6 both differences have gcd 2. Albert's theorem applies: both one-sided nuclei have order q for (1,5), and both have order q² for (2,4), after unital normalization; this is the intended comparison at RESULT.md line 21, as made explicit at line 43. As an independent check, write the left multiplication spread as L_x=M_x-M_(c x^(q^r))F^s, with F the q-Frobenius and M scalar multiplication. If A=sum a_j F^j belongs to its left composition idealizer, then for j outside {0,s} the coefficient of F^j in A L_x vanishes identically in x. It is a_j x^(q^j)-a_(j-s)c^(q^(j-s))x^(q^(r+j-s)), with indices modulo 6. The two powers are independent over K, since r!=s. Thus a_i can survive only when i and i+s both belong to {0,s}; as 2s is nonzero modulo 6 for these examples, A=M_a. Matching F^s then gives a^(q^r)=a. The opposite spread yields the right nucleus by the same argument. Under isotopy the left composition idealizer changes by conjugation; for a unital product, applying an idealizer element to L_1 shows it is L_a, and the idealizer identity is exactly left-nucleus associativity. The idealizer calculation is over F_q; the cited nucleus theorem establishes the obstruction to isotopy without requiring an F_q-linear isotopy. Inspected VERIFICATION.md and verify_semifield.py (lines 79–120); did not execute. The degree-six product checks are sampled and do not check nuclei.

## originality

PASS

Albert supplies the binomial family, norm-based admissibility and the isotopy obstruction, not the comparison of the literal commuting relations of these nonunital products. The bounded comparisons found no equivalent native-relation classification and degree-six witness. Credit is confined to the native spread, exact profile and explicit nonreconstruction result; no priority is asserted for the ingredients.

## value

PASS

This is a structural counterexample about a natural observation on a classical family. Even the full labeled relation on the common field cannot recover isotopy, a strictly stronger obstruction than equality of tuple counts or of an abstract graph. The proof isolates why: relative Frobenius controls commutation, while the individual twists control the distinguishing nucleus orders. The arity formula packages the complete profile once that mechanism is known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
