# Complete classification of one- and two-step factorial divisor doublings

## Finding

Let \(\tau(N)\) be the number of positive divisors of a positive integer \(N\), and for every integer \(n\ge1\) put
\[
K(n)=\min\{k\ge1:\tau((n+k)!)\ge2\tau(n!)\}.
\]
This minimum exists because each subsequent prime multiplies the factorial divisor count by two. The following assertions determine **every** \(n\) for which \(K(n)\le2\).

1. \(K(n)=1\) if and only if \(n+1\) is prime or \(n=3\).
2. For \(n\ge1\) with \(n+1\) composite and \(n\ne3\), one has \(K(n)=2\) if and only if either \(n+2\) is prime, or both \(m=n+1\) and \(m+1\) are composite and one of these conditions holds:
   - \(m=2p\) and \(m+1=3q\), for primes \(p,q\);
   - \(m=3p\) and \(m+1=2q\), for primes \(p,q\);
   - \(m\in\{8,15,20,25,34\}\).

Equivalently, among consecutive composite arguments \(m,m+1\), one has
\[
\frac{\tau((m+1)!)}{\tau((m-1)!)}\ge2
\]
**exactly** in the two prime-pair families and the five exceptional windows above. The five exceptions and the prime-pair alternatives exhaust all arguments, including arbitrarily large ones.

## Assumptions and scope

All variables in the theorem are positive integers, all specified \(p,q\) are primes, and all inequalities are inclusive as written. A prime-pair family does **not** assert that it has infinitely many members: that question entails simultaneous primality of two linear forms. The result classifies the two-step threshold, not the distribution of higher values of \(K(n)\).

Write \(V_p(x)=\sum_{j\ge1}\lfloor x/p^j\rfloor\) for the exponent of prime \(p\) in \(x!\); write \(\Omega(t)\) for the total number of prime factors of \(t\) with multiplicity, \(P(t)\) for its largest prime factor, and
\[
S(t)=\sum_{p^a\parallel t}ap,\qquad R(t)=\frac{\tau(t!)}{\tau((t-1)!)}.
\]
The exact factors and finite cutoff specified below provide an independently executable certificate for the finite portion of the proof.

## Proof

**Step 1: exact local ratio.** Since \(t!=t(t-1)!\), for every integer \(t\ge2\),
\[
R(t)=\prod_{p^a\parallel t}\frac{V_p(t-1)+a+1}{V_p(t-1)+1}.
\tag{1}
\]
If \(t\) is prime, \(R(t)=2\). Also \(V_p(t-1)+1\ge t/p\) for every \(p\mid t\), so the elementary inequality \(1+x\le e^x\) gives
\[
R(t)\le\exp(S(t)/t).\tag{2}
\]

**Step 2: two regimes.** Suppose \(t\ge2048\) is composite. If \(P(t)\le\sqrt t\), then
\[
S(t)\le\Omega(t)\sqrt t\le(\log_2t)\sqrt t,
\quad R(t)\le e^{h(t)},\quad h(t):=\frac{\log_2t}{\sqrt t}.
\tag{3}
\]
Here \(\log_2 t\) means \(\log t/\log2\), **not** an iterated logarithm. The function \(h\) decreases for \(t\ge2048\), and \(h(t)\le11/\sqrt{2048}<11/45\).

Otherwise \(P(t)>\sqrt t\). Write \(t=aP\), with \(P=P(t)\) prime and integer \(a\ge2\). Then \(P\nmid a\) and \(P^2>t-1\); hence \(V_P(t-1)=a-1\). The \(P\)-factor in (1) is exactly \(1+1/a\). For the remaining factors, apply (2) restricted to primes dividing \(a\), and use \(S(a)\le a\) (the sum of prime factors with multiplicity never exceeds their product). We obtain
\[
R(t)\le\left(1+\frac1a\right)e^{S(a)/t}
\le\left(1+\frac1a\right)e^{1/P}
\le\left(1+\frac1a\right)e^{1/\sqrt t}.
\tag{4}
\]
The assertion \(S(a)\le a\) follows inductively from \(uv\ge u+v\) for integers \(u,v\ge2\), with the prime case giving equality.

**Step 3: consecutive composite arguments.** Let \(m\ge2048\) and suppose both \(m,m+1\) are composite. We show that \(R(m)R(m+1)<2\), unless one is twice a prime and the other is three times a prime. Both arguments are at least \(2048\). From \(45^2<2048\), (3)--(4), and the elementary bound
\[
e^u\le(1-u/2)^{-2}\qquad(0\le u<2),\tag{5}
\]
there are three cases.

