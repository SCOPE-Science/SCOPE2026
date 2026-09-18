# Unit rigidity and a clean–domain dichotomy for projection-transfer rings

Let \(R\) be an associative unital \(*\)-ring, let \(P(R)\) denote its projections, and let \(U(R)\) be its unit group. Two recent notions are:

- \(R\) is **pro-\(*\)-reversible** if
  \[
  ab\in P(R)\quad\Longrightarrow\quad b^*a\in P(R)
  \]
  for all \(a,b\in R\);
- \(R\) is **pro-symmetric** if
  \[
  abc\in P(R)\quad\Longrightarrow\quad acb\in P(R)
  \]
  for all \(a,b,c\in R\).

The purpose of this note is to isolate a structural phenomenon that is not visible from the zero-product definitions alone: these projection-transfer conditions are very rigid on clean/exchange rings, but can remain genuinely noncommutative on domains with small unit groups.

## Theorem 1 — unit rigidity

For every unital \(*\)-ring \(R\):

1. If \(R\) is pro-\(*\)-reversible, then every unit is self-adjoint,
   \[
   u^*=u\qquad (u\in U(R)),
   \]
   and \(U(R)\) is abelian.
2. If \(R\) is pro-symmetric, then \(U(R)\) is abelian.

Consequently, in either class every element of \(J(R)\) commutes with every unit, and \(J(R)\) is a commutative ideal. Every nilpotent commutes with every unit and with every other nilpotent. In the pro-\(*\)-reversible case, all elements of \(J(R)\) and all nilpotents are also self-adjoint.

### Proof

Assume first that \(R\) is pro-\(*\)-reversible and let \(u\in U(R)\). Put \(a=u\) and \(b=u^{-1}\). Since \(ab=1\in P(R)\),
\[
(u^{-1})^*u=(u^*)^{-1}u\in P(R).
\]
This element is a unit. The only invertible idempotent is \(1\), so
\[
(u^*)^{-1}u=1,
\]
and hence \(u^*=u\).

Now if \(u,v\in U(R)\), the unit \(uv\) is also self-adjoint. Therefore
\[
uv=(uv)^*=v^*u^*=vu,
\]
so \(U(R)\) is abelian.

For the pro-symmetric case, let \(u,v\in U(R)\) and take
\[
a=(uv)^{-1},\qquad b=u,\qquad c=v.
\]
Then \(abc=1\in P(R)\), hence \(acb\in P(R)\). But \(acb\) is a unit, so it must equal \(1\). Multiplying by \(uv\) gives \(vu=uv\).

Finally, if \(j\in J(R)\), then \(1+j\in U(R)\). If \(u\in U(R)\), commutativity of the unit group gives
\[
u(1+j)=(1+j)u,
\]
hence \(uj=ju\). Taking two radical elements gives commutativity of \(J(R)\). The same argument applies to nilpotents because \(1+n\) is a unit whenever \(n\) is nilpotent. In the pro-\(*\)-reversible case, \((1+j)^*=1+j\) and \((1+n)^*=1+n\), so \(j^*=j\) and \(n^*=n\). \(\square\)

The recent pro-\(*\)-reversible theory also proves that every idempotent is self-adjoint and central; equivalently, all idempotents are projections and are central. The pro-symmetric theory proves that every pro-symmetric ring is symmetric, hence reversible; reversible rings have central idempotents. Thus both classes are idempotent-central (often called *abelian rings* in the ring-theoretic sense), while Theorem 1 adds a separate unit-group rigidity.

## Theorem 2 — clean and exchange classification

Let \(R\) be a unital \(*\)-ring.

### (a) Clean rings

If \(R\) is clean, then
\[
\boxed{R\text{ pro-symmetric}\iff R\text{ commutative},}
\]
and
\[
\boxed{R\text{ pro-}*\text{-reversible}\iff R\text{ commutative and }*=\mathrm{id}_R.}
\]

### (b) Exchange rings

The same equivalences hold if “clean” is replaced by “exchange.”

### Proof

