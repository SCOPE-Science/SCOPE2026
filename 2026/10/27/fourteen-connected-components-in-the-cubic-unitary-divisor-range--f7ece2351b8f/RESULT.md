# Fourteen connected components in the cubic unitary-divisor range

## Finding
For a real exponent \(t\), let \(\sigma_t^*(n)\) be the sum of the \(t\)-th powers of the unitary divisors of the positive integer \(n\). Thus \(\sigma_t^*(p^a)=1+p^{at}\) for every prime \(p\) and integer \(a\ge1\). At \(t=-3\), the closure
\[
\mathcal R_3=\overline{\{\sigma_{-3}^*(n):n\ge1\}}\subset\mathbb R
\]
has **exactly fourteen connected components**, each a nondegenerate closed interval. Their precise endpoints are as follows.

Set
\[
T=\prod_{p\ge11\;\mathrm{prime}}(1+p^{-3})
 =\frac{\zeta(3)}{\zeta(6)\prod_{p\in\{2,3,5,7\}}(1+p^{-3})},
\]
and, for \(\mathbf a=(a_2,a_3,a_5,a_7)\) with nonnegative integer entries, set
\[
U(\mathbf a)=\prod_{\substack{p\in\{2,3,5,7\}\\a_p>0}}(1+p^{-3a_p}).
\]
Then
\[
\boxed{\displaystyle \mathcal R_3=\bigcup_{j=1}^{14}[U(\boldsymbol\ell_j),\,T U(\boldsymbol r_j)]},
\]
where the intervals are listed in strictly increasing, mutually disjoint order in the following **exact** table.

| \(j\) | \(\boldsymbol\ell_j\) | \(\boldsymbol r_j\) | Number of contributing intervals |
| ---: | :---: | :---: | ---: |
| 1 | \((0,0,0,0)\) | \((2,2,2,1)\) | 66 |
| 2 | \((2,0,1,0)\) | \((2,2,1,1)\) | 6 |
| 3 | \((0,1,0,0)\) | \((3,1,2,1)\) | 18 |
| 4 | \((0,1,1,0)\) | \((3,1,1,1)\) | 9 |
| 5 | \((2,1,0,0)\) | \((2,1,2,2)\) | 4 |
| 6 | \((2,1,0,1)\) | \((2,1,2,1)\) | 2 |
| 7 | \((2,1,1,0)\) | \((2,1,1,2)\) | 2 |
| 8 | \((2,1,1,1)\) | \((2,1,1,1)\) | 1 |
| 9 | \((1,0,0,0)\) | \((1,2,2,1)\) | 12 |
| 10 | \((1,0,1,0)\) | \((1,2,1,1)\) | 6 |
| 11 | \((1,1,0,0)\) | \((1,1,2,2)\) | 4 |
| 12 | \((1,1,0,1)\) | \((1,1,2,1)\) | 2 |
| 13 | \((1,1,1,0)\) | \((1,1,1,2)\) | 2 |
| 14 | \((1,1,1,1)\) | \((1,1,1,1)\) | 1 |

In particular, \(-3\in\mathcal E_{14}^*\), where \(\mathcal E_k^*\) denotes the exponents with exactly \(k\) connected components in the closure of the unitary-divisor range.

## Assumptions and scope
The closure is taken in the real line; a prime omitted from \(n\) supplies factor \(1\). An integer containing a prime to a positive exponent \(a\) supplies factor \(1+p^{-3a}\). All infinite products below converge absolutely. The claim is for the single natural parameter \(t=-3\), not for an interval of parameters or a monotonicity law.

## Proof
**1. Connectedness of the prime tail.** Enumerate the primes \(p_1=2,p_2=3,\ldots\), and write
\[
w_j=\log(1+p_j^{-3}),\qquad S_j=\sum_{i>j}w_i.
\]
For each \(j\ge10\), Defant's established prime-ratio lemma [1, Lemma 2.2] gives \(p_{j+1}^3<2p_j^3\). As \(u\mapsto\log(1+u)/u\) strictly decreases on \((0,\infty)\), we have \(w_j<2w_{j+1}\). If \(S_j<w_j\) at some such index, then
\[
S_{j+1}=S_j-w_{j+1}<w_j-w_{j+1}<w_{j+1},
\]
so the failure persists at every larger index. This is impossible: the prime number theorem gives \(\pi(2x)-\pi(x)\to\infty\), and for \(p_j=x\),
\[
\frac{S_j}{w_j}\ge
\bigl(\pi(2x)-\pi(x)\bigr)
\frac{\log(1+(2x)^{-3})}{\log(1+x^{-3})}
\longrightarrow\infty.
\]
Thus \(w_j\le S_j\) for every \(j\ge10\).

For \(j=5,6,7,8,9\), respectively, the strictly stronger finite rational inequalities
\[
1+p_j^{-3}<\prod_{q\in Q_j}(1+q^{-3})
\]
hold for the sets of later primes
\[
\begin{aligned}
Q_5&=\{13,17,19\},&Q_6&=\{17,19,23,29\},\\
Q_7&=\{19,23\},&Q_8&=\{23,29,31\},\\
Q_9&=\{29,31,37\}.
\end{aligned}
\]
The inequalities are checked as exact rational comparisons by `verify.py`. Hence \(w_j\le S_j\) for all \(j\ge5\).

