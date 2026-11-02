# Closed-factor spectrum of cyclic distinct-run powers

## Finding
Let \(q\ge3\); let \(a_0,\ldots,a_{q-1}\) be distinct letters, and let \(r_0,\ldots,r_{q-1}\) be positive integers. Put
\[
P=a_0^{r_0}a_1^{r_1}\cdots a_{q-1}^{r_{q-1}},\qquad p=\sum_{i=0}^{q-1}r_i,\qquad W=P^k\quad(k\ge2).
\]
A *closed factor* is a nonempty contiguous factor of \(W\) that is either a letter or a complete first return to a nonempty proper factor; repeated factors are counted only once. Write \(C_+(W)\) for the number of distinct nonempty closed factors.

**Theorem.** For all these parameters,
\[
\boxed{C_+(W)=(k-2)p^2+\frac{p^2-\sum_i r_i^2}{2}+2p.}
\]
In particular each further copy of \(P\) adds *exactly* \(p^2\) distinct closed factors, and the base count depends on the run lengths only through \(p\) and \(\sum_i r_i^2\).

The stronger result gives a disjoint, exhaustive structural classification and every length coefficient. Define \((x)_+=\max(x,0)\), and for \(1\le m\le(k-1)p\), set
\[
h_k(m)=\min\{p,(k-1)p-m+1\}.
\]
For each \(\ell\ge1\), the number \(c_\ell(W)\) of distinct closed factors of length \(\ell\) is
\[
\begin{aligned}
c_\ell(W)={}&\sum_{i=0}^{q-1}\mathbf1_{1\le\ell\le r_i}
+\sum_{i=0}^{q-1}\sum_{s=1}^{r_i}\mathbf1_{\ell=p-r_i+2s}\\
&+\sum_{m=1}^{(k-1)p}\mathbf1_{\ell=p+m}
\left(h_k(m)-\sum_{i=0}^{q-1}(r_i-m+1)_+\right).
\end{aligned}
\]
The displayed expressions count only distinct *nonempty* factors; the empty word, if included by convention, increases the total by one.

## Assumptions and scope
The alphabet letters \(a_i\) are pairwise different and indexed cyclically modulo \(q\). The inequalities \(q\ge3\), \(r_i\ge1\), and \(k\ge2\) are required. The factor relation is contiguous, not scattered. A closed word has a proper nonempty border occurring exactly twice (as prefix and suffix); letters are closed by convention. The proof uses the fact that each directed boundary bigram \(a_i a_{i+1}\) (including \(a_{q-1}a_0\)) occurs in the bi-infinite periodic extension only at one phase modulo \(p\). In particular, a factor containing a directed boundary has uniquely determined starting phase modulo \(p\).

## Proof
We classify all closed factors into three disjoint types. Below, indices on symbols and run lengths are cyclic modulo \(q\).

**Type A: constant factors.** For each \(i\) and \(1\le s\le r_i\), the factor \(a_i^s\) is closed. These \(\sum_i r_i=p\) factors are all distinct.

**Type B: complete returns with a constant frontier.** A nonconstant closed factor with a constant frontier must start and end in runs of the same letter \(a_i\). Its frontier is \(a_i^s\) for some \(s\ge1\). There cannot be an intervening full run of \(a_i\), since that would give another occurrence of the frontier. The two end fragments must each have length exactly \(s\): if one were longer, the border \(a_i^s\) would occur in at least two positions of that fragment. Consequently the complete factor is precisely
\[
B_{i,s}=a_i^s\,a_{i+1}^{r_{i+1}}\cdots a_{i+q-1}^{r_{i+q-1}}\,a_i^s,
\qquad 1\le s\le r_i.
\]
Conversely, each such factor is a complete first return to \(a_i^s\), because it contains only its two endpoint runs of \(a_i\). It occurs in \(P^2\), hence in \(W\), and different \((i,s)\) give different factors. There are exactly \(p\) such factors, of lengths \(p-r_i+2s\).

**Type C: complete returns with a mixed-letter frontier.** Consider a proper border containing at least two distinct symbols. It contains a directed boundary \(a_i a_{i+1}\), whose occurrences are spaced exactly \(p\) positions apart in the periodic extension. Therefore the shift between the two border occurrences is a positive multiple of \(p\). In particular a closed word having a mixed-letter frontier has length \(p+m\) for some \(m\ge2\), and the first \(m\) letters of the word form a mixed-letter factor. Indeed, since a word of length \(L>p\) has the period \(p\), its prefix of length \(m=L-p\) is a border. Any border longer than \(m\) would have a shift smaller than \(p\); if it were mixed-letter, this contradicts unique boundary phases; if it were constant, it would not be longer than the mixed-letter border. Hence the longest border is the length-\(m\) prefix. Because that prefix contains a directed boundary, it can occur only in phases differing by multiples of \(p\), and the length-\(p+m\) factor has exactly the two occurrences at offsets \(0\) and \(p\). Conversely, every length-\(p+m\) factor whose first \(m\) letters include a directed boundary is therefore closed.