Suppose first that \(R\) is clean and pro-symmetric. Every element can be written
\[
x=e+u
\]
with \(e^2=e\) and \(u\in U(R)\). Pro-symmetry implies reversibility, hence every idempotent is central, while Theorem 1 gives an abelian unit group. For
\[
x=e+u,\qquad y=f+v,
\]
all terms involving \(e\) or \(f\) commute, and \(uv=vu\). Hence \(xy=yx\). Conversely, every commutative ring is pro-symmetric, independently of the chosen involution.

Now suppose \(R\) is clean and pro-\(*\)-reversible. The cited projection-transfer result gives \(e^*=e\) for every idempotent, and Theorem 1 gives \(u^*=u\) for every unit. Therefore every clean decomposition \(x=e+u\) satisfies
\[
x^*=e^*+u^*=e+u=x.
\]
Thus \(*=\mathrm{id}_R\). Since an involution is an anti-automorphism,
\[
xy=(xy)^*=y^*x^*=yx,
\]
so \(R\) is commutative. The converse is immediate.

For exchange rings, both projection-transfer conditions force all idempotents to be central. Nicholson's theorem that idempotent-central exchange rings are clean therefore reduces the exchange case to the clean case. \(\square\)

## Corollary 3 — finite-dimensional algebras collapse

Let \(A\) be a finite-dimensional unital algebra over a field and let \(*\) be any ring involution on \(A\). Then
\[
\boxed{A\text{ is pro-symmetric}\iff A\text{ is commutative},}
\]
and
\[
\boxed{A\text{ is pro-}*\text{-reversible}\iff A\text{ is commutative and }*=\mathrm{id}_A.}
\]

Indeed, every finite-dimensional algebra is Artinian, hence exchange (in fact semiperfect and clean). The same conclusion applies to all left or right Artinian \(*\)-rings and, more generally, to all semiperfect \(*\)-rings.

This is a sharp restriction: within the usual finite-dimensional setting there are no genuinely noncommutative examples of either projection-transfer class.

## Theorem 4 — exact domain criteria

Let \(R\) be a (not necessarily commutative) domain with involution. Then
\[
\boxed{R\text{ is pro-}*\text{-reversible}\iff u^*=u\text{ for every }u\in U(R),}
\]
and
\[
\boxed{R\text{ is pro-symmetric}\iff U(R)\text{ is abelian}.}
\]

### Proof

A domain has only the idempotents \(0,1\), hence only the projections \(0,1\). It is also directly finite: if \(xy=1\), then
\[
(yx-1)y=0,
\]
and \(y\ne0\), so \(yx=1\).

Necessity in both statements is Theorem 1. For the first converse, assume every unit is self-adjoint and let \(ab\in P(R)=\{0,1\}\). If \(ab=0\), then one of \(a,b\) is zero, so \(b^*a=0\). If \(ab=1\), direct finiteness makes \(a,b\) units and gives \(ba=1\). Hence
\[
b^*a=ba=1.
\]
Thus \(R\) is pro-\(*\)-reversible.

For the second converse, assume \(U(R)\) is abelian and let \(abc\in P(R)\). If \(abc=0\), one factor is zero and therefore \(acb=0\). If \(abc=1\), direct finiteness implies that \(a,b,c\) are units. Since the unit group is abelian,
\[
acb=abc=1.
\]
Thus \(R\) is pro-symmetric. \(\square\)

For a division ring this immediately specializes to the familiar rigid boundary: pro-symmetry forces the division ring to be a field, and pro-\(*\)-reversibility forces a field with the identity involution.

## Example 5 — a noncommutative domain in both classes

Let
\[
F=k\langle x,y\rangle
\]
be the free associative algebra on two generators over a field \(k\), equipped with the reversal involution
\[
(a_1a_2\cdots a_m)^*=a_m\cdots a_2a_1,
\qquad x^*=x,\quad y^*=y,
\]
extended \(k\)-linearly.

The free algebra is a domain. Its units are exactly \(k^\times\): if nonzero elements \(f,g\) satisfy \(fg=1\), comparison of highest homogeneous degrees forces both to have degree zero. Thus \(U(F)=k^\times\) is abelian and every unit is fixed by \(*\).