A standard greedy lemma for positive summable weights states that if each weight is at most the sum of the weights after it, then their subsums exhaust the full interval from zero to the total sum. Indeed, for a residual target in \([0,w_j+S_j]\), omit \(w_j\) if the target is at most \(S_j\); otherwise include \(w_j\). The resulting residual belongs to \([0,S_j]\), and the residual tends to zero because the remaining total tends to zero. Applying this lemma to the \(w_j\) for \(j\ge5\) shows that the closure of finite products \(\prod_{j\ge5}(1+p_j^{-3})^{\varepsilon_j}\), \(\varepsilon_j\in\{0,1\}\), is precisely \([1,T]\). These finite products come from squarefree integers supported on primes at least \(11\). Conversely, allowing higher prime exponents cannot give products outside \([1,T]\), since \(1+p^{-3a}\le1+p^{-3}\). Thus the **full** unitary-divisor tail closure for primes \(p\ge11\) is exactly \([1,T]\).

**2. Finite reduction at the four small primes.** For \(p=2,3,5,7\), let \(h_{p,a}=1+p^{-3a}\), and put \(A_2=4\) and \(A_3=A_5=A_7=2\). Exact rational product bounds in Step 3 give \(h_{p,A_p}\le T\) for each of these primes. For every \(a\ge A_p\), the interval \(h_{p,a}[1,T]\) is contained in \([1,h_{p,A_p}T]\). Meanwhile \([1,T]\cup h_{p,A_p}[1,T]=[1,h_{p,A_p}T]\), because \(h_{p,A_p}\le T\). This equality remains valid after multiplication by any fixed factor contributed by the other three primes. Therefore **all** exponents at a small prime can be replaced without loss by the finite options \(a=0,1,\ldots,A_p\). It follows that
\[
\mathcal R_3=\bigcup_{\mathbf a\in\{0,1,2,3,4\}\times\{0,1,2\}^3}
[U(\mathbf a),T U(\mathbf a)].
\]
This is an exact reduction to \(5\cdot3^3=135\) rationally placed intervals, not a numerical truncation of the original range.

**3. Rational certificate for the fourteen maximal intervals.** Let \(Q=1000\) and let
\[
T_-=\prod_{\substack{11\le p\le Q\\p\text{ prime}}}(1+p^{-3}),
\qquad
T_+=\frac{T_-}{1-1/(2Q^2)}.
\]
The integral test gives \(\sum_{n>Q}n^{-3}\le1/(2Q^2)\). Since \(\log(1+x)\le x\) and \(e^u\le(1-u)^{-1}\) for \(0\le u<1\), one has the rigorous enclosure
\[
T_-<T<T_+.
\]
The accompanying standalone `verify.py` computes both bounds as Python `fractions.Fraction` objects and proves \(h_{p,A_p}\le T_-\). It forms all \(135\) distinct rational numbers \(U(\mathbf a)\) and, for each of the **two** enclosures, sorts the intervals \([U(\mathbf a),T_{\pm}U(\mathbf a)]\), merging intervals whenever their endpoints overlap. It verifies, by exact rational comparisons, that both lists yield **fourteen** maximal components and, crucially, identical partitions of the same \(135\) labeled intervals. Because each true interval contains its lower-enclosure interval and is contained in its upper-enclosure interval, the common partition is also exactly the partition of the true intervals. Its smallest left and largest right factor in each component are the tuples tabulated above. This proves all the exact component endpoints and all thirteen strict gaps, hence the theorem.

## Verification
Execute `python3 verify.py` (Python standard library only) in the directory containing this document. The verifier checks prime-ratio instances \(10\le j\le3099\), all five exceptional rational tail inequalities, the four exponent cutoffs, all \(135\) rational support factors, both rigorous enclosures for the tail product, and the matching fourteen-component partitions. Its output begins `VERIFY_OK prime_ratio_indices 3090 small_prime_tail_cases 5 head_products 135 connected_components 14 prime_product_cutoff 1000` and then reports the component endpoint patterns. Finite checks for prime ratios supplement, but do not replace, the published infinite prime-ratio lemma used in Step 1. The infinite interval claim follows from the analytic argument, not the finite enumeration alone.

## Relationship to prior work
Defant [1] proved the connectedness threshold \(\eta^*\approx1.974255\) for unitary divisor ranges and posed the problem of determining the parameter sets \(\mathcal E_k^*\). His result implies only **disconnectedness** at \(t=-3\), not the number or exact endpoints of components. A subsequently published exact decomposition at \(t=-2\) [2] gives exactly two components there but not at \(t=-3\). The ordinary (nonunitary) divisor-function papers by Zubrilina [3] and Achenjang–Berger [4] concern different Euler factors and do not imply this theorem. In particular, the integer \(14\) here is not obtained from the ordinary-divisor component count. This result provides one further exact point of Defant's component-count spectrum, with thirteen explicit gaps.

## Limitations
The classification does not describe parameter neighborhoods around \(-3\), determine the structure for arbitrary real exponents, or establish monotonicity of the component count. The proof relies on the published prime-ratio lemma and the prime number theorem; its finite certificate is not an independent proof of those infinite facts. Prior-art searches cannot eliminate the risk of unindexed equivalent work. No independent mathematical validation is asserted.

## References
1. C. Defant, *Ranges of Unitary Divisor Functions*, arXiv:1507.02654, first version 2015-07-09, published in *Integers* 18 (2018), A15. Primary MSC 11B05.
2. *Exactly two connected components for the unitary divisor range at \(t=-2\)*, published research record, 2026-10-04, identifier `2026/10/4/SCOPE-exactly-two-connected-components-for-the-unitary-divisor-range-a--95ec686c61cb`.
3. N. Zubrilina, *On the Number of Connected Components of Ranges of Divisor Functions*, arXiv:1711.02871 (2017).
4. N. Achenjang and A. Berger, *On Gaps in the Closures of Images of Divisor Functions*, arXiv:1808.07550 (2018).
