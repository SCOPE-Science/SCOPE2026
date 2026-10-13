# The six three-prime Lucas pseudoprime signatures at the factor three

## Finding

Let \(D\) be a prime with \(D\equiv1\pmod4\). For odd primes \(3<q<r\) with \(D\nmid3qr\), put \(n=3qr\) and
\[
 (a,b,c)=\left(\left(\frac D3\right),\left(\frac Dq\right),\left(\frac Dr\right)\right).
\]
Then \(n\) is an *absolute Lucas pseudoprime of discriminant \(D\)* precisely for the six rows below. Here \(k,j\) are the positive integers in the proof, and the final column is an explicit prime discriminant witness.

| \(n=3qr\) | \((q,r)\) | \((a,b,c)\) | \((k,j)\) | witness \(D\) |
| ---: | ---: | :---: | :---: | ---: |
| \(105\) | \((5,7)\) | \((-1,+1,-1)\) | \((2,5)\) | \(41\) |
| \(195\) | \((5,13)\) | \((+1,+1,-1)\) | \((1,10)\) | \(109\) |
| \(255\) | \((5,17)\) | \((-1,+1,+1)\) | \((1,13)\) | \(89\) |
| \(399\) | \((7,19)\) | \((-1,-1,-1)\) | \((1,7)\) | \(41\) |
| \(561\) | \((11,17)\) | \((+1,+1,+1)\) | \((2,5)\) | \(157\) |
| \(2703\) | \((17,53)\) | \((-1,+1,+1)\) | \((1,10)\) | \(89\) |

For every fixed row, the satisfying prime discriminants have relative density \(1/8\) among primes congruent to \(1\) modulo \(4\), and hence are infinite in number. Equivalently the density among all primes is \(1/16\).

## Assumptions and scope

A Lucas sequence with integral parameters \(A,B\), \(\gcd(A,B)=1\), and discriminant \(D=A^2-4B\) is given by \(U_0=0\), \(U_1=1\), and \(U_{h+2}=AU_{h+1}-BU_h\). An odd composite integer \(n\) is an *absolute Lucas pseudoprime of discriminant \(D\)* if it satisfies \(U_{n-(D/n)}(A,B)\equiv0\pmod n\) for every admissible parameter pair with \(\gcd(n,DB)=1\). The symbols \((D/p)\) are Legendre symbols at odd primes; \((D/n)\) is the Jacobi symbol. We restrict the theorem to prime \(D\equiv1\pmod4\) and exactly three distinct prime factors of \(n\), the smallest being \(3\). The prime condition makes all three quadratic character signs attainable independently while keeping the discriminant genuine.

## Proof

**1. Local criterion.** Williams' Korselt-type criterion [1, 2] states that for an odd composite integer \(n\), absolute Lucas pseudoprimality for a discriminant coprime to \(n\) is equivalent to \(n\) being squarefree and
\[
 p-\left(\frac Dp\right)\mid n-\left(\frac Dn\right)
 \qquad\text{for every prime }p\mid n.
\]
For \(n=3qr\), write \(a=(D/3),b=(D/q),c=(D/r)\), so the Jacobi symbol is \(abc\). The divisibility tests become
\[
 3-a\mid3qr-abc,\qquad q-b\mid3qr-abc,\qquad r-c\mid3qr-abc.
\]

**2. Two small quotients.** Reducing the last test modulo \(r-c\) and the middle test modulo \(q-b\) gives positive integers
\[
 k=\frac{3q-ab}{r-c},\qquad j=\frac{3r-ac}{q-b}.
\]
Since \(r\ge q+2\) and \(q\ge5\), we have \(r-c\ge q+1\), and therefore \(1\le k<3\), hence \(k\in\{1,2\}\). Also \(r=c+(3q-ab)/k\le3q+2\). Consequently, for \(k=1\),
\[
 j\le\frac{9q+7}{q-1}\le13,
\]
while for \(k=2\),
\[
 j\le\frac{9q+11}{2(q-1)}\le7.
\]
Eliminating \(r\) between the formulas for \(j\) and \(k\) yields the *integer equality*
\[
 (jk-9)q=b(jk-3a)+kc(3-a).\tag{1}
\]
The exceptional case \(jk=9\) requires \((k,j)=(1,9)\), but then the right side of (1) becomes \((3-a)(3b+c)\ne0\). Thus \(jk\ne9\), and
\[
 q=\frac{b(jk-3a)+kc(3-a)}{jk-9}.\tag{2}
\]

