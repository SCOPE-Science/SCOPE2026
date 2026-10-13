# Parity-separated prime-support obstructions for the alternating Lehmer divisibility

## Finding
Let \(\beta\) be the multiplicative alternating divisor-sum function, defined for every prime \(p\) and integer \(a\ge1\) by
\[
\beta(p^a)=p^a-p^{a-1}+p^{a-2}-\cdots+(-1)^a.
\]
Write \(\omega(n)\) for the number of distinct prime factors of \(n\). **Theorem.** For every composite integer \(n\) such that \(\beta(n)\mid n-1\), either \(n=4\), or
\[
\begin{cases}
\omega(n)\ge4,&\text{if }n\text{ is odd},\\
\omega(n)\ge5,&\text{if }n\text{ is even}.
\end{cases}
\]
Equivalently, \(4\) is the only composite solution with \(\omega(n)\le3\), and it is the only **even** composite solution with \(\omega(n)\le4\). Both exclusions hold for arbitrary prime exponents. No existence at the remaining thresholds is asserted.

## Assumptions and scope
All integers and exponents are positive, prime factors are distinct unless explicitly raised to powers, and divisibility has its ordinary integer meaning. The function \(\beta(1)=1\). The statement applies to every composite integer, without numerical bound; the single exception \(4\) satisfies \(\beta(4)=3\mid3\). The supporting paper is Tóth's survey, initially public on 2011-11-21; its Problem 4 asks whether any further composite solution exists.

## Proof
For any prime \(p\) and integer \(a\ge1\), the exact local identity is
\[
\frac{\beta(p^a)}{p^a}=\frac{p}{p+1}+\frac{(-1)^a}{(p+1)p^a}.
\]
It follows that \(\beta(p^a)/p^a\ge (p-1)/p\); for even \(a\) the stronger lower bound \(\beta(p^a)/p^a>p/(p+1)\) holds. The exact minimum over \(a\ge2\) is attained at \(a=3\), whence
\[
\frac{\beta(3^a)}{3^a}\ge\frac{20}{27},\qquad
\frac{\beta(5^a)}{5^a}\ge\frac{104}{125}\quad(a\ge2).
\]
In addition, \(\beta(2^a)/2^a\ge1/2\). For odd \(p\), the integer \(\beta(p^a)\) is odd exactly when \(a\) is even, since its \(a+1\) alternating terms are all odd.

**The positive quotient is at least two away from \(4\).** Tóth's exact counting identity is
\[
\beta(n)=\#\{1\le j\le n:\gcd(j,n)\text{ is a perfect square}\}.
\]
For composite \(n\neq4\), at least two integers in \([1,n]\) have nonsquare gcd with \(n\): if \(n\) has two distinct prime divisors \(p,q\), take \(j=p,q\); if \(n=p^a\) with odd \(p\) and \(a\ge2\), take \(j=p,2p\); if \(n=2^a\) with \(a\ge3\), take \(j=2,6\). Consequently \(\beta(n)<n-1\). If \(\beta(n)\mid n-1\), then
\[
K:=\frac{n-1}{\beta(n)}\in\mathbb Z,\qquad K\ge2.
\]

**Even case.** Assume \(n\neq4\) is even and \(\omega(n)\le4\). The integer \(n-1\) is odd, so \(\beta(n)\) is odd, and hence every odd-prime exponent of \(n\) is even. Writing \(n=2^a\prod_{i=1}^r p_i^{b_i}\), where \(r\le3\), yields
\[
\frac{\beta(n)}{n}\ge\frac12\prod_{i=1}^r\frac{p_i}{p_i+1}
\ge\frac12\cdot\frac34\cdot\frac56\cdot\frac78
=\frac{105}{384}>\frac14.
\]
Therefore \(K<(n/\beta(n))<4\). Being the quotient of two odd integers, \(K\) is odd; thus \(K=3\). In particular \(3\mid n-1\) and \(3\nmid n\). Now the odd primes \(p_i\) are all at least \(5\), giving the strictly stronger bound
\[
\frac{\beta(n)}n\ge\frac12\cdot\frac56\cdot\frac78\cdot\frac{11}{12}
=\frac{385}{1152}>\frac13.
\]
This forces \(K<3\), a contradiction.

