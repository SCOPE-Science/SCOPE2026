# Arbitrarily many exactly classified best greedy Egyptian triples

## Finding

For every odd integer \(q\ge3\), set
\[
 a=\frac{q+1}{2},\qquad b=aq,\qquad L=6qab,\qquad c=L^2+1,\qquad Q=qc,
\]
\[
 S=\frac2q+\frac1c,\qquad
 \theta=S+\frac{1}{72Q^2a^2b^2}.
\]
The ordinary greedy Egyptian underapproximation of \(\theta\), taking the largest admissible reciprocal at each of the first three steps with strict inequality, is \((a,b,c)\). It is also a **best** three-term underapproximation: no nondecreasing triple of integers \(2\le x\le y\le z\) has reciprocal sum strictly between \(S\) and \(\theta\).

More precisely, **all** nondecreasing three-term representations of its maximal sum \(S\) are
\[
 \left(\frac{q+d}{2},\frac{q+q^2/d}{2},c\right),
 \qquad d\mid q^2,\quad 1\le d\le q.
\]
Consequently, the number of best denominator triples is exactly
\[
 \frac{\tau(q^2)+1}{2}
\]
when repeated denominators are permitted. Exactly
\[
 \frac{\tau(q^2)-1}{2}
\]
of these triples have strictly increasing denominators, and the greedy triple belongs to that strictly increasing class. Here \(\tau\) is the positive-divisor counting function. Taking \(q\) to be a product of \(t\) different odd primes gives respectively \((3^t+1)/2\) and \((3^t-1)/2\) **best** triples. In particular, the multiplicity of a best greedy three-term underapproximation is unbounded, even under the distinct-denominator convention.

## Assumptions and scope

All integer parameters are exact. The target \(\theta\) is a rational in \((0,1)\). Under Nathanson's convention, an admissible three-term denominator tuple satisfies \(2\le x\le y\le z\) and \(1/x+1/y+1/z<\theta\). The 'distinct' variant replaces the weak inequalities by strict ones. 'Best' means the largest achievable strict underapproximation sum for exactly three terms, not the nearest rational of arbitrary unit-fraction length. Only the explicitly constructed family of targets is claimed. There is no claim that all three-denominator best approximations are always greedy, nor that the multiplicity above bounds the number for general targets.

## Proof

**1. Greedy denominators.** For \(q\ge3\) odd, \(a\ge2\), \(a<b<c\), \(b=aq\ge a^2-a+1\), and \(c=L^2+1\ge b^2-b+1\). Since \(\theta-S=1/(72Q^2a^2b^2)\) lies strictly between zero and \(1/(c(c-1))\), the standard greedy interval criterion (Nathanson, Theorem 2) gives the greedy tuple \((a,b,c)\). Alternatively, the inequalities \(1/a<\theta\le1/(a-1)\), \(1/b<\theta-1/a\le1/(b-1)\), and \(1/c<\theta-1/a-1/b\le1/(c-1)\) follow successively from those growth inequalities. The identity \(1/a+1/b=2/q\) is exact.

**2. The rational \(S\) has no one- or two-term unit-fraction representation.** It lies strictly between \(1/a\) and \(1/(a-1)\), so is not a single unit fraction. Suppose \(S=1/x+1/y\) with integers \(2\le x\le y\). Because \(S<1/(a-1)\) and \(S>2/q\), necessarily \(a\le x<q\). Put \(k=2x-q\ge1\). The second denominator would be
\[
 y=\frac{qxc}{kc+qx},\qquad
 0<\frac{qx}{k}-y=\frac{(qx)^2}{k(kc+qx)}<\frac1k,
\]
where the final strict inequality uses \(c>(qx)^2\), since \(x<q\) and \(c>L^2\ge q^4\). But if \(y\) is an integer, the positive difference \((qx-ky)/k\) is at least \(1/k\). Contradiction.

**3. Exact classification of representations of \(S\).** Suppose \(1/x+1/y+1/z=S\) with \(2\le x\le y\le z\). Because \(1/x<S<1/(a-1)\) and \(S>1/a\), while \(S\le3/x\), we have \(a\le x<3a\). Moreover \(S\le1/x+2/y\) and \(S-1/x\ge S-1/a=1/b+1/c>1/b\), so \(y<2b\). Set
\[
 N=2xy-q(x+y)\in\mathbb Z,\quad R=qxy<6qab=L.
\]
Then \(1/z=1/c+N/R\), so \(z=Rc/(Nc+R)\). If \(N<0\), positivity forces \(c<R/|N|\le R<L<c\), impossible. If \(N>0\), comparing with the rational \(R/N\) yields
\[
 0<\frac RN-z=\frac{R^2}{N(Nc+R)}<\frac1N
\]
because \(c>L^2>R^2\). For integral \(z\), the positive difference \((R-Nz)/N\) is at least \(1/N\), again impossible. Hence \(N=0\), so \(z=c\) and \(1/x+1/y=2/q\). Equivalently \((2x-q)(2y-q)=q^2\). The positive odd divisors \(d=2x-q\le2y-q=q^2/d\) give precisely the displayed parameterization. Every such pair satisfies \(2\le x\le y\le b<c\), and conversely sums to \(2/q\). Since \(q^2\) is a square, its positive divisors pair off with one diagonal factor, giving \((\tau(q^2)+1)/2\) tuples. Exactly one pair is diagonal (\(x=y=q\)); all the other \((\tau(q^2)-1)/2\) have distinct denominators, and \(z=c\) differs from both.