**3. An explicit complete finite cutoff.** Equation (2) gives
\[
 0<q\le\frac{jk+3+4k}{|jk-9|}.
\]
For \(k=1\) and \(1\le j\le13\) with \(j\ne9\), the right side has maximum \(17\), at \(j=10\). For \(k=2\) and \(1\le j\le7\), its maximum is \(21\), at \(j=5\). Therefore \(q\le21\) and \(r\le3q+2\le65\). Every potential solution is captured by
\[
 q\in\{5,7,11,13,17,19\},\quad q<r\le65\text{ prime},\quad (a,b,c)\in\{-1,+1\}^3.
\]
An exact trial-division enumeration of those bounded candidates, accepting **all three original local divisibility tests**, gives the table in the Finding. Grouping by \(q\), the complete outcomes are \(q=5\): \((r;a,b,c)=(7;-1,+1,-1),(13;+1,+1,-1),(17;-1,+1,+1)\); \(q=7\): \((19;-1,-1,-1)\); \(q=11\): \((17;+1,+1,+1)\); \(q=13\): none; \(q=17\): \((53;-1,+1,+1)\); and \(q=19\): none. The accompanying standard-library script implements both this independent bounded sieve and the separate quotient-equation enumeration of all \(160\) sign/quotient cases, checking that their outputs agree. The cutoff proof and both exhaustive enumerations establish the asserted necessity; substitution in the three tests establishes sufficiency.

**4. Realization and density.** Fix any row and its three distinct odd prime factors. At each of \(3,q,r\), exactly half of the nonzero residue classes are quadratic residues and exactly half are quadratic nonresidues. By the Chinese remainder theorem, the desired triple of Legendre signs and \(D\equiv1\pmod4\) therefore select exactly one eighth of the reduced residue classes that are \(1\) modulo \(4\), modulo \(4n\). Dirichlet's theorem yields infinitely many primes in each selected class; the prime number theorem in arithmetic progressions gives equal relative prime densities among those reduced classes. Thus each row has prime-discriminant density \(1/8\) conditioned on \(D\equiv1\pmod4\) (and \(1/16\) relative to all primes). The finitely many primes dividing \(n\) have zero effect on this density.

## Verification

Run `python3 VERIFIER.py` from the directory containing the accompanying file. The verifier uses no third-party libraries, checks the full \(160\)-case quotient sieve and an independently structured bounded prime/sign sieve, and tests a prime discriminant witness for each row using Euler's criterion. `VERIFIER_OUTPUT.txt` contains the output from a successful execution of that same file. The infinite sign-realization and density statements are mathematical consequences of the Chinese remainder theorem and prime distribution in arithmetic progressions; the finite runs do not substitute for those theorems.

## Relationship to prior work

Williams [2] proved the general Korselt-type equivalence and supplied related constructions, but did not state this complete six-row answer for the smallest possible prime factor of a three-prime absolute Lucas pseudoprime. Helmreich and Webster [1] proved quantitative bounds and tabulation algorithms and reported computations for specified discriminants. The first public preprint concerns discriminant \(5\); the expanded journal version additionally tabulates \(-7,-11,13\). Neither is an exhaustive result across **every prime** discriminant with the exact three-symbol classification and conditional density. The all-plus row \(561\) is the classical Carmichael boundary; the all-minus row \(399\) is the Lucas–Carmichael boundary. The other four rows are mixed-sign possibilities that those two special classes do not imply. This is an explicit endpoint of the general criterion, not a replacement for it.

## Limitations

The statement fixes exactly three distinct prime factors and requires the least prime factor \(3\). It does not classify integers with other factor supports, prime-power factors, or composite/nonfundamental discriminants. Its originality is in the exact cross-discriminant classification and density, rather than the general Korselt criterion itself. An equivalent explicit enumeration in literature not inspected here remains possible.

## References

1. Chloe Helmreich and Jonathan Webster, *Tabulating Absolute Lucas Pseudoprimes*, arXiv:2306.17691v1, first posted 30 June 2023, https://arxiv.org/html/2306.17691v1; expanded version *INTEGERS* 24A (2024), article A8, https://math.colgate.edu/~integers/a8Proc23/a8Proc23.pdf.
2. H. C. Williams, *On Numbers Analogous to the Carmichael Numbers*, *Canadian Mathematical Bulletin* 20 (1977), 133–143, https://doi.org/10.4153/CMB-1977-025-9.
3. W. Carlip and L. Somer, *Square-free Lucas d-pseudoprimes and Carmichael-Lucas numbers*, *Czechoslovak Mathematical Journal* 57 (2007), 447–463, https://doi.org/10.1007/s10587-007-0072-6. Their rank-based notion requires care before comparing it to fixed-discriminant absolute Lucas pseudoprimes.
