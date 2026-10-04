# Commutator fibers and commuting probabilities of finite Kronecker path algebras

## Finding

Let \(q\) be a prime power and let \(r\ge1\). Let \(A_{r,q}\) be the path algebra over \(\mathbf F_q\) of the quiver with two vertices and \(r\) parallel arrows from the first vertex to the second. Equivalently,
\[
A_{r,q}
=
\left\{
\begin{pmatrix}
a&v\\
0&c
\end{pmatrix}
:
a,c\in\mathbf F_q,\ v\in\mathbf F_q^r
\right\},
\]
with multiplication
\[
(a,v,c)(d,w,f)=(ad,\;aw+fv,\;cf).
\]

Then \(A_{r,q}\) has exactly
\[
\boxed{q^r+2}
\]
distinct element-centralizers. Its center has \(q\) elements. Apart from the whole algebra, its distinct centralizers consist of one subalgebra of size \(q^{r+1}\) and \(q^r\) subalgebras of size \(q^2\).

The additive commutator set is exactly the Jacobson radical
\[
J=
\{(0,z,0):z\in\mathbf F_q^r\}.
\]
The number of ordered pairs with zero commutator is
\[
\boxed{
q^{2r+2}+(q^2-1)q^{r+2}.
}
\]
Every fixed nonzero element of \(J\) has exactly
\[
\boxed{
q^{r+2}(q^2-1)
}
\]
ordered commutator representations. Therefore
\[
\boxed{
\operatorname{Pr}(A_{r,q})
=
q^{-2}+(q^2-1)q^{-r-2}.
}
\]

The number of centralizers does not determine the commuting probability, even inside this family. If \(p\) is prime, \(M\ge2\), and \(a\mid M\), then
\[
A_{M/a,p^a}
\]
has \(p^M+2\) centralizers, while
\[
\operatorname{Pr}(A_{M/a,p^a})
=
p^{-M}+(1-p^{-M})p^{-2a}.
\]
For fixed \(p\) and \(M\), these values are strictly decreasing as \(a\) increases, hence are pairwise distinct for distinct divisors \(a\).

The smallest illustrative collision is
\[
A_{2,2}
\quad\text{and}\quad
A_{1,4}.
\]
Both have exactly \(6\) centralizers, but
\[
\operatorname{Pr}(A_{2,2})=\frac7{16},
\qquad
\operatorname{Pr}(A_{1,4})=\frac{19}{64}.
\]
The second algebra has
\[
A_{1,4}/Z(A_{1,4})\cong C_2^4
\]
as an additive group, giving an explicit commuting probability in the elementary-abelian rank-four central-factor case that was excluded from the explicit \(6\)-centralizer probability list in the motivating 2018 paper.

## Assumptions and scope

The algebra is finite, associative, and unital. The field \(\mathbf F_q\) is arbitrary; no restriction on its characteristic is used.

The commuting probability of a finite ring \(R\) is
\[
\operatorname{Pr}(R)
=
\frac{|\{(x,y)\in R^2:xy=yx\}|}{|R|^2}.
\]
An element-centralizer is
\[
C_R(x)=\{y\in R:xy=yx\}.
\]

The quiver has no paths of length two, so its arrow space is the Jacobson radical and has square zero. The theorem concerns element-centralizers and additive commutators, not module endomorphism rings or centralizers of representations.

## Proof

Write
\[
x=(a,v,c),\qquad y=(d,w,f),
\]
and set
\[
\delta=a-c,\qquad \varepsilon=d-f.
\]
Direct multiplication gives
\[
[x,y]=xy-yx
=
(0,\;\delta w-\varepsilon v,\;0).
\]
Each pair \((\delta,v)\in\mathbf F_q\times\mathbf F_q^r\) has exactly \(q\) lifts to an element \(x\), since \(c\) is free and \(a=c+\delta\). The same holds for \(y\).

