# Exact longest subsequence-substring phases for opposite periodic permutations

## Finding

Fix integers \(q\ge2\), \(m\ge1\), and \(n\ge1\). Let \(P=0\,1\,\cdots\,(q-1)\), let \(Q=(q-1)\,\cdots\,1\,0\), and put \(X=P^m\), \(Y=Q^n\). A common subsequence-substring is a nonempty word occurring as a scattered subsequence of \(X\) and a contiguous factor of \(Y\). Its maximum length is

\[
L=\min\left\{qn,\ m+n-1,\ m+\left\lceil\frac{m}{q-1}\right\rceil\right\}.
\]

More strongly, **all distinct maximum-length common subsequence-substrings** are precisely the length-\(L\) factors of \(Y\) starting at residues \(r\) modulo \(q\) satisfying

\[
\max\{0,\,q(L-m)-L+1\}\ \le r\ \le\ \min\{q-1,\,qn-L\}.
\]

Their number is therefore

\[
N=\max\left\{0,\ 1+\min\{q-1,qn-L\}-\max\{0,q(L-m)-L+1\}\right\}.
\]

When \(q\ge3\) and \(m=n\ge2\), the formula reduces to \(L=m+\lceil m/(q-1)\rceil\). Yet the ordinary longest common subsequence has length at least \(2m-1\): restricting each period to letters \(0,q-1\) produces two opposite alternating words, whose common subsequence can have length \(2m-1\). Thus for every fixed \(q\ge3\), the subsequence-to-substring restriction causes an additive linear loss in this periodic family.

## Assumptions and scope

Letters \(0,1,\ldots,q-1\) are distinct and appear exactly once per period in opposite orders. Powers mean concatenations of full periods; both exponents are positive. Factors may start at any zero-based position, and scattered embeddings preserve the input order. Each distinct factor is counted once, even if it appears at several positions. Reversing the direction of the two roles generally changes the optimum: the substring requirement is imposed on \(Y\), not on \(X\).

## Proof

**Greedy embedding criterion.** Take a nonempty factor \(F=Y[s:s+\ell]\) of length \(1\le\ell\le qn\), beginning at zero-based index \(0\le s\le qn-\ell\). Adjacent letters of \(Q^n\) decrease inside a period and increase only at a transition \(0\to q-1\) between periods. In the increasing word \(P^m\), the greedily earliest embedding puts the first letter of \(F\) into the first copy of \(P\). Each subsequent decrease necessarily moves the embedding into the next copy of \(P\), whereas each increase \(0\to q-1\) is matched in that same copy. Since each letter occurs once per copy of \(P\), there is no alternative earlier embedding. Consequently, \(F\) embeds in \(X\) if and only if its number of decreasing adjacent pairs is at most \(m-1\).

Let \(w(s,\ell)\) be the number of increasing transitions inside \(F\). The transitions occur across edges indexed \(q-1,2q-1,\ldots,(n-1)q-1\). Hence

\[
w(s,\ell)=\left\lfloor\frac{s+\ell-1}{q}\right\rfloor-\left\lfloor\frac{s}{q}\right\rfloor
=\left\lfloor\frac{r+\ell-1}{q}\right\rfloor,
\qquad r=s\bmod q.
\]

There are \(\ell-1-w(s,\ell)\) decreasing transitions, so the criterion is equivalent to

\[
\left\lfloor\frac{r+\ell-1}{q}\right\rfloor\ge\ell-m
\quad\Longleftrightarrow\quad
r\ge q(\ell-m)-\ell+1.
\]

**All optimal phases.** For fixed \(\ell\), the possible starting residues are exactly \(0\le r\le\min\{q-1,qn-\ell\}\). Each such residue occurs as the initial position \(s=r\), and all starts with the same residue yield identical length-\(\ell\) factors. Different residues yield different first letters, because the letters within a period are distinct. Intersecting this possible-residue interval with the greedy criterion gives the stated interval and its counting formula, with \(\ell=L\).

**Maximum length.** Write \(t=\ell-1\). Among all length-\(t\) windows of transitions in \(Y\), the largest possible number of increasing edges is

