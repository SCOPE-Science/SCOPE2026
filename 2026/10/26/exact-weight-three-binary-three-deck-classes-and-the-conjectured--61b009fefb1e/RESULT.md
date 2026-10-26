# Exact weight-three binary three-deck classes and the conjectured generating function

## Finding

The conjectured generating function of Chrisnata, Kiah, Karingula, Vardy, Yaakobi, and Yao [1, Conjecture 1] is correct for every word length. More precisely, let \(D_{3,3}(n)\) be the number of distinct length-three scattered-subsequence decks of binary words of length \(n\) containing exactly three ones. Then

\[
\boxed{\sum_{n\geq0}D_{3,3}(n)z^n=\frac{z^3}{(1-z)^4}-\frac{z^7}{(1-z)^2(1-z^2)(1-z^4)}.}
\]

Furthermore, every equivalence class has either one or two words, and all two-word classes are classified explicitly below. For \(n\geq7\), the number of unordered collision pairs is

\[
P_n=\sum_{s\geq1}\sum_{y\geq1}\max\{0,n-2y-4s\},
\qquad D_{3,3}(n)=\binom n3-P_n.
\]

Here \(P_n=0\) when \(n<7\). The first collision, already known in [1] and [3], occurs at length seven between \(\mathtt{1000110}\) and \(\mathtt{0110001}\). The new theorem identifies *every* collision and proves the full conjecture, not merely the first collision or an asymptotic bound.

## Assumptions and scope

The alphabet is \(\{0,1\}\); a word contains exactly three ones. A length-three *scattered* subsequence is specified by any increasing triple of positions; the three-deck records the eight multiplicities of binary triples. Index the word's positions by \(0,\ldots,n-1\). Let \(0\leq a<b<c<n\) be the positions of the three ones. All statements hold for each integer \(n\geq0\), with an empty set of admissible words when \(n<3\). Binomial coefficients \(\binom{v}{k}\) are zero for \(0\leq v<k\).

## Proof

**1. A complete three-coordinate test.** Put \(h=n-3\) and \(z_1=a\), \(z_2=b-1\), \(z_3=c-2\). These are the numbers of zeros preceding the respective occurrences of one. Write \(X_{u}\) for the number of scattered subsequences spelling \(u\). Directly choosing the distinguished zero or one positions gives

\[
X_{011}=2a+b-1,\qquad
X_{110}=3n-b-2c-4,\qquad
X_{001}=\binom a2+\binom{b-1}2+\binom{c-2}2.
\]

For words with the same length and exactly three ones, equality of these three counts is **equivalent** to equality of the complete three-deck. To prove sufficiency, note that \(X_{000}=\binom h3\) and \(X_{111}=1\). Exactly \(3h\) subsequences have two ones and one zero, hence

\[X_{011}+X_{101}+X_{110}=3h.\]

Also \(2a+b\) and \(b+2c\), determined by the displayed counts, determine \(a+b+c\), hence \(\sum_i z_i=a+b+c-3\). In turn, \(X_{001}=\frac12(\sum_i z_i^2-\sum_i z_i)\) determines \(\sum_i z_i^2\). The two remaining one-one-zero-free-pattern counts satisfy

\[
X_{100}=\sum_{i=1}^{3}\binom{h-z_i}{2},\qquad
X_{010}=\sum_{i=1}^{3}z_i(h-z_i),
\]

and so are determined by \(h\), \(\sum_i z_i\), and \(\sum_i z_i^2\). This reconstructs all eight components. Necessity is immediate.

