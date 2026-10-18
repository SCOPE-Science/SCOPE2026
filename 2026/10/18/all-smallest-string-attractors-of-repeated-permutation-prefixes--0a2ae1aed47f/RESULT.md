# All smallest string attractors of repeated-permutation prefixes

## Finding
Let \(q\ge 2\), \(m\ge 1\), and \(0\le r<q\) be integers, and let \(a_0,\ldots,a_{q-1}\) be pairwise different letters. Set \(P=a_0\cdots a_{q-1}\) and \(T=P^m a_0\cdots a_{r-1}\), with the suffix empty when \(r=0\). Its minimum string-attractor cardinality equals \(q\). Every smallest attractor contains exactly one occurrence of each letter, and the following conditions classify *all* such attractors.

Index positions from zero, and write the uniquely chosen occurrence of \(a_j\) as \(p_j=j+qt_j\), where \(0\le t_j<m+\mathbf 1_{j<r}\). If \(m=1\) or \(r=q-1\), every such choice is a string attractor. If \(m\ge2\) and \(r\le q-2\), a choice fails to be an attractor **if and only if**
\[
 t_{q-1}=m-1,\quad t_r=0,\quad t_j\in\{0,m\}\quad(0\le j<r).
\]
In the latter case failure is witnessed by the single factor \(F_r=a_{q-1}a_0\cdots a_r\); in fact, meeting an occurrence of \(F_r\) is sufficient to hit every factor after the individual letters are hit.

The number \(A_q(m,r)\) of smallest attractors is consequently
\[
 A_q(m,r)=\begin{cases}
 2^r,&m=1,\\
 m(m+1)^{q-1},&m\ge2,\ r=q-1,\\
 (m+1)^r m^{q-r}-2^r m^{q-r-2},&m\ge2,\ 0\le r\le q-2.
 \end{cases}
\]
For \(m\ge2\), \(r\le q-2\), a uniformly chosen position for each symbol is a smallest attractor with probability \(1-m^{-2}(2/(m+1))^r\).

## Assumptions and scope
A string attractor is a subset \(\Gamma\) of text positions such that, for every distinct nonempty contiguous factor \(U\) of \(T\), at least one occurrence interval of \(U\) intersects \(\Gamma\). Occurrences may overlap. All choices and counts above refer to position *sets*, not occurrence tuples; because letters are distinct, they coincide for one-per-letter selections. The theorem allows all integers in the stated ranges, including the short-word and incomplete-final-period boundary cases. It does not assert a formula for arbitrary periodic words containing repeated letters.

## Proof
**Lower bound and candidate sets.** Every letter \(a_j\) occurs as a length-one factor, and their occurrence-position sets are disjoint. Therefore any attractor contains at least \(q\) positions. A size-\(q\) candidate necessarily consists of exactly one position \(p_j=j+qt_j\) for each \(j\). There are \((m+1)^r m^{q-r}\) candidates; it remains to identify those meeting all factors.

**Occurrences of a factor.** Fix a factor \(U\) of length \(\ell\), with first symbol \(a_s\) and last symbol \(a_e\). Since all letters within \(P\) are different, all occurrences start in residue class \(s\) modulo \(q\), at consecutive positions \(s,s+q,\ldots\) until the text ends. The final occurrence ends at the last position \(E\) in \(T\) congruent to \(e\) modulo \(q\). Thus \(E=qm+e\) when \(e<r\), and \(E=q(m-1)+e\) when \(e\ge r\). These formulas refer to factors which actually occur, so the indicated final start necessarily exists.

**Short factors.** Suppose \(\ell<q\). If the factor does not cross a period boundary, then \(s\le e\) and \(U=a_s\cdots a_e\). The chosen position \(p_e\) lies inside an occurrence of \(U\): an ordinary full period suffices if \(t_e<m\), while the final partial period suffices when \(t_e=m\), because then \(e<r\). If \(U\) crosses a boundary, \(s>e\). When \(e<r\), the occurrence crossing the boundary after the full period containing \(p_{q-1}\) exists, so \(p_{q-1}\) hits \(U\). When \(e\ge r\), the factor \(U\) contains \(F_r=a_{q-1}a_0\cdots a_r\), and each occurrence of \(F_r\) extends to an occurrence of \(U\) using the same period boundary. Therefore any candidate intersecting an occurrence of \(F_r\) also hits \(U\). If \(m=1\) and \(e\ge r\), no boundary-crossing occurrence of \(U\) exists; this last case is vacuous.

**Long factors.** Suppose \(\ell\ge q\). Successive occurrence intervals begin \(q\) positions apart and have length at least \(q\), so their union is the single interval \([s,E]\). Assume a candidate misses this union. The chosen position \(p_{q-1}\) is at least \(s\), so missing forces \(p_{q-1}>E\). If \(e<r\), then \(E=qm+e\), while \(p_{q-1}\le qm-1\), an impossibility. Thus \(e\ge r\), \(E=q(m-1)+e\), and necessarily \(e\le q-2\), \(t_{q-1}=m-1\). In particular \(r\le q-2\). Since the selected position for \(a_r\) is no larger than \(E\), missing also requires \(p_r<s\), hence \(t_r=0\) and \(r<s\). Likewise, for each \(j<r\), a selected position \(p_j\) outside \([s,E]\) must occur either in the first period (\(t_j=0\)) or in the appended suffix (\(t_j=m\)). These are precisely the displayed exceptional conditions. If \(m=1\), the inequality \(r<s\) and \(\ell\ge q\) would require a length-\(q\) occurrence starting at \(s>r\), impossible in a text of length \(q+r\). If \(r=q-1\), the inequality \(r\le q-2\) is impossible. Hence no candidate fails in those two regimes.

