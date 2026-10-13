# Primitive arithmetic progressions inside every Wang–Zelinsky construction row

## Finding
A positive integer \(n\) is strongly pseudoperfect if some subset \(S\) of its positive divisors is closed under \(d\mapsto n/d\) and has sum \(2n\). Following Wang and Zelinsky, call such an integer primitive if it is not \(m^k\) for any strongly pseudoperfect \(m\) and integer \(k\ge2\).

For every \(b,t\ge1\), define
\[
a=b+t(b+1),\qquad q=2^{b+1}-1,\qquad p=2^{a+1}-(2^b+1),
\]
and
\[
N_{b,t}=2^a p q.
\]
Then \(N_{b,t}\) is primitive strongly pseudoperfect. For each fixed \(b\), writing
\[
P_b(X)=\#\{t\ge1:N_{b,t}\le X\},
\]
one has
\[
P_b(X)=\frac{\log X}{2(b+1)\log 2}+O_b(1).
\]

For \(b=1\) the progression restriction is unnecessary: every integer \(a\ge2\) gives a primitive strongly pseudoperfect number
\[
3\cdot2^a(2^{a+1}-3).
\]

## Assumptions and scope
All variables are integers in the displayed ranges. No primality assumption is made on \(p\) or \(q\). The word primitive is used only in the perfect-power sense introduced in the cited 2026 paper; it does not mean squarefree, minimal under divisibility, or primitive pseudoperfect in another convention.

The construction lies inside the two-parameter family of Wang and Zelinsky's Theorem 9. The new point is that every fixed \(b\)-row contains an explicit arithmetic progression of exponents on which the members are automatically primitive, together with its logarithmic counting law.

## Proof
First, \(a+1=(t+1)(b+1)\). Hence, modulo \(q=2^{b+1}-1\),
\[
2^{a+1}\equiv1,
\]
so
\[
p=2^{a+1}-(2^b+1)\equiv-2^b\pmod q.
\]
Because \(q\) is odd, this gives \(\gcd(p,q)=1\). Both \(p\) and \(q\) are odd and exceed \(1\).

Consider the \(4(a+1)\) distinct divisors
\[
\mathcal F=\{2^i p^\varepsilon q^\delta:0\le i\le a,\ \varepsilon,\delta\in\{0,1\}\}.
\]
The coprimality just proved makes the displayed elements distinct, and \(d\mapsto N_{b,t}/d\) preserves \(\mathcal F\). Remove the two complementary pairs
\[
\left\{2^b,\frac{N_{b,t}}{2^b}\right\},
\qquad
\left\{q2^b,\frac{N_{b,t}}{q2^b}\right\}.
\]
Let the remaining set be \(S\). It is complement-closed. Since
\[
\sum_{d\in\mathcal F}d=(2^{a+1}-1)(p+1)(q+1),
\]
a direct substitution of \(p=2^{a+1}-(2^b+1)\) and \(q=2^{b+1}-1\) gives
\[
(2^{a+1}-1)(p+1)(q+1)
-2^b-\frac{N_{b,t}}{2^b}
-q2^b-\frac{N_{b,t}}{q2^b}
=2N_{b,t}.
\]
Thus \(\sum_{d\in S}d=2N_{b,t}\), proving strong pseudoperfectness.

It remains to prove primitivity. Put \(m=b+1\ge2\), so \(q=2^m-1\). This Mersenne number is never a nontrivial perfect power. Indeed, if \(q=z^r\) for a prime \(r\), then \(z\) is odd. For \(r=2\), the case \(m=2\) is immediate, while for \(m\ge3\) the congruence \(z^2\equiv1\pmod 8\) makes \(z^2+1=2^m\) impossible. For odd \(r\),
\[
z^r+1=(z+1)(z^{r-1}-z^{r-2}+\cdots-z+1),
\]
and the second factor is an odd integer greater than \(1\), so the product cannot be a power of \(2\).

