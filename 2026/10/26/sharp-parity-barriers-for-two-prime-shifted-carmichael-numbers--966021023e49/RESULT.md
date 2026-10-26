# Sharp parity barriers for two-prime shifted Carmichael numbers

## Finding
Fix an integer \(a\ge2\). Call a squarefree integer \(n\) an \((a,a)\)-Carmichael integer when \(p-a\mid n-a\) for every prime \(p\mid n\). This note classifies the two-prime case with both prime factors larger than \(a\), including the sharp parity-sensitive upper bound on their size.

For distinct primes \(p>q>a\), put \(c=a-1\). The following are equivalent:

1. \(n=pq\) is \((a,a)\)-Carmichael.
2. \(p-a\mid q-1\) and \(q-a\mid p-1\).
3. There are *unique* positive integers \(u<v\) such that, with \(d=uv-1\),
\[
 d\mid (v+1)c,\qquad d\mid (u+1)c,\qquad
 p=a+\frac{(v+1)c}{d},\quad
 q=a+\frac{(u+1)c}{d}.
\]

In (3) the displayed numbers are required to be prime (and hence their inequality \(p>q>a\) is automatic when \(u<v\)). Thus the finite parameter test enumerates *all* such semiprimes at any fixed \(a\). It has a parity restriction: when \(a\) is even, \(u,v\) must both be even.

The largest prime divisor has the **sharp uniform bounds**
\[
 p\le\begin{cases}
 4a-3,&a\text{ odd},\\
 a+\dfrac{5(a-1)}7=\dfrac{12a-5}7,&a\text{ even}.
 \end{cases}
\]
The odd-case bound is attained by \((a,p,q)=(11,41,31)\) and the even-case bound is attained by \((a,p,q)=(8,13,11)\). Consequently, for each fixed \(a\ge2\), only finitely many squarefree \((a,a)\)-Carmichael integers have exactly two prime factors both greater than \(a\). This is a complete classification for that natural large-prime branch, **not** a bound on integers with three or more prime factors or with a prime at most \(a\).

## Assumptions and scope
The shift \(a\) is a fixed integer at least \(2\), and \(p,q\) denote distinct primes strictly greater than \(a\). Divisibility has its usual integer meaning. All formulae are unconditional. When writing the parameters, \(u,v\) are positive integers satisfying \(1\le u<v\), so \(uv-1>0\). The prime-factor support is exactly \(\{p,q\}\), rather than two prime factors counted with repetition. The restriction \(p,q>a\) makes the shifted divisors positive and coprime to \(a\). The theorem does not silently extend to factors at most \(a\).

## Proof
**Step 1: a shifted Korselt reduction.** Modulo \(p-a\), the integer \(pq-a\) is congruent to \(a(q-1)\), because \(p\equiv a\pmod{p-a}\). Since \(p>a\) is prime, \(\gcd(a,p-a)=\gcd(a,p)=1\). Therefore
\[
 p-a\mid pq-a\quad\Longleftrightarrow\quad p-a\mid q-1.
\]
The same argument with \(p,q\) interchanged proves (1) equivalent to (2).

**Step 2: complete positive-integer parametrization.** Write \(r=p-a\), \(s=q-a\), and \(c=a-1\). Then \(r>s>0\), and (2) becomes \(r\mid s+c\), \(s\mid r+c\). Define the positive integers
\[
 u=\frac{s+c}{r},\qquad v=\frac{r+c}{s}.
\]
The equations \(ur=s+c\) and \(vs=r+c\) imply
\[
 (uv-1)r=(v+1)c,\qquad (uv-1)s=(u+1)c.
\]
Their right sides are positive, so \(d=uv-1>0\), and \(r>s\) gives \(v>u\). Consequently \(u,v\) are uniquely determined and the integrality conditions in (3) follow. Conversely, for any \(1\le u<v\) satisfying both integrality conditions, define \(r=(v+1)c/d\) and \(s=(u+1)c/d\). These are positive integers with \(r>s\), and the same equations show \(s+c=ur\), \(r+c=vs\). If \(a+r\), \(a+s\) are prime, their product satisfies (2) and hence (1). This proves the bijection.

The parameter search is finite: since \(s\ge1\), the equality \((uv-1)s=(u+1)c\) yields \(v\le c+(c+1)/u\le 2c+1\). Thus it suffices to test integer pairs \(1\le u<v\le 2a-1\). No external primality conjecture is needed.

