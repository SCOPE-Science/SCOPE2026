# A two-insertion moment separates all three-run binary subsequence patterns

## Finding

A binary pattern \(p\) is **strongly Wilf-equivalent** to a pattern \(q\) when, for every host length \(n\geq0\) and every \(k\geq0\), exactly as many binary host words of length \(n\) contain \(p\) as a scattered subsequence \(k\) times as contain \(q\) that many times. A pattern's *runs* are its maximal constant-letter blocks.

**Theorem.** If \(p\) has at most three runs, a binary word \(q\) is strongly Wilf-equivalent to \(p\) **if and only if** \(q\) is obtained from \(p\) by reversal, bit complementation, or their composition. In particular, Conjecture 5.2 of Menon--Singh holds for this entire infinite subclass, even when \(q\) is not assumed to have three runs beforehand.

The separation is determined by the occurrence-count distribution at only two host lengths, \(\ell+1\) and \(\ell+2\), where \(\ell=|p|\). More explicitly, for positive integers \(a,b,c\), let \(p=1^a0^b1^c\) and let \(X_p(w)\) be its number of subsequence embeddings into \(w\). Define

\[
T(a,b,c)=\sum_{w\in\{0,1\}^{a+b+c+2}}X_p(w)^2.
\]

Writing \(\ell=a+b+c\) and \(r=(a,b,c)\), its exact closed form is

\[
\begin{aligned}
T(a,b,c)={}&4\binom{\ell+2}{2}
+2(\ell+2)\sum_{i=1}^3r_i(r_i+1)
+6\sum_{i=1}^3\binom{r_i+2}{4}\\
&+4\sum_{1\leq i<j\leq3}\binom{r_i+1}{2}\binom{r_j+1}{2}
+2(ab+bc+ac)-2ac\,\mathbf 1_{\{b\geq2\}}.
\end{aligned}
\]

All terms except the final correction are symmetric in the three run lengths. For example, three inequivalent patterns with run lengths \(\{1,2,3\}\), putting the middle run at lengths \(1,2,3\) respectively, have second-moment values \(598,592,594\) at host length \(8\).

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), positions are linearly ordered, embeddings are strictly increasing index sequences, and the length of the host can be arbitrary. A word having \(k\) embeddings contributes once to the \(k\)-th occurrence-frequency class, not \(k\) times. The theorem applies to every nonempty binary pattern having one, two, or three maximal runs; no restriction on their positive lengths is imposed. Binomial coefficients with a lower index exceeding the upper are zero. The computational tests stated below are finite checks and do not substitute for the all-length combinatorial argument.

## Proof

**Step 1: extract the unordered run multiset.** Let \(B_{n,p}(k)\) denote the number of \(n\)-letter words with exactly \(k\) embeddings of \(p\). Menon--Singh, Lemma 3.6, proves that for any \(k\geq2\), \(B_{\ell+1,p}(k)\) equals the number of runs of length \(k-1\) in \(p\). Equality of all frequency distributions therefore forces the two patterns to have the same multiset of run lengths, in particular the same number of runs. For one or two runs, this already fixes the run composition up to reversal. Complementation fixes the initial bit.

**Step 2: count the second moment by two omitted pairs.** Assume three runs and, by complementation, take \(p=1^a0^b1^c\). Set \(n=\ell+2\). Each embedding \(p\hookrightarrow w\) is specified by an omitted two-element set \(A\subseteq[n]\) and the prescribed values \(p_1,\ldots,p_\ell\) at the other positions. Expanding the square and summing over hosts, an ordered pair \((A,B)\) contributes zero if the two prescriptions disagree and otherwise contributes exactly \(2^{|A\cap B|}\); the positions omitted by both embeddings are free binary letters.

If \(A=B\), the contribution is \(4\binom n2\). If \(|A\cap B|=1\), choose the common omitted position in \(n\) ways. After suppressing that position, the two remaining distinct one-letter omissions must occupy the same constant run. A run of length \(r\) has \(r+1\) possible single-omission positions, giving \(r(r+1)\) ordered pairs of different omissions. With the factor \(2\) for the common free symbol, this part contributes \(2n\sum_i r_i(r_i+1)\).

For disjoint omitted sets, list their union in increasing order as \(h_1<h_2<h_3<h_4\), and label each position by \(A\) or \(B\), with two of each label. Compatibility can be checked exactly: for every \(t\notin A\cup B\), the two prescribed letters must satisfy

