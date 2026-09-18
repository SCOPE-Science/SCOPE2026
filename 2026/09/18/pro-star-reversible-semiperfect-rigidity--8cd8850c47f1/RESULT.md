# Pro-star reversibility collapses on semiperfect rings

## Statement

Let \(R\) be an associative unital ring with involution \(*\), and let
\[
P(R)=\{p\in R:p^2=p=p^*\}.
\]
Following Chen--Wang--Zou, call \(R\) **pro-\(*\)-reversible** if
\[
ab\in P(R)\quad\Longrightarrow\quad b^*a\in P(R)
\]
for all \(a,b\in R\).

The following gives a rigidity theorem for this new class.

**Theorem 1 (unit rigidity).** If \(R\) is pro-\(*\)-reversible, then every unit is self-adjoint:
\[
U(R)\subseteq \{x:x^*=x\}.
\]
Consequently \(U(R)\) is abelian. Every idempotent of \(R\) is also self-adjoint, and \(R\) is reversible.

**Theorem 2 (local and semiperfect collapse).**

1. If \(R\) is local, then
\[
R\text{ is pro-}*\text{-reversible}
\iff
R\text{ is commutative and }*=\operatorname{id}_R.
\]
2. More generally, if \(R\) is semiperfect, then
\[
\boxed{
R\text{ is pro-}*\text{-reversible}
\iff
R\text{ is commutative and }*=\operatorname{id}_R.
}
\]

Hence the same equivalence holds for every left or right Artinian ring, every finite ring with identity, and every finite-dimensional algebra over a field.

There is also a sharp contrasting criterion outside the semiperfect setting.

**Theorem 3 (domain boundary).** If \(R\) is a domain, not assumed commutative, then
\[
\boxed{
R\text{ is pro-}*\text{-reversible}
\iff
*\text{ fixes }U(R)\text{ pointwise}.
}
\]
Thus pro-\(*\)-reversibility does not force the involution to be trivial on arbitrary rings. For example, if \(k\) is a field of characteristic different from \(2\), then \(k[x]\) with
\[
f(x)^*=f(-x)
\]
is pro-\(*\)-reversible, although \(*\ne\operatorname{id}\).

Finally, the converse from \(*\)-reversibility to pro-\(*\)-reversibility already fails in the smallest possible nontrivial finite size. The field \(\mathbb F_4\), with Frobenius involution \(x^*=x^2\), is \(*\)-reversible but not pro-\(*\)-reversible. No unital ring of order \(<4\) gives such a separation.

## Proof of unit rigidity

Let \(u\in U(R)\). Put \(a=u\) and \(b=u^{-1}\). Then \(ab=1\in P(R)\), so
\[
(u^{-1})^*u=(u^*)^{-1}u\in P(R).
\]
This element is a unit. The only invertible idempotent is \(1\), hence
\[
(u^*)^{-1}u=1,
\]
and therefore \(u^*=u\).

If \(u,v\in U(R)\), then \(uv\) is a unit and hence self-adjoint. Thus
\[
uv=(uv)^*=v^*u^*=vu,
\]
so \(U(R)\) is abelian.

Now let \(e^2=e\). Since \((1-e)e=0\in P(R)\), pro-\(*\)-reversibility gives
\[
p=e^*(1-e)\in P(R).
\]
Self-adjointness of \(p\) yields
\[
e^*(1-e)=(1-e^*)e.
\]
After expansion, both sides contain \(-e^*e\), so \(e^*=e\). Thus every idempotent is a projection.

For reversibility, suppose \(ab=0\). Then \(b^*a\in P(R)\). Applying the defining condition again to the product \(b^*a\) shows that
\[
a^*b^*=(ba)^*\in P(R),
\]
so \(ba\in P(R)\). But
\[
(ba)^2=b(ab)a=0.
\]
An idempotent with square zero is zero, hence \(ba=0\). Therefore \(R\) is reversible.

As is standard for reversible rings, every idempotent is central. Indeed reversibility implies semicommutativity: from \(xy=0\), first \(yx=0\), then \(y(xr)=0\), and reversing once more gives \((xr)y=0\) for every \(r\). Applying this to \(e(1-e)=0=(1-e)e\) gives
\[
eR(1-e)=0=(1-e)Re,
\]
so \(er=ere=re\) for every \(r\).

## Local rings

Assume \(R\) is local and pro-\(*\)-reversible. If \(x\) is a unit, unit rigidity gives \(x^*=x\). If \(x\) is not a unit, then \(1-x\) is a unit, so
\[
1-x^*=(1-x)^*=1-x,
\]
and again \(x^*=x\). Hence \(*=\operatorname{id}_R\) on all of \(R\).

Since an involution is anti-multiplicative,
\[
xy=(xy)^*=y^*x^*=yx,
\]
so \(R\) is commutative. The converse is immediate: if \(R\) is commutative and \(*\) is the identity, then \(b^*a=ba=ab\), so every projected product stays the same projection.

## Semiperfect rings

