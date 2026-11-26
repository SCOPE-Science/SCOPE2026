# Independent mathematical audit

## correctness

PASS

For λ≠0 the sextic gradient vanishes exactly on its three axis pairs. At each point the coordinate along the axis given by the sum of the other two coordinate squares has nonzero derivative; the equation is v³+x² times a unit in the sense v³+x²ε, and a formal square root of ε gives the stated cusp. Its delta is 1 by the normalization with parameter of orders 2 and 3. The square-coordinate map is a morphism to the smooth Hesse cubic. On its generic point the cover adjoins the square roots of U/W and V/W. Their valuations at the U- and V-axis flexes give independent square classes even over an algebraic closure, proving generic connectedness and geometric integrality of the literal sextic: the finite squaring map has no curve component over an axis point. At each of the three flexes tame Kummer inertia has order 2 (over the algebraic closure local units are squares), giving g=4 by Riemann–Hurwitz, also 10−6 by the cusp calculation. The normalization is smooth over the base: away from the three branch points it is étale over E, and at a rational flex a transverse odd Kummer valuation gives index 2 with the remaining local extension either split or obtained by a square root of a unit with nonzero residue, hence étale. In the intermediate U=s², t=(V+s²+1)/s gives the stated quadratic in s; the transformation is reversible on the function field. Completing the square, with 4=1, gives the smooth separable sextic in t. The involutions fixing the E and F quotient fields are (t,r)→(−t,−r) and (t,r)→(−t,r), whose product is the hyperelliptic involution. They split the genus-two Jacobian into two elliptic factors. In the full Klein-four cover the trivial-character part is E; each nontrivial part comes from one such quotient’s complement to E and is isogenous to F. Permuting the coordinates identifies the three intermediates over k, and the pullbacks and idempotents descend to k. The Hasse tests give λ² and 2λ respectively; the Weierstrass cubic’s only critical root candidate x=−λ gives value −λ², so both elliptic factors are smooth ordinary. Isogeny preserves ordinarity and hence the asserted p-rank, a-number and slopes. Over finite fields the geometric normalization bijection at the unibranch cusps is Frobenius-equivariant, so counts agree over every extension. Independent symbolic substitution modulo 3 and point counts via separate F3 and F9 arithmetic ran as python3 /workspace/branches/independent_reproduction.py sextic. At q=3 the triples (#D,#E,#F) are (0,6,2) and (0,3,3); at q=9 they are (18,12,12) and (30,15,15). They corroborate the stated Weil factors; the arbitrary-field and extension claims follow from the proof, not this finite replay. The uploaded script was inspected, not executed.

## originality

PASS

The distinct claim is the uniform characteristic-three normalization, explicit k-defined elliptic-factor decomposition and resulting arithmetic for this literal singular pencil. The closest antecedents cover a classical smooth-family classification, general abelian-cover isogeny tools, or geometric analogues with different base curves or different defining equations. None of the inspected statements identifies this characteristic-three pencil and its explicit factors. No novelty is assigned to the general character-decomposition method or to the classical family name.

## value

PASS

The computation resolves what geometry and arithmetic survive at a small characteristic excluded from the motivating smooth-family classification. Explicit ordinary elliptic factors over the base field determine all finite-extension counts from genus-one data, not just selected examples; the six-cusp normalization explains why those counts also apply to the original singular sextic. This gives usable information across the whole punctured pencil.

The dated certificate retains the supplied scientific assessment, sources and limitations.
