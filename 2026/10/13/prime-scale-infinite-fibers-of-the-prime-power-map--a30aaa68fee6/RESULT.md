# Prime-scale infinite fibers of the prime-power map
## Finding
Let \(P:\mathbb N\to\mathbb N\) be the prime-power map of Steven and Hoseana. Thus \(P(1)=1\); if \(x\) is a prime power \(p^k\), then \(P(x)=p^{k-1}\); and otherwise \(P(x)=x-Q(x)\), where \(Q(x)\) is the largest prime power not exceeding \(x\).

For every fixed integer \(y\ge 1\), choose pairwise distinct primes
\[
r_1,s_1,\ldots,r_y,s_y>y,
\]
put
\[
M_y=\prod_{j=1}^y r_js_j,
\]
and let \(a_y\pmod{M_y}\) be the Chinese-remainder class defined by
\[
a_y\equiv-j\pmod{r_js_j}\qquad(1\le j\le y).
\]
Then \(\gcd(a_y,M_y)=1\), and every prime \(q\equiv a_y\pmod{M_y}\) satisfies
\[
P(q+y)=y.
\]
Therefore each fiber \(P^{-1}(\{y\})\) is infinite. More quantitatively, if
\[
F_y(X)=\#\{x\le X:P(x)=y\},
\]
then
\[
\liminf_{X\to\infty}\frac{F_y(X)\log X}{X}\ge\frac1{\varphi(M_y)}>0.
\]
Hence every vertex in the functional graph of \(P\) has infinite indegree.

## Assumptions and scope
The domain is the positive integers, with the prime-power map normalized exactly as in Steven–Hoseana. A prime power means \(p^k\) with \(p\) prime and \(k\ge1\), so primes themselves are prime powers. The argument uses only the Chinese remainder theorem and the standard prime number theorem in arithmetic progressions. Dirichlet's theorem alone already gives the qualitative infinitude of every fiber; the prime number theorem in arithmetic progressions supplies the stated quantitative lower bound.

The primes \(r_j,s_j\) may be chosen arbitrarily subject to pairwise distinctness and \(r_j,s_j>y\). The displayed constant \(1/\varphi(M_y)\) is therefore explicit once such a choice is fixed, but it is not claimed to be optimal.

## Proof
Because every prime divisor of \(M_y\) is larger than \(y\), for each \(1\le j\le y\) neither \(r_j\) nor \(s_j\) divides \(j\). The congruences
\[
a_y\equiv-j\pmod{r_js_j}
\]
are imposed on pairwise coprime moduli, so the Chinese remainder theorem gives a unique class \(a_y\pmod{M_y}\). If a prime \(t\mid M_y\) belongs to the pair \(r_j,s_j\), then \(a_y\equiv-j\not\equiv0\pmod t\); hence \(\gcd(a_y,M_y)=1\).

Now let \(q\) be any prime with \(q\equiv a_y\pmod{M_y}\). For every \(1\le j\le y\),
\[
q+j\equiv0\pmod{r_js_j}.
\]
Thus \(q+j\) has the two distinct prime divisors \(r_j\) and \(s_j\), so \(q+j\) is not a prime power. On the other hand, \(q\) itself is a prime and hence a prime power. It follows that among the integers
\[
q,q+1,\ldots,q+y
\]
the largest prime power is exactly \(q\). In particular \(q+y\) is not a prime power and
\[
P(q+y)=(q+y)-q=y.
\]
This proves that every prime \(q\equiv a_y\pmod{M_y}\) gives a distinct preimage \(q+y\) of \(y\).

Since \(\gcd(a_y,M_y)=1\), the prime number theorem in arithmetic progressions gives
\[
\#\{q\le X-y:q\text{ prime},\ q\equiv a_y\pmod{M_y}\}\sim\frac{\operatorname{Li}(X)}{\varphi(M_y)}.
\]
Every prime counted on the left produces a distinct element of the fiber below \(X\). Therefore
\[
F_y(X)\ge\left(\frac1{\varphi(M_y)}+o(1)\right)\frac X{\log X},
\]
which yields the claimed liminf and completes the proof.

## Verification
The accompanying `verify.py` independently constructs the CRT classes for \(1\le y\le3\), finds a prime in each class, verifies the prescribed two-prime divisibility of every intermediate \(q+j\), and confirms that the constructed endpoint maps to \(y\) by the defining largest-prime-power rule. This finite replay is regression evidence for the construction only; the theorem for all \(y\) is the symbolic argument above together with the prime number theorem in arithmetic progressions.

## Relationship to prior work
Steven and Hoseana introduced this map and studied its forward dynamics, including prime powers in orbits and a recursively defined sequence built from minimum preimages. Their Proposition 15 identifies one minimum-preimage relation along that special sequence. The inspected paper does not state that every fiber is infinite, does not give a family of arithmetic progressions contained in arbitrary fibers, and does not give a fiber-counting lower bound.

OEIS A336825 records the prime-power map sequence and related formulas, including the source literature, but the inspected entry does not state the fiber theorem above. The present result concerns the global inverse branching of the same map and is not implied by the source paper's forward-orbit results.

## Limitations
The theorem gives a constructed subset of each fiber, not a classification of the full fiber. The constant \(1/\varphi(M_y)\) depends on the chosen auxiliary primes and is not optimized. The result does not address the source paper's conjectures about the frequency of prime powers in typical forward orbits.

## References
1. Steven and Jonathan Hoseana, “The Prime-Power Map,” arXiv:2008.01368, first submitted August 4, 2020; *Journal of Integer Sequences* 24 (2021), Article 21.2.2.
2. OEIS A336825, “The prime-power map,” with references to Steven–Hoseana.
3. Prime number theorem in arithmetic progressions, in its standard fixed-modulus form.
