# Four all-smooth anticanonical pencils on the cyclic quartic quintic del Pezzo surface over \(\mathbf F_2\)

## Finding

Let \(\alpha\in\mathbf F_{16}\) satisfy \(\alpha^4+\alpha+1=0\), and let \(S\) be the blow-up of \(\mathbf P^2_{\mathbf F_2}\) at the degree-four closed point with geometric orbit
\[
B=\{(1:\alpha^{2^i}:\alpha^{2^{i+1}}):0\le i<4\}.
\]
This is the degree-five del Pezzo surface of cyclic quartic Frobenius type. In its six-dimensional anticanonical section space, exactly **18** of the 63 nonzero sections define geometrically smooth genus-one curves. Exactly **four** two-dimensional binary subspaces have all three nonzero members geometrically smooth. These four *all-smooth anticanonical pencils* constitute a single free orbit under \(\operatorname{Aut}_{\mathbf F_2}(S)\cong C_4\). For **every** such pencil, its scheme-theoretic base locus is geometrically reduced and consists of one closed point of degree **five**; in particular it has no rational base points. Each pencil has member rational-point-count multiset \((1,1,5)\).

## Assumptions and scope

All schemes and rational points are over \(\mathbf F_2\), and geometric smoothness is over its algebraic closure. A pencil is an unordered two-dimensional \(\mathbf F_2\)-subspace of \(H^0(S,-K_S)\), not a chosen ordered basis. A smooth member means a geometrically smooth, connected genus-one anticanonical divisor. We count actual pencils, rather than only isomorphism classes.

The four points in \(B\) are in general position: a direct determinant check over \(\mathbf F_{16}\) shows no three collinear. Their blow-up is a smooth degree-five del Pezzo surface. Its anticanonical sections are ternary cubic forms vanishing at all four geometric points, a six-dimensional \(\mathbf F_2\)-space. Because the four base points form one Frobenius orbit, the condition is equivalent to one evaluation equation at \((1:\alpha:\alpha^2)\).

In the coefficient-mask tables the monomials from least to most significant bit are
\[
X^3,\ X^2Y,\ X^2Z,\ XY^2,\ XYZ,\ XZ^2,\ Y^3,\ Y^2Z,\ YZ^2,\ Z^3.
\]
The four pencils, specified by their three nonzero section masks, are:

| Pencil | Nonzero masks |
| --- | --- |
| 1 | `0x185`, `0x2e4`, `0x361` |
| 2 | `0x189`, `0x2e4`, `0x36d` |
| 3 | `0x1a6`, `0x2c7`, `0x361` |
| 4 | `0x1aa`, `0x2c7`, `0x36d` |

## Proof

**The geometric smoothness reduction.** Every nonzero cubic through \(B\) has multiplicity one at each point of \(B\). If a reduced cubic were singular at one of these four points, Frobenius invariance would make all four singular. This is impossible: an irreducible plane cubic has at most one geometric singular point by the genus formula, and a reduced reducible cubic has at most three geometric singular points, by Bézout applied to its line/conic or three-line components. A nonreduced plane cubic contains a repeated line, necessarily Frobenius-invariant and hence defined over \(\mathbf F_2\); no line contains the four points of \(B\). Thus each cubic defines its anticanonical divisor by strict transform, with no exceptional components, and geometric smoothness of this divisor is equivalent to geometric smoothness of the cubic. The genus is one by adjunction, since \(K_S^2=5\).

**An exhaustive criterion for binary cubic smoothness.** A geometrically singular reduced cubic has at most three geometric singular points, as above. Frobenius acts on that finite set, so at least one singular point has residue degree at most three. A nonreduced cubic contains an \(\mathbf F_2\)-rational repeated line and has an \(\mathbf F_2\)-rational singular point. Hence testing the cubic and its three homogeneous partial derivatives at every point of \(\mathbf P^2(\mathbf F_2)\), \(\mathbf P^2(\mathbf F_4)\), and \(\mathbf P^2(\mathbf F_8)\) is **equivalent** to geometric smoothness, not merely a finite heuristic. Independently, affine-chart Gröbner bases test whether the polynomial and first partials generate the unit ideal over the algebraic closure.

**Exact finite census.** The evaluation equation yields 63 nonzero cubics. Both independent algorithms identify precisely 18 geometrically smooth ones, whose rational-point count distribution is: five with one point, four with two, four with four, and five with five. A binary pencil with generators \(F,G\) is all-smooth precisely when \(F,G,F+G\) are among these 18. Exhausting all pairs gives exactly the four pencils displayed above, each with rational-point-count profile \((1,1,5)\).

