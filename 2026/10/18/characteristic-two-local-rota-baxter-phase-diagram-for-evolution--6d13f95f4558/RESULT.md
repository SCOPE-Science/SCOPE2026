# Characteristic-two local Rota–Baxter phase diagram for evolution algebras

## Finding

For a finite-dimensional evolution algebra \(E\) over a field \(K\) of characteristic \(2\), let \(\operatorname{RB}_0(E)\) be the set of linear weight-zero Rota–Baxter operators and \(\operatorname{LRB}_0(E)\) the set of **linear local** weight-zero Rota–Baxter operators, with the pointwise local notion defined below. The following statements form a characteristic-two rigidity and separation theorem.

**Independent-square rigidity.** If the nonzero squares of the elements of a natural basis of \(E\) are linearly independent, then
\[
\operatorname{RB}_0(E)=\operatorname{LRB}_0(E)
=\operatorname{Hom}_K(E,\operatorname{Ann}(E)).
\]
In particular, if \(K=\mathbb F_q\), \(q=2^m\), \(n=\dim E\), and \(a=\dim\operatorname{Ann}(E)\), each class contains exactly \(q^{na}\) operators. This includes all evolution algebras with \(\dim E^2=n-1\) and a one-dimensional annihilator, such as the nilpotent chain \(e_i^2=e_{i+1}\) for \(i<n\), \(e_n^2=0\): here there are exactly \(q^n\) operators of either kind.

**Complete two-dimensional phase diagram.** Let \(E\) be **any** two-dimensional evolution algebra over \(\mathbb F_q\), \(q=2^m\). The following mutually exclusive structural cases classify both operator sets by cardinality. In the last two cases, choose a nonzero generator \(v\) of the one-dimensional square \(E^2=\mathbb F_qv\); the condition \(v^2=0\) is independent of the choice of generator.

| Square structure | \(|\operatorname{RB}_0(E)|\) | \(|\operatorname{LRB}_0(E)|\) |
|---|---:|---:|
| \(E^2=0\) | \(q^4\) | \(q^4\) |
| \(\dim E^2=1\), precisely one natural-basis square vanishes | \(q^2\) | \(q^2\) |
| \(\dim E^2=2\) | \(1\) | \(1\) |
| \(\dim E^2=1\), both natural-basis squares nonzero, \(v^2=0\) | \(q\) | \(q\) |
| \(\dim E^2=1\), both natural-basis squares nonzero, \(v^2\ne0\) | \(2q-1\) | \(q^2\) |

Consequently, strict inclusion \(\operatorname{RB}_0(E)\subsetneq\operatorname{LRB}_0(E)\) holds **if and only if** the final case occurs; its exact cardinality gap is \((q-1)^2\). More explicitly, in that case \(\operatorname{LRB}_0(E)=\operatorname{Hom}_{\mathbb F_q}(E,N)\), where \(N=\{x\in E:x^2=0\}\) is a one-dimensional subspace, and the ordinary operators form the union of two distinct one-dimensional linear subspaces of this two-dimensional Hom space.

**Census of labeled algebra structures.** Fix an ordered basis of \(\mathbb F_q^2\), and allow every ordered pair of vectors as its two natural-basis squares. The respective numbers of labeled multiplication tables in the five cases above are
\[
1,\quad 2(q^2-1),\quad q(q-1)^2(q+1),\quad (q-1)^2,\quad q(q-1)^2.
\]
These sum to \(q^4\). Exactly \(q(q-1)^2\) labeled two-dimensional evolution multiplications have a strict local-to-global gap; the corresponding proportion is \((q-1)^2/q^3\). These are **labeled tables**, not isomorphism classes.

## Assumptions and scope

An evolution algebra here is a commutative, not necessarily associative, algebra admitting a natural basis \(e_1,\ldots,e_n\) with \(e_ie_j=0\) when \(i\ne j\). All operators and local witnesses are \(K\)-linear. An ordinary weight-zero Rota–Baxter operator is a map \(R:E\to E\) satisfying, for every \(x,y\in E\),
\[
R(x)R(y)=R(R(x)y+xR(y)).\tag{1}
\]
A linear map \(T:E\to E\) is **local** if for each \(x\in E\) an ordinary weight-zero Rota–Baxter operator \(R_x\) exists with \(T(x)=R_x(x)\). The field has characteristic \(2\) throughout. The general rigidity assertion works over arbitrary such fields; the complete two-dimensional counts and census require finite fields \(\mathbb F_{2^m}\), for which the square-root map is bijective. The first and third rows of the table include degenerate and perfect evolution algebras, respectively; nilpotency is **not** assumed in the two-dimensional result.

