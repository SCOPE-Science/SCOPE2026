# Exact weight-three enumeration of binary palindromic periodicities

## Finding

Let \(Q(n)\) be the number of **linear, position-indexed** binary words of length \(n\) with exactly three occurrences of \(1\) that are *palindromic periodicities*. For every \(n\ge 3\),

\[
\boxed{\sum_{n\ge3}Q(n)z^n=\frac{z^3(1+3z+5z^2+z^4-z^5-z^6)}{(1-z)^4(1+z)^2(1+z^2)(1+z+z^2)}.}
\]

In particular, the enumerator is an exact degree-three quasipolynomial of period dividing \(12\):

\[
Q(n)=\frac{n^3}{18}+\frac{5n^2}{24}-
\begin{cases}\frac{5n}{6},&n\text{ even},\\\frac{7n}{12},&n\text{ odd}\end{cases}
+c_{n\bmod12},
\]

where the twelve constants \(c_0,c_1,\ldots,c_{11}\), in order, are

\[
0,\ \frac{23}{72},\ \frac7{18},\ -\frac58,\ \frac49,\ \frac{55}{72},\ -\frac12,\ -\frac{13}{72},\ \frac89,\ -\frac18,\ -\frac1{18},\ \frac{19}{72}.
\]

Consequently, among binary length-\(n\) words with three ones, the fraction that are palindromic periodicities tends to exactly \(1/3\):

\[
\boxed{\lim_{n\to\infty}\frac{Q(n)}{\binom n3}=\frac13.}
\]

The initial exact counts for \(n=3,4,\ldots,17\) are
\(1,4,10,14,25,36,52,68,93,116,150,182,225,268,324\).

## Assumptions and scope

A nonempty finite word \(w\) of length \(n\) is a *palindromic periodicity* precisely if there is a positive integer \(d\le n\) and a length-\(d\) word \(r\) that is the concatenation of two possibly empty palindromes, such that \(w\) is the length-\(n\) prefix of \(r^{\omega}\). This is the word-period definition of Fici, Shallit, and Simpson. A word which is a product of two palindromes is called *symmetric*. Equivalently, its reversal is a cyclic rotation of it. The alphabet is the labeled set \(\{0,1\}\); occurrences at different positions and different linear words are distinguished, and no quotient by rotations or reflections is taken.

The weight-three layer is the **first nontrivial Hamming-weight layer**: every binary word with zero, one, or two ones is symmetric (a one- or two-mark circular configuration always has a reflection), hence is a palindromic periodicity. By exchanging the two letters the same holds for words with at most two zeros.

For a weight-three word write its one-positions (zero-based) as \(x<y<z\), and put

\[
u=y-x,\qquad v=z-y,\qquad h=n-z+x.
\]

Then \(u,v,h\) are positive, \(u+v+h=n\), and \(0\le x<h\). Conversely, every such tuple \((u,v,h,x)\) specifies one word. We use \(a_+=\max\{0,a\}\).

## Proof

**1. Reflection and root classification.** A circular word with exactly three marked positions is symmetric exactly when **two of its three circular gaps coincide**. Indeed, a reflection preserving three marks fixes one and exchanges two; the two adjacent arcs at the fixed mark are equal. Conversely, equal adjacent arcs give a reflection. A circular word with one or two marks is always symmetric.

If \(u=v\), \(u=h\), or \(v=h\), the entire word is symmetric, hence all \(h\) permissible offsets \(x\) qualify. Suppose henceforth \(u,v,h\) are pairwise distinct, so the entire word is not symmetric. A proper symmetric word-period has length \(d<n\); let \(t=n-d\), and let \(r=w[0..d-1]\). Its number of ones is one, two, or three.

If \(r\) has **one** one, all three one-positions of \(w\) lie in one congruence class modulo \(d\). In increasing order they differ by exactly \(d\), forcing \(u=v\), a contradiction.

