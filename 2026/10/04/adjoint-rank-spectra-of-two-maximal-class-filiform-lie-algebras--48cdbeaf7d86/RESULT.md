# Adjoint-rank spectra of two maximal-class filiform Lie algebras

## Finding

Let \(q\) be a prime power and let \(n\ge6\). On the vector space with basis
\[
e_1,\ldots,e_n,
\]
define two Lie algebras over \(\mathbf F_q\).

The first is
\[
L_n(q):\qquad [e_1,e_i]=e_{i+1}\quad(2\le i\le n-1),
\]
with all other basis brackets zero apart from those forced by alternating bilinearity.

The second is
\[
M_n(q):\qquad [e_1,e_i]=e_{i+1}\quad(2\le i\le n-1),
\]
together with
\[
[e_2,e_j]=e_{j+2}\quad(3\le j\le n-2),
\]
and no further nonzero basis brackets.

Both algebras have nilpotency class \(n-1\). For a finite Lie algebra \(X\), write
\[
R_X(T)=\sum_{x\in X}T^{\operatorname{rank}(\operatorname{ad}_x)}.
\]
Then
\[
\boxed{
R_{L_n(q)}(T)
=q+(q^{n-1}-q)T+(q-1)q^{n-1}T^{n-2}.
}
\]
For the second family,
\[
\boxed{
R_{M_n(q)}(T)
=q+q(q-1)T+(q^{n-2}-q^2)T^2
 +(q-1)q^{n-2}T^{n-3}
 +(q-1)q^{n-1}T^{n-2}.
}
\]

If
\[
d(X)=\frac{\bigl|\{(x,y)\in X^2:[x,y]=0\}\bigr|}{|X|^2}
\]
is the element commutativity degree, these rank spectra give
\[
\boxed{
d(L_n(q))=q^{-2}+(q^2-1)q^{-n}
}
\]
and
\[
\boxed{
d(M_n(q))=q^{-4}+2(q^2-1)q^{-n}.
}
\]
Their difference is
\[
d(L_n(q))-d(M_n(q))
=\frac{(q^2-1)(q^{n-4}-1)}{q^n}>0.
\]
Thus the element commutativity degree distinguishes these two explicit maximal-class families in every dimension \(n\ge6\). For fixed \(q\),
\[
\lim_{n\to\infty}d(L_n(q))=q^{-2},
\qquad
\lim_{n\to\infty}d(M_n(q))=q^{-4}.
\]

## Assumptions and scope

The ground field is the finite field \(\mathbf F_q\), with no restriction on characteristic. The bracket definitions above satisfy the Jacobi identity in every characteristic. The only potentially nontrivial Jacobi relation for \(M_n(q)\) involving both defining bracket families is the triple \((e_1,e_2,e_j)\); its two nonzero terms are opposite copies of \(e_{j+3}\), and therefore cancel, including in characteristic two.

The lower central series of either algebra contains
\[
\langle e_{k+1},\ldots,e_n\rangle
\]
at the \(k\)-th nontrivial step, because repeated bracketing with \(e_1\) advances the index by one. Hence both have nilpotency class \(n-1\).

The originality domain is \(n\ge6\). The five-dimensional standard model appearing as \(L_{5,7}\) in the motivating commutativity-degree paper was already computed there; the present statement uses that low-dimensional computation only as a boundary check rather than as new content.

## Proof

For
\[
x=\sum_{i=1}^{n}a_i e_i,
\]
consider the rank of \(\operatorname{ad}_x\).

For \(L_n(q)\), if \(a_1\ne0\), then
\[
[x,e_i]=a_1e_{i+1}\qquad(2\le i\le n-1),
\]
so the image contains the independent vectors
\[
e_3,\ldots,e_n
\]
and has rank \(n-2\). There are
\[
(q-1)q^{n-1}
\]
such elements.

If \(a_1=0\), every bracket of \(x\) is zero except possibly
\[
[x,e_1]=-
\sum_{i=2}^{n-1}a_i e_{i+1}.
\]
This map has rank one exactly when at least one of
\[
a_2,\ldots,a_{n-1}
\]
is nonzero, giving \(q^{n-1}-q\) elements. The remaining \(q\) elements are precisely the center \(\langle e_n\rangle\) and have rank zero. This proves the formula for \(R_{L_n(q)}(T)\).

Now consider \(M_n(q)\). If \(a_1\ne0\), the vectors
\[
[x,e_i],\qquad 2\le i\le n-1,
\]
have successive leading terms
\[
a_1e_{i+1}.
\]
With respect to the ordered basis \(e_3,\ldots,e_n\), these vectors form a triangular family with nonzero diagonal coefficient \(a_1\). Hence the adjoint rank is \(n-2\), again on exactly
\[
(q-1)q^{n-1}
\]
elements.

Suppose next that \(a_1=0\) and \(a_2\ne0\). The vectors
\[
[x,e_i]=a_2e_{i+2}\qquad(3\le i\le n-2)
\]
span \(\langle e_5,\ldots,e_n\rangle\), a space of dimension \(n-4\). In addition,
\[
[x,e_1]=-
\sum_{i=2}^{n-1}a_i e_{i+1}
\]
has a nonzero \(e_3\)-component, so it contributes one further independent direction. The vector \([x,e_2]\) already lies in \(\langle e_5,\ldots,e_n\rangle\). Thus the rank is \(n-3\). The number of such elements is
\[
(q-1)q^{n-2}.
\]

