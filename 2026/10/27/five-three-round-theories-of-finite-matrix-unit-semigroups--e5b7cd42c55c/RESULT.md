# Five three-round theories of finite matrix-unit semigroups

## Finding

**Theorem.** Let \(B_n=\{0\}\cup([n]\times[n])\) be the aperiodic Brandt semigroup of matrix units, for every integer \(n\ge1\). In first-order logic with equality, a distinguished constant \(0\), and the *ternary multiplication relation* \(R(x,y,z)\) meaning \(xy=z\), the exact quantifier-rank-three equivalence criterion is

\[
B_m\equiv_3 B_n\quad\Longleftrightarrow\quad \min\{m,5\}=\min\{n,5\}.
\]

Thus there are exactly five rank-three theories in this family. Every member has a rank-three-equivalent member of size at most \(26\), and the bound is sharp **among members of this family**: the smallest representative of the stabilized class is \(B_5\), with \(5^2+1=26\) elements.

## Assumptions and scope

For \(i,j,k,l\in[n]\), multiplication is

\[
(i,j)(k,l)=\begin{cases}(i,l),&j=k,\\0,&j\ne k,\end{cases}
\]

and every product involving \(0\) is \(0\). The constant \(0\) is explicitly named. The product is a **relation**, not a function symbol: a quantifier-free formula cannot directly name products as terms. Quantifier rank is maximal nesting depth, so conjunctions of separately quantified subformulas do not add ranks. The conclusion is about full first-order rank at most three, with unrestricted Boolean combinations and quantifier alternation, not merely existential formulas.

## Proof

**1. Four strict rank-three thresholds.** Write the following quantifier-free abbreviations:

\[
D(x):=(x\ne0\land R(x,x,0)),\qquad
E(x):=(x\ne0\land R(x,x,x)),
\]

\[
Z(x,y):=R(x,y,0)\land R(y,x,0).
\]

The predicate \(D\) says that \(x=(i,j)\) with \(i\ne j\); \(E\) says that \(x=(i,i)\). For two variables define the rank-one formula

\[
F(x,y):=D(x)\land D(y)\land x\ne y\land Z(x,y)
\land\forall z\bigl(\neg R(x,z,y)\land\neg R(z,x,y)\bigr).
\]

If \(x=(a,b)\) and \(y=(c,d)\), the first four requirements give \(a\ne b\), \(c\ne d\), \(b\ne c\), and \(d\ne a\). A product \(xz=y\) is possible for some \(z\) exactly when \(a=c\); a product \(zx=y\) is possible exactly when \(b=d\). Thus \(F(x,y)\) holds precisely when \(a,b,c,d\) are **four different indices**.

Let

\[
H(x,y,z):=E(z)\land R(x,z,0)\land R(z,x,0)
\land R(y,z,0)\land R(z,y,0).
\]

For \(F(x,y)\), the formula \(H(x,y,z)\) says that \(z=(e,e)\) and its index \(e\) is distinct from the four endpoints of \(x,y\). The four sentences

\[
\begin{aligned}
\phi_2&:=\exists x\,D(x),\\
\phi_3&:=\exists x\exists y\bigl(D(x)\land D(y)\land x\ne y\land Z(x,y)\bigr),\\
\phi_4&:=\exists x\exists y\,F(x,y),\\
\phi_5&:=\exists x\exists y\bigl(F(x,y)\land\exists z\,H(x,y,z)\bigr)
\end{aligned}
\]

all have quantifier rank at most three. Directly from the multiplication table, \(B_n\models\phi_j\) iff \(n\ge j\) for \(j=2,3,4,5\): for \(\phi_3\), in \(B_2\) the two distinct off-diagonal elements are mutual inverses, whereas in \(B_3\), \(x=(1,2)\), \(y=(1,3)\) witness the sentence. For \(\phi_4\) four distinct indices are necessary and sufficient, and \(\phi_5\) similarly requires five. Therefore all five candidate classes are pairwise distinct.

**2. Uniform three-round back-and-forth for all indices at least five.** Play the ordinary three-move Ehrenfeucht--Fraïssé game on \(B_m,B_n\), for \(m,n\ge5\). During each of the first two moves, Duplicator sends \(0\) to \(0\) and nonzero pairs to nonzero pairs while preserving the *equality partition of all coordinate indices used so far*. At most four indices have appeared, so this response is always available in either structure. The resulting chosen elements agree on every equality and multiplication atom involving those elements and \(0\).

