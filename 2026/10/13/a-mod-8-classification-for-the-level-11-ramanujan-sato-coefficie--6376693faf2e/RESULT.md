# A mod-\(8\) classification for the level-\(11\) Ramanujan–Sato coefficients

## Finding
For the level-\(11\) Ramanujan–Sato coefficients \(c_{11}(n)\) defined by Campbell’s double-binomial formula, for every integer \(n\ge 1\),
\[
c_{11}(n)\equiv4\pmod8
\]
if and only if
\[
n=2^k\qquad\text{or}\qquad n=3\cdot2^k
\]
for some integer \(k\ge0\). At every other positive index,
\[
c_{11}(n)\equiv0\pmod8.
\]
Equivalently, \(\nu_2(c_{11}(n))=2\) exactly on these two dyadic rays, while \(\nu_2(c_{11}(n))\ge3\) elsewhere.

## Assumptions and scope
For integers \(n\ge0\), use Campbell’s formula
\[
c_{11}(n)=\sum_{\substack{a,b\ge0\\3a+b\le n}}T_n(a,b),
\]
where
\[
T_n(a,b)=
\binom na
\binom{n-a}{a+b}^{\!2}
\binom{2a+2b}{b}
\binom{2n-4a-2b}{n-3a-b}.
\]
The proof uses only exact binomial identities, Lucas’ parity criterion, and Kummer’s carry interpretation of prime-adic valuations. The statement concerns positive indices; the initial value is \(c_{11}(0)=1\).

Write \(s_2(m)\) for the number of ones in the binary expansion of a nonnegative integer \(m\), and write \(\nu_2(m)\) for the exponent of \(2\) in a positive integer \(m\).

## Proof
First observe the exact involution
\[
T_n(a,b)=T_n\bigl(a,n-3a-b\bigr).
\]
Indeed, under \(b\mapsto n-3a-b\), the squared binomial coefficient is replaced by its complementary form and the last two binomial factors are interchanged.

Consider first the slice \(a=0\). Then
\[
T_n(0,b)=\binom nb^2\binom{2b}{b}\binom{2n-2b}{n-b}.
\]
Legendre’s formula, equivalently Kummer’s theorem, gives
\[
\nu_2\binom nb=s_2(b)+s_2(n-b)-s_2(n),
\qquad
\nu_2\binom{2m}{m}=s_2(m).
\]
Hence, with
\[
A=s_2(b)+s_2(n-b),
\]
one has
\[
\nu_2\bigl(T_n(0,b)\bigr)=3A-2s_2(n).
\]
Since \(A\ge s_2(n)\), three cases follow.

If \(s_2(n)\ge3\), every term on the \(a=0\) slice is divisible by \(8\). If \(s_2(n)=2\), the only terms not divisible by \(8\) occur when \(A=2\), equivalently when the addition \(b+(n-b)=n\) is carry-free. There are exactly four such values of \(b\), one for each binary submask of \(n\). Each corresponding term has exact valuation \(2\), so their total is \(4\cdot4\equiv0\pmod8\); all remaining terms vanish modulo \(8\). If \(s_2(n)=1\), so \(n=2^k\), the only terms with valuation below \(3\) are \(b=0\) and \(b=n\). Both equal \(\binom{2n}{n}\), whose valuation is \(1\), and therefore their sum is \(4\) modulo \(8\). Thus
\[
\sum_b T_n(0,b)\equiv
\begin{cases}
4\pmod8,&n=2^k,\\
0\pmod8,&\text{otherwise}.
\end{cases}
\]

It remains to analyze \(a>0\). We first prove that every such summand is divisible by \(4\). Put
\[
u=a+b,
\qquad
v=n-2a-b.
\]
The summation inequalities give \(u,v\ge a>0\), and
\[
\binom{n-a}{a+b}=\binom{u+v}{u}.
\]
If this binomial coefficient is even, its square already contributes a factor \(4\). Suppose instead it is odd. Lucas’ theorem then says that \(u\) and \(v\) have disjoint binary supports.

