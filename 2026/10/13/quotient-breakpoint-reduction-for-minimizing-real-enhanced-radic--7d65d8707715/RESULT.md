# Quotient-breakpoint reduction for minimizing real enhanced radicals
## Finding
Let \(a<b\) be coprime positive integers with \(a+b=c\). For every prime \(\ell\mid bc\), put \(m_\ell=v_\ell(bc)\) and \(M=\max_{\ell\mid bc}m_\ell\). For an integer degree \(d\ge2\), define
\[
P_d=a\prod_{\ell\mid bc}\ell^{\lfloor m_\ell/d\rfloor+(m_\ell\bmod d)}.
\]
When \(M\ge2\), every degree minimizing \(P_d\) over \(2\le d\le M\) belongs to
\[
\mathcal D=\bigcup_{\ell\mid bc}\left\{\left\lfloor\frac{m_\ell}{q}\right\rfloor:q\ge1,\ \left\lfloor\frac{m_\ell}{q}\right\rfloor\ge2\right\}.
\]
Consequently an exact search needs at most
\[
2\sum_{\ell\mid bc}\lfloor\sqrt{m_\ell}\rfloor
\]
candidate degrees. If \(M=1\), all degrees \(d\ge2\) give the same value, so \(d=2\) alone suffices for optimization.

For the Reyssat triple \(2+3^{10}\cdot109=23^5\), the candidate set is exactly \(\{2,3,5,10\}\); direct evaluation on those four degrees recovers the published minimizing degree \(d=5\).
## Assumptions and scope
The statement concerns the real enhanced-radical objective in which the exponent contributed by a prime of valuation \(m\) at degree \(d\) is \(\lfloor m/d\rfloor+(m\bmod d)\). It does not address the separate \(p\)-adic or combined-gain objectives, and it makes no assertion about the truth of the \(abc\) conjecture or about which triples maximize a gain statistic.

The input is an individual coprime \(abc\)-triple together with the exact prime valuations of \(bc\). The result is a deterministic reduction of the finite degree search stated in the source literature.
## Proof
For a fixed positive integer \(m\), set
\[
e_m(d)=\lfloor m/d\rfloor+(m\bmod d).
\]
Write \(q=\lfloor m/d\rfloor\) and \(m=qd+r\), where \(0\le r<d\). Then
\[
e_m(d)=q+r=m-q(d-1).
\]
If \(\lfloor m/(d+1)\rfloor=q\) as well, then
\[
e_m(d+1)=m-qd=e_m(d)-q.
\]
Thus, on any step \(d\to d+1\) for which the quotient \(\lfloor m/d\rfloor\) does not drop, the exponent decreases by exactly \(\lfloor m/d\rfloor\).

Now suppose \(2\le d<M\) and \(d\notin\mathcal D\). For every \(\ell\mid bc\), the quotient \(\lfloor m_\ell/d\rfloor\) is unchanged when \(d\) is replaced by \(d+1\): if it dropped, then \(d\) would be the right endpoint of a quotient plateau and hence \(d=\lfloor m_\ell/q\rfloor\) for the old positive quotient \(q\), placing \(d\) in \(\mathcal D\). Therefore
\[
\frac{P_{d+1}}{P_d}=\prod_{\ell\mid bc}\ell^{-\lfloor m_\ell/d\rfloor}.
\]
Because \(d<M\), at least one valuation satisfies \(m_\ell>d\), so at least one exponent in this product is positive. Hence \(P_{d+1}<P_d\). A non-breakpoint degree strictly inside \([2,M]\) therefore cannot minimize \(P_d\). The endpoint \(M\) belongs to \(\mathcal D\), since a prime with valuation \(M\) contributes \(\lfloor M/1\rfloor=M\). This proves the candidate reduction.

For the cardinality bound, the set of distinct quotients \(\lfloor m/q\rfloor\) has at most \(2\lfloor\sqrt m\rfloor\) elements: quotients arising from \(q\le\lfloor\sqrt m\rfloor\) contribute at most \(\lfloor\sqrt m\rfloor\) values, while for larger \(q\) every quotient is at most \(\lfloor\sqrt m\rfloor\). Taking a union over the prime valuations gives the stated bound.
## Verification
The accompanying `verify.py` uses exact integer arithmetic. It exhaustively checked every exponent vector of lengths one, two, and three with entries from \(1\) through \(25\), for a total of \(16{,}275\) vectors. For each vector it compared minimizers from the full degree interval with minimizers from \(\mathcal D\), checked strict descent at every omitted interior degree, and checked the stated candidate-count bound. It also independently evaluated the Reyssat exponent vector and obtained candidate degrees \(\{2,3,5,10\}\) with minimizing degree \(5\).

Replay output:

`VERIFY_OK exhaustive_vectors=16275 max_exponent=25 reyssat_candidates=2,3,5,10 reyssat_minimizer=5`

The exhaustive computation is a consistency check; the infinite statement is proved by the quotient-plateau argument above.
## Relationship to prior work
Laniewski and Müller formulate the real enhanced-radical minimization explicitly as a finite search over degrees up to the largest valuation and ask for systematic information about the minimizing presentation. Their formula is the objective \(P_d\) used here, but their stated reduction stops at the full interval \(2\le d\le M\). De Weger earlier defined the real enhanced radical, observed that optimization is finite once the degree exceeds the largest exponent, and tabulated all degrees for the Reyssat example. The quotient-breakpoint pruning theorem above is not stated in either inspected source.

For the Reyssat example, the prior table remains the source of the known optimum \(d=5\). The present result explains why the other tested degrees outside \(\{2,3,5,10\}\) are provably unnecessary for exact optimization.
## Limitations
The candidate bound is universal but not claimed sharp, and different primes can contribute the same breakpoint. The result does not identify the globally largest exponent factor among known \(abc\)-triples, does not bound the minimizing degree independently of the valuation data, and does not replace factorization of \(bc\). Literature searches can miss unindexed or differently phrased prior observations; the closest inspected primary sources do not contain this reduction.
## References
R. Laniewski and K. Müller, *The quality plane of abc-triples and the decomposition into gains*, arXiv:2610.03212v1, 2026.

B. de Weger, *On the approximation gain for abc-triples*, arXiv:2602.08051v2, 2026.
