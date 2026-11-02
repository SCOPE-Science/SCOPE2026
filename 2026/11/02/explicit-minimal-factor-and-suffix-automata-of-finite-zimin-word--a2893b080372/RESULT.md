# Explicit minimal factor and suffix automata of finite Zimin words

## Finding
For every integer \(n\geq 1\), let \(Z_0=\varepsilon\) and \(Z_n=Z_{n-1}a_nZ_{n-1}\), where \(a_1,\ldots,a_n\) are distinct literal letters. Put \(N=2^n-1\). The following partial deterministic automaton has state set \(Q=\{0,1,\ldots,N\}\), initial state \(0\), and alphabet \(\{a_1,\ldots,a_n\}\):

1. From \(0\), there is an \(a_s\)-transition to \(2^{s-1}\), for every \(1\leq s\leq n\).
2. For a state \(1\leq p\leq N\), set \(r=1+\lfloor\log_2 p\rfloor\). If \(p<2^r-1\), its only outgoing transition is \(p\xrightarrow{a_{1+\nu_2(p+1)}}p+1\).
3. If \(p=2^r-1\), its outgoing transitions are precisely \(p\xrightarrow{a_s}2^{s-1}\) for \(r<s\leq n\).

All undefined transitions reject. With every state accepting, the automaton recognizes **exactly the contiguous factors**, including \(\varepsilon\), of \(Z_n\) and is minimal among partial deterministic automata. With only \(0\) and the \(n\) states \(2^r-1\) (\(1\leq r\leq n\)) accepting, the *same labelled transition graph* is the minimal partial deterministic automaton accepting exactly the suffixes of \(Z_n\), including \(\varepsilon\).

There are exactly \(2^n\) states and \(2^n-1+\binom n2\) transitions. More finely, for each \(1\leq s\leq n\), the number of transitions labelled \(a_s\) is exactly \(2^{n-s}+s-1\). For any nonempty factor \(u\), the reached state is the end position of its **earliest** occurrence in \(Z_n\). Thus the whole exponential-size automaton has an explicit arithmetic transition rule requiring only \(O(n)\) bits of state storage (not an explicit graph construction).

## Assumptions and scope
A factor means a contiguous substring, not a scattered subsequence or a morphic image of a pattern. Positions are numbered from \(1\) to \(N\), and \(\nu_2(p)\) is the largest \(t\geq0\) such that \(2^t\) divides the positive integer \(p\). The automata are *partial*: missing transitions reject immediately; a complete deterministic automaton additionally needs one rejecting sink, giving \(2^n+1\) states. The empty factor and empty suffix are included. The theorem covers all integers \(n\geq1\), including \(n=1\), without assumptions on letter order.

## Proof
**Ruler positions.** The recursion gives \(Z_n[p]=a_{1+\nu_2(p)}\) for every \(1\leq p\leq2^n-1\). This follows by induction, since the central position \(2^{n-1}\) has letter \(a_n\), and the two flanking blocks repeat \(Z_{n-1}\).

**A complete factor-occurrence lemma.** Fix a nonempty factor \(u\), and let \(a_r\) be its maximum-indexed letter. Two appearances of \(a_r\) cannot lie in one factor without an intervening letter of index greater than \(r\): consecutive \(a_r\)-positions are separated by \(2^r\), and their midpoint has valuation at least \(r\). Therefore \(a_r\) occurs exactly once in \(u\). The radius-\((2^{r-1}-1)\) neighborhood of *every* \(a_r\)-position is the same copy of \(Z_{r-1}a_rZ_{r-1}\). Consequently, for uniquely determined \(0\leq i,j<2^{r-1}\),

\[
u=\operatorname{suf}_i(Z_{r-1})\,a_r\,\operatorname{pre}_j(Z_{r-1}),
\]

and, conversely, every such word occurs at every \(a_r\)-position and nowhere else. Its complete set of occurrence end positions is

\[
E_{r,j}=\{2^{r-1}+j+t2^r:0\leq t<2^{n-r}\}.
\]

Its smallest ending position is \(p=2^{r-1}+j\). As \(r\) and \(j\) vary, the possible values of \(p\) partition \(\{1,\ldots,N\}\) into blocks \([2^{r-1},2^r-1]\). Factors with the same \(p\) have the same ending-position set and hence the same possible right extensions.

**Exact transitions.** If \(p\) belongs to the block indexed by \(r\) and \(p<2^r-1\), then all endpoints in \(E_{r,j}\) have the same next letter, \(a_{1+\nu_2(p+1)}\); the endpoints after appending it are exactly \(E_{r,j+1}\), whose earliest member is \(p+1\). If \(p=2^r-1\), every eligible next position has form \(2^r(t+1)\), and its possible letters are exactly \(a_s\) for \(r<s\leq n\). Appending \(a_s\) yields the ending-position set of \(a_s\), whose earliest member is \(2^{s-1}\). The first occurrence of \(a_s\) is also at \(2^{s-1}\), giving the initial transitions. Thus the stated graph records *all and only* factor extensions and recognizes exactly the factors with all states final.