**Automorphisms.** Exhausting the 168 elements of \(\operatorname{PGL}_3(\mathbf F_2)\) gives exactly four that preserve \(B\). In row-bitmask notation their matrices are \((1,2,4)\), \((1,3,5)\), \((1,4,3)\), and \((1,5,2)\); they form \(C_4\). Boitrel's classification establishes that these lifts are the entire automorphism group of this cyclic quartic degree-five del Pezzo surface, not merely a subgroup. Explicit polynomial substitution sends pencil 2 through all four pencils, so the action is transitive with trivial stabilizers.

**The base scheme.** Take pencil 2 and its generators
\[
F=X^3+XY^2+Y^2Z+YZ^2,\qquad
G=X^2Z+XZ^2+Y^3+Y^2Z+Z^3.
\]
Over \(\mathbf F_2\), with \(X=1\) and lexicographic order \(Z>Y\), the ideal \((F,G)\) has Gröbner basis
\[
Z+Y^8+Y^7+Y^6+Y^5,\quad
Y^9+Y^5+Y^4+Y^3+Y^2+Y+1.
\]
The eliminant factors exactly as
\[
(Y^4+Y+1)(Y^5+Y^2+1),
\]
with both factors irreducible and distinct over \(\mathbf F_2\). The companion linear equation in \(Z\) and the absence of common points on \(X=0\) show that the nine plane base points are geometrically distinct. Four constitute the already-blown-up degree-four orbit \(B\), and five form one closed point of degree five. Transversality and the blow-up therefore leave precisely this reduced quintic orbit as the scheme-theoretic base locus on \(S\). Automorphism transitivity propagates this conclusion to all four pencils.

## Verification

The standalone program `verify_enumeration.py` uses exact \(\mathbf F_{16}\) arithmetic, exhaustive binary cubics and matrices, algebraic Gröbner smoothness tests in all three projective affine charts, exact orbit computation, and the base-scheme elimination. Its reference output is `enumeration_output.json`. The independent pure-Python program `verify_independent.py` enumerates geometric singular points over fields of orders two, four, and eight and checks the binary cubic smoothness lemma. It separately reconstructs the 18 smooth members, four pencils, rational-point counts, and irreducible degree-four and degree-five factors; its reference output is `independent_output.json`. Run both with Python 3; the first requires SymPy, and the second uses only the standard library. Their outputs were compared with their included reference JSON files. The independent point-test method checks a mathematically complete extension range, not sampled extensions.

## Relationship to prior work

Boitrel classifies degree-five del Pezzo surfaces over perfect fields, including the quartic cyclic type, and identifies its full rational automorphism group; the cited classification does not specify this anticanonical pencil census. Blache and collaborators study anticanonical codes on del Pezzo surfaces and record finite-field Galois types; their examined rank-one code construction does not give these four smooth pencils on the rank-two cyclic quartic surface over \(\mathbf F_2\). Asgarli and Ghioca study smooth-member pencils of projective hypersurfaces over finite fields, motivating the all-smooth question, but do not state this fixed-surface classification. The novelty asserted is the exact census, free automorphism action, and Frobenius-transitive reduced base locus on this specific surface, not the existence or classification of degree-five del Pezzo surfaces themselves.

## Limitations

The claim concerns this one \(\mathbf F_2\)-isomorphism class of degree-five del Pezzo surface and rational two-dimensional anticanonical subspaces; it does not classify all del Pezzo surfaces, all finite fields, or higher-dimensional linear systems. The computations exhaust this finite parameter space but do not establish worldwide publication priority. Earlier unindexed computations or implicit stronger results may exist. No independent human audit has been performed.

## References

1. A. Boitrel, *Del Pezzo surfaces of degree 5 over perfect fields*, arXiv:2304.05328, first publicly posted 2023-04-11. Theorem 1.1, case 3(f), and relevant proof. https://arxiv.org/abs/2304.05328
2. R. Blache, A. Couvreur, E. Hallouin, D. Madore, J. Nardi, M. Rambaud, H. Randriam, *Anticanonical codes from del Pezzo surfaces with Picard rank one*, arXiv:1903.09397, first publicly posted 2019-03-22. https://arxiv.org/abs/1903.09397
3. S. Asgarli and D. Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169, first publicly posted 2022-03-14. https://arxiv.org/abs/2203.07169
