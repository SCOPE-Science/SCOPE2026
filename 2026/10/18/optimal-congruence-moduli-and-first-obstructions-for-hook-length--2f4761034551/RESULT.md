# Optimal congruence moduli and first obstructions for hook-length and core-partition series

## Finding
Let \(t\ge2\) be an integer. Put \(A(q)=\prod_{j\ge1}(1-q^j)\), as a formal power series with integer coefficients, and define
\[
F_{t^2}(q)=A(q)^{t^2-1}=\sum_{n\ge0}a_t(n)q^n,
\qquad
C_t(q)=\frac{A(q^t)^t}{A(q)}=\sum_{n\ge0}b_t(n)q^n.
\]
These are, respectively, the Nekrasov--Okounkov hook-length generating function at the square parameter and the generating function for \(t\)-core partitions. Define the positive integer
\[
g(t)=\gcd\{a_t(n)-b_t(n):n\ge0\}.
\]
The greatest-common-divisor is well-defined and nonzero because \(a_t(1)-b_t(1)=-t^2\). For every \(t\ge2\),
\[
\boxed{\displaystyle
g(t)=\begin{cases}
p^{a+1},& t=p^a\text{ for a prime }p\text{ and integer }a\ge1,\\
1,&t\text{ has at least two distinct prime divisors}.
\end{cases}}
\]
More precisely, for every prime-power parameter \(t=p^a\), the congruence
\[
a_{p^a}(n)\equiv b_{p^a}(n)\pmod{p^{a+1}}
\]
holds for **every** integer \(n\ge0\); its exponent is best possible, and the first failure upon strengthening to modulus \(p^{a+2}\) occurs at exactly \(n=p^{a-1}\):
\[
\begin{aligned}
a_{p^a}(n)-b_{p^a}(n)&\equiv0\pmod{p^{a+2}} &&(0\le n<p^{a-1}),\\
a_{p^a}(p^{a-1})-b_{p^a}(p^{a-1})&\equiv-p^{a+1}\pmod{p^{a+2}}.
\end{aligned}
\]
For any non-prime-power \(t\), any prime \(p\mid t\), and the unique factorization \(t=p^a u\) with \(a\ge1\), \(p\nmid u\), \(u>1\), the *first* nonzero coefficient of \(F_{t^2}-C_t\) modulo \(p\) occurs at degree \(p^{2a}\), with
\[
a_t(p^{2a})-b_t(p^{2a})\equiv-u^2\pmod p.
\]

## Assumptions and scope
All products and congruences are identities in the complete ring \(\mathbb Z[[q]]\) or its quotient by the indicated positive integer; the coefficient variable is formal. The prime-power statement is universal in primes \(p\), exponents \(a\ge1\), and coefficient indices \(n\ge0\). The non-prime-power statement applies separately at each prime divisor of \(t\). No analytic convergence hypothesis is used.

## Proof
**1. Power-lifting lemma.** For every prime \(p\), integer \(r\ge1\), and series \(H(q)\in\mathbb Z[[q]]\), one has
\[
H(q)^{p^r}\equiv H(q^p)^{p^{r-1}}\pmod{p^r}.
\]
The base is the characteristic-\(p\) Frobenius identity \(H(q)^p\equiv H(q^p)\pmod p\). If \(U\equiv V\pmod{p^k}\) with \(k\ge1\), write \(U=V+p^k W\). Binomial expansion gives \(U^p\equiv V^p\pmod{p^{k+1}}\): the linear term has factor \(p^{k+1}\); terms with \(2\le j\le p-1\) have factors divisible by \(p^{1+2k}\); the final term has factor \(p^{kp}\). Raising the base identity to the \(p^{r-1}\)-th power therefore proves the lemma. Substitution \(q\mapsto q^{p^j}\) preserves every congruence.

**2. Prime powers and the first higher-order failure.** Fix \(t=p^a\). Let
\[
H_j(q)=A(q^{p^j})^{p^{2a-j}},\qquad 0\le j\le a.
\]
The lemma gives \(H_j\equiv H_{j+1}\pmod{p^{2a-j}}\) for \(0\le j<a\). Thus \(H_0\equiv H_a\pmod{p^{a+1}}\). Since \(A(q)\) has constant coefficient one, division by \(A(q)\) preserves divisibility, and
\[
F_{p^{2a}}(q)-C_{p^a}(q)=\frac{H_0(q)-H_a(q)}{A(q)}
\]
is coefficientwise divisible by \(p^{a+1}\).