If \(r\) has **three** ones, no one may repeat within the observed prefix. This is equivalent to \(1\le t\le\min\{x,h-1-x\}\). The circular gaps of \(r\) are \(u,v,h-t\). Thus \(r\) is symmetric precisely when \(h-t\in\{u,v\}\), because \(u\ne v\). For each such gap \(g<h\), the allowed offsets form the interval

\[
I_g=\{x:h-g\le x\le g-1\}.
\]

If \(r\) has **two** ones, they must be the first two observed marks: the third repeats the first. Otherwise the earlier first mark would also have to repeat before the end, producing a fourth one. Consequently \(d=z-x=u+v\) and \(t=h\). The necessary and sufficient conditions are that the second mark lies in the root and does not repeat, namely \(x<v\) and \(x+u\ge h\). Hence this case contributes offsets

\[
I_0=\{x:\max(0,h-u)\le x\le\min(h-1,v-1)\}.
\]

The root is symmetric because it has two ones. These cases exhaust all symmetric word-periods.

**2. Gap criterion.** Let \(m=\min\{u,v\}\) and \(M=\max\{u,v\}\). If \(h<m\), interval \(I_0\) is all \(\{0,\ldots,h-1\}\). If \(m<h<M\), interval \(I_0\) has exactly \(m\) offsets and contains every applicable \(I_g\). If \(h>M\), interval \(I_M=[h-M,M-1]\) contains \(I_0\) whenever nonempty and contributes \((2M-h)_+\) offsets. Thus the **exact gap-count lemma** is

\[
C(u,v,h)=
\begin{cases}
h,&\text{if two of }u,v,h\text{ coincide},\\
h,&h<\min(u,v),\\
\min(u,v),&\min(u,v)<h<\max(u,v),\\
(2\max(u,v)-h)_+,&h>\max(u,v).
\end{cases}
\]

It counts offsets \(x\), not merely ordered gap triples. Therefore \(Q(n)=\sum_{u,v,h\ge1\,;\,u+v+h=n}C(u,v,h)\), with no symmetry quotient.

**3. Generating function.** Split positive gap triples into those with coincident gaps and those with all gaps distinct. The \(u=v\) contribution and the \(h=u\) or \(h=v\) contribution (excluding all-equal triples to avoid overcounting) are respectively

\[
E_1(z)=\frac{z^3}{(1-z^2)(1-z)^2},\qquad
E_2(z)=2\left[\frac{z^3}{(1-z)(1-z^2)^2}-\frac{z^3}{(1-z^3)^2}\right].
\]

For all-distinct gaps, write their sorted values as \(a<b<c\). The six permutations \((u,v,h)\) have total contribution \(4a+2(2b-c)_+\). Set \(a=A\), \(b=A+B\), and \(c=A+B+C\), with \(A,B,C\ge1\). Their total length is \(3A+2B+C\). The \(4a\) part is

\[
D_1(z)=\frac{4z^6}{(1-z^3)^2(1-z^2)(1-z)}.
\]

For the remaining positive-part contribution, define

\[
\begin{aligned}
P(z)&=\frac{z^5}{(1-z^3)(1-z^2)},\\
T(z)&=z^5\left[\frac1{(1-z^3)^2(1-z^2)}+\frac1{(1-z^3)(1-z^2)^2}\right],\\
Z(z)&=\frac{z^7}{(1-z^4)(1-z^3)}.
\end{aligned}
\]

The finite geometric identity

\[
\sum_{C=1}^{A+B-1}(A+B-C)z^C
=\frac{z\big[(A+B-1)-(A+B)z+z^{A+B}\big]}{(1-z)^2}
\]

now gives

\[
D_2(z)=\frac{2z}{(1-z)^2}\big((1-z)T(z)-P(z)+Z(z)\big).
\]

Summing \(E_1+E_2+D_1+D_2\), and multiplying out the denominators, yields the boxed rational generating function. This is an identity of formal power series (no analytic convergence assumption is used).

