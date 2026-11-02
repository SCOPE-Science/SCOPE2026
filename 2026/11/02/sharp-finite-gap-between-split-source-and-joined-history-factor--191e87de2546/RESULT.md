# Sharp finite gap between split-source and joined-history factor parsing

## Finding

Let \(R\) be a nonempty finite reference word, and let \(s\) be a nonempty target over a finite alphabet. In **split-source adaptive factor parsing**, each phrase is either a single symbol, a contiguous factor of \(R\), or a contiguous factor of the target prefix decoded strictly before that phrase. In **joined-history factor parsing**, each phrase is either a single symbol or a contiguous factor of the concatenated word consisting of \(R\) followed by the target prefix decoded strictly before the phrase. All source occurrences must be entirely in the available history, and no phrase may copy from its own undecoded positions. Let \(A_R(s)\) and \(P_R(s)\) denote the respective minimum numbers of phrases.

**Theorem.** For every such \(R,s\),
\[
P_R(s)\le A_R(s)\le 2P_R(s)-1.
\]
For every integer \(m\ge1\), there is a reference of length \(m\) on an alphabet of \(m\) distinct letters and a target satisfying the simultaneous equalities
\[
P_R(s)=m,\qquad A_R(s)=2m-1.
\]
Consequently the largest possible split-to-joined ratio among inputs having joined-history optimum exactly \(m\) is \(2-1/m\). The universal multiplicative constant \(2\) is a sharp supremum but is **never attained** by a finite nonempty target.

An explicit sharp family is obtained from pairwise distinct letters \(a_1,\ldots,a_m\) by setting
\[
R=a_1a_2\cdots a_m,\quad T_1=R,\quad
T_j=T_{j-1}(a_j a_{j+1}\cdots a_m)T_{j-1}
\quad(2\le j\le m),\quad s=T_m.
\]
Its target length is \((m-1)2^m+1\).

## Assumptions and scope

The alphabet may vary with \(m\). The two models use the same single initial reference and the same target; only admissibility of factors crossing the reference/decoded-target boundary differs. Literal single-symbol phrases are always permitted, including when the symbol does not occur in the reference. Counts concern phrases, **not** the bit cost of pointers or a particular compressed file format. The result applies to finite, nonempty inputs and completely nonoverlapping source occurrences in already available text. No asymptotic average-source claim is made.

For compactness let \(\sigma_j=a_j\cdots a_m\), and let \(T_j\) denote the family above. A factor means a contiguous substring, never a scattered subsequence.

## Proof

**1. Universal upper bound.** Take an optimum joined-history parsing with \(p=P_R(s)\) phrases. Its first phrase is a literal or a factor of \(R\), since no target prefix has yet been decoded, hence is a legal single split-source phrase. For every subsequent joined-history phrase, choose an occurrence in \(R\) concatenated with the already decoded target prefix. If the occurrence stays wholly on either side of the join, it is already split-source admissible. If it crosses the join, cut the phrase at that point. Its first piece is a suffix of \(R\), and its second piece is a prefix of the previously decoded target prefix; both pieces are legal split-source phrases, sequentially. The same argument remains valid when preceding phrases have been split, since their concatenated decoded text is unchanged. Therefore \(A_R(s)\le1+2(p-1)=2p-1\). Inclusion of admissible sources gives \(P_R(s)\le A_R(s)\).

**2. Greedy optimality.** For both models, choose at each target position a longest admissible next phrase. This minimizes phrase count. Indeed, in any optimum parse whose next phrase is shorter than the greedy phrase, replace that phrase and every following complete phrase covered by the greedy extension with the greedy phrase. If the extension ends inside an old phrase, retain only its nonempty suffix. The retained suffix remains legal because it is a factor of the old phrase's fixed reference occurrence or previously decoded history occurrence; the decoded prefix at its new start contains every source position that was available at its old start. All later source occurrences also remain available. Thus the modified parse uses no more phrases and begins with the greedy choice. Iterate from left to right. The argument includes literals as one-symbol base cases.

**3. Joined-history construction.** The initial phrase \(T_1=R\) is available in the reference. At stage \(j\), for \(2\le j\le m\), the block \(\sigma_jT_{j-1}\) is a factor of \(RT_{j-1}\): start at the \(j\)-th reference letter and continue across the reference/decoded-target join. Therefore \(P_R(T_m)\le m\).

**4. Exact greedy split-source parsing.** For \(m=1\), both costs equal one. Suppose \(m\ge2\). Greedy split-source parsing begins with the phrase \(R\). At stage \(j=2\), the new block \(\sigma_2T_1\) splits greedily as \(\sigma_2\mid T_1\): the reference contains \(\sigma_2\) only as its terminal suffix, so the first phrase cannot extend; the occurrence of \(T_1\) in the decoded prefix is followed, if a later stage exists, by \(a_2\), whereas the next target symbol is \(a_3\). Thus the second phrase cannot extend either.

