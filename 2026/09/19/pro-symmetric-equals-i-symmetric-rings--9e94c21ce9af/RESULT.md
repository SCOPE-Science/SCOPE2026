# Pro-symmetric rings coincide with I-symmetric rings

Let \(R\) be an associative unital ring. Write \(E(R)\) for its idempotents and \(U(R)\) for its unit group. Following Alghazzawi--Leroy, a subset \(S\subseteq R\) is **symmetric** if
\[
abc\in S\quad\Longrightarrow\quad acb\in S
\]
for all \(a,b,c\in R\). Han--Lee--Lee call a ring **I-symmetric** when \(E(R)\) is a symmetric subset. For a ring with involution \(*\), Chen--Wang--Zou call \(R\) **pro-symmetric** when
\[
abc\in P(R)\quad\Longrightarrow\quad acb\in P(R),
\]
where \(P(R)=\{p:p^2=p=p^*\}\).

## Theorem

For every unital ring \(R\), the following are equivalent.

1. \(R\) is I-symmetric.
2. \(R\) is symmetric and \(U(R)\) is abelian.
3. For all \(a,b,c\in R\), if \(abc\in E(R)\), then
   \[
   acb=abc.
   \]

If \(R\) is equipped with any involution \(*\), these are also equivalent to:

4. \((R,*)\) is pro-symmetric.

Consequently, pro-symmetry is independent of the chosen involution: a unital ring admitting involutions is pro-symmetric for one involution if and only if it is pro-symmetric for every involution. Equivalently, the projection-based class introduced in arXiv:2609.20084 is precisely the pre-existing I-symmetric class.

### Proof

The equivalence of (1) and (3) is Proposition 3.13 of Chen--Wang--Zou: their "Condition 2" is exactly that \(E(R)\) is a symmetric subset. Their Proposition 3.2 also shows that I-symmetry implies ordinary symmetry.

It remains to isolate the unit-group condition.

**(1) implies (2).** Let \(u,v\in U(R)\). Put
\[
a=v^{-1}u^{-1},\qquad b=u,\qquad c=v.
\]
Then \(abc=1\in E(R)\). I-symmetry gives
\[
q:=acb=v^{-1}u^{-1}vu\in E(R).
\]
But \(q\) is a unit, and an invertible idempotent is \(1\). Hence \(q=1\), so \(uv=vu\). Thus \(U(R)\) is abelian.

**(2) implies (3).** Let \(p=abc\in E(R)\), and put \(q=acb\). A symmetric ring is reversible, and a reversible ring has central idempotents; hence \(p\) is central.

From
\[
(1-p)abc=0
\]
symmetry gives
\[
(1-p)acb=0,
\]
so \(pq=q\). Likewise, from \(abc(1-p)=0\), symmetry applied to the triple \(a,b,c(1-p)\) gives
\[
ac(1-p)b=0.
\]
Since \(p\) is central, this is \(q(1-p)=0\), so \(qp=q\). Therefore \(q\in pRp\).

Work now in the corner \(S=pRp\), whose identity is \(p\), and set
\[
A=pap,\qquad B=pbp,\qquad C=pcp.
\]
Because \(p\) is central,
\[
ABC=p,
\qquad
q=ACB.
\]
The corner \(S\) is reversible, hence directly finite. Indeed, if \(xy=p\) in \(S\), then
\[
x(p-yx)=0;
\]
reversibility gives \((p-yx)x=0\), and multiplying on the right by \(y\) yields \(yx=p\).

Since \(ABC=p\), direct finiteness first shows that \(AB\) and \(C\) are units of \(S\), and then that \(A\) and \(B\) are units as well. Because \(p\) is central, the map
\[
U(S)\longrightarrow U(R),\qquad x\longmapsto x+(1-p)
\]
is an injective group homomorphism. The group \(U(R)\) is abelian, so \(U(S)\) is abelian. Hence \(A,B,C\) commute and
\[
q=ACB=ABC=p.
\]
This proves (3).

Finally suppose \(R\) carries an involution. If (3) holds and \(abc\in P(R)\), then \(abc\in E(R)\) and therefore \(acb=abc\in P(R)\); hence \((R,*)\) is pro-symmetric. Conversely, if \((R,*)\) is pro-symmetric, Chen--Wang--Zou Proposition 4.1 implies that \(R\) is symmetric. For units \(u,v\), the same substitution as above has \(abc=1\in P(R)\), so pro-symmetry makes \(q=v^{-1}u^{-1}vu\) a projection. Since \(q\) is a unit, \(q=1\), and therefore \(U(R)\) is abelian. Thus (2) holds. ∎