**4. Quasipolynomial and density.** Exact partial fractions are

\[
\begin{aligned}
G(z)={}&-\frac{4(z+1)}{9(z^2+z+1)}+\frac{z+1}{4(z^2+1)}
+\frac3{16(z+1)}-\frac1{8(z+1)^2}\\
&+\frac{143}{144(1-z)}-\frac{17}{18(1-z)^2}
-\frac1{4(1-z)^3}+\frac1{3(1-z)^4}.
\end{aligned}
\]

Coefficient extraction using \([z^n](1-z)^{-k}=\binom{n+k-1}{k-1}\) gives the displayed quasipolynomial and the twelve constants. The unique pole of order four is at \(z=1\), with coefficient \(1/3\), so \(Q(n)=n^3/18+O(n^2)\). Since \(\binom n3=n^3/6+O(n^2)\), the fraction tends to \(1/3\).

## Verification

The standalone file `verify.py` independently checks the definition by examining every possible period and every possible split of its root into two palindromes, rather than assuming the gap formula. It compares this predicate with the gap lemma for all \(7{,}315\) weight-three words at lengths \(3\) through \(21\), checks direct aggregate counts independently, and compares the gap sum with a separately computed rational-function coefficient recurrence at every length \(3\) through \(160\). The script uses only the Python standard library and prints `VERIFY_OK` on success. Further exact symbolic partial fraction and residue checks were performed in rational arithmetic.

These finite checks support the derivation; the all-length result follows from the proof, not from extrapolating the computations.

## Relationship to prior work

Simpson introduced palindromic periodicities in *Palindromic Periodicities* (public preprint 2024-02-08). Fici, Shallit, and Simpson, *Some Remarks on Palindromic Periodicities* (public preprint 2024-07-15; published as *On Palindromic Periodicities* in 2025), establish the symmetric-period characterization and study factors of particular infinite words, classes such as trapezoidal words, and unrestricted counting. Their published conclusion explicitly asks for the asymptotic number of **all** binary palindromic periodicities of a given length, recorded in OEIS A374495. The present result is instead a complete exact solution of the natural **fixed Hamming-weight-three slice**; it does not answer the unrestricted question.

The earlier theorem that every trapezoidal binary word is a palindromic periodicity does not settle this problem: the weight-three palindromic periodicity `01100100` contains all four binary length-two factors and hence is not trapezoidal. General enumeration of products of two palindromes also does not cover all palindromic periodicities: `01100100` is a palindromic periodicity with symmetric proper word-period `0110010`, but its own cyclic gaps \((1,3,4)\) are distinct, so it is not symmetric.

## Limitations

The theorem counts **linear** binary words of **exactly three ones**. It does not count cyclic necklace classes, words with four or more ones, or the unrestricted binary palindromic-periodicity language. The searched and inspected papers do not show the displayed fixed-weight generating function or the asymptotic density, but unindexed equivalent enumerations cannot be excluded from literature searches alone. The direct full-length asymptotic counting problem remains open in the cited literature.

## References

1. J. Simpson, *Palindromic Periodicities*, arXiv:2402.05381, first posted 2024-02-08. https://arxiv.org/abs/2402.05381
2. G. Fici, J. Shallit, J. Simpson, *Some Remarks on Palindromic Periodicities*, arXiv:2407.10564, first posted 2024-07-15. https://arxiv.org/abs/2407.10564
3. G. Fici, J. Shallit, J. Simpson, *On Palindromic Periodicities*, CPM 2025, LIPIcs 331, 11:1–11:14, doi:10.4230/LIPIcs.CPM.2025.11. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2025.11
4. OEIS A374495, counts of binary palindromic periodicities without a Hamming-weight restriction. https://oeis.org/A374495
5. C. Guo, J. Shallit, A. M. Shur, *On the Combinatorics of Palindromes and Antipalindromes*, arXiv:1503.09112, 2015. https://arxiv.org/abs/1503.09112
