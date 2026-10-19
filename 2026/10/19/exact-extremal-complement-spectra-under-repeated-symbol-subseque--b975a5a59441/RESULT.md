# Exact extremal complement spectra under repeated-symbol subsequence deletion

## Finding

Fix an alphabet \(\Sigma\) of size at least two, a distinguished letter \(a\in\Sigma\), and integers \(n\ge k\ge1\). For a length-\(n\) word \(w\) containing at least \(k\) copies of \(a\), let \(C(w,a^k)\) be the **set** of distinct words produced by deleting precisely \(k\) occurrences of \(a\), with different deletion-position choices giving the same result counted once. Define \(M(n,k)=\max_{w\in\Sigma^n,\,a^k\text{ subsequence of }w}|C(w,a^k)|\).

For each integer \(1\le r\le R=\min\{\lfloor(n+1)/2\rfloor,n-k+1\}\), set
\[
 m=n-r+1,\qquad t=\left\lfloor\frac mr\right\rfloor,\qquad s=m-rt,
 \qquad P_j(z)=1+z+\cdots+z^j.
\]
Then the **exact maximum for every \(n,k\)** is
\[
 \boxed{M(n,k)=\max_{1\le r\le R}[z^k]\,P_t(z)^{r-s}P_{t+1}(z)^s.}
\]
Here \([z^k]\) extracts the coefficient of \(z^k\). The value does not depend on \(|\Sigma|\) once \(|\Sigma|\ge2\). For every maximizing \(r\), the maximum is attained by a binary word consisting of \(r\) positive \(a\)-runs separated by single occurrences of a different letter \(b\), with \(r-s\) runs of length \(t\) and \(s\) runs of length \(t+1\) in any order.

More strongly, **at fixed number \(r\) of \(a\)-runs**, that balanced binary word coefficientwise dominates the entire deletion-count polynomial of every length-\(n\) word, simultaneously for every allowable number of deleted \(a\)'s.

In particular, the first nontrivial triple-symbol case has a closed form:
\[
\boxed{
M(n,3)=\begin{cases}
1,&n=3,\\
2,&n=5,\\
5,&n=7,\\
\binom{(n+1)/2}{3},&n\ge9\text{ odd},\\
\binom{n/2}{3}+n/2-1,&n\ge4\text{ even}.
\end{cases}}
\]

## Assumptions and scope

The deletion pattern is the single repeated letter \(a^k\), not an arbitrary fixed subsequence of length \(k\). The alphabet may contain more than two letters. Deletion histories are not distinguished: the object is a set of different remaining words, rather than a multiset of embeddings. No upper bound on \(n\) or \(k\), other than \(n\ge k\ge1\), is assumed. A source word is not required to use every symbol of the ambient alphabet.

## Proof

**1. Run polynomial is exact.** Write the word as alternating positive maximal \(a\)-runs of lengths \(x_1,\ldots,x_r\) and non-\(a\) separators (allowing other non-\(a\) letters, repeated separators, and non-\(a\) prefixes/suffixes). The ordered subsequence of all non-\(a\) letters is unchanged by the permitted deletions. Accordingly an output uniquely specifies the number of \(a\)'s retained between consecutive non-\(a\) letters, and hence uniquely specifies the number \(j_i\) removed from each positive run. Conversely every vector with \(0\le j_i\le x_i\) and \(\sum_{i=1}^r j_i=k\) produces one distinct output. Thus
\[
|C(w,a^k)|=[z^k]\prod_{i=1}^r P_{x_i}(z).
\]
This identity also applies with \(k=0\) when interpreting the constant coefficient.

**2. No wasted separators at an optimum with fixed \(r\).** If there are \(m_0=\sum_i x_i\) copies of \(a\), the other letters occupy at least \(r-1\) positions, so \(m_0\le n-r+1\). Increasing a run length never decreases any coefficient, because \(P_{j+1}(z)-P_j(z)=z^{j+1}\) has nonnegative coefficients. Therefore a coefficientwise upper bound is obtained by allocating a total \(m=n-r+1\) copies of \(a\) to \(r\) positive runs and using exactly one \(b\) between consecutive runs. Such words exist. The conditions \(m\ge r\) and \(m\ge k\) are precisely \(r\le\lfloor(n+1)/2\rfloor\) and \(r\le n-k+1\).

**3. Coefficientwise balancing.** For integers \(x\ge y+2\ge3\) the exact polynomial identity
\[
 P_{x-1}(z)P_{y+1}(z)-P_x(z)P_y(z)
     =z^{y+1}+z^{y+2}+\cdots+z^{x-1}
\]
has nonnegative coefficients. Multiplying by the unchanged factors preserves that property. Repeatedly transfer one \(a\) from any longer run to any shorter run whose length is at least two less. This process terminates because the sum of squares of the run lengths strictly decreases, and its final lengths are \(t=\lfloor m/r\rfloor\) and \(t+1\), with exactly \(s=m-rt\) longer runs. The resulting product coefficientwise dominates the original product. Together with Steps 1–2, this proves both the fixed-\(r\) assertion and the global maximum formula, including attainability for every parameter.

