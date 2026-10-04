# Almost-abelian Lie algebras have rank-only commutativity spectra

## Finding

Let \(L\) be a finite-dimensional nonabelian almost-abelian Lie algebra over
\[
\mathbf F_q.
\]
Thus \(L\) has an abelian ideal \(V\) of codimension \(1\). Write
\[
\dim_{\mathbf F_q}V=n
\]
and choose
\[
t\in L\setminus V.
\]
The bracket is determined by the nonzero linear map
\[
A=\operatorname{ad}_t|_V:V\to V.
\]
Put
\[
r=\operatorname{rank}A.
\]
Then
\[
L^2=A(V),
\qquad
r=\dim_{\mathbf F_q}L^2.
\]

Define the adjoint-rank enumerator
\[
R_L(T)
=
\sum_{x\in L}
T^{\operatorname{rank}(\operatorname{ad}_x)}.
\]
Then
\[
\boxed{
R_L(T)
=
q^{n-r}
+
\bigl(q^n-q^{n-r}\bigr)T
+
(q-1)q^nT^r.
}
\]
When \(r=1\), the two terms involving \(T\) combine. Thus, for \(r=1\), the only adjoint ranks are \(0\) and \(1\); for \(r>1\), the only adjoint ranks are
\[
0,\quad 1,\quad r.
\]

Equivalently, the centralizer distribution is completely determined by \(n\) and \(r\):

- exactly \(q^{n-r}\) elements have centralizer size \(q^{n+1}\);
- exactly \(q^n-q^{n-r}\) elements have centralizer size \(q^n\);
- exactly \((q-1)q^n\) elements have centralizer size \(q^{n+1-r}\).

The element commutativity degree therefore has the dimension-free formula
\[
\boxed{
d(L)
=
\frac{q^r+q^2-1}{q^{r+2}}.
}
\]

For fixed \(q\), this value depends only on
\[
r=\dim L^2,
\]
not on the ambient dimension or on the Jordan or rational canonical form of \(A\).

For every fixed \(n\ge1\), all values
\[
r=1,\ldots,n
\]
occur, for example by taking \(A\) of rank \(r\). Hence the commutativity degrees of \((n+1)\)-dimensional nonabelian almost-abelian Lie algebras are exactly
\[
\boxed{
\left\{
\frac{q^r+q^2-1}{q^{r+2}}
:
1\le r\le n
\right\}.
}
\]
These values strictly decrease as \(r\) increases. Consequently, within the almost-abelian family,
\[
\boxed{
d(L)\text{ determines }\dim L^2.
}
\]

## Assumptions and scope

The element commutativity degree is
\[
d(L)
=
\frac{
|\{(x,y)\in L^2:[x,y]=0\}|
}{
|L|^2
}.
\]

The phrase “almost-abelian” means nonabelian with an abelian ideal of codimension \(1\).

The theorem concerns element commutativity, not the distinct notion of subalgebra commutativity.

No assumption is made on the characteristic, diagonalizability, separability, or nilpotency of the defining endomorphism \(A\).

## Proof

Every element of \(L\) has a unique expression
\[
x=\alpha t+u,
\qquad
\alpha\in\mathbf F_q,\quad u\in V.
\]
For
\[
y=\beta t+v,
\]
using \([V,V]=0\) gives
\[
[x,y]
=
\alpha A(v)-\beta A(u).
\]

First suppose
\[
\alpha\ne0.
\]
As \(v\) varies over \(V\) with \(\beta=0\), the values
\[
[x,v]=\alpha A(v)
\]
fill all of \(A(V)\). Every bracket \([x,y]\) also lies in \(A(V)\). Therefore
\[
\operatorname{Im}(\operatorname{ad}_x)=A(V)
\]
and
\[
\operatorname{rank}(\operatorname{ad}_x)=r.
\]
There are
\[
(q-1)q^n
\]
such elements.

Now suppose
\[
\alpha=0.
\]
Then
\[
[x,y]=-\beta A(u).
\]
If
\[
A(u)=0,
\]
then \(x\) is central and the adjoint rank is \(0\). There are
\[
|\ker A|=q^{n-r}
\]
such elements.

If
\[
A(u)\ne0,
\]
then the image of \(\operatorname{ad}_x\) is the one-dimensional span of \(A(u)\), so the adjoint rank is \(1\). There are
\[
q^n-q^{n-r}
\]
such elements.

This proves the rank enumerator.

