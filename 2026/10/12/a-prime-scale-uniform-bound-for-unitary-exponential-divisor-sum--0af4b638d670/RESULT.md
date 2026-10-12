# A prime-scale uniform bound for unitary–exponential divisor-sum level sets

## Finding
Write \(\sigma^*(n)\) for the sum of unitary divisors of \(n\) and \(\sigma^{(e)}(n)\) for the sum of its exponential divisors. For every real \(c>0\), put
\[
N_c(x)=\#\{1\le n\le x:\sigma^*(n)/\sigma^{(e)}(n)=c\}.
\]
For all real \(x\ge2\), the uniform estimate
\[
\sup_{c>0}N_c(x)\ll\frac{x}{\log x}
\]
holds with an absolute implied constant. More precisely,
\[
\limsup_{x\to\infty}\frac{\log x}{x}\sup_{c>0}N_c(x)
\le\frac65\frac{\zeta(2)\zeta(3)}{\zeta(6)}
=2.3323157241\ldots.
\]
In particular, the solutions of \(\sigma^*(n)=\sigma^{(e)}(n)\) number \(O(x/\log x)\) up to \(x\). This does not determine whether there are infinitely many such solutions.

## Assumptions and scope
For a prime \(p\) and integer \(a\ge1\),
\[
\sigma^*(p^a)=1+p^a,\qquad
\sigma^{(e)}(p^a)=\sum_{d\mid a}p^d.
\]
Both functions are multiplicative and equal \(1\) at \(n=1\); their ratio \(R(n)=\sigma^*(n)/\sigma^{(e)}(n)\) is positive and multiplicative. For a squarefree positive integer \(s\),
\[
R(s)=\prod_{p\mid s}(1+p^{-1})=\frac{\sigma(s)}{s}.
\]
A positive integer is called *powerful* if each prime dividing it has exponent at least two; \(1\) counts as powerful. Let \(\Phi(X,y)\) count positive integers at most \(X\) whose prime factors, if any, exceed \(y\). The only analytic input is the established rough-number bound \(\Phi(X,y)<(3/5)X/\log y\) for \(3\le y\le\sqrt X\), proved by Fan–Pomerance. No hypotheses on the arithmetic type of \(c\), nor any restriction on prime exponents in \(n\), are imposed.

## Proof
**Squarefree injectivity.** We first prove that the map \(s\mapsto \sigma(s)/s\) is injective on squarefree positive integers. If two squarefree integers have the same ratio, cancel their common prime factors to obtain coprime squarefree \(a,b\) with \(\sigma(a)/a=\sigma(b)/b\). Suppose one is not \(1\); choose the largest prime \(p\) dividing \(ab\) and interchange \(a,b\) so \(p\mid a\). Then
\[
b\sigma(a)=a\sigma(b)
\]
forces \(p\mid\sigma(a)=\prod_{q\mid a}(q+1)\) because \(p\nmid b\). For \(p\ge5\), every prime \(q\mid a\) has \(q\le p\), and \(p\mid q+1\) would force \(q=p-1\), an even nonprime. This is impossible. When the support is contained in \(\{2,3\}\), the four ratios corresponding to \(1,2,3,6\) are \(1,3/2,4/3,2\), all distinct. Thus \(a=b=1\), proving injectivity.

**Small-prime decomposition.** Fix \(0<\varepsilon<1/2\) and take \(x\) sufficiently large that \(y=x^{1/2-\varepsilon}\ge3\). Every positive integer \(n\le x\) has a unique factorization \(n=dsm\), where \(d\) collects all complete prime powers \(p^a\parallel n\) with \(p\le y\) and \(a\ge2\), the squarefree factor \(s\) collects exactly the primes \(p\le y\) with exponent \(1\), and \(m\) contains the complete prime-power factors \(p^a\parallel n\) with \(p>y\). These factors are pairwise coprime, \(d\) is powerful, and \(m\) is \(y\)-rough. Therefore
\[
R(n)=R(d)\frac{\sigma(s)}s R(m).
\]
For each fixed pair \((d,m)\), squarefree injectivity allows *at most one* \(s\) with \(R(dsm)=c\). Discarding the remaining restrictions on \(s\), we obtain the uniform bound
\[
N_c(x)\le\sum_{\substack{d\le x\\d\text{ powerful}}}\Phi(x/d,y).
\]

