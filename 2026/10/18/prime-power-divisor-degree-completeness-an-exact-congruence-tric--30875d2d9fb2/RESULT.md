# Prime-power divisor-degree completeness: an exact congruence trichotomy

## Finding

Fix a rational prime \(r\), an exponent \(a\ge1\), and a rational prime \(p\). Call \(r^a\) *\(p\)-practical* when \(X^{r^a}-1\) has a monic divisor of every integer degree from \(0\) through \(r^a\) over the finite field \(\mathbb F_p\), with repeated factors allowed according to their multiplicities.

**Theorem.** If \(r=2\), every \(2^a\) is \(p\)-practical for every prime \(p\). If \(r\) is odd, then

\[
\begin{aligned}
a=1:\quad&r^a\text{ is }p\text{-practical}\iff p=r\text{ or }p\equiv\pm1\pmod r;\\
a\ge2:\quad&r^a\text{ is }p\text{-practical}\iff p=r\text{ or }p\equiv1\pmod r\text{ or }p\equiv-1\pmod{r^2}.
\end{aligned}
\]

Moreover, in every unsuccessful case with odd \(r\), the **least missing degree** is exactly \(2\) when \(p\not\equiv\pm1\pmod r\), and exactly \(r+1\) when \(a\ge2\), \(p\equiv-1\pmod r\), and \(p\not\equiv-1\pmod{r^2}\). In the latter case every degree \(0,1,\ldots,r\) is attainable. Thus the complete property stabilizes at the square: for each odd \(r\), its qualifying characteristics are identical for all exponents \(a\ge2\).

By the prime number theorem in arithmetic progressions, for each fixed odd \(r\), the qualifying rational primes \(p\) have natural density \(2/(r-1)\) when \(a=1\) and \((r+1)/(r(r-1))\) for every \(a\ge2\). The exceptional characteristic \(p=r\) contributes density zero.

## Assumptions and scope

All quantities \(r,p\) are rational primes and \(a\) is a positive integer. Divisors are monic and belong to \(\mathbb F_p[X]\), with the multiplicities of the factorization of \(X^{r^a}-1\). The degree \(0\) divisor is \(1\); the degree \(r^a\) divisor is the polynomial itself. This is a theorem about finite-field divisor degrees, not about positive integer divisors, divisors over \(\mathbb Z[X]\), or \(p\)-adic polynomial divisibility. No unproved analytic hypothesis is used; the density statement uses the standard unconditional prime number theorem for reduced residue classes.

For \(p\ne r\), put \(e_j=\operatorname{ord}_{r^j}(p)\) for \(1\le j\le a\). Standard cyclotomic factorization says that \(\Phi_{r^j}(X)\) splits over \(\mathbb F_p\) into \(r^{j-1}(r-1)/e_j\) irreducible factors, each of degree \(e_j\); \(\Phi_1(X)=X-1\) contributes a factor of degree one. This factor-degree criterion is classical and is recorded explicitly by Thompson in her work on \(p\)-practical integers.

## Proof

**Contiguous-degree lemma (classical; compare Thompson’s thesis, Theorem A.1).** Suppose factors considered so far realize every sum of degrees in \(\{0,\ldots,T\}\). Adding \(c\ge1\) distinct available factors, each of degree \(d\le T+1\), realizes every integer degree through \(T+cd\). Indeed the intervals \([jd,jd+T]\) for \(0\le j\le c\) meet or are adjacent. This remains true when the factors arise with finite multiplicities, provided those multiplicities are counted as separate copies.

**Characteristic divides the exponent base.** If \(p=r\), the binomial identity in characteristic \(p\) gives \(X^{r^a}-1=(X-1)^{r^a}\). Its powers give every desired degree. This includes \(r=2,p=2\).

**The even prime-power base.** Let \(r=2\), \(p\ne2\). The factors \(X-1\) and \(X+1\) give all degrees through \(2\). At level \(j\ge2\), every irreducible factor of \(\Phi_{2^j}(X)\) has degree \(e_j=\operatorname{ord}_{2^j}(p)\le\varphi(2^j)=2^{j-1}\). Immediately before that level, degrees \(0,\ldots,2^{j-1}\) are available. Hence the contiguous-degree lemma applies; the new total degree is \(2^j\). Induction proves all \(a\).

**Odd base: an order obstruction.** Let \(r\ge3\), \(p\ne r\), and write \(d=\operatorname{ord}_r(p)\). If \(d\ge3\), every factor from any \(\Phi_{r^j}\) has degree divisible by \(d\), because reduction modulo \(r\) shows \(d\mid\operatorname{ord}_{r^j}(p)\). With only one factor of degree \(1\), no divisor of degree \(2\) can occur. Conversely, \(d=1\) is precisely \(p\equiv1\pmod r\), and \(d=2\) is precisely \(p\equiv-1\pmod r\), since the unique element of multiplicative order two in \((\mathbb Z/r\mathbb Z)^\times\) is \(-1\). Thus only these two congruence classes can work.

**The positive congruence class.** Suppose \(p\equiv1\pmod r\), and set \(t=v_r(p-1)\ge1\). The lifting-the-exponent identity for odd \(r\) implies

