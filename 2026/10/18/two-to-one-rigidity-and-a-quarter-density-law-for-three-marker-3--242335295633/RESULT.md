# Two-to-one rigidity and a quarter-density law for three-marker 3-decks

## Finding

For an integer \(n\geq3\), consider binary words of length \(n\) containing exactly three ones. The **\(3\)-binomial profile** of a word records, for every binary word of length one, two, or three, the number of its occurrences as a scattered subsequence (positions need not be adjacent). Two words are **\(3\)-binomially equivalent** when all of these counts agree.

**Theorem.** Every equivalence class restricted to binary words of length \(n\) and Hamming weight three has size at most two. All non-singleton classes are described by the following disjoint and exhaustive parametrization. Set \(z=n-3\), and choose integers \(u\geq0\), \(t\geq1\), and \(a\geq t\) with
\[
 a+2u+3t\leq z.
\]
For the first word, the numbers of zeros preceding its successive ones are
\[
(a,\ a+u,\ a+2u+3t).
\]
For its unique distinct equivalent word, those three numbers are
\[
(a-t,\ a+u+2t,\ a+2u+2t).
\]
These pairs, and no others, are the two-element equivalence classes.

Let \(C(n)\) denote their number, with \(C(n)=0\) for \(n<3\). Then for every \(n\geq3\),
\[
 C(n)=\sum_{t\geq1}\sum_{u\geq0}\max\{0,n-2-2u-4t\},
 \qquad
 \sum_{n\geq0}C(n)x^n=\frac{x^7}{(1-x)^2(1-x^2)(1-x^4)}.
\]
The sums are finite for each \(n\). Thus the number of distinct profiles on the weight-three layer is exactly
\[
\binom n3-C(n),
\]
and the number of singleton words is \(\binom n3-2C(n)\). In particular,
\[
C(n)=\frac{n^3}{48}+O(n^2),\qquad
\lim_{n\to\infty}\frac{2C(n)}{\binom n3}=\frac14.
\]
Hence a uniformly sampled binary word with exactly three ones is asymptotically ambiguous with probability one quarter under its complete length-at-most-three scattered-subsequence profile; every such ambiguous word has exactly one partner.

## Assumptions and scope

All words are linear, not cyclic; their alphabet is \(\{0,1\}\). The words in the theorem have length \(n\), exactly three ones, and consequently exactly \(z=n-3\) zeros. The standard \(k\)-binomial relation uses the **counts** of every scattered binary word of length at most \(k\), not merely whether a subsequence exists. The notion agrees with that in Freydenberger et al., *Testing k-binomial equivalence* (2015). The first case with an ambiguity in the specified layer is \(n=7\). Moreover, no word with fewer than three ones can be ambiguous at this observation depth: for weight one, \(\binom{w}{01}\) gives the sole zero-before-one count; for weight two, \(\binom{w}{01}\) and \(\binom{w}{001}\) determine the sum and the sum of squares of the two ordered zero-before-one counts, hence determine both counts uniquely.

There is a bijection between such words and nondecreasing integer triples
\[
0\leq a\leq b\leq c\leq z:
\]
\(a,b,c\) count zeros strictly before the first, second, and third ones, respectively. The one-positions (zero-based) are \(a,b+1,c+2\). This encoding remains valid when two or three ones are adjacent.

## Proof

**1. Reduction to three numeric invariants.** Let \(S=a+b+c\), \(Q=\binom a2+\binom b2+\binom c2\), and \(T=2a+b\). If \(\binom{w}{v}\) means the number of scattered occurrences of \(v\) in \(w\), then
\[
\begin{aligned}
\binom{w}{01}&=S,& \binom{w}{001}&=Q,& \binom{w}{011}&=T.
\end{aligned}
\]
The first equality counts zeros preceding each one. The second chooses two zeros before each one. In the third, a zero before the first one can be paired with either of the other two ones, while a zero before the second one can be paired with the third.

