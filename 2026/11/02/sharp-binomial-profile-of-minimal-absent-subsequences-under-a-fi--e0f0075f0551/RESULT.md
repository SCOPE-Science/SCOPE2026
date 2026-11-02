# Sharp binomial profile of minimal absent subsequences under a fixed letter count

## Finding

Let \(w\) be any finite word over the fixed binary alphabet \(\{0,1\}\), containing exactly \(k\ge1\) occurrences of \(1\). A *minimal absent subsequence* (MAS) is a word \(v\) that is not a scattered subsequence of \(w\), although every word obtained by deleting a single position of \(v\) is a subsequence of \(w\). Denote by \(M_r(w)\) the number of distinct MAS having exactly \(r\) occurrences of \(1\).

**Theorem.** For all integers \(r\),
\[
0\le M_r(w)\le \binom{k+1}{r},
\]
where the binomial coefficient is interpreted as zero outside \(0\le r\le k+1\). The one family
\[
w_k=(010)^k
\]
simultaneously attains equality for every \(r\in\{0,1,\ldots,k+1\}\). Consequently, the sharp total number of distinct minimal absent subsequences among all such words is
\[
\max_{|w|_1=k}|\operatorname{MAS}(w)|=2^{k+1}.
\]
The bound is independent of the number of zeros in \(w\). It concerns **minimal** absent scattered subsequences, not absent substrings or shortest absent subsequences.

## Assumptions and scope

Words are finite, the ambient alphabet is exactly \(\{0,1\}\), and scattered-subsequence embedding respects order but need not use adjacent positions. The two symbols remain admissible as patterns even if one does not appear in \(w\). Occurrences and MAS are counted as distinct **words**, not as embeddings. Minimality is equivalent to the requirement that every one-position deletion embeds: any proper subsequence is below one of these deletions. Every MAS has at most \(k+1\) ones: a word with at least \(k+2\) ones remains absent after deleting **any** single position, contradicting minimality.

Write
\[
w=0^{a_0}1\,0^{a_1}1\cdots1\,0^{a_k},\qquad a_j\ge0.
\]
The \(i\)-th source one has *one-index* \(i\in\{1,\ldots,k\}\). For an existing subsequence, its *greedy embedding* matches each successive letter at the earliest possible source position.

## Proof

### 1. An injective encoding of all minimal absences

Let \(v\) be an MAS, and let \(t\in\{0,1\}\) be its final letter. The proper prefix \(v^-\), obtained by deleting that final letter, embeds greedily in \(w\). Record the strictly increasing one-indices
\[
I(v)=(i_1<\cdots<i_s)
\]
of the source ones matched by this embedding. Since \(v^-\) has \(s\) ones, the full word \(v\) has \(s+\mathbf1_{\{t=1\}}\) ones. We claim that \(v\) is uniquely determined by the pair \((I(v),t)\).

To see this, express \(v\) as
\[
v=0^{b_0}1\,0^{b_1}1\cdots1\,0^{b_s}t.
\]
For each block preceding a matched one, its zero count is forced by the selected one-indices. Before the first matched one, \(b_0=0\) if \(i_1=1\); otherwise
\[
b_0=1+\sum_{h=0}^{i_1-2}a_h.
\]
Between two consecutive selected ones \(i_j,i_{j+1}\), the count is \(b_j=0\) if \(i_{j+1}=i_j+1\); otherwise
\[
b_j=1+\sum_{h=i_j}^{i_{j+1}-2}a_h.
\]
Indeed, a positive block that precedes some selected source one must contain precisely one more zero than can be read before the **previous** source one. Fewer zeros would select an earlier one. More zeros would not be minimal: after deleting one zero from that block, the same source one would still be selected, and the unchanged remainder would still fail to embed. This uses the defining greedy property and single-position deletion minimality. If there is no earlier source one available, the block must instead be empty. These assertions also handle zero-length source gaps.

