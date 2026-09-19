# Unit rigidity characterizes pro-star-reversible rings

## Statement

Let \(R\) be an associative unital ring equipped with an involution \(*\). Write
\[
U(R)=\{u\in R:\ u\text{ is invertible}\}
\]
and let \(P(R)\) denote the projections of \(R\).

Recall that \(R\) is **\(*\)-reversible** if
\[
ab=0\quad\Longrightarrow\quad b^*a=0,
\]
and is **pro-\(*\)-reversible** if
\[
ab\in P(R)\quad\Longrightarrow\quad b^*a\in P(R).
\]

Then the following are equivalent:

1. \(R\) is pro-\(*\)-reversible.
2. \(R\) is \(*\)-reversible and every unit is fixed by the involution:
   \[
   u^*=u\qquad(u\in U(R)).
   \]

Equivalently, among \(*\)-reversible rings, pro-\(*\)-reversibility is exactly the additional requirement
\[
U(R)\subseteq \operatorname{Sym}(R,*).
\]

Consequently, every pro-\(*\)-reversible ring has abelian unit group.

## Proof

### Necessity

The implication
\[
\text{pro-}*\text{-reversible}\Longrightarrow *\text{-reversible}
\]
is Proposition 3.5 of Chen--Wang--Zou, arXiv:2609.20076v1.

Now let \(u\in U(R)\). Put
\[
a=u^{-1},\qquad b=u.
\]
Then
\[
ab=1\in P(R).
\]
By pro-\(*\)-reversibility,
\[
b^*a=u^*u^{-1}\in P(R).
\]
The element \(u^*u^{-1}\) is also a unit. A unit that is idempotent must equal \(1\). Hence
\[
u^*u^{-1}=1,
\]
and therefore
\[
u^*=u.
\]

### Sufficiency

Assume now that \(R\) is \(*\)-reversible and every unit of \(R\) is fixed by \(*\). Let
\[
p=ab\in P(R).
\]

A \(*\)-reversible ring is reversible. In a reversible ring every idempotent is central, and Lemma 3.1 of Chen--Wang--Zou gives
\[
ba=ab=p.
\]
Set
\[
q=1-p.
\]
Then \(p,q\) are central projections.

First isolate the \(q\)-corner. Since
\[
(qa)(qb)=qab=qp=0,
\]
\(*\)-reversibility gives
\[
(qb)^*(qa)=qb^*a=0.
\]
Thus
\[
qb^*a=0. \tag{1}
\]

Now work in the corner \(pRp\), whose identity is \(p\). Define
\[
A=pa,\qquad B=pb.
\]
Centrality of \(p\) and \(ab=ba=p\) give
\[
AB=BA=p.
\]
Hence \(A\) and \(B\) are mutually inverse units of \(pRp\). In the whole ring,
\[
B+q
\]
is a unit with inverse \(A+q\). By hypothesis every unit is fixed by the involution, so
\[
(B+q)^*=B+q.
\]
Since \(q^*=q\), this yields \(B^*=B\). Therefore
\[
pb^*a=B^*A=BA=p. \tag{2}
\]

Combining (1) and (2),
\[
b^*a=(p+q)b^*a=p.
\]
Thus \(b^*a\) is a projection. Hence \(R\) is pro-\(*\)-reversible.

This proves the equivalence.

Finally, if \(u,v\in U(R)\), then \(u,v,uv\) are all fixed by \(*\). Hence
\[
uv=(uv)^*=v^*u^*=vu,
\]
so \(U(R)\) is abelian.

## Consequences

### Local rings

A local ring is clean. More directly, for every \(x\in R\), either \(x\) or \(1-x\) is a unit. If \(R\) is pro-\(*\)-reversible, the theorem fixes every unit. Therefore:

- if \(x\) is a unit, then \(x^*=x\);
- if \(1-x\) is a unit, then
  \[
  1-x=(1-x)^*=1-x^*,
  \]
  so again \(x^*=x\).

Thus the involution is the identity on all of \(R\). Since an involution is anti-multiplicative,
\[
xy=(xy)^*=y^*x^*=yx.
\]
Hence:

\[
\boxed{\text{A local }*\text{-ring is pro-}*\text{-reversible}
\iff
R\text{ is commutative and }*= \mathrm{id}.}
\]

The reverse implication is immediate.

### Division rings

Every nonzero element of a division ring is a unit. Hence the theorem immediately gives
\[
\boxed{\text{A division }*\text{-ring is pro-}*\text{-reversible}
\iff
R\text{ is a field and }*=\mathrm{id}.}
\]

### Clean rings

A 2013 result of Fakieh shows that every idempotent of a unital \(*\)-reversible ring is fixed by the involution. In a clean pro-\(*\)-reversible ring, the theorem also fixes every unit. If
\[
x=e+u
\]
with \(e^2=e\) and \(u\in U(R)\), then
\[
x^*=e^*+u^*=e+u=x.
\]
Thus \(*=\mathrm{id}\), and the ring is commutative. Therefore
\[
\boxed{\text{A clean }*\text{-ring is pro-}*\text{-reversible}
\iff
R\text{ is commutative and }*=\mathrm{id}.}
\]

### Noncommutative examples still exist

The clean hypothesis cannot be dropped. Let
\[
R=k\langle x,y\rangle
\]
be the free associative algebra on two generators, with the word-reversal involution fixing \(k,x,y\). This is a domain, hence \(*\)-reversible. Its units are precisely the nonzero scalars, all fixed by the involution. The theorem therefore implies that \(R\) is pro-\(*\)-reversible, although \(R\) is noncommutative.

## Relation to the 2026 preprint

Chen--Wang--Zou introduce pro-\(*\)-reversibility in arXiv:2609.20076v1, prove that it implies \(*\)-reversibility, and exhibit a \(*\)-reversible ring that is not pro-\(*\)-reversible. Their Question 3.7 asks whether every \(*\)-reversible ring is pro-\(*\)-reversible; Example 3.13 answers this negatively.

The theorem above gives the sharp extension criterion left after that counterexample:
\[
\boxed{
R\text{ \(*\)-reversible is pro-\(*\)-reversible}
\iff
*\text{ fixes }U(R)\text{ pointwise}.
}
\]
For the ring in their Example 3.13, the displayed unit
\[
\begin{pmatrix}1&1\\0&1\end{pmatrix}
\]
is moved by the involution, so the criterion detects the failure immediately.

## Originality and limitations

The notion of pro-\(*\)-reversibility appears to have been introduced in arXiv:2609.20076v1. Targeted searches for equivalent formulations involving fixed units, self-adjoint units, projections, and \(*\)-reversibility did not locate the criterion above.

The proof is elementary once the unit substitution \(u^{-1}u=1\) is noticed, so independent prior or concurrent discovery is a meaningful residual risk. Older literature on \(*\)-reversible rings already contains the facts that such rings are reversible and that their idempotents are fixed by the involution; those facts are treated here as prior art. The claimed contribution is the exact unit-fixed characterization of the new pro-\(*\)-reversible class and its clean/local/division consequences.

No independent validation is asserted.

## References

1. H. Chen, L. Wang, H. Zou, *On \(\ast\)-Reversible and Generalized \(\ast\)-Reversible Rings*, arXiv:2609.20076v1, 17 September 2026. https://arxiv.org/abs/2609.20076
2. A. Fakieh, *Reversible Rings with Involutions and Some Minimalities*, The Scientific World Journal (2013), Article ID 650702. https://doi.org/10.1155/2013/650702
