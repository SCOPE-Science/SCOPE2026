# An exponent-one log-log saving for sums of a prime and a Zumkeller number

## Finding

A *Zumkeller number* is a positive integer whose complete set of positive divisors admits a partition into two equal-sum classes. Let \(\mathcal E\) consist of positive integers that cannot be written as a prime plus a Zumkeller number, and put \(\alpha(X)=\#\{n\le X:n\in\mathcal E\}\). Then, as \(X\to\infty\),

\[
\boxed{\alpha(X)\ll\frac{X}{\log\log X}.}
\]

The proof also identifies a sharp density mechanism. There is a sequence of pairwise coprime *odd* Zumkeller numbers \(z_1,z_2,\ldots\) obtained from minimally abundant consecutive-prime blocks, such that, writing \(P_j\) for the smallest prime dividing \(z_j\),

\[
\frac{\varphi(z_j)}{z_j}=\frac12+O(P_j^{-1}),\qquad
\prod_{j=1}^{r}\left(1-\frac{\varphi(z_j)}{z_j}\right)
\sim K2^{-r}
\]

for a finite constant \(K>1\) depending on the starting block. For *any* family of odd Zumkeller seeds, each factor \(1-\varphi(z_j)/z_j\) exceeds \(1/2\); hence the failure-density factor \(1/2\) is sharp **per seed** in such coprimality sieves. This does not bound the number of usable seeds for a given \(X\), and is not a global lower bound for \(\alpha(X)\).

## Assumptions and scope

All primes are positive rational primes, all logarithms are natural, and the implicit constants are absolute once a sufficiently large first prime block and a fixed Linnik exponent \(L>1\) are chosen. The estimate holds as \(X\to\infty\); no explicit effective starting value for \(X\) is claimed. The proof uses standard Mertens estimates, Bertrand's postulate, Linnik's least-prime bound, and the established existence of odd Zumkeller consecutive-prime blocks. No unproved hypotheses on prime gaps are required.

For the block construction, write \(p_k\) for the \(k\)-th prime. Let \(f(k)\) be the first integer \(m\ge k\) satisfying

\[
B_k:=\prod_{i=k}^{m}\left(1+\frac1{p_i}\right)\ge2,
\]

and set \(A_k=\prod_{i=k}^{f(k)}p_i\). The cited theorem of Somu--Kukla--Tran establishes that \(A_k\) is an odd Zumkeller number for all sufficiently large \(k\).

## Proof

**1. Exact local factor and its limiting value.** Let \(P=p_k\), \(Q=p_{f(k)}\). Minimality gives

\[
2\le B_k<2(1+Q^{-1})\quad\text{and}\quad
C_k:=\prod_{i=k}^{f(k)}(1-p_i^{-2})=1+O(P^{-1}).
\]

The latter follows, uniformly in the final index, from \(0\le1-C_k\le\sum_{m\ge P}m^{-2}=O(P^{-1})\). Since \(A_k\) is squarefree, the identity \((1-p^{-1})=(1-p^{-2})/(1+p^{-1})\) gives

\[
\frac{\varphi(A_k)}{A_k}=\frac{C_k}{B_k}=\frac12+O(P^{-1}).
\]

Furthermore, for *every* Zumkeller integer \(z=\prod p^{a_p}\), its equal-sum partition forces \(\sigma(z)\ge2z\), while

\[
\frac{\varphi(z)\sigma(z)}{z^2}=
\prod_{p^{a_p}\parallel z}(1-p^{-a_p-1})<1.
\]

Therefore \(\varphi(z)/z<1/2\) for every Zumkeller \(z\). For the blocks the previous estimate is consequently approached strictly from below.

**2. Size and spacing of the blocks.** Mertens' theorem and the absolutely convergent series \(\sum_p p^{-2}\) imply

\[
\log B_k=\log\log Q-\log\log P+O((\log P)^{-1}).
\]

Combining with \(\log B_k=\log2+O(Q^{-1})\) yields \(\log Q=2\log P+O(1)\), uniformly as \(k\to\infty\). In particular, \(Q\asymp P^2\). Choose the first index \(s_1\) past the threshold of the odd Zumkeller-block theorem, then recursively set \(s_{j+1}=f(s_j)+1\), \(P_j=p_{s_j}\), \(Q_j=p_{f(s_j)}\), and \(z_j=A_{s_j}\). Their prime supports are disjoint, so \(z_j\) are pairwise coprime. Bertrand's postulate and \(Q_j\asymp P_j^2\) give \(P_{j+1}\asymp P_j^2\). Thus \(\log P_j\ll2^j\), while the Chebyshev bound \(\vartheta(y)\ll y\) gives, for a fixed \(D>0\),

\[
\log z_j\le\vartheta(Q_j)\ll Q_j\le\exp(D2^j)
\quad(j\ge1).
\]

By starting sufficiently far out, \(P_{j+1}>2P_j\) holds throughout. Hence \(\sum_jP_j^{-1}<\infty\), and step 1 shows that

\[
\prod_{j=1}^{r}\left(1-\frac{\varphi(z_j)}{z_j}\right)
=2^{-r}\prod_{j=1}^{r}\bigl(1+O(P_j^{-1})\bigr)
\sim K2^{-r},\quad 1<K<\infty.
\]

The factors in this final product are each strictly greater than one. Conversely, for any sequence of odd Zumkeller seeds, step 1 shows that its product of coprimality-failure densities is strictly greater than \(2^{-r}\). This identifies the sharp failure-density factor per independent seed without asserting sharpness of the true exceptional count or of the number of seeds available below a given height.

**3. Representations above a uniform odd-seed threshold.** Fix one odd Zumkeller number \(z\), and write \(R=\operatorname{rad}(z)\). Because coprime positive multiples of Zumkeller numbers are Zumkeller, each \(z(2Rm+1)\), \(m\ge1\), is Zumkeller. For even \(n\) with \(\gcd(n,z)=1\), the residue \(n-z\) is coprime to \(2zR\). A least prime \(q\equiv n-z\pmod{2zR}\) is \(\ll(2zR)^L\ll z^{2L}\) by Linnik's theorem, uniformly in the residue. For \(n\) larger than the latter bound plus \(z\), one has \(n-q-z>0\) and it is divisible by \(2zR\); consequently

\[
n=q+z\left(2R\frac{n-q-z}{2zR}+1\right)
=q+z(2Rm+1),\qquad m\ge1.
\]

Thus any exceptional even \(n\) above an absolute multiple of \(z^{2L}\) must satisfy \(\gcd(n,z)>1\). This reconstructs the quantitative mechanism of Li's Lemma 3.2, including its uniformity in the residue class.

**4. Exact finite-interval CRT bound.** Put \(Z_r=\prod_{j\le r}z_j\). An exceptional even integer \(n\le X\), unless it lies beneath the largest seed threshold, satisfies \(\gcd(n,z_j)>1\) for every \(j\le r\). There are exactly \(z_j-\varphi(z_j)\) forbidden residue classes modulo \(z_j\). CRT, together with evenness modulo \(2\), gives precisely \(\prod_{j\le r}(z_j-\varphi(z_j))\) classes modulo \(2Z_r\); each contributes at most \(X/(2Z_r)+1\) integers up to \(X\). Therefore

\[
\#\{n\le X:n\in\mathcal E,\ 2\mid n\}
\ll \max_{j\le r}z_j^{2L}
+X2^{-r}+Z_r.
\]

The last term is the finite-interval residue-class error and cannot in general be deleted.

**5. Choice of sieve depth.** Enlarge \(D\) if necessary so that all bounds \(\log z_j\le\exp(D2^j)\) hold. For sufficiently large \(X\), select

\[
r=\left\lfloor\log_2\left(\frac{\log\log X}{2D}\right)\right\rfloor.
\]

Then \(2^r\asymp\log\log X\) and \(\max_{j\le r}\log z_j\le(\log X)^{1/2}\). Also \(\log Z_r\le r(\log X)^{1/2}=o(\log X)\). Consequently \(\max_jz_j^{2L}+Z_r=X^{o(1)}\), which is \(O(X/\log\log X)\). Step 4 proves the asserted bound for the even exceptional integers.

**6. Odd integers.** Let \(p\) be any odd prime and choose the least \(t\ge1\) with \(2^{t+1}-1>p\). The known two-prime Zumkeller criterion makes \(w=p2^t\) Zumkeller, with \(w\ll p^2\). Every \(w(2pm+1)\) is Zumkeller. For odd \(n\) with \(p\nmid n\), the residue \(n-w\) is coprime to \(2pw\), a modulus \(\ll p^3\). As in step 3, Linnik yields a representation \(n=q+w(2pm+1)\) whenever \(n\gg p^{3L}\). Choosing an odd prime \(p\asymp X^{1/(3L+1)}\) by Bertrand, the number of exceptional odd \(n\le X\) is \(O(p^{3L}+X/p)=O(X^{1-1/(3L+1)})\). This is \(o(X/\log\log X)\). Combining parities proves the theorem.

## Verification

The analytical proof uses unrestricted prime blocks and standard asymptotic theorems. The supplied `verify.py` checks the minimal threshold, exact rational Euler-product identities, monotone convergence toward \(1/2\) in six finite prime blocks, CRT forbidden-class counts for four independently selected coprime modulus families, and the divisor/totient inequality for several known Zumkeller numbers. Execute with `python3 verify.py`. Successful execution prints `VERIFY_OK`. These finite checks are not a proof of the infinite asymptotic statement.

## Relationship to prior work

Li (arXiv:2610.19574v1, Theorem 1.2) proves \(\alpha(X)\ll X/(\log\log X)^A\), with \(A=\log_2(2\pi^2/(2\pi^2-3))\approx0.2378\), and constructs disjoint prime blocks using the weaker uniform estimate \(\varphi(z_j)/z_j>3/(2\pi^2)\). The present result uses **the same natural blocks** but obtains the limiting value \(1/2\), a summable local error, and a finite-interval CRT remainder, giving exponent \(1\). Somu--Kukla--Tran (arXiv:2310.14149v2, Lemma 3.3) supplies the crucial published theorem that sufficiently late blocks are genuinely Zumkeller; their proof invokes the divisor-subset lemmas of Benkoski and Erdős. This argument does not establish that the resulting exponent is best possible for all methods, nor that no wider theorem implicitly covers it.

## Limitations

The bound is asymptotic and has no explicit numerical threshold. Its implied constant depends on an existential starting index for odd Zumkeller blocks and a fixed exponent in Linnik's theorem; no computation certifies that index. The result does not classify individual exceptional integers, give a lower bound of order \(X/\log\log X\), or settle any optimal global exponent. The structural density optimality concerns only the indicated independent-seed coprimality sieve. An equivalent result may occur implicitly in stronger unlocated analytic-number-theory literature; independent mathematical validation has not been performed.

## References

1. T. H. S. Li, *The Density and Quantitative Upper Bound of Integers Not Expressible as the Sum of a Prime and a Zumkeller Number*, arXiv:2610.19574v1 (first public version October 14, 2026), Theorem 1.2 and Lemmas 2.1--2.5 and 3.1--3.3. https://arxiv.org/html/2610.19574v1
2. S. T. Somu, A. Kukla and D. V. K. Tran, *Some Results on Zumkeller Numbers*, arXiv:2310.14149v2 (first public version October 22, 2023), Lemma 3.3. https://arxiv.org/html/2310.14149v2
3. S. J. Benkoski and P. Erdős, *On Weird and Pseudoperfect Numbers*, Math. Comp. 28 (1974), 617--623, Lemmas 1 and 2. https://www.renyi.hu/~p_erdos/1974-24.pdf
4. U. V. Linnik, *On the least prime number in an arithmetic progression. I*, Mat. Sb. 15(57) (1944), 139--178.
5. Standard prime-reciprocal Mertens theorem, Chebyshev's estimate for \(\vartheta\), and Bertrand's postulate, as stated in the references of item 1.
