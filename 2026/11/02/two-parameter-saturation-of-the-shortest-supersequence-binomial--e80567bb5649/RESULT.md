# Two-parameter saturation of the shortest-supersequence binomial bound

## Finding
For integers \(p,n\ge 2\), let
\[
U_{p,n}=(0^p1)^n,\qquad V_{p,n}=(1^p0)^n,
\]
where concatenation is implicit and \(0^p\) means a run of \(p\) zeros. A common supersequence is a word containing both inputs as scattered subsequences. Then the shortest common-supersequence length is exactly \(2pn+1\), and the number of **distinct** shortest common supersequence words is
\[
\boxed{S_{p,n}=\binom{2((p-1)n+1)}{(p-1)n+1}.}
\]
Writing \(h=(p-1)n+1\), this attains the general binomial upper bound \(\binom{2h}{h}\) for the number of length-minimal common supersequences of two inputs each of length \((p+1)n\) whose shortest common supersequence has length \(2pn+1\). The equality family has a nonempty common subsequence (indeed its longest common subsequence has length \(2n-1\)). The proof gives an explicit bijection with balanced binary words of length \(2h\).

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\), both inputs have the displayed forms, and \(p,n\) are arbitrary integers at least two. Words are counted as strings, not as embedding multiplicities. A shortest common supersequence is not to be confused with an arbitrary deletion-minimal common supersequence; the latter may have greater length in general, and no assertion about all deletion-minimal supersequences of these inputs is required here.

## Proof
**1. Length and terminal letter.** The word \(U_{p,n}\) requires \(pn\) zeros, and \(V_{p,n}\) requires \(pn\) ones. Therefore any common supersequence has length at least \(2pn\). A length-\(2pn\) common supersequence would use exactly \(pn\) of each letter. Its last zero must precede a one for \(U_{p,n}\), while its last one must precede a zero for \(V_{p,n}\), a contradiction. Hence the shortest length is at least \(2pn+1\).

At this length every common supersequence contains either \(pn+1\) zeros and \(pn\) ones, or vice versa. Consider the first case. All \(pn\) ones must be used in any embedding of \(V_{p,n}\), and its terminal zero follows the last one; hence the common supersequence ends in zero. Its prefix \(x\) of length \(2pn\) has exactly \(pn\) letters of either kind. Since \(U_{p,n}\) ends in one, it embeds in \(x\), using all \(pn\) zeros there. Thus \(x\) must end in one. Also \((1^p0)^{n-1}1^p\) embeds in \(x\), using all \(pn\) ones, because the final zero of \(V_{p,n}\) is necessarily the removed terminal zero. Conversely, if the two latter embeddings exist in such an \(x\), then \(x0\) is a common supersequence of the two inputs. By exchanging zero and one, common supersequences with \(pn\) zeros and \(pn+1\) ones are counted equally.

**2. Boundary characterization.** Let \(x\) be balanced with \(pn\) occurrences of each letter and final symbol one. For each symbol \(c\), list the positions of its occurrences in increasing order. The two embeddings in Step 1 are possible if and only if, for every \(k=1,\ldots,n-1\), the \((kp)\)-th occurrence of \(c\) is *not immediately followed* by its \((kp+1)\)-th occurrence, for both \(c=0\) and \(c=1\). Indeed, the required embeddings use all occurrences of their respective heavy letters: a separator of the opposite letter is needed between consecutive blocks of \(p\), and the final-one condition supplies the last separator for \(U_{p,n}\). This establishes both necessity and sufficiency. We call such \(x\) admissible.

**3. Forced-step deletion.** In an admissible \(x\), mark the symbol immediately after the \((kp)\)-th occurrence of each letter \(c\), for every \(1\le k<n\). Each marked symbol is the opposite letter. The marks are at distinct positions (two different preceding positions cannot share an immediate successor), and no mark is on the final symbol: there is a later occurrence of the boundary letter. There are exactly \(n-1\) marked zeros and \(n-1\) marked ones. Removing all marks yields a binary word \(y\) with exactly \(h=(p-1)n+1\) zeros and \(h\) ones, ending in one.

This map is bijective. To recover \(x\) from \(y\), read \(y\) from left to right, outputting each symbol, and whenever the running occurrence count of an output symbol \(c\) reaches a positive multiple \(kp<pn\), immediately output the opposite symbol before consuming another input symbol. Repeat this forced rule, including cascades, until no further output is forced. Every such forced output is the successor of the boundary occurrence that caused it, so any admissible \(x\) reconstructs exactly.

