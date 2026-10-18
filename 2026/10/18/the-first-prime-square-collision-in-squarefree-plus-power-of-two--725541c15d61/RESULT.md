# The first prime-square collision in squarefree-plus-power-of-two progressions

## Finding
Let \(E=\{0,1,2,3,5,6,7,8,9,11,12,13,14,15,17,18,19,20\}\). For a prime \(p\equiv7\pmod{36}\), say that \(p\) **fails the first eighteen admissible exponents** if every positive integer \(p-2^a\), \(a\in E\), is non-squarefree. For each \(0\le j\le18\), define the absolutely convergent product
\[
H_j=\prod_{q\ge5\atop q\,\mathrm{prime}}\left(1-\frac{j}{q(q-1)}\right),\qquad H_0=1.
\]
The relative density among primes \(p\equiv7\pmod{36}\) of those failing all eighteen exponents exists, is strictly positive, and equals
\[
\boxed{\Theta_{18}=\sum_{j=0}^{18}(-1)^j\binom{18}{j}H_j+
\sum_{j=2}^{18}(-1)^j\binom{16}{j-2}\frac{H_j}{20-j}.}
\]
The second sum is **strictly positive**. Thus the formal 18-distinct-class extrapolation of the earlier disjoint local-factor law is a strict underestimate. The additional term is the exact correction forced by the first prime-square collision, \(2^{20}\equiv1\pmod{25}\). Every sufficiently large prime counted here requires an exponent at least \(21\) for any squarefree-plus-power-of-two representation (if one exists).

## Assumptions and scope
All primes \(p\) are rational, and the density is relative to \(\pi(X;36,7)\) as \(X\to\infty\). The finite exceptions \(p\le2^{20}\) do not affect it; positivity of the remainders is required in the definition. Squarefree means divisible by no prime square. For \(p\equiv7\pmod{36}\), exponents congruent to \(4\pmod6\) are inadmissible because \(9\mid p-2^a\). The displayed set therefore consists of precisely the eighteen admissible exponents from \(0\) through \(20\). Neither the Erdős representation conjecture for all exponents nor quantitative error terms in this density are asserted.

## Proof
**1. Exact first collision.** For odd \(q\), the congruences \(p\equiv2^a\pmod{q^2}\) and \(p\equiv2^b\pmod{q^2}\) are identical if and only if \(q^2\mid2^{|b-a|}-1\). For \(1\le d\le20\), trial division by primes \(5\le q\le\sqrt{2^{20}-1}<1024\) finds exactly the pair \((d,q)=(20,5)\). This is also an elementary bounded certificate: loop through all integers \(5\le q\le1023\), retain primes, and test divisibility of \(2^d-1\) by \(q^2\) for each \(1\le d\le20\), as in the attached verifier. No larger \(q\) can satisfy the divisibility. In particular the \(18\) shifts \(2^a\), \(a\in E\), give distinct reduced residue classes modulo \(q^2\) for each prime \(q\ge7\). At \(q=5\), exactly the two exponents \(0\) and \(20\) coincide, leaving \(17\) distinct classes.

**2. A simultaneous squarefree-density lemma for these shifts.** Write \(T\subseteq E\), \(j=|T|\), and let \(r_q(T)\) be the number of distinct elements of \(\{2^a\bmod q^2:a\in T\}\). For every fixed \(T\), the primes in the progression \(p\equiv7\pmod{36}\) for which all \(p-2^a\), \(a\in T\), are squarefree have relative density
\[
\delta(T)=\prod_{q\ge5}\left(1-\frac{r_q(T)}{q(q-1)}\right).
\]
Here is a full justification that also handles the colliding residue classes. The shifts are fixed and \(q=2,3\) never creates a square divisor when \(a\in E\), by reducing \(p-2^a\) modulo \(4\) and \(9\). For positive \(n\) and \(y\ge2\), put \(D_y(n)=\sum_{d^2\mid n,\ d\le y}\mu(d)\), \(D(n)=\sum_{d^2\mid n}\mu(d)\), \(B(n)=\sum_{d^2\mid n}1\), and \(B_{>y}(n)=\sum_{d^2\mid n,\ d>y}1\). Then \(D(n)=\mathbf1_{n\ \mathrm{squarefree}}\) and \(|D-D_y|\le B_{>y}\). For any fixed positive integer \(m\), the number of squarefree \(m\)-tuples whose least common multiple is \(L\) is \((2^m-1)^{\omega(L)}\) if \(L\) is squarefree. Expansion of the \(m\)th powers and the count of multiples of \(L^2\) give, uniformly for every fixed additive shift \(c\),
\[
\sum_{c<n\le X}B(n-c)^m\ll_m X,
\qquad
\sum_{c<n\le X}B_{>y}(n-c)^m\ll_m Xy^{-1/2}+X^{3/4}.
\]
Indeed both follow by grouping tuple least common multiples \(L\le\sqrt X\), using \(X/L^2+1\), the convergent sums \(\sum_L(2^m-1)^{\omega(L)}/L^{3/2}\) and \(\sum_L(2^m-1)^{\omega(L)}/L^2\), and \(L>y\) for the second bound. Set \(m=18\), \(y=(\log X)^{72}\). Hölder bounds the total of every cross term in the replacement of the product \(\prod_{a\in T}D(p-2^a)\) by \(\prod_{a\in T}D_y(p-2^a)\) by \(O_T(X/(\log X)^2+X^{71/72})=o(X/\log X)\), even after dropping primality. There are at most \(y^{18}\) tuples of squarefree divisors in the truncated main term, and each resulting modulus divides \(36y^{36}\), a fixed power of \(\log X\). The Chinese remainder theorem either rules out a tuple of congruences \(p\equiv2^a\pmod{d_a^2}\), or combines it into a single **reduced** residue class of modulus \(36\operatorname{lcm}(d_a)^2\). Uniform Siegel–Walfisz equidistribution applies to all admissible tuples; the total error remains \(o(X/\log X)\). Finally the absolutely convergent Möbius sum factors prime-by-prime: if a prime \(q\) is assigned to a nonempty subset of labels with identical residues modulo \(q^2\), its signed total is \(-1\) per distinct residue class, since \(\sum_{\emptyset\ne S\subseteq C}(-1)^{|S|}=-1\). Thus its Euler factor is exactly \(1-r_q(T)/\varphi(q^2)\), proving the density lemma. Finite initial exceptions and negative shifted arguments are omitted.

