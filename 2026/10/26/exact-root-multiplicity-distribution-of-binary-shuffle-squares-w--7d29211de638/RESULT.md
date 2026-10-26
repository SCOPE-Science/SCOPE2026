# Exact root-multiplicity distribution of binary shuffle squares with two ones

## Finding

For every integer \(m\geq 0\), consider the binary linear words of length \(2m+2\) with exactly two occurrences of \(1\). Write each such word uniquely as
\[
W=0^A1\,0^B1\,0^C,\qquad A,B,C\in\mathbb Z_{\geq0},\quad A+B+C=2m.
\]
A *shuffle-square root* is a word \(U\) for which the positions of \(W\) can be partitioned into two subsequences, both spelling \(U\), in their original order. Count distinct roots, not partitions, and let \(R(W)\) be their number.

**Complete root criterion.** The possible roots are exactly \(0^q1\,0^{m-q}\) with integer \(q\) in the interval
\[
\max\!\left\{\left\lceil\frac A2\right\rceil,m-C\right\}
\ \le q\le\
\min\!\left\{A,m-\left\lceil\frac C2\right\rceil\right\}.
\]
In particular, a root exists if and only if
\[
(A\bmod2)+(C\bmod2)\ \le B\le m.
\]

**Complete distribution.** Define \(S(j)=0\) for integers \(j<0\), and
\[
S(j)=\frac{3j^2+3j+2}{2}\qquad(j\geq0).
\]
For every positive integer \(t\), the number of length-\(2m+2\) words with exactly \(t\) distinct shuffle-square roots is
\[
\boxed{N_m(t)=S(m-3t+3)-S(m-3t).}
\]
The number with at least one root is \(S(m)\), and the number with no root is \(\binom{2m+2}{2}-S(m)\). Equivalently, the complete positive-root distribution has generating function
\[
\boxed{\sum_{m\geq0}\sum_{t\geq1}N_m(t)x^my^t
=\frac{y(1+x+x^2)^2}{(1-x)^2(1-x^3y)}.}
\]
The largest root multiplicity is \(\lfloor m/3\rfloor+1\); the number of words attaining it is respectively \(1,4,10\) as \(m\equiv0,1,2\pmod3\). For \(m\ge3\), exactly \(9(m-1)\) words have a unique root. Thus the fraction of uniquely rooted words **among shuffle squares in this layer** tends to zero, whereas the fraction of all two-one words which are shuffle squares tends to \(3/4\).

A structural explanation is the *three-gap peeling bijection*: for each \(s\geq0\), subtracting \(2s\) zeros from **each** of the three zero gaps is a bijection from words with at least \(s+1\) roots at parameter \(m\) to all shuffle squares of this form at parameter \(m-3s\). The statement applies when \(m\ge3s\).

## Assumptions and scope

Words are finite and linear (no identification under reversal or rotation), over the labeled alphabet \(\{0,1\}\). A root is a *distinct word* of length \(m+1\), and different interleaving witnesses of the same root count only once. Both zero gaps and their boundary values may vanish. The results hold for every integer \(m\ge0\); for \(m=0\), the only word is \(11\), with root \(1\). No statement about unrestricted compositions or larger alphabets is asserted.

## Proof

**1. Exact root interval.** Since the output has exactly two ones, each root must have exactly one one. Thus it is uniquely of the form \(U_q=0^q1\,0^{m-q}\), with \(0\le q\le m\). The first output one must be supplied by one copy and the second by the other: two copies of a one-one root contribute one output one apiece. Before the first output one, its copy needs exactly \(q\) preceding zeros and the other copy may contribute any number between zero and \(q\). Hence \(q\le A\le2q\). Symmetrically, after the second output one, the two copies must contribute between \(m-q\) and \(2(m-q)\) zeros, giving \(m-q\le C\le2(m-q)\). These four inequalities are also sufficient. To construct an interleaving, distribute the first \(A\) zeros as \(q\) for the first-to-one copy and \(A-q\) for the second copy; put the next \(2q-A\) zeros into the second copy before its one, and the next \(2(m-q)-C\) zeros into the first copy after its one; finally distribute the last \(C\) zeros as \(m-q\) for the second-to-one copy and \(C-(m-q)\) for the first. The two middle allocations sum to \(B\), because \(A+B+C=2m\). All allocations are nonnegative by the four inequalities. Therefore precisely the asserted integer interval comprises the roots.

