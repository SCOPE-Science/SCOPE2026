# Primitive Achilles progressions: an infinite family and a sharp first occurrence

## Finding

An **Achilles number** is a positive integer all of whose prime exponents are at least two, but which is not a perfect power. A three-term arithmetic progression is **primitive** if its three terms have greatest common divisor one. There exist **infinitely many increasing primitive three-term arithmetic progressions consisting entirely of Achilles numbers**; in fact, the exhibited progressions are pairwise coprime.

Among all primitive increasing three-term arithmetic progressions of Achilles numbers, the smallest possible largest term is exactly \(57967\). The unique progression with largest term at most \(57967\) is
\[
(14283,36125,57967)=(3^3\cdot23^2,\,5^3\cdot17^2,\,7^3\cdot13^2).
\]

Here is an explicit infinite parametrization. For an integer \(t\), define
\[
\begin{aligned}
X(t)&=-5750t^2+8500t-621,\\
Y(t)&=4250t^2-1242t+459,\\
Z(t)&=-3250t^2+351.
\end{aligned}
\]
Let \(t\) run through the infinite congruence class
\[
t\equiv8482369351\pmod{34462998570},\qquad t\ge8482369351.
\]
Then
\[
\bigl(27X(t)^2,\,125Y(t)^2,\,343Z(t)^2\bigr)
\]
is an increasing, pairwise-coprime three-term arithmetic progression of Achilles numbers; distinct such \(t\) produce distinct progressions.

## Assumptions and scope

All indices and terms are ordinary positive integers; the parametrization above uses the indicated integer congruence class and nonnegative multiples of its modulus. A number with factorization \(\prod_i p_i^{e_i}\) is Achilles exactly when \(\min_i e_i\ge2\) and \(\gcd_i e_i=1\). A three-term arithmetic progression \(a<b<c\) has \(a+c=2b\); primitiveness means \(\gcd(a,b,c)=1\). Pairwise coprimality is stronger and is established for the constructed family. No upper bound on the common difference, relative to its first term, is asserted.

## Proof

**1. Exact polynomial identity and growth.** Direct expansion gives
\[
27X(t)^2+343Z(t)^2=250Y(t)^2.
\]
Thus the displayed three terms form an arithmetic progression with common difference
\[
\begin{aligned}
\Delta(t)&=125Y(t)^2-27X(t)^2\\
&=1365125000t^4+1319625000t^3-1463062500t^2\\
&\quad+142519500t+15922818.
\end{aligned}
\]
For every integer \(t\ge2\), the first and third summands together equal
\(t^2(1365125000t^2-1463062500)>0\), while the other displayed summands are positive. Hence the progression is strictly increasing and has positive terms for all such \(t\).

**2. The resultant forces coprimality.** The degree-two Sylvester determinant of \(X\) and \(Y\), calculated from their integer coefficients, is
\[
\operatorname{Res}(X,Y)=90724673403000
=2^3\cdot3^3\cdot5^3\cdot7^6\cdot13^4.
\]
For any prime \(p\) dividing both \(X(t)\) and \(Y(t)\), specialization of the Sylvester Bézout identities forces \(p\mid\operatorname{Res}(X,Y)\). Consequently, if \(p\mid\gcd(27X(t)^2,125Y(t)^2)\), then \(p\in\{2,3,5,7,13\}\). In the cases \(p=3\) and \(p=5\), the fixed cube factors are included in this set; no other primes arise.

At \(t=1\), the three polynomial values are
\[
(X(1),Y(1),Z(1))=(2129,3467,-2899),
\]
and \(\gcd(27\cdot2129^2,125\cdot3467^2)=1\). Whenever \(t\equiv1\pmod{2730}\), the two respective terms have the same residues at every prime \(2,3,5,7,13\) as when \(t=1\). Hence their gcd is one. Both are odd for every integer \(t\). Writing the three terms as \(A,B,C\) with \(A+C=2B\), we have \(\gcd(A,C)=\gcd(A,2B)=1\) and \(\gcd(B,C)=\gcd(B,A)=1\). Thus all three terms are pairwise coprime.

