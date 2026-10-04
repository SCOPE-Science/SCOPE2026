# A dimension-field threshold for strengthened domination in zero-divisor dot product graphs

## Finding

Let \(q\) be a prime power and \(n\ge3\). Let \(ZD(\mathbb F_q^n)\) be Badawi's zero-divisor dot product graph: its vertices are the nonzero vectors of \(\mathbb F_q^n\) having at least one zero coordinate, with distinct vertices adjacent exactly when their standard dot product is zero. Then \[\gamma_t\!\left(ZD(\mathbb F_q^n)\right)=\min\{n,q+1\},\] and \[\gamma_{\mathrm{pr}}\!\left(ZD(\mathbb F_q^n)\right)=2\left\lceil\frac{\min\{n,q+1\}}2\right\rceil.\] Thus the zero-divisor restriction creates a sharp dimension-field threshold: below the projective-line covering threshold the coordinate basis is optimal, while above it a projective line of orthogonal hyperplanes is optimal; paired domination is exactly the least even integer not smaller than total domination.

The two formulas are uniform over all finite fields and all dimensions \(n\ge3\).

## Assumptions and scope

Let
\[
V=\mathbb F_q^n,
\qquad n\ge3,
\]
with the standard symmetric bilinear form
\[
B(x,y)=x\cdot y=\sum_{i=1}^n x_i y_i.
\]
For the product ring \(\mathbb F_q^n\), a nonzero vector is a zero-divisor exactly when at least one coordinate is zero. Hence
\[
V\!\left(ZD(\mathbb F_q^n)\right)
=
\bigcup_{i=1}^n H_i\setminus\{0\},
\qquad
H_i=\{x\in V:x_i=0}.
\]
For a nonzero vector \(d\), write
\[
d^\perp=\{x\in V:B(x,d)=0}.
\]

A total dominating set must meet the open neighborhood of every vertex, including every selected vertex. A paired dominating set is a dominating set whose induced subgraph has a perfect matching.

## Proof

We first record the finite-space covering fact used for the lower bound.

**Subspace-cover lemma.** A finite-dimensional vector space over \(\mathbb F_q\) cannot be the union of at most \(q\) proper linear subspaces.

To see this, enlarge the putative covering subspaces so that none is contained in another and choose one of maximal dimension, say \(U_1\). The union inside \(U_1\) of its intersections with at most \(q-1\) other covering subspaces has cardinality at most
\[
(q-1)q^{\dim U_1-1}<|U_1|,
\]
so choose \(b\in U_1\) outside all those intersections. Choose \(a\notin U_1\). Each other covering subspace contains at most one point of the affine line
\[
\{a+\lambda b:\lambda\in\mathbb F_q}.
\]
The remaining at most \(q-1\) subspaces therefore cannot cover its \(q\) points, a contradiction.

Now let \(D\) be a total dominating set of \(ZD(\mathbb F_q^n)\). For each coordinate hyperplane \(H_i\), total domination gives
\[
H_i\subseteq\bigcup_{d\in D}d^\perp.
\tag{1}
\]
Assume \(|D|<q+1\). Restricting (1) to \(H_i\), the subspace-cover lemma implies that for some \(d\in D\),
\[
H_i\subseteq d^\perp.
\]
Consequently
\[
d\in H_i^\perp=\operatorname{span}(e_i).
\]
This must occur for every \(i\), and a nonzero vector cannot be a scalar multiple of two distinct coordinate vectors. Hence \(|D|\ge n\). Therefore every total dominating set satisfies
\[
|D|\ge\min\{n,q+1\}.
\tag{2}
\]

If \(n\le q+1\), the coordinate basis
\[
D_0=\{e_1,\ldots,e_n}
\]
is a total dominating set. Indeed, every zero-divisor vertex has a zero coordinate and is therefore orthogonal to the corresponding basis vector; the basis vectors themselves are pairwise orthogonal because \(n\ge3\). Thus
\[
\gamma_t\le n.
\tag{3}
\]

