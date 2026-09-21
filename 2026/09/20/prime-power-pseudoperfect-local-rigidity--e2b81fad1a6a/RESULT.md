# Local congruence criterion and three-support rigidity for prime power pseudoperfect numbers

## Statement

For an integer
\[
n=\prod_{i=1}^s p_i^{a_i}>1,
\qquad P_i=p_i^{a_i},\qquad m_i=\frac{n}{P_i},
\]
define
\[
H(n)=\frac1n+\sum_{i=1}^s\sum_{k=1}^{a_i}\frac1{p_i^k}.
\]
Thus `n` is prime power pseudoperfect when \(H(n)=1\).

### Theorem 1: local integrality criterion
For every \(n>1\),
\[
H(n)\in\mathbb Z
\quad\Longleftrightarrow\quad
m_i\equiv p_i-1\pmod{P_i}\quad(1\le i\le s).
\]
In particular, when \(\omega(n)\le4\), these congruences are equivalent to prime power pseudoperfectness:
\[
H(n)=1
\quad\Longleftrightarrow\quad
\frac{n}{p_i^{a_i}}\equiv p_i-1\pmod{p_i^{a_i}}
\quad\text{for every }p_i^{a_i}\Vert n.
\]
For squarefree \(n\), the condition reduces to the familiar weak-primary-pseudoperfect congruence \(n/p\equiv-1\pmod p\).

### Theorem 2: rigidity with three prime supports and a simple middle prime
Let
\[
n=p^a q r^c,
\qquad p<q<r,
\qquad a,c\ge1,
\]
have exactly three distinct prime divisors and suppose the middle prime has exponent one. Then
\[
n\text{ is prime power pseudoperfect}
\quad\Longleftrightarrow\quad
\boxed{n=6\cdot7^c\quad(c\ge1)}.
\]
Consequently, every three-support prime power pseudoperfect number outside the family \(6\cdot7^c\) has middle-prime exponent at least two.

## Proof of Theorem 1
Put
\[
T=nH(n)=1+\sum_{i=1}^s m_i(1+p_i+\cdots+p_i^{a_i-1}).
\]
Fix \(i\). Modulo \(P_i\), every block with index \(j\ne i\) vanishes, because it retains the full factor \(P_i\). Hence, with
\[
U_i=1+p_i+\cdots+p_i^{a_i-1}=\frac{P_i-1}{p_i-1},
\]
we have
\[
T\equiv1+m_iU_i\pmod{P_i}.
\]
The congruence \(1+m_iU_i\equiv0\pmod{P_i}\) is equivalent to \(m_i\equiv p_i-1\pmod{P_i}\). Indeed, multiplying the first congruence by \(p_i-1\), which is coprime to \(P_i\), gives
\[
(p_i-1)+m_i(P_i-1)\equiv p_i-1-m_i\equiv0\pmod{P_i};
\]
the converse follows by reversing the calculation. Since the \(P_i\) are pairwise coprime, the Chinese remainder theorem gives
\[
n\mid T
\quad\Longleftrightarrow\quad
P_i\mid T\ \text{for every }i,
\]
which is exactly \(H(n)\in\mathbb Z\).

It remains to show that for at most four distinct prime divisors, a positive integral value of \(H(n)\) cannot exceed 1. Since each finite geometric sum is strictly smaller than its infinite counterpart,
\[
H(n)<\frac1n+\sum_{p\mid n}\frac1{p-1}.
\]
For \(s=1,2,3,4\), using the smallest possible distinct primes and \(n\ge\prod_{p\mid n}p\) gives respectively the upper bounds
\[
\frac32,\qquad
1+\frac12+\frac16=\frac53,\qquad
1+\frac12+\frac14+\frac1{30}=\frac{107}{60},
\]
and
\[
1+\frac12+\frac14+\frac16+\frac1{210}=\frac{269}{140},
\]
all strictly below 2. Thus a positive integral \(H(n)\) must equal 1. The converse is immediate.

## Proof of Theorem 2
Assume \(n=p^a q r^c\) is prime power pseudoperfect with \(p<q<r\) and the exponent of \(q\) equal to one.

First, \(p=2\). If all three primes were odd, then \(p\ge3,q\ge5,r\ge7\), so
\[
H(n)<\frac12+\frac14+\frac16+\frac1{105}=\frac{389}{420}<1,
\]
a contradiction.

Write
\[
A=2^a,\qquad R=r^c,\qquad V=1+r+\cdots+r^{c-1}=\frac{R-1}{r-1}.
\]
The sum of the reciprocal powers of 2 is \(1-1/A\). The equation \(H(n)=1\) therefore becomes
\[
\frac1q+\frac VR+\frac1{AqR}=\frac1A.
\]
After multiplying by \(AqR\),
\[
AR+AqV+1=qR.
\]
Set \(d=q-A\). The right-hand side shows \(d>0\), and using \(R=1+(r-1)V\) gives
\[
d-1=\bigl(Aq-d(r-1)\bigr)V. \tag{1}
\]

