# Ordered-prime construction for Novák numbers

A **Novák number** is a positive integer \(n\) satisfying
\[
n\mid 2^n+1.
\]
The result below gives an exact local criterion from the increasing prime factorization of \(n\), and then applies it to primitive solutions with two distinct prime factors.

## Theorem 1: ordered-prime prefix criterion

Let \(n>1\), and write its prime-power factorization in increasing prime order as
\[
n=p_0^{a_0}p_1^{a_1}\cdots p_r^{a_r},
\qquad p_0<p_1<\cdots<p_r,\qquad a_i\ge 1.
\]
Put
\[
N_i=\prod_{j=0}^i p_j^{a_j}.
\]
Then \(n\) is a Novák number if and only if

1. \(p_0=3\), and
2. for every \(1\le i\le r\),
   \[
   p_i\mid 2^{N_{i-1}}+1.
   \]

In particular, whenever \(n\) is Novák, every increasing-prime prefix
\[
3^{a_0},\quad 3^{a_0}p_1^{a_1},\quad \ldots,\quad
3^{a_0}p_1^{a_1}\cdots p_i^{a_i}
\]
is itself a Novák number.

### Proof: necessity

Assume \(n\mid 2^n+1\), and let \(p\mid n\) be prime. Set
\[
t=\operatorname{ord}_p(2).
\]
Since \(2^n\equiv -1\pmod p\), we have \(t\mid 2n\) but \(t\nmid n\). The integer \(n\) is odd, so necessarily
\[
t=2d\qquad\text{with }d\mid n.
\]
Also \(t\mid p-1\), hence every prime divisor of \(d\) is strictly smaller than \(p\). Because \(t=2d\) is the exact order, \(2^d\equiv-1\pmod p\).

Take first \(p=p_0\), the least prime factor of \(n\). Every prime divisor of \(d\) would have to divide \(n\) and be smaller than \(p_0\), so \(d=1\). Thus \(\operatorname{ord}_{p_0}(2)=2\), which forces \(2\equiv-1\pmod{p_0}\), hence \(p_0=3\).

Now take \(p=p_i\) with \(i\ge1\). All prime divisors of \(d\) occur among \(p_0,\ldots,p_{i-1}\), and \(d\mid n\), so \(d\mid N_{i-1}\). Since \(N_{i-1}/d\) is odd,
\[
2^{N_{i-1}}=(2^d)^{N_{i-1}/d}\equiv -1\pmod{p_i}.
\]
Therefore \(p_i\mid 2^{N_{i-1}}+1\), as required.

### Proof: sufficiency

The base prefix \(3^{a_0}\) is Novák: by the standard lifting-the-exponent identity,
\[
v_3(2^{3^{a_0}}+1)=v_3(2+1)+v_3(3^{a_0})=a_0+1.
\]

Suppose inductively that \(M=N_{i-1}\) is Novák and that the next prime \(p=p_i\) divides \(2^M+1\). Since \(p\nmid M\), for \(a=a_i\) the odd-power factorization gives
\[
2^M+1\mid 2^{Mp^a}+1,
\]
so \(M\mid2^{Mp^a}+1\). Also LTE gives
\[
v_p(2^{Mp^a}+1)=v_p(2^M+1)+a\ge a+1.
\]
Thus \(p^a\mid2^{Mp^a}+1\). Since \((M,p)=1\),
\[
Mp^a\mid2^{Mp^a}+1.
\]
Hence \(N_i\) is Novák. Induction proves the theorem.

## Corollary 2: complete two-prime classification

Let \(a,b\ge1\) and let \(q>3\) be prime. Then
\[
\boxed{\;3^a q^b\text{ is Novák}\iff q\mid 2^{3^a}+1.\;}
\]
Thus the exponents of \(q\) are unrestricted once \(q\) occurs at the corresponding \(3\)-power prefix.

## Corollary 3: primitive two-prime solutions

Use the Bailey--Smyth notion of **primitive**: a Novák number is primitive if it cannot be generated from smaller Novák numbers by their two closure operations (multiplying a Novák number by one of its divisors, and taking least common multiples).

For \(a,b\ge1\) and prime \(q>3\),
\[
\boxed{\;3^a q^b\text{ is primitive}\iff b=1\text{ and }
q\mid \Phi_{2\cdot3^a}(2).\;}
\]
Equivalently,
\[
\boxed{\;3^a q^b\text{ is primitive}\iff b=1\text{ and }
\operatorname{ord}_q(2)=2\cdot3^a.\;}
\]
Here
\[
\Phi_{2\cdot3^a}(2)
=\frac{2^{3^a}+1}{2^{3^{a-1}}+1}
=2^{2\cdot3^{a-1}}-2^{3^{a-1}}+1.
\]

Indeed, if \(b>1\), then \(3^a q^{b-1}\) is already a smaller Novák number with the same prime support. If \(q\) already divides \(2^{3^j}+1\) for some \(j<a\), then \(3^j q\) is a smaller Novák number with the same prime support. Conversely, if \(b=1\) and \(a\) is the first level at which \(q\mid2^{3^a}+1\), no smaller Novák number can contain \(q\) without introducing an extra prime, so neither Bailey--Smyth closure operation can generate \(3^a q\) from smaller members.