**4. Closed triple-deletion formula.** For fixed \(r\), let \(d=n-2r+1\ge0\) be the number of additional \(a\)'s beyond one per run in the canonical binary construction. When deleting three \(a\)'s, the possible distributions among the runs have types \((1,1,1)\), \((2,1)\), and \((3)\). Balance gives exactly
\[
 B(r,d)=\binom r3+(r-1)\min(r,d)+\min\{r,\max(0,d-r)\}
\]
different outcomes (with \(\binom r3=0\) for \(r<3\)). The global formula maximizes this expression over admissible \(r\).

Write \(n=2R-1+\varepsilon\), where \(\varepsilon\in\{0,1\}\) and \(R=\lfloor(n+1)/2\rfloor\). For \(r=R-h\) one has \(d=2h+\varepsilon\). When \(d\le r\),
\[
 B(r,d)=\binom r3+(r-1)d,
 \quad \binom R3-\binom r3=\sum_{j=r}^{R-1}\binom j2.
\]
For odd \(n\), \(\varepsilon=0\): if \(r\ge4\), the sum is at least \(h\binom r2\ge2h(r-1)\). When \(d>r\), use \(B(r,d)\le\binom r3+r^2\). If \(r\ge5\), then \(h>r/2\), so the sum is at least \(h\binom r2>r^2(r-1)/4\ge r^2\). The remaining \(r\le4\) cases have \(B(r,d)\le\binom r3+r^2\); for \(r=4,d>r\) necessarily \(R\ge7\), giving \(20<\binom73=35\), while \(r\le3\) gives at most \(10=\binom53\). Hence for all odd \(n\ge9\), \(r=R\) attains the maximum \(\binom R3\).

For even \(n\), \(\varepsilon=1\): the \(r=R\) value is \(\binom R3+R-1\). When \(d\le r\) and \(r\ge3\), the difference between this value and \(B(r,d)\) equals
\[
 \sum_{j=r}^{R-1}\binom j2-h(2r-3)
 \ge \frac{h(r-2)(r-3)}2\ge0.
\]
When \(d>r\) and \(r\ge5\), \(h\ge r/2\), so \(\sum_{j=r}^{R-1}\binom j2\ge r^2(r-1)/4\ge r^2\), which again suffices. For \(r=4,d>r\), \(R\ge6\) and \(B\le20<25=\binom63+5\); for \(r=3,d>r\), \(R\ge5\) and \(B\le10<14\). For \(r=2\), \(B\le4\), with the only borderline \(R=3\) giving \(B=3\), and \(r=1\) gives at most one. Direct evaluation handles \(n=4\). Finally, direct evaluation for odd \(n=3,5,7\) gives respectively \(1,2,5\). This proves the stated closed formula.

## Verification

The standalone files `verify.py` and `majorization_check.py` require only Python 3 standard library. Running `python3 verify.py` enumerates every binary word through length 12 and every ternary word through length 8; for every word and every eligible deletion count it explicitly enumerates deletion-position subsets and deduplicates the resulting words. It compares their maxima with the coefficient formula and verifies the closed triple-deletion expression for \(3\le n\le250\). Running `python3 majorization_check.py` enumerates all positive integer compositions of total \(a\)-run length at most 18 and checks the coefficientwise dominance inequality over all coefficients. Actual run results are recorded in `VERIFICATION.md`. These finite checks corroborate the exact all-parameter proof; they do not replace it.

## Relationship to prior work

Adamson, Fleischmann, and Huch introduced complement scattered factors \(C(w,u)\) and gave algorithms and structural results for singletons and other special patterns. Their Section 5 explicitly leaves upper bounds for \(|C(w,u)|\), or closed formulas in special cases, open. The present theorem supplies such an **exact extremal formula only for the natural repeated-symbol pattern** \(u=a^k\), together with a coefficientwise optimizer principle and a closed triple-deletion evaluation. It does not settle unrestricted \(u\). The earlier subsequence-counting algorithms of Torres-Jimenez and collaborators count embeddings of each subsequence, a different multiplicity-sensitive quantity; their result does not give the distinct-output extremum here. Vatter's recent log-concavity work concerns unrestricted distinct subsequences by length, likewise a different statistic.

## Limitations

No classification of every maximizer is claimed: balanced two-symbol witnesses are guaranteed, but different words may tie in a particular coefficient. There is no comparable formula here for an arbitrary nonconstant deletion pattern, no assertion about multiset-weighted outcomes, and no proof about asymptotic optimization in regimes where the deletion pattern itself varies. Scientific originality is assessed by comparison with identified literature and published indexed records; an unindexed earlier derivation remains possible. Independent scientific validation has not been performed.

## References

1. Duncan Adamson, Pamela Fleischmann, Annika Huch, **(Sets of) Complement Scattered Factors**, arXiv:2603.20790v1, posted March 21, 2026, especially Sections 3–5. https://arxiv.org/html/2603.20790v1
2. J. Torres-Jimenez, I. Izquierdo-Marquez, D. Ramirez-Acuna, R. Peralta, **A Near Optimal Algorithm to Count Occurrences of Subsequences of a Given Length**, Discrete Mathematics, Algorithms and Applications **9** (2017), 1750042, DOI:10.1142/S1793830917500422.
3. Vincent Vatter, **Log-concavity of subsequence counts of words**, arXiv:2608.22147, first posted August 23, 2026 (background on a distinct statistic).
