# Unit rigidity characterizes pro-star-reversible rings — provenance-corrected presentation

## Status and provenance

The theorem below is correct, but this record is not a separate discovery of the unit-group criterion.

The broader SCOPE record
`2026/09/19/unit-group-criterion-pro-star-reversibility--dcd6bac06405`
was first committed at 2026-09-19T10:47:25Z and already proved the exact equivalence
\[
\text{pro-}*\text{-reversible}
\iff
\text{\(*\)-reversible and every unit is fixed by }*.
\]
An even earlier SCOPE record,
`2026/09/18/pro-star-reversible-semiperfect-rigidity--8cd8850c47f1`,
committed at 2026-09-18T22:24:59Z, already contained the unit-rigidity implication and the local/semiperfect collapse. This record was first committed later, at 2026-09-19T23:20:48Z.

Accordingly, the record is retained as an alternate proof and a compact collection of consequences. No separate originality or priority claim is made.

## Theorem

Let \(R\) be a unital ring with involution \(*\). Then the following are equivalent:

1. \(R\) is pro-\(*\)-reversible:
   \[
   ab\in P(R)\Longrightarrow b^*a\in P(R).
   \]
2. \(R\) is \(*\)-reversible and every unit is self-adjoint:
   \[
   ab=0\Longrightarrow b^*a=0,\qquad u^*=u\quad(u\in U(R)).
   \]

Under these equivalent conditions, if \(ab=p\in P(R)\), then in fact
\[
b^*a=p.
\]

Consequently the unit group is abelian. Every local or clean pro-\(*\)-reversible ring is commutative with the identity involution, and a division \(*\)-ring is pro-\(*\)-reversible exactly when it is a field with the identity involution.

## Proof

Assume first that \(R\) is pro-\(*\)-reversible. Chen--Wang--Zou prove that pro-\(*\)-reversibility implies \(*\)-reversibility. For \(u\in U(R)\), take \(a=u^{-1}\) and \(b=u\). Then \(ab=1\) is a projection, so
\[
u^*u^{-1}\in P(R).
\]
It is also a unit. The only invertible idempotent is \(1\), hence \(u^*=u\).

Conversely, assume \(R\) is \(*\)-reversible and every unit is fixed. Let \(p=ab\in P(R)\). A \(*\)-reversible ring is reversible; in a reversible ring idempotents are central, and the standard idempotent-product lemma gives \(ba=p\). Put \(q=1-p\).

Because
\[
(qa)(qb)=qab=0,
\]
\(*\)-reversibility gives
\[
qb^*a=0. \tag{1}
\]
In the corner \(pRp\), the elements \(A=pa\) and \(B=pb\) are inverse units. Thus \(B+q\) is a unit of \(R\), with inverse \(A+q\). By hypothesis \(B+q\) is self-adjoint, so \(B^*=B\). Therefore
\[
pb^*a=B^*A=BA=p. \tag{2}
\]
Adding (1) and (2) yields \(b^*a=p\), proving pro-\(*\)-reversibility.

If \(u,v\) are units, then \(u,v,uv\) are fixed by the involution, so
\[
uv=(uv)^*=v^*u^*=vu.
\]
Hence \(U(R)\) is abelian.

For a local ring, each \(x\) or \(1-x\) is a unit, so the unit criterion forces \(x^*=x\) for every \(x\); anti-multiplicativity then forces commutativity. For a clean ring, write \(x=e+u\); idempotents in a unital \(*\)-reversible ring are self-adjoint and units are fixed, so again \(x^*=x\). The division-ring statement is immediate because every nonzero element is a unit.

Noncommutative examples exist outside the clean setting: the free associative algebra \(k\langle x,y\rangle\), with word-reversal involution fixing \(k,x,y\), is a domain whose units are the nonzero scalars; the criterion therefore makes it pro-\(*\)-reversible.

## Scientific role of this record

The mathematics is useful as a short proof and as a convenient collection of local, clean, and division consequences. Its scientific value is corroborative and expository relative to the earlier SCOPE records above. The original external source, Chen--Wang--Zou, introduced pro-\(*\)-reversibility and did not state the pointwise unit-group criterion in the public version inspected.

## References

1. H. Chen, L. Wang, H. Zou, *On \(*\)-Reversible and Generalized \(*\)-Reversible Rings*, arXiv:2609.20076 (2026).
2. A. H. Fakieh, *Reversible Rings with Involutions and Some Minimalities*, The Scientific World Journal (2013), Article 650702.
3. SCOPE record `2026/09/19/unit-group-criterion-pro-star-reversibility--dcd6bac06405`, first committed 2026-09-19T10:47:25Z.
4. SCOPE record `2026/09/18/pro-star-reversible-semiperfect-rigidity--8cd8850c47f1`, first committed 2026-09-18T22:24:59Z.