**3. Exact prime-exponent witnesses.** Impose, additionally,
\[
t\equiv5\pmod{11^2},\qquad
 t\equiv0\pmod{17^2},\qquad
 t\equiv3\pmod{19^2}.
\]
The moduli \(2730,121,289,361\) are pairwise coprime. The Chinese remainder theorem gives precisely
\[
t\equiv8482369351\pmod{34462998570}.
\]
Since \(X(5)\equiv11\pmod{121}\), \(Y(0)\equiv170\pmod{289}\), and \(Z(3)\equiv342\pmod{361}\), we have for every such \(t\)
\[
\nu_{11}(X(t))=\nu_{17}(Y(t))=\nu_{19}(Z(t))=1.
\]
The condition \(t\equiv1\pmod{2730}\) also gives \(3\nmid X(t)\), \(5\nmid Y(t)\), and \(7\nmid Z(t)\). Therefore the first term has prime exponents \(3\) at \(3\) and \(2\) at \(11\), the second has exponents \(3\) at \(5\) and \(2\) at \(17\), and the third has exponents \(3\) at \(7\) and \(2\) at \(19\). Every other prime exponent, if present, is even and at least two. Each term is consequently powerful but not a perfect power, since its exponent gcd divides \(\gcd(3,2)=1\). As \(t\) grows along the congruence class, the first term is asymptotic to \(27\cdot5750^2t^4\), so the resulting progressions are distinct and infinite in number.

**4. Sharp first occurrence.** The progression
\[
14283+57967=2\cdot36125
\]
is primitive, and each term has prime-exponent multiset \(\{2,3\}\), so it provides the stated upper bound. To prove minimality, the standalone exact-integer verifier enumerates **every** positive integer \(n\le57967\), factors it using a smallest-prime-factor sieve, and selects it if and only if all exponents are at least two and their gcd is one. There are exactly \(186\) such integers. For every ordered pair \(a<b\) of these integers, the only possible third AP term is \(c=2b-a\); the verifier tests every pair for \(c\le57967\), membership, and \(\gcd(a,b)=1\). Its complete search returns precisely \((14283,36125,57967)\). Because every eligible progression must appear in this exhaustive pair search, no primitive Achilles progression has a smaller largest term. This enumeration is a complete finite proof for the sharp cutoff, not a substitute for the symbolic infinite-family proof.

## Verification

Run `python3 verify.py` using Python 3 standard library. It reconstructs the degree-four polynomial identity and difference, evaluates the integer Sylvester determinant by a 24-term permutation sum, checks its exact prime factorization, and verifies CRT residues and seven separated large parameter values. It independently enumerates the \(186\) Achilles numbers at or below \(57967\), cross-checks them against the square-cube representation of powerful numbers, and exhausts all primitive three-term progressions below the bound. The expected terminal output begins `VERIFY_OK` and records `primitive_triples=[(14283, 36125, 57967)]`.

## Relationship to prior work

Chan's 2022 preprint gives infinite progressions of powerful numbers with controlled gaps, but its proof of the three-term construction uses **two perfect-square entries**, so it does not establish three Achilles entries. Bajpai, Bennett and Chan (2023), Theorem 1.2 and Section 5.1, give infinitely many primitive powerful progressions via **three perfect squares**; their Section 5.2 concerns cubefull rather than Achilles entries. Van Doorn (2026) again constructs three-term progressions with **two squares**. These are stronger in other directions (short gaps, longer progressions, or higher-powerful conditions), but their explicit constructions and stated theorems do not imply that *every* term is powerful without being a perfect power while the progression is primitive. OEIS A390953 lists the individual odd Achilles numbers \(14283\), \(36125\) and \(57967\), but not the arithmetic-progression theorem or its minimality. The fixed-prime-support asymptotic and strong-Achilles classifications in other indexed mathematical records concern counts and multiplicative structure rather than primitive three-term progressions. No exhaustive novelty guarantee is made from the absence of a match.

## Limitations

The existence family is a specific quartic parametrization within one large residue class; it is not a classification of all primitive Achilles progressions, does not settle four-term Achilles progressions, and gives no optimal common-difference asymptotics. The least-value statement applies to **primitive** three-term progressions only, with the *largest* member minimized; nonprimitive progressions are outside that extremum. The exhaustive part is verified only through the mathematically sufficient cutoff \(57967\), while infinitude is proved symbolically. Prior art not located by the inspected searches remains a bibliographic risk.

## References

1. Tsz Ho Chan, *Arithmetic progressions among powerful numbers*, arXiv:2210.00281v1, publicly posted 1 October 2022; https://arxiv.org/abs/2210.00281 .
2. Prajeet Bajpai, Michael A. Bennett and Tsz Ho Chan, *Arithmetic progressions in squarefull numbers*, arXiv:2302.03113v1, publicly posted 6 February 2023; https://arxiv.org/abs/2302.03113 . Relevant: Theorem 1.2, Sections 5.1–5.3.
3. Wouter van Doorn, *Three-term arithmetic progressions of consecutive powerful numbers*, arXiv:2605.06697v1, publicly posted 4 May 2026; https://arxiv.org/abs/2605.06697 . Relevant: Theorem 1 and Section 3.
4. OEIS A390953, *Odd Achilles numbers*; https://oeis.org/A390953 . Relevant: the listing of the three seed terms.