**Reachability and minimality.** For every \(p\in\{1,\ldots,N\}\), the prefix of \(Z_n\) ending at \(p\) has earliest ending position \(p\), so its path reaches state \(p\); hence all states are reachable. If a factor has earliest ending position \(p\), the maximum length of any right extension that remains a factor is precisely \(N-p\): the remaining suffix after its earliest occurrence realizes that length, while later occurrences cannot yield a longer extension. Therefore different states have different maximal lengths of accepted continuations, and the factor automaton is minimal. The initial state is distinguished by maximum continuation length \(N\).

A nonempty factor is a suffix of \(Z_n\) precisely when its endpoint set contains \(N=2^n-1\). Since \(N\equiv2^r-1\pmod{2^r}\), this occurs for \(E_{r,j}\) exactly when \(p=2^r-1\). Therefore the asserted accepting states recognize exactly the suffixes. The maximum length of a continuation that makes the factor a suffix is again \(N-p\), so these reachable states are pairwise distinguishable for the suffix language as well.

**Edge counts.** The consecutive prefix path supplies one transition labelled \(a_s\) for each appearance of \(a_s\) in \(Z_n\), namely \(2^{n-s}\) such transitions. There are precisely \(s-1\) additional \(a_s\)-transitions: from the initial state and the earlier block ends other than the predecessor of the first \(a_s\). Hence the label count is \(2^{n-s}+s-1\). Summing over \(s\) gives \((2^n-1)+n(n-1)/2\), completing the proof.

## Verification
The accompanying standard-library-only `checker.py` independently constructs the classical online suffix automaton, compares its complete labelled transition graph to the arithmetic rule through rank \(11\), and checks all label counts. It separately enumerates *every* factor, its full occurrence-endpoint set, earliest ending position, and suffix status through rank \(7\). All tests passed. To reproduce, run `python3 checker.py` in the directory containing this result and the checker; it prints `ALL CHECKS PASSED`. The unrestricted conclusions follow from the proof, not from finite testing.

## Relationship to prior work
Głowinski and Rytter [1] provide a linear-time interleaving criterion for testing whether a literal word is a factor of a Zimin word (their Lemma 2); they do not give the labelled minimal automaton or the transition counts. Fici [2] treats general suffix automata, end-position equivalence, and state/edge bounds and formulas; these do not specify the complete state-by-state Zimin graph. Fici [3] establishes general relationships with special factors and minimal-size automata, so minimal state count alone is **not** asserted to be a new type of result. Rytter and Shur [4] study Zimin-pattern embeddings rather than literal-factor automata. The integer sequence of total edge counts has the pre-existing arithmetic formula catalogued as OEIS A132925 [5], but the entry does not attribute it to Zimin automata. The stated contribution is the **explicit labelled graph, its factor/suffix interpretation, and the per-letter edge law**, not a new general membership algorithm or first discovery of the integer sequence.

## Limitations
The alphabet grows with the Zimin rank, and symbols are treated literally. The result does not classify automata of all images of Zimin patterns, other recursive palindromes, or arbitrary text families; it does not improve the known linear-time literal-factor membership bound. A plausible broad comparison source [3] was accessible only at abstract level, and complete historical-priority verification remains open. All review here is non-independent.

## References
[1] R. Głowinski and W. Rytter, *Compressed Pattern-Matching with Ranked Variables in Zimin Words*, arXiv:1307.1560v1 (2013-07-05), especially Section 2 and Lemma 2. https://arxiv.org/html/1307.1560v1

[2] G. Fici, *Combinatorics of Finite Words and Suffix Automata*, CAI 2009 (presentation dated 2009-05-20), DOI:10.1007/978-3-642-03564-7_16. https://www.researchgate.net/publication/220795075_Combinatorics_of_Finite_Words_and_Suffix_Automata

[3] G. Fici, *Special factors and the combinatorics of suffix and factor automata*, Theoretical Computer Science 412 (2011), 3604–3615, DOI:10.1016/j.tcs.2011.03.007. https://iris.unipa.it/handle/10447/73740

[4] W. Rytter and A. M. Shur, *On Searching Zimin Patterns*, arXiv:1409.8235v1 (2014-09-29). https://arxiv.org/pdf/1409.8235

[5] OEIS Foundation, A132925, entry for \(2^n-1+\binom n2\). https://oeis.org/A132925

[6] A. Blumer et al., *The smallest automaton recognizing the subwords of a text*, Theoretical Computer Science 40 (1985), 31–55, DOI:10.1016/0304-3975(85)90157-4.
