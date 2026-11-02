# A logarithmic first-obstruction law for prime-power binomial divisibility

## Finding
For positive integers \(a,b\), define \(f(a,b)=0\) if \(bn+1\) divides \(\binom{(a+b)n}{an}\) for every positive integer \(n\), and otherwise define \(f(a,b)\) as the least positive index where divisibility fails.

Fix a prime \(p\), an integer \(r\ge2\), and a coefficient \(b\) with \(1\le b<p^r\) and \(p\nmid b\). Let \(j=j_p(b)\in\{1,\ldots,p-1\}\) be the unique solution of \(bj\equiv-1\pmod p\), and put \(Q=\lfloor bj/p^r\rfloor\). Then
\[
 f(p^r,b)>j\quad\Longleftrightarrow\quad j+Q\ge p\quad\text{and}\quad p^2\nmid bj+1.
\]
Otherwise \(f(p^r,b)=j\). In particular, \(f(p^r,b)=j\) for every \(1\le b\le p^{r-1}\) coprime to \(p\).

Let \(M_{p,r}\) be the number of such \(b\) satisfying \(f(p^r,b)>j_p(b)\), and let \(\delta_{p,r}=M_{p,r}/\varphi(p^r)\). For odd \(p\), define \(m=(p+1)/2\). Then
\[
\left|\delta_{p,r}-\left(\frac{p-1}{p}-\sum_{j=m}^{p-1}\frac1j\right)\right|\le\frac{2}{p^{r-1}}.
\]
For \(p=2\), \(M_{2,r}=0\). Consequently, for every choice of integers \(r=r(p)\ge2\),
\[
 \lim_{p\to\infty\atop p\text{ prime}}\delta_{p,r(p)}=1-\log 2.
\]
Thus the complementary proportion whose first eligible index is already a failure tends to \(\log2\).

There is also an exact finite formula. For \(j\in\{m,\ldots,p-1\}\), set \(B=p^r\), \(L_j=\lceil(p-j)B/j\rceil\), and let \(a_{j,s}\in\{0,\ldots,p^s-1\}\) be the solution to \(ja_{j,s}\equiv-1\pmod{p^s}\), for \(s=1,2\). Define
\[
 R_{j,s}=\left\lfloor\frac{B-1-a_{j,s}}{p^s}\right\rfloor-\left\lfloor\frac{L_j-1-a_{j,s}}{p^s}\right\rfloor.
\]
Then \(M_{p,r}=\sum_{j=m}^{p-1}(R_{j,1}-R_{j,2})\). Empty sums are zero.

## Assumptions and scope
The base \(p\) is any prime, \(r\ge2\), and the parameter \(b\) runs through the invertible integers below \(p^r\). The definition of \(f\) is global in all positive indices, not truncated to the tested range. The density is uniform over the \(\varphi(p^r)\) admissible coefficients. The first potentially failing index \(j_p(b)\) is always an integer between \(1\) and \(p-1\).

## Proof
**No earlier failure.** Sun's binomial divisibility theorem gives
\[
 \frac{bn+1}{\gcd(p^r,bn+1)}\mid\binom{(p^r+b)n}{p^rn}
\]
for every positive integer \(n\). For \(1\le n<j\), the denominator is prime to \(p\), so \(\gcd(p^r,bn+1)=1\) and divisibility holds. Thus \(f(p^r,b)\ge j\).

**Exactly one possible carry.** At \(n=j\), write \(bj=Qp^r+R\) with \(0\le R<p^r\). As \(b<p^r\) and \(j<p\), one has \(0\le Q\le j-1<p\). Kummer's theorem identifies the \(p\)-valuation of \(\binom{p^rj+bj}{p^rj}\) with the number of carries when adding \(p^rj\) and \(bj\) in base \(p\). All digits below position \(r\) contribute zero carries, while the digits at position \(r\) are \(j\) and \(Q\). Since \(j+Q\le2p-2\), there is either zero or one carry, with no further carry at position \(r+1\). Therefore
\[
 \nu_p\!\left(\binom{(p^r+b)j}{p^rj}\right)={\bf1}_{j+Q\ge p}.
\]
Since \(p\mid bj+1\), the cited divisibility theorem guarantees the necessary valuations at every prime other than \(p\). The binomial is divisible by \(bj+1\) exactly when its \(p\)-valuation is at least \(\nu_p(bj+1)\). With the preceding zero-or-one bound, divisibility at \(j\) occurs precisely when \(j+Q\ge p\) and \(\nu_p(bj+1)=1\). This proves the first assertion, including the possibility that \(p^2\mid bj+1\).