**Odd case.** Suppose \(n\) is an odd composite with \(\omega(n)\le3\). The local lower bound yields
\[
\frac{\beta(n)}n\ge\prod_{p\mid n}\left(1-\frac1p\right).
\]
If \(\omega(n)\le2\), the right side is at least \((2/3)(4/5)=8/15>1/2\); if \(\omega(n)=3\) with smallest prime at least \(5\), it is at least \((4/5)(6/7)(10/11)=48/77>1/2\). If the least prime is \(3\) and the second is at least \(7\), it is at least \((2/3)(6/7)(10/11)=40/77>1/2\). If the first primes are \(3,5\) and the third is at least \(17\), it is at least \((2/3)(4/5)(16/17)=128/255>1/2\). Any of these cases yields \(K<n/\beta(n)<2\), impossible.

The only remaining support is \(\{3,5,r\}\) with \(r\in\{7,11,13\}\). In this case \(\beta(n)/n\ge(2/3)(4/5)(6/7)=16/35>1/3\), hence \(2\le K<3\), forcing \(K=2\). Write \(n=3^a5^br^c\), with \(a,b,c\ge1\). If \(a\ge2\), the strengthened \(3\)-power bound gives
\[
\frac{\beta(n)}n\ge\frac{20}{27}\cdot\frac45\cdot\frac67=\frac{32}{63}>\frac12,
\]
a contradiction; therefore \(a=1\). Since \(\beta(3)=2\), the equation \(2\beta(n)=n-1\) implies \(n\equiv1\pmod4\). For \(r=13\) this fails, since \(n=3\cdot5^b13^c\equiv3\pmod4\). For \(r=7\) or \(11\), it forces \(c\) to be odd. If \(r=7\), reduction modulo \(3\) shows
\[
\beta(7^c)=7^c-7^{c-1}+\cdots-1\equiv 0\pmod3
\]
for odd \(c\), impossible because \(3\mid n\) but \(\beta(n)\mid n-1\). Thus \(r=11\). If \(b\ge2\), the strengthened \(5\)-power bound gives
\[
\frac{\beta(n)}n\ge\frac23\cdot\frac{104}{125}\cdot\frac{10}{11}
=\frac{416}{825}>\frac12,
\]
so \(b=1\). Finally \(11\equiv1\pmod5\) and \(c\) is odd, hence \(5\mid\beta(11^c)\); yet \(5\mid n\) and \(\beta(n)\mid n-1\). This last contradiction completes the proof.

## Verification
The self-contained Python file `verify.py` independently evaluates the multiplicative local formula against the square-gcd count for \(n\le300\), tests every integer \(2\le n\le10^6\) for the original divisibility, and checks prime-support restrictions for all composite hits. It returns only \(n=4\) as a composite hit in this finite range. The inequalities and congruences above, not any finite search, prove the theorem for all integers.

## Relationship to prior work
Tóth's survey, first public in 2011, formulates the exact divisibility question as Problem 4; its section on basic properties supplies the local formulas and parity fact, and its proof section uses the elementary fact \(\beta(n)<n-1\) for composite \(n\neq4\). The survey reports a finite computation, not an unrestricted prime-support obstruction. Iannucci's 2006 paper studies the same arithmetic function under the notation \(\rho\), but investigates the distinct equation \(k\rho(n)=n\), not \(\rho(n)\mid n-1\). Classical Lehmer necessary conditions for \(\varphi(n)\mid n-1\) apply directly only to the squarefree part of this problem, because \(\beta(n)=\varphi(n)\) precisely when \(n\) is squarefree. The present statement additionally eliminates nonsquarefree three-prime-support cases and even four-prime-support cases with unrestricted exponents.

## Limitations
The argument gives necessary support conditions only; it does not establish existence of any composite solution other than \(4\), nor resolve Tóth's unrestricted problem. The finite checker provides a reproducibility cross-check and is not an exhaustive proof. Novelty comparisons can miss unindexed or otherwise inaccessible earlier derivations.

## References
1. László Tóth, *A survey of the alternating sum-of-divisors function*, arXiv:1111.4842v1 (first submitted 2011-11-21), especially §§2, 7–8, Problem 4. https://arxiv.org/abs/1111.4842 ; full text https://arxiv.org/html/1111.4842v2 .
2. Douglas E. Iannucci, *On a Variation of Perfect Numbers*, Integers 6 (2006), A41, https://math.colgate.edu/~integers/g41/g41.pdf .
3. OEIS A206369, *The alternating sum-of-divisors function*, https://oeis.org/A206369 (definition and tabulated values, not a classification of the divisibility equation).