For the stronger modulus, the first \(a-1\) steps give \(H_0\equiv H_{a-1}\pmod{p^{a+2}}\); when \(a=1\), this equality is exact. Write \(h=p^{a-1}\). As \(A(q)\equiv1-q\pmod{q^2}\),
\[
H_{a-1}(q)=A(q^h)^{p^{a+1}}\equiv 1-p^{a+1}q^h\pmod{q^{h+1}},
\]
whereas \(H_a(q)=A(q^{p^a})^{p^a}\equiv1\pmod{q^{h+1}}\). Hence, modulo \(p^{a+2}\), all coefficients of \(H_0-H_a\) below degree \(h\) vanish, while its coefficient at degree \(h\) is \(-p^{a+1}\). Multiplying by the integral unit \(1/A(q)\) leaves this first nonzero coefficient unchanged modulo \(p^{a+2}\). This proves both the first-failure assertion and optimality.

**3. Parameters with at least two prime factors.** Fix a prime \(p\mid t\) and write \(t=p^a u\), \(p\nmid u\), \(u>1\). In \(\mathbb F_p[[q]]\), repeated Frobenius gives
\[
A(q)^{t^2}=A(q^{p^{2a}})^{u^2},
\quad
A(q^t)^t=A(q^{p^{2a}u})^u.
\]
Their difference has zero coefficients in degrees \(0\le n<p^{2a}\) and coefficient \(-u^2\ne0\pmod p\) at degree \(p^{2a}\). Division by \(A(q)\), a unit with constant coefficient one modulo \(p\), preserves that first nonzero degree and coefficient. Thus \(p\nmid g(t)\) for every prime divisor \(p\) of \(t\).

Finally, because \(A(q)=1-q+O(q^2)\), and \(A(q^t)^t=1+O(q^t)\), one has
\[
a_t(1)-b_t(1)=-t^2.
\]
Consequently \(g(t)\mid t^2\). If \(t\) has at least two distinct prime factors, none can divide \(g(t)\), so \(g(t)=1\). If \(t=p^a\), step 2 shows that \(p^{a+1}\) divides \(g(t)\), but \(p^{a+2}\) does not; no other prime can divide it because \(g(t)\mid t^2\). Thus \(g(p^a)=p^{a+1}\). All cases are proved.

## Verification
The accompanying standalone `verify.py` computes \(F_{t^2}(q)-C_t(q)\) by exact integer arithmetic. It uses the logarithmic-derivative recurrence for Euler-product powers, an independent partition-number computation for the unit reciprocal, and additional direct factor-by-factor checks on smaller instances. Tested parameter values include \(2,4,8,3,9,5,25,7\) and non-prime-powers \(6,10,12,15,18,20,21,30\). It reports `VERIFY_OK` after checking the uniform exponents and the exact first obstruction coefficients. These finite tests do not prove the universally quantified assertions; the preceding formal-series argument does.

## Relationship to prior work
Sharma, *A Prime-Power Dichotomy for Nekrasov--Okounkov Hook Lengths and \(t\)-Core Partitions* (arXiv:2610.01422v1, first public October 1, 2026), proves that congruence modulo \(t\) holds at every coefficient exactly when \(t\) is a prime power, and proves the stronger modulus \(p^2\) for a prime \(t=p\). Its prime-power Proposition 2 states modulus \(p^a\) for \(t=p^a\). The genuinely strengthened part here is the **best possible** modulus \(p^{a+1}\) for all higher prime powers \(a\ge2\), including the exact first index where modulus \(p^{a+2}\) fails. The all-parameter gcd formulation joins that sharp new case to the previously known prime/non-prime-power dichotomy; the older special cases are not claimed as new. The early non-prime-power obstruction is also treated in Sharma's Section 4 and is credited.

Han, *The Nekrasov--Okounkov hook length formula: refinement, elementary proof, extension and applications* (arXiv:0805.1398), establishes the underlying hook-length and core-partition product identities, but does not state these optimal prime-power coefficient congruence exponents in the examined material. Other general power-lifting identities may contain implicit specializations; no assertion of independently certified literature uniqueness is made.

## Limitations
The classification concerns uniform coefficient congruences, not the valuations of every individual coefficient or distribution of such valuations. Its proof uses elementary formal power-series arithmetic; it neither requires nor proves new modular-form identities. The theorem's originality is assessed against the identified sources and available mathematical records, and complete absence of implicit earlier coverage has not been independently established.

## References
1. M. Sharma, *A Prime-Power Dichotomy for Nekrasov--Okounkov Hook Lengths and \(t\)-Core Partitions*, arXiv:2610.01422v1 (2026), https://arxiv.org/abs/2610.01422.
2. G.-N. Han, *The Nekrasov--Okounkov hook length formula: refinement, elementary proof, extension and applications*, arXiv:0805.1398 (2008), https://arxiv.org/abs/0805.1398.
3. F. Garvan, D. Kim, D. Stanton, *Cranks and \(t\)-cores*, Invent. Math. 101 (1990), 1--17.
