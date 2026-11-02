# Complete palindromic and minimal-absent-palindrome spectra of binary block powers

## Finding

For every triple of integers \(a,b,k\geq1\), consider the finite binary word
\[
W=(0^a1^b)^k,\qquad p=a+b,\qquad n=kp.
\]
A *minimal absent palindromic word* (MAPW) over \(\{0,1\}\) is a nonempty palindrome \(u\) absent as a contiguous factor of \(W\) whose interior \(u[2..|u|-1]\) occurs as a factor (the empty interior occurs). This is the MAPW definition of Mieno et al. [1], not the generally different definition of an ordinary minimal absent factor.

Define \(R_0,R_1\) by
\[
(R_0,R_1)=
\begin{cases}
\bigl(\frac{k-1}{2}p,\frac{k-1}{2}p\bigr),&k\text{ odd},\\
\bigl((\frac{k}{2}-1)p+b,(\frac{k}{2}-1)p+a\bigr),&k\text{ even}.
\end{cases}
\]
For each integer \(t\geq0\), let \(v_{0,t}\) be the length-\(t\) prefix of the right-infinite periodic word \((1^b0^a)^\omega\), and let \(v_{1,t}\) be the corresponding prefix of \((0^a1^b)^\omega\). Write \(v^R\) for reversal.

The **complete set** of distinct palindromic factors, including the empty word \(\varepsilon\), is exactly the disjoint union
\[
\begin{aligned}
\operatorname{Pal}(W)={}&\{\varepsilon\}\cup\{0^j:1\le j\le a\}\cup\{1^j:1\le j\le b\}\\
&\cup\{v_{0,t}^R0^av_{0,t}:1\le t\le R_0\}\\
&\cup\{v_{1,t}^R1^bv_{1,t}:1\le t\le R_1\}.
\end{aligned}
\]
In particular, the complete palindromic-factor length enumerator is
\[
H_{a,b,k}(z)=1+\sum_{j=1}^a z^j+\sum_{j=1}^b z^j
+\sum_{t=1}^{R_0}z^{a+2t}+\sum_{t=1}^{R_1}z^{b+2t}.
\]
The **complete MAPW length enumerator** is
\[
\boxed{B_{a,b,k}(z)=(2z^2-1)H_{a,b,k}(z)+1+2z.}
\]
Equivalently, if \(h_j=[z^j]H_{a,b,k}(z)\), with \(h_j=0\) outside its support, then the number of MAPWs of each length \(\ell\geq2\) is precisely \(2h_{\ell-2}-h_\ell\); there are no MAPWs of length one.

Two useful consequences are
\[
\boxed{|\operatorname{MAPW}(W)|=kp+4,\qquad
\max_{u\in\operatorname{MAPW}(W)}|u|=kp-\min(a,b)+2.}
\]
The cardinality is also obtainable from general results on rich words and eertrees; the specific finite-power palindromic-factor classification, **all-length MAPW spectrum**, and exact longest-length boundary are the subject of the finding.

## Assumptions and scope

All exponents \(a,b,k\) are **positive integers**, with no restriction that \(a\neq b\), and \(k=1\) is included. The alphabet is exactly the two symbols \(\{0,1\}\), with factors contiguous. Different occurrences of an identical factor are counted only once. The empty palindrome is included in \(H\) but not in the MAPW set. The length-generating variable \(z\) is an indeterminate, so all enumerator equalities are polynomial identities.

## Proof

**Step 1 (possible centers).** Every run of zeros in \(W\) has length \(a\), and every run of ones has length \(b\). A nonconstant palindrome cannot be centered at a run boundary, since the letters immediately on opposite sides of such a boundary differ. Nor can a nonconstant palindrome be centered off the midpoint of its central run: the first transition away from the center would then occur at unequal distances on the left and right, contradicting symmetry. Hence a nonconstant palindrome must contain one **entire** central run and be centered at its midpoint. Every constant palindrome is among the two unary collections listed above.

**Step 2 (symmetric wings).** In the bi-infinite continuation of the alternating runs, both wings read outward from a central zero run as the same infinite sequence \((1^b0^a)^\omega\). Thus the unique possible palindrome with central zero run and wing length \(t\) is \(v_{0,t}^R0^av_{0,t}\). Its availability at the \(j\)-th zero run is equivalent to having \(t\) characters available on both sides. Those available lengths are \((j-1)p\) and \((k-j)p+b\), respectively, so its maximal available radius is
\[
r_{0,j}=\min\bigl((j-1)p,(k-j)p+b\bigr),\qquad1\le j\le k.
\]
Likewise, at the \(j\)-th one run, the maximal radius is
\[
r_{1,j}=\min\bigl((j-1)p+a,(k-j)p\bigr),\qquad1\le j\le k.
\]
For each center type, all wing lengths between one and the largest available radius occur. Maximizing these two piecewise-linear minimum functions over integer \(j\) gives
\[
\max_jr_{0,j}=R_0,\qquad \max_jr_{1,j}=R_1
\]
with the stated even/odd formulas. Conversely, no larger radius can occur. Two different wing lengths yield different total lengths within a ray; a zero-centered mixed palindrome cannot equal a one-centered mixed palindrome because its central run has the opposite symbol. Neither ray contains a unary word. This proves the asserted disjoint set decomposition and the formula for \(H_{a,b,k}\).