Suppose now that \(n>q+1\). We construct a total dominating set of size \(q+1\). Choose a two-dimensional subspace \(L\subseteq\mathbb F_q^n\), supported on the first three coordinates, for which the restriction of \(B\) has one-dimensional radical.

In characteristic two, take
\[
r=e_1+e_2,\qquad u=e_3,
\qquad L=\operatorname{span}\{r,u}.
\]
Then \(r\) spans the radical of \(B|_L\).

In odd characteristic, let \(S\) be the set of squares in \(\mathbb F_q\). Since
\[
|S|=\frac{q+1}2,
\]
the sets \(S\) and \(-1-S\) intersect; hence choose \(a,b\) with
\[
a^2+b^2=-1.
\]
Then
\[
r=e_1+a e_2+b e_3
\]
is isotropic. Choose
\[
u\in r^\perp\setminus\operatorname{span}(r).
\]
The restriction to \(L=\operatorname{span}\{r,u}\) has radical exactly \(\operatorname{span}(r)\): otherwise a two-dimensional totally isotropic subspace would lie inside its one-dimensional orthogonal complement in the nondegenerate three-dimensional coordinate space.

Choose one nonzero representative from each of the \(q+1\) one-dimensional subspaces of \(L\), choosing \(r\) on the radical line, and call the resulting set \(D_L\). Every member of \(D_L\) is a zero-divisor because it is supported on the first three coordinates while \(n>q+1\ge3\).

For every \(x\in V\), the linear functional
\[
d\longmapsto B(x,d)
\]
on the two-dimensional space \(L\) has a nonzero kernel vector. Hence some member of \(D_L\) is orthogonal to \(x\). Moreover, the radical representative \(r\) is orthogonal to every member of \(D_L\), so every selected vertex also has a distinct selected neighbor. Therefore \(D_L\) is total dominating and
\[
\gamma_t\le q+1.
\tag{4}
\]
Equations (2)--(4) prove
\[
\gamma_t\!\left(ZD(\mathbb F_q^n)\right)=\min\{n,q+1\}.
\]

For paired domination, every paired dominating set is total dominating and has even cardinality, so if
\[
m=\min\{n,q+1\},
\]
then
\[
\gamma_{\mathrm{pr}}\ge2\left\lceil\frac m2\right\rceil.
\tag{5}
\]

When \(n\le q+1\), the basis \(D_0\) induces a clique. If \(n\) is even it already has a perfect matching. If \(n\) is odd, add
\[
e_1+e_2.
\]
This new zero-divisor vertex is adjacent to \(e_3\); match those two and match the remaining \(n-1\) basis vertices inside their clique. Hence the lower bound (5) is attained.

Assume \(n>q+1\). If \(q\) is odd, choose a nonzero \(c\in\mathbb F_q\) such that \(-c\) is a nonsquare. Again using \(|S|=(q+1)/2\), choose \(a,b\) with
\[
a^2+b^2=c.
\]
Set
\[
L=\operatorname{span}\{e_1,\,a e_2+b e_3}.
\]
The restricted quadratic form is
\[
x^2+c y^2,
\]
which is anisotropic because \(-c\) is a nonsquare. Choose one representative from each projective line of \(L\). As above, the corresponding \(q+1\) orthogonal hyperplanes cover all of \(V\). Inside \(L\), orthogonal complementation is a fixed-point-free involution on its \(q+1\) projective lines, so these representatives have a perfect matching. They are all zero-divisors because they are supported on three coordinates. Thus
\[
\gamma_{\mathrm{pr}}=q+1
\]
for odd \(q\).

If \(q\) is even and \(n\ge5\), take
\[
L=\operatorname{span}\{e_1+e_2,\,e_3+e_4}.
\]
The restriction of \(B\) to \(L\) is zero, so one representative from each of its \(q+1\) projective lines gives a pairwise orthogonal total dominating set; all representatives are zero-divisors because their support lies in the first four coordinates. Add \(e_5\), which is orthogonal to all of them. The resulting \(q+2\) vertices induce a complete graph and therefore admit a perfect matching.