**Summation over powerful parts.** The reciprocal sum over powerful integers is
\[
A:=\sum_{d\text{ powerful}}\frac1d
=\prod_p\frac{1+p^{-3}}{1-p^{-2}}
=\frac{\zeta(2)\zeta(3)}{\zeta(6)}<\infty.
\]
Moreover, every powerful integer has a unique representation \(d=a^2b^3\) with \(a\ge1\) and squarefree \(b\ge1\). Summing first over \(a\) and splitting at \(b=z^{1/3}\) proves
\[
\sum_{\substack{d>z\\d\text{ powerful}}}\frac1d
\ll z^{-1/2}\sum_{b\ge1}b^{-3/2}+\sum_{b>z^{1/3}}b^{-3}
\ll z^{-1/2}\qquad(z\ge1).
\]
Indeed, for \(b\le z^{1/3}\), sum \(a^{-2}\) over \(a>\sqrt{z/b^3}\), which is at most a constant times \(\sqrt{b^3/z}\). For larger \(b\), sum all \(a^{-2}\).

If \(d\le x^{2\varepsilon}\), then \(x/d\ge x^{1-2\varepsilon}=y^2\), so the Fan–Pomerance inequality applies and gives
\[
\Phi(x/d,y)<\frac35\frac{x/d}{\log y}
=\frac{3}{5(1/2-\varepsilon)}\frac{x/d}{\log x}.
\]
For \(d>x^{2\varepsilon}\), the elementary bound \(\Phi(x/d,y)\le x/d\), followed by the powerful-tail estimate, gives \(O(x^{1-\varepsilon})\). Consequently, **simultaneously for all** \(c>0\),
\[
N_c(x)\le\frac{3A}{5(1/2-\varepsilon)}\frac{x}{\log x}
+O(x^{1-\varepsilon}).
\]
The error term is independent of \(c\). Divide by \(x/\log x\), take the limsup as \(x\to\infty\), and then let the *fixed* parameter \(\varepsilon\downarrow0\). The stated \((6/5)A\) bound follows. The uniform \(O(x/\log x)\) conclusion also follows by fixing, for example, \(\varepsilon=1/4\).

## Verification
The file `verify.py` independently evaluates the two multiplicative divisor functions from prime-power definitions for every integer up to \(100000\). It checks pairwise distinctness of all \(60794\) squarefree ratios in this range and finds equality precisely at \(1,20,45,320,6615\). Its expected output is

`VERIFY_OK limit=100000 squarefree_unique=60794 equality_hits=[1, 20, 45, 320, 6615]`

This finite computation tests definitions and small cases, **not** the infinite counting theorem. The latter rests on the elementary squarefree-injectivity proof, the reciprocal powerful-number tail, and Fan–Pomerance's explicit rough-number theorem.

## Relationship to prior work
Trudgian introduced the comparison \(\sigma^*(n)\) versus \(\sigma^{(e)}(n)\), listed the first equalities, and asked whether infinitely many equalities exist. The contemporaneous sequence OEIS A236474 records examples, not a counting upper bound. Classical Erdős–Wintner continuity methods can show qualitative zero density for individual values of \(R\), but a zero-density statement alone has no explicit \(x/\log x\) rate. Here that rate follows from a distinct mechanism: squarefree-value injectivity plus sieving the large-prime tail. Fan–Pomerance supplies the quantitative sieve estimate, not an application to divisor-sum equalities. Related published studies of the **positive comparison density** and of **bounded exponent families** likewise do not imply the unrestricted uniform level-set count.

## Limitations
The result is a uniform upper bound, not an asymptotic formula or lower bound. Its constant is an available explicit bound, not claimed optimal. It does not distinguish finite from infinite individual fibers, nor settle the infinitude question for the equality fiber. Prior work on generalized concentration of arithmetic-function values may contain stronger relevant bounds not found in the literature comparison.

## References
1. T. Trudgian, *The sum of the unitary divisor function*, arXiv:1312.4615v1, first public 2013-12-17; *Publications de l'Institut Mathématique* 97(111) (2015), 175–180, DOI 10.2298/PIM140617001T; especially Section 4.
2. K. (S.) Fan and C. Pomerance, *An inequality related to the sieve of Eratosthenes*, arXiv:2306.03339v3 (2023), Theorem 1; \(\Phi(X,y)<0.6X/\log y\) for \(3\le y\le\sqrt X\).
3. OEIS A236474, *Numbers whose sum of unitary divisors is equal to the sum of exponential divisors*, first authored 2014-01-29.
4. P. Erdős, *Remarks on number theory II. Some problems on the \(\sigma\) function*, *Acta Arithmetica* 5 (1959), 171–177, historical background on divisor-sum ratios; squarefree injectivity is reproved in full above.
