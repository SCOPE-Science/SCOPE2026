# Unit groups exactly detect pro-star-reversibility

## Statement

Let \(R\) be a unital ring with involution \(*\). Recall that \(R\) is **\(*\)-reversible** if
\[
ab=0\implies b^*a=0,
\]
and **pro-\(*\)-reversible** if
\[
ab\in P(R)\implies b^*a\in P(R),
\]
where \(P(R)=\{p:p^2=p=p^*\}\) is the set of projections.

### Theorem

For every unital \(*\)-ring \(R\), the following are equivalent:

1. \(R\) is pro-\(*\)-reversible.
2. \(R\) is \(*\)-reversible and every unit is fixed by the involution:
   \[
   u^*=u\qquad (u\in U(R)).
   \]

Moreover, under these equivalent conditions, whenever \(ab=p\in P(R)\), one has the stronger identity
\[
\boxed{b^*a=p=ab.}
\]

Thus the gap between \(*\)-reversibility and pro-\(*\)-reversibility is exactly the existence of a unit moved by the involution.

## Proof

Assume first that \(R\) is pro-\(*\)-reversible. The implication
\[
\text{pro-\(*\)-reversible}\Longrightarrow \text{\(*\)-reversible}
\]
is Proposition 3.5 of Chen--Wang--Zou (2026).

Let \(u\in U(R)\). Put \(a=u\) and \(b=u^{-1}\). Then \(ab=1\in P(R)\), so pro-\(*\)-reversibility gives
\[
(u^{-1})^*u=(u^*)^{-1}u\in P(R).
\]
This element is a unit. An invertible idempotent is necessarily \(1\); hence
\[
(u^*)^{-1}u=1,
\]
and therefore \(u^*=u\).

Conversely, suppose that \(R\) is \(*\)-reversible and that every unit is fixed by \(*\). Let
\[
ab=p\in P(R),\qquad e=1-p.
\]
A \(*\)-reversible ring is reversible. In a reversible ring every idempotent is central, and if \(ab\) is idempotent then \(ba=ab\). Hence \(p\) and \(e\) are central and
\[
ba=p.
\]
Define
\[
u=pa+e,\qquad v=pb+e.
\]
Using centrality of \(p,e\), together with \(ab=ba=p\), gives
\[
uv=vu=1.
\]
Thus \(u,v\in U(R)\), so by hypothesis \(u^*=u\) and \(v^*=v\). Since \(p^*=p\) and \(e^*=e\), this yields
\[
pa^*=pa,\qquad pb^*=pb.
\]
Consequently
\[
pb^*a=pba=p.
\]
On the other hand,
\[
(ea)b=eab=ep=0.
\]
By \(*\)-reversibility,
\[
b^*ea=0.
\]
Since \(e\) is central,
\[
eb^*a=0.
\]
Therefore
\[
b^*a=(p+e)b^*a=p.
\]
In particular \(b^*a\in P(R)\), proving pro-\(*\)-reversibility and the displayed stronger identity. \(\square\)

## Structural consequences

### Corollary 1: the unit group is abelian

Every pro-\(*\)-reversible ring has abelian unit group. Indeed, the theorem gives \(u^*=u\) for every unit, so for \(u,v\in U(R)\),
\[
uv=(uv)^*=v^*u^*=vu.
\]

### Corollary 2: the involution is trivial on the Jacobson radical

If \(R\) is pro-\(*\)-reversible, then
\[
\boxed{x^*=x\quad\text{for every }x\in J(R).}
\]
For \(x\in J(R)\), the element \(1+x\) is a unit, hence \((1+x)^*=1+x\).

### Corollary 3: clean rings collapse to the trivial involution

Suppose \(R\) is clean, i.e. every element has a decomposition
\[
x=e+u
\]
with \(e^2=e\) and \(u\in U(R)\). Then
\[
\boxed{R\text{ is pro-\(*\)-reversible}\iff *=\mathrm{id}_R.}
\]

For the forward direction, a unital \(*\)-reversible ring has every idempotent fixed by \(*\) (Fakieh, Proposition 8), while the theorem above fixes every unit. Thus a clean decomposition gives
\[
x^*=e^*+u^*=e+u=x
\]
for all \(x\in R\). Since an involution is anti-multiplicative, \(*=\mathrm{id}_R\) also forces \(R\) to be commutative. The converse is immediate.

Since every semiperfect ring is clean, it follows in particular that
\[
\boxed{
R\text{ semiperfect and pro-\(*\)-reversible}
\iff
R\text{ is commutative and }*=\mathrm{id}_R.
}
\]
Hence the same conclusion applies to Artinian rings and local rings.

### Corollary 4: division rings

A division \(*\)-ring is pro-\(*\)-reversible if and only if it is a field with the identity involution. Indeed, every nonzero element is a unit, so the theorem makes \(*\) the identity; anti-multiplicativity then forces commutativity.

## Sharpness outside the clean setting

Pro-\(*\)-reversibility does not force the involution to be trivial without an additive hypothesis such as cleanness. Let
\[
R=\mathbb F_2[x],\qquad f(x)^*=f(x+1).
\]
This is a nontrivial involution of order two. The ring is a domain, hence \(*\)-reversible, while
\[
U(R)=\{1\}
\]
is fixed pointwise. The theorem therefore implies that \(R\) is pro-\(*\)-reversible. Thus the clean/semiperfect collapse above is a genuine boundary rather than a consequence of pro-\(*\)-reversibility alone.

## Relation to the 2026 source paper

Chen--Wang--Zou introduced pro-\(*\)-reversible rings and proved that they imply \(*\)-reversibility. Their Question 3.7 asks whether the converse holds; Example 3.13 answers negatively using
\[
V_2(\mathbb C)=\left\{\begin{pmatrix}a&b\\0&a\end{pmatrix}:a,b\in\mathbb C\right\}
\]
with the involution sending the off-diagonal entry to its negative. In that example their two displayed factors are inverse units, and one of them is moved by the involution. The theorem above identifies this as the complete obstruction: among \(*\)-reversible rings, pro-\(*\)-reversibility is equivalent to pointwise fixation of the unit group.

The source paper contains no occurrence of “unit” or “invertible” in its arXiv v1 HTML text, so this criterion is not one of its stated characterizations.

## Limitations and originality boundary

The result is claimed only to the best of our knowledge. The notions of reversible rings, \(*\)-reversible rings, clean rings, and the fact that idempotents of a unital \(*\)-reversible ring are self-adjoint are prior art. Likewise, semiperfect \(\Rightarrow\) clean is classical and is not claimed here.

The claimed contribution is the exact criterion
\[
\text{pro-\(*\)-reversible}
\iff
\text{\(*\)-reversible}+\text{all units self-adjoint},
\]
together with the resulting structural consequences for unit groups, Jacobson radicals, clean/semiperfect rings, and division rings, and the nonclean sharpness example above. Because pro-\(*\)-reversibility was introduced only in the cited 2026 preprint, the principal residual originality risk is an equivalent observation appearing under different terminology or in a revision/concurrent follow-up.

## References

1. H. Chen, L. Wang, H. Zou, *On \(*\)-Reversible and Generalized \(*\)-Reversible Rings*, arXiv:2609.20076v1 (2026). https://arxiv.org/abs/2609.20076v1
2. A. H. Fakieh, *Reversible Rings with Involutions and Some Minimalities*, The Scientific World Journal 2013, Article ID 650702. https://doi.org/10.1155/2013/650702
3. J. Han and W. K. Nicholson, *Extensions of Clean Rings*, Communications in Algebra 29 (2001), 2589--2595. https://doi.org/10.1081/AGB-100002409