Let \(t=\nu_2(a)\). At least one of \(u,v\), call it \(w\), has binary digit \(0\) in position \(t\). We claim
\[
4\mid\binom{2w}{w-a}.
\]
To see this, write \(a=2^t(2s+1)\). Because the \(t\)-th digit of \(w\) is zero, both \(w-a\) and \(w+a\) have digit \(1\) in position \(t\). When these two integers are added to obtain \(2w\), there is therefore a carry out of position \(t\), regardless of any incoming carry from lower positions. The digit of \(2w\) in position \(t+1\) equals the digit of \(w\) in position \(t\), hence is zero. The incoming carry at position \(t+1\) consequently forces a second carry. Kummer’s theorem gives the claimed divisibility by \(4\). If \(w=u\), this binomial coefficient is \(\binom{2u}{b}\); if \(w=v\), it is \(\binom{2v}{v-a}\), the final factor of \(T_n(a,b)\). Thus
\[
4\mid T_n(a,b)
\qquad(a>0).
\]

Now use the involution in \(b\). Every nonfixed pair contributes twice the same multiple of \(4\), hence contributes \(0\) modulo \(8\). A fixed point satisfies
\[
2b=n-3a.
\]
Writing \(u=a+b\), its summand becomes
\[
T_n(a,b)=
\binom na
\binom{2u}{u}^{\!2}
\binom{2u}{b}^{\!2}.
\]
Because
\[
\nu_2\binom{2u}{u}=s_2(u),
\]
a fixed summand can be nonzero modulo \(8\) only when \(s_2(u)=1\), so \(u\) is a power of \(2\), and when \(\binom{2u}{b}\) is odd. Since \(0\le b<u\) and \(2u\) has only one nonzero binary digit, Lucas’ theorem forces \(b=0\). Hence \(a=u=2^k\) and \(n=3\cdot2^k\). Conversely, in exactly this case \(\binom{3a}{a}\) is odd and the squared central binomial coefficient has valuation exactly \(2\), so the fixed summand is \(4\) modulo \(8\).

Combining the \(a=0\) slice with the \(a>0\) paired slices proves the stated dichotomy for every \(n\ge1\).

## Verification
The bundled `verify.py` performs exact-integer checks independent of floating-point arithmetic. It verifies Campbell’s binomial formula against the published D-finite recurrence for \(0\le n\le40\), verifies the residue classification from the recurrence for \(1\le n\le500\), checks the summand involution in \(13{,}880\) cases, checks all \(a>0\) summands through \(n=80\) for divisibility by \(4\), and exhaustively tests \(12{,}285\) bounded instances of the carry lemma. Its observed output is

`VERIFY_OK formula_recurrence=0..40 residue_pattern=1..500 symmetry_cases=13880 a_positive_terms=28431 carry_lemma_cases=12285 fixed_exceptions=5`

These finite checks corroborate the proof; they are not used to infer the infinite statement.

## Relationship to prior work
Campbell’s 2026 preprint proves the double-binomial formula above, thereby resolving the longstanding request for a fixed finite binomial expression for the level-\(11\) coefficients. The paper does not state the mod-\(8\) classification proved here.

OEIS A284756 records the recurrence, initial values, and references for the same sequence, but its inspected comments and formulas do not state a mod-\(8\) or exact \(2\)-adic minimum-valuation law.

Caruso, Fürnsinn, Vargas-Montoya, and Zudilin study reductions of Apéry-like generating series modulo primes. Their table includes A284756 and describes the level-\(11\) factorization pattern modulo odd primes. That result is a different, mod-prime statement and does not imply the mod-\(8\) classification here. The present proof specifically exploits Campbell’s newly available binomial summation together with binary carry structure.

## Limitations
The theorem determines only whether the valuation is exactly \(2\) or at least \(3\); it does not give \(\nu_2(c_{11}(n))\) when the valuation exceeds \(2\). No assertion is made about congruences modulo higher powers of \(2\), nor about analogous coefficient sequences at other levels. The literature comparison found no equivalent statement in the inspected sources, but search non-detection is not a proof of worldwide novelty. Independent audit has not been performed.

## References
1. John M. Campbell, *On a problem on Ramanujan–Sato series of level 11*, arXiv:2610.00551v1, 2026.
2. OEIS Foundation Inc., *A284756*, recurrence sequence for \(c_{11}\).
3. Xavier Caruso, Florian Fürnsinn, Daniel Vargas-Montoya, and Wadim Zudilin, *Galois Groups of Apéry-like Series Modulo Primes*, arXiv:2510.23298v1, 2025.
4. Shaun Cooper, Jinqi Ge, and Dongxi Ye, *Hypergeometric Transformation Formulas of Degrees 3, 7, 11 and 23*, J. Math. Anal. Appl. 421 (2015), 1358–1376, DOI:10.1016/j.jmaa.2014.07.061.
