# Strict exponent balancing and sharp support extrema for recursive divisor counts

## Finding

Let \(\kappa_0(1)=1\) and, for every integer \(n>1\), let
\[
\kappa_0(n)=1+\sum_{\substack{d\mid n\\d<n}}\kappa_0(d).
\]
For a prime factorization \(n=\prod_{i=1}^{r}p_i^{a_i}\), put \(m=\Omega(n)=\sum_i a_i\) and \(r=\omega(n)\). The value \(\kappa_0(n)\) depends only on the exponent multiset \(\mathbf a=(a_1,\ldots,a_r)\).

**Strict balancing theorem.** Fix \(m\ge r\ge1\). If two positive entries satisfy \(a\ge b+2\), transferring one unit from the larger entry to the smaller entry strictly increases the recursive divisor count:
\[
\mathcal K(\ldots,a-1,\ldots,b+1,\ldots)>\mathcal K(\ldots,a,\ldots,b,\ldots).
\]
Consequently, \(\mathcal K\) is strictly Schur-concave on the positive integer exponent vectors of fixed length and sum: if one vector strictly majorizes another, its value is strictly smaller. This is a **partial-order** statement; incomparable signatures are not claimed to be ordered.

Write \(m=qr+t\), where \(q\ge1\) and \(0\le t<r\). Define
\[
\mathbf u=(m-r+1,1,\ldots,1),\qquad
\mathbf b=(\underbrace{q+1,\ldots,q+1}_{t},\underbrace{q,\ldots,q}_{r-t}).
\]
For every such \(n\), the **sharp fixed-support envelope** is
\[
\boxed{\mathcal K(\mathbf u)\le\kappa_0(n)\le\mathcal K(\mathbf b).}
\]
Equality at either end holds **exactly** when the exponent multiset equals that end's displayed signature. If the two end signatures coincide, both equalities necessarily hold. The prime bases themselves can be arbitrary distinct primes.

These are computable **exact integers**: for a positive exponent vector \(\mathbf a\) of sum \(m\), put
\[
P_{\mathbf a}(k)=\prod_{i=1}^r\binom{a_i+k-1}{a_i},\quad
\mathcal K(\mathbf a)=\sum_{k=1}^{\infty}\frac{P_{\mathbf a}(k)}{2^k}
=2\sum_{j=1}^{m}\Delta^jP_{\mathbf a}(0),
\]
where \(\Delta P(k)=P(k+1)-P(k)\), and \(\Delta^j\) denotes its \(j\)-fold iterate.

Splitting one positive exponent into two positive exponents strictly increases \(\mathcal K\). Thus, at fixed \(\Omega(n)=m\), the global minimum is \(2^m\), attained only for prime powers, and the global maximum is \(2\sum_{j=1}^{m}j!\,{m\brace j}\), attained only for squarefree integers. Here \({m\brace j}\) denotes a Stirling number of the second kind. The endpoint values are classical; the new assertion is the majorization comparison and the full fixed-\((m,r)\) sharp envelope.

## Assumptions and scope

Integers satisfy \(n\ge2\) and \(1\le r=\omega(n)\le m=\Omega(n)\); exponents are positive integers. The balancing operation preserves the number of distinct primes, their identities, and the total prime-factor multiplicity; splitting changes the number of distinct primes and may use a new prime. No upper bound is imposed on \(m\), \(r\), or the prime bases.

The term *strict Schur-concavity* is used on the integer domain: \(\mathbf a\succ\mathbf c\) means \(\mathbf a\) majorizes \(\mathbf c\), and the sorted exponent multisets differ. It does not assert a continuous extension or any comparison of incomparable vectors.

## Proof

**1. Positive series for the recursive divisor count.** Let \(\tau_k(n)\) count ordered \(k\)-tuples of positive integers, allowing units, whose product is \(n\). Stars and bars in each prime exponent gives
\[
\tau_k(n)=\prod_{i=1}^r\binom{a_i+k-1}{a_i}=P_{\mathbf a}(k).
\]
For each fixed \(n\), this grows polynomially in \(k\), so the series \(S(n)=\sum_{k\ge1}2^{-k}\tau_k(n)\) converges absolutely. The divisor-convolution identity \(\sum_{d\mid n}\tau_k(d)=\tau_{k+1}(n)\) yields
\[
2S(n)=\tau_1(n)+\sum_{k\ge1}2^{-k}\tau_{k+1}(n)
=1+\sum_{d\mid n}S(d).
\]
Since \(S(1)=1\), subtracting the \(d=n\) term recovers the defining recursion of \(\kappa_0\), giving \(S(n)=\kappa_0(n)\) by induction. The same coefficient formula appears in prior work, cited below; it is used as a lemma here, not claimed as novel.

**2. Strict balancing.** For \(k\ge1\), write \(f_k(a)=\binom{a+k-1}{a}\). When \(a\ge b+2\), the positive product term changes by the factor
\[
\frac{f_k(a-1)f_k(b+1)}{f_k(a)f_k(b)}
=\frac{a(b+k)}{(a+k-1)(b+1)}
=1+\frac{(k-1)(a-b-1)}{(a+k-1)(b+1)}.
\]
This equals \(1\) at \(k=1\) and is strictly greater than \(1\) for every \(k\ge2\). Other factors stay positive, so the full positive series strictly increases. Every strict majorization comparison of positive integer vectors of equal sum and length can be effected by a finite sequence of such decreasing-disparity transfers, with permutations allowed. Thus strict Schur-concavity follows.

