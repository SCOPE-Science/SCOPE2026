# Independent mathematical audit

## correctness

PASS

The frozen formulas are mathematically correct: outside the equal-color flat F the arrow columns give independent pivots; after removing them, only the nonzero weighted incidence rows on S⊆F remain. The incidence kernel consists of constants on spanning components, in all characteristics and with parallel arrows. Exact colorings of F are proper colorings of its contraction, counted by q^c times the matroid characteristic polynomial. For one cycle, independent bridge differences give factors 1+(q²−1)T. On the cycle the q lifts of each admissible difference vector cancel the 1/q character average; the trivial and nontrivial edge-character sums are 1+(q²−1)T and 1−T respectively. Only zero differences with full cycle arrow support need the one-degree correction. I separately enumerated the GF(4) triangle from products and column reduction over GF(2)[x]/(x²+x+1), obtaining (4,36,792,3264), as predicted. The supplied prime-field verifier was inspected, not executed; historical replay is `python verify.py` in the source directory. For the narrowed replacement I rechecked the generator and isomorphism arguments directly. Each pair and arrow contributes the polynomial (d_u−d_v)z′−(d′_u−d′_v)z; one reversal multiplies all generators on that arrow by a unit, so the ideals themselves coincide for every s≥2. The full arrow ideal is the characteristic abelian derived ideal, and the quotient action has three distinct weights on the three one-dimensional arrow lines. Isomorphism must permute the functional weights after one common dual quotient isomorphism, not rescale them independently. Independence of the first two weights leaves one relation, with generators (1,1,1) and (1,1,−1) respectively; no permutation and common rescaling works in odd characteristic. In characteristic two the brackets match. For a forest the independent edge differences allow all sign changes to be absorbed in the quotient, verifying the comparison in the repaired proof. The repaired RESULT.md and VERIFICATION.md give algebraic replay, not a finite test or a formal attestation.

## originality

PASS

This PASS is solely for the repaired triangle witness. The original featured rank claim fails the originality criterion: the earlier 38b9edb44d0d Finding and proof have the same complete simple-graph rank distribution, normalization and pivot lemma, the parallel-edge extension changes neither elimination nor the spanning-component kernel, and the unicyclic expression is an explicit specialization, not a second new invariant. The exact sign-invariance argument is also established background in the catalogue. The repaired files remove those priority claims and state the genuinely distinct obstruction: identical embedded commuting ideals at all arities in a natural pair of Lie-nonisomorphic triangle orientations, certified by the signed dependence. Closest inspected claims use an associative invariant on a forest, a commutator tensor up to independent input/output maps, or outer derivations; none gives the triangle Lie witness. This is a best-of-knowledge assessment, not a historical priority certification.

## value

PASS

For the repaired claim the triangle is the first simple cycle, not an arbitrary test instance. Forest weights are independent and can absorb every arrow sign in a diagonal change of coordinates. Closing the triangle introduces exactly one dependence. Changing its signs prevents Lie isomorphism even though the full polynomial ideals, not just finite-field pair counts or the adjoint spectrum, still coincide at every arity. This gives a concrete reconstruction boundary and separates commuting-equation information from the intrinsic quotient action on the derived ideal. The standard rank and reorientation results are retained as context only, not offered as new value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