For completeness, the algorithm terminates and generates all required forced outputs for any balanced \(y\) ending in one. Let \(r_c\) be the number of boundary events fired for letter \(c\), so \(0\le r_c\le n-1\). Upon completion the two output occurrence counts are \(h+r_1\) zeros and \(h+r_0\) ones. If \(m=\min(r_0,r_1)<n-1\), assume without loss of generality \(r_0=m\). Then the zero count is at least \(h+m\ge p(m+1)\), because
\[
h+m-p(m+1)=(p-1)(n-m-1)\ge0.
\]
Thus the \((m+1)\)-th zero boundary must have fired, a contradiction. Hence \(r_0=r_1=n-1\). Furthermore, before consuming the final (one) symbol of \(y\), the base occurrence counts are \(h\) zeros and \(h-1\) ones. If any boundary remains unfired, the same minimum-event argument gives either the preceding nonnegative difference or
\[
h-1+m-p(m+1)=(p-1)(n-m-1)-1\ge0
\]
for \(p\ge2\), again a contradiction. Hence all forced output occurs before that final input symbol: the expansion ends in one, has \(pn\) occurrences of each letter, and satisfies the boundary characterization. Thus expansion and compression are mutual inverses.

**4. Enumeration and equality.** There are \(\binom{2h-1}{h}\) balanced words \(y\) of length \(2h\) ending in one. Therefore there are that many shortest common supersequences ending in zero. Swapping symbols gives the same number ending in one. Their union is disjoint, so
\[
S_{p,n}=2\binom{2h-1}{h}=\binom{2h}{h}.
\]
This also produces examples and establishes that the lower bound on length is attained. The usual common-subsequence/shortest-supersequence identity gives longest common-subsequence length \(2(p+1)n-(2pn+1)=2n-1\). Finally, the general upper bound of Lin for length-minimal common supersequences, specialized to two equal-length inputs with excess lengths \(h\) each, is \(\binom{2h}{h}\), so equality holds. \(\square\)

## Verification
Run `python3 verify.py` using only the Python standard library. Its independent shortest-supersequence dynamic program checks \(84\) parameter pairs, a constructive inverse check evaluates \(14{,}706\) balanced bridges, and direct source-word enumeration tests \(5{,}960\) short words. These finite checks supplement, rather than replace, the unrestricted proof. Expected output and exact execution results are in `verification_output.txt`.

## Relationship to prior work
Sopp, Liyanage, Gong and Zhu (2026, arXiv:2603.22591) study computation and enumeration of deletion-minimal common supersequences and provide the motivating computational framework. Lin (2026, arXiv:2609.26650), building on earlier work, establishes the universal binomial bound for the number of shortest common supersequences, but the inspected text does not describe this two-parameter repeated-run equality family or the balanced-word bijection. An earlier result on opposite single-block strings treats different inputs (one monotone zero block followed by one monotone one block versus the reverse); its parameters do not cover \((0^p1)^n,(1^p0)^n\) when \(n\ge2\). The present contribution is a structured equality case with a nonzero common-subsequence length, not a new general upper bound.

## Limitations
The theorem counts only *shortest* common supersequences and does not claim that every deletion-minimal common supersequence is shortest. General binary inputs, multiple strings, and larger alphabets are excluded. The bijection gives exact counts, but no improvement in arbitrary-input enumeration complexity is asserted. Publication priority has not been independently confirmed; possible unindexed or inaccessible equivalent statements remain a residual risk.

## References
- Braeden Sopp, Adiesha Liyanage, Mingyang Gong, Binhai Zhu, *Computing and Enumerating Minimal Common Supersequences Between Two Strings*, arXiv:2603.22591v1 (first posted 2026-03-23), https://arxiv.org/abs/2603.22591.
- Andrew D. Lin, *Lower Bounds for all List-Decodable Deletion Codes*, arXiv:2609.26650v1 (first posted 2026-09-22), especially the general counting bound, https://arxiv.org/abs/2609.26650.
- Noga Alon, Gabriela Bourla, Ben Graham, Xiaoyu He, Noah Kravitz, *Logarithmically larger deletion codes of all distances*, arXiv:2209.11882v1 (2022), earlier general counting-bound context, https://arxiv.org/abs/2209.11882.