**4. The common sum is best, not merely greedy.** Suppose another nondecreasing triple \((x,y,z)\) has sum \(T\) with \(S<T<\theta\). Since \(T<\theta\le1/(a-1)\), \(x\ge a\). From \(S<T\le3/x\) we obtain \(x<3a\). From \(T\le1/x+2/y\) and \(S-1/x\ge1/b+1/c\) we obtain \(y<2b\). Put \(H=1/x+1/y\) and recall \(Q=qc\) is an integer denominator for \(S\). Step 2 excludes \(H=S\). If \(H>S\), the positive rational \(H-S\) has numerator at least one over denominator \(Qxy\), hence
\[
 T-S\ge H-S\ge\frac1{Qxy}>\frac1{6Qab}>\theta-S,
\]
a contradiction. If \(H<S\), then \(S-H\ge1/(Qxy)>1/(6Qab)\); because \(T>S\), we have \(1/z>S-H\) and thus \(z<6Qab\). The positive rational \(T-S\) has denominator dividing \(Qxyz\); hence
\[
 T-S\ge\frac1{Qxyz}>
 \frac1{Q(3a)(2b)(6Qab)}
 =\frac1{36Q^2a^2b^2}=2(\theta-S),
\]
another contradiction. Therefore no admissible triple has a sum between \(S\) and \(\theta\) that exceeds \(S\). Every triple classified in Step 3 is a best three-term underapproximation of \(\theta\).

**5. Unbounded multiplicity.** If \(q\) is squarefree with exactly \(t\) different odd prime factors, \(\tau(q^2)=3^t\). Arbitrarily large \(t\) exist, giving both stated unbounded multiplicities.

## Verification

The attached stand-alone Python 3 checker uses `fractions.Fraction` and integer divisor enumeration. It checks the actual three greedy denominators and every divisor-supplied sum for ten odd values of \(q\). For eight smaller values it also enumerates every possible bounded first two denominators: it proves by exact rational tests that the complete equal-sum triple list coincides with the divisor list and that no candidate third denominator yields a sum strictly between \(S\) and \(\theta\). Its 58,020 screened parameter pairs are finite consistency checks, not the proof for all \(q\); the general conclusions follow from the preceding inequalities.

## Relationship to prior work

The motivating question is Nathanson's *Underapproximation by Egyptian fractions*, open Problem 2(b), which asks for distinct denominator tuples with exactly the same sum as an \(n\)-term greedy underapproximation for \(n\ge3\), and how many can exist. Nathanson's Sections 6–7 already contain **two-term** equal-best examples, and his Theorem 2 supplies the greedy interval criterion used above. The factorization \((2x-q)(2y-q)=q^2\) and the divisor count for \(2/q\) are classical; neither is claimed as new. The added result is the explicit very-small perturbation yielding a **best** three-term sum whose **entire** denominator-tuple fiber is exactly classified, with unbounded multiplicity, including the distinct-denominator variant. Chu's two-term best-approximation results, Kovač's almost-everywhere eventual-greediness theorem, and Kovač–Tang's rational eventual-greediness theorem address different quantifiers: two terms or asymptotically long approximations, not exact three-term multiplicities for this explicit family. Searches of relevant published mathematical results did not uncover an implication yielding this exact family and count; this is not a proof of universal novelty.

## Limitations

The assertion concerns one explicit rational target for each odd \(q\ge3\) and exactly three terms. The distinction between nondecreasing and strictly increasing denominators is essential to the two count formulas. It does not classify best representations at other targets or longer lengths, and its asymptotic multiplicity follows from selecting squarefree \(q\) rather than a density theorem for generic targets. Bibliographic search cannot exclude all implicit earlier specializations of general Egyptian-fraction counting theory. Independent scientific validation has not been performed.

## References

1. M. B. Nathanson, *Underapproximation by Egyptian fractions*, arXiv:2202.00191v1 (first public 2022-02-01), subsequently J. Number Theory 242 (2023), 208–234; especially Theorem 2, Sections 6–7, and Open Problem 2(b). https://arxiv.org/html/2202.00191v2
2. H. V. Chu, *A Threshold for the Best Two-term Underapproximation by Egyptian Fractions*, arXiv:2306.12564 (2023), https://arxiv.org/html/2306.12564v2
3. V. Kovač, *On eventually greedy best underapproximations by Egyptian fractions*, arXiv:2406.07218 (2024), https://arxiv.org/html/2406.07218v3
4. V. Kovač and Q. Tang, *Eventually greedy best Egyptian underapproximations of rational numbers via optimal control*, arXiv:2607.28387 (2026), https://arxiv.org/abs/2607.28387