**One critical factor detects every failure.** Now take \(m\ge2\) and \(r\le q-2\). The factor \(F_r\) has exactly the \(m-1\) occurrences crossing complete-period boundaries numbered \(0,\ldots,m-2\). Their intervals together cover precisely \([q-1,\,q(m-1)+r]\). A chosen \(a_{q-1}\) lies outside this interval exactly when \(t_{q-1}=m-1\); a chosen \(a_r\) lies outside exactly when \(t_r=0\); and for \(0\le j<r\), the chosen position lies outside exactly when \(t_j=0\) or \(t_j=m\). Therefore the exceptional conditions are sufficient as well as necessary for failure. Conversely, when \(F_r\) is hit, all short factors are hit by the preceding argument, and a long factor cannot be missed since a missed long factor would force exactly these exceptional conditions. This gives the claimed equivalence.

**Existence and enumeration.** In each regime there is a successful one-per-letter candidate: when \(m\ge2\) and \(r\le q-2\), choose \(t_{q-1}=0\). Hence the minimum is exactly \(q\). For \(m=1\), exactly \(r\) letters occur twice, yielding \(2^r\) choices. For \(m\ge2\), \(r=q-1\), every choice is valid and their number is \(m(m+1)^{q-1}\). For the remaining case there are \((m+1)^r m^{q-r}\) candidates, and exactly \(2^r m^{q-r-2}\) exceptional ones: \(t_{q-1}\) and \(t_r\) are fixed, the \(r\) earlier ranks have two choices each, and the remaining \(q-r-2\) ranks have \(m\) choices each. Subtraction gives the formula and division by the candidate count gives the probability. \(\square\)

## Verification
Run `python3 check.py` in the directory containing the standalone companion checker. The checker computes all distinct factors and their full occurrence masks directly from each text, then tests every one-per-letter candidate against all factors. For every \(2\le q\le6\), \(1\le m\le4\), \(0\le r<q\), it independently checks the classification and exact total. There are \(80\) parameter cells and \(71{,}426\) checked candidate sets. The recorded run is in `check_output.txt`. The computation corroborates boundary handling but the proof above establishes the unrestricted theorem.

## Relationship to prior work
The directly motivating work of Banbara et al. [1] characterizes *all* smallest string attractors of Fibonacci, period-doubling, and Thue–Morse words. Those are different (nonperiodic recursive) families; the present theorem instead classifies every smallest attractor in each repeated-permutation prefix, for arbitrarily large alphabets and for every partial ending.

Mantaci et al. [2, Proposition 4] prove a general size bound for powers, \(\gamma(u)\le\gamma(u^n)\le\gamma(u)+1\). That inequality supplies neither the exact choice criterion nor the number of all minimum attractors. Dvořáková [3] gives minimum-cardinality information for certain episturmian factors, but no enumeration of all optimal position sets for this periodic-permutation family. An earlier published classification [4] proves the \(q=2,r=0\) case \(A_2(m,0)=m^2-1\) for \(m\ge3\); this binary complete-period case is **not claimed as new**. Our formula strictly encompasses it and handles all \(q\ge3\) and all partial-period boundaries.

Searches for all-smallest-attractor classifications, periodic/permutation word aliases, and complete pair criteria did not reveal a theorem covering the full parameterized result. The proof comparison uses statements and implications, not title matching; the lower-cardinality bound alone does not determine these counts.

## Limitations
The theorem concerns prefixes of a periodic permutation with no repeated letter in one period; it makes no statement about arbitrary periodic words or minimal attractors larger than \(q\). The binary full-period subcase already appears in [4]. A possibly differently phrased or unindexed earlier enumeration cannot be ruled out, and the finite checker cannot establish the all-parameter claim without the proof.

## References
1. M. Banbara, H. Bannai, P. Guo, D. Köppl, T. Mieno, and Y. Okamoto, “The Smallest String Attractors of Fibonacci, Period-Doubling, and Thue–Morse Words,” arXiv:2602.16152, first version 2026-02-18, https://arxiv.org/abs/2602.16152 .
2. S. Mantaci, A. Restivo, G. Romana, G. Rosone, and M. Sciortino, “String Attractors and Combinatorics on Words,” arXiv:1907.04660, 2019, https://arxiv.org/abs/1907.04660 .
3. L. Dvořáková, “String attractors of episturmian sequences,” arXiv:2211.01660, 2022, https://arxiv.org/abs/2211.01660 .
4. “All smallest attractors in two exceptional antipalindromic pseudostandard families,” 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-all-smallest-attractors-in-two-exceptional-antipalindromic-pseud--fe2566e0098c .
