# Three exact phases of generalized Frobenius numbers for three consecutive denominations

## Finding

For every integer \(a\ge 3\), let \(h=\lfloor a/2\rfloor\), and let \(g_p\) be the largest nonnegative integer admitting at most \(p\) ordered nonnegative representations using the three denominations \(a,a+1,a+2\). For every integer \(0\le p\le 2a\), the following complete three-regime formula holds:

\[
 g_p=\begin{cases}
 a(h+p)+2p-1,&0\le p\le h,\\
 a(h+p+1)-1,&h+1\le p\le a+1,\\
 a(h+a+2+j+e)+2j+1,& p=a+2+2j+e\le 2a,\quad e\in\{0,1\},\ j\ge0.
 \end{cases}
\]

The first regime is the known consecutive-denomination specialization of Komatsu–Ying, Theorem 1. The claimed extension is the second and third regimes, which extend beyond their boundary \(p=h\). The exact transition from increments \(a+2\) to increments \(a\), followed by an alternating two-step pattern, persists uniformly for arbitrarily large \(a\).

## Assumptions and scope

Fix an integer \(a\ge3\), let \(d_a(n)\) denote the number of triples \((x,y,z)\in\mathbb Z_{\ge0}^3\) satisfying \(ax+(a+1)y+(a+2)z=n\), and set \(g_p=\max\{n\in\mathbb Z_{\ge0}:d_a(n)\le p\}\). Since the generators have gcd one, the maximum exists. All variables \(a,p,j\) are integers in the ranges in the displayed theorem; \(e\) is the unique remainder of \(p-a-2\) upon division by two in the final regime. No assertion is made for \(p>2a\) or for nonconsecutive progressions.

## Proof

**Elementary counting formula.** Write \(n=aq+r\), with \(q\ge0\), \(0\le r<a\). In a representation put \(s=x+y+z\). Then \(n=as+y+2z\), hence \(s=q-t\) and \(y+2z=r+at\) for a unique nonnegative integer \(t\). With \(u=r+at\), the number of solutions at that value of \(t\) is
\[
 F(q,r;t)=\begin{cases}
 \lfloor u/2\rfloor-\max(0,u-(q-t))+1,&0\le u\le 2(q-t),\\
 0,&\text{otherwise}.
 \end{cases}
\]
Thus \(d_a(aq+r)=\sum_{t\ge0} F(q,r;t)\). Only finitely many terms occur. Appending one coin of denomination \(a\) injects the representation set of \(n\) into that of \(n+a\), so \(d_a(n+a)\ge d_a(n)\). Therefore, to prove a proposed value \(G=g_p\), it suffices to verify \(d_a(G)=p\) and \(d_a(G+r)>p\) for all \(1\le r\le a\): all larger numbers are congruent modulo \(a\) to one of these \(a\) successors and have no fewer representations. We perform these checks below, using \(a=2h+b\) with \(b\in\{0,1\}\).

**First regime, \(0\le p\le h\).** Let \(G=a(h+p)+2p-1\). For \(p\ge1\), its quotient and remainder are \((h+p,2p-1)\); only the \(t=0\) summand survives and has value \(p\). For \(p=0\), its quotient and remainder are \((h-1,a-1)\) and every summand vanishes. If \(p\ge1\), among the next \(a\) integers the same-quotient residues \(2p\le r\le a-1\) have \(F(q,r;0)\ge p+1\). The next-quotient residues \(0\le r\le2p-1\), where \(q=h+p+1\), have \(F(q,r;0)+F(q,r;1)=p+2-(r\bmod2)\) if \(b=0\), or \(p+1\) if \(b=1\). For \(p=0\), the next \(a\) values have quotient \(h\) and a positive \(t=0\) summand. Thus each successor has at least \(p+1\) representations. This recovers the known formula, independently.

**Second regime, \(h+1\le p\le a+1\).** Put \(t=p-h\), so \(1\le t\le h+b+1\), and \(G=a(h+p+1)-1\). At \(G\) the quotient and remainder are \((h+p,a-1)\). The nonzero contributions are \(F(q,r;0)=h+b\) and \(F(q,r;1)=t-b\) (allowing zero), hence \(d_a(G)=p\).

For all its \(a\) successors, write \(n=aQ+r\) with \(Q=h+p+1\), \(0\le r<a\). The only possible summands are
\[
\begin{aligned}
F(Q,r;0)&=\lfloor r/2\rfloor+1,\\
F(Q,r;1)&=\begin{cases}
 h+\lfloor(b+r)/2\rfloor+1,&r\le t-b,\\
 p+1-\lceil(b+r)/2\rceil,&r>t-b,
\end{cases}\\
F(Q,r;2)&=\max\{0,t-b-\lceil r/2\rceil\}.
\end{aligned}
\]
All \(F(Q,r;k)\) for \(k\ge3\) vanish. If \(b=0\) and \(r\le t\), the sum exceeds \(p+1\) by \(1+\lfloor r/2\rfloor-(r\bmod2)\ge0\); for \(r>t\), already the first two summands are \(p+2-(r\bmod2)\ge p+1\). If \(b=1\) and \(r\le t-1\), the sum is \(p+1+\lfloor r/2\rfloor\); for \(r\ge t\), the first two summands equal \(p+1\). Thus every successor is strictly above level \(p\).

