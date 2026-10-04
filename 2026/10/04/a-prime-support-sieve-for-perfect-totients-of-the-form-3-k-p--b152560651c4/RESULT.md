# A prime-support sieve for perfect totients of the form \(3^k p\)
## Finding
For every integer \(k\ge 2\) and prime \(p>3\), write \(p-1=2^a3^b u\) with \(a\ge1\), \(b\ge0\), and \(\gcd(u,6)=1\). If \(3^k p\) is a perfect totient number, then \[\frac{\phi(u)}{u}>\frac{3(p+2)}{4(p-1)}>\frac34.\] Equivalently, the prime support of \(u\) must satisfy \[\prod_{\ell\mid u}\left(1-\frac1\ell\right)>\frac{3(p+2)}{4(p-1)}.\] Hence any finite set \(R\) of primes at least \(5\) with \(\prod_{\ell\in R}(1-1/\ell)\le 3/4\) is forbidden from simultaneously dividing \(p-1\). In particular, \(p\not\equiv1\pmod{35}\), \(p\not\equiv1\pmod{55}\), and \(p\not\equiv1\pmod{65}\).

The restriction is uniform in \(k\): it applies simultaneously to every exponent \(k\ge2\), including the unresolved range \(k\ge4\) highlighted in the literature on perfect totients of the form \(3^k p\).

## Assumptions and scope
For an integer \(n>1\), let \(\phi\) be Euler's totient and define
\[F(n)=\phi(n)+\phi^2(n)+\cdots+1,\]
where the iteration stops at \(1\). A perfect totient number satisfies \(F(n)=n\). The theorem concerns integers \(n=3^k p\) with \(k\ge2\) and prime \(p>3\). Write \(p-1=2^a3^b u\), where \(a\ge1\), \(b\ge0\), and \(\gcd(u,6)=1\).

## Proof
First prove an elementary orbit bound. If \(m\ge2\) is even, then
\[F(m)\le 2\phi(m)-1.\]
For \(m=2\) this is equality. If \(m>2\), then \(y=\phi(m)\) is even. Induction gives \(F(y)\le y-1\), while \(F(m)=y+F(y)\); therefore \(F(m)\le2y-1=2\phi(m)-1\). The same induction also uses \(2\phi(m)\le m\) for even \(m\), so it closes from the base case.

Now suppose \(n=3^k p\) is perfect totient. Its first iterate is
\[m=\phi(n)=2\cdot3^{k-1}(p-1).\]
Since \(F(n)=m+F(m)=n\),
\[F(m)=3^{k-1}(p+2).\]
From \(p-1=2^a3^b u\) and \(k\ge2\), multiplicativity gives
\[\phi(m)=2\cdot3^{k-2}(p-1)\frac{\phi(u)}u.\]
Applying the orbit bound,
\[3^{k-1}(p+2)=F(m)\le2\phi(m)-1<\frac43\,3^{k-1}(p-1)\frac{\phi(u)}u.\]
After cancellation,
\[\frac{\phi(u)}u>\frac{3(p+2)}{4(p-1)}>\frac34.\]
Finally \(\phi(u)/u=\prod_{\ell\mid u}(1-1/\ell)\). If a finite set \(R\) of primes dividing \(u\) has product at most \(3/4\), then the full Euler product is at most that value, a contradiction. The three stated congruence exclusions follow from
\[\left(1-\frac15\right)\left(1-\frac17\right)=\frac{24}{35},\quad
\left(1-\frac15\right)\left(1-\frac1{11}\right)=\frac8{11},\quad
\left(1-\frac15\right)\left(1-\frac1{13}\right)=\frac{48}{65},\]
all of which are less than \(3/4\).

## Verification
The accompanying `verify.py` independently implements Euler's totient and the complete totient-orbit sum. It checks \(F(m)\le2\phi(m)-1\) for every even \(m\le20000\), then examines every prime \(p\le200000\) and every \(2\le k\le8\). Every perfect-totient hit in that finite range satisfies the exact cross-multiplied support inequality and the three congruence exclusions. The replay output is:

`VERIFY_OK limit=200000 kmax=8 even_checked=10000 target_hits=[(2, 619, 5571, 103), (3, 1733, 46791, 433), (2, 1747, 15723, 97), (3, 5189, 140103, 1297), (2, 49003, 441027, 8167)] sieve_violations=0`

This finite computation is corroborative only; the theorem is proved symbolically above.

## Relationship to prior work
Iannucci, Moujie, and Cohen study exactly the family \(3^k p\), give several sufficient constructions for \(k=2,3\), eliminate particular nested-prime factorizations for \(k\ge4\), and explicitly leave the existence of any \(3^k p\) perfect totient with \(k\ge4\) open. Their inspected full text does not state the Euler-product restriction above. Shparlinski studies global distribution and congruence properties of the iterated-totient sum, not a prime-support condition on \(p-1\). Deng eliminates a deeper prescribed prime-chain factorization for \(k\ge4\), again without a uniform Euler-product sieve on arbitrary \(p-1\). OEIS A082897 was checked as the natural table of known perfect totient numbers and is consistent with the finite replay.

## Limitations
The condition is necessary, not sufficient, and it does not settle whether perfect totients \(3^k p\) exist for \(k\ge4\). It constrains only the distinct prime divisors of the factor of \(p-1\) coprime to \(6\); exponents of those primes do not change the Euler product. Older foundational sources from 1939 and 1982 were not available for direct full-text inspection here, so there remains a literature-access risk that an equivalent elementary inequality appeared there. The later full-text papers inspected describe those older results in narrower forms, and targeted statement searches found no equivalent formulation.

## References
1. D. E. Iannucci, D. Moujie, and G. L. Cohen, "On Perfect Totient Numbers", *Journal of Integer Sequences* 6 (2003), Article 03.4.5. Published December 18, 2003. https://cs.uwaterloo.ca/journals/JIS/VOL6/Cohen2/cohen50.html
2. I. E. Shparlinski, "On the Sum of Iterations of the Euler Function", *Journal of Integer Sequences* 9 (2006), Article 06.1.6. https://cs.uwaterloo.ca/journals/JIS/VOL9/Shparlinski/shpar43.html
3. M. Deng, "A Note On Perfect Totient Numbers", *Journal of Integer Sequences* 12 (2009), Article 09.6.2. https://cs.uwaterloo.ca/journals/JIS/VOL12/Deng/deng1.html
4. OEIS Foundation Inc., A082897, "Perfect totient numbers". https://oeis.org/A082897
