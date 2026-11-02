# Sharp longest nondivisibility runs in Pascal rows modulo prime powers

## Finding

For a prime \(p\), an integer \(\alpha\ge 1\), and \(n\ge0\), let \(L_{p,\alpha}(n)\) denote the maximum length of an interval of consecutive indices \(k\in\{0,\ldots,n\}\) on which every coefficient \(\binom nk\) is **not divisible** by \(p^\alpha\). Write
\[
n+1=p^r m,\qquad r=\nu_p(n+1),\qquad p\nmid m,
\]
and let \(R\) be the least positive residue of \(m\) modulo \(p^\alpha\). Then
\[
\boxed{L_{p,\alpha}(n)=p^r R=(n+1)\bmod p^{r+\alpha},}
\]
where the last residue is represented by an integer in \(\{1,\ldots,p^{r+\alpha}-1\}\). The final equality holds since the residue is nonzero. Both the initial and terminal blocks of \(p^rR\) indices attain this length. Every index interval of \(p^rR+1\) consecutive entries in the row contains a coefficient divisible by \(p^\alpha\).

## Assumptions and scope

All quantifiers are unconditional: \(p\) is any rational prime, \(\alpha\ge1\) is any integer, and \(n\ge0\) is any integer. The interval must lie entirely inside one fixed row of Pascal's triangle; intervals are not cyclic, and the endpoint coefficients count. An interval is good when every coefficient on it has \(p\)-adic valuation strictly smaller than \(\alpha\). The residue \(R\) is unique because \(p\nmid m\), so \(1\le R<p^\alpha\).

## Proof

**Step 1 (remove trailing digits).** Let \(r=\nu_p(n+1)\) and \(m=(n+1)/p^r\). Then
\[
n=p^r(m-1)+(p^r-1).
\]
For every \(0\le k\le n\), write \(k=p^r t+u\) with \(0\le u<p^r\). The last \(r\) base-\(p\) digits of \(n\) are all \(p-1\), so subtracting \(u\) produces no borrow among those digits and no borrow into the higher digits. By Kummer's theorem, the total number of borrows in subtracting \(k\) from \(n\) equals the number in subtracting \(t\) from \(m-1\). Therefore
\[
\nu_p\binom nk=\nu_p\binom{m-1}{t}.
\]
Every good or bad entry in row \(m-1\) is consequently repeated exactly \(p^r\) times in row \(n\). Because the first and last entries of any Pascal row are good, a maximal good run scales exactly by \(p^r\), even when the shorter row is entirely good.

**Step 2 (lower bound in the reduced row).** Put \(N=m-1\), \(Q=p^\alpha\), and \(R=m\bmod Q\) with \(1\le R<Q\). The final \(\alpha\) base-\(p\) digits of \(N\) represent \(R-1\). For every \(0\le k<R\), subtracting \(k\) from \(N\) has no borrow out of its last \(\alpha\) digits, since \(k\le R-1\). All higher digits of \(k\) vanish, so the number of borrows is at most \(\alpha-1\). By Kummer, the first \(R\) binomial coefficients of row \(N\) are good. Symmetry gives the last \(R\) as well.

**Step 3 (the sharp covering certificate).** Suppose \([K,K+R]\) is an interval of \(R+1\) consecutive integers inside \([0,N]\). Write \(K=Qh+u\) with \(0\le u<Q\), and expand \(u=\sum_{i=0}^{\alpha-1}u_i p^i\) and \(R=\sum_{i=0}^{\alpha-1}R_i p^i\). Here \(R_0\ge1\) because \(p\nmid m\). Construct the index
\[
Z=Qh+\sum_{i=0}^{\alpha-1}\max(u_i,R_i)p^i.
\]
Since \(Z-K=\sum_i\max(0,R_i-u_i)p^i\le R\), one has \(K\le Z\le K+R\le N\). The last \(\alpha\) digits of \(N\) are \((R_0-1,R_1,\ldots,R_{\alpha-1})\), read from lowest to highest. Subtracting \(Z\) from \(N\) forces a borrow out of the units digit, because \(\max(u_0,R_0)\ge R_0>R_0-1\). For each higher position \(1\le i<\alpha\), the incoming borrow persists since \(\max(u_i,R_i)+1>R_i\). Thus at least \(\alpha\) borrows occur, and Kummer gives
\[
p^\alpha\mid\binom NZ.
\]
Every \(R+1\)-term block therefore contains a bad coefficient. Combining with Step 2, the maximal length in row \(N\) is exactly \(R\); Step 1 multiplies it by \(p^r\), proving the claimed formula and covering property.

## Verification

The accompanying standalone `verify.py` enumerates exact integer binomial coefficients, independently measures maximal good runs, checks both endpoint runs and every forbidden interval for its test range, and tests the explicitly constructed covering index against a separately implemented base-\(p\) borrow counter. Run `python3 verify.py` from the extracted directory. The recorded result is

```
VERIFY_OK exact_rows=8320 forbidden_windows=1221990 digit_cover_certificates=667809
```

The proof above, not finite enumeration, establishes the assertion for all parameters. The digit construction is an explicit certificate for every forbidden block.

## Relationship to prior work

Kummer's classical valuation theorem is the main imported fact. Fine's theorem counts the nonzero entries in a Pascal row modulo a prime. Rowland's 2010 preprint (published in 2011) extends such **counts** to every prime power through digit-word statistics. Spiegelhofer and Wallner's 2016 preprint obtains explicit generating functions for the **counts** at each exact valuation. These theorems classify how many entries meet the valuation threshold, but do not themselves specify the ordering of survivors or their maximum uninterrupted stretch. The result here instead provides an exact extremal interval invariant and a constructive witness within every longer interval. Later analytical work on typical valuation distributions also concerns counts rather than this extremal question. A literature search cannot exclude equivalent results in unlocated earlier work, including studies of Pascal-row zero-block geometry and classical prime-power digit congruences.

## Limitations

The theorem describes the **maximum** consecutive good-run length, not the number or full distribution of all maximal runs, or the full residue values of the coefficients. It applies to prime-power divisibility in ordinary binomial Pascal rows, not general multinomial arrays or arbitrary integer moduli without further reduction. The historical priority conclusion remains provisional; no independent mathematical audit has been performed.

## References

1. E. E. Kummer, *Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen* (1852), valuation-by-borrows theorem.
2. N. J. Fine, *Binomial coefficients modulo a prime*, American Mathematical Monthly **54** (1947), 589–592.
3. E. Rowland, *The number of nonzero binomial coefficients modulo \(p^\alpha\)*, arXiv:1001.1783v1 (posted 2010-01-12); Journal of Combinatorics and Number Theory **3** (2011), 15–25. https://arxiv.org/abs/1001.1783
4. L. Spiegelhofer and M. Wallner, *An explicit generating function arising in counting binomial coefficients divisible by powers of primes*, arXiv:1604.07089v1 (posted 2016-04-24). https://arxiv.org/abs/1604.07089
5. L. Spiegelhofer and M. Wallner, *Divisibility of binomial coefficients by powers of two*, arXiv:1710.10884v1 (posted 2017-10-30). https://arxiv.org/abs/1710.10884