**3. Inclusion–exclusion and the exact formula.** For \(q\ge7\), \(r_q(T)=j\). For \(q=5\), \(r_5(T)=j-\mathbf1_{\{0,20\}\subseteq T}\). Hence
\[
\delta(T)=H_j\left(1+\frac{\mathbf1_{\{0,20\}\subseteq T}}{20-j}\right),
\]
where \(20-j\ge2\). The event of failure at every exponent is the product of the complements of the eighteen squarefree events. Applying inclusion–exclusion over all \(T\subseteq E\), and counting \(\binom{18}{j}\) subsets of size \(j\), of which \(\binom{16}{j-2}\) contain both \(0\) and \(20\), gives the boxed expression.

**4. Strict positivity of the collision correction.** Form a product probability space indexed by primes \(q\ge7\), independently choosing one reduced residue modulo \(q^2\) uniformly. At each \(q\) at most one of the eighteen labels is hit by the selected residue; write \(U\subseteq E\) for the labels never hit by any \(q\ge7\). This is well-defined almost surely, because the total expected number of hits is bounded by \(18\sum_{q\ge7}1/(q(q-1))<\infty\). For the \(q=5\) factor, compare two probability laws: the *actual* one, which assigns probability \(1/20\) to hitting the pair \(\{0,20\}\), probability \(1/20\) to each of the other sixteen singleton labels, and probability \(3/20\) to hitting none; and an *artificial all-distinct* law, assigning probability \(1/20\) to each of eighteen singleton labels and \(2/20\) to none. Conditioning on \(U\), the probability that all labels are covered differs between these two laws by \(1/20\) if \(U=\{0,20\}\) and by zero otherwise. Consequently the second sum in the boxed formula equals
\[
\boxed{\frac1{20}\Pr(U=\{0,20\})>0.}
\]
Strictness follows by selecting sixteen distinct primes \(q_a\ge7\), one for each \(a\in E\setminus\{0,20\}\), forcing the residue at \(q_a\) to be \(2^a\), and requiring all other primes \(q\ge7\) to avoid the two residue classes \(1,2^{20}\). These requirements have positive joint probability: the finitely many forced events have positive probabilities, and the avoidance tail has a positive convergent product because \(\sum_{q\ge7}2/(q(q-1))<\infty\).

**5. Positive density of complete failures.** Choose eighteen distinct primes \(q_a\ge7\), one per \(a\in E\), and impose the CRT conditions \(p\equiv7\pmod{36}\) and \(p\equiv2^a\pmod{q_a^2}\). The resulting residue class is coprime to its modulus, hence contains a positive relative proportion of the primes \(p\equiv7\pmod{36}\) by Dirichlet's theorem. Every sufficiently large such prime has all eighteen remainders divisible by the specified squares. Thus \(\Theta_{18}>0\).

## Verification
The accompanying `verify.py` checks the exact exponent list, all potential prime-square divisors of \(2^d-1\) for \(1\le d\le20\), and the local Euler-factor identities for all subsets of up to eighteen exponents at small primes. It independently evaluates the formula in a finite product probability model containing sixteen primes \(q\ge7\), where the first collision creates a strictly positive event that the artificial no-collision model cannot realize. These are finite checks of lemmas, not a proof of asymptotic prime equidistribution; the preceding argument supplies the infinite proof.

## Relationship to prior work
Harman and Paquin, *The One-Power Erdős Conjecture for Primes \(p\equiv7\pmod{36}\)*, arXiv:2610.07214 (first submitted 2026-10-05), prove exact densities for the first four exponents and explain how their method extends to the first sixteen admissible exponents of width below twenty. Their Proposition 2 and Remark 3 identify the \(q=5\), twenty-step congruence collision, while Remark 4 explicitly leaves its changed local factors untreated. The present result determines the first such out-of-range exact density, including a strictly positive quantitative collision correction. The underlying squarefree sieve draws on Mirsky's 1949 work; no claim is made to originate general linear-form squarefree sieving.

## Limitations
No decimal digits for \(\Theta_{18}\) are claimed: its alternating formula is numerically ill-conditioned. No universal representation theorem or explicit lower bound for the least prime with all eighteen failures is established. The result is a specialized explicit local-factor calculation based on standard sieve methods; an earlier general multivariate squarefree distribution theorem may imply its existence implicitly. Independent validation has not been performed.

## References
1. Shen Harman and Dana Paquin, *The One-Power Erdős Conjecture for Primes \(p\equiv7\pmod{36}\)*, arXiv:2610.07214, first public 2026-10-05. Specifically Lemma 2, Proposition 2, Theorem 4, Remark 4, and Theorem 5.
2. L. Mirsky, *The number of representations of an integer as the sum of a prime and a \(k\)-free integer*, 1949, as cited in the first reference.
3. Andrew Granville and Kannan Soundararajan, *A binary additive problem of Erdős and the order of 2 mod \(p^2\)*, 1998, as cited in the first reference.
