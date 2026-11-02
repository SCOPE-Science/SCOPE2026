# Prime-power Pascal columns: exact valuation densities and sharp threshold periods

## Finding
Fix a prime \(p\), an integer \(a\ge1\), and write \(m=p^a\). For every integer \(n\ge m\), let
\[
W_{p,a}(n)=\nu_p\!\left(\binom{n-1}{m-1}\right).
\]
The natural density \(\mu_{p,a}(v)\) of positive integers \(n\) with \(W_{p,a}(n)=v\) exists for every integer \(v\ge0\) and is
\[
\boxed{\mu_{p,a}(0)=p^{-a},\qquad
\mu_{p,a}(v)=\frac{p-1}{p+1}\,p^{-|a-v|}
\left(1-p^{-2\min(a,v)}\right)\quad(v\ge1).}
\tag{1}
\]
The probability-generating function of these densities is
\[
\boxed{\sum_{v\ge0}\mu_{p,a}(v)z^v
=p^{-a}+\frac{(p-1)^2}{p^{a+2}}
\frac{\sum_{r=1}^{a}(pz)^r}{1-z/p}.}
\tag{2}
\]
For each positive integer \(v\), the Boolean sequence
\(\mathbf 1_{\{W_{p,a}(n)\ge v\}}\), defined for \(n\ge m\), has **least eventual period exactly** \(p^{a+v-1}\). The threshold \(v=a\) corresponds to the arithmetic divisibility
\[
W_{p,a}(n)\ge a\quad\Longleftrightarrow\quad n\mid\binom n{p^a}.
\]
Consequently, the latter divisibility event has least eventual period \(p^{2a-1}\) and exact natural density
\[
\boxed{\delta_{p,a}=\frac{p}{p+1}\left(1-p^{-2a}\right).}
\tag{3}
\]
These statements hold simultaneously for **every prime** \(p\) and \(a\ge1\). The already-known binary column-density theory covers the corresponding \(p=2\) marginal densities; the uniform explicit profile and sharp threshold-period statement are formulated with that prior coverage acknowledged.

## Assumptions and scope
The valuation \(\nu_p(u)\) is the exponent of \(p\) in a positive integer \(u\). Natural density means the limit, for each fixed \(p,a,v\),
\[
\lim_{X\to\infty}\frac{1}{X}\#\{m\le n\le X: W_{p,a}(n)=v\}.
\]
For an eventually periodic Boolean sequence on \(n\ge m\), the least eventual period is the smallest positive integer \(T\) for which the predicate at \(n\) and \(n+T\) agrees for all sufficiently large \(n\); the proof actually supplies agreement for all \(n\ge m\). We do not assign a value to \(W_{p,a}(n)\) for \(n<m\).

## Proof
**1. Exact valuation identity.** Write \(n=p^a q+r\), where \(q\ge1\) and \(0\le r<p^a\). Kummer's carry/borrow theorem applied to \(\binom{n-1}{p^a-1}\) yields
\[
W_{p,a}(n)=\begin{cases}
0,&r=0,\\
a-s+\nu_p(q),&1\le r<p^a,\ s=\nu_p(r)<a.
\end{cases}
\tag{4}
\]
Indeed, if \(r=0\), the low \(a\) base-\(p\) digits of \(n-1\) are all \(p-1\), so subtracting \(p^a-1\) produces no borrows. If \(r>0\) and \(s=\nu_p(r)\), the low \(s\) digits of \(n-1\) are \(p-1\); subtraction first borrows at digit \(s\), then carries that borrow through the remaining \(a-s-1\) low digits and through exactly \(\nu_p(q)\) leading zero digits of \(q\). This gives \(a-s+\nu_p(q)\) borrows. Equivalently, \(\binom n{p^a}=\frac{n}{p^a}\binom{n-1}{p^a-1}\), so the same identity follows from \(\nu_p\binom n{p^a}=\nu_p(q)\).

**2. Exact distribution.** For uniformly distributed integers \(n\), the residue \(r\pmod{p^a}\) is uniform, and, conditional on each \(r\), the quotient \(q\) is equidistributed in residue classes modulo every fixed power of \(p\). Thus the limiting probabilities are
\[
\Pr(r=0)=p^{-a},\quad
\Pr(\nu_p(r)=s)=\frac{p-1}{p^{s+1}}\ (0\le s<a),\quad
\Pr(\nu_p(q)=t\mid r)=\frac{p-1}{p^{t+1}}\ (t\ge0).
\]
When \(r>0\), put \(j=a-s\) (so \(1\le j\le a\)); by (4), \(W=j+t\). For each \(v\ge1\), summing over \(j\le\min(a,v)\) gives
\[
\begin{aligned}
\mu_{p,a}(v)
&=\sum_{j=1}^{\min(a,v)}
\frac{p-1}{p^{a-j+1}}\frac{p-1}{p^{v-j+1}}\\
&=\frac{(p-1)^2}{p^{a+v+2}}
\sum_{j=1}^{\min(a,v)}p^{2j}
=\frac{p-1}{p+1}p^{-|a-v|}
\bigl(1-p^{-2\min(a,v)}\bigr).
\end{aligned}
\]
The \(r=0\) event gives \(\mu(0)=p^{-a}\). Summing the independent geometric exponents first proves the generating function (2). In particular, for \(v\ge a\) the positive masses form an exact geometric tail with ratio \(1/p\). Their sum from \(v=a\) to infinity is (3).