- If both largest prime factors are at most the corresponding square roots, (3) gives
\[
R(m)R(m+1)<e^{22/45}\le(45/34)^2<2.
\]
- If exactly one is at most its square root, (3)--(4) and \(a\ge2\) give
\[
R(m)R(m+1)<\tfrac32 e^{12/45}\le\tfrac32(15/13)^2
=\tfrac{675}{338}<2.
\]
- If both have larger-than-square-root prime factors, write \(m=aP\), \(m+1=bQ\) as in (4). The cofactor attached to the even argument is even and at least \(2\), and the other cofactor is odd and at least \(3\). Unless these cofactors are exactly \(2\) and \(3\), their two leading factors have product at most \((3/2)(6/5)=9/5\): either the even cofactor is at least \(4\) or the odd cofactor is at least \(5\). Consequently
\[
R(m)R(m+1)<\tfrac95e^{2/45}
\le\tfrac95(45/44)^2<2.
\]
In the omitted cofactor case the integers necessarily form the two stated prime-pair configurations.

Conversely, for a prime-pair configuration at or above \(2048\), the two factors from the large primes in (1) are exactly \(3/2\) and \(4/3\), whose product is \(2\); all other prime factors in (1) are greater than one, so \(R(m)R(m+1)>2\).

To verify (5), take logarithms and use \(-\log(1-v)\ge v\) for \(0\le v<1\).

**Step 4: bounded exact certificate.** The accompanying self-contained `verify.py` exhaustively checks each integer \(2\le m<2048\) with exact integer numerator/denominator comparisons from (1), using prime exponents computed independently by Legendre's formula. Among consecutive composite pairs, it finds **exactly** 60 windows meeting the inequality: 55 satisfying one of the two prime-pair conditions and precisely five others beginning at \(m=8,15,20,25,34\). It also checks that among composite \(m\) in this range, \(R(m)\ge2\) occurs only at \(m=4\). By (3)--(4), no composite \(m\ge2048\) has \(R(m)\ge2\). Indeed the first regime bounds it by \(e^{11/45}<2\), and the second bounds it by \((3/2)e^{1/45}<2\), using (5) for both. Thus the one-step assertion follows, and multiplication of consecutive ratios completes the two-step classification.

## Verification

Run `python3 verify.py` with Python 3 standard library only. The checker uses a smallest-prime-factor sieve, exact Legendre valuations, and integer cross-multiplication. It independently recomputes \(\tau(m!)\) cumulatively for \(2\le m\le2048\), including a separate full-range threshold comparison. The expected output includes `composite_pairs=1430`, `two_step_hits=60`, `prime_pair_hits=55`, `exceptional=[8, 15, 20, 25, 34]`, `one_step=[4]`, and `exact_integer=PASS`. It makes no assertion that finite tests alone prove the unbounded claim: the cutoff above is handled in Steps 2--3.

## Relationship to prior work

Freiberg, *Long runs of integers with small prime factors and the divisor function of \(n!\)* (2026), defines the identical threshold \(K(n)\), recalls the upper bound (2) as Lemma 4.1, and proves lower bounds for \(K(n)\) along sparse large values. Erdős, Graham, Ivić and Pomerance, *On the number of divisors of \(n!\)* (1996), introduced and studied the threshold, particularly average orders and large exceptional values. Their inspected treatments do not state the present exact one- and two-step classification. The upper bound (2), its standard factorial-divisor proof, and prime jumps are not presented as original.

## Limitations

The classification supplies no asymptotic count for the simultaneous-prime families and does not determine \(K(n)\) when it is at least three. Priority comparisons cover accessible primary texts and indexed research records, not every possible unpublished derivation or computational table. The finite certificate is exhaustive only on its explicitly specified range; the unrestricted exclusion is justified by the independent analytic estimate.

## References

- T. Freiberg, *Long runs of integers with small prime factors and the divisor function of \(n!\)*, arXiv:2609.15597v1 (first posted 2026-09-14), §§1 and 4. https://arxiv.org/html/2609.15597
- P. Erdős, S. W. Graham, A. Ivić, and C. Pomerance, *On the number of divisors of \(n!\)* (1996), §§2--4. https://math.dartmouth.edu/~carlp/factorial.pdf
