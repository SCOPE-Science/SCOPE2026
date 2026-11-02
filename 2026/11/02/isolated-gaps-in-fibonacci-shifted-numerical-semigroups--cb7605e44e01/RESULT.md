# Isolated gaps in Fibonacci-shifted numerical semigroups

## Finding
Let \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\). For each integer \(a\ge5\), set \(m=F_a\) and
\[
S_a=\langle F_a+F_j:j\ge0\rangle
=\langle m,m+F_2,\ldots,m+F_{a-1}\rangle.
\]
An *isolated gap* is a positive integer \(g\notin S_a\) with \(g-1,g+1\in S_a\). Let \(\mathcal I_a\) be the subsets of \(\{6,7,\ldots,a-1\}\) containing no consecutive indices (the empty set is permitted). Then **all** isolated gaps are, without repetition,
\[
\boxed{g_I=(1+|I|)F_a+F_2+F_4+\sum_{j\in I}F_j\quad(I\in\mathcal I_a).}
\]
In particular, their number is exactly \(F_{a-4}\). More precisely, for every integer \(k\ge0\), the number satisfying \(\lfloor g/F_a\rfloor=k+1\) is
\[
\boxed{\binom{a-5-k}{k}},
\]
where this is zero unless \(0\le k\le\lfloor(a-5)/2\rfloor\). The largest isolated gap equals the Frobenius number \(\mathrm F(S_a)\) when \(a\) is odd, and equals \(\mathrm F(S_a)-3\) when \(a\) is even. Here the known formula \(\mathrm F(S_a)=\lfloor(a-1)/2\rfloor F_a-1\) is used only for the last comparison.

## Assumptions and scope
All semigroups are additive submonoids of the nonnegative integers. The number \(a\) is an arbitrary integer at least five; the theorem is not an asymptotic statement. A Zeckendorf expansion of \(r\ge0\) is the unique sum of nonconsecutive Fibonacci numbers \(F_j\) with indices \(j\ge2\). Write \(J(r)\) for its set of indices and \(\beta(r)=|J(r)|\). Define \(\beta(0)=0\). A binomial coefficient with an inadmissible nonnegative selection size is interpreted as zero.

The theorem concerns isolated *missing integers*, not pseudo-Frobenius numbers or the genus. The excluded small parameters have distinct boundary behavior: \(S_3=\langle2,3\rangle\) has isolated gap \(1\), whereas \(S_4=\langle3,4,5\rangle\) has none.

## Proof
**1. Membership thresholds from the established Apéry formula.** Robles-Pérez and Rosales proved that for each \(0\le r<m\), the smallest element of \(S_a\) congruent to \(r\pmod m\) is \(w(r)=m\beta(r)+r\) (their Theorem 4.6). Consequently, for every integer \(q\ge0\),
\[
qm+r\in S_a\quad\Longleftrightarrow\quad q\ge\beta(r).
\]
In particular, no multiple of \(m\) is a gap.

**2. An isolated gap must sit immediately below its residue threshold.** Suppose \(1\le r\le m-2\) and \(g=qm+r\). The three necessary and sufficient conditions for isolation are
\[
q<\beta(r),\qquad q\ge\beta(r-1),\qquad q\ge\beta(r+1).
\]
For \(r=m-1\), the last inequality is omitted, because \(g+1=(q+1)m\in S_a\). The summand-minimality of Zeckendorf expansions gives \(\beta(r)\le\beta(r-1)+1\) by adding \(F_2=1\) to a representation of \(r-1\). Thus the inequalities force \(q=\beta(r)-1\). We are left with \(\beta(r)>\beta(r-1)\), plus \(\beta(r)>\beta(r+1)\) whenever \(r<m-1\).

**3. Characterizing the rise on the left.** If \(2\in J(r)\), subtracting one simply deletes its \(F_2\) summand, so \(\beta(r-1)=\beta(r)-1\). Conversely, if \(2\notin J(r)\), write \(j\ge3\) for the smallest index in \(J(r)\). Replacing the term \(F_j\) with the Zeckendorf expansion of \(F_j-1\) gives the expansion of \(r-1\): the next selected index in \(J(r)\), if present, is at least \(j+2\), while all replacement indices are at most \(j-1\), so the two blocks do not interfere. Since \(F_j-1\) has at least one summand for \(j\ge3\), we have \(\beta(r-1)\ge\beta(r)\). Therefore
\[
\beta(r)>\beta(r-1)\quad\Longleftrightarrow\quad 2\in J(r).
\]

**4. Characterizing the fall on the right.** Assume \(2\in J(r)\). If \(4\notin J(r)\) and \(r\le m-2\), the equality \(2F_2=F_3\) shows that the Zeckendorf expansion of \(r+1\) is obtained by replacing its \(F_2\) with \(F_3\). All remaining indices are at least five, so the new indices are nonconsecutive and \(\beta(r+1)=\beta(r)\). If instead \(4\in J(r)\), use
\[
2F_2+F_4=F_5.
\]
Adding one and replacing those three terms with one term expresses \(r+1\) using \(\beta(r)-1\) Fibonacci summands. Summand-minimality implies \(\beta(r+1)\le\beta(r)-1\). Hence, for \(1\le r\le m-2\), the two strict-neighbor conditions hold exactly when \(2,4\in J(r)\).

