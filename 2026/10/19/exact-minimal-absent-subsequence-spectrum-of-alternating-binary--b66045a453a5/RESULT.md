# Exact minimal-absent-subsequence spectrum of alternating binary words

## Finding

Let \(W_m=(ab)^m\) for every integer \(m\ge1\), and let \(\mathcal M_m\) be the set of binary words absent as scattered subsequences of \(W_m\) but whose every proper subsequence is present. Define the terminal greedy-position statistic, for each nonempty binary word \(v=v_1\cdots v_k\), by
\[
L(v)=k+\mathbf 1_{\{v_1=b\}}+\sum_{i=1}^{k-1}\mathbf 1_{\{v_i=v_{i+1}\}}.
\]
Then \(v\in\mathcal M_m\) if and only if \(k\ge2\), its first two letters are not \(ab\), it contains no contiguous \(aba\) or \(bab\), and either \(L(v)=2m+1\), or \(L(v)=2m+2\) and the last two letters agree.

Write \(B_m(u)=\sum_{v\in\mathcal M_m}u^{|v|}\). Its complete length spectrum is
\[
B_m(u)=[z^{2m+1}]F(u,z)+u[z^{2m}]F(u,z),\qquad
F(u,z)=\frac{uz(1+z+uz^2)}{1-uz^2-u^2z^3}.
\]
In particular, \(M_m=B_m(1)\) has generating function
\[
\sum_{m\ge1}M_mx^m=\frac{3x-x^2+2x^3}{1-2x+x^2-x^3},
\]
and \(M_1=3\), \(M_2=5\), \(M_3=9\), with \(M_{m+3}=2M_{m+2}-M_{m+1}+M_m\) for \(m\ge1\). The first seven counts are \(3,5,9,16,28,49,86\).

## Assumptions and scope

The alphabet is exactly \(\{a,b\}\); subsequence means **scattered** (not necessarily contiguous) occurrence. In the definition of minimality, deleting any single letter must yield a subsequence; this is equivalent to requiring every proper subsequence to occur. The parameter \(m\) ranges over all positive integers. Formal coefficient extraction \([z^r]\) is in the ring of formal power series; \(u\) marks the length of a minimal absent word. No probability model or computational asymptotic assumption is required.

## Proof

**Greedy embedding.** Embed a nonempty word into the infinite alternating word \(abab\cdots\) by choosing each letter's first available occurrence. A leading \(a\) finishes at position \(1\), a leading \(b\) at position \(2\); an immediately opposite successor advances one position, while an equal successor advances two. Consequently the earliest possible terminal position is exactly \(L(v)\). Thus
\[
v\preceq W_m\quad\Longleftrightarrow\quad L(v)\le2m.
\]

**Deletion losses.** For \(k\ge2\), compare \(L(v)\) with the value after deleting one letter. Deleting the first letter decreases \(L\) by \(0\) exactly when the prefix is \(ab\), and decreases it by \(2\) otherwise. Deleting an interior letter decreases \(L\) by \(0\) exactly when it is the middle of \(aba\) or \(bab\), and by \(2\) otherwise: the difference is \(1+\mathbf1_{\{v_{i-1}=v_i\}}+\mathbf1_{\{v_i=v_{i+1}\}}-\mathbf1_{\{v_{i-1}=v_{i+1}\}}\). Deleting the final letter decreases \(L\) by \(1\) for unequal last letters and by \(2\) for equal last letters.

Every one-letter deletion must therefore lower \(L\) to at most \(2m\). Because each loss is at most \(2\), a minimal absent word has \(L\in\{2m+1,2m+2\}\). For \(L=2m+1\), zero losses are forbidden; for \(L=2m+2\), all losses must equal \(2\). This gives precisely the structural classification in the finding. Length-one candidates cannot be absent because both letters occur in \(W_m\).