Finally take \(a_1=a_2=0\). Then only \([x,e_1]\) and \([x,e_2]\) can be nonzero. If at least one of
\[
a_3,\ldots,a_{n-2}
\]
is nonzero, let \(a_k\) be the first nonzero coefficient in that range. The leading terms of \([x,e_1]\) and \([x,e_2]\) occur respectively in the distinct basis directions \(e_{k+1}\) and \(e_{k+2}\), so the two vectors are independent. Hence the adjoint rank is two. There are
\[
q^2(q^{n-4}-1)=q^{n-2}-q^2
\]
such elements.

If
\[
a_3=\cdots=a_{n-2}=0
\]
but \(a_{n-1}\ne0\), then only \([x,e_1]=-a_{n-1}e_n\) is nonzero. The rank is one, and there are \(q(q-1)\) such elements because \(a_n\) is free. The remaining \(q\) elements, with only \(a_n\) possibly nonzero, form the center and have rank zero. This proves the formula for \(R_{M_n(q)}(T)\).

For any \(n\)-dimensional Lie algebra \(X\) over \(\mathbf F_q\), rank-nullity gives
\[
|C_X(x)|=q^{n-\operatorname{rank}(\operatorname{ad}_x)}.
\]
Therefore
\[
d(X)=\frac{1}{q^n}
\sum_{x\in X}q^{-\operatorname{rank}(\operatorname{ad}_x)}.
\]
Substituting the two rank polynomials yields
\[
d(L_n(q))=q^{-2}+(q^2-1)q^{-n}
\]
and
\[
d(M_n(q))=q^{-4}+2(q^2-1)q^{-n}.
\]
The displayed positive difference and the two fixed-field limits follow immediately.

## Verification

The included replay constructs both brackets from their definitions rather than from the closed formulas. It verifies the Jacobi identity on every basis triple and then enumerates every element, constructs its adjoint matrix, and computes the matrix rank by finite-field Gaussian elimination.

The tested instances are
\[
(q,n)=(2,9),\qquad(3,7),\qquad(4,6).
\]
The \(q=4\) run uses \(\mathbf F_4\cong\mathbf F_2[\alpha]/(\alpha^2+\alpha+1)\), so the checks are not restricted to prime fields.

For every tested case and both families, the replay verifies the full predicted rank multiplicity table, the centralizer-sum count of ordered commuting pairs, and the displayed rational formula for \(d(X)\). It also directly enumerates all ordered pairs for the smallest \((q,n)=(2,6)\) case as an independent check of the centralizer-sum identity.

The replay returns `VERIFY_OK`.

Finite enumeration is not used to prove the universal theorem.

## Relationship to prior work

Shamsaki, Erfanian and Parvizi introduced the element commutativity degree for finite-dimensional Lie algebras over finite fields and expressed it through adjoint-image sizes. Their Example 3.8 explicitly computes the five-dimensional algebra \(L_{5,7}\), whose bracket is the five-dimensional instance of the first family above, obtaining
\[
\frac{q^3+q^2-1}{q^5}.
\]
The formula for \(L_n(q)\) specializes to exactly that value at \(n=5\), but the present originality claim begins at \(n=6\) and gives the entire adjoint-rank spectrum rather than only the averaged commutativity degree.

A later paper by the same authors studies structural and asymptotic questions for the invariant. Its exact higher-dimensional calculations concern class-three Lie algebras with derived subalgebra of dimension two. For \(n\ge6\), both algebras here have nilpotency class \(n-1\), while their derived subalgebras have dimension \(n-2\); consequently those class-three results do not imply the formulas above. That later paper also proves existence of families with several prescribed asymptotic commutativity degrees, so no novelty is claimed merely for the existence of the limits \(q^{-2}\) or \(q^{-4}\).

The first family is the standard model filiform algebra, a canonical object in the theory of filiform Lie algebras. The second bracket is the customary \(\mathfrak m_2\)-type maximal-class bracket. Literature on these families addresses automorphisms, derivations, cohomology and deformations; the searches recorded for this result did not locate an all-dimensional element-commutativity or adjoint-rank-spectrum formula for either pair of families.

## Limitations

Only the two explicitly defined maximal-class families are treated. General filiform deformations can have additional brackets and different centralizer strata.

The originality domain is \(n\ge6\); low-dimensional special cases already occur in the recent commutativity-degree literature and are used only for consistency checks.

The result is for finite fields. It does not claim a classification of commuting varieties over infinite fields.

The asymptotic limits are consequences of the exact formulas. The result does not claim that realizing \(q^{-2}\) or \(q^{-4}\) as an asymptotic commutativity degree is itself new.

## References

1. A. Shamsaki, A. Erfanian and M. Parvizi, “On the commutativity degree of a finite-dimensional Lie algebra,” arXiv:2406.10064v1, first public version 14 June 2024; *Quaestiones Mathematicae*, DOI 10.2989/16073606.2026.2630095.
2. A. Shamsaki, A. Erfanian and M. Parvizi, “Characterizing Lie Algebra Structure via the Commutativity Degree,” *Journal of Mathematics* (2026), Article 9921706, DOI 10.1155/jom/9921706.
3. L. Sheng, W. Liu and Y. Liu, “Local Automorphisms and Local Superderivations of Model Filiform Lie Superalgebras,” *Journal of Mathematics* (2024), Article 6650997, DOI 10.1155/2024/6650997.
4. I. Tsartsaflis, “On the Betti numbers of filiform Lie algebras over fields of characteristic two,” arXiv:1511.03132v1. This is used only for the standard \(\mathfrak m_0\) and \(\mathfrak m_2\) bracket notation, not as the cohort-owning source.