The only remaining even-characteristic case with \(n>q+1\) is
\[
(q,n)=(2,4).
\]
Here
\[
\{e_2,e_3,e_4,e_3+e_4}
\]
is total dominating: a vertex with a zero among coordinates two, three, or four is orthogonal to the corresponding basis vector, while the only pattern with just the first coordinate zero is orthogonal to \(e_3+e_4\). It has the perfect matching
\[
\{e_2,e_3+e_4},\qquad \{e_3,e_4}.
\]
Thus (5) is attained in every case, proving
\[
\gamma_{\mathrm{pr}}\!\left(ZD(\mathbb F_q^n)\right)
=
2\left\lceil\frac{\min\{n,q+1\}}2\right\rceil.
\]

## Verification

The standalone `verify.py` constructs \(ZD(\mathbb F_q^n)\) directly for six prime-field cases and exhaustively computes the minimum total and paired dominating sets. The cases cover both sides of the threshold and both parities. It separately checks the projective-plane paired constructions beyond the threshold for odd fields and the characteristic-two constructions, including the exceptional pair \((q,n)=(2,4)\).

Exact output:

```text
VERIFY_OK
q=2 n=3 vertices=6 gamma_t=3 gamma_pr=4
q=2 n=4 vertices=14 gamma_t=3 gamma_pr=4
q=2 n=5 vertices=30 gamma_t=3 gamma_pr=4
q=3 n=3 vertices=18 gamma_t=3 gamma_pr=4
q=3 n=4 vertices=64 gamma_t=4 gamma_pr=4
q=5 n=3 vertices=60 gamma_t=3 gamma_pr=4
odd_field_projective_constructions=q3n5,q5n7_passed
even_characteristic_paired_constructions=q2n4,q2n5_passed
```

The exhaustive finite calculations are corroborative only. The theorem for all prime powers follows from the subspace-cover argument and the explicit finite-field constructions above.

## Relationship to prior work

Badawi introduced the total and zero-divisor dot product graphs and proved connectivity, diameter, girth, and comparison results with the classical zero-divisor graph. The accessible full article does not treat domination parameters.

Abdulla and Badawi later studied the structure of dot product graphs over finite fields and residue rings. For a two-factor finite-field product they identify the zero-divisor dot product graph as a complete bipartite graph. That special two-dimensional structure is outside the stated range \(n\ge3\), and their structural results do not supply the dimension-field threshold proved here.

Saleh and Megahed study ordinary domination for total dot product graphs over residue rings and unit/congruence variants. Their domination section concerns the total graph rather than the zero-divisor induced graph and gives upper bounds in a different arithmetic setting. It does not state total or paired domination for \(ZD(\mathbb F_q^n)\).

The decisive new feature here is that restricting to zero-divisors changes the covering problem from all nonzero vectors to the union of the coordinate hyperplanes. The minimum therefore becomes \(\min\{n,q+1\}\), so the dimension enters sharply; this behavior is not implied by a domination formula for the ambient total dot product graph.

## Limitations

The theorem assumes a finite field and the standard dot product. It does not address finite chain rings or general finite commutative coefficient rings, where orthogonal hyperplanes need not be vector subspaces over a field.

No classification of all minimum dominating sets is claimed. The proof determines the exact cardinalities and supplies canonical optimal constructions.

The lower bound uses the sharp fact that at least \(q+1\) proper subspaces are needed to cover a finite vector space when no single one contains the whole target subspace.

## References

1. A. Badawi, “On the Dot Product Graph of a Commutative Ring,” *Communications in Algebra* 43 (2015), 43–50. DOI: 10.1080/00927872.2014.897188.
2. M. Abdulla and A. Badawi, “On the Dot Product Graph of a Commutative Ring II,” *International Electronic Journal of Algebra* 28 (2020), 61–74. DOI: 10.24330/ieja.768135.
3. D. Saleh and N. Megahed, “Dot product graphs and domination number,” *Journal of the Egyptian Mathematical Society* 28 (2020), Article 31. DOI: 10.1186/s42787-020-00092-6.