**Step 3: parity restriction.** If \(a\) is even then \(p,q\) are odd, hence \(r,s,c\) are odd. Both \(s+c\) and \(r+c\) are even. Because their respective divisors \(r,s\) are odd, \(u,v\) are even.

**Step 4: sharp bounds.** From (3),
\[
 \frac{p-a}{a-1}=\frac{v+1}{uv-1}.
\]
For positive \(u<v\), this expression decreases strictly as either variable increases while the other is fixed. For unrestricted integral parameters the maximum occurs at \((u,v)=(1,2)\), giving \((p-a)/(a-1)\le3\), hence \(p\le4a-3\). When \(a\) is even, Step 3 forces even \(2\le u<v\), with maximum at \((u,v)=(2,4)\), giving \((p-a)/(a-1)\le5/7\). These are the asserted bounds.

For sharpness, \(a=11\), \((u,v)=(1,2)\) gives \(p=41\), \(q=31\), both prime, and
\[
 41-11=30\mid41\cdot31-11=1260,
 \qquad31-11=20\mid1260.
\]
Likewise \(a=8\), \((u,v)=(2,4)\) gives \(p=13\), \(q=11\), and
\[
 13-8=5\mid13\cdot11-8=135,
 \qquad11-8=3\mid135.
\]
Thus no smaller uniform linear bound of the displayed parity-specific form can hold. Finiteness follows immediately from either bound.

## Verification
The standalone `verify.py` runs a fully independent direct search through every prime pair \(a<q<p\le4a-3\) for each integer \(2\le a\le100\), testing the original shifted divisibilities directly. A separate search independently computes candidates from the \((u,v)\) parametrization with \(1\le u<v\le2a-1\). It compares the two sets exactly and checks both parity bounds and the explicit equality examples. Its expected successful output is

`VERIFY_OK parameters=99 parameterized_pairs=183 sharp_odd=11 sharp_even=8 independent_enumeration=PASS finite_only=YES`

The finite checks corroborate the algebraic classification. The general theorem and sharp uniform bounds are proved in the steps above, not inferred from the tests.

## Relationship to prior work
Wright's 2026 study introduces the same shifted Carmichael condition and investigates conditional lower bounds for the count of integers with a prescribed greatest common divisor among \(p-a\). The inspected main theorems and proof construct numbers with many prime factors; they do not state this exact large-prime semiprime parametrization or its sharp parity-sensitive factor bounds. Zheng's earlier \((a,b)\)-Carmichael terminology is broader, with a documented focus on \((-1,1)\); its abstract was consulted but its full text was not exhaustively checked. Ordinary Carmichael numbers correspond to shift \(a=1\), for which distinct semiprimes cannot satisfy Korselt's criterion, whereas for fixed \(a\ge2\) the branch here can be nonempty. Previously recorded two-prime classifications for weak Carmichael numbers concern a different arithmetic condition and do not imply these equal-shift inequalities. The claimed contribution is the **exact parameter bijection and sharp parity-stratified bounds**, not the basic modular reduction alone.

## Limitations
The restriction \(p,q>a\) is essential to the stated domain; pairs with one smaller prime and all products with three or more prime factors are outside this theorem. The paper of Zheng concerning generalized shifts was compared at the abstract level only; an unindexed existing parametrization cannot be excluded. The finite verifier is not an exhaustive novelty check and does not certify any unbounded claim. This is an unconditional elementary classification and does not require the prime-distribution conjecture in Wright's counting theorem.

## References
1. T. Wright, *\((a,a)\)-Carmichael numbers and greatest common divisors of \(p-a\)*, arXiv:2607.02738v1, first publicly posted 2026-07-02. https://arxiv.org/abs/2607.02738 ; lawful full text consulted at https://www.researchgate.net/publication/408521135_aa-Carmichael_numbers_and_greatest_common_divisors_of_p-a .
2. Q.-Y. Zheng, *There are infinitely many \((-1,1)\)-Carmichael numbers*, arXiv:2207.08641 (2022). https://arxiv.org/abs/2207.08641 .
3. A. Korselt, *Problème chinois*, L'Intermédiaire des Mathématiciens 6 (1899), 142--143; standard classical Carmichael criterion (for shift \(1\)).