Let \(R\) be semiperfect and pro-\(*\)-reversible. Choose a complete orthogonal family of local idempotents
\[
1=e_1+\cdots+e_t,
\]
with each \(e_iRe_i\) local. By Theorem 1 the \(e_i\) are self-adjoint and central. Therefore
\[
R\cong \prod_{i=1}^t e_iR,
\qquad e_iR=e_iRe_i,
\]
and each factor is a local ring stable under \(*\). The pro-\(*\)-reversible condition passes to every such factor. By the local result, each \(e_iR\) is commutative and carries the identity involution. Hence \(R\) itself is commutative and \(*=\operatorname{id}_R\).

The converse was already noted. Standard structure theory gives the advertised Artinian, finite-ring, and finite-dimensional-algebra corollaries because all of those rings are semiperfect.

## Domains and the sharp boundary

Let \(R\) be a domain. Its only idempotents, hence its only projections, are \(0\) and \(1\). Necessity in Theorem 3 is exactly the unit-rigidity argument above.

Conversely, suppose \(*\) fixes every unit. If \(ab\in P(R)\), then \(ab=0\) or \(ab=1\). In the first case the absence of zero divisors gives \(a=0\) or \(b=0\), so \(b^*a=0\). In the second case, a domain is directly finite: from \(ab=1\),
\[
a(ba-1)=0
\]
and \(a\ne0\), hence \(ba=1\). Thus \(a,b\) are units, \(b^*=b\), and
\[
b^*a=ba=1.
\]
So \(R\) is pro-\(*\)-reversible.

For \(k[x]\) with \(f(x)^*=f(-x)\), the units are exactly \(k^\times\), all fixed by \(*\); Theorem 3 therefore gives a nontrivial-involution pro-\(*\)-reversible example. This shows that semiperfectness in Theorem 2 is a genuine boundary rather than a dispensable hypothesis.

## A minimal finite separation from star-reversibility

Every division ring with involution is \(*\)-reversible, since a zero product has a zero factor. By Theorem 1, a pro-\(*\)-reversible division ring would have every nonzero element self-adjoint. Hence the involution would be the identity, and anti-multiplicativity would force the division ring to be commutative.

Take \(\mathbb F_4=\mathbb F_2(\alpha)\) with \(\alpha^2+\alpha+1=0\) and Frobenius involution \(x^*=x^2\). This field is \(*\)-reversible. But with
\[
a=\alpha,\qquad b=\alpha^{-1}=\alpha^2,
\]
we have \(ab=1\in P(\mathbb F_4)\), while
\[
b^*a=\alpha\alpha=\alpha^2\notin\{0,1\}=P(\mathbb F_4).
\]
Thus it is not pro-\(*\)-reversible.

A unital ring of prime order is the corresponding prime field, whose involution is necessarily the identity. Therefore orders \(2\) and \(3\) cannot separate the two notions, and the order-four example is minimal.

## Relation to prior work

Chen, Wang, and Zou introduced pro-\(*\)-reversibility in arXiv:2609.20076v1. They prove that pro-\(*\)-reversible rings are reversible and \(*\)-reversible, and they give an upper-triangular complex-algebra example showing that the converse \(*\)-reversible \(\Rightarrow\) pro-\(*\)-reversible fails. Their paper also proves an equivalent projection condition from which self-adjointness of idempotents follows. Those facts are prior work.

The contribution here is the unit obstruction, the exact local and semiperfect classification, the domain criterion showing where nontrivial involutions can survive, and the minimal finite counterexample \(\mathbb F_4\). The semiperfect decomposition into local corners is standard ring theory.

There is related literature in which self-adjoint units force trivial involution under additional clean-type hypotheses; for example, Viswanathan proves such an implication for a particular feebly-\(*\)-clean setting with \(2\) invertible. The semiperfect theorem above uses neither a clean decomposition nor invertibility of \(2\).

## Limitations and originality

Originality is claimed only to the best of our knowledge. The terminology pro-\(*\)-reversible was introduced in arXiv:2609.20076v1, and targeted searches for that property together with units, local rings, semiperfect rings, Artinian rings, and domains did not locate the results above. The source paper was inspected directly and does not discuss units, local rings, semiperfect rings, or finite rings.

Because the unit argument is short, an equivalent observation may exist under older terminology concerning involutions that fix units, clean rings, or projection-preserving reversibility. The standard semiperfect decomposition and earlier results on \(*\)-reversible rings are not claimed as new. No independent validation is asserted.

## References

1. H. Chen, L. Wang, H. Zou, *On \(*\)-Reversible and Generalized \(*\)-Reversible Rings*, arXiv:2609.20076v1 (2026).
2. T. Y. Lam, *A First Course in Noncommutative Rings*, 2nd ed., Graduate Texts in Mathematics 131, Springer, Chapter 8: Perfect and Semiperfect Rings (2001).
3. W. M. Fakieh, S. K. Nauman, *Reversible Rings with Involutions and Some Minimalities*, Scientific World Journal 2013, Article 650702.
4. S. Viswanathan, *Feebly r-clean ring and feebly \(*\)-r-clean ring*, Ratio Mathematica 48 (2023), 176--188.
