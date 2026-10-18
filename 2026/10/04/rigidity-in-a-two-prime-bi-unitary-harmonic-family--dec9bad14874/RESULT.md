# Rigidity in a two-prime bi-unitary harmonic family

## Finding
Let \(p\) and \(q\) be distinct primes and \(a\ge1\). Then \(p^{2a}q\) is bi-unitary harmonic if and only if
\[
(p,a,q)=(3,1,5).
\]
In particular, the unique such integer is \(45=3^2\cdot5\).

## Definitions and scope
For a positive integer \(m\), denote by \(\sigma^{**}(m)\) the sum and by \(d^{**}(m)\) the number of its bi-unitary divisors. The bi-unitary harmonic condition is
\[
\sigma^{**}(m)\mid m\,d^{**}(m).
\]
The functions are multiplicative on coprime factors. In the prime-power cases used here,
\[
\sigma^{**}(p^{2a})=\sigma(p^{2a})-p^a
=\frac{(p^a-1)(p^{a+1}+1)}{p-1},\qquad
 d^{**}(p^{2a})=2a,
\]
and \(\sigma^{**}(q)=q+1\), \(d^{**}(q)=2\).
The theorem concerns precisely exponent patterns \((2a,1)\), not all two-prime bi-unitary harmonic numbers.

## Proof
Put
\[
A=\frac{p^a-1}{p-1}=1+p+\cdots+p^{a-1},\qquad C=p^{a+1}+1.
\]
The defining divisibility gives
\[
AC(q+1)\mid 4a\,p^{2a}q.
\tag{1}
\]
Since \(\gcd(AC,p)=1\) and \(\gcd(q+1,q)=1\), necessary consequences are
\[
AC\mid4aq,\qquad q+1\mid4ap^{2a}.
\tag{2}
\]
Moreover \(AC>p^{2a}\) for every prime \(p\) and integer \(a\ge1\): indeed
\(AC=(1+\cdots+p^{a-1})(p^{a+1}+1)\) exceeds
\(p^{a-1}\cdot p^{a+1}=p^{2a}\).

**Case 1: \(q<p\).** The exceptional consecutive-prime pair \((q,p)=(2,3)\) must be separated: here (2) would give \(AC\mid8a\), while
\(AC>3^{2a}=9^a>8a\) for every \(a\ge1\), a contradiction.
For all other \(q<p\), the prime \(p\) cannot divide \(q+1\): otherwise \(p\le q+1<p+1\), so \(p=q+1\), which among primes occurs only for the already excluded pair \((2,3)\). Thus (2) implies \(q+1\mid4a\), hence \(q<4a\). We obtain
\[
p^{2a}<AC\le4aq<16a^2.
\]
Because \(p\ge3\), this is impossible when \(a\ge2\): \(9^a\ge16a^2\) for all \(a\ge2\) (the base case is \(81>64\), and the ratio \(9^a/a^2\) grows thereafter). Consequently \(a=1\). Then \(q+1\mid4\) gives \(q=3\), and \(p>3\), whereas \(AC=p^2+1>12=4q\), contradicting (2).

**Case 2: \(p<q\le4a\).** By (2),
\[
p^{2a}<AC\le4aq\le16a^2.
\]
Since \(p\ge2\), this is impossible for \(a\ge4\), as \(4^a\ge16a^2\) for \(a\ge4\). If \(a=1\), the only candidate prime \(p<q\le4\) is \(p=2,q=3\), with \(AC=5\nmid12\); the arithmetically possible \(p=3\) has no prime \(q\) between 3 and 4. For \(a=2\), \(p=2\) is the only possibility under \(p^4<64\), and then \(AC=27\nmid8q\) for primes \(2<q\le8\). For \(a=3\), \(p=2\) is again the only possibility under \(p^6<144\), and \(AC=119\nmid12q\) for primes \(2<q\le12\) (the factor 17 exceeds \(q\)). Thus this case is empty.

