# Weight-zero Rota–Baxter rigidity for finite-dimensional reduced commutative algebras

## Finding
Let \(A\) be a finite-dimensional commutative reduced algebra over an arbitrary field \(k\), with or without a unit. Every \(k\)-linear weight-zero Rota–Baxter operator \(R:A\to A\) vanishes:
\[
\boxed{\operatorname{RB}_0(A)=\{0\}.}
\]
Consequently, the result applies to finite-dimensional commutative semisimple algebras, and to the group algebra \(k[G]\) for a finite abelian group \(G\) when \(\operatorname{char}(k)\nmid |G|\). The chief scope of this statement beyond earlier direct-sum-of-fields results is its characteristic-free treatment of nonsplit field factors and nonunital reduced algebras. The characteristic-zero split-field case, including prime-cyclic group algebras after scalar extension, was already covered by the earlier zero-operator literature and is **not** claimed as a new resolution of the cyclic-prime question.

## Hypotheses and boundary
Reduced means having no nonzero nilpotent elements. Finite dimensionality, commutativity, and weight zero are essential hypotheses *for the argument given here*; no claim is made for arbitrary infinite-dimensional algebras, noncommutative algebras, or nonzero weights. The algebra need not possess an identity. The nonmodular assumption in the group-algebra corollary ensures semisimplicity by Maschke's theorem; no claim about modular group algebras follows.

The following is a valid sharpness example: **in a unital commutative algebra**, if \(e\ne0\) satisfies \(e^2=0\), then \(R(x)=ex\) is a nonzero weight-zero Rota–Baxter operator, since \(R(1)=e\ne0\). More generally, a central square-zero element gives such an operator whenever \(eA\ne0\). It is false that a nonzero square-zero element alone ensures nonzero left multiplication on a *nonunital* algebra: for an algebra with identically zero multiplication, all such maps are zero. The earlier unqualified nonunital boundary assertion is corrected here.

## Proof
The weight-zero Rota–Baxter identity is
\[
R(x)R(y)=R\bigl(R(x)y+xR(y)\bigr)\qquad(x,y\in A).
\]
It implies \(B=\operatorname{Im}R\) is a subalgebra: products of two image elements again belong to the image. As a subalgebra of a reduced commutative algebra, \(B\) is reduced. Suppose \(R\ne0\), so that \(B\ne0\).

A nonzero finite-dimensional commutative reduced algebra, even one without a unit, contains a nonzero idempotent. Indeed, if \(B\) has no unit, its unitization \(B^+=k\oplus B\) is reduced: if \((\lambda,b)^N=0\), the projection to \(k\) forces \(\lambda=0\), and then \(b^N=0\) forces \(b=0\). The finite-dimensional commutative reduced unital algebra \(B^+\) is Artinian reduced, hence a finite product of fields. Every nonzero ideal in such a product contains a nonzero idempotent. The ideal \(B\) is nonzero; therefore it contains \(e\ne0\) with \(e^2=e\). (If \(B\) is already unital, take its identity.)

Choose \(x\in A\) with \(R(x)=e\). Applying the identity to \((x,x)\) yields
\[
e=e^2=R(2ex).
\]
When \(\operatorname{char}(k)=2\), the right-hand side is \(R(0)=0\), a contradiction. Otherwise \(R(ex)=e/2\). Put \(y=ex\). Since \(e^2=e\), we have \(ey=y\), and applying the identity to \((y,y)\) gives
\[
\frac e4=R\left(2\frac e2y\right)=R(ey)=R(y)=\frac e2.
\]
As 2 is invertible, this forces \(e=0\), again a contradiction. Therefore \(R=0\) for every characteristic.

For the corollary, finite-dimensional commutative semisimple algebras are reduced. If \(G\) is finite abelian and the characteristic of \(k\) does not divide \(|G|\), then \(k[G]\) is semisimple by Maschke and commutative by abelianity. For the boundary, whenever \(e\) is central with \(e^2=0\), multiplication by \(e\) satisfies
\[
R(x)R(y)=e^2xy=0=R(2exy)=R(R(x)y+xR(y)).
\]
It is nonzero if and only if \(eA\ne0\); this is automatic when \(A\) has a unit and \(e\ne0\). In particular, \(k[\varepsilon]/(\varepsilon^2)\) admits the nonzero operator \(R(x)=\varepsilon x\).

## Verification and exact scope
The proof is symbolic and works over every field. The existing `artifacts/verify.py` independently enumerates linear maps on split reduced algebras \(\mathbf F_2^n\), \(n=1,2,3\), and \(\mathbf F_3^n\), \(n=1,2\), and checks that the only weight-zero operator is zero. It also checks multiplication by \(\varepsilon\) on dual numbers over \(\mathbf F_2,\mathbf F_3,\mathbf F_5\). These finite checks corroborate but cannot replace the unrestricted image-idempotent proof. The corrected boundary is additionally witnessed by any nonzero zero-multiplication nonunital algebra, in which every left-multiplication map is zero.

## Relationship to prior work and originality limit
Gubarev's *Rota–Baxter operators on a sum of fields* (arXiv:1811.08219, 2018), Introduction §1, explicitly states that weight-zero Rota–Baxter operators on finite direct sums \(F^n\) are all trivial, citing Gubarev's earlier *Rota–Baxter operators on unital algebras* (arXiv:1805.00723). In characteristic zero, after scalar extension to an algebraic closure, a finite-dimensional commutative semisimple algebra splits, so this prior vanishing statement already entails the zero conclusion on all such algebras and, specifically, the nonmodular cyclic-prime group-algebra corollary. The present finding **does not claim those implications as new**.

The claim isolated for originality here is the elementary characteristic-independent and nonunital reduced-algebra rigidity mechanism, including arbitrary nonsplit finite field extensions and their products. Gubarev's characteristic-zero nilpotence theorem is also a relevant earlier general restriction, though mere nilpotence of \(R\) is weaker than its vanishing without the additional image-idempotent argument. Guo, Rosenkranz, and Zheng (arXiv:1402.3702) classified low-order semigroup algebras and posed a prime-cyclic question, now known to have a positive characteristic-zero answer already implicit in the prior split-field result.

This argument gives an economical structural obstruction based on the absence of nilpotents; it is not a claim of a new general Rota–Baxter structure theory. A still earlier characteristic-free image-idempotent lemma under different terminology could cover the remaining result, and the originality assessment is correspondingly qualified. The zero-multiplication boundary demonstrates why the original square-zero corollary needed correction.

## References
- V. Gubarev, *Rota–Baxter operators on a sum of fields*, arXiv:1811.08219 (2018), §1: weight-zero operators on a split product are already trivial.
- V. Gubarev, *Rota–Baxter operators on unital algebras*, arXiv:1805.00723 (2018); *Moscow Mathematical Journal* **21** (2021), 325–364.
- L. Guo, M. Rosenkranz, S. Zheng, *Classification of Rota–Baxter operators on semigroup algebras of order two and three*, arXiv:1402.3702; *Communications in Algebra* **47** (2019), 3094–3116.