For \(3\le j\le m\), expand the new block as
\[
\sigma_jT_{j-1}
=\underbrace{\sigma_jT_{j-2}}_{u_j}
\underbrace{\sigma_{j-1}T_{j-2}}_{v_j}.
\]
Both \(u_j\) and \(v_j\) occur in the previously decoded \(T_{j-1}=T_{j-2}\sigma_{j-1}T_{j-2}\), starting respectively one character into and at the beginning of the central suffix \(\sigma_{j-1}\). Both source occurrences terminate at the final character of \(T_{j-1}\).

To prove maximality, observe that \(T_{j-1}\) contains the special adjacent pair \(a_m a_{j-1}\) **exactly once**, at the first join from \(T_{j-2}\) into \(\sigma_{j-1}\); this pair does not occur in \(T_{j-2}\). Indeed all adjacent pairs internal to \(R\) or its suffixes advance from \(a_i\) to \(a_{i+1}\), and the only other backward-jump pairs introduced in earlier stages have second symbol \(a_1,\ldots,a_{j-2}\). Neither \(u_j\) nor \(v_j\) contains \(a_m a_{j-1}\); each is longer than \(T_{j-2}\). Hence an occurrence in \(T_{j-1}\) cannot lie inside either copy of \(T_{j-2}\) or cross the first join. Each has precisely its displayed occurrence inside the central suffix followed by the second copy. Since it reaches the end of the available history, \(u_j\) cannot be extended. The fixed reference is too short to supply a competing occurrence.

After reading \(u_j\), the available history is \(T_{j-1}u_j\). Its new boundary has adjacent pair \(a_m a_j\), which is absent from \(v_j\). Also \(|v_j|=|u_j|+1\), so \(v_j\) cannot lie wholly inside \(u_j\). Thus its unique available occurrence is still the one in \(T_{j-1}\) ending at that word's end, and it cannot be extended. Therefore \(u_j\mid v_j\) are exactly the next two greedy phrases. By greedy optimality the full cost is
\[
A_R(T_m)=1+2(m-1)=2m-1.
\]
The universal upper bound now forces \(m\le P_R(T_m)\), which together with Step 3 gives \(P_R(T_m)=m\).

Finally, if \(L_j=|T_j|\), then \(L_1=m\) and \(L_j=2L_{j-1}+m-j+1\), yielding \(L_m=(m-1)2^m+1\). The ratio is \(2-1/m\), proving both sharpness at every finite joined-history phrase count and the unattained sharp supremum.

## Verification

Run `python3 verify.py` from the directory containing the attached verifier. The verification is independent of the symbolic proof: it computes longest admissible phrases directly, computes globally optimal phrase counts by a separate backward dynamic program for the smaller constructions, checks unique-occurrence properties of the two-phrase induction, and exhaustively tests short binary reference/target pairs. Saved output is in `verification_output.txt`.

The verifier confirms the family for \(1\le m\le7\), including independent dynamic-programming optimality checks for \(1\le m\le5\), and checks \(1764\) binary reference/target pairs against both greedy-optimal counts and the universal inequalities. The arbitrary-\(m\) claim rests on the mathematical proof, not this finite enumeration.

## Relationship to prior work

Marteau, *On the Adaptive Covering Complexity of Strings: Unifying Relative and Self-Referential Compression*, arXiv:2610.26021, first publicly posted October 19, 2026, defines the split-source factor model and proves the comparison \(P_R(s)\le A_R(s)\le2P_R(s)\) for a single preset reference (Theorem IV.10). Remark IV.11 explicitly says that it is not known whether the factor two can be attained and reports a finite search with maximum ratio \(5/3\). The present theorem strengthens the additive bound, constructs equality at every joined-history phrase count, and resolves the factor's sharpness versus finite nonattainment. The source's greedy exchange argument is consistent with the self-contained exchange proof here.

Kosolobov and Shur, *Comparison of LZ77-type Parsings*, arXiv:1708.03558 (2017), prove several sharp comparisons among overlapping/nonoverlapping and pair/triple LZ encodings, including a superficially similar \(2k-1\) extremal phrase-count pattern. Their variants change overlap and phrase-encoding rules within a single target history; they do **not** compare a fixed reference kept separate from the decoded target with their concatenated-history model. The shared numeric pattern is not a proof of the present theorem or a claim of disjoint mathematical ancestry.

## Limitations

The sharp witnesses use a growing alphabet of \(m\) symbols and target length \((m-1)2^m+1\). No fixed-alphabet sharpness or optimal witness length is claimed. The comparison does not concern sliding-window limits, overlapping self-copies, phrase bit costs or multiple separately segmented external references. Publication-priority searches and primary-source comparisons do not rule out an unindexed equivalent treatment. Independent external mathematical validation has not been performed.

## References

1. P.-F. Marteau, *On the Adaptive Covering Complexity of Strings: Unifying Relative and Self-Referential Compression*, arXiv:2610.26021, 2026, https://arxiv.org/abs/2610.26021, specifically Definitions III.1–III.3, Theorem IV.10, Remark IV.11, and greedy exchange Lemma IV.1.
2. D. Kosolobov and A. M. Shur, *Comparison of LZ77-type Parsings*, arXiv:1708.03558 (first posted 2017; journal 2019), https://arxiv.org/abs/1708.03558, specifically Theorem 3 and Sections 2–4.