For fixed \(m\), the possible factors in \(W=P^k\) have distinct starting phases \(t\in\{0,\ldots,h_k(m)-1\}\), where \(1\le m\le(k-1)p\). The number \(h_k(m)\) follows by requiring \(t+p+m\le kp\) and keeping only the first \(p\) phases. Their first \(m\) letters are constant precisely if the starting phase lies within a run of length \(r_i\ge m\) and is at least \(m\) positions before its end. There are \((r_i-m+1)_+\) such phases in run \(i\). Every excluded phase is available: its index is at most \(p-m\), whereas \(h_k(m)\ge p-m+1\) whenever \(m\le p\); for \(m>p\) no constant prefix is possible. Thus the number of Type-C factors of length \(p+m\) is
\[
h_k(m)-\sum_i(r_i-m+1)_+.
\]
The factors within Type C are distinct because their lengths and directed-boundary phases distinguish them.

**Exhaustiveness and disjointness.** Every closed nonconstant word has a nonempty longest border, which is either constant (Type B) or mixed-letter (Type C). Type A is constant, Type B is nonconstant with constant longest border, and Type C has a mixed-letter longest border; hence these types are disjoint. Summing their length counts gives the stated coefficient formula.

For the total, direct summation yields
\[
\sum_{m=1}^{(k-1)p}h_k(m)=(k-2)p^2+\frac{p(p+1)}2,
\qquad\sum_{m\ge1}(r_i-m+1)_+=\frac{r_i(r_i+1)}2.
\]
Adding \(p\) factors of Type A, \(p\) of Type B and the resulting number of Type C gives
\[
\begin{aligned}
C_+(W)&=2p+(k-2)p^2+\frac{p(p+1)}2-
\sum_i\frac{r_i(r_i+1)}2\\
&=(k-2)p^2+\frac{p^2-\sum_i r_i^2}{2}+2p,
\end{aligned}
\]
which is an integer because \(p^2-\sum_i r_i^2=2\sum_{i<j}r_i r_j\). This proves both statements.

## Verification
The accompanying standalone script `verify_closed_factors.py` enumerates literal distinct substrings of each tested word, tests the closed condition through every proper border and its literal occurrence count, independently constructs all three classified types, compares the exact sets and length histograms, and checks the formula. The successful run covered 4,032 distinct parameter cases: \(q\in\{3,4,5\}\), all \(r_i\in\{1,2,3,4\}\), and \(k\in\{2,3,4\}\). It compared 1,454,640 factor instances and 910,800 closed-factor instances. These finite checks are corroboration, not a replacement for the proof for arbitrary parameters.

For instance \(q=3\), \((r_0,r_1,r_2)=(2,1,1)\), and \(k=2\) give \(p=4\) and exactly \(13\) distinct nonempty closed factors. For \((1,1,1)\) and \(k=2\), the total is \(9\).

## Relationship to prior work
Parshina–Zamboni (2018) give a closed-factor complexity formula for aperiodic Arnoux–Rauzy words; their hypotheses do not cover finite powers of periodic distinct-run words. Parshina–Puzynina (2021, revised 2023), especially Propositions 1–2 and Lemmas 1–3, establish general facts and *bounds* for closed factors of primitive-root powers, but not the arbitrary distinct-run Type-A/B/C classification, length profile, or exact second-moment total. Badkobeh–Fici–Lipták (2013) give general closed-word characterizations and extremal bounds, likewise not this formula. A previously recorded result on binary five-run words concerns a two-letter alternating-run family with different repeated-letter geometry, so its claim neither specializes to nor implies this distinct-alphabet theorem.

## Limitations
The theorem does not classify closed factors when letters in nonadjacent run blocks repeat, or when \(P\) is not of the indicated distinct-letter cyclic-run form. Its periodic-phase argument cannot be applied unchanged to arbitrary periodic roots. Computational checks cover only finite parameters. The novelty comparison did not establish global uniqueness against all unpublished or unindexed results; independent scrutiny remains appropriate.

## References
1. O. Parshina and L. Q. Zamboni, *Open and closed factors of Arnoux–Rauzy words*, arXiv:1810.05472, first posted 2018-10-12, especially Theorem 1 and Section 2.
2. O. Parshina and S. Puzynina, *Finite and infinite closed-rich words*, arXiv:2111.00863, first posted 2021-11-01; Proposition 1–2 and Lemmas 1–3.
3. G. Badkobeh, G. Fici, and Z. Lipták, *On the Number of Closed Factors in a Word*, arXiv:1305.6395, 2013, especially Definition 1, Proposition 4, and the extremal discussion.
