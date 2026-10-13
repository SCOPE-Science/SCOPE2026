# Eighteen étale two-dimensional self-distributive coalgebra products over every finite field
## Finding
For every finite field \(\mathbb F_q\), including fields of characteristic \(2\), consider two-dimensional counital coalgebras \(C\) for which the dual algebra \(C^*\) is étale of dimension \(2\). Up to counital-coalgebra isomorphism there are exactly two such coalgebras: the split form dual to \(\mathbb F_q\times\mathbb F_q\), and the nonsplit form dual to \(\mathbb F_{q^2}\).

Among both forms together, there are exactly
\[
18
\]
isomorphism classes of bilinear products \(m:C\otimes C\to C\) satisfying comultiplication compatibility
\[
\Delta(uv)=u_{(1)}v_{(1)}\otimes u_{(2)}v_{(2)}
\]
and generalized right self-distributivity
\[
(uv)w=(u w_{(1)})(v w_{(2)}).
\]
Exactly \(9\) of these classes additionally satisfy the multiplicative-counit condition
\[
\varepsilon(uv)=\varepsilon(u)\varepsilon(v).
\]
More precisely, the split form contributes \(13\) classes, of which \(6\) have multiplicative counit, while the nonsplit form contributes \(5\) classes, of which \(3\) have multiplicative counit. These numbers are independent of \(q\).

## Assumptions and scope
A finite-dimensional counital coalgebra is called étale here when its dual algebra is a finite étale algebra. The theorem concerns only the two-dimensional étale slice; it does not classify the non-étale two-dimensional coalgebra forms. Isomorphisms are linear counital-coalgebra isomorphisms that also preserve the product. No restriction on the characteristic of \(\mathbb F_q\) is imposed.

The multiplication convention is the generalized self-distributive one used in the cited literature. The count \(18\) only requires compatibility with comultiplication and the self-distributive identity. The count \(9\) imposes the additional condition that the counit is multiplicative.

## Proof
A two-dimensional finite étale \(\mathbb F_q\)-algebra is isomorphic either to \(\mathbb F_q\times\mathbb F_q\) or to \(\mathbb F_{q^2}\). Dualizing gives exactly two étale counital coalgebra forms.

For the split form choose group-like basis vectors \(g_0,g_1\), so \(\Delta g_i=g_i\otimes g_i\) and \(\varepsilon(g_i)=1\). Compatibility with comultiplication forces each basis product \(g_i g_j\) to lie in \(\{0,g_0,g_1\}\): writing a product as a linear combination, the mixed tensor coefficient must vanish while each surviving coefficient is an idempotent of the field, hence is \(0\) or \(1\). Thus there are only \(3^4\) labeled tables to test. Carter--Crans--Elhamdadi--Saito give exactly \(21\) compatible self-distributive labeled tables, and Bardakov--Kozlovskaya--Talalaev identify their \(13\) orbits under the transposition \(g_0\leftrightarrow g_1\). This transposition is the full nontrivial coalgebra automorphism, so these are exactly the \(13\) split isomorphism classes. The counit is multiplicative precisely when no basis product is zero. Direct orbit enumeration of the \(21\) tables leaves exactly \(6\) such split classes.

For the nonsplit form let \(E=\mathbb F_{q^2}\). Since every finite-field extension is separable, including in characteristic \(2\), scalar extension of the dual coalgebra from \(\mathbb F_q\) to \(E\) splits it into two group-like lines. The nontrivial element \(\sigma\in\operatorname{Gal}(E/\mathbb F_q)\) exchanges those two group-likes. A product descends to \(\mathbb F_q\) exactly when its split multiplication table is fixed by the simultaneous swap of both inputs and the output. Among the same \(21\) labeled tables, exactly \(5\) are swap-fixed, and exactly \(3\) of those have no zero entry.

It remains to check that these descended tables are already isomorphism classes. The coalgebra automorphism group of the nonsplit form is dual to \(\operatorname{Aut}_{\mathbb F_q}(E)=\operatorname{Gal}(E/\mathbb F_q)\cong C_2\). Its nonidentity element is precisely the swap used in descent. Every descended table is fixed by that swap, so no two distinct descended tables are identified. Hence the nonsplit contribution is \(5\), or \(3\) with multiplicative counit. Adding the two nonisomorphic coalgebra forms gives \(13+5=18\) and \(6+3=9\).

## Verification
The supplied `artifacts/verify.py` independently enumerates all \(3^4=81\) possible group-like tables. It checks the self-distributive identity, obtains exactly \(21\) labeled solutions, computes exactly \(13\) swap-orbits and \(6\) nonzero-entry swap-orbits, and then computes exactly \(5\) swap-fixed tables with \(3\) nonzero-entry fixed tables. Its recorded output ends with `CHECK_OK`.

The finite computation verifies the table and orbit counts only. The characteristic-free statement and the passage from tables to isomorphism classes use the symbolic étale-algebra and Galois-descent argument above.

## Relationship to prior work
Carter, Crans, Elhamdadi and Saito classify the two-group-like coalgebra at the labeled-table level: their Lemma 3.8 gives the \(21\) tables and identifies the no-zero condition for counit-compatible shelf morphisms. Bardakov, Kozlovskaya and Talalaev give \(13\) split tables up to basis permutation and a full complex two-dimensional classification; their Section 4 assumes characteristic different from \(2\) for the displayed coalgebra normal forms. Their type-3 formulas therefore do not supply the characteristic-two nonsplit finite-field form.

A recent published comparison result proves that a nonsquare quadratic coalgebra in characteristic different from \(2\) has exactly \(5\) compatible products, \(3\) with multiplicative counit. The present theorem does not merely restate that result: it replaces the square-root normal form by separable quadratic descent, which remains valid in characteristic \(2\), proves the nonsplit isomorphism count using its coalgebra automorphism group, and combines it with the split orbit count to classify the entire two-dimensional étale finite-field slice.

## Limitations
The result does not cover non-étale two-dimensional coalgebras, infinite base fields, or additional rack/quandle invertibility or idempotence axioms. The terminology surrounding whether counit multiplicativity is included in “bialgebra compatibility” differs across sources, so the theorem states the two counts separately. The originality comparison is strongest against the two directly relevant full texts and the recent published nonsquare classification; an older characteristic-two treatment under different descent terminology remains a residual risk.

## References
1. V. G. Bardakov, T. A. Kozlovskaya, D. V. Talalaev, “Self-distributive algebras and bialgebras,” arXiv:2501.19152; Theoretical and Mathematical Physics 224 (2025), 1103–1118, DOI: 10.1134/S0040577925070013.
2. J. S. Carter, A. S. Crans, M. Elhamdadi, M. Saito, “Cohomology of Categorical Self-Distributivity,” Journal of Homotopy and Related Structures 3 (2008), 13–63, arXiv:math/0607417.