**Run enumeration.** Give each word the weight \(u^{|v|}z^{L(v)}\). A constant run of length \(\ell\ge1\) contributes \(u^{\ell}z^{2\ell-1}\) to this weight, and an initial \(b\) contributes one further \(z\). Let
\[
S=\frac{uz}{1-uz^2},\qquad T=\frac{u^2z^3}{1-uz^2}
\]
be the generating functions for a nonempty run and a run of length at least two. Avoiding \(aba\) and \(bab\) means all **internal** runs have length at least two; avoiding initial \(ab\) means a word beginning with \(a\) and having at least two runs must also have a first run of length at least two. Words beginning with \(a\) contribute \(S/(1-T)\); those beginning with \(b\) contribute \(zS+zS^2/(1-T)\). Summing and reducing gives
\[
F(u,z)=\frac{S}{1-T}+zS+\frac{zS^2}{1-T}
=\frac{uz(1+z+uz^2)}{1-uz^2-u^2z^3}.
\]

Let \(H\) count the same allowed words with equal final two letters. Removing one final letter from such a word, or appending a copy of the final letter to an arbitrary nonempty allowed word, is a bijection and multiplies the weight by \(uz^2\). Hence \(H=uz^2F\). The first alternative in the structural classification contributes \([z^{2m+1}]F\), and the second contributes \([z^{2m+2}]H=u[z^{2m}]F\), proving the bivariate spectrum.

**Univariate recurrence.** At \(u=1\), \(F(1,z)=z(1+z+z^2)/(1-z^2-z^3)\). Define \(d_n=[z^n]F(1,z)\), so \(d_0=0\), \(d_1=d_2=1\), \(d_3=2\), and \(d_n=d_{n-2}+d_{n-3}\) for \(n\ge4\). The total count is \(M_m=d_{2m}+d_{2m+1}\). The characteristic polynomial of the \(d_n\) recurrence is \(r^3-r-1\); for any root \(r\), its square satisfies \((r^2)^3-2(r^2)^2+r^2-1=0\), by \(r^3=r+1\). As the cubic has three distinct roots, each even/odd subsequence, and hence \(M_m\), satisfies \(M_{m+3}-2M_{m+2}+M_{m+1}-M_m=0\). The initial counts \(3,5,9\) yield the displayed rational ordinary generating function.

## Verification

The included standalone `checker.py` independently tests subsequence membership by scanning \(W_m\), checks minimality by deleting every position, and compares the result for every candidate binary word of length at most \(2m+2\) for each \(1\le m\le7\). It separately computes coefficients of the bivariate rational series and checks the refined length counts and total recurrence. Run `python3 checker.py` from the package directory and compare standard output with `computation.txt`. All assertions passed in the recorded computation. The finite tests corroborate, but do not establish, the statements for unbounded \(m\); the preceding proof establishes them.

## Relationship to prior work

Manea, Ringleb, Siemer, and Winkler (2025) develop optimal algorithms enumerating all minimal absent subsequences of a general string, including a DAG representation; Kosche, Koß, Manea, and Siemer develop general characterizations and algorithms; Adamson and coauthors study bounds and counting for absent subsequences. Those generic results are compatible with, but do not explicitly provide, the length-refined exact closed series for the particular infinite alternating family and the resulting three-term total-count recurrence. The exact series and recurrence here are the claim under review, not the elementary definitions or general algorithms.

## Limitations

The formulas apply to alternating binary strings of even length and count **minimal absent subsequences**, not shortest absent subsequences or absent contiguous substrings. They do not assert the same sequence for arbitrary periodic inputs. The review is a literature comparison rather than an independent audit; an earlier equivalent formula in unindexed or inaccessible work remains possible. A relevant 2023 chapter on absent subsequence problems was not available for full-text inspection, so no non-coverage conclusion is drawn from its abstract.

## References

1. F. Manea, T. Ringleb, S. Siemer, and M. Winkler, *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471 (initial public release 2025-04-30).
2. M. Kosche, T. Koß, F. Manea, and S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968; *Fundamenta Informaticae*.
3. D. Adamson, P. Fleischmann, A. Huch, and M. Wiedenhöft, *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599.
4. Z. Troníček, *On Problems Related to Absent Subsequences*, 2023, DOI:10.1007/978-3-031-49614-1_26 (abstract inspected; full text unavailable).