The final block is likewise determined. If \(t=0\), the prefix \(v^-\) must consume **all** zeros after the final selected source one, so
\[
b_s=\sum_{h=i_s}^{k}a_h
\]
when \(s\ge1\), or \(b_0=\sum_{h=0}^ka_h\) when \(s=0\). One additional terminal zero is absent. If \(t=1\), and the last selected source one is not the \(k\)-th, the zero count must be one greater than the zeros available before the final source one:
\[
b_s=1+\sum_{h=i_s}^{k-1}a_h.
\]
For \(s=0\), this means \(b_0=1+\sum_{h=0}^{k-1}a_h\). If \(s\ge1\) and \(i_s=k\), it instead forces \(b_s=0\): a positive final zero block could be shortened without making another one available, contradicting minimality. In every case the reconstruction is unique.

Thus \(v\mapsto(I(v),t)\) is injective. If \(v\) has \(r\) ones, there are at most \(\binom{k}{r}\) possibilities with \(t=0\) and \(\binom{k}{r-1}\) with \(t=1\). Pascal's identity proves
\[
M_r(w)\le\binom{k}{r}+\binom{k}{r-1}=\binom{k+1}{r}.
\]
This includes \(r=0\), \(r=k+1\), and the empty selected set.

### 2. A witness realizing every possible code

Fix \(k\ge1\) and put \(w_k=(010)^k\). Its zero runs have lengths \(a_0=a_k=1\) and \(a_j=2\) for \(1\le j<k\). Choose any subset \(I=(i_1<\cdots<i_s)\) of \(\{1,\ldots,k\}\) and choose \(t\in\{0,1\}\). Construct a word
\[
v(I,t)=0^{b_0}1\,0^{b_1}1\cdots1\,0^{b_s}t
\]
by the explicit rules
\[
\begin{aligned}
b_0&=2(i_1-1) && (s\ge1),\\
b_j&=\begin{cases}0,&i_{j+1}=i_j+1,\\2(i_{j+1}-i_j)-1,&i_{j+1}>i_j+1,\end{cases}&&(1\le j<s),\\
b_s&=2(k-i_s)+1 && (s\ge1,\ t=0),\\
b_s&=\begin{cases}0,&i_s=k,\\2(k-i_s)+1,&i_s<k,\end{cases}&&(s\ge1,\ t=1).
\end{aligned}
\]
For the empty set \(I\), use \(b_0=2k\), with either choice of \(t\). Notice that when \(t=0\) the final zero is **in addition to** the \(b_s\) zeros; in particular \(v(\varnothing,0)=0^{2k+1}\).

Greedy embedding of \(v(I,t)^-\) matches precisely the selected source one-indices \(I\). A gap of \(d\ge2\) between selected ones requires \(2d-1\) zeros: this skips the intervening source ones and stops just before the desired one. An adjacent selection requires no zeros. The terminal letter cannot be matched: for \(t=0\), its prefix has already consumed the available final zeros; for \(t=1\), it has either consumed the zero immediately after the last source one or already matched the last source one.

We next check minimality, not merely absence. Deleting any zero from a positive *nonfinal* block changes the next greedy one-index from \(i_j\) to \(i_j-1\); all subsequent selected one-indices can shift down by one, leaving enough zeros or an additional source one for the terminal letter. This follows directly from the \(2d-1\) gap formula; in the initial block the relevant transition is from \(2(i_1-1)\) to \(2(i_1-1)-1\). Deleting a zero from the final block makes the terminal letter embeddable, by its defining threshold. For \(t=0\), deleting the terminal zero itself simply leaves the greedily embeddable prefix.

Deleting a selected target one merges its two adjacent zero blocks. Keep earlier selected source one-indices and shift every later selected index down by one. The merged count fits before the newly chosen next one: if the preceding selected one has index \(p\ge1\) and the following selected one has index \(q\), the available zeros between source indices \(p\) and \(q-1\) number \(2(q-p-1)\), and the merged count is at most that quantity. When there is no preceding selected one, the available zeros before source index \(q-1\) number \(2q-3\), again at least the merged count. If the deleted one was last, the final two zero blocks fit either among all remaining zeros (for \(t=0\)) or before the last source one (for \(t=1\)); explicitly, with preceding index \(p\ge1\), their counts, including the terminal zero when applicable, are at most \(2(k-p)+1\) for \(t=0\) and at most \(2(k-p)\) for \(t=1\). With no preceding selected one, they are at most \(2k\) zeros and \(2k-1\) zeros, respectively. All later unmerged gaps are unchanged under a uniform index shift. Therefore the word resulting from any single-one deletion also embeds.

