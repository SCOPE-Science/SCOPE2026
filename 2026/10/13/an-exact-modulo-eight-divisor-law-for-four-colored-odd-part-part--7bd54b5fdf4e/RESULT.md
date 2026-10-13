# An exact modulo-eight divisor law for four-colored odd-part partitions

## Finding

For each integer \(n\geq 0\), let \(a_4(n)\) count partitions of \(n\) in which every positive odd part may independently use any of four distinguishable colors, while every positive even part has a single color. A part of fixed size and color may be repeated. Put
\[
\chi_{-3}(d)=\begin{cases}0,&3\mid d,\\1,&d\equiv1\pmod3,\\-1,&d\equiv2\pmod3,\end{cases}
\qquad H(N)=\sum_{d\mid N}\chi_{-3}(d).
\]
Then **for every positive odd integer \(n\)**,
\[
\boxed{a_4(n)\equiv 2H(12n+1)\pmod8.}
\]
In particular, \(a_4(n)\) is always congruent to \(0\) or \(4\) modulo \(8\) at odd indices. To decide which, factor \(N=12n+1\). Its residue is \(4\) modulo \(8\) precisely when (i) each prime \(p\equiv2\pmod3\) divides \(N\) to an even exponent, and (ii) among primes \(p\equiv1\pmod3\), exactly one has exponent congruent to \(1\pmod4\), while every other has an even exponent. In all other cases the residue is zero.

This law has two distributional consequences:
\[
\lim_{X\to\infty}\frac{\#\{1\leq n\leq X:\ n\text{ odd and }8\mid a_4(n)\}}{\#\{1\leq n\leq X:\ n\text{ odd}\}}=1,
\]
and infinitely many positive odd \(n\) satisfy \(a_4(n)\equiv4\pmod8\), including every \(n=(p-1)/12\) with \(p\equiv13\pmod{24}\) prime.

## Assumptions and scope

All identities are identities of formal power series with integer coefficients, hence require no analytic convergence. The coefficient congruence and prime-factor classification apply to all positive odd indices, without a primality, squarefreeness, or size condition. No residue classification is asserted for even indices, or modulo \(16\) or higher powers of two.

Writing \(E(q)=\prod_{m\geq1}(1-q^m)\), the generating function and the overpartition series are
\[
F_4(q)=\sum_{n\geq0}a_4(n)q^n=\frac{E(q^2)^3}{E(q)^4},\qquad
P(q)=\frac{E(q^2)}{E(q)^2}.
\]
The first identity is the standard colored-partition product; \(P(q)\) is the ordinary overpartition generating function.

## Proof

**1. Two-adic theta reduction.** By Jacobi's triple product,
\[
P(q)^{-1}=\frac{E(q)^2}{E(q^2)}
=1+2\sum_{s\geq1}(-1)^s q^{s^2}.
\]
Thus \(P(q)=1+2B(q)\) for some \(B(q)\in\mathbb Z[[q]]\), with
\[
B(q)\equiv\sum_{s\geq1}q^{s^2}\pmod2.
\]
Because \(F_4(q)=E(q^2)P(q)^2\), squaring and using Frobenius in characteristic two gives
\[
F_4(q)\equiv E(q^2)\left(1+4\sum_{s\geq1}q^{s^2}
+4\sum_{s\geq1}q^{2s^2}\right)\pmod8.
\]
For odd \(n\), the first and third terms contain only even powers of \(q\). Euler's pentagonal number theorem now yields
\[
a_4(n)\equiv4T(n)\pmod8,\qquad
T(n)=\#\{(j,s)\in\mathbb Z\times\mathbb Z_{>0}:
 j(3j-1)+s^2=n\}.
\]
Indeed, \(E(q^2)=\sum_{j\in\mathbb Z}(-1)^j q^{j(3j-1)}\); after multiplication by four the signs disappear modulo eight. The number \(j(3j-1)\) is even, so every admissible \(s\) is odd when \(n\) is odd.

**2. Exact conversion to quadratic-form representations.** Put \(N=12n+1\), which satisfies \(N\equiv13\pmod{24}\) for odd \(n\). The substitutions
\[
x=6j-1,\qquad y=2s
\]
turn \(j(3j-1)+s^2=n\) into \(x^2+3y^2=N\), with \(x\equiv-1\pmod6\) and \(y>0\). Conversely, every integer solution \((x,y)\) of \(x^2+3y^2=N\) satisfies: \(x\) is odd and not divisible by three; \(y\equiv2\pmod4\); and \(x,y\neq0\). The first two claims follow by reducing the equation modulo three, four, and eight; the last follows because \(N\equiv5\pmod8\) is not a square. Consequently each orbit \((\pm x,\pm y)\) has four elements and exactly one has \(x\equiv-1\pmod6\) and \(y>0\). If \(r_3(N)\) counts all signed integer solutions of \(x^2+3y^2=N\), then
\[
r_3(N)=4T(n).
\]

