# Classification of nested consecutive-pair six-term square-difference identities

## Finding
Let \(\mathcal F(a,b)=|a^2-b^2|\). Suppose two affine triples are each reduced by first combining a consecutive pair, and suppose their outputs agree for every integer \(x\):
\[
\mathcal F(\mathcal F(x+a,x+a+1),x+c)=\mathcal F(\mathcal F(x+A,x+A+1),x+C).
\]
If the two triples are not identical, then after translating all offsets by \(-a\), there is an integer \(q\) for which the identity is exactly
\[
\mathcal F(\mathcal F(x,x+1),x+2-3q)
=
\mathcal F(\mathcal F(x+2q-1,x+2q),x+5q-2)
=
3|(x+1-q)(x+3q-1)|.
\]
Thus the complete normalized offset family is
\[
P_q=\{{0,1,2-3q,2q-1,2q,5q-2\}},
\]
which is a translate of the centrally symmetric set
\[
\{{\pm q,\pm(q-1),\pm(4q-2)\}}.
\]
The six offsets are distinct exactly for \(q\notin\{{0,1\}}\). Interchanging the two triples replaces \(q\) by \(1-q\), so these two parameters describe the same shape. Among six-distinct members, the minimum span is \(12\), attained exactly at \(q=-1\) and \(q=2\). This minimum member is, up to translation,
\[
\{{0,4,5,7,8,12\}},
\]
the six-term translation-invariant identity already displayed by Hickerson and Kleber in 1999. The six-term identity used by Shen and Wu in 2026 is the \(q=3\) member (equivalently \(q=-2\) after swapping), whose translated offset set is \(\{{0,7,8,12,13,20\}}\) and whose span is \(20\).

## Assumptions and scope
The classification concerns exactly the natural nested architecture above: each of two three-element groups contains one consecutive pair, that pair is reduced first, and the resulting number is then reduced with the third entry. It does not classify arbitrary six-element reduction trees. Repeated offsets are allowed algebraically, but the span statement concerns six distinct offsets. The result does not alter the already established classification of interval lengths reducible to zero.

## Proof
Write \(u=2a+1\), \(v=c\), \(u'=2A+1\), and \(v'=C\). Before the outer absolute value, the two nested reductions are represented by
\[
Q_{u,v}(x)=(2x+u)^2-(x+v)^2
=3x^2+(4u-2v)x+(u^2-v^2),
\]
and similarly for \(Q_{u',v'}\).

If the absolute values agree for every integer \(x\), then \(Q_{u,v}(x)^2-Q_{u',v'}(x)^2\) vanishes at infinitely many integers. Hence
\((Q_{u,v}-Q_{u',v'})(Q_{u,v}+Q_{u',v'}))\) is the zero polynomial. The sum has leading coefficient \(6\), so it is not the zero polynomial; therefore \(Q_{u,v}=Q_{u',v'}\).

Equality of the linear coefficients gives
\[
2u-v=2u'-v'=k.
\]
Thus \(v=2u-k\) and \(v'=2u'-k\). Equality of constant terms becomes
\[
(u-u')\bigl(4k-3(u+u')\bigr)=0.
\]
The first factor would make \(u=u'\), and then the common linear coefficient also gives \(v=v'\), the excluded identical-triple case. Hence
\[
3(u+u')=4k.
\]
Since \(u,u',k\) are integers, \(3\mid k\); write \(k=3t\). Then
\[
A=2t-a-1,\qquad c=4a+2-3t,\qquad C=5t-4a-2.
\]
After translating offsets by \(-a\) and putting \(q=t-a\), this is exactly \(P_q\). Direct factorization gives the common output
\[
(2x+1)^2-(x+2-3q)^2
=3(x+1-q)(x+3q-1),
\]
and the second triple gives the same factorization.

For distinctness, each offset is an affine function of \(q\). Solving all pairwise equalities shows that an integer collision occurs only for \(q=0\) or \(q=1\). Also
\[
P_q-q=\{{\pm q,\pm(q-1),\pm(4q-2)\}},
\]
which proves central symmetry and makes the involution \(q\leftrightarrow1-q\) transparent. For \(q\ge2\), the minimum and maximum offsets are \(2-3q\) and \(5q-2\), so the span is \(8q-4\). For \(q\le-1\), they are \(5q-2\) and \(2-3q\), so the span is \(4-8q\). The least possible value is therefore \(12\), exactly at \(q=2\) and \(q=-1\).

## Verification
`verify_identity_family.py` checks the coefficient algebra, all integral pair-collision parameters, the involution \(q\leftrightarrow1-q\), the span formulas, the Hickerson--Kleber and Shen--Wu specializations, and direct integer evaluations over a broad deterministic grid. A successful replay prints `VERIFY_OK`.

## Relationship to prior work
Hickerson and Kleber (1999), Section 4, equation (4.0), give the translation-invariant six-term pattern \(\{{n-6,n-2,n-1,n+1,n+2,n+6\}}\), which is the minimum-span \(q=2\) member of this classification. Their paper also uses it twice inside the length-60 construction. Shen and Wu (2026), Lemma 3.1, use \(\{{x,x+7,x+8,x+12,x+13,x+20\}}\), which is the \(q=3\) member, as the six-element identity in their proof for 36 consecutive integers. Neither inspected source states the one-parameter classification, the \(q\leftrightarrow1-q\) equivalence, or the minimum-span uniqueness within this nested consecutive-pair architecture.

## Limitations
The originality conclusion is relative to the inspected primary sources and targeted semantic/web searches; an unindexed equivalent parametrization may exist. The result classifies one natural reduction-tree architecture, not all universal six-term reductions. The smaller 1999 member is not new and is explicitly credited as prior work. No new reduction of a consecutive interval is claimed.

## References
1. D. Hickerson and M. Kleber, “Reducing a Set by Subtracting Squares,” *Journal of Integer Sequences* 2 (1999), Article 99.1.4, especially Section 4, equation (4.0).
2. Z. Shen and Y. Wu, “Reducing Every Set of 36 Consecutive Integers to Zero by Differences of Squares,” arXiv:2609.00098v1 (2026), especially Lemma 3.1.