**Step 3 (exact absent extension accounting).** Every palindrome of length at least two has a unique representation \(cvc\), with \(c\in\{0,1\}\) and \(v\) its (possibly empty) palindromic interior. Thus the collection of **candidate** palindromic extensions of occurring palindromes is counted, without duplication, by \(2z^2H(z)\). Among these candidates the occurring palindromes are exactly those of length at least two, enumerated by \(H(z)-1-2z\): both one-letter palindromes occur because \(a,b\ge1\). Every candidate that does not occur meets the MAPW definition, and every MAPW is such a candidate. Subtraction therefore gives
\[
B(z)=2z^2H(z)-(H(z)-1-2z),
\]
which is the claimed full length spectrum.

**Step 4 (counts and longest boundary).** Directly from the even/odd formulas, \(R_0+R_1=(k-1)p\). Consequently \(H(1)=1+a+b+R_0+R_1=kp+1\) and \(B(1)=H(1)+3=kp+4\). The largest palindromic-factor length is
\[
L=\max\{a,b,a+2R_0,b+2R_1\}=(k-1)p+\max(a,b).
\]
Every MAPW has an occurring interior and therefore length at most \(L+2\). Given an occurring palindrome of maximal length \(L\), either of its two palindromic extensions has length \(L+2\) and is absent, showing equality. Substituting \(p=a+b\) produces the displayed longest-MAPW formula.

## Verification

The included `verify.py` reconstructs literal factor sets and palindromic factors directly for each \(1\le a,b\le7\) and \(1\le k\le8\). It independently tests the predicted two-ray palindromic set and MAPW set, every coefficient of the enumerator, the exact total, and the longest MAPW. This covers \(392\) parameter triples. Finite checking does not prove the universal claim; the four proof steps above establish it for all positive integers.

## Relationship to prior work

Mieno et al. [1] introduce MAPWs and prove the general eertree missing-edge characterization (their Section 5.2, Lemma 7 and Corollary 1), as well as dynamic maintenance algorithms. That general characterization is used transparently in Step 3 and is not claimed as new. It does **not** state the two complete finite-power palindromic rays or the explicit parameter-dependent length polynomial here.

Glen et al. [2] establish richness properties of periodic words. In particular, their Theorem 3.1 concerns when a periodic word is rich, which is consistent with our derived \(H(1)=|W|+1\). Together with [1], such general facts account for the easily obtained total \(|W|+4\); this total is presented as a consequence, not an independent priority claim. Neither general theorem resolves the two endpoint-dependent radii \(R_0,R_1\) and the entire finite-word MAPW length spectrum without the additional run-center analysis.

The algorithmic results for ordinary minimal absent factors on run-length encoded strings in Akagi et al. [3] concern a different absent-word predicate (all proper contiguous factors present). They are not an exact classification of palindromes whose **interior** occurs.

## Limitations

The theorem concerns exactly equal repetitions of a two-run period over a **binary** alphabet, not arbitrary binary words, unequal run sequences, cyclic factors, or a larger ambient alphabet. The MAPW definition differs from the ordinary minimal-absent-factor definition. The direct formula for the total count can already be obtained from general published theory; only the full explicit finite-power structure and length spectrum are assessed as potentially new. An equivalent specialized length formula outside the inspected literature remains a possible originality risk. No independent audit or external certification has been performed.

## References

[1] T. Mieno, K. Watanabe, Y. Nakashima, S. Inenaga, H. Bannai, M. Takeda, *Palindromic Trees for a Sliding Window and Its Applications*, arXiv:2006.02134, first submitted 2020-06-03, especially Section 5.2.

[2] A. Glen, J. Justin, S. Widmer, L. Q. Zamboni, *Palindromic Richness*, arXiv:0801.1656, first submitted 2008-01-10, especially Theorem 3.1.

[3] T. Akagi, K. Okabe, T. Mieno, Y. Nakashima, S. Inenaga, *Minimal Absent Words on Run-Length Encoded Strings*, CPM 2022, LIPIcs 223, article 27 (abstract considered; full text not used as negative evidence).
