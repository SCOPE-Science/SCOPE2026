# Reduced finite commutative algebras admit no weight-zero Rota–Baxter operators

## Finding

Let \(A\) be a finite-dimensional commutative reduced algebra over an arbitrary field \(k\). The algebra need not be unital.

Then every weight-zero Rota–Baxter operator
\[
R:A\to A
\]
is zero:
\[
\boxed{\operatorname{RB}_0(A)=\{0\}.}
\]

Consequently, every weight-zero Rota–Baxter operator on a finite-dimensional commutative semisimple algebra is zero.

In particular, if \(G\) is a finite abelian group and
\[
\operatorname{char}k\nmid |G|,
\]
then
\[
\boxed{\operatorname{RB}_0(k[G])=\{0\}.}
\]
Thus every finite cyclic group algebra over a characteristic-zero field has only the zero weight-zero Rota–Baxter operator. This settles, in particular, the prime-cyclic question raised after the classifications for cyclic groups of orders \(2\) and \(3\).

The reduced hypothesis is a genuine boundary. If a commutative algebra contains a nonzero element \(e\) with
\[
e^2=0,
\]
then the map
\[
R(x)=ex
\]
is a nonzero weight-zero Rota–Baxter operator. For example, the dual-number algebra
\[
k[\varepsilon]/(\varepsilon^2)
\]
has the nonzero operator \(R(x)=\varepsilon x\).

## Assumptions and scope

Reduced means that \(A\) has no nonzero nilpotent elements. No hypothesis on the characteristic of \(k\) is needed.

The finite-dimensional hypothesis is used to force a nonzero reduced commutative subalgebra to contain a nonzero idempotent. The theorem does not claim the same conclusion for arbitrary infinite-dimensional reduced algebras.

The group-algebra corollary assumes \(G\) finite abelian and nonmodular characteristic. It follows from Maschke semisimplicity together with commutativity.

## Proof

A weight-zero Rota–Baxter operator satisfies
\[
R(x)R(y)=R\bigl(R(x)y+xR(y)\bigr)
\]
for all \(x,y\in A\).

First observe that
\[
B=\operatorname{Im}R
\]
is a subalgebra: if \(u=R(x)\) and \(v=R(y)\), then
\[
uv=R\bigl(R(x)y+xR(y)\bigr)\in B.
\]
Because \(A\) is reduced, so is \(B\).

Assume for contradiction that \(R\ne0\). Then \(B\ne0\). We claim that \(B\) contains a nonzero idempotent.

If \(B\) is not unital, form its unitization
\[
B^+=k\oplus B.
\]
This algebra is again reduced: if \((\lambda,b)^n=0\), projection to \(k\) gives \(\lambda=0\), and then \(b^n=0\), hence \(b=0\). A finite-dimensional commutative reduced unital algebra is Artinian reduced, hence a finite product of fields. The nonzero ideal \(B\subseteq B^+\) therefore contains a nonzero idempotent. Thus there exist \(x\in A\) and \(0\ne e\in A\) with
\[
e=R(x),\qquad e^2=e.
\]

Apply the Rota–Baxter identity to \((x,x)\). Commutativity gives
\[
e=e^2=R(2ex).
\]
If \(\operatorname{char}k=2\), the right-hand side is \(R(0)=0\), contradicting \(e\ne0\).

Now suppose \(\operatorname{char}k\ne2\). Then
\[
R(ex)=\frac e2.
\]
Put
\[
y=ex.
\]
Since \(e^2=e\), one has \(ey=y\). Applying the Rota–Baxter identity to \((y,y)\) yields
\[
\left(\frac e2\right)^2
=
R\left(2\frac e2y\right)
=
R(ey)
=
R(y)
=
\frac e2.
\]
Hence
\[
\frac e4=\frac e2,
\]
so \(e=0\), again a contradiction. Therefore \(R=0\).

A finite-dimensional commutative semisimple algebra is a finite product of fields and is reduced, proving the first corollary.

Finally, if \(G\) is finite abelian and \(\operatorname{char}k\nmid |G|\), Maschke's theorem makes \(k[G]\) semisimple, while abelianity makes it commutative. Hence the theorem applies.

For the boundary example, if \(e\) is central and \(e^2=0\), define \(R(x)=ex\). Then
\[
R(x)R(y)=e^2xy=0,
\]
while
\[
R\bigl(R(x)y+xR(y)\bigr)
=e(exy+xey)=2e^2xy=0.
\]
Thus \(R\) is a nonzero weight-zero Rota–Baxter operator whenever \(e\ne0\).

## Verification

The included checker exhaustively tests all linear endomorphisms of the split reduced algebras
\[
\mathbf F_2^n\quad(n=1,2,3)
\]
and
\[
\mathbf F_3^n\quad(n=1,2),
\]
with coordinatewise multiplication. In every case, the zero map is the only weight-zero Rota–Baxter operator.

The checker also verifies, over
\[
\mathbf F_2,\quad\mathbf F_3,\quad\mathbf F_5,
\]
that left multiplication by \(\varepsilon\) on the dual numbers
\[
\mathbf F_q[\varepsilon]/(\varepsilon^2)
\]
is a nonzero weight-zero Rota–Baxter operator.

The checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the theorem.

## Relationship to prior work

Gubarev proves that every weight-zero Rota–Baxter operator on a unital associative algebraic algebra over a characteristic-zero field is nilpotent as a linear operator. That result is broad but does not force the operator to vanish: the same paper exhibits nonzero weight-zero operators on matrix and square-zero settings.

The result above adds a different structural obstruction. On a finite-dimensional commutative reduced algebra, the image of a nonzero Rota–Baxter operator would itself be a nonzero reduced finite-dimensional subalgebra and hence contain an idempotent. The Rota–Baxter identity makes such an image idempotent impossible in every characteristic. Thus nilpotence strengthens to exact vanishing on this class, and the proof does not require characteristic zero or a unit.

Guo, Rosenkranz, and Zheng classified the semigroup algebras of orders \(2\) and \(3\). They found only the zero weight-zero operator on the cyclic group algebras of orders \(2\) and \(3\), and asked whether the same holds for every cyclic group of prime order. The group-algebra corollary above answers that question affirmatively over characteristic zero and, more generally, for every finite abelian group in nonmodular characteristic.

Targeted semantic and literature searches under reduced, semisimple commutative, product-of-fields, group-algebra, and weight-zero Rota–Baxter formulations did not locate this exact vanishing theorem.

## Limitations

Finite dimensionality is essential to the idempotent argument as stated. No assertion is made here for arbitrary infinite-dimensional reduced commutative algebras.

The group-algebra corollary is nonmodular. When the characteristic divides the group order, nilpotents can occur and the reduced hypothesis can fail.

The theorem concerns weight zero only. Nonzero-weight Rota–Baxter operators have a different, often projection-like, structure.

Failed searches do not prove novelty.

## References

1. V. Gubarev, “Rota–Baxter operators on unital algebras,” arXiv:1805.00723v1, first public version 2 May 2018; *Moscow Mathematical Journal* 21 (2021), 325–364, DOI 10.17323/1609-4514-2021-21-2-325-364. MSC 16W99, 17C20.
2. L. Guo, M. Rosenkranz, and S. Zheng, “Classification of Rota-Baxter operators on semigroup algebras of order two and three,” arXiv:1402.3702v1; *Communications in Algebra* 47 (2019), 3094–3116, DOI 10.1080/00927872.2018.1552278.