**3. Divisor evaluation.** For positive odd \(N\) not divisible by three, the classical representation formula is
\[
r_3(N)=2\sum_{d\mid N}\chi_{-3}(d)=2H(N).
\]
For completeness, this follows by unique factorization in the Eisenstein integer ring \(\mathbb Z[\omega]\), \(\omega=(-1+\sqrt{-3})/2\). The number of integral ideals of norm \(N\) is \(H(N)\): split primes \(p\equiv1\pmod3\) contribute \(e+1\) choices at exponent \(e\), whereas inert primes \(p\equiv2\pmod3\) contribute one choice if their exponent is even and none otherwise. The ring is a principal ideal domain. Each ideal of odd norm has six associate generators. Modulo two, the six units map twice onto the three nonzero elements of \(\mathbb F_4\), and exactly two generators lie in \(\mathbb Z[\sqrt{-3}]\), those whose \(\omega\)-coefficient is even. Their norms are exactly the solutions \(x^2+3y^2=N\), proving the factor two. The same formula is recorded explicitly by Hirschhorn in the reference below.

Therefore \(a_4(n)\equiv4T(n)=r_3(N)=2H(N)\pmod8\), completing the coefficient identity.

**4. Exact residues.** Since \(N\) is nonsquare, \(H(N)\) is even by its prime-power factorization. If any prime congruent to two modulo three has odd exponent, then \(H(N)=0\). Otherwise
\[
H(N)=\prod_{p\equiv1\,({\rm mod}\,3)}\bigl(\nu_p(N)+1\bigr).
\]
This product is two modulo four exactly when one factor has valuation one at two and all others are odd. Equivalently, one split-prime exponent is \(1\pmod4\) and the others are even. This proves the asserted exhaustive residue test.

**5. Density and infinitely many exceptions.** The odd indices correspond bijectively to the integers \(N\equiv13\pmod{24}\). For each prime \(p\equiv1\pmod3\), necessarily \(p\geq7\), the proportion of integers in this progression with \(\nu_p(N)=1\) is exactly \((p-1)/p^2\); these events are independent over every fixed finite set of such primes by the Chinese remainder theorem. The sum of these probabilities diverges, since \(\sum_{p\equiv1\,({\rm mod}\,3)}1/p\) diverges. Consequently the proportion of the progression with fewer than two distinct such prime divisors of exact exponent one tends to zero: for a growing finite set of primes, independence makes the probability of zero or one such occurrence tend to zero. With at least two, the product for \(H(N)\) has two even factors, so \(4\mid H(N)\), implying \(8\mid a_4(n)\).

On the other hand, Dirichlet's theorem supplies infinitely many primes \(p\equiv13\pmod{24}\). For \(n=(p-1)/12\), we have \(H(12n+1)=H(p)=2\), giving \(a_4(n)\equiv4\pmod8\). These establish the two distributional statements.

## Verification

The standalone script `verify.py` computes all partition coefficients modulo eight by independent unrestricted-color dynamic programming through index \(1200\), evaluates \(H(12n+1)\) by explicit divisors, enumerates all representations \(x^2+3y^2=12n+1\), and enumerates the pentagonal-plus-square witnesses separately. For all \(600\) positive odd indices at most \(1200\), it verifies the three independent identities against the claimed congruence, as well as exact integer partition coefficients through index \(18\). The output is recorded in `verifier_output.txt`. These finite checks are corroboration; the general claim and density statements depend on the proofs above, not the finite computations.

## Relationship to prior work

Hirschhorn and Sellers [1] introduce this colored-partition family and its generating function, and prove \(a_4(7m+4)\equiv0\pmod7\) among other modulo-seven results. Jameson and Sellers [2] give a uniform approach to modulo-three congruences for the same family. The exact modulo-eight formula at every positive odd index, its prime-exponent classification, and its density-one consequence are distinct statements; no claim of priority over the definitions, product identities, or prior progressions is made. Hirschhorn's classical formula [3] evaluates the quadratic form representation count independently of the colored-partition sequence. Formula [3], combined with the theta reduction of the colored partition product, yields the present result. The standard divisor-sum sequence itself is also tabulated in [4]; that table does not state an identity with the colored partition coefficients.

## Limitations

The coefficient formula does not address even indices or residues beyond modulo eight. The density proof is qualitative and provides no effective error term. The congruence has been verified computationally only to a finite cutoff, not exhaustively by computation. The September 2026 paper [2] was available through metadata and abstract, but its full text could not be inspected; a differently phrased equivalent result in that text or elsewhere cannot be ruled out without further independent literature review. No independent audit is claimed.

## References

[1] M. D. Hirschhorn and J. A. Sellers, *A Family of Congruences Modulo 7 for Partitions with Monochromatic Even Parts and Multi-Colored Odd Parts*, arXiv:2507.09752 (first posted July 13, 2025), especially its generating function (4), Theorem 1.3, and proof. https://arxiv.org/html/2507.09752v2

[2] M. Jameson and J. A. Sellers, *A uniform proof approach for congruences modulo 3 for partitions with \(k\)-colored odd parts*, arXiv:2609.19440 (posted September 16, 2026). https://arxiv.org/abs/2609.19440

[3] M. D. Hirschhorn, *Three Classical Results on Representations of a Number*, Séminaire Lotharingien de Combinatoire **42** (1998), formula (1). DOI: 10.1007/978-3-642-56513-7_6.

[4] OEIS A002324, *Number of divisors of \(n\) congruent to one modulo three minus those congruent to two modulo three*, including its prime-factor formula. https://oeis.org/A002324