If \(d=1\), equation (1) gives \(r-1=Aq\). Hence
\[
q=A+1,\qquad r=A(A+1)+1=A^2+A+1.
\]
Modulo 3, if \(a\) is even then \(A\equiv1\pmod3\), so \(r\equiv0\pmod3\), impossible because \(r>3\). If \(a>1\) is odd then \(A\equiv2\pmod3\), so \(q=A+1\equiv0\pmod3\), again impossible because \(q>3\). The only surviving case is \(a=1\), yielding \((A,q,r)=(2,3,7)\).

Now suppose \(d>1\). Equation (1) has positive left-hand side, so its coefficient of \(V\) is a positive integer and therefore \(V\le d-1\). If \(c\ge2\), then
\[
V\ge r+1>q>d-1,
\]
a contradiction. Thus \(c=1\) at this stage, so \(V=1\). Equation (1) then becomes
\[
dr=Aq+1.
\]
Since \(q=A+d\),
\[
d(r-A)=A^2+1.
\]
Put \(e=r-A\). Then \(e>d>1\) and
\[
de=A^2+1\equiv2\pmod3.
\]
Thus \(d,e\) are nonzero modulo 3, with one congruent to 1 and the other to 2. Since \(A\equiv1\) or \(2\pmod3\), exactly one of
\[
q=A+d,\qquad r=A+e
\]
is divisible by 3. In the present case both are greater than 3, contradicting primality. Hence \(d>1\) is impossible.

We have proved that every number in the stated slice has the form \(6\cdot7^c\). Conversely,
\[
\frac12+\frac13+\sum_{j=1}^c\frac1{7^j}+\frac1{6\cdot7^c}
=\frac56+\frac{1-7^{-c}}6+\frac{7^{-c}}6=1,
\]
so every \(6\cdot7^c\) is prime power pseudoperfect.

## Context and relation to prior work
John Machacek introduced prime power pseudoperfect numbers and proved that every term greater than 1 of OEIS A073935 is prime power pseudoperfect. He also proved the closure rule that if \(n\) is prime power pseudoperfect and \(n+1\) is prime, then \(n(n+1)^k\) is prime power pseudoperfect for every nonnegative \(k\). Starting from \(n=6\), this constructs the family \(6\cdot7^c\). The theorem above supplies a converse inside the natural three-support slice whose middle prime occurs to the first power: no other family is possible there.

OEIS A283423 records prime power pseudoperfect numbers and notes that it eventually diverges from A073935. The local criterion above applies to that broader class, including prime powers and non-A073935 examples, and for up to four prime supports turns a global Egyptian-fraction equality into independent prime-power congruences.

The squarefree specialization is compatible with the established weak-primary-pseudoperfect/1-Sondow condition. Recent work on primary pseudoperfect numbers, including the port formalism of Wang, concerns the squarefree equation; the searches described in the review did not locate the prime-power congruence criterion or the three-support uniqueness statement proved here.

## Verification
A standalone exact-rational verifier is included as `artifacts/verify.py`. It checks all integers \(2\le n\le100000\) with at most four distinct prime divisors, comparing the defining equality \(H(n)=1\) against the local congruences. It checks 98,158 integers and finds zero mismatches. It also verifies the first twelve members of \(6\cdot7^c\) directly by exact rational arithmetic. The deterministic output is in `artifacts/verification.txt`.

The finite computation is supporting evidence only; both the local criterion and the three-support classification are proved above for all stated parameters.

## Limitations
- The equivalence between local congruences and \(H(n)=1\) is proved here only for \(\omega(n)\le4\). For arbitrary support size, the congruences characterize integrality of \(H(n)\), not by themselves the value 1.
- The three-support classification assumes the middle prime has exponent exactly one. It does not classify the case \(p^a q^b r^c\) with \(b\ge2\).
- Originality is to the best of our knowledge. Terminology around weak primary pseudoperfect and Sondow-type congruences creates some residual risk of an equivalent formulation under a different name.

## References
1. J. Machacek, *Egyptian Fractions and Prime Power Divisors*, Journal of Integer Sequences 21 (2018), Article 18.3.7. https://cs.uwaterloo.ca/journals/JIS/VOL21/Machacek/mach4.pdf
2. OEIS A283423, *Prime power pseudoperfect numbers*. https://oeis.org/A283423
3. J. M. Grau, A. M. Oller-Marcén, D. Sadornil, *On μ-Sondow Numbers*, arXiv:2111.14211. https://arxiv.org/abs/2111.14211
4. H. Wang, *Port Fillings for Primary Pseudoperfect Numbers*, arXiv:2605.21518. https://arxiv.org/abs/2605.21518
