# Fixed-content enumeration of binary words with a distance-two conjugate

## Finding
For an integer \(n\ge 2\), let \(\sigma\) be one-position cyclic rotation of binary words, let \(|w|_1\) be the number of ones, and define the indexed-word polynomial
\[
H_n(y)=\sum_{\substack{w\in\{0,1\}^n\\ \exists\,1\le j<n:\ d_H(w,\sigma^j w)=2}}y^{|w|_1}.
\]
For \(1\le i\le\lfloor n/2\rfloor\), put \(g_i=\gcd(n,i)\), \(L_i=n/g_i\), and define
\[
F_{n,i}(y)=n(1+y^{L_i})^{g_i-1}\sum_{a=1}^{L_i-1}y^a.
\]
Write \(\mu\) for the number-theoretic Möbius function. Define the polynomial
\[
P_i(x)=-\sum_{\substack{d\mid i\\d>1}}\mu(d)(1+x^d)^{i/d},\qquad P_1(x)=0.
\]
Set
\[
B_{n,i}(y)=
\begin{cases}
\displaystyle \frac ni\left[(y^{L_i-1}-y^{L_i+1})P_i'(y^{L_i})+iyP_i(y^{L_i})\right],&i\mid n,\\[4pt]
\displaystyle n(y+y^{L_i-1})(1+y^{L_i})^{g_i-1},&i\nmid n.
\end{cases}
\]
Then the **exact fixed-weight enumeration**, valid for every integer \(n\ge2\), is
\[
\boxed{H_n(y)=\sum_{i=1}^{\lfloor n/2\rfloor}\bigl(F_{n,i}(y)-B_{n,i}(y)\bigr).}
\]
Every indexed word counted by \(H_n\) is primitive; hence the exact number of its **rotation necklaces** with \(t\) ones is \([y^t]H_n(y)/n\), for each \(0\le t\le n\).

A uniform prime-length phenomenon follows. For every odd prime \(p\),
\[
[y^t]H_p(y)=
\begin{cases}
p,&t=1\text{ or }t=p-1,\\
p(p-1)/2,&2\le t\le p-2,\\
0,&t=0\text{ or }t=p.
\end{cases}
\]
Consequently there are exactly \((p-1)/2\) rotation necklaces at **each** interior weight \(2\le t\le p-2\), despite the substantially varying size \(\binom pt\) of the full constant-weight layer. The indexed words at a specified weight are exactly the rotations of supports that are proper, nonempty arithmetic progressions in \(\mathbb Z/p\mathbb Z\).

## Assumptions and scope
All words are over the labeled binary alphabet \(\{0,1\}\); Hamming distance compares equally aligned indexed positions. The phrase “has a distance-two conjugate” means \(d_H(w,\sigma^j w)=2\) for **some nonzero** cyclic shift \(j\), not distance at most two, nor the minimum over all shifts including zero. In the polynomial, each indexed word is counted once even if several shifts qualify. Rotation necklaces identify cyclic shifts but do not identify bit complementation or reversal. The theorem makes no claims about other alphabet sizes or other target distances.

For example, the coefficient vectors \(([y^t]H_n)_{t=0}^n\) are
\[
\begin{array}{c|l}
n&\text{coefficients in increasing weight}\!\\\hline
7&(0,7,21,21,21,21,7,0)\\
8&(0,8,24,40,16,40,24,8,0)\\
9&(0,9,36,27,45,45,27,36,9,0)\\
12&(0,12,60,96,72,168,48,168,72,96,60,12,0).
\end{array}
\]

## Proof
**1. One-shift enumerator.** Fix \(i\) with \(1\le i\le\lfloor n/2\rfloor\) and write \(g=\gcd(n,i)\), \(L=n/g\). The permutation of positions induced by adding \(i\) has exactly \(g\) cycles, each of length \(L\). For a binary cyclic sequence, the number of transitions between adjacent entries is even. The global Hamming distance is two exactly when one of these position cycles has two transitions, and every other cycle has none. The exceptional cycle must comprise a nonempty cyclic run of \(a\) ones and \(L-a\) zeros, for some \(1\le a<L\). Choosing its position cycle (\(g\) ways), its cyclic run origin (\(L\) ways), and which \(b\) of the other \(g-1\) cycles are all one yields \(n\binom{g-1}{b}\) indexed words of weight \(bL+a\). Their polynomial is precisely \(F_{n,i}\). In particular, no duplicate choices arise within one shift because the exceptional cycle and transition pair are determined by the word.

**2. Intersections and earliest shifts.** It is sufficient to consider shifts \(i\le\lfloor n/2\rfloor\), since the Hamming distances at shifts \(i\) and \(n-i\) agree. The double-shift structure lemma for near-commuting words (Gabrić, Lemma 14) states that, for \(1\le j<i\le n/2\), a word has Hamming distance two under both shifts exactly when it differs in one coordinate from a word of period \(\gcd(n,i,j)\). Its proof analyzes overlaps of the two cyclic periodicity constraints; this lemma is also independently testable by direct enumeration at small lengths.

If \(i\nmid n\), let \(g=\gcd(n,i)<i\). A word already counted by a smaller shift is exactly a one-coordinate change to a period-\(g\) word: one direction follows from the intersection lemma, and the converse follows because shift \(g\) is smaller than \(i\). Here \(L=n/g\ge3\), so the original period-\(g\) word is unique: distinct period-\(g\) words differ in at least \(L\) coordinates and cannot both be at distance one from the same word. Changing a zero to a one, or a one to a zero, in a period-\(g\) word of weight \(bL\) produces exactly \(L(g-b)\) words of weight \(bL+1\) or \(Lb\) words of weight \(bL-1\), respectively. Summing \(\binom gb\) choices gives \(n(y+y^{L-1})(1+y^L)^{g-1}\) after pairing and simplifying coefficients. This is the second branch of \(B_{n,i}\).

If \(i\mid n\), a double-shift word is instead exactly one coordinate different from \(u^{L}\), where \(u\) is a nonprimitive binary word of length \(i\), since a period strictly smaller than \(i\) is equivalent to such a nonprimitive base. The converse uses a proper period of \(u\) as the smaller shift. The weight polynomial of nonprimitive length-\(i\) binary words is
\[
P_i(x)=(1+x)^i-\sum_{d\mid i}\mu(d)(1+x^d)^{i/d}
=-\sum_{\substack{d\mid i\\d>1}}\mu(d)(1+x^d)^{i/d},
\]
by primitive-word Möbius inversion. If \(c_r=[x^r]P_i(x)\), a nonprimitive base of weight \(r\) has \(Lr\) one-to-zero flips and \(L(i-r)\) zero-to-one flips. Thus their weight polynomial is
\[
L\sum_{r=0}^i c_r\left(r y^{Lr-1}+(i-r)y^{Lr+1}\right)
=\frac ni\left[(y^{L-1}-y^{L+1})P_i'(y^L)+iyP_i(y^L)\right].
\]
There is no overcounting of error templates: for \(L\ge3\), distinct repeated bases are separated by at least three positions. At \(L=2\), if two nonprimitive bases gave the same one-error word, those bases would differ in one position. But two nonprimitive equal-length words cannot differ in one position: any period of the first would make the second differ from its corresponding rotation in exactly two positions, contradicting the fact that a power has every nonzero rotational distance either zero or at least four (rotational distance is an integer multiple of its exponent, while positive binary rotational distances are at least two). This proves uniqueness even at the boundary. Thus the first branch of \(B_{n,i}\) is exact.

The set of words whose **smallest** qualifying shift in \(\{1,\ldots,\lfloor n/2\rfloor\}\) is \(i\) therefore has weight polynomial \(F_{n,i}-B_{n,i}\). Summation gives the announced identity without inclusion–exclusion ambiguity.

**3. Primitive necklaces.** Suppose a counted word were a proper power \(w=v^k\), \(k\ge2\). Every rotation conjugate is another \(k\)-fold power and has distance \(k\,d_H(v,\sigma^jv)\) from \(w\), for an appropriate shift of the root. A positive Hamming distance between a word and a rotation cannot equal one (the number of cyclic mismatches in a binary cycle cannot be odd at value one). Therefore a positive distance for the proper power is at least \(2k\ge4\), contrary to the defining distance two. Every counted word is thus primitive, and each rotation necklace has exactly \(n\) indexed members, all of the same weight.

**4. Prime-length specialization.** For odd prime \(p\), every \(i<p\) has \(g=1\) and \(L=p\). At \(i=1\), there are no smaller shifts and \(F_{p,1}=p\sum_{a=1}^{p-1}y^a\). For every \(2\le i\le(p-1)/2\), the nondivisor branch subtracts exactly \(p(y+y^{p-1})\), so the contribution is \(p\sum_{a=2}^{p-2}y^a\). This proves the displayed coefficients. With \(g=1\), the one-shift structure in Step 1 says precisely that the one-positions form a proper nonempty cyclic interval in the progression order with difference \(i\); equivalently, the support is an arithmetic progression modulo \(p\). Each qualifying word is therefore of this form, and the converse follows from its two transitions. The coefficient statement gives the exact number of corresponding necklaces.

## Verification
The accompanying standard-library program `verify.py` computes the symbolic enumerator using binomial coefficients, greatest common divisors and Möbius inversion. It independently enumerates all binary words and checks all rotations for every \(2\le n\le17\), and independently checks every *earliest-shift* weight polynomial for \(2\le n\le14\). It matches the published unweighted totals in OEIS A179674 for all \(2\le n\le43\) upon setting \(y=1\), and checks prime-length coefficients for sixteen odd primes through \(59\). It also checks coefficient nonnegativity, bit-complement symmetry, and divisibility by \(n\). Executing `python3 verify.py` returns `VERIFY_OK`. These finite checks corroborate, but do not replace, the all-length proof above.

## Relationship to prior work
Gabrić, *Words that almost commute* (first preprint 2021; later journal version), determines the **unweighted** cardinality of binary and larger-alphabet words having a distance-two conjugate, the individual-shift totals, overlap structure, and total necklace counts. The present identity explicitly refines those counts **at every fixed number of ones**, including the weight-sensitive overlap correction. In particular, setting \(y=1\) recovers Gabrić's formulas; this is a compatibility check, not an independent claim of novelty. Shallit's work establishes foundational restrictions on attainable Hamming distances between conjugates, but does not present a fixed-weight enumerator. OEIS A179674 lists the unweighted totals, not a coefficient array. No novelty is claimed for the known intersection characterization itself.

## Limitations
The argument is specialized to binary alphabets and distance exactly two; a nonbinary composition vector would require an additional treatment of symbol-change choices. The closed polynomial is a refinement of existing structural analysis rather than a new characterization. A mathematically equivalent unindexed constant-composition formula may exist elsewhere in the literature. Automated finite tests cannot establish priority, and no independent expert validation is claimed.

## References
1. D. Gabrić, *Words that almost commute*, arXiv:2110.01120, first publicly submitted October 3, 2021 UTC, https://arxiv.org/pdf/2110.01120 . In particular Lemmas 6–7, 9–16 and Theorems 17 and 19.
2. J. Shallit, *Hamming distance for conjugates*, arXiv:0710.1234, https://arxiv.org/pdf/0710.1234 .
3. OEIS A179674, *Number of binary length-n words having a conjugate at Hamming distance two*, https://oeis.org/A179674 .
