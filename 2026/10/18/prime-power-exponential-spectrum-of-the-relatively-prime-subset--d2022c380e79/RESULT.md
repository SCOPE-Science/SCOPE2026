# Prime-power exponential spectrum of the relatively-prime-subset deficit

## Finding

For a positive integer \(n\), let \(f(n)\) count the nonempty subsets of \(\{1,\ldots,n\}\) having greatest common divisor one, let \(D(n)=\sum_{d\mid n}f(d)\), and let \(\Phi(n)\) count the nonempty subsets whose gcd is coprime to \(n\). These are the classical functions studied by Pongsriiam. Set
\[
\Delta_D(n)=2^n-D(n),\qquad \Delta_\Phi(n)=2^n-\Phi(n).
\]
For every \(n\ge3\), define the *least nondivisor* \(r(n)=\min\{d\ge2:d\nmid n\}\) and the smallest prime factor \(q(n)=\min\{p:p\text{ prime},\ p\mid n\}\). The following statements hold.

**Uniform first-order asymptotic.** For an absolute constant \(c>0\), as \(n\to\infty\) through all positive integers,
\[
\boxed{\Delta_D(n)=2^{\lfloor n/r(n)\rfloor}
\left(1+O\left(e^{-c n/(\log n)^2}\right)\right).}
\]
The implied constant is absolute. In particular,
\[
\frac{\log_2\Delta_D(n)}{n}=\frac1{r(n)}+O\!\left(\frac{\log n}{n}\right),
\quad
\frac1n\log_2\frac{\Delta_D(n)}{\Delta_\Phi(n)}
=\frac1{r(n)}-\frac1{q(n)}+O\!\left(\frac{\log n}{n}\right),
\]
with absolute implied constants. Consequently the ratio \(\Delta_D(n)/\Delta_\Phi(n)\) tends to infinity along odd \(n\) and to zero along even \(n\). Thus its overall limsup is infinite and its liminf is zero, as asked in Question 3.3 of the originating paper.

**Exact phase classification and limiting law.** The value \(r(n)\) is always a prime power. Write \(L_m=\operatorname{lcm}(1,\ldots,m)\), with \(L_1=1\). For each prime power \(p^a\ge2\),
\[
\boxed{r(n)=p^a\quad\Longleftrightarrow\quad
L_{p^a-1}\mid n\ \text{and}\ p\nmid\frac{n}{L_{p^a-1}}.}
\]
The natural density of this fiber is exactly
\[
\boxed{w_{p^a}=\frac{1-1/p}{L_{p^a-1}}.}
\]
These weights sum to one. More precisely, the empirical probability distribution of
\[
Y_n=\frac{\log_2(2^n-D(n))}{n},\qquad n\ge3,
\]
where the empirical measure is explicitly \(\frac{1}{\lfloor X\rfloor-2}\sum_{3\le n\le\lfloor X\rfloor}\delta_{Y_n}\) for \(X\ge3\), converges weakly as \(X\to\infty\) to the **purely atomic probability measure**
\[
\boxed{\mu=\sum_{p\ \mathrm{prime}}\sum_{a\ge1}
\frac{1-1/p}{L_{p^a-1}}\,\delta_{1/p^a}.}
\]
Its first four atoms have locations \(1/2,1/3,1/4,1/5\) and respective weights \(1/2,1/3,1/12,1/15\), totaling \(59/60\). There is no atom at zero.

## Assumptions and scope

All subsets are nonempty and taken from \(\{1,\ldots,n\}\); the gcd of a singleton is its element. All limits are over positive integers, and weak convergence means convergence of integrals against bounded continuous test functions on \(\mathbb R\). The pointwise assertions use \(n\ge3\), while the fiber equivalence holds for every \(n\ge1\) (with \(r(1)=2\) and \(r(2)=3\)). The source date refers to the first public preprint of the founding paper, not to a later journal edition.

## Proof