\[
p_{t-\#\{s\in A:s<t\}}=p_{t-\#\{s\in B:s<t\}},
\]

with one-based indices. Between consecutive holes the two subscripts differ by zero, one, or two. Inspecting the three constant runs, the six possible ordered hole-label shapes give this complete classification:

| Hole-label shape | Number of compatible four-position choices |
|---|---|
| \(AABB\), \(BBAA\) | \(U=\sum_i\binom{r_i+2}{4}+ab+bc+ac\mathbf1_{\{b=1\}}\) each |
| \(ABAB\), \(BABA\), \(ABBA\), \(BAAB\) | \(V=\sum_i\binom{r_i+2}{4}+\sum_{i<j}\binom{r_i+1}{2}\binom{r_j+1}{2}\) each |

Here is a direct way to reconstruct the table without assuming any spectral or asymptotic lemma. Track the difference \(\#\{A\text{-holes before }t\}-\#\{B\text{-holes before }t\}\) as each of the four labels is crossed. For an alternating or nested shape, every nonzero interval forces equality of adjacent source letters. The two intervals either both lie inside one constant run, counted by \(\binom{r_i+2}{4}\), or lie in two different runs, counted by \(\binom{r_i+1}{2}\binom{r_j+1}{2}\). For a blocked shape, the offset instead follows \(0,1,2,1,0\) (up to sign): a compatible choice can be internal to one run, cross exactly one of the two run boundaries in \(ab\) or \(bc\) ways, or cross both boundaries in \(ac\) ways **only when the middle run is a singleton**. In that exceptional case the offset-two equality compares the two equal outer letters across the singleton. All other placements violate the displayed equality at the first crossed boundary. This accounts for every four-position choice, including runs of length one.

Disjoint omitted pairs have no free host letters, so the disjoint contribution is \(2U+4V\). Adding all three cases gives

\[
T=4\binom n2+2n\sum_i r_i(r_i+1)+2U+4V,
\]

which simplifies to the stated formula because \(2(ab+bc)+2ac\mathbf1_{\{b=1\}}=2(ab+bc+ac)-2ac\mathbf1_{\{b\geq2\}}\).

**Step 3: recover the middle run.** Once the unordered multiset \(\{a,b,c\}\) is known, every term in \(T\) but \(-2ac\mathbf1_{\{b\geq2\}}\) is fixed. If \(b=1\), that correction is zero, whereas it is strictly negative for any other middle length. If \(b\geq2\), its magnitude equals \(2abc/b\). For fixed positive product \(abc\), different choices of \(b\) give different magnitudes. Thus \(T\) uniquely determines the middle length. The outer two lengths are then determined as an unordered pair, which is exactly the remaining reversal ambiguity. Reversal and bit complementation indeed preserve each occurrence-frequency distribution by the corresponding bijection on host words. This proves both implications.

## Verification

The included standard-library `verify.py` independently expands ordered pairs of omitted positions and checks the six shape contributions for all \(216\) triples \((a,b,c)\) with \(1\leq a,b,c\leq6\). It also computes subsequence counts directly by a dynamic program over every binary host word of length \(\ell+2\), for all \(81\) triples in that range with \(\ell\leq9\). Both agree with the exact formula; execution prints `VERIFY_OK`. These exhaustive checks cover only their stated finite domains. The infinite result follows from the compatibility classification and run-multiset argument above.

## Relationship to prior work

Menon and Singh introduced this occurrence-frequency framework, proved the run-multiset invariant (their Lemma 3.6), and posed the classification as Conjecture 5.2. Their full accessible 2023 preprint discusses patterns with at most three runs for *maximal occurrences* and for internal zeros, but not the present second-moment separation theorem. Roger Tian's accessible 2025 manuscript gives a general occurrence-computation formula and word-construction algorithms but not a three-run equivalence classification. Janson and Szpankowski study random hidden-pattern statistics and asymptotic normality, a different host-length regime. Glenn Bruda's publicly available 2026 article studies eventual polynomial dependence on host length for fixed occurrence count and an upper bound on occurrences; it does not assert this classification. The present theorem uses one finite, small-host moment to separate entire strong-Wilf classes, rather than calculating \(B_{n,p}(k)\) for all \(n,k\).

## Limitations

This resolves the conjecture only for patterns with at most three runs. Neither four-or-more-run classes nor other alphabets are classified. The moment formula concerns the **raw second moment summed across all hosts**, not a variance normalized by a random-host distribution. A comprehensive global priority guarantee is not claimed: an unindexed equivalent or unpublished result might exist. The finite verifier is corroboration, not a proof of the universal quantifiers.

## References

- K. Menon and A. Singh, *Subsequence frequency in binary words*, arXiv:2306.07870v1 (first public 13 June 2023), especially Lemma 3.6 and Conjecture 5.2. https://arxiv.org/html/2306.07870v1
- G. Bruda, *Enumerating binary words restricted by subsequence frequency*, arXiv:2607.02578 (first public 30 June 2026), Sections 1--4. https://arxiv.org/abs/2607.02578
- R. Tian, *Counting occurrences of a pattern in a binary word*, arXiv:2507.03205v1 (3 July 2025), Sections 4--6. https://arxiv.org/html/2507.03205v1
- S. Janson and W. Szpankowski, *Hidden Words Statistics for Large Patterns*, arXiv:2003.09584v1 (21 March 2020), Sections 1--3. https://arxiv.org/html/2003.09584v1