**3. Sharp fixed-support bounds.** Among positive \(r\)-component integer vectors summing to \(m\), \(\mathbf u\) majorizes every vector and every vector majorizes \(\mathbf b\). Any non-endpoint vector admits a finite sequence of strict balancing moves toward \(\mathbf b\), and can be reached from \(\mathbf u\) by transfers; the inequalities and sharp equality cases follow. Distinct primes of any requested exponent signature exist, so both extrema are attained.

**4. Strict increase when a prime exponent is split.** For all \(k\ge2\) and positive \(a,b\),
\[
\frac{f_k(a+b)}{f_k(a)}=\prod_{s=1}^{b}\frac{a+s+k-1}{a+s}
<\prod_{s=1}^{b}\frac{s+k-1}{s}=f_k(b).
\]
Hence replacing the exponent \(a+b\) by \(a,b\) strictly increases every \(k\ge2\) summand of the positive series and preserves the \(k=1\) summand. Repeating splits connects the prime-power signature to the squarefree signature. The known endpoint counts are \(\mathcal K((m))=2^m\) and \(\mathcal K((1,\ldots,1))=2\sum_{j=1}^{m}j!\,{m\brace j}\), obtained respectively from exponent compositions and ordered partitions of \(m\) labeled prime factors. The strictness of the splits determines their equality cases.

**5. Exact finite evaluation.** The polynomial \(P_{\mathbf a}(k)\) has degree \(m\) and \(P_{\mathbf a}(0)=0\). By Newton's forward expansion, \(P_{\mathbf a}(k)=\sum_{j=0}^m\Delta^jP_{\mathbf a}(0)\binom{k}{j}\). The identity \(\sum_{k=0}^{\infty}2^{-k}\binom{k}{j}=2\) for every \(j\ge0\) then gives \(\mathcal K(\mathbf a)=2\sum_{j=1}^m\Delta^jP_{\mathbf a}(0)\). This finite formula is already represented in the literature in an equivalent form and is given solely to specify the sharp constants constructively.

## Verification

The accompanying `verify.py` computes \(\kappa_0\) from its original proper-divisor recursion on exponent lattices and, separately, from forward differences of the binomial product. It checks every unordered positive exponent signature with \(1\le m\le11\), verifies every eligible strict balancing and splitting move, and verifies both fixed-support sharp endpoints and the classical global endpoints. The actual output in `verification_output.txt` reports 194 signatures, 410 balancing transfers, and 910 splitting comparisons. As examples, for \(m=6,r=2\), the sharp lower signature \((5,1)\) has count \(224\) and upper signature \((3,3)\) has count \(504\); for \(m=7,r=3\), these are \((5,1,1)\mapsto1952\) and \((3,2,2)\mapsto6344\). The finite tests are regression checks; the unrestricted theorem follows from the symbolic proof, not enumeration.

## Relationship to prior work

Fink's *Recursively divisible numbers* (first arXiv posting 2019-12-17) introduced and investigated this recursion, related \(\kappa_0\) to ordered factorizations, and computed the prime-power and squarefree cases. Fink's 2023 *Properties of the recursive divisor function and the number of ordered factorizations* proves the positive convolution series. Fink's distinct 2023 paper *Number of ordered factorizations and recursive divisors*, Theorems 1 and 2, gives **exactly** the infinite binomial series and the finite binomial-difference representation above. Neither formula is presented here as new.

Knopfmacher and Mays's author-provided *A Survey of Factorization Counting Functions* includes MacMahon's general formula, tables by prime-exponent signature, and remarks that a total ordering which makes all factorization-counting columns monotone breaks in higher multiplicity. This finding addresses a different, precisely restricted **majorization partial order**, including all fixed-support extremal signatures, without claiming a total order or comparative results for unordered factorizations. Coppersmith and Lewenstein treat global growth upper/lower bounds for ordered factorizations, rather than fixed-\((m,r)\) sharp extremal signatures. The known formulas and endpoint values are treated as antecedents; strict transfer/split inequalities and the resulting exact fixed-support envelope are the new claim.

## Limitations

No comparison is asserted for two different exponent signatures incomparable under majorization, even when they share \(m\) and \(r\). The theorem does not optimize \(\kappa_0(n)\) subject to a bound on the numerical size of \(n\), nor does it extend automatically to other recursive divisor weights. Although the focal primary literature and several equivalent formulations were inspected, an uncatalogued classical statement of strict majorization monotonicity in the extensive factorization literature remains a residual originality risk. 
## References

1. T. M. A. Fink, *Recursively divisible numbers*, arXiv:1912.07979, initially submitted 2019-12-17, https://arxiv.org/abs/1912.07979 (full text https://arxiv.org/html/1912.07979v2).
2. T. M. A. Fink, *Properties of the recursive divisor function and the number of ordered factorizations*, arXiv:2307.09140, https://arxiv.org/html/2307.09140v1.
3. T. M. A. Fink, *Number of ordered factorizations and recursive divisors*, arXiv:2307.16691, Theorems 1–2, https://arxiv.org/pdf/2307.16691.
4. A. Knopfmacher and M. E. Mays, *A Survey of Factorization Counting Functions*, International Journal of Number Theory 1 (2005), 563–581, https://doi.org/10.1142/S1793042105000315 (author-provided manuscript text at https://www.researchgate.net/publication/263873839_A_SURVEY_OF_FACTORIZATION_COUNTING_FUNCTIONS).
5. D. Coppersmith and M. Lewenstein, *Constructive bounds on ordered factorizations*, SIAM Journal on Discrete Mathematics 19 (2005), 301–303, https://doi.org/10.1137/S0895480104445861 (author-provided preprint at https://www.researchgate.net/publication/220533137_Constructive_Bounds_on_Ordered_Factorizations).