\[
\operatorname{ord}_{r^j}(p)=r^{\max(0,j-t)}.
\]

For \(j\le\min(a,t)\), all cyclotomic factors have degree \(1\). Once \(j>t\), the new factors have degree \(r^{j-t}\le r^{j-1}\); by induction the previous levels already realize every degree through \(r^{j-1}\), so the contiguous-degree lemma applies. Induction covers all \(j\le a\).

**The negative congruence class.** Suppose \(p\equiv-1\pmod r\) and set \(t=v_r(p+1)\ge1\). Applying lifting the exponent to \(p^2\) yields

\[
\operatorname{ord}_{r^j}(p)=2r^{\max(0,j-t)}.
\]

For \(j\le\min(a,t)\), the nontrivial factors all have degree \(2\), with a total of \((r^{\min(a,t)}-1)/2\) copies; together with the degree-one factor, their subset sums are every degree through \(r^{\min(a,t)}\).

If \(a\ge2\) but \(t=1\), the levels \(j\ge2\) have factor degrees \(2r^{j-1}\ge2r\). The degree-one factor and the \((r-1)/2\) degree-two factors of level \(j=1\) realize every degree through \(r\), but none from \(r+1\) through \(2r-1\) can use a higher-level factor. Consequently the least missing degree is \(r+1\).

Finally, if \(t\ge2\), the initial \(\min(a,t)\) levels give every degree through \(r^{\min(a,t)}\). For each \(j>t\), all new factors have degree \(2r^{j-t}\le r^{j-1}\) because \(r^{t-1}\ge r\ge3>2\). Apply the contiguous-degree lemma successively to reach all degrees through \(r^a\). This proves the claimed equivalences and all missing-degree assertions.

**Densities.** For odd \(r\) and \(a=1\), two reduced residue classes modulo \(r\) occur, yielding density \(2/(r-1)\). For \(a\ge2\), exactly \(r\) reduced residue classes modulo \(r^2\) satisfy \(p\equiv1\pmod r\), and one additional class satisfies \(p\equiv-1\pmod{r^2}\). These classes are disjoint, giving \((r+1)/(r(r-1))\) out of \(\varphi(r^2)=r(r-1)\) classes. The finitely many characteristics dividing the modulus do not affect density. This completes the proof.

## Verification

The included `VERIFY.py` checks the theorem using exact multiplicative orders modulo prime powers, the resulting cyclotomic factor-degree multisets, and a bitset computation of every attainable divisor degree. It tests 1,242 triples with \(r\le19\), \(p\le199\), and \(r^a\le625\), checking not just the binary practical property but the exact least missing degree. Running `python VERIFY.py --factor` adds 242 independent tests using actual factorizations of \(X^{r^a}-1\) over finite fields via SymPy. Both modes passed. Neither finite computation substitutes for the preceding proof of the infinite statement or the prime-density theorem.

## Relationship to prior work

Thompson introduced \(p\)-practicality and the general characterization of divisor degrees by multiplicative orders, and established the familiar sufficient congruences \(p\equiv\pm1\pmod n\) for a fixed exponent \(n\). In particular, her work explicitly mentions the prime-index example \(n=5\) and the same-characteristic prime-power observation \(n=p^k\). These statements are acknowledged as prior knowledge. The present result gives a precise classification simultaneously for every prime-power index, including characteristics \(p\equiv1\pmod r\) not necessarily \(1\pmod{r^a}\), the least excluded degree outside the allowed classes, and a prime-density formula stable in the exponent. Thompson's generic multiplicative-order criterion provides a starting point but does not state this prime-power congruence trichotomy or its exact first-gap and density conclusions in the inspected relevant sections. The identification of the new combined result as absent from all other literature has not been independently certified.

## Limitations

The classification applies only to prime-power indices and polynomial divisibility over prime fields. It does not classify composite indices with two or more distinct prime factors, arbitrary extension fields, or counts of divisors of each degree. The prime-density limit has no effective error term here. A differently worded or incompletely indexed prior prime-power classification remains a residual originality risk. The correctness proof is independent of finite testing.

## References

1. L. Thompson, *On the divisors of \(x^n-1\) in \(\mathbb F_p[x]\)*, arXiv:1111.5403, first submitted 23 November 2011. https://arxiv.org/abs/1111.5403
2. L. Thompson, *Variations on a question concerning the degrees of divisors of \(x^n-1\)*, Journal de Théorie des Nombres de Bordeaux 26 (2014), 253–268, preprint arXiv:1206.4355 (2012), especially Lemma 2.3, Proposition 2.4, and the discussion preceding Theorem 3.1. https://arxiv.org/abs/1206.4355 ; https://doi.org/10.5802/jtnb.866
3. L. Thompson, *Products of Distinct Cyclotomic Polynomials*, Dartmouth College PhD thesis, 24 May 2012, Chapter 6, §§6.1–6.3, 6.6. https://www.lolathompson.com/uploads/1/1/0/6/110629329/thesis.pdf
4. P. Pollack and L. Thompson, *On the degrees of divisors of \(T^n-1\)*, arXiv:1206.2084, 2012, on related number-field practical divisor degrees. https://arxiv.org/abs/1206.2084
