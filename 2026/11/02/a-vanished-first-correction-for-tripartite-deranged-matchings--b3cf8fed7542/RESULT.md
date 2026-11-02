# A vanished first correction for tripartite deranged matchings

## Finding

Fix an integer \(m\geq1\). Let \(G_m=K_{2m,2m,2m}\) be the complete tripartite graph with three labeled parts of cardinality \(2m\). Let \(M\) be **any** fixed perfect matching of \(G_m\). Set
\[
p_m=\frac{\operatorname{pm}(G_m-M)}{\operatorname{pm}(G_m)},
\]
where \(\operatorname{pm}(H)\) counts perfect matchings of a finite graph \(H\). Then, as the integer \(m\) tends to infinity,
\[
\boxed{p_m=e^{-3/4}\left(1+\frac{3}{128m^2}+O(m^{-3})\right).}
\]
In particular, the entire \(m^{-1}\) correction vanishes, and the first nonzero correction is positive and of order \(m^{-2}\). The implied constant is absolute and independent of the fixed matching \(M\).

The limiting value \(e^{-3/4}\) and the exact inclusion–exclusion identity used below are already known; the finding concerns the quantitative second-order expansion and its nonzero coefficient.

## Assumptions and scope

The graph is simple and undirected; all its vertices and the three parts are distinguished. A perfect matching meets every vertex exactly once. Write \((x)_{\underline r}=x(x-1)\cdots(x-r+1)\), with \((x)_{\underline0}=1\). Every perfect matching of \(G_m\) has exactly \(m\) edges between each unordered pair of parts (subtract the three partwise degree equations). Thus its orbit under independent part-preserving vertex relabeling is unique, and \(p_m\) is independent of the particular matching \(M\).

All asymptotics are along positive integers \(m\to\infty\). No exact sign or monotonicity assertion is made for every finite \(m\), and no higher-partite or growing-number-of-parts expansion is asserted.

## Proof

**Step 1: Exact finite identity.** The total perfect-matching count is
\[
\operatorname{pm}(G_m)=\binom{2m}{m}^{3}(m!)^3.
\]
The original matching \(M\) has \(m\) edges of each of the three types. Inclusion–exclusion on those \(3m\) edges (Johnston–Kayll–Palmer, equation (7) in the cited manuscript), divided by the displayed total count, gives
\[
p_m=\sum_{i,j,k=0}^{m}\frac{(-1)^{i+j+k}}{i!j!k!}
R_m(i,j)R_m(j,k)R_m(k,i),
\qquad R_m(a,b)=\frac{(m)_{\underline a}(m)_{\underline b}}{(2m)_{\underline{a+b}}}.
\tag{1}
\]
One can also establish (1) directly: choose respectively \(i,j,k\) prescribed edges between the three part pairs, then count the remaining balanced matchings by three partition choices and three bijections. The ratio of surviving choices to unrestricted choices is the product of the three displayed falling-factorial ratios.

**Step 2: Coefficient expansions.** For nonnegative fixed integers \(a,b\), Taylor expansion of the logarithms of the falling factorials yields
\[
\log R_m(a,b)=-(a+b)\log 2+\frac{\alpha(a,b)}{m}+\frac{\beta(a,b)}{m^2}
+O\!\left(\frac{(1+a+b)^4}{m^3}\right),
\]
where
\[
\alpha(a,b)=\frac{a+b-(a-b)^2}{4}
\]
and
\[
\beta(a,b)=
-\frac{a(a-1)(2a-1)+b(b-1)(2b-1)}{12}
+\frac{(a+b)(a+b-1)(2a+2b-1)}{48}.
\]
These expressions follow from the elementary finite sums
\[
\sum_{h=0}^{u-1}h=\frac{u(u-1)}2,\qquad
\sum_{h=0}^{u-1}h^2=\frac{u(u-1)(2u-1)}6.
\]
Define the symmetric three-index polynomials
\[
A(i,j,k)=\alpha(i,j)+\alpha(j,k)+\alpha(k,i),\qquad
B(i,j,k)=\beta(i,j)+\beta(j,k)+\beta(k,i).
\]
The product in (1), for indices small relative to \(m\), consequently becomes
\[
R_m(i,j)R_m(j,k)R_m(k,i)
=4^{-(i+j+k)}\left[1+\frac{A}{m}+\frac{B+A^2/2}{m^2}
+O\!\left(\frac{(1+i+j+k)^6}{m^3}\right)\right].
\tag{2}
\]

**Step 3: Rigorous exchange of expansion and infinite sum.** Take the cutoff \(L=\lfloor m^{1/10}\rfloor\). For \(0\leq i,j,k\leq L\), Taylor's formula for \(\log(1-t)\) uniformly gives the remainder in (2) with an absolute constant for sufficiently large \(m\). Indeed all underlying ratios have \(t=O(L/m)\), the third-order logarithmic remainder is bounded by a constant times \((1+i+j+k)^4/m^3\), and exponentiation adds a bounded \((1+i+j+k)^6/m^3\) remainder. Summed with the absolute factorial weights, this is \(O(m^{-3})\) because
\[
\sum_{i,j,k\geq0}\frac{4^{-(i+j+k)}(1+i+j+k)^6}{i!j!k!}<\infty.
\]
For indices outside the cutoff, \(0\le R_m(a,b)\le1\) whenever \(0\le a,b\le m\) (each is a ratio of binomial counts), so the discarded exact terms have total absolute mass at most the tail of \(\sum_{i,j,k}1/(i!j!k!)\) where at least one index exceeds \(L\). This is \(o(m^{-N})\) for every fixed \(N>0\) by factorial decay. The corresponding tails of the coefficient-polynomial series in (2) obey the same estimate. Therefore, summation of (2) through order \(m^{-2}\), with an overall \(O(m^{-3})\) error, is justified rather than merely formal.