For the third move, let \(U\) be the set of previously used coordinate indices, with \(|U|\le4\). If the new chosen pair uses at most one index outside \(U\), its entire equality pattern can again be matched on the other side because at most five indices are needed. The same holds if the new pair uses two new indices but \(|U|\le3\).

The sole remaining case is that \(|U|=4\) and the Spoiler's third element is \((e,f)\) with \(e\ne f\), both indices new. The two previously selected nonzero elements must be \(x=(a,b)\) and \(y=(c,d)\) with \(a,b,c,d\) pairwise distinct. All nine products between the three selected elements are then \(0\), and the three elements are nonzero and distinct. In the responding structure use instead the third element \(z'=(a,d)\), where \(a,d\) now denote the matching index representatives. As the four indices are distinct, \(z'\) is nonzero, differs from \(x,y\), has square \(0\), and every product involving \(z'\) and either \(x\) or \(y\) is \(0\). Hence the three chosen elements in both structures satisfy **exactly the same equality and ternary-multiplication atoms**, including atoms with the named zero. The final position is a partial isomorphism.

This is a winning three-move Duplicator strategy regardless of which structure Spoiler chooses in each round. By the Ehrenfeucht--Fraïssé theorem, all \(B_n\) with \(n\ge5\) satisfy exactly the same sentences of quantifier rank at most three.

Combining the thresholds in Step 1 with stabilization in Step 2 proves the theorem and the sharp representative bound.

## Verification

Run \(\texttt{python code/verify_brandt.py}\) from the directory containing this document using Python 3 (standard library only). The program checks all four threshold formulas on full semigroups through \(n=7\); independently forms complete three-round first-order types by direct enumeration through \(n=6\); and checks the pair-extension atomic-profile saturation on canonical equality-pattern orbits for \(n=5,6,7\). Its expected output is in \(\texttt{verification/verify_output.txt}\). The program uses the relational atomic language, explicitly including the zero constant.

These finite calculations corroborate the proof. They do **not** prove stabilization for all \(n\); the explicit three-move strategy in Step 2 does.

## Relationship to prior work

Gelbaum and Schanuel, *A characterization of the semigroup of matrix units* (1980), Theorem 1, characterize semigroups of matrix units by a unique nonzero middle-factor property. Their result supplies a precise foundational description of this object but does not compare the depth-three theories of different index sizes. Mitchell's 2004 analysis of maximum independent sets of aperiodic Brandt semigroups concerns a different invariant, and Gray--Ruškuc (2007) determine generating ranks of completely \(0\)-simple semigroups. The present invariant is equivalence in a deliberately **relational** first-order language; the classical algebraic characterizations do not imply this threshold without additional model-theoretic analysis.

Exact equivalence searches also used the synonyms *Brandt semigroups*, *aperiodic Brandt semigroups*, *semigroups of matrix units*, and *Rees matrix semigroups with diagonal sandwich matrix*. No stronger directly covering result was located in the examined materials; this is not a claim of exhaustive novelty.

## Limitations

The theorem is restricted to the aperiodic Brandt semigroups over the trivial group, a **named zero**, and ternary relational multiplication. It does not assert the same result when multiplication is a function symbol, when the zero is unnamed, or for Brandt semigroups over arbitrary nontrivial groups. The bound \(26\) is optimal only among members of the displayed family. Not every relevant historical document was available as full text. Independent verification beyond the included reproducible check has not been performed.

## References

1. B. R. Gelbaum and S. Schanuel, *A characterization of the semigroup of matrix units*, J. Austral. Math. Soc. (Series A) 29 (1980), 291--296, doi:10.1017/S1446788700021273. Relevant full text: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/978EC44242CE809907913DE7D75C9BBC/S1446788700021273a.pdf/characterization_of_the_semigroup_of_matrix_units.pdf
2. J. D. Mitchell, *Turán's graph theorem and maximum independent sets in Brandt semigroups*, Proceedings of the Workshop Semigroups and Languages (2004), 151--163, doi:10.1142/9789812702616_0009.
3. R. Gray and N. Ruškuc, *Generating Sets of Completely 0-Simple Semigroups*, Communications in Algebra 33 (2005), 4657--4678; online 1 February 2007, doi:10.1080/00927870500276676.
4. N. D. Gilbert and M. Samman, *Endomorphism seminear-rings of Brandt semigroups*, Communications in Algebra 38 (2010), 4028--4041, doi:10.1080/00927870903286892.
