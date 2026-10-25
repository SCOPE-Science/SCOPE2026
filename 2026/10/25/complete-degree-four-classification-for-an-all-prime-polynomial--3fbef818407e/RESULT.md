# Complete degree-four classification for an all-prime polynomial divisibility condition

## Finding
Let \(f\in\mathbb Z[x]\) be monic of degree exactly four. Then
\[
 f(p)\mid f(p^p)\quad\text{for every prime }p
\]
holds if and only if \(f\) is one of the following thirteen polynomials:
\[
\begin{gathered}
x^4,\quad x^3(x-1),\quad x^2(x-1)^2,\quad x^2(x^2-1),\\
x(x-1)^3,\quad x(x-1)^2(x+1),\quad x(x-1)(x^2+x+1),\\
(x-1)^4,\quad (x-1)^3(x+1),\quad (x-1)^2(x+1)^2,\\
(x-1)^2(x^2+x+1),\quad (x-1)(x+1)(x^2+x+1),\\
(x-1)(x+1)(x^2+1).
\end{gathered}
\]
The classification is exact over all primes, not just a finite range of test primes.

## Assumptions and scope
All polynomials have integer coefficients and are monic. Divisibility is ordinary integer divisibility. The degree is exactly four. Write \(\Phi_d\) for the \(d\)-th cyclotomic polynomial. The statement does not classify degrees five and above.

## Proof
The published eventual-divisibility theorem says that if \(f(p)\mid f(p^p)\) for all sufficiently large primes, then
\[
f(x)=x^a\prod_d\Phi_d(x)^{e_d},\qquad a,e_d\in\mathbb Z_{\ge0}.
\]
The published all-prime necessary condition further says that, unless \(f\) is a power of \(x\), \(\Phi_1(x)=x-1\) divides \(f\). Factor out \(x^a\); it does not affect the condition, since \(p\nmid\Phi_d(p)\) for every prime \(p\) and every \(d\), and \(p^a\mid p^{ap}\).

If \(x-1\mid f\) and the cyclotomic part has degree at most four, every index in its support belongs to \(\{1,2,3,4,6\}\), because \(\varphi(d)\le3\) for every non-1 index that can fit beside \(\Phi_1\) in degree at most four. Write
\[
g(x)=\Phi_1(x)^{e_1}\Phi_2(x)^{e_2}\Phi_3(x)^{e_3}\Phi_4(x)^{e_4}\Phi_6(x)^{e_6},
\]
where \(e_1\ge1\) and
\[
e_1+e_2+2e_3+2e_4+2e_6\le4.
\]
For every prime \(p\ge5\), none of the five indices is divisible by \(p\). The cyclotomic identity
\[
\Phi_d(x^p)=\Phi_d(x)\Phi_{pd}(x)\quad(p\nmid d)
\]
therefore gives \(g(p)\mid g(p^p)\) automatically. It remains to check exactly \(p=2\) and \(p=3\).

At \(p=2\), the values at \(2\) and \(4\) give
\[
g(2)=3^{e_2+e_6}7^{e_3}5^{e_4},\qquad
g(4)=3^{e_1+e_3}5^{e_2}7^{e_3}17^{e_4}13^{e_6}.
\]
Thus \(g(2)\mid g(4)\) exactly when
\[
e_1+e_3\ge e_2+e_6,\qquad e_2\ge e_4.
\]
At \(p=3\), using \(\Phi_3(27)=757\), \(\Phi_4(27)=730=2\cdot5\cdot73\), and \(\Phi_6(27)=703=19\cdot37\), the only additional inequalities are
\[
e_1\ge e_3,\qquad e_2\ge e_6.
\]
Consequently the admissible exponent vectors are precisely those satisfying the displayed degree bound and
\[
e_1+e_3\ge e_2+e_6,\quad e_2\ge e_4,\quad e_1\ge e_3,\quad e_2\ge e_6.
\]
Enumerating these nonnegative integer vectors gives exactly twelve cyclotomic parts \(g\), of degrees one through four:
\[
\Phi_1;\quad \Phi_1\Phi_2,\ \Phi_1^2;\quad
\Phi_1\Phi_3,\ \Phi_1^2\Phi_2,\ \Phi_1^3;
\]
\[
\Phi_1\Phi_2\Phi_4,\ \Phi_1\Phi_2\Phi_3,\ \Phi_1^2\Phi_3,
\ \Phi_1^2\Phi_2^2,\ \Phi_1^3\Phi_2,\ \Phi_1^4.
\]
Multiplying each part of degree \(d\) by \(x^{4-d}\), and adding \(x^4\), yields the thirteen listed polynomials. The cyclotomic factorization and the exact checks at \(2\) and \(3\) prove both necessity and sufficiency.

## Verification
The accompanying standard-library verifier enumerates all exponent vectors with cyclotomic degree at most four, applies the exact necessary-and-sufficient inequalities obtained from the prime factorizations at \(2\) and \(3\), and confirms the twelve cyclotomic parts and thirteen degree-four polynomials. The proof handles every prime \(p\ge5\) symbolically via the cyclotomic identity; finite computation is used only to enumerate the small exponent vectors.

## Relationship to prior work
Klahn's paper characterizes the eventual-divisibility condition and proves that a non-power-of-\(x\) polynomial satisfying the condition for every prime must have \(x-1\) as a factor. It also gives a sufficient family for the all-prime condition, but does not state a complete low-degree list. The present result resolves the full degree-four layer by combining those general theorems with the exact exceptional local checks at \(2\) and \(3\). It is a finite classification, not a new classification in arbitrary degree.

## Limitations
No classification is claimed for degree five or higher. The general all-prime problem remains only partially characterized by the cited source. The result depends on the published general cyclotomic-factorization theorem; the new contribution is the complete degree-four specialization.

## References
1. Benjamin Klahn, *A divisor problem for polynomials*, arXiv:2202.02100v1 (first public version 4 February 2022), especially Theorems 2.1 and 2.2 and Lemma 3.4. https://arxiv.org/abs/2202.02100.
2. The full primary PDF, including the cyclotomic identity and proof of the all-prime necessary condition: https://arxiv.org/pdf/2202.02100.