**Step 4: Exact polynomial moments.** For a polynomial \(F\) in three variables and any real \(\lambda\), define the algebraic, not necessarily positive, linear functional
\[
\mathcal E_{\lambda}[F]=e^{-3\lambda}
\sum_{i,j,k\geq0}\frac{\lambda^{i+j+k}}{i!j!k!}F(i,j,k).
\]
It factorizes across variables. In particular,
\[
\mathcal E_{\lambda}[i]=\lambda,\quad
\mathcal E_{\lambda}[i^2]=\lambda^2+\lambda,\quad
\mathcal E_{\lambda}[i^3]=\lambda^3+3\lambda^2+\lambda,\quad
\mathcal E_{\lambda}[i^4]=\lambda^4+6\lambda^3+7\lambda^2+\lambda,
\]
with analogous identities for \(j,k\) and multiplicativity between distinct variables. Direct substitution into the explicit polynomials \(A,B\) gives the identities, valid for every \(\lambda\),
\[
\mathcal E_{\lambda}[A]=0,\qquad
\mathcal E_{\lambda}[B]=-\frac{3\lambda^2}{4},\qquad
\mathcal E_{\lambda}[A^2/2]=\frac{9\lambda^2}{8}.
\tag{3}
\]
Here we use \(\lambda=-1/4\) only as an algebraic evaluation; it is **not** a probability parameter. The normalized signed sum with factors \((-1/4)^{i+j+k}\) equals \(e^{-3/4}\mathcal E_{-1/4}[\cdot]\). The order-\(m^{-1}\) contribution vanishes by (3), while the order-\(m^{-2}\) contribution is
\[
\mathcal E_{-1/4}[B+A^2/2]
=\frac{3}{8}\left(-\frac14\right)^2=\frac{3}{128}.
\]
Inserting these values into the termwise expansion of (1) proves the claimed formula, including its remainder and matching-uniformity.

## Verification

The accompanying `verify.py` uses only the Python standard library. Execute `python3 verify.py` in a directory containing the standalone file. It independently counts perfect matchings using a vertex-mask recurrence, both with and without prescribed edges, for \(m=1,2,3\); independently evaluates the inclusion–exclusion count for \(1\leq m\leq12\); and exactly reproduces the polynomial moment identities in (3) using rational-coefficient sparse polynomials and Stirling-number moments. The successful run ends with `VERIFY_OK`.

For small \(m\), the exact fractions are \(p_1=1/2\), \(p_2=275/576\), and \(p_3=409621/864000\). These checks are consistency tests; the proof for unbounded \(m\) is the uniform summation argument above.

## Relationship to prior work

Johnston, Kayll, and Palmer (2022, arXiv:2209.11319), Theorem 5 and equation (7), establish \(p_m\to e^{-3/4}\) and supply the same exact triple inclusion–exclusion sum. Spiro and Surya (2022, arXiv:2211.01872), Theorem 1.2, prove Poisson convergence for the number of repeated matching edges in all balanced complete multipartite graphs. Granet and Joos (first public 2023, arXiv:2301.10131), Theorem 1.2, prove broader Poisson convergence in robust regular expanders. Deng (2025, arXiv:2505.13799), studies multivariate versions, and identifies quantitative convergence rates as an explicit future direction. None of those inspected theorems specifies the cancellation of the \(m^{-1}\) term and the coefficient \(3/128\) for this particular probability. The new statement strengthens the known tripartite limit, rather than claiming a new limit or new finite inclusion–exclusion formula.

## Limitations

This is a second-order asymptotic for **only the zero-overlap probability** in the three-part balanced case, not a second-order total-variation theorem for the full overlap distribution. The proof does not specify a numerical constant for the \(O(m^{-3})\) remainder or a finite cutoff beyond which the probability lies above its limit. Independent mathematical audit and exhaustive historical publication-priority verification have not occurred; an earlier equivalent expansion outside the searched literature remains possible.

## References

1. D. Johnston, P. M. Kayll, C. Palmer, *Deranged matchings: proofs and conjectures*, first public 2022-09-22, arXiv:2209.11319, https://arxiv.org/abs/2209.11319 (Section 3, especially equation (7) and Theorem 5).
2. S. Spiro, E. Surya, *Counting Deranged Matchings*, first public 2022-11-03, arXiv:2211.01872, https://arxiv.org/abs/2211.01872 (Theorem 1.2 and Section 3).
3. B. Granet, F. Joos, *Random perfect matchings in regular graphs*, first public 2023-01-24, arXiv:2301.10131, https://arxiv.org/abs/2301.10131 (Theorem 1.2).
4. B. Deng, *Deranged Perfect Matchings on complete graph and balanced complete r-partite graph*, first public 2025-05-20, arXiv:2505.13799, https://arxiv.org/abs/2505.13799 (Sections 4 and 6).
