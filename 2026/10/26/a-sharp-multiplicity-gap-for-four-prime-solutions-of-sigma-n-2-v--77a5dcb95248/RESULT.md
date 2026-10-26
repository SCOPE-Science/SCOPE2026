# A sharp multiplicity gap for four-prime solutions of \(\sigma(n)=2\varphi(n)\)

## Finding
Let \(\omega(n)\) be the number of distinct prime divisors of \(n\) and \(\Omega(n)\) the number of prime factors with multiplicity. If \(\omega(n)=4\) and \(\Omega(n)=5\), then \(\sigma(n)\ne2\varphi(n)\). The multiplicity threshold is sharp: \(2011009=7^3\cdot11\cdot13\cdot41\) satisfies \(\sigma(2011009)=2\varphi(2011009)\), with \(\omega(2011009)=4\) and \(\Omega(2011009)=6\). Thus any nonsquarefree four-prime solution must have at least six prime factors counted with multiplicity.

## Assumptions and scope
Here \(\sigma(n)\) denotes the ordinary sum of positive divisors, \(\varphi(n)\) Euler's totient, and all primes are positive rational primes. The excluded multiplicity class consists precisely of \(n=t^2uvw\) for four pairwise distinct primes \(t,u,v,w\). The theorem does not exclude squarefree four-prime solutions or classify higher multiplicities. The numerical witness is previously recorded in the literature; the claim of interest is the universal exclusion of the first nonsquarefree layer.

## Proof
Write the four distinct primes in increasing order as \(p<q<r<s\). For each prime \(z\), put
\[
f(z)=\frac{z+1}{z-1},\qquad g(z)=\frac{z^2+z+1}{z(z-1)}=f(z)\left(1+\frac1{z(z+1)}\right).
\]
These are the respective factors in \(\sigma(n)/\varphi(n)\) at exponent one and two. Both strictly decrease with \(z\), with \(g(z)>f(z)>1\), and the surplus \(g(z)/f(z)\) decreases. Thus placing the square on the smallest prime maximizes the ratio. If \(p=2\) then \(f(p)=3>2\); if \(p=3\), \(f(p)=2\) and the other factors make the ratio strictly exceed two. Hence \(p\ge5\).

If \(p\ge11\), the ratio is at most \(g(11)f(13)f(17)f(19)=931/528<2\). If \(p=7\) and \(q\ge13\), it is at most \(g(7)f(13)f(17)f(19)=95/48<2\). If \(p=5\) and \(q\ge23\), it is at most \(g(5)f(23)f(29)f(31)=744/385<2\). The pair \((p,q)=(5,7)\) gives \(f(5)f(7)=2\), so adding other factors makes equality impossible. Therefore only the five ordered initial pairs \((5,11),(5,13),(5,17),(5,19),(7,11)\) remain.

First exclude placing the square on the largest prime \(s\). Since \(s\) divides \(\varphi(s^2)\), the equation would force \(s\mid\sigma(pqr s^2)\), hence \(s\mid(p+1)(q+1)(r+1)\), as \(1+s+s^2\equiv1\pmod{s}\). But each of the three factors \(p+1,q+1,r+1\) is strictly between zero and \(s\), contradicting primality of \(s\).

It remains to square one of \(p,q,r\). For each of the five pairs, let \(r\) range over primes greater than \(q\), and let \(r'\) be the next prime after \(r\). For every \(s>r\), the ratio is at most \(g(p)f(q)f(r)f(r')\). This upper bound is strictly decreasing in \(r\). The first values of \(r\) where the upper bound is already below two, together with the exact upper bounds, are
\[
\begin{array}{c|c|c}
(p,q)&r&g(p)f(q)f(r)f(r')\\ \hline
(5,11)&53&7533/3770\\
(5,13)&41&2387/1200\\
(5,17)&29&279/140\\
(5,19)&29&124/63\\
(7,11)&19&152/77
\end{array}
\]
Consequently only \(10+6+2+1+2=21\) initial triples \((p,q,r)\) remain; the attached exact-arithmetic certificate enumerates precisely these triples with no size cutoff on \(s\).

For each of the three choices \(t\in\{p,q,r\}\) of squared prime, define
\[
R=g(t)\prod_{z\in\{p,q,r\}\setminus\{t\}}f(z).
\]
If \(R\ge2\), no fourth factor \(f(s)>1\) can give two. Otherwise \(Rf(s)=2\) forces the unique rational value
\[
s=\frac{2+R}{2-R}.
\]
The exact certificate finds precisely six integer values with \(s>r\): \((p,q,r;s)=(5,11,29;559),(5,11,31;249),(5,13,29;63),(5,17,19;63),(5,19,23;32),(7,11,13;39)\), with the square on \(p\) throughout. Every such \(s\) is composite: \(559=13\cdot43\), \(249=3\cdot83\), \(63=3^2\cdot7\), \(32=2^5\), and \(39=3\cdot13\). No prime \(s\) remains. This proves the exclusion for all exponents with pattern \((2,1,1,1)\).

For sharpness, \(n=7^3\cdot11\cdot13\cdot41=2011009\) has \(\sigma(n)=400\cdot12\cdot14\cdot42=2822400\) and \(\varphi(n)=294\cdot10\cdot12\cdot40=1411200\); the ratio is exactly two.

## Verification
The accompanying standalone Python program `verify_multiplicity_gap.py` uses only exact integer arithmetic and rational fractions. It checks all reduction inequalities and five stopping thresholds, exhausts the 21 surviving triples and three square placements, confirms the six candidate last values are composite, independently tests all integers through \(300000\) in the target multiplicity class, and checks the sharp witness. The finite direct enumeration is corroboration, not a substitute for the proved infinite reduction and exact certificate. Reproduce with `python3 verify_multiplicity_gap.py`.

## Relationship to prior work
Broughan and Delbourgo (2013) prove the \(\sigma(n)=2\varphi(n)\) classification for at most three distinct primes, and establish finiteness at any prescribed multiplicity bound. Broughan and Zhou (2014) investigate low prime support and related quotient equations. Neither inspected primary paper establishes this exact four-prime multiplicity-five exclusion. OEIS A062699 includes the numerical sharpness witness, which is therefore not claimed as a new numerical discovery. This result distinguishes the first nonsquarefree support-four layer from both the established three-prime theorem and a list of known solutions.

## Limitations
This theorem says nothing about the general \(\Omega(n)\ge6\) case, and the witness does not classify that layer. The proof is exact, but full publication-priority certainty is not possible from indexed literature searches; an equivalent unindexed formulation could exist. No independent audit is claimed here.

## References
1. K. A. Broughan and D. Delbourgo, *On the Ratio of the Sum of Divisors and Euler's Totient Function I*, Journal of Integer Sequences 16 (2013), Article 13.8.8. https://cs.uwaterloo.ca/journals/JIS/VOL16/Broughan/broughan26.pdf
2. K. A. Broughan and Q. Zhou, *On the Ratio of the Sum of Divisors and Euler's Totient Function II*, Journal of Integer Sequences 17 (2014), Article 14.9.2. https://cs.uwaterloo.ca/journals/JIS/VOL17/Broughan/bro32.pdf
3. OEIS A062699, solutions of \(\sigma(n)=2\varphi(n)\). https://oeis.org/A062699