For any \(x\in L\),
\[
|C_L(x)|
=
q^{n+1-\operatorname{rank}(\operatorname{ad}_x)}.
\]
Thus the displayed rank counts immediately give the centralizer distribution.

The standard centralizer average gives
\[
d(L)
=
\frac{1}{|L|}
\sum_{x\in L}
\frac{1}{|\operatorname{Im}(\operatorname{ad}_x)|}.
\]
Substituting the three rank strata yields
\[
d(L)
=
\frac{1}{q^{n+1}}
\left(
q^{n-r}
+
\frac{q^n-q^{n-r}}{q}
+
\frac{(q-1)q^n}{q^r}
\right).
\]
Simplifying,
\[
d(L)
=
\frac{1}{q^2}
+
\frac{q^2-1}{q^{r+2}}
=
\frac{q^r+q^2-1}{q^{r+2}}.
\]

For fixed \(q\), the term
\[
\frac{q^2-1}{q^{r+2}}
\]
strictly decreases with \(r\), so the commutativity degree determines \(r\).

Finally, every \(r\) with
\[
1\le r\le n
\]
is realized by a nonzero linear map \(A:V\to V\) of rank \(r\), for example a diagonal projection of rank \(r\). This proves the exact finite spectrum for fixed dimension.

## Verification

The included replay constructs almost-abelian Lie algebras directly from finite-field matrices \(A\), enumerates every element, builds every adjoint matrix, and computes its rank by finite-field Gaussian elimination.

It verifies examples over
\[
\mathbf F_2,\quad
\mathbf F_3,\quad
\mathbf F_4,\quad
\mathbf F_5,
\]
including nilpotent, semisimple, and nonsemisimple defining maps, and ranks
\[
r=1,\quad2,\quad3.
\]

For each example, the replay independently checks:

- the exact adjoint-rank histogram;
- the exact number of commuting ordered pairs;
- the closed formula
  \[
  d(L)=\frac{q^r+q^2-1}{q^{r+2}}.
  \]

The replay returns `VERIFY_OK`.

Finite enumeration is not used to prove the theorem.

## Relationship to prior work

Shamsaki, Erfanian, and Parvizi introduced the element commutativity degree for finite-dimensional Lie algebras over finite fields and expressed it through adjoint-image sizes. Their paper computes the invariant for Heisenberg algebras and for the unique nonabelian two-dimensional Lie algebra, proves invariance under isoclinism, and derives general bounds. It does not state an almost-abelian classification in the inspected full text.

The rank-one case of the theorem explains why the three-dimensional Heisenberg algebra and the two-dimensional affine Lie algebra have the same commutativity degree: both are almost-abelian with
\[
\dim L^2=1.
\]
The theorem extends this mechanism to arbitrary dimension and arbitrary derived rank.

Avetisyan gives a systematic structural treatment of almost-abelian Lie algebras over arbitrary fields, identifying them with codimension-one abelian extensions controlled by one linear operator. That structural classification does not study finite-field commuting probabilities.

A later paper on possible commutativity-degree values classifies several low-dimensional or low-derived-rank situations. In particular, its central-quotient-dimension-three result contains the three-dimensional full-rank almost-abelian case, but its inspected text contains no almost-abelian or codimension-one-abelian-ideal theorem and does not imply the arbitrary-rank formula above.

Searches using “almost abelian,” “codimension one abelian ideal,” “commutativity degree,” “commuting probability,” “derived rank,” and the displayed closed formula did not locate an equivalent result.

## Limitations

The theorem applies only to Lie algebras having an abelian ideal of codimension \(1\).

The commutativity degree recovers only
\[
\dim L^2
\]
inside this family. It generally does not recover the similarity class of the defining operator \(A\), and therefore does not classify almost-abelian Lie algebras up to isomorphism.

The rank enumerator is stronger than the scalar commutativity degree but still forgets the detailed rational canonical structure of \(A\).

Failed searches do not prove novelty.

## References

1. A. Shamsaki, A. Erfanian, and M. Parvizi, “On the commutativity degree of a finite-dimensional Lie algebra,” arXiv:2406.10064v1, first public version 14 June 2024. The later journal version lists MSC 17B66, 17B05, 17B30.
2. Z. Avetisyan, “The structure of almost Abelian Lie algebras,” arXiv:1610.05365v1, first public version 17 October 2016; *International Journal of Mathematics* 33 (2022), article 2250057.
3. A. Shamsaki, “Characterizing Lie Algebra Structure via the Commutativity Degree,” *Journal of Mathematics* (2026), article 9921706.