For \(q>3\), first occurrence at level \(a\) is equivalent to divisibility by the displayed cyclotomic quotient. To see this, put \(x=2^{3^{a-1}}\). The quotient is \(x^2-x+1\), while the preceding term is \(x+1\); their gcd divides \(3\). Hence a prime \(q>3\) dividing the quotient is new at level \(a\). Its order is then exactly \(2\cdot3^a\).

## Corollary 4: infinitely many primitive two-prime Novák numbers

For every \(a\ge2\), the integer
\[
C_a=\Phi_{2\cdot3^a}(2)
\]
has a prime divisor \(q_a>3\). Indeed,
\[
v_3(C_a)=v_3(2^{3^a}+1)-v_3(2^{3^{a-1}}+1)=1,
\]
while \(C_a>3\). Therefore \(3^a q_a\) is primitive by Corollary 3. Distinct levels give distinct orders \(2\cdot3^a\), so they give distinct primes and distinct primitive Novák numbers.

Consequently there are infinitely many primitive Novák numbers having exactly two distinct prime factors.

More quantitatively, if \(P_2(x)\) counts primitive Novák numbers \(n\le x\) with exactly two distinct prime factors, then for \(x\ge e^9\),
\[
\boxed{\;P_2(x)\ge \lfloor\log_3\log x\rfloor-1.\;}
\]
For each \(a\ge2\), choose \(q_a\mid C_a\), \(q_a>3\). Since
\[
3^a q_a\le3^a C_a
<3^a 2^{2\cdot3^{a-1}}<e^{3^a},
\]
every \(2\le a\le\lfloor\log_3\log x\rfloor\) supplies a distinct primitive example below \(x\).

The first levels recover familiar primitive terms:
\[
3^2\cdot19=171,
\qquad
3^3\cdot87211=2354697,
\qquad
3^4\cdot163=13203,
\]
and also \(3^4\cdot135433=10970073\), \(3^5\cdot1459=354537\), and \(3^5\cdot139483=33894369\).

## Computational check

The supplied exact-integer verification performs two independent bounded checks:

- every odd \(n\le10^6\) is tested both directly by \(2^n\equiv-1\pmod n\) and by the ordered-prime prefix criterion; both methods find 40 Novák numbers and there are zero mismatches;
- for every prime \(5\le q<200000\), \(1\le a\le8\), and \(1\le b\le3\), all 431,568 triples \(3^a q^b\) are compared against the direct congruence. There are 102 hits by each method and zero mismatches.

These computations are supporting evidence only; the theorem is proved without a cutoff.

## Relation to prior work and originality boundary

Bailey and Smyth proved that every nontrivial Novák number has least prime factor \(3\), gave strong restrictions from the exact power of \(3\), and introduced the primitive closure notion used above. Kalmynin proved the useful forward extension principle that if \(N\) is Novák and \(p\mid2^N+1\), then arbitrary powers of \(p\) can be adjoined while preserving the Novák property. OEIS A136475 records the prime factors of the successive cyclotomic quotients \(\Phi_{2\cdot3^a}(2)\), motivated by fast generation of Novák numbers.

The new contribution claimed here is the exact **if-and-only-if ordered-prime prefix criterion for the full prime factorization**, together with the resulting exact primitive classification in the two-prime-support case and the unconditional infinitude/counting consequence for primitive two-prime solutions. The sufficiency direction is closely related to Kalmynin's extension lemma; the converse prefix structure is the essential additional step.

To the best of our knowledge, searches of the Bailey--Smyth note, Kalmynin's paper, the relevant OEIS entries, later/current web-indexed literature, and the current SCOPE archive did not locate these statements in this form or a stronger theorem that immediately states them. The main residual originality risk is older or poorly indexed work on the congruence \(n\mid2^n+1\), including Břetislav Novák's original work and recreational/problem literature, or a general self-divisibility theorem for recurrence sequences whose specialization may imply the prefix criterion without using Novák terminology.

## Reproducibility

Run

```text
python artifacts/verify.py
```

with Python 3 and SymPy. The verification used SymPy 1.14.0; all congruence checks use exact integer arithmetic. Expected output is stored in `artifacts/verification.txt`.

## References

1. T. Bailey and C. Smyth, *Primitive solutions of n | 2^n + 1*, online note: https://webhomes.maths.ed.ac.uk/~chris/papers/n_divides_2to_nplus1.pdf
2. A. B. Kalmynin, *On Novák numbers*, Sbornik Mathematics 209 (2018), 491--502; arXiv:1611.00417: https://arxiv.org/abs/1611.00417
3. OEIS A006521, Novák numbers: https://oeis.org/A006521
4. OEIS A136473, primitive solutions: https://oeis.org/A136473
5. OEIS A136475, prime factors of successive quotients \((2^{3^{k+1}}+1)/(2^{3^k}+1)\): https://oeis.org/A136475
6. J. J. Alba González, F. Luca, C. Pomerance, and I. E. Shparlinski, *On numbers n dividing the nth term of a linear recurrence*, Proc. Edinburgh Math. Soc. 55 (2012), 271--289, doi:10.1017/S0013091510001355.