**2. Existence and counting.** The interval is nonempty precisely when its two upper bounds exceed its two lower bounds. The inequalities \(A\ge\lceil A/2\rceil\) and \(C\ge\lceil C/2\rceil\) are automatic. The remaining two conditions are \(A+C\ge m\), equivalently \(B\le m\), and \(\lceil A/2\rceil+\lceil C/2\rceil\le m\). Setting \(\varepsilon_A=A\bmod2\) and \(\varepsilon_C=C\bmod2\), and using \(A+C=2m-B\), the second becomes \(B\ge\varepsilon_A+\varepsilon_C\). For \(B=0\), this requires both \(A,C\) even, yielding \(m+1\) choices. For every \(1\le B\le m\), the parity constraint is automatic because \(A+C\equiv B\pmod2\) (if \(B=1\), exactly one outer gap is odd). There are \(2m-B+1\) choices. Consequently
\[
S(m)=(m+1)+\sum_{B=1}^m(2m-B+1)=\frac{3m^2+3m+2}{2}.
\]

**3. Peeling bijection.** Put \(s=t-1\). The root interval contains at least \(t\) integers exactly when every upper bound exceeds every lower bound by at least \(s\). The four resulting inequalities are
\[
A\ge2s,\quad C\ge2s,\quad B\le m-s,\quad B\ge2s+\varepsilon_A+\varepsilon_C.
\]
The last inequality follows from \(m-\lceil A/2\rceil-\lceil C/2\rceil=(B-\varepsilon_A-\varepsilon_C)/2\). All three gaps are therefore at least \(2s\). Subtract \(2s\) from each gap and set \(m'=m-3s\). The new gaps are nonnegative, total \(2m'\), and satisfy
\[
\varepsilon_{A-2s}+\varepsilon_{C-2s}\le B-2s\le m'.
\]
By step 2 these are exactly the shuffle squares with two ones and parameter \(m'\). Adding \(2s\) zeros to each of their gaps reverses the construction. Hence the number with \(R(W)\ge t\) is \(S(m-3(t-1))\), proving the distribution by subtraction.

**4. Generating function and extrema.** The elementary series identity
\[
\sum_{m\ge0}S(m)x^m=\frac{1+x+x^2}{(1-x)^3}
\]
combined with \(N_m(t)=S(m-3(t-1))-S(m-3t)\) gives the asserted bivariate rational function. Since \(S(j)>0\) exactly for \(j\ge0\), the largest possible root count is \(\lfloor m/3\rfloor+1\), and the number attaining it is \(S(m\bmod3)\), namely \(1,4,10\). Similarly, \(N_m(1)=S(m)-S(m-3)=9(m-1)\) for \(m\ge3\).

**5. Two asymptotic consequences and an incidence identity.** With the output chosen uniformly among the words in this fixed-composition layer, \(\Pr(R>0)=S(m)/\binom{2m+2}{2}\to3/4\) as \(m\to\infty\). Conditional on \(R>0\), the peeling identity gives, for \(0\le u\le1/3\),
\[
\Pr\bigl(R/m>u\mid R>0\bigr)\longrightarrow(1-3u)^2.
\]
Thus \(R/m\), conditional on being a shuffle square, has limiting density \(6(1-3u)\) on \([0,1/3]\), and conditional mean asymptotic to \(m/9\). An independent check counts root-output incidences by fixing \(q\). Each \(U_q\) generates exactly \((q+1)(m-q+1)\) distinct outputs, so
\[
\sum_W R(W)=\sum_{q=0}^{m}(q+1)(m-q+1)=\binom{m+3}{3}.
\]
The same follows by differentiating the bivariate generating function in \(y\) at \(y=1\), which gives \((1-x)^{-4}\).

## Verification

Run `python3 verify.py` using Python 3 and only the standard library. It independently tests the root interval with a two-copy interleaving automaton for every two-one word with \(0\le m\le15\), and constructs all output shuffles of each one-one root for \(0\le m\le9\). The first census contains \(2856\) words, of which \(2056\) admit a root; the constructive check traverses \(715\) distinct root-output incidences. It additionally checks the finite distribution, extrema and incidence identities through \(m=100\). The supplied implementation printed `PASS` for all tests. All-length validity rests on the preceding proof, not the finite tests.

## Relationship to prior work

Buss and Soltys introduced the decision problem and proved NP-completeness for recognizing general shuffle squares, in a preprint first public on 30 November 2012 [1]. Guégan and Ochem studied avoidance and explicitly assigned the problem to MSC \(68R15\) [2]. Grytczuk, Pawlik and Pleszczyński [3, Section 2.5, Theorem 3] **already characterized which linear two-one binary words are shuffle squares**, and [3, Corollary 1] **already proved exactly the scalar total** \(S(m)=(3m^2+3m+2)/2\). Their Proposition 1 also establishes that any such even binary word has **some cyclic rotation** which is a shuffle square. The existence criterion and the total \(S(m)\) in this manuscript are reproved only as premises and are **not presented as new findings**.

Datko and Pawlik [4, Proposition 1] showed that a *fixed root* \(0^q1\,0^{m-q}\) produces \((q+1)(m-q+1)\) distinct shuffle outputs, which agrees with the incidence identity above. Their Section 3 studies root multiplicities of unrestricted binary shuffle squares, provides finite enumerations, and identifies some uniquely rooted families [4, Theorem 2]. Their explicit example `0000100100` has two roots and lies in the present fixed-composition family. The present result instead gives the complete inverse-image multiplicity distribution for **every** length in that natural sparse layer, including an exact bijection and limiting law; it is not obtained from their per-root totals alone, because totals do not determine output overlaps. The unrestricted uniqueness-ratio conjecture in [4] is not resolved here.

OEIS A005448 [5] explicitly records this exact same binary-shuffle-square counting interpretation with a 7 September 2023 attribution to Pawlik and a reference to [3]. Thus the aggregate count is established prior art, **not an originality claim**. What is new here, relative to these inspected statements, is the exact number of **distinct roots of each word**, the all-length inverse **multiplicity distribution** \(N_m(t)\), its three-gap peeling bijection, and its rational generating function and conditional limit law. The classification of membership in [3] and counts of outputs for one fixed root in [4] do not imply the distribution of overlaps of those root-output sets. Searches for synonyms including self-interleavings, self-shuffle roots, fixed Hamming weight, and uniquely rooted/explicit shuffle squares did not identify a covering multiplicity distribution. Historical priority remains subject to unindexed equivalent work.

## Limitations

The theorem is restricted to linear binary words with exactly two ones and an even number of zeros; it does not classify arbitrary binary shuffle squares, their general decision complexity, or more than two marked symbols. The limiting distribution is conditional on being a shuffle square. Computation checks finite ranges only. No claim of exhaustive worldwide publication coverage is made.

## References

[1] S. Buss and M. Soltys, *Unshuffling a Square is NP-Hard*, arXiv:1211.7161v1 (public 2012-11-30); subsequently *J. Comput. Syst. Sci.* 80 (2014), 766–776. https://arxiv.org/abs/1211.7161.

[2] G. Guégan and P. Ochem, *A short proof that shuffle squares are 7-avoidable*, *RAIRO Theor. Inform. Appl.* 50 (2016), 101–103, doi:10.1051/ita/2016007. https://www.numdam.org/item/ITA_2016__50_1_101_0/.

[3] J. Grytczuk, B. Pawlik and M. Pleszczyński, *Variations on shuffle squares*, arXiv:2308.13882 (2023; version 2024), Section 2.5, Theorem 3 and Corollary 1. https://arxiv.org/html/2308.13882v2.

[4] D. Datko and B. Pawlik, *Roots of Binary Shuffle Squares*, *Symmetry* 17 (2025), 305, doi:10.3390/sym17020305. https://doi.org/10.3390/sym17020305.

[5] OEIS A005448, centered triangular numbers; includes Pawlik's 2023 interpretation as the number of length-\(2n\) binary shuffle squares containing exactly two ones. https://oeis.org/A005448.