**2. All possible collisions.** Suppose that a second triple \((a',b',c')\) gives the same three-deck. Equality of \(X_{011}\) and \(X_{110}\) forces

\[
(a',b',c')=(a+s,b-2s,c+s)
\]

for some integer \(s\). The change in \(X_{001}\), using \(\binom{v+r}{2}-\binom v2=rv+\binom r2\) in its polynomial sense for integral \(r\), is exactly

\[
X'_{001}-X_{001}=s(a-2b+c)+3s^2=s\bigl(3s-(x-y)\bigr),
\]

where \(x=b-a\geq1\) and \(y=c-b\geq1\). Thus either \(s=0\) (the same word) or

\[
s=\frac{x-y}{3}\in\mathbb Z\setminus\{0\}.
\]

In the nontrivial case the new two successive gaps are \(b'-a'=y\) and \(c'-b'=x\). Consequently every three-deck class has at most two words: starting from any word there is at most one other possible triple. Conversely, whenever the displayed nonzero integer \(s\) produces three positions in \(\{0,\ldots,n-1\}\), step 1 shows that the two words have identical complete three-decks. The operation is an involution, swapping \(x\) and \(y\).

**3. Counting pairs without duplication.** Orient each two-word class by its member with \(x>y\), hence \(s\geq1\). Parameterize \(x=y+3s\), where \(y,s\geq1\), and write \(a\geq0\) for the first position. The two ordered triples of one-positions are

\[
(a,\ a+y+3s,\ a+2y+3s)
\quad\text{and}\quad
(a+s,\ a+y+s,\ a+2y+4s).
\]

They are both increasing and within the word if and only if

\[0\leq a\leq n-1-2y-4s.\]

There are therefore exactly \(\max\{0,n-2y-4s\}\) choices of \(a\), and each unordered pair occurs **once** because exactly one member has \(x>y\). Thus the count of paired classes is \(P_n\) as claimed. There are \(\binom n3\) total weight-three words; merging each pair into one class subtracts precisely \(P_n\), proving \(D_{3,3}(n)=\binom n3-P_n\).

**4. Rational generating function.** For integers \(v\geq0\),

\[
\sum_{n\geq0}\max\{0,n-v\}z^n=\frac{z^{v+1}}{(1-z)^2}
\]

as an identity of formal power series. Substitute \(v=2y+4s\), sum geometric series over \(y,s\geq1\), and obtain

\[
\sum_{n\geq0}P_nz^n
=\frac{z}{(1-z)^2}\cdot\frac{z^2}{1-z^2}\cdot\frac{z^4}{1-z^4}
=\frac{z^7}{(1-z)^2(1-z^2)(1-z^4)}.
\]

Since \(\sum_{n\geq0}\binom n3 z^n=z^3/(1-z)^4\), subtraction gives the displayed identity for all \(n\). This is a formal identity, not an inference from finitely many coefficients. \(\square\)

## Verification

The accompanying standalone `verify.py` computes all eight scattered-triple counts in two independent ways (direct position triples and a subsequence-count recursion). It exhaustively groups **all** weight-three words for lengths \(3\) through \(36\), testing collision multiplicities, the exact partner map, the integer pair formula, and the generating-function coefficients. Independent coefficient comparisons continue through length \(140\). The recorded output from the actual packaged verifier is:

`THREE_DECK_WEIGHT3_PASS lengths=3..36 direct_deck_comparisons=715 enumerated_words=66045 series_coefficients=0..140 all_classes_at_most_two=True first_collision_length=7`

The general proof above, not these finite checks, establishes the identities for arbitrary \(n\).

## Relationship to prior work

Chrisnata et al. [1, Section 5.3] already analyzed the zero-block linear kernel, proved bounds of order \(n^3\), supplied the first colliding pair, and explicitly conjectured the rational generating function stated here [1, Conjecture 1]. None of those statements is claimed as new. The advance is the quadratic equality test, a complete involutive classification of all collision classes, and consequently a proof of the published conjecture for every length.

Lejeune, Rigo, and Rosenfeld [2] studied finite-word binomial equivalence more broadly, principally obtaining general bounds and two-deck results. Nilforoushan and Parvaresh [4] subsequently determined the asymptotic exponent for all binary three-decks without fixing Hamming weight, but did not establish this weight-three exact collision distribution. An identical solution under different terminology in uninspected literature remains a residual originality risk.

## Limitations

This theorem covers **binary words of exactly three ones and scattered subsequences of exactly length three**. It neither counts all unrestricted binary three-decks nor proves analogous exact formulas for larger fixed weights or longer decks. No claim is made that a finite computational census alone proves the infinite theorem. This is a mathematical proof with reproducible finite checks; no independent mathematical audit is claimed.

## References

[1] J. Chrisnata, H. M. Kiah, S. R. Karingula, A. Vardy, E. Yaakobi, and H. Yao, *On the number of distinct k-decks: Enumeration and bounds*, Advances in Mathematics of Communications 17 (2023), 960–978; first online 30 August 2021, https://doi.org/10.3934/amc.2021032 . Author-posted full text: https://www.researchgate.net/publication/354441361_On_the_number_of_distinct_k_-decks_Enumeration_and_bounds . See §5.3 and Conjecture 1.

[2] M. Lejeune, M. Rigo, and M. Rosenfeld, *On the binomial equivalence classes of finite words*, arXiv:2001.11732 (2020), https://arxiv.org/abs/2001.11732 .

[3] B. Manvel, A. Meyerowitz, A. Schwenk, K. Smith, and P. Stockmeyer, *Reconstruction of sequences*, Discrete Mathematics 94 (1991), 209–219, as cited in [1].

[4] A. Nilforoushan and F. Parvaresh, *Improved upper bound on the number of distinct k-decks for any k and alphabet size by counting the independent parameters*, arXiv:2609.23106 (19 September 2026), https://arxiv.org/abs/2609.23106 .