Because \(\gcd(p,q)=1\), every prime dividing \(q\) occurs in \(N_{b,t}\) with exactly its exponent in \(q\). If \(N_{b,t}=M^k\) with \(k\ge2\), all those exponents would be divisible by \(k\), making \(q\) a \(k\)-th power, contradiction. Hence \(N_{b,t}\) is not any nontrivial perfect power and is therefore primitive strongly pseudoperfect.

For fixed \(b\),
\[
N_{b,t}=2q\,4^a\left(1-\frac{2^b+1}{2^{a+1}}\right),
\qquad a=b+t(b+1).
\]
The last factor stays between two positive constants depending only on \(b\), and the sequence is strictly increasing in \(t\). Therefore
\[
\log N_{b,t}=2(b+1)t\log2+O_b(1),
\]
which yields the asserted formula for \(P_b(X)\).

Finally take \(b=1\). For every \(a\ge2\), \(q=3\) and \(p=2^{a+1}-3\) is coprime to \(3\). The same divisor-set identity proves strong pseudoperfectness, while \(3\) occurs to the first power, so the resulting integer cannot be a nontrivial perfect power. This proves the strengthened \(b=1\) statement.

## Verification
The bundled `verify_primitive_rows.py` reconstructs the divisor set for \(1\le b,t\le9\), verifies distinctness of the \(4(a+1)\) box divisors, complement closure, and the exact sum \(2N_{b,t}\). It also checks the strengthened \(b=1\) row for every \(2\le a\le39\).

A successful replay prints a line beginning `VERIFY_OK`. The finite replay is only a normalization and arithmetic regression check. The all-parameter claim is proved by the algebraic identity, the Mersenne perfect-power lemma, and the asymptotic estimate above.

## Relationship to prior work
Wang and Zelinsky's Theorem 9 proves strong pseudoperfectness for the broader parameter family with \(a>b\ge1\), \(q=2^{b+1}-1\), and \(p=2^{a+1}-(2^b+1)\), and records a four-omitted-divisor representation when \(p\) and \(q\) are prime. Later in the same paper they introduce the perfect-power notion of primitive strongly pseudoperfect numbers and pose questions about primitive examples. The inspected theorem does not connect those two parts by proving primitivity on fixed parameter rows or giving the counting law above.

A closely related public result proves that every \(60\cdot2^n\) is strongly pseudoperfect. Since these numbers have prime valuations equal to \(1\) at \(3\) and \(5\), that family already supplies infinitely many primitive strongly pseudoperfect numbers. Thus the present result does not claim the first infinitude theorem. Its content is the row-by-row primitive subfamily inside the Wang–Zelinsky two-parameter construction and its exact logarithmic scale.

Another nearby result classifies strongly pseudoperfect integers with \(\Omega(n)\le3\); it concerns small prime-factor multiplicity rather than perfect-power primitivity or the present parameter family. OEIS A334405 records strongly pseudoperfect numbers but does not encode the row-by-row primitive theorem or counting law.

## Limitations
The theorem does not settle whether there are infinitely many odd primitive strongly pseudoperfect numbers, classify all primitive strongly pseudoperfect numbers, or claim that the displayed exponent progression is maximal for any \(b\). The counting formula is for the explicit subfamily only.

Literature searches and database comparisons can miss unindexed work. The originality claim is therefore limited to the inspected primary paper, the cited database, the two closest public results, and targeted searches described in the review materials.

## References
1. Audrey Wang and Joshua Zelinsky, “Strongly Pseudoperfect Numbers,” arXiv:2609.36068v1, first posted 28 September 2026; primary MSC \(11A25\).
2. OEIS A334405, strongly pseudoperfect numbers.
3. “All dyadic multiples \(60\cdot2^n\) are strongly pseudoperfect,” published-finding corpus, 4 October 2026.
4. “Strongly pseudoperfect integers with \(\Omega(n)\le3\),” published-finding corpus, 4 October 2026.