First determine the center. An element \(x\) commutes with every \(y\) exactly when
\[
\delta w-\varepsilon v=0
\]
for all \(\varepsilon,w\). Taking \(\varepsilon=0\) and arbitrary \(w\) gives \(\delta=0\), and then taking arbitrary \(\varepsilon\) gives \(v=0\). Hence
\[
Z(A_{r,q})=\{(a,0,a):a\in\mathbf F_q\},
\]
which has \(q\) elements.

Now classify all centralizers.

If \(\delta=0\) and \(v\ne0\), the equation
\[
\varepsilon v=0
\]
forces \(\varepsilon=0\). Therefore every such element has the same centralizer
\[
H=\{(d,w,d):d\in\mathbf F_q,\ w\in\mathbf F_q^r\},
\]
of size \(q^{r+1}\).

If \(\delta\ne0\), put
\[
u=\delta^{-1}v.
\]
The commuting equation is equivalent to
\[
w=\varepsilon u.
\]
Thus
\[
C_{A_{r,q}}(x)
=
C_u
=
\{(f+\varepsilon,\varepsilon u,f):f,\varepsilon\in\mathbf F_q\},
\]
which has size \(q^2\). Distinct vectors \(u\) give distinct centralizers, because \(C_u\) contains \((1,u,0)\), and equality \(C_u=C_{u'}\) forces \(u=u'\). There are \(q^r\) possibilities for \(u\).

The whole algebra is the centralizer of every central element. It is distinct from \(H\) and all \(C_u\). Therefore the total number of distinct element-centralizers is
\[
1+1+q^r=q^r+2.
\]

For the commutator fibers, reduce to counting solutions of
\[
\delta w-\varepsilon v=z
\]
in
\[
(\delta,v,\varepsilon,w)
\in
\mathbf F_q\times\mathbf F_q^r\times\mathbf F_q\times\mathbf F_q^r.
\]
Every reduced solution has \(q^2\) lifts to an ordered pair of algebra elements.

For \(z=0\), if \((\delta,\varepsilon)=(0,0)\), then \(v,w\) are arbitrary, giving \(q^{2r}\) solutions. If \(\delta\ne0\), there are \((q-1)q\) choices for \((\delta,\varepsilon)\), \(q^r\) choices for \(v\), and \(w\) is forced. If \(\delta=0\) and \(\varepsilon\ne0\), then \(v=0\) and \(w\) is arbitrary, giving \((q-1)q^r\) solutions. Hence the reduced zero fiber has
\[
q^{2r}+(q^2-1)q^r
\]
points, and the full zero fiber has
\[
q^{2r+2}+(q^2-1)q^{r+2}.
\]

For fixed \(z\ne0\), the pair \((\delta,\varepsilon)=(0,0)\) contributes nothing. For every one of the \(q^2-1\) remaining pairs, the linear map
\[
(v,w)\longmapsto \delta w-\varepsilon v
\]
from \(\mathbf F_q^{2r}\) onto \(\mathbf F_q^r\) is surjective with kernel of size \(q^r\). Therefore every nonzero \(z\) has
\[
(q^2-1)q^r
\]
reduced representations and
\[
q^{r+2}(q^2-1)
\]
full representations.

Since
\[
|A_{r,q}|=q^{r+2},
\]
division of the zero-fiber count by \(q^{2r+4}\) gives
\[
\operatorname{Pr}(A_{r,q})
=
q^{-2}+(q^2-1)q^{-r-2}.
\]

Finally, fix a prime \(p\), an integer \(M\ge2\), and a divisor \(a\mid M\). Put
\[
q=p^a,\qquad r=M/a.
\]
Then
\[
q^r=p^M,
\]
so every algebra in this divisor family has exactly \(p^M+2\) centralizers. Substitution in the probability formula gives
\[
\operatorname{Pr}(A_{M/a,p^a})
=
p^{-M}+(1-p^{-M})p^{-2a}.
\]
The coefficient \(1-p^{-M}\) is positive, so this expression is strictly decreasing in \(a\). Thus distinct divisors give distinct probabilities despite the common centralizer count.

For \(p=2\) and \(M=2\), the choices \(a=1,2\) yield
\[
\operatorname{Pr}(A_{2,2})=\frac7{16},
\qquad
\operatorname{Pr}(A_{1,4})=\frac{19}{64}.
\]
Also
\[
|A_{1,4}:Z(A_{1,4})|=4^2=16,
\]
and its additive central factor is the four-dimensional elementary abelian \(2\)-group.

## Verification

The included replay constructs the algebra multiplication directly and exhaustively checks the theorem for
\[
(q,r)=(2,1),(2,2),(2,3),(3,1),(3,2),(4,1),(4,2).
\]
The \(\mathbf F_4\) cases use the polynomial realization
\[
\mathbf F_4=\mathbf F_2[t]/(t^2+t+1).
\]

For each case, the replay independently:

- enumerates every algebra element;
- computes products and additive commutators from the multiplication law;
- constructs every element-centralizer as an explicit set;
- verifies that there are exactly \(q^r+2\) distinct centralizers;
- verifies the predicted centralizer-size multiset;
- enumerates every commutator fiber;
- verifies the zero-fiber and nonzero-fiber formulas;
- verifies the commuting probability.

It also checks directly that \(A_{2,2}\) and \(A_{1,4}\) both have six centralizers but probabilities \(7/16\) and \(19/64\).

The replay returns `VERIFY_OK`.

Finite enumeration is not used to prove the theorem.

## Relationship to prior work

Dutta, Basnet, and Nath study commuting probabilities through the number of distinct element-centralizers. Their 2018 paper defines \(n\)-centralizer finite rings, computes exact probabilities in several small-\(n\) situations, and proves the general prime-rank-two case in which the additive central factor is \(C_p^2\). For \(6\)-centralizer rings, their explicit probability theorem excludes two possible central-factor types, one of which is \(C_2^4\).

The present theorem treats the standard generalized Kronecker path algebras uniformly for all finite fields and all arrow multiplicities. Except at the prime-field one-arrow boundary, their additive central factors have higher elementary-abelian rank than the rank-two case. The exact centralizer geometry has two different proper centralizer sizes, and the full commutator fibers are determined, not just the zero fiber.

The specialization \(A_{1,4}\) has additive central factor \(C_2^4\), is \(6\)-centralizer, and has commuting probability \(19/64\). Thus it supplies an explicit value in one of the central-factor cases left outside the 2018 paper's displayed \(6\)-centralizer probability list.

More generally, the divisor construction shows that the integer \(n=|\operatorname{Cent}(R)|\) does not determine \(\operatorname{Pr}(R)\): the same value \(p^M+2\) supports several distinct probabilities inside a single natural path-algebra family.

Searches using the phrases “commuting probability”, “Kronecker algebra”, “path algebra”, “radical square zero”, “\(6\)-centralizer”, “\(C_2^4\)”, “\(19/64\)”, and “commutator distribution” did not locate the theorem, its centralizer decomposition, or the \(19/64\) specialization.

## Limitations

The theorem concerns the path algebra of the two-vertex quiver with parallel arrows all in one direction. More general radical-square-zero algebras can have several vertices and a genuinely matrix-valued commutator constraint.

The result does not classify all \(n\)-centralizer finite rings and does not determine all possible commuting probabilities for a fixed \(n\).

A structurally equivalent statement could exist in the literature under bilinear-map or isoclinism terminology not captured by the searches.

The numerical \(6\)-centralizer specialization is a consequence of the uniform theorem; it is not claimed to complete the full classification of all \(6\)-centralizer rings.

## References

1. J. Dutta, D. K. Basnet, and R. K. Nath, “Commuting probabilities of \(n\)-centralizer finite rings,” arXiv:1803.04111v1, first public version 12 March 2018. Primary MSC 16U70, 16U80.
2. J. Liu, “Dimension vectors of elementary modules of generalized Kronecker quivers,” arXiv:2304.04182v1, first public version 9 April 2023; *Communications in Algebra* 51 (2023), 4223–4233. This source records the standard generalized Kronecker family as the quiver with two vertices and parallel arrows.