\[
\min\left\{n-1,\left\lceil\frac{t}{q}\right\rceil\right\}.
\]

The upper bounds follow from the total number \(n-1\) of increasing edges and their mutual spacing \(q\). For \(t\le q(n-1)\), a window beginning with the first such edge (at index \(q-1\)) realizes \(\lceil t/q\rceil\). For \(t>q(n-1)\), a window beginning at index zero includes all \(n-1\) increasing edges. Thus a length \(\ell\) is feasible exactly when

\[
1\le\ell\le qn,\qquad
\ell-m\le n-1,\qquad
\ell-m\le\left\lceil\frac{\ell-1}{q}\right\rceil.
\]

The middle inequality says \(\ell\le m+n-1\). For \(\ell>m\), writing \(h=\ell-m\ge1\), the last inequality is equivalent, by integer ceiling arithmetic, to

\[
(q-1)h\le m+q-2
\quad\Longleftrightarrow\quad
h\le\left\lceil\frac{m}{q-1}\right\rceil.
\]

For \(\ell\le m\), that inequality holds automatically. Therefore feasibility is equivalent to the three bounds in the displayed formula for \(L\), proving both necessity and sufficiency. The finite maximum is positive because single letters match.

**Linear-loss consequence.** For \(q\ge3\), \(m=n\ge2\), one has \(m+\lceil m/(q-1)\rceil\le2m-1\le qm\). The ordinary LCS of \(X\) and \(Y\) has length at least \(2m-1\): retain only \(0\) and \(q-1\) in each of the two words and delete the first letter from one of the opposite alternating length-\(2m\) strings. The resulting common length-\(2m-1\) subsequence exists in both words. The lower bound on the difference is thus \(m-1-\lceil m/(q-1)\rceil\), asymptotic to \((q-2)m/(q-1)\) for fixed \(q\ge3\).

## Verification

Run `python3 check.py` from the directory containing this report. The checker constructs both words from the definition and independently enumerates every possible substring and greedily tests its scattered embeddability. For all \(q=2,\ldots,8\) and \(m,n=1,\ldots,9\), it compares the optimum length, the count, and the exact sets of optimal distinct words to the closed formulas (567 parameter cells). An independent per-factor comparison covers 70,756 cases for smaller parameters. Recorded output is provided as `check_output.txt`. These finite checks corroborate, but do not establish, the all-parameter proof above.

## Relationship to prior work

Li, Deka and Deka introduced the longest common subsequence-substring problem and gave a general dynamic-programming algorithm [1]. Golan, Kraus, Porat and Shalom investigated its conditional complexity, algorithms, approximation and multi-string variants [2]. Li and coauthors also studied a constrained version [3]. Their general algorithms evaluate individual finite input pairs; the inspected texts do not supply this all-parameter closed form, optimal-factor classification, or linear-loss separation for opposite ordered periods. General algorithms should not be mistaken for explicit previously published symbolic classifications. This comparison is not a guarantee against unindexed equivalent results.

## Limitations

The theorem is specific to opposite permutations repeated in full periods; arbitrary permutations, imperfect periods, and arbitrary input words are not classified. The result gives a combinatorial closed form, not a faster worst-case algorithm for unrestricted LCSS. It establishes a lower bound on the **ordinary** LCS only to exhibit a gap; it does not classify ordinary LCS witnesses here. No independent scientific audit has been performed.

## References

[1] R. Li, J. Deka and K. Deka, *An Algorithm for the Longest Common Subsequence and Substring Problem*, arXiv:2308.00925 (2023), https://arxiv.org/abs/2308.00925 .

[2] S. Golan, M. Kraus, E. Porat and B. Riva Shalom, *Exploring the Gap Between LCS and LCStr*, 37th CPM (2026), LIPIcs 369, article 27, https://doi.org/10.4230/LIPIcs.CPM.2026.27 .

[3] R. Li, J. Deka, K. Deka and D. Li, *An Algorithm for the Constrained Longest Common Subsequence and Substring Problem*, arXiv:2308.01322 (2023), https://arxiv.org/abs/2308.01322 .
