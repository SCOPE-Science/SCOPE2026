# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

For a primary exponent set \(T=\{t_1>\cdots>t_s\}\), the Cartan matrix is the min-matrix
\[
(\min(t_i,t_j))_{i,j}.
\]
Li--Xi, Lemma 2.18, gives the required unimodular integral congruence to
\[
\operatorname{diag}(t_1-t_2,\ldots,t_{s-1}-t_s,t_s).
\]
The primary decomposition makes the full Cartan matrix a block sum of these forms, up to Morita equivalence and permutation.

Chen--Xi, Theorem 4.9 and the definition of \(Sg\)-equivalence, imply that singularly equivalent centralizer matrix algebras have the same multiset \(\mathcal U\) of non-unit gap entries. Thus the two Cartan matrices differ, after integral congruence, only by the number of diagonal \(1\)'s. Stable integral congruence follows, and so does isomorphism of cokernels.

The realization statement is checked directly: choosing cumulative block lengths \(t_i=d_i+\cdots+d_s\) makes the consecutive gap multiset exactly \(\{d_1,\ldots,d_s\}\).

The example \(T=\{4,2\}\) gives diagonal gaps \((2,2)\), while \(T=\{5,1\}\) gives \((4,1)\). Both determinants are \(4\), but the cokernels are respectively \((\mathbb Z/2)^2\) and \(\mathbb Z/4\).

## Originality — PASS, to the best of our knowledge

The underlying Cartan-matrix calculation is classical in this setting, and the integral congruence is explicit in Li--Xi; neither is claimed as new. Chen--Xi (2026) prove preservation of the Cartan determinant under singular equivalence, using the same non-unit gap multiset, but the checked paper does not state preservation of the Cartan cokernel, Smith normal form, or stable integral Cartan form.

Targeted literature checks using the phrases and synonyms "Cartan group", "Cartan cokernel", "Smith normal form", "stable integral Cartan form/congruence", and "centralizer matrix algebra" did not locate an earlier centralizer-specific statement. Mendoza--Sáenz--Marcos establish general Cartan-group results, including derived invariance and realization by standardly stratified algebras, but not the centralizer-specific singular-equivalence statement found here.

Residual risk remains because the new invariant follows by a short synthesis of two explicit known ingredients, so an equivalent observation may exist in the literature under different terminology.

## Value — PASS

The conclusion strictly strengthens a recent singular-equivalence invariant: determinant preservation records only the order of the finite Cartan group, whereas the Cartan group distinguishes examples with equal determinant, such as \((\mathbb Z/2)^2\) versus \(\mathbb Z/4\). The stable integral form gives a direct obstruction to singular equivalence.

The realization theorem also shows that the invariant is not confined to a narrow family of abelian groups: every finite abelian group already occurs among nilpotent one-matrix centralizers over an arbitrary field.

## Evidence checked

- Dubey--Prasad--Singla, arXiv:math/0611897: centralizer Cartan matrices and determinant formula.
- Li--Xi, arXiv:2312.08794, Lemma 2.18: explicit integral congruence to the gap diagonal.
- Chen--Xi, arXiv:2603.20643v2, Theorem 4.9 and Theorem 6.5: classification by \(Sg\)-equivalence and preservation of Cartan determinant; the definition of \(Sg\)-equivalence gives equality of the non-unit gap multiset.
- Mendoza--Sáenz--Marcos, arXiv:1804.01168: Cartan-group terminology, derived invariance, and general realization results.

## Scientific limitations

The singular-invariance theorem is confined to centralizer matrix algebras. The proof depends on the explicit classification of singular equivalences in that class. No claim is made that Cartan groups are preserved by arbitrary singular equivalences of finite-dimensional algebras.