**Third regime, \(a+2\le p\le2a\).** Write uniquely \(p=a+2+2j+e\) with \(j\ge0\) and \(e\in\{0,1\}\), and set \(q_0=h+a+2+j+e\) and \(G=aq_0+2j+1\). In the stated range \(2j+1<a\), so this is its quotient-remainder decomposition. At \(G\) the \(t=0,1,2,3\) contributions are respectively
\[
 j+1,\qquad h+j+b+1,\qquad h+e,\qquad0.
\]
No higher \(t\) contributes, and their sum is exactly \(p=a+2+2j+e\).

Its \(a\) successors occur in two disjoint groups. In the first group \(n=aq_0+r\), with \(2j+2\le r<a\). The three possibly nonzero contributions are
\[
\begin{aligned}
 F(q_0,r;0)&=\lfloor r/2\rfloor+1,\\
 F(q_0,r;1)&=\begin{cases}
 h+\lfloor(b+r)/2\rfloor+1,&r\le h+j+e+1,\\
 a+j+e+2-\lceil(b+r)/2\rceil,&r>h+j+e+1,
 \end{cases}\\
 F(q_0,r;2)&=h+j+e+1-\lceil r/2\rceil .
\end{aligned}
\]
All higher summands vanish. Subtracting \(p+1\) from their sum gives, for the low-\(r\) and high-\(r\) subcases respectively,
\[
\begin{array}{c|cc}
 &r\le h+j+e+1&r>h+j+e+1\\\hline
 b=0&\lfloor r/2\rfloor-j-(r\bmod2)&h+e+1-\lceil r/2\rceil-(r\bmod2)\\
 b=1&\lfloor r/2\rfloor-j-1&h+e-\lceil r/2\rceil
\end{array}
\]
Each expression is nonnegative: use \(r\ge2j+2\), the displayed subcase inequality, and \(r\le2h+b-1\). In the second group \(n=a(q_0+1)+r\), with \(0\le r\le2j+1\), the four contributions are
\[
\begin{aligned}
F(q_0+1,r;0)&=\lfloor r/2\rfloor+1,\\
F(q_0+1,r;1)&=h+\lfloor(b+r)/2\rfloor+1,\\
F(q_0+1,r;2)&=h+j+e+2-\lceil r/2\rceil,\\
F(q_0+1,r;3)&=\begin{cases}j+e+1-\lceil r/2\rceil,&b=0,\\ j+e-\lfloor r/2\rfloor,&b=1.
\end{cases}
\end{aligned}
\]
All further contributions vanish. Here \(d_a(n)-(p+1)=e+2-2(r\bmod2)\ge0\) if \(b=0\), and equals \(e\ge0\) if \(b=1\). Thus all \(a\) successors of \(G\) admit more than \(p\) representations. Monotonicity along residue classes establishes the formula for all larger \(n\). This concludes the proof. \(\square\)

## Verification

A standalone exact-integer dynamic program, included as `verify.py`, recomputes the number of representations using the generating-function recurrence for each of the three denominations. For every integer \(3\le a\le120\) and every \(0\le p\le2a\), it checks the proposed \(G\) against all representation counts from zero through the largest candidate plus \(a\), and confirms \(G\) is exactly the last \(n\) with \(d_a(n)\le p\). The check spans 14,632 parameter pairs. A second independently coded enumeration verifies explicit triples in 3,374 small cases. Finite checks corroborate but are not an infinite proof; the proof above derives the inequalities for every parameter within scope.

To reproduce, run `python3 verify.py` using Python 3 standard library.

## Relationship to prior work

Komatsu and Ying [1, Theorem 1] proved a general arithmetic-progression formula only for \(0\le p\le\lfloor a/2\rfloor\); the first displayed line is their specialization to \(d=1\), not a novel claim. Their final section [1, Section 7] explicitly asks for convenient formulas beyond that parameter range. The second and third lines give a uniform answer for the consecutive-coin case, through \(p=2a\). Their Apéry-table method does not itself state these lines.

Subwattanachai [2, Theorem 1] provides a three-denomination formula under a divisibility hypothesis on one denomination by another after a pairwise-gcd reduction. This hypothesis does not hold for \((a,a+1,a+2)\) with \(a\ge3\), and its specialized representation-count levels therefore do not cover the theorem. General large-parameter methods cited in [2] have not been established to imply these explicit small-to-linear parameter phase transitions. No equivalent exact three-phase statement was identified in the inspected source texts or related-index searches; this is not a universal priority guarantee.

## Limitations

Only consecutive triples with \(a\ge3\) and levels \(0\le p\le2a\) are classified; the case \(p>2a\), arbitrary progression step, and full formulas for genus or gap sums are open here. An independent mathematical audit has not been performed. Equivalent results in unindexed literature remain a residual originality risk.

## References

[1] Takao Komatsu and Haotian Ying, *The p-numerical semigroup of the triple of arithmetic progressions*, arXiv:2206.13052 (first submitted 27 June 2022), Theorem 1 and Section 7. https://arxiv.org/abs/2206.13052

[2] Kittipong Subwattanachai, *Generalized Frobenius Number of Three Variables*, arXiv:2309.09149 (first submitted 17 September 2023), Theorem 1 and Remark 2. https://arxiv.org/abs/2309.09149