For the terminal residue \(r=m-1\), the standard alternating expansion \(F_a-1=F_{a-1}+F_{a-3}+\cdots\) ends in \(F_2\) if \(a\) is odd and in \(F_3\) if \(a\) is even. In the former case \(a\ge5\) and it contains both \(F_2,F_4\); in the latter it contains no \(F_2\). Thus the same criterion covers the terminal residue. We have proved that precisely those residues with \(2,4\in J(r)\) yield isolated gaps, each with \(q=\beta(r)-1\).

**5. Complete enumeration.** If \(2,4\in J(r)\), nonconsecutiveness forces index three and index five to be absent. The remaining indices form an arbitrary independent subset \(I\subseteq\{6,\ldots,a-1\}\). Conversely, every such subset, adjoined to \(\{2,4\}\), is a valid Zeckendorf expansion of a residue \(r<m\). Since \(\beta(r)=2+|I|\), the displayed formula for \(g_I\) follows. Different subsets give distinct residues by Zeckendorf uniqueness.

There are \(a-6\) positions available when \(a\ge6\), and independent subsets of a path on \(n\) vertices are counted by \(F_{n+2}\); the case \(a=5\) has the single empty subset. Thus \(|\mathcal I_a|=F_{a-4}\) for every \(a\ge5\). The number of size-\(k\) independent subsets on \(a-6\) consecutive positions is \(\binom{a-5-k}{k}\), proving the level formula.

Finally, if \(a\) is odd, the rightmost maximally large independent subset is \(I=\{6,8,\ldots,a-1\}\), which yields \(r=m-1\) and hence \(g_I=\mathrm F(S_a)\). If \(a\) is even, the rightmost maximum-cardinality choice is \(I=\{7,9,\ldots,a-1\}\) (empty for \(a=6\)), which gives \(r=m-4\) and \(g_I=\mathrm F(S_a)-3\). Since a higher quotient by \(m\) dominates all lower quotients, these choices maximize \(g_I\). This completes the proof.

## Verification
The standalone pure-Python program `verify.py` independently constructs semigroup membership by forward dynamic programming, computes Apéry representatives by a shortest-path algorithm, evaluates Zeckendorf digit counts, and compares the *entire* set of isolated gaps with the formula. It covers each integer parameter \(3\le a\le22\) and checks 435,045 membership decisions, including the two small boundary cases. It additionally checks each binomial level count. Run with `python3 verify.py`; no packages beyond the Python standard library are required. These finite calculations are supporting tests; the preceding argument proves the unrestricted statement for all \(a\ge5\).

## Relationship to prior work
The Apéry formula and Frobenius value of the family are due to Robles-Pérez and Rosales (arXiv:2210.00816, first posted 3 October 2022). A later paper on shifted \(r\)-Fibonacci semigroups explicitly classifies their pseudo-Frobenius elements and types (Arabian Journal of Mathematics, DOI 10.1007/s40065-025-00513-3, Section 10). Those results are acknowledged; pseudo-Frobenius elements are a different statistic from isolated gaps. Moreno-Frías and Rosales study isolated gaps and perfect semigroups in arXiv:2305.14967, but their general covariety results do not state this Fibonacci-family classification. The present statement converts the established Zeckendorf Apéry description into a complete, closed Fibonacci count and an exact level distribution for isolated gaps. A general membership algorithm for a semigroup can, of course, enumerate its finite gaps; the claim is the symbolic classification, not mere computability.

## Limitations
The result applies only to the specified Fibonacci-shifted family and to isolated gaps, not to arbitrary numerical semigroups or other gap-pattern statistics. The proof uses the established Apéry theorem rather than reproving it. The closed formula may be implicit in other work on Zeckendorf summand counts or numerical-semigroup gaps; no independent external scientific review has been performed. The computational checks through \(a=22\) alone do not establish the infinite result.

## References
1. A. M. Robles-Pérez and J. C. Rosales, *The extended Frobenius problem for Fibonacci sequences incremented by a Fibonacci number*, arXiv:2210.00816 (first version 2022-10-03), particularly Theorem 4.6 and Theorem 5.6; https://arxiv.org/abs/2210.00816.
2. M. Á. Moreno-Frías and J. C. Rosales, *The covariety of perfect numerical semigroups with fixed Frobenius number*, arXiv:2305.14967 (2023-05-24), subsequently *Czechoslovak Mathematical Journal* 74 (2024), 697–714; https://arxiv.org/abs/2305.14967.
3. *The extended Frobenius problem for r-Fibonacci sequences shifted by r-Fibonacci numbers*, *Arabian Journal of Mathematics* (2025), DOI 10.1007/s40065-025-00513-3, especially Section 10; https://link.springer.com/article/10.1007/s40065-025-00513-3.