**Case 3: \(p<q\) and \(q>4a\).** As \(q\nmid4a\), (2) implies \(q\mid AC\). Moreover \(\gcd(A,C)\mid p+1\). To see this, if \(d\mid A,C\), then \(p^a\equiv1\pmod d\) and \(p^{a+1}\equiv-1\pmod d\), hence \(p\equiv-1\pmod d\). (We used \(d\mid A\Rightarrow d\mid p^a-1\).) If the prime \(q\) divided both \(A\) and \(C\), it would divide \(p+1\); because \(q>p\), this would require \(q=p+1\), hence \((p,q)=(2,3)\), contrary to \(q>4a\). Thus \(q\) divides exactly one of \(A,C\).

If \(q\mid A\), then (2) implies \(AC/q\mid4a\), impossible because \(C=p^{a+1}+1>4a\). Therefore \(q\mid C\) and
\[
A(C/q)\mid4a,\qquad A\mid4a.
\tag{3}
\]
In particular \(2^a-1\le A\le4a\), forcing \(a\le4\).

For \(a=1\), \(A=1\) and \(C=p^2+1=tq\) with \(t\mid4\). If \(t=1\), primality forces \((p,q)=(2,5)\), but \(q+1=6\nmid4p^2=16\). If \(t=4\), no prime \(p\) has \(4\mid p^2+1\). If \(t=2\), then \(p\) is odd and
\[
q=(p^2+1)/2,\qquad (p^2+3)/2=q+1\mid4p^2.
\]
For \(p\ne3\), \(q+1\) is coprime to \(p\), so it must divide \(4\), impossible since \(p\ge5\). Thus \(p=3,q=5\).

For \(a=2\), condition \(A=p+1\mid8\) gives \(p=3\) or \(7\). The corresponding \(C\) are \(28\) and \(344\). The first has no prime factor \(q>8\); the second has only \(q=43>8\), for which \(A(C/q)=8\cdot8=64\nmid8\).

For \(a=3\), \(A=p^2+p+1\le12\) forces \(p=2\); then \(A=7,C=17\), and the only \(q>12\) is \(17\), but \(A(C/q)=7\nmid12\).

For \(a=4\), \(A=1+p+p^2+p^3\le16\) forces \(p=2\); then \(C=33\) has no prime factor \(q>16\).

These cases establish that \((p,a,q)=(3,1,5)\) is the sole candidate. Directly,
\[
\sigma^{**}(45)=10\cdot6=60,\qquad45d^{**}(45)=45\cdot4=180,
\]
so \(60\mid180\). The candidate is valid, completing the proof.

## Verification and limitations
The inequalities and divisibilities reduce the infinite family to the finite branches above; finite tests alone are not used to infer the unbounded classification. The accompanying `verify.py` independently implements the bi-unitary prime-power formula, replays those bounded branches, and corroborates the final candidate. In particular, the exceptional pair \((q,p)=(2,3)\) is excluded quantitatively rather than by the incorrect assertion that consecutive primes cannot occur.

The classification says nothing about \(p^{2a}q^b\) with \(b>1\), or about every possible two-prime bi-unitary harmonic pattern. It extends the previously established isolated \(p^2q=45\) slice in a natural exponent family. Originality remains a best-of-knowledge assessment: a different presentation of the entire even-exponent family in older number-theory literature cannot be categorically excluded.

## Prior work and references
J. Sándor, *On bi-unitary harmonic numbers*, arXiv:1105.0294 (2011), establishes the multiplicative divisor formulas and records the isolated \(p^2q=45\) result, as well as nearby low-support nonexistence statements. A. Manea and N. Minculete, *Types of integer harmonic numbers (II)*, Bulletin of the Transilvania University of Braşov 9(58) (2016), 67–82, treat other structured exponent families. OEIS A286325 is a corroborative table, not an infinite-family proof.