**Step 1: partition by the exact gcd.** Every nonempty subset \(A\subseteq\{1,\ldots,n\}\) with \(\gcd(A)=g\) is uniquely obtained by multiplying a gcd-one subset of \(\{1,\ldots,\lfloor n/g\rfloor\}\) by \(g\). Hence the exact identities
\[
2^n-1=\sum_{g=1}^n f(\lfloor n/g\rfloor),\qquad
D(n)=\sum_{\substack{1\le g\le n\\g\mid n}}f(\lfloor n/g\rfloor),
\]
\[
\Phi(n)=\sum_{\substack{1\le g\le n\\\gcd(g,n)=1}}f(\lfloor n/g\rfloor).
\]
The middle equality also follows by changing variables in the divisor sum defining \(D\). Thus
\[
\Delta_D(n)=1+\sum_{\substack{1\le g\le n\\g\nmid n}}f(\lfloor n/g\rfloor),\qquad
\Delta_\Phi(n)=1+\sum_{\substack{1\le g\le n\\\gcd(g,n)>1}}f(\lfloor n/g\rfloor).
\]

**Step 2: a uniform exponential main term.** Every subset containing one has gcd one. Also a subset with gcd greater than one has all its elements divisible by some \(d\ge2\). A union bound therefore gives, for every \(t\ge1\),
\[
2^{t-1}\le f(t)\le2^t-1,\qquad
0\le2^t-1-f(t)\le
\sum_{d=2}^t(2^{\lfloor t/d\rfloor}-1)
\le t2^{\lfloor t/2\rfloor}.
\]
Fix \(n\ge3\), and abbreviate \(r=r(n)\) and \(t=\lfloor n/r\rfloor\). Every smaller positive divisor index divides \(n\), while \(r\nmid n\). Isolate the term indexed by \(g=r\) in the exact deficit sum. Every remaining index is at least \(r+1\), so
\[
\left|\Delta_D(n)-2^t\right|
\le t2^{\lfloor t/2\rfloor}
+n2^{\lfloor n/(r+1)\rfloor}.
\tag{1}
\]
To make this estimate uniform when \(r\) varies, observe that \(L_{r-1}\mid n\). For every integer \(m\ge1\) and \(0\le k\le m\), \(\binom{m}{k}\mid L_m\): for a prime \(p\), Legendre's formula expresses its valuation as a sum of at most \(\lfloor\log_p m\rfloor\) carries, each in \(\{0,1\}\). Since the maximum binomial coefficient is at least \(2^m/(m+1)\),
\[
n\ge L_{r-1}\ge\frac{2^{r-1}}r.
\]
It follows, elementarily, that \(r=O(\log n)\) with an absolute constant. Moreover,
\[
t\ge\frac nr-1,\qquad
 t-\left\lfloor\frac n{r+1}\right\rfloor
\ge\frac{n}{r(r+1)}-1.
\]
Dividing (1) by \(2^t\) and using \(r=O(\log n)\) proves the displayed uniform relative error with some absolute \(c>0\). No probabilistic or numerical extrapolation is used.

For \(q=q(n)\), the smallest index \(g\ge2\) with \((g,n)>1\) is \(g=q\). Let \(s=\lfloor n/q\rfloor\). The same partition and the elementary bounds on \(f\) give
\[
2^{s-1}\le\Delta_\Phi(n)\le1+n2^s,
\quad
2^{t-1}\le\Delta_D(n)\le1+n2^t.
\]
Taking logarithms and using \(\lfloor n/r\rfloor/n=1/r+O(1/n)\) (and similarly for \(q\)) yields the uniform exponent identities. For odd \(n\), \(r=2\), \(q\ge3\), and \(1/r-1/q\ge1/6\); for even \(n\), \(q=2\), \(r\ge3\), and \(1/r-1/q\le-1/6\). Hence the claimed contrasting ratio limits.