## Proof

**1. Square-zero outputs and the rigidity theorem.** Setting \(y=x\) in (1) and using commutativity and characteristic \(2\) gives
\[
R(x)^2=R(2R(x)x)=0\qquad(x\in E).\tag{2}
\]
For \(z=\sum_i z_ie_i\), natural-basis orthogonality gives \(z^2=\sum_i z_i^2e_i^2\). If the nonzero \(e_i^2\)'s are linearly independent, this vanishes exactly when \(z_i=0\) at every index with \(e_i^2\ne0\), since a field has no nonzero square-zero scalar. These are precisely the elements of \(\operatorname{Ann}(E)\): indeed, \(ze_j=z_je_j^2\) for every \(j\). Consequently every ordinary \(R\) takes values in \(\operatorname{Ann}(E)\). A linear local \(T\) does too, because \(T(x)=R_x(x)\) satisfies (2). Conversely every linear map with image in \(\operatorname{Ann}(E)\) satisfies (1), since both sides vanish. This proves the first equality and its dimension/count assertions. In particular, \(\dim E^2=n-a\) when the nonzero squares are independent, and \(a=1\) in the indicated maximal-rank chain family.

**2. Rank-zero, rank-two and one-vanishing-square cases.** The first three rows are immediate from Step 1: when both squares vanish the annihilator is all of \(E\); when precisely one square vanishes it has dimension one; when the squares are linearly independent it is zero. Their linear map spaces have dimensions respectively four, two and zero.

**3. The genuinely dependent case.** Suppose both natural-basis squares are nonzero and span a common line. Write
\[
e_1^2=a v,\quad e_2^2=b v,\quad a,b\in\mathbb F_q^\times,\quad v\ne0.\tag{3}
\]
Then multiplication has the rank-one bilinear form
\[
xy=B(x,y)v,\qquad B(x,y)=a x_1y_1+b x_2y_2.\tag{4}
\]
The finite field has unique square roots. Put
\[
u=\sqrt b\,e_1+\sqrt a\,e_2,\qquad N=\mathbb F_qu=\{x:x^2=0\},\qquad \beta(x)=B(u,x).\tag{5}
\]
The form \(B\) is nondegenerate, so \(\beta\ne0\), and \(B(u,u)=2ab=0\). By (2), every ordinary operator has the unique form
\[
R_\ell(x)=\ell(x)u,\qquad\ell\in E^*.\tag{6}
\]
Substitution into (1), using (4), gives
\[
\ell(v)\bigl(\ell(x)\beta(y)+\ell(y)\beta(x)\bigr)=0
\quad\text{for all }x,y\in E.\tag{7}
\]
As \(\beta\) is nonzero, the alternating tensor expression in parentheses vanishes for all pairs precisely when \(\ell\) is a scalar multiple of \(\beta\). Thus
\[
\operatorname{RB}_0(E)=
\{R_\ell:\ell(v)=0\}\ \cup\ \{R_{c\beta}:c\in\mathbb F_q\}.\tag{8}
\]
Both are one-dimensional linear families; they agree precisely when \(\beta(v)=0\). To identify this condition intrinsically, write \(v=v_1e_1+v_2e_2\). The equations imply
\[
\beta(v)=\sqrt{ab}(\sqrt a\,v_1+\sqrt b\,v_2),
\qquad
v^2=(\sqrt a\,v_1+\sqrt b\,v_2)^2v.\tag{9}
\]
The factors \(ab\) and \(v\) are nonzero, proving \(\beta(v)=0\iff v^2=0\).

If \(v^2=0\), (8) is a single line of \(q\) operators. Every local \(T\) takes values in \(N\) by (2). Evaluating at the nonzero vector \(v\), every available ordinary witness vanishes there, so \(T(v)=0\); hence \(T=R_\ell\) with \(\ell(v)=0\), an ordinary operator. Thus the local class also has size \(q\).

If \(v^2\ne0\), the two lines in (8) are distinct and contain \(2q-1\) operators. For every \(x\ne0\), at least one of these two one-dimensional families has a coefficient functional nonzero at \(x\): otherwise \(x\) would lie in the intersection of two distinct one-dimensional kernels in \(E\), which is zero. Varying the scalar in that family therefore realizes **every value in \(N\)** at \(x\). At \(x=0\), every linear map has value zero. It follows that every map \(T\in\operatorname{Hom}(E,N)\) is local, yielding exactly \(q^2\) local operators and the strict gap. This establishes the entire phase diagram.