## Consequences

### Clean rings collapse to the commutative case

If \(R\) is clean and pro-symmetric (equivalently I-symmetric), then \(R\) is commutative. Indeed, symmetric rings have central idempotents, and the theorem gives an abelian unit group. Write arbitrary elements as
\[
x=e+u,\qquad y=f+v
\]
with \(e,f\) idempotent and \(u,v\) units. The idempotents commute with everything and the units commute with each other, hence \(xy=yx\). The converse is immediate. Thus
\[
\boxed{\text{clean pro-symmetric rings}=\text{commutative clean rings}.}
\]

### Division rings

Every division ring is symmetric. The theorem therefore gives
\[
\boxed{\text{a division \(*\)-ring is pro-symmetric iff it is a field}.}
\]
This explains uniformly why the quaternion division ring separates symmetry from pro-symmetry in arXiv:2609.20084.

### Noncommutative pro-symmetric rings exist

The clean hypothesis above cannot be omitted. Let
\[
R=\mathbb F_2\langle x,y\rangle
\]
with the word-reversal involution. This free associative algebra is a domain, hence symmetric. Its only units are the nonzero scalars, so over \(\mathbb F_2\) one has \(U(R)=\{1\}\). The theorem therefore makes \((R,*)\) pro-symmetric, although \(xy\ne yx\).

## Relation to prior literature

Alghazzawi--Leroy introduced symmetric subsets of rings, and their Proposition 3.11 shows that membership in a symmetric subset is preserved under arbitrary permutations of factors. Han--Lee--Lee subsequently studied the special case \(S=E(R)\) under the name I-symmetric rings. Their published abstract states, in particular, that for an abelian semiperfect ring, I-symmetry, commutativity of the unit group, and ring commutativity are equivalent.

Chen--Wang--Zou independently formulate the idempotent condition as "Condition 2" and introduce the projection-based pro-symmetric condition for \(*\)-rings. Their Proposition 3.13 proves that their idempotent condition forces equality of the two transposed triple products, while Section 4 develops pro-symmetry as an apparently involution-dependent strengthening of symmetry.

The contribution here is the general criterion
\[
\boxed{\text{I-symmetric}\iff\text{symmetric with abelian unit group},
\]
and its consequence
\[
\boxed{\text{pro-symmetric}\iff\text{I-symmetric},
\]
which removes the involution from the classification entirely.

## Limitations and originality qualification

The full body of Han--Lee--Lee, *Symmetry on zero and idempotents*, Communications in Algebra 51 (2023), 464--474, DOI 10.1080/00927872.2022.2102177, was not inspected. Its abstract was inspected and contains the closely related abelian-semiperfect special case described above. This is the principal residual originality risk: if the inaccessible body contains the unrestricted criterion "I-symmetric iff symmetric with abelian unit group", then that part of the present theorem would be prior art, while the identification with the 2026 pro-symmetric notion and its involution-independence would remain a new application unless separately covered.

To the best of our knowledge, targeted searches for the unrestricted criterion and for an identification of pro-symmetric rings with I-symmetric rings did not locate an earlier statement. The 2019 symmetric-subset paper and the 2026 arXiv source were inspected at the relevant definitions and propositions.

## References

1. H. Chen, L. Wang, H. Zou, *Transposed Triple Products and Pro-Symmetric Rings in \(*\)-Rings*, arXiv:2609.20084v1 (2026). https://arxiv.org/abs/2609.20084
2. D. Alghazzawi, A. Leroy, *Commutatively closed sets in rings*, Communications in Algebra 47 (2019), 1629--1641. DOI: 10.1080/00927872.2018.1513011.
3. J. Han, C. I. Lee, Y. Lee, *Symmetry on zero and idempotents*, Communications in Algebra 51 (2023), 464--474. DOI: 10.1080/00927872.2022.2102177.
4. D. Khurana, G. Marks, A. K. Srivastava, *On Unit-Central Rings*, in Advances in Ring Theory (2010), 205--212. DOI: 10.1007/978-3-0346-0286-0_13.
