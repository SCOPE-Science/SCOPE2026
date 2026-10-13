# The weight-three binary 3-deck generating function
## Finding
Let \(D_{3,3}(n)\) denote the number of distinct length-\(3\) subsequence decks among binary words of length \(n\) and Hamming weight \(3\). Then, for every \(n\ge 0\),
\[
\sum_{n\ge0}D_{3,3}(n)z^n
=
\frac{z^3}{(1-z)^4}
-
\frac{z^7}{(1-z)^2(1-z^2)(1-z^4)}.
\]
This proves the generating-function formula posed as Conjecture 1 by Chrisnata, Kiah, Karingula, Vardy, Yaakobi, and Yao.

## Assumptions and scope
A length-\(3\) deck records, with multiplicity, every binary subsequence of length \(3\). A weight-\(3\) word is written uniquely as
\[
W(a,b,c,d)=\mathtt0^a\mathtt1\mathtt0^b\mathtt1\mathtt0^c\mathtt1\mathtt0^d,
\qquad a,b,c,d\in\mathbb Z_{\ge0}.
\]
Thus \(a+b+c+d=n-3\). The statement counts deck-equivalence classes only inside this fixed-weight slice; it makes no claim about the total number \(D_3(n)\) of all binary \(3\)-decks.

## Proof
For \(u=(a,b,c,d)\), write \(N_p(u)\) for the multiplicity of the length-\(3\) pattern \(p\) in the deck of \(W(u)\). Directly counting the location of the zero relative to the three ones gives
\[
N_{011}=3a+b,\qquad N_{101}=2b+2c,\qquad N_{110}=c+3d.
\]
Therefore, if two gap vectors \(u\) and \(u'\) have the same three coordinates above, their difference lies in the one-dimensional kernel of
\[
\begin{pmatrix}3&1&0&0\\0&2&2&0\\0&0&1&3\end{pmatrix},
\]
so for some integer \(t\),
\[
u'=(a+t,b-3t,c+3t,d-t).
\]

The remaining nonconstant coordinates with exactly one one are
\[
\begin{aligned}
N_{001}(u)&=\binom a2+\binom{a+b}2+\binom{a+b+c}2,\\
N_{010}(u)&=a(b+c+d)+(a+b)(c+d)+(a+b+c)d,\\
N_{100}(u)&=\binom{b+c+d}2+\binom{c+d}2+\binom d2.
\end{aligned}
\]
Substitution of \(u'\) and cancellation give the exact differences
\[
\begin{aligned}
N_{001}(u')-N_{001}(u)&=t(c-b+3t),\\
N_{010}(u')-N_{010}(u)&=-2t(c-b+3t),\\
N_{100}(u')-N_{100}(u)&=t(c-b+3t).
\end{aligned}
\]
The coordinates \(N_{000}=\binom{n-3}{3}\) and \(N_{111}=1\) depend only on \(n\). Hence two distinct weight-\(3\) words have the same \(3\)-deck exactly when
\[
t\ne0\qquad\text{and}\qquad b-c=3t.
\]

Orient every nontrivial pair so that \(t>0\). Writing \(b=c+3t\) and \(d=t+e\), every two-element deck class is represented uniquely by
\[
(a,c+3t,c,t+e)
\quad\longleftrightarrow\quad
(a+t,c,c+3t,e),
\]
where \(a,c,e\ge0\) and \(t\ge1\). A given gap vector has at most one nontrivial partner because \(t=(b-c)/3\) is forced, so no deck class in this slice has more than two words.

The length relation for an oriented pair is
\[
n=a+e+2c+4t+3.
\]
Consequently the generating function for the number of two-word classes is
\[
\sum_{a,e,c\ge0}\sum_{t\ge1}z^{a+e+2c+4t+3}
=
\frac{z^7}{(1-z)^2(1-z^2)(1-z^4)}.
\]
There are \(\binom n3\) weight-\(3\) binary words, with generating function
\[
\sum_{n\ge0}\binom n3z^n=\frac{z^3}{(1-z)^4}.
\]
Each two-word class lowers the number of distinct decks by exactly one, and all other classes are singletons. Subtracting the two generating functions proves the formula.

## Verification
The bundled `verify.py` reconstructs the eight deck coordinates from the gap formulas and independently recomputes them by direct enumeration of all length-\(3\) subsequences for every weight-\(3\) word through length \(12\). It then exhaustively groups every weight-\(3\) word through length \(35\) by its exact deck, checks that every class has size at most \(2\), and checks that every two-word class is exactly of the parameterized form above.

The verifier also enumerates every oriented collision parameter tuple through length \(50\) and compares the resulting counts with the coefficients of
\[
\frac{z^7}{(1-z)^2(1-z^2)(1-z^4)}.
\]
All arithmetic is integer and exhaustive within the stated finite ranges. These computations are checks of the algebraic proof, not substitutes for its all-\(n\) argument.

## Relationship to prior work
Chrisnata et al. introduced the fixed-weight quantity \(D_{3,3}(n)\), observed the first collision at length \(7\), derived the same one-dimensional kernel direction \((1,-3,3,-1)\), proved \(D_{3,3}(n)=\Theta(n^3)\), and then stated the displayed generating function as Conjecture 1. They reported computational agreement for the first \(20\) coefficients but did not prove the formula.

Lejeune, Rigo, and Rosenfeld study the equivalent language of \(k\)-binomial equivalence. Their full text gives a detailed description for binary \(2\)-binomial classes and explicitly notes that analogous structure for \(k\ge3\) has no clear general answer; it does not classify the fixed-weight-three binary \(3\)-classes used here.

Nilforoushan and Parvaresh subsequently sharpen general asymptotic bounds on the number of distinct \(k\)-decks and prove \(D_{2,3}(n)=\Theta(n^9)\) for unrestricted binary words. That result concerns the total number of binary \(3\)-decks, not the exact fixed-weight quantity \(D_{3,3}(n)\), and does not imply the generating function above.

Targeted searches under the exact notation \(D_{3,3}(n)\), the conjectured rational function, \(3\)-binomial equivalence at binary weight \(3\), the kernel direction \((1,-3,3,-1)\), and the explicit length-\(7\) collision did not locate a later statement proving or implying this formula.

## Limitations
The argument is specific to binary words of Hamming weight \(3\) and decks of subsequence length \(3\). It does not determine \(D_3(n)\), analogous fixed-weight quantities for larger weight or deck length, or reconstruction thresholds.

A residual originality risk remains for an unindexed proof or unpublished note. The literature comparison found no covering result in the direct source, the standard binomial-equivalence treatment, the recent general distinct-deck bound, or targeted exact-formula searches.

## References
1. J. Chrisnata, H. M. Kiah, S. R. Karingula, A. Vardy, E. Yaakobi, and H. Yao, “On the number of distinct \(k\)-decks: Enumeration and bounds,” *Advances in Mathematics of Communications* 17 (2023), 960–978, DOI 10.3934/amc.2021032; early access 2021-08-30.
2. M. Lejeune, M. Rigo, and M. Rosenfeld, “On the binomial equivalence classes of finite words,” *International Journal of Algebra and Computation* 30 (2020), 1375–1397, arXiv:2001.11732, DOI 10.1142/S0218196720500459.
3. A. Nilforoushan and F. Parvaresh, “Improved upper bound on the number of distinct \(k\)-decks for any \(k\) and alphabet size by counting the independent parameters,” arXiv:2609.23106 (2026).