Every \(v(I,t)\) is consequently a minimal absent subsequence. Different choices of \((I,t)\) give different words, because their greedy selected one-indices and terminal letters are recoverable. There are \(\binom{k}{r}\) choices with \(t=0\), \(s=r\), and \(\binom{k}{r-1}\) with \(t=1\), \(s=r-1\). Hence \(M_r(w_k)=\binom{k+1}{r}\) simultaneously for all \(r\), completing the proof. Summing these counts gives \(2^{k+1}\).

## Verification

The standalone Python 3 program `verify.py` uses two separate finite mechanisms. Its first enumerates all distinct subsequences of each binary word of lengths \(1\) through \(11\), generates one-letter minimal extensions, and checks the binomial inequality and the injective reconstruction for **4094 input words**. Its second independently constructs every \(v(I,t)\) for \(w_k\), for \(1\le k\le9\), and directly checks absence, every single-position deletion, distinctness, and the complete Pascal-triangle multiplicity profile. For \(k\le3\), it also compares the constructed set against full brute-force MAS enumeration. Running `python verify.py` terminates with `VERIFY_OK binary_words=4094 witness_k=1..9 canonical_injection=checked`.

These finite checks test the formulas and boundary cases but do **not** substitute for the all-integer proof above.

## Relationship to prior work

Kosche, Koß, Manea and Siemer introduced and studied minimal and shortest absent subsequences and proved a general canonical greedy-embedding characterization (Theorem 3.1 of *Absent Subsequences in Words*). That characterization motivates the present injection, but the explicit sharp minority-letter bound, its full fixed-one-count profile, and the single family simultaneously realizing every layer are separate statements not supplied by that characterization. The same work demonstrates exponential MAS families over larger alphabets; those length/alphabet examples do not give the present fixed-count bound.

Adamson, Fleischmann, Huch, Manea, Sarnighausen-Cahn and Wiedenhöft study extrema of **all absent subsequences of a prescribed length** at fixed subsequence-universality index, which does not count minimal absent subsequences by occurrences of a designated symbol. Manea, Ringleb, Siemer and Winkler develop optimal **enumeration algorithms** for MAS and longest-MAS computation, rather than this parameter-sensitive extremal profile. The closest indexed research records on shortest absent subsequences and subsequence universality concern different invariants. These distinctions are by mathematical implication and quantified parameters, not by title alone.

## Limitations

The result is specific to a binary alphabet, the count of one designated source letter, and minimal absent **scattered subsequences**. It does not assert an analogue for arbitrary larger alphabets, enumerate all extremizers, determine MAS lengths, or bound all absent (nonminimal) subsequences. The source-length dependence disappears only in the stated *cardinality upper bound*. Published indexed and accessible literature was compared, but an unindexed equivalent or an implicit earlier parameter specialization remains a research novelty risk. No independent scientific validation has been performed.

## References

1. Maria Kosche, Tore Koß, Florin Manea, Stefan Siemer, *Absent Subsequences in Words*, arXiv:2108.13968, first public August 31, 2021; Fundamenta Informaticae 189 (2022), 199–240. https://arxiv.org/abs/2108.13968 . See especially Definition 2.4, Theorem 3.1 and Propositions 3.6–3.10.
2. Duncan Adamson, Pamela Fleischmann, Annika Huch, Florin Manea, Paul Sarnighausen-Cahn, Max Wiedenhöft, *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599, first public July 26, 2024. https://arxiv.org/abs/2407.18599 .
3. Florin Manea, Tina Ringleb, Stefan Siemer, Maximilian Winkler, *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471, April 30, 2025. https://arxiv.org/abs/2504.21471 .
