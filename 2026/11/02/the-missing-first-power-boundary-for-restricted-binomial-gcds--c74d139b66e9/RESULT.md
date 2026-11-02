# The missing first-power boundary for restricted binomial gcds

## Finding
For every prime \(p\), let \(m=p+1\) and, for integers \(q\ge2\), put
\[
G_p(q)=\gcd\left\{\binom{(p+1)q}{(p+1)d}:1\le d<q\right\}.
\]
Then the exact initial valuation profile is
\[
 v_p(G_p(q))=\begin{cases}0&2\le q<p,\\2&q=p.\end{cases}
\]
In particular the least row at which the sharp global valuation maximum of two is attained equals
\[
 T_p(p+1)=p(p+1).
\]
The case \(p=2\), namely \(T_2(3)=6\), was already recorded by McTague; the uniform odd-prime statement and the jump from zero to two are the present contribution.

## Assumptions and scope
Here \(p\) is an arbitrary prime; \(q\) and \(d\) are positive integers in the displayed ranges. The selected binomial gcd is over a nonempty set for \(q\ge2\). The symbol \(v_p\) denotes the ordinary prime-adic valuation. For a fixed \(m\) coprime to \(p\), the least extremal row \(T_p(m)\) is the smallest multiple \(N=mq\), \(q\ge2\), satisfying the sharp global maximum \(v_p(G(N;m))=r_p(m)\), where \(r_p(m)\) is the least positive integer \(r\) such that \(m<p^r\). Fairfax-Ball proved that this maximum is \(r_p(m)\) and is attained for some admissible row. As \(p<p+1<p^2\) for all primes \(p\), we have \(r_p(p+1)=2\).

## Proof
Kummer's theorem equates the valuation of \(\binom{x+y}{x}\) to the number of carries in base \(p\) when \(x\) and \(y\) are added.

Take any \(2\le q<p\). For every \(1\le d<q\), the two addends are
\[
 x=(p+1)d=pd+d,\qquad y=(p+1)(q-d)=p(q-d)+(q-d).
\]
Their base-\(p\) expansions have digit pairs \((d,d)\) and \((q-d,q-d)\), from the units column upward, because \(0<d,q-d<p\). Each column sums to \(q<p\), and hence there are no carries. Consequently every selected binomial coefficient has valuation zero, giving \(v_p(G_p(q))=0\).

At \(q=p\), the same two addends are \(x=pd+d\) and \(y=p(p-d)+(p-d)\), where \(1\le d<p\). In the units column the sum is \(d+(p-d)=p\), producing a carry of one. In the next column the sum including this carry is \(d+(p-d)+1=p+1\), producing one further carry. At the next column the incoming carry is absorbed without producing another. Thus **every** selected binomial coefficient has exactly two base-\(p\) carries, even when \(p=2\). This proves \(v_p(G_p(p))=2\). Since the known universal upper bound is two and all earlier admissible multipliers have valuation zero, the least attaining row is \(p(p+1)\). \(\square\)

## Verification
The accompanying `verify.py` independently counts carries for all pairs \((p,q)\) with primes \(p\le199\) and \(2\le q\le p\), totaling 46 primes and 280419 selected binomial coefficients. It checks that every count equals zero before \(q=p\) and two at \(q=p\). For primes \(p\le13\), it separately calculates factorial binomial coefficients with exact integer arithmetic and recovers the same valuations. Executing `python verify.py` returned `VERIFY_OK`.

## Relationship to prior work
Fairfax-Ball, *Sharp \(p\)-adic Extrema and Least Extremal Rows for Restricted Binomial GCDs*, arXiv:2610.01328 (first available October 1, 2026), proves the global maximum and establishes \(T_p(p^a+1)=p^{3a}+1\) for \(a\ge2\). Remark 8.3 explicitly excludes \(a=1\), explaining why that argument cannot handle the boundary. The formula above fills precisely that excluded first-power regime; it is **not** obtained by substituting \(a=1\) into the higher-power formula. McTague, arXiv:1510.06696, records \(T_2(3)=6\) and gives a theorem under a congruence hypothesis \(p\equiv1\pmod m\), which fails when \(m=p+1\). Wu, arXiv:2606.20940, studies the same selected gcd and provides formulas under prime-power or congruence restrictions that do not settle the present odd-prime boundary. This priority comparison is based on the accessible primary texts, not on absence from search results alone.

## Limitations
Only the initial multiplier range \(2\le q\le p\) is classified; no valuations for \(q>p\) are asserted. The global bound of two is imported from Fairfax-Ball, although the first-attainment statement follows from elementary Kummer carrying. This is an exact boundary theorem, not a new general theory of binomial gcds. Earlier implicit appearances of the uniform boundary formula remain a priority risk, and no independent validation has occurred.

## References
1. J. Fairfax-Ball, *Sharp \(p\)-adic Extrema and Least Extremal Rows for Restricted Binomial GCDs*, arXiv:2610.01328 (2026), Sections 2–8, especially Remark 8.3.
2. C. McTague, *On the Greatest Common Divisor of Binomial Coefficients*, arXiv:1510.06696v5 (2018), Theorem Q and Remarks.
3. C. W. Wu, *Computing the Greatest Common Divisor of Binomial Coefficients*, arXiv:2606.20940v2 (2026), Sections 1–2.
4. E. E. Kummer, *Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen* (1852), the carry theorem.
