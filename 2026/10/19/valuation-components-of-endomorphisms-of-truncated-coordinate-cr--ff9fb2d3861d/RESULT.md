# Valuation components of endomorphisms of truncated coordinate-cross algebras

## Finding
Fix integers \(r,d\geq2\) and a field \(k\). Define the local Artinian algebra
\[
A_{r,d}(k)=k[x_1,\ldots,x_r]/(x_i x_j\ (i\ne j),\ x_i^{d+1}\ (1\leq i\leq r)).
\]
Let \(E_{r,d}\) be the **reduced augmentation-preserving endomorphism variety**, with coordinates obtained by expressing each \(k\)-algebra endomorphism image of every \(x_i\) in the augmentation ideal. Put \(N=d+1\), \(h=\lfloor N/2\rfloor\), and
\[
c_{r,d}=\begin{cases}rd/2,&d\text{ even},\\r(d-1)/2+1,&d\text{ odd}.\end{cases}
\]
Then \(E_{r,d}\) is a union of **exactly \(c_{r,d}^{\,r}\) geometrically irreducible linear subspaces**, with every component specified explicitly in the proof. In particular, \(E_{r,d}\) is geometrically equidimensional if and only if \(r=2\) or \(d=2\). If \(r,d\geq3\), the components meeting the automorphism locus have strictly smaller dimension than some other components. Only \(r!\) components meet the automorphism locus.