Theorem 4 gives
\[
\boxed{F\text{ is both pro-symmetric and pro-}*\text{-reversible}.}
\]
Yet \(F\) is noncommutative and the involution is nontrivial, since
\[
(xy)^*=yx\ne xy.
\]
Hence the clean/exchange hypothesis in Theorem 2 is essential: projection-transfer conditions can be extremely weak on domains whose projection set is \(\{0,1\}\) and whose unit group is small.

The unit criterion also gives a one-line explanation of a recent example separating \(*\)-reversibility from pro-\(*\)-reversibility: in the dual-number-type algebra \(V_2(\mathbb C)\), the displayed unit with off-diagonal entry \(1\) is not fixed by the involution, so Theorem 1 immediately forbids pro-\(*\)-reversibility.

## Relation to prior work

Chen, Wang and Zou introduced pro-\(*\)-reversible rings in arXiv:2609.20076v1 (17 September 2026). Their Definition 3.2 is the definition used above; Lemma 3.3 shows pro-\(*\)-reversible rings are reversible, Lemma 3.8 shows the relevant projection condition forces idempotents to be self-adjoint and central, and Corollary 3.11 gives an equivalent projection formulation. Their Example 3.13 separates \(*\)-reversibility from pro-\(*\)-reversibility.

The same authors introduced pro-symmetric rings in arXiv:2609.20084v1 (17 September 2026). They prove that every pro-symmetric ring is symmetric, and Proposition 4.7 shows that whenever a triple product is a projection, all six permutations of that triple product coincide. These statements are treated here as prior work.

Nicholson's exchange-ring theory supplies the classical fact that idempotent-central exchange rings are clean. Related unit-group rigidity is also classical: Nicholson studied semiperfect rings with abelian unit groups, and Han–Lee–Lee proved, among other results, that for an idempotent-central semiperfect ring their stronger I-symmetry condition, an abelian unit group, and commutativity are equivalent.

The contribution here is narrower: the universal unit consequences of the two new projection-transfer notions, the resulting clean/exchange classifications (including the finite-dimensional collapse), and the exact domain criteria together with the free-algebra boundary example. Targeted searches using the new terminology and equivalent formulations did not locate these statements in the prior literature.

## Limitations

The originality assessment is to the best of our knowledge. Both motivating notions were introduced in very recent preprints, so revisions or independent observations may appear quickly. The arguments above are elementary syntheses of the new definitions with classical clean/exchange and unit-group facts; equivalent statements could exist under older terminology not using “pro-symmetric” or “pro-\(*\)-reversible.” No novelty is claimed for clean rings, exchange rings, the classical structure of semiperfect rings with abelian unit groups, or the fact that the free associative algebra is a domain with scalar units.

The clean/exchange theorem does not classify arbitrary rings in either new class. The domain theorem applies only to zero-divisor-free rings; outside that setting, zero products introduce additional constraints not encoded solely by the unit group.

## References

1. H. Chen, L. Wang, H. Zou, *On \(\ast\)-Reversible and Generalized \(\ast\)-Reversible Rings*, arXiv:2609.20076v1, 2026. https://arxiv.org/abs/2609.20076
2. H. Chen, L. Wang, H. Zou, *Transposed Triple Products and Pro-Symmetric Rings in \(\ast\)-Rings*, arXiv:2609.20084v1, 2026. https://arxiv.org/abs/2609.20084
3. W. K. Nicholson, *Lifting idempotents and exchange rings*, Trans. Amer. Math. Soc. 229 (1977), 269–278. https://doi.org/10.1090/S0002-9947-1977-0439876-2
4. W. K. Nicholson, *Semiperfect rings with abelian group of units*, Pacific J. Math. 49 (1973), 191–198. https://doi.org/10.2140/pjm.1973.49.191
5. J. Han, C. I. Lee, Y. Lee, *Symmetry on zero and idempotents*, Comm. Algebra 51 (2023), 464–474. https://doi.org/10.1080/00927872.2022.2102177
