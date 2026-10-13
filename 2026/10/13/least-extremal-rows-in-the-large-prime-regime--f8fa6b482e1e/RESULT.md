# Least extremal rows in the large-prime regime
## Finding
Let \(m\ge 2\) and let \(p>m\) be prime. For every admissible row \(N>m\) with \(m\mid N\), define
\[
G(N;m)=\gcd\left\{\binom{N}{k}:0<k<N,\ m\mid k\right\}.
\]
Let \(r_p(m)\) be the least positive integer \(r\) such that \(m<p^r\), and let \(T_p(m)\) be the least admissible row at which \(v_p(G(N;m))\) attains its maximum. Since \(p>m\), one has \(r_p(m)=1\). The least extremal row is
\[
T_p(m)=m\left\lceil\frac{p+1}{m}\right\rceil.
\]
Equivalently, \(T_p(m)\) is the first multiple of \(m\) strictly larger than \(p\). More strongly, if \(T_p(m)=p+s\), then \(1\le s<m\) and every selected coefficient in that row has exact valuation
\[
v_p\!\binom{T_p(m)}{k}=1
\qquad(0<k<T_p(m),\ m\mid k).
\]

## Assumptions and scope
The hypotheses are exactly \(m\ge2\) and prime \(p>m\). In particular \(p\nmid m\). The statement concerns the fixed-divisibility restriction \(m\mid k\), not restrictions such as coprimality or non-coprimality of the lower index. The formula resolves the entire regime \(r_p(m)=1\); it does not assert a formula for \(p<m\).

## Proof
Write
\[
T=m\left\lceil\frac{p+1}{m}\right\rceil=p+s.
\]
Because \(m<p\) and a prime \(p\) cannot be divisible by \(m\ge2\), \(T\) is the next multiple of \(m\) after \(p\), so \(1\le s<m\).

First consider a selected lower index \(k\) in row \(T\). Since consecutive selected indices differ by \(m\),
\[
m\le k\le T-m=p+s-m<p,
\]
and because \(s<m\), also \(k>s\). In base \(p\), the row is \(T=p+s\). At the \(p\)-boundary one has \(k\bmod p=k>s=T\bmod p\), so subtracting \(k\) from \(T\) produces one borrow. There can be no further borrow: \(T<p+m<2p<p^2\) for \(p\ge3\), and for every higher power the residues are simply \(k<T\). Kummer's theorem therefore gives
\[
v_p\!\binom{T}{k}=1
\]
for every selected \(k\). Hence \(v_p(G(T;m))=1\).

For minimality, every earlier admissible row \(N<T\) is a multiple of \(m\) lying strictly below \(p\), by the definition of \(T\). Thus every factorial occurring in \(\binom{N}{k}\) has argument below \(p\), so \(v_p\!\binom{N}{k}=0\) for all \(0<k<N\). Consequently \(v_p(G(N;m))=0\) for every earlier admissible row.

For completeness, the value \(1\) is the global maximum in this regime. A direct specialization of the usual leading-digit carry argument gives the upper bound. Write an arbitrary admissible row as \(N=mq\), and write \(q=\lambda p^t+b\) with \(1\le\lambda\le p-1\) and \(0\le b<p^t\). If \(b>0\), choose the selected index \(k=mb\); after the common lower block is separated, its carry count is that of \(X+\lambda m\), where \(0\le X<m<p\) and \(X+\lambda m<pm<p^2\), so there is at most one carry. If \(b=0\) and \(\lambda\ge2\), choose \(k=mp^t\); after shifting by \(p^t\), the carry count is that of \(m+(\lambda-1)m=\lambda m<p^2\), again at most one. If \(b=0\) and \(\lambda=1\), choose \(k=mp^{t-1}\); after shifting, the sum is \(m+(p-1)m=pm\), which has one carry because \(m<p\). Thus every admissible row has restricted-GCD valuation at most \(1\), while the row \(T\) attains \(1\). This proves the formula for \(T_p(m)\).

## Verification
A standalone exact-integer checker evaluates the Legendre-formula valuation of every selected binomial coefficient for all \(2\le m\le80\) and every prime \(m<p\le401\). It verifies that every selected coefficient in the predicted target row has valuation exactly \(1\), that every earlier admissible row has restricted-GCD valuation \(0\), and, on a smaller subrange, confirms the same statements by direct exact binomial arithmetic. The replay result is:

`VERIFY_OK cases=5250 target_coefficients=53641 lower_rows=48391 m_max=80 p_max=401`

These finite checks are supplementary; the proof above is valid for all allowed \(m\) and \(p\).

## Relationship to prior work
Fairfax-Ball, arXiv:2610.01328v1, proves the sharp maximum \(r_p(m)\), constructs the row \(N=mp\) when \(m<p\), then defines the least extremal row \(T_p(m)\). Its exact least-row theorem treats the different family \(m=p^a+1\) with \(a\ge2\); the large-prime regime \(p>m\) is not given a least-row formula there. The present result replaces the generic attaining row \(mp\) by the exact minimum, which always lies in \(p<T_p(m)<p+m\), and identifies the exact valuation of every selected coefficient at that minimum.

McTague, arXiv:1510.06696v5, gives a complete valuation criterion under the congruence \(p\equiv1\pmod m\). That theorem overlaps one residue-class subfamily and can recover the target-row valuation there, but it neither covers arbitrary primes \(p>m\) nor formulates the all-residue least-row classification above. Fairfax-Ball, arXiv:2609.37754v1, gives a complete valuation formula under \(p\equiv-1\pmod m\), so it similarly overlaps another residue-class subfamily rather than the unrestricted large-prime regime. Wu, arXiv:2606.20940v2, studies the same selected-GCD family but does not supply this least-extremal-row formula.

## Limitations
The theorem is confined to \(p>m\), equivalently \(r_p(m)=1\). The literature comparisons establish non-implication from the inspected sources, not historical uniqueness. A 2026 paper on binomial GCDs with non-coprime lower indices uses a different selection rule; only its public description was available in the inspected literature trail, so an unexpected equivalence through that different restriction remains a low residual risk.

## References
1. J. Fairfax-Ball, *Sharp \(p\)-adic Extrema and Least Extremal Rows for Restricted Binomial GCDs*, arXiv:2610.01328v1, 2026.
2. J. Fairfax-Ball, *Restricted Binomial GCDs at Primes Congruent to \(-1\)*, arXiv:2609.37754v1, 2026.
3. C. McTague, *On the Greatest Common Divisor of Binomial Coefficients \(\binom{n}{q},\binom{n}{2q},\binom{n}{3q},\dots\)*, arXiv:1510.06696v5; *American Mathematical Monthly* 124 (2017), 353–356.
4. C. W. Wu, *Computing the Greatest Common Divisor of Binomial Coefficients \(\binom{mn}{mk}\)*, arXiv:2606.20940v2, 2026.
5. E. E. Kummer, *Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen*, *Journal für die reine und angewandte Mathematik* 44 (1852), 93–146.