**Step 3: exact prime-power phases.** If the least nondivisor \(r\) had at least two distinct prime divisors, its coprime prime-power factors would each be smaller than \(r\), hence would each divide \(n\), forcing \(r\mid n\), a contradiction. So \(r=p^a\). Conversely, the requirement that all positive integers less than \(p^a\) divide \(n\) is exactly \(L_{p^a-1}\mid n\). Since the \(p\)-valuation of this least common multiple is \(a-1\), the additional requirement \(p^a\nmid n\) is exactly \(p\nmid n/L_{p^a-1}\). This proves the fiber equivalence. Its density follows by counting multiples of \(L_{p^a-1}\) with quotient not divisible by \(p\).

**Step 4: total mass and distribution.** The condition \(r(n)>R\) is equivalent to \(L_R\mid n\), so for each fixed positive integer \(R\) its natural density is \(1/L_R\). The fibers with \(r\le R\) partition its complement. Therefore
\[
\sum_{p^a\le R}w_{p^a}=1-\frac1{L_R}.
\]
Since \(L_R\to\infty\), the weights sum to one. For each fixed prime power \(p^a\), the uniform exponent estimate shows \(Y_n\to1/p^a\) along that fiber. Given a bounded continuous test function, truncate to fibers \(r\le R\). Their frequencies converge to the displayed weights, while the remaining density equals \(1/L_R\), which can be made arbitrarily small. Let \(R\to\infty\) to obtain the claimed weak limit. The first four weights follow from \(L_1=1\), \(L_2=2\), \(L_3=6\), \(L_4=12\).

## Verification

`CHECK.py` is a complete standard-library integer checker. Run `python3 CHECK.py` from the directory holding this document. It independently constructs \(f(t)\) using the gcd-partition recursion through \(t=450\), checks it against exhaustive subset gcd enumeration through \(t=17\), verifies both exact deficit identities, elementary exponential envelopes and alternating comparisons through \(n=450\), and checks prime-power fiber identities at multiple moduli. Successful output ends with `VERIFY_OK`. The finite tests corroborate the theorem; Steps 1–4 supply the proof for every admissible \(n\).

## Relationship to prior work

Pongsriiam's 2013 article defined \(f,\Phi,D\), proved the divisor-sum/gcd interpretation of \(D\) (Corollary 9), supplied summatory asymptotics (Theorem 3), and explicitly asked about limit superior and inferior of the ratio \((2^n-D(n))/(2^n-\Phi(n))\) (Question 3.3). Pongsriiam's later *Local behaviors* study already proves the alternating sign of \(D(n)-\Phi(n)\) (Theorem 9); that sign result is **not** claimed as new here. The present contribution is the uniform *pointwise* least-nondivisor asymptotic, prime-power phase classification, exact all-phase density, and full limiting measure for its logarithmic deficit, as well as the explicit exponential comparison rate. The OEIS A224840 entry tabulates \(D(n)\) and states its gcd-subset characterization; these alone do not contain the pointwise spectrum or limiting law. These comparisons do not exclude every uncatalogued equivalent theorem.

## Limitations

The statement concerns the complete family of subsets of an initial integer interval with the ordinary gcd; it makes no claim for arbitrary sets or other gcd statistics. The limiting measure describes the exponentially rescaled *deficit*, not a central limit theorem for subset samples. The result does not determine the exact unnormalized sums raised in the second half of the 2013 Question 3.3. Full independent validation and exhaustive historical literature coverage have not been performed. The proof's global error term is qualitative in its absolute constant.

## References

1. P. Pongsriiam, “Relatively Prime Sets, Divisor Sums, and Partial Sums,” *Journal of Integer Sequences* **16** (2013), Article 13.9.1; publicly posted 2013-06-20 as arXiv:1306.4891. https://arxiv.org/abs/1306.4891 ; full journal text https://www.maths.tcd.ie/EMIS/journals/JIS/VOL16/Pongsriiam/pong2.pdf .
2. P. Pongsriiam, “Local behaviors of the number of relatively prime sets,” *International Journal of Number Theory* **12** (2016), 1575–1593, DOI:10.1142/S1793042116500962; author manuscript available at https://www.researchgate.net/publication/287391047_Local_behaviors_of_the_number_of_relatively_prime_sets .
3. OEIS A224840, “Divisor sum of the arithmetic function A085945(n),” https://oeis.org/A224840 .