Over \(\mathbb F_q\), define
\[
T_{r,d}(q)=q^{r\lfloor(d+1)/2\rfloor}
+r(q-1)\sum_{a=1}^{\lfloor d/2\rfloor}q^{d+(r-2)a}.
\]
The complete finite-field endomorphism count is
\[
\boxed{\#\operatorname{End}_{\mathbb F_q}(A_{r,d})=T_{r,d}(q)^r.}
\]
This counts unital, base-field-linear algebra endomorphisms; all such endomorphisms preserve the unique maximal ideal. The independent formula for automorphisms, \(r!(q-1)^r q^{r(d+r-2)}\), is an **established antecedent**, used here only to locate its open locus within the component classification.

## Assumptions and scope
All fields and all characteristics are allowed. The variety is the reduced affine variety underlying the augmentation-preserving endomorphism parameter scheme, not a claim that the universal nonreduced scheme has no embedded structure. The algebra's basis is \(1\) together with \(x_j,x_j^2,\ldots,x_j^d\) for \(1\leq j\leq r\). Its maximal ideal \(\mathfrak m\) is the direct sum of the \(r\) branch ideals, and \(\mathfrak m^{d+1}=0\). Consequently, any choice of generator images in \(\mathfrak m\) respecting \(x_i x_j=0\) automatically respects every truncation relation.

## Proof
**Step 1: independent output branches.** Every proposed image is unique in the form
\[
\phi(x_i)=\sum_{j=1}^r f_{ji}(x_j),\qquad
f_{ji}(t)\in t k[t]/(t^{N}).
\]
Because distinct output branches multiply to zero, the conditions \(\phi(x_i)\phi(x_l)=0\), \(i\ne l\), are equivalent to the separate conditions \(f_{ji}f_{jl}=0\) for every output branch \(j\). Therefore the augmentation-preserving endomorphism parameter scheme is a Cartesian product of \(r\) identical annihilating-tuple schemes \(Y_{r,d}\), each formed by \(r\) polynomials in \(t k[t]/(t^N)\) with pairwise zero products. Passing to reduced varieties preserves this finite product over a field (and here the displayed component description independently supplies geometric reducedness of the product).

**Step 2: valuations and components.** Define \(v(0)=N\), and define \(v(f)\) of nonzero \(f\) as the smallest exponent with nonzero coefficient, in \(\{1,\ldots,d\}\). Since a polynomial's initial coefficient cannot cancel in a product, \(fg=0\) in \(k[t]/(t^N)\) exactly when \(v(f)+v(g)\geq N\). Thus a tuple with valuation vector \((a_1,\ldots,a_r)\) is permitted precisely when \(a_i+a_l\geq N\) for all \(i\ne l\).

For each distinguished index \(i\in\{1,\ldots,r\}\) and each \(1\leq a< N/2\), let \(L_{i,a}\) be the coordinate-linear space
\[
 v(f_i)\geq a,\qquad v(f_l)\geq N-a\quad(l\ne i).
\]
If \(N\) is even, add one further linear space \(L_*\) specified by \(v(f_l)\geq N/2\) for every \(l\). Here the valuation inequalities are the linear conditions that the lower coefficients vanish; the convention \(v(0)=N\) includes zero.

These spaces cover \(Y_{r,d}\): choose an entry of minimum valuation. If the minimum is \(<N/2\), all other valuations are at least \(N\) minus it. If the minimum is \(\geq N/2\), then either \(N\) is even and \(L_*\) applies, or \(N\) is odd and a chosen entry can be lowered to \((N-1)/2\) while the others remain at least \((N+1)/2\). Conversely, all displayed spaces satisfy every zero-product constraint. No listed space contains another: their valuation lower-bound vectors are pairwise incomparable under the coordinatewise order. Therefore they are exactly the geometric irreducible components of the reduced variety. For odd \(N=2h+1\), there are \(rh\) such spaces; for even \(N=2h\), there are \(r(h-1)+1\). Their dimensions are respectively
\[
\dim L_{i,a}=N+(r-2)a,\qquad \dim L_*=rh.
\]
Products of the branch components give all components of \(E_{r,d}\), and dimensions add. For \(r=2\), all single-branch dimensions equal \(N\). For \(d=2\), all single-branch components have dimension \(r+1\). When \(r,d\geq3\), there exist components of different dimensions: if \(N\) is even, compare \(L_{i,1}\) with \(L_*\); if \(N\) is odd, compare \(L_{i,1}\) with \(L_{i,2}\). (The latter case has \(N\geq5\).) This proves the equidimensionality criterion.

**Step 3: finite-field count.** For \(N=2h\), the tuples with all valuations at least \(h\) number \(q^{rh}\). Every other tuple has a unique distinguished entry of valuation \(a\) with \(1\leq a\leq h-1\), and all remaining entries have valuation at least \(N-a\). There are \((q-1)q^{d-a}\) ways to choose the distinguished entry and \(q^{a(r-1)}\) ways to choose the others. For \(N=2h+1\), the same disjoint stratification uses the baseline all valuations at least \(h+1\) and exceptional \(1\leq a\leq h\). The baseline always contains \(q^{rh}\) tuples. These disjoint counts give the stated unified expression for \(T_{r,d}(q)\). Independence of the \(r\) output branches gives its \(r\)-th power.

**Step 4: automorphism-bearing components.** Reduction modulo \(\mathfrak m^2\) takes an endomorphism to an \(r\times r\) coefficient matrix. Since \(d\geq2\), the relations between different generators imply that each row has at most one nonzero coefficient. Invertibility therefore requires a monomial matrix, with one nonzero coefficient in each row and column. A valuation-one entry in a given output branch forces all other entries of that output branch to have valuation at least \(d\). Hence such a point belongs to exactly one component \(L_{i,1}\) in each output branch, and the distinguished indices across branches form a permutation. Conversely any point in the corresponding product component with its \(r\) distinguished initial coefficients nonzero is an automorphism by Nakayama's lemma. Exactly \(r!\) components meet the automorphism locus. Each has dimension \(r(d+r-1)\). For \(r,d\geq3\) a larger-dimensional component exists by the preceding dimension comparison. The automorphism group formula itself is already known and is not asserted as a new theorem here.

## Verification
The accompanying self-contained `verify.py` computes literal polynomial products and exhaustively checks annihilating columns for ten prime-field configurations, including \(2\leq r\leq4\) and \(2\leq d\leq4\). In four small configurations it enumerates complete endomorphism assignments, tests invertibility of their actual tangent matrices, and compares the two counts with the formulas. It independently enumerates all admissible valuation vectors and their coordinatewise-minimal elements for \(2\leq r\leq5\), \(2\leq d\leq6\), checking the component enumeration and equidimensionality boundary. The expected terminal output is `VERIFY_OK_CROSS_ENDOMORPHISMS`. Finite tests provide corroboration, not a proof for unbounded parameters or arbitrary fields.

## Relationship to prior work
W. F. Moore's *Cohomology of Fiber Products of Local Rings* (arXiv:0704.3631v1, first posted 26 April 2007) treats fiber-product local rings and their homological invariants, not these endomorphism varieties. R. Díaz, A. Liendo, G. Manzano-Flores, and A. Regeta, *The Automorphism groups of zero-dimensional monomial algebras* (arXiv:2408.02197; first posted 2024), and R. Díaz with G. Lucchini Arteche, *Finite-dimensional monomial algebras are determined by their automorphism group* (arXiv:2409.15081; first posted 2024), provide broad automorphism-group results in characteristic zero, not a classification of noninvertible endomorphism components. An earlier publicly recorded computation titled *Automorphisms of truncated coordinate-cross algebras over arbitrary fields* (4 October 2026) covers the exact present family of algebras and the complete arbitrary-characteristic automorphism group; this is expressly treated as prior coverage. The present claim concerns the **full reduced endomorphism variety**, its geometric components, dimensions and all finite-field endomorphism counts, none of which is implied by knowing only its invertible open subvariety. No claim of absolute bibliographic uniqueness is made.

## Limitations
The result is about augmentation-preserving homomorphisms and the underlying reduced geometric variety; it does not compute nilpotent thickening or embedded components of the universal Hom scheme, or the composition-semigroup Green relations. The proof does not establish the minimum number of observations needed to recover the source algebra from counts. Possible unpublished or differently titled earlier treatments of multibranch annihilating-tuple schemes remain a literature-priority risk. Independent mathematical validation has not been performed.

## References
1. W. F. Moore, *Cohomology of Fiber Products of Local Rings*, arXiv:0704.3631v1 (26 April 2007).
2. R. Díaz, A. Liendo, G. Manzano-Flores, A. Regeta, *The Automorphism groups of zero-dimensional monomial algebras*, arXiv:2408.02197 (first posted 5 August 2024).
3. R. Díaz, G. Lucchini Arteche, *Finite-dimensional monomial algebras are determined by their automorphism group*, arXiv:2409.15081 (first posted 23 September 2024).
4. *Automorphisms of truncated coordinate-cross algebras over arbitrary fields*, publicly recorded mathematical result dated 4 October 2026.