**4. Counting the algebra structures.** Every pair of vectors \((e_1^2,e_2^2)\in(\mathbb F_q^2)^2\) defines one labeled multiplication, so there are \(q^4\) in total. The rank-zero pair contributes one; the exactly-one-zero pairs number \(2(q^2-1)\); the rank-two pairs are the invertible \(2\times2\) matrices, numbering \((q^2-1)(q^2-q)=q(q-1)^2(q+1)\). For rank one with both squares nonzero, choose their common projective image line (\(q+1\) choices) and the two nonzero coordinates of the square vectors along a fixed generator (\((q-1)^2\) choices). Of those image lines, two are coordinate-axis lines and \(q-1\) are not. On a nonaxis line \(v=(s,1)\), \(s\ne0\), the equation \(v^2=0\) is \(as^2+b=0\) and admits exactly \(q-1\) nonzero choices of \((a,b)\). On an axis line, \(v^2\ne0\) for all nonzero \((a,b)\). Therefore the isotropic case occurs \((q-1)(q-1)=(q-1)^2\) times and the complementary case occurs \(q(q-1)^2\) times. Summing gives the five-row census and the stated density.

## Verification

The accompanying self-contained `verify.py` uses only Python's standard library. It implements genuine finite-field arithmetic over \(\mathbb F_2\), \(\mathbb F_4=\mathbb F_2[z]/(z^2+z+1)\), and \(\mathbb F_8=\mathbb F_2[z]/(z^3+z+1)\). For every one of the \(16\) labeled two-dimensional algebras over \(\mathbb F_2\) and every one of the \(256\) over \(\mathbb F_4\), it directly enumerates every linear endomorphism and tests (1) on all ordered pairs of natural-basis vectors; bilinearity makes these tests exhaustive. It then tests each candidate local operator at **every** input against the entire set of ordinary-witness values. It checks the structural category, both operator cardinalities and each census count. It also checks five representative structural classes over \(\mathbb F_8\). Separately, it exhausts all \(512\) and \(65,536\) linear endomorphisms of binary nilpotent chain algebras in dimensions three and four, respectively, verifying ordinary and local operator equality and the predicted annihilator maps. All tests end with `VERIFY_OK`.

The computations test finite cases only; the all-field rigidity and all-even-prime-power formulas follow from the symbolic proof above.

## Relationship to prior work

Qaralleh, Mukhamedov and Khakimov (arXiv:2606.22623, first public June 21, 2026) study **local** weight-zero Rota–Baxter operators on nilpotent evolution algebras of maximal nilindex over fields of **characteristic zero**. Their Theorem 3.4 gives a family with nonzero diagonal strings and typically strict inclusion of ordinary into local operators. Their preceding arXiv:2601.08669 classifies ordinary operators in the same characteristic-zero nilpotent setting. The present result treats characteristic two, where equation (2) forces all images into the square-zero cone and produces a collapse for independent squares, followed by a complete low-dimensional classification of the precise exceptions. The characteristic-zero results do **not** imply these characteristic-two counts or the square-zero-cone dichotomy.

Ladra and Murodov (arXiv:1906.09098, Theorem 3.3) classify ordinary Rota–Baxter operators for two-dimensional **complex** evolution algebras, not characteristic-two fields and not pointwise-local operators. That earlier classification is credited rather than claimed as new. Existing finite-field ordinary-operator enumerations for associative exterior algebras have different multiplication tensors and do not imply the two-dimensional evolution-algebra phase diagram.

## Limitations

The full two-dimensional phase diagram is stated only for finite characteristic-two fields; no analogous counts are asserted for arbitrary imperfect characteristic-two fields. The general independent-square theorem works over any field of characteristic two, but it does not classify evolution algebras with higher-dimensional dependencies among nonzero natural-basis squares. The arithmetic census is of **labeled multiplication tables**, not algebra isomorphism classes. The pointwise-local definition is algebraic and should not be confused with analytic neighborhood-local operators. An independent mathematical priority or peer review has not been performed.

## References

1. I. Qaralleh, F. Mukhamedov and O. Khakimov, *Local Rota--Baxter operators of weight zero on nilpotent evolution algebras with maximal nilindex*, arXiv:2606.22623v1, first publicly submitted 2026-06-21. https://arxiv.org/abs/2606.22623
2. I. Qaralleh, F. Mukhamedov and O. Khakimov, *Rota--Baxter operators of nilpotent evolution algebras with maximal nilindex*, arXiv:2601.08669, 2026. https://arxiv.org/abs/2601.08669
3. M. Ladra and S. Murodov, *On chains and Rota--Baxter operators of evolution algebras*, arXiv:1906.09098, 2019. https://arxiv.org/abs/1906.09098