Conversely, these three statistics, together with \(n\) and weight three, determine **every** scattered count of length at most three. The length-two counts are \(\binom{w}{00}=\binom z2\), \(\binom{w}{10}=3z-S\), \(\binom{w}{11}=3\). For length three, in the order indicated,
\[
\begin{array}{cc|cc}
000&\binom z3 &001&Q\\
010&(z-1)S-2Q &011&T\\
100&3\binom z2-(z-1)S+Q &101&2(S-T)\\
110&3z-2S+T &111&1.
\end{array}
\]
Indeed, \(010\) counts a zero before and a zero after one chosen one, so its count is \(\sum_{d\in\{a,b,c\}}d(z-d)\). Similarly, \(100\) is \(\sum_d\binom{z-d}{2}\). The pattern \(101\) counts zeros between two chosen ones, giving \((b-a)+(c-a)+(c-b)=2(c-a)\). Finally, \(110\) counts zeros after the second member of a chosen pair of ones and yields \((z-b)+2(z-c)\). Thus two weight-three words of length \(n\) are \(3\)-binomially equivalent **if and only if** their \((S,Q,T)\) agree.

**2. At most one distinct partner.** Suppose a triple \((a',b',c')\) has the same \((S,Q,T)\). The two linear equations give
\[
b'=T-2a',\qquad c'=S-T+a'.
\]
Equality of \(Q\) is equivalent, since \(S\) is fixed, to equality of sums of squares. The possible first coordinates are therefore roots of
\[
6y^2+(2S-6T)y+T^2+(S-T)^2
 =a^2+b^2+c^2.
\]
This quadratic has at most two real roots. One is \(a\), so any other must be \(a'=T-S/3-a\). Consequently the profile fiber has at most two words, with no need to assume that one-positions are distinct beyond the encoded order.

Put \(u=b-a\geq0\) and \(v=c-b\geq0\). The candidate second root gives exactly
\[
 (a',b',c')=\left(a+\frac{u-v}{3},\ a+\frac{u+2v}{3},\ a+\frac{4u+2v}{3}\right).
\]
It is integral only if \(u\equiv v\pmod3\); its consecutive differences are \(v,u\). If \(u=v\), the candidate equals the original triple and the class is a singleton. If \(u\ne v\), integrality and \(0\leq a'\leq b'\leq c'\leq z\) are also sufficient: the constructed triple has identical \(S,T,Q\), by the quadratic identity, hence the same complete scattered profile.

**3. Canonical classification of every pair.** In any distinct pair, the two triples have opposite ordered gap pairs \((u,v)\) and \((v,u)\). Exactly one has \(u<v\), so write \(v=u+3t\) for a unique integer \(t\geq1\). The candidate formula becomes
\[
 (a,b,c)=(a,a+u,a+2u+3t),\qquad
 (a',b',c')=(a-t,a+u+2t,a+2u+2t).
\]
Both belong to \([0,z]\) precisely when \(a\geq t\) and \(a+2u+3t\leq z\). The second triple's last coordinate is smaller than the first triple's last coordinate, while the first triple's first coordinate exceeds the second's, so these two inequalities capture all endpoints. This proves completeness, uniqueness, and the stated parametrization.

**4. Exact enumeration.** For fixed \(t\geq1\) and \(u\geq0\), the permissible integer choices are
\[
t\leq a\leq z-2u-3t.
\]
Their number is \(\max\{0,z-2u-4t+1\}=\max\{0,n-2-2u-4t\}\), proving the double sum. For \(L\geq0\), the coefficient identity
\[
\sum_{n\geq0}\max\{0,n-L\}x^n=\frac{x^{L+1}}{(1-x)^2}
\]
then gives
\[
\sum_{n\geq0}C(n)x^n
=\sum_{u\geq0,t\geq1}\frac{x^{3+2u+4t}}{(1-x)^2}
=\frac{x^7}{(1-x)^2(1-x^2)(1-x^4)}.
\]
The only pole of order four is at \(x=1\), with leading local factor \(1/[8(1-x)^4]\); other poles have order at most two. Hence \(C(n)=n^3/48+O(n^2)\). Since \(\binom n3=n^3/6+O(n^2)\), the ambiguity fraction tends to \(1/4\). All assertions follow. \(\square\)

## Verification

The standalone Python 3 program `verify_three_marker.py` independently calculates every scattered count for all words of weight three and lengths \(3\leq n\leq30\) using an ordinary subsequence-count dynamic program. For each length it groups words by their entire measured profile, compares every group with the proposed explicit partner, verifies that no group has more than two words, and checks the exact doubleton and total class counts. It additionally compares two different coefficient formulas for every length through 1000. Its observed terminal status was `VERIFY_OK`.

For example, the first non-singleton pair, already explicitly listed in OEIS A258585, is `0110001` and `1000110` at length seven. The checker finds one doubleton at length seven, 14 at length twelve, 100 at length twenty, and 406 at length thirty. None of these finite checks substitutes for the proof of the statements at arbitrary lengths.

To reproduce from the directory containing both files, run `python3 verify_three_marker.py`. Python's standard library is sufficient. The program contains no network activity and reads no external data.

## Relationship to prior work

The definition of \(k\)-binomial equivalence and algorithmic testing is classical; Freydenberger, Gawrychowski, Karhumäki, Manea, and Rytter (arXiv:1509.00622, 2015) give general polynomial-time testing methods. Lejeune, Rigo, and Rosenfeld (arXiv:2001.11732, 2020) study general \(k\)-binomial class counts and singleton languages; their treatment and conclusion focus on \(2\)-binomial structures and general growth bounds, not the present full weight-three \(3\)-binomial fiber classification.

OEIS A258585, created in November 2015, tabulates **global** binary \(3\)-binomial class counts and explicitly lists the length-seven collision `0110001`/`1000110`. That collision is acknowledged as previously known. The new statement here is not that a collision exists, but an exact classification of **all** weight-three collisions at **every** length, a rational generating function for all two-element fibers, and their limiting one-quarter density.

Chrisnata, Kiah, Rao, Vardy, Yaakobi, and Yao (2019 conference; later journal version DOI:10.3934/amc.2021032) compute unrestricted short-deck enumerations through finite lengths and general bounds. Their accessible abstract and table are global, not a weight-three all-length statement. A later work by Nilforoushan and Parvaresh (arXiv:2609.23106, September 2026) obtains general polynomial-order results for unrestricted decks. Neither global count determines how classes split across weights or whether a particular sparse layer has fibers of size two. No originality claim is made for the general deck methodology or earlier global tabulations.

## Limitations

The theorem is about binary words with exactly three ones. It does not classify fibers on higher Hamming-weight layers or determine the unrestricted \(3\)-binomial class count. It concerns fixed-length complete scattered counts up to three, not contiguous length-three factors and not ordinary deletion balls. The asymptotic density uses the uniform distribution on the weight-three layer, not the uniform distribution on all binary strings.

The proof is self-contained, but mathematical novelty cannot be established by unsuccessful searches alone. The journal full text of Chrisnata et al. could not be obtained during the literature comparison, despite searches for lawful full text; a previously unindexed sparse-layer specialization inside that paper remains a residual originality risk. Independent review has not been performed.

## References

1. D. D. Freydenberger, P. Gawrychowski, J. Karhumäki, F. Manea, and W. Rytter, *Testing k-binomial equivalence*, arXiv:1509.00622 (first posted 2015-09-02), https://arxiv.org/abs/1509.00622.
2. M. Lejeune, M. Rigo, and M. Rosenfeld, *On the binomial equivalence classes of finite words*, arXiv:2001.11732 (2020), https://arxiv.org/abs/2001.11732.
3. J. Shallit, OEIS A258585, *Number of equivalence classes of 3-binomial complexity for binary words of length n* (2015), https://oeis.org/A258585.
4. J. Chrisnata, H. M. Kiah, S. Rao Karingula, A. Vardy, E. Yaakobi, and H. Yao, *On the number of distinct k-decks: Enumeration and bounds*, Proc. ISCIT (2019); expanded journal version, *Advances in Mathematics of Communications* 17 (2023), 960–978, https://doi.org/10.3934/amc.2021032.
5. A. Nilforoushan and F. Parvaresh, *Improved upper bound on the number of distinct k-decks for any k and alphabet size by counting the independent parameters*, arXiv:2609.23106 (2026), https://arxiv.org/abs/2609.23106.