**Exact census.** The inequality \(j+\lfloor bj/B\rfloor\ge p\) is equivalent to \(b\ge (p-j)B/j\). Since \(b<B\), this inequality can hold only when \(j>p/2\), giving the range \(j=m,\ldots,p-1\) for odd \(p\); it never holds for \(p=2\). For fixed \(j\), the condition \(bj\equiv-1\pmod p\) selects exactly one residue class modulo \(p\), while the excluded condition \(p^2\mid bj+1\) selects exactly one subclass modulo \(p^2\). Counting these progressions in \([L_j,B)\) gives \(R_{j,1}-R_{j,2}\), hence the exact formula for \(M_{p,r}\).

**Logarithmic density.** Counting a single residue class modulo \(p^s\) in an interval of length \(T\) incurs an absolute error less than one relative to \(T/p^s\). Thus, with \(T_j=B-L_j\), each summand differs by less than two from \((1/p-1/p^2)T_j\). Since \(L_j\) differs by less than one from \((p-j)B/j\), the same summand differs by less than three from \((1/p-1/p^2)B(2j-p)/j\). Dividing by \(\varphi(B)=B(1-1/p)\) and summing over fewer than \(p/2\) terms gives the displayed error bound \(2/p^{r-1}\). The main term is
\[
 \frac1p\sum_{j=m}^{p-1}\left(2-\frac pj\right)
 =\frac{p-1}{p}-\sum_{j=m}^{p-1}\frac1j.
\]
The harmonic-number difference tends to \(\log2\) as odd primes tend to infinity. The error bound is uniform over every \(r\ge2\), completing the proof.

## Verification
Execute `python verify.py` with Python 3. The standalone checker tests the first eligible index by independent factorial-valuation arithmetic, direct whole-binomial divisibility for small prime powers, and exact progression counts for 12 prime-power configurations. Its finite samples corroborate but are not the proof of the infinite result.

## Relationship to prior work
Zhi-Wei Sun introduced the first-failure function \(f(a,b)\) and proved the general gcd-reduced divisibility theorem in *On divisibility concerning binomial coefficients* (arXiv:1005.1054v12, Section 1, Theorem 1.4). Guo and Krattenthaler proved the proposed eventual nondivisibility and supplied general bounds on \(f\) in *Some divisibility properties of binomial and q-binomial coefficients* (arXiv:1301.7651v3, Sections 1, 2 and 4). Neither paper states the prime-power parameter census or the limiting logarithmic density. Kummer's carry theorem supplies the local valuation tool; the present contribution combines the precise first-index criterion, arithmetic-progression census and uniform two-parameter density law.

## Limitations
The formula classifies whether the first possible obstruction \(j_p(b)\) is genuine; for delayed coefficients it does not compute the later exact value of \(f(p^r,b)\). The restriction \(b<p^r\) is essential to the one-carry argument. The result has not been independently audited, and equivalent coverage in historical literature outside the inspected sources remains possible.

## References
- Z.-W. Sun, *On divisibility concerning binomial coefficients*, arXiv:1005.1054v12 (2010), https://arxiv.org/html/1005.1054v12.
- V. J. W. Guo and C. Krattenthaler, *Some divisibility properties of binomial and q-binomial coefficients*, arXiv:1301.7651v3 (2013), https://arxiv.org/html/1301.7651v3.
- E. E. Kummer, *Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen*, J. Reine Angew. Math. 44 (1852), 93–146 (carry criterion).
