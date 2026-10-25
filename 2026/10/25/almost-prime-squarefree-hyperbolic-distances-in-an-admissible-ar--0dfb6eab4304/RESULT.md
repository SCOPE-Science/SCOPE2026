# Almost-prime squarefree hyperbolic distances in an admissible arithmetic progression

## Finding

Let
\[
N_{11,20}^{(7)}(x)=\#\left\{(a,b,c,d)\in\mathbb Z^4:\ ad-bc=1,\ n=a^2+b^2+c^2+d^2\le x,\ \mu^2(n)=1,\ n\equiv11\pmod{20},\ \omega(n)\le7\right\}.
\]
There is a constant \(c_0>0\) such that
\[
N_{11,20}^{(7)}(x)\ge c_0\frac{x}{\log x}
\]
for all sufficiently large \(x\). This is a lower bound for representations, so a single norm can contribute more than once.

## Assumptions and scope

Here \(\mu\) is the Möbius function, \(\mu^2(n)=1\) means that \(n\) is square-free, and \(\omega(n)\) counts distinct prime divisors. The congruence \(n\equiv11\pmod{20}\) implies that \(n\) is odd, \(n\equiv3\pmod4\), and \(5\nmid n\). The claim concerns this one admissible residue class and the number of determinant-one integer matrices with the indicated norm; it does not assert a lower bound of this order for the number of distinct norms.

## Proof

Put \(r(m)=\#\{(u,v)\in\mathbb Z^2:u^2+v^2=m\}\) and \(A_n=r(n-2)r(n+2)\). The standard linear change of variables for determinant-one matrices shows that for odd \(n\equiv3\pmod4\), the number of quadruples with norm \(n\) is \(A_n/2\). Consequently,
\[
N_{11,20}^{(7)}(x)=\frac12\sum_{\substack{n\le x\\n\equiv11\ (20)}}\mu^2(n)A_n\,\mathbf 1_{\{\omega(n)\le7\}}.
\]

We adapt the shifted-convolution estimate and Richert weighted linear sieve used for square-free hyperbolic distances. For square-free \(d\) with \((d,10)=1\), consider
\[
A_d(x)=\sum_{\substack{n\le x\\n\equiv11\ (20)\\d\mid n}}r(n-2)r(n+2).
\]
Using \(r(m)=4\sum_{k\mid m}\chi_4(k)\) for \(m\equiv1\pmod4\), expand one factor and write \(k\mid n-2\) as a congruence. Since \(n\equiv11\pmod{20}\), both \(n-2\) and \(n+2\) are units modulo \(5\); since \(d\mid n\) and \(d\) is odd, any common divisor of \(d\) and \(k\mid n-2\) divides \(2\), hence \((d,k)=1\). The Chinese remainder theorem therefore gives a single residue class for the remaining sum of \(r(n+2)\) modulo \(20dk\), coprime to that modulus and congruent to \(1\pmod4\).

The two-squares progression estimate then gives the same level of distribution as in the unrestricted odd case, with constants changed only by the fixed local factor at \(5\). This factor is positive: \(\chi_4(5)=1\), so the local factor \(1-\chi_4(5)/5=4/5\) is nonzero. More precisely, for square-free \(d\) coprime to \(10\), the progression estimate has a main term \(X_5 g(d)x\), where \(X_5>0\), \(g\) is multiplicative on primes other than \(5\), and \(g(p)=1/p+O(p^{-2})\); its summed remainders retain the bound
\[
\sum_{d\le D}|R_d|\ll D^{1/2}x^{11/12+\varepsilon}+Dx^{1/2+\varepsilon}
\]
for \(D\le x^{1/6-4\varepsilon}\), after changing constants depending on the fixed progression.

In the sieve, omit the prime \(5\), which cannot divide any integer in the progression. Removing one prime does not change the dimension-one sieve condition, and the positive fixed local factor leaves the sieve main term of order \(x\). The Richert weights and parameters used for the seven-prime-factor bound therefore give a weighted lower bound \(\gg x/\log x\). As in the unrestricted proof, the contribution of nonsquare-free terms is \(o(x/\log x)\); on the remaining support, \(\Omega(n)=\omega(n)\), and a positive Richert weight forces \(\omega(n)\le7\). Since the weights are at most one, the sum of \(A_n\) over square-free members of this progression with \(\omega(n)\le7\) is \(\gg x/\log x\). Multiplication by the representation factor \(1/2\) proves the claim.

## Verification

The key inputs are the identity for the odd determinant-one representation count, the two-squares progression estimate, the shifted-convolution level of distribution, and Richert's weighted linear sieve. The fixed-modulus adaptation is justified by the explicit Chinese-remainder calculation above; the exponent of the level-of-distribution bound is unchanged because the extra modulus factor is fixed. The local factor at \(5\) is positive, so the lower-bound sieve is not annihilated by a congruence obstruction.

## Relationship to prior work

Sedunova's *On the hyperbolic prime number theorem* proves an unconditional \(\gg x/\log x\) lower bound for square-free determinant-one norms with at most seven distinct prime factors without fixing a residue class. Its proof supplies the shifted-convolution estimate and the Richert sieve used here. The present statement restricts to \(n\equiv11\pmod{20}\); the unrestricted lower bound alone would not imply a lower bound in this individual class. Friedlander and Iwaniec's earlier hyperbolic prime number theorem supplies the underlying determinant-one parametrization and two-squares progression estimates.

## Limitations

No explicit value of \(c_0\) is claimed. The argument treats the single progression \(11\pmod{20}\), not every admissible residue class. It counts matrix representations, not distinct integers \(n\), and does not improve the bound of seven prime factors. The proof is an analytic extension of an existing sieve argument; a separate independent audit has not been performed.

## References

1. A. Sedunova, *On the hyperbolic prime number theorem*, arXiv:2609.28200 (first public version, 2026-09-23), especially the square-free representation identity, the shifted-convolution estimate, and the Richert-sieve argument. https://arxiv.org/abs/2609.28200
2. J. B. Friedlander and H. Iwaniec, *Hyperbolic prime number theorem*, Acta Mathematica 202 (2009), 1–19. DOI: 10.1007/s11511-009-0033-z.
3. H. Halberstam and H.-E. Richert, *Sieve Methods*, London Mathematical Society Monographs 4, Academic Press, 1974.