**3. Exact threshold periods.** Fix \(v\ge1\), and set \(T=p^{a+v-1}\). From (4), for \(r>0\) the threshold \(W\ge v\) is equivalent to
\[
\nu_p(q)\ge\max(0,v-a+s).
\tag{5}
\]
The exponent on the right is at most \(v-1\), since \(s\le a-1\). Replacing \(n\) with \(n+T\) preserves \(r\) and changes \(q\) by \(p^{v-1}\), so (5) is unchanged. When \(r=0\), both sides of the shift have valuation zero. Thus \(T\) is a period on all \(n\ge m\).

To prove *least* period, observe that any eventual period of a sequence already having period \(T\) must divide \(T\). It therefore suffices to disprove period \(T/p\). If \(v=1\), choose \(n=m+(p-1)p^{a-1}\). Formula (4) shows \(W(n)\ge1\), whereas \(n+T/p=2m\) has \(W=0\). If \(v\ge2\), choose \(n=mp^{v-1}+p^{a-1}\). Then \(\nu_p(r)=a-1\) and \(\nu_p(q)=v-1\), giving \(W(n)=v\). Replacing \(n\) by \(n+T/p\) changes \(q\) to \(p^{v-1}+p^{v-2}\), so \(W(n+T/p)=v-1\). These witnesses have infinitely many translates by \(T\), ruling out \(T/p\) as an eventual period. Therefore \(p^{a+v-1}\) is the least eventual period.

**4. The row-number divisibility corollary.** For \(n\ge m\), the identity \(m\binom n m=n\binom{n-1}{m-1}\) implies
\(n\mid\binom n m\) exactly when \(m\mid\binom{n-1}{m-1}\), since \(\binom{n-1}{m-1}\) is integral. With \(m=p^a\) this is \(W\ge a\). The sharp period is \(p^{2a-1}\), and its density is the sum of the geometric tail computed in Step 2.

## Verification
The accompanying standalone `verify.py` uses Legendre factorial valuations (independent of the borrow derivation) and direct exact integer binomial coefficients. It checks the mass at every tested positive \(v\), the full Boolean period, explicit sharpness witnesses, and the direct \(n\mid\binom n{p^a}\) period count. Eleven \((p,a)\) cases are tested, with prime bases \(2,3,5,7\), exponents through \(a=5\), and valuation layers through \(v=5\). All pass. Finite checks do not establish the formulas for unrestricted \(p,a,v\); Steps 1–4 do.

## Relationship to prior work
Kummer's theorem gives the borrow description of individual binomial valuations, a principal ingredient and not claimed as new. Rowland's *The number of nonzero binomial coefficients modulo \(p^\alpha\)* (arXiv:1001.1783, initially public 2010-01-12) counts values along a fixed row while the lower index varies. Rowland's *Two binomial coefficient conjectures* (arXiv:1102.1464, 2011-02-07), Section 3, establishes periodicity of \(\operatorname{frac}(\binom n m/n)\) for fixed \(m\), including its period for a prime-power \(m\), and the zero-residue frequency for \(m=p\). Therefore general periodicity and the \(a=1\) zero-frequency are **known**. His text does not present the full distribution (1) for \(a\ge2\) or the exact least periods for every threshold \(v\).

Spiegelhofer and Wallner, *An explicit generating function arising in counting binomial coefficients divisible by powers of primes* (arXiv:1604.07089, initially public 2016-04-24), Section 2.4, explicitly presents a general **binary** fixed-column density framework \(\rho_2(j,t)\), so the \(p=2\) specialization of the marginal densities is covered by that framework even without an identical displayed closed form. Their stated column-density formulas do not give the corresponding odd-prime complete family or the sharp least periods of each valuation threshold. Robbins' 1982 and 1985 papers study how many lower indices in each fixed row obey divisibility by the row number; that is the dual counting direction, not the fixed-column distribution here. Bibliographic priority outside these sources is not asserted.

## Limitations
The theorem covers the valuation distribution and the divisibility threshold, not the full residue spectrum of \(\binom{n-1}{p^a-1}\) modulo \(p^a\). The zero-frequency case at \(a=1\) and the binary fixed-column density framework are established prior contributions. No independent mathematical audit has been performed; the proof has undergone only the reported self-review. Unindexed or inaccessible literature could contain an equivalent all-prime distribution or period statement.

## References
- E. Kummer, *Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen* (1852), classical borrow theorem.
- E. Rowland, *The number of nonzero binomial coefficients modulo \(p^\alpha\)*, arXiv:1001.1783 (initial public posting 2010-01-12), https://arxiv.org/abs/1001.1783.
- E. Rowland, *Two binomial coefficient conjectures*, arXiv:1102.1464 (initial public posting 2011-02-07), https://arxiv.org/abs/1102.1464.
- L. Spiegelhofer and M. Wallner, *An explicit generating function arising in counting binomial coefficients divisible by powers of primes*, arXiv:1604.07089 (initial public posting 2016-04-24), https://arxiv.org/abs/1604.07089.
- N. Robbins, *On the Number of Binomial Coefficients which are Divisible by their Row Number*, Canad. Math. Bull. 25 (1982), 363–365, DOI: 10.4153/CMB-1982-052-3.
