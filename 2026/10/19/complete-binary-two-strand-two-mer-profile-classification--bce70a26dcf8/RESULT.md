# Complete binary two-strand two-mer profile classification
## Finding
For every integer \(n\ge2\), let \(\mathcal X_n\) be the set of unordered multisets \(\{\!\{u,v\}\!\}\) of two words in \(\{0,1\}^n\), allowing \(u=v\). Let \(M_2(u,v)\) be the multiset union of their contiguous ordered pairs, counting multiplicities. The exact number \(P(n)\) of distinct pooled spectra is
\[
P(n)=\begin{cases}5n^2-8n+6,&n\text{ even},\\5n^2-8n+4,&n\text{ odd}.
\end{cases}
\]
Consequently a largest binary two-strand, read-length-two reconstruction code has precisely \(P(n)\) codewords. For \(n=2,3,4,5,6\) the values are \(10,25,54,89,138\), respectively. Every attainable profile can also be characterized explicitly by the theorem below.

## Assumptions and scope
The input consists of two **linear** binary words of a **common** length \(n\ge2\), with repetition allowed and unordered strand identity. All contiguous length-two substrings of each word are pooled with multiplicities; there are exactly \(2(n-1)\) observed pairs. In particular, the observer receives neither strand endpoints nor the strand assignment of any pair.

Write the pooled count vector as \((A,B,C,D)=(c_{00},c_{01},c_{10},c_{11})\). Put \(L=n-1\), \(T=2L\), \(s=B+C\), and \(t=B-C\). All vector entries are nonnegative integers summing to \(T\).

**Structural characterization.** Precisely the following profiles occur:

1. \(s=0\), with \(A\in\{0,L,2L\}\) and \(D=T-A\).
2. \(s\ge2\) even and \(t=0\), with every \(0\le A\le T-s\) realized.
3. \(s\ge1\) odd and \(|t|=1\), with every \(0\le A\le T-s\) realized.
4. \(s\ge2\) even and \(|t|=2\), with every \(0\le A\le T-s\) realized, **except** that \(s=2L\) is impossible when \(L\) is even.

Here \(B=(s+t)/2\) and \(C=(s-t)/2\); the stipulated nonnegativity and total impose the automatic upper bounds \(s\le2L\) in case 2, \(s\le2L-1\) in case 3, and \(s\le2L\) in case 4. No other pooled profiles occur.

## Proof
**Single-word lemma.** In one binary length-\(n\) word let \(a,b,c,d\) be the numbers of \(00,01,10,11\) adjacent pairs. Set \(r=b+c\). If \(r=0\), the word is constant, hence \((a,d)=(L,0)\) or \((0,L)\). Otherwise \(1\le r\le L\), and the signs of consecutive transitions alternate, whence \(b-c=0\) if \(r\) is even and \(b-c=\pm1\) if \(r\) is odd. Conversely, for every such \(r\) and admissible sign, *each* \(a\in\{0,\ldots,L-r\}\) occurs. Choose the alternating sequence of its \(r\) transitions, then insert all \(a\) \(00\)-loops in any zero-run and the other \(L-r-a\) \(11\)-loops in any one-run. Both kinds of run exist because \(r>0\). This constructs a length-\(n\) word with the prescribed four counts.

**Necessity of the characterization.** Each constituent word contributes signed transition imbalance in \(\{-1,0,1\}\), so the pooled imbalance has absolute value at most \(2\). Moreover \(s\equiv t\pmod2\). If both words have no transitions, their \(00\)-counts are either \(0\) or \(L\), yielding case 1. If \(|t|=2\), both strands have the same odd-direction imbalance, hence both have an odd positive number of transitions. The largest odd transition count not exceeding \(L\) is \(L\) for odd \(L\) and \(L-1\) for even \(L\); this rules out only \(s=2L\) when \(L\) is even. All other restrictions follow immediately.

**Sufficiency for \(|t|=2\).** Every even \(s\) from \(2\) up to twice the largest odd integer at most \(L\) splits into two positive odd integers at most \(L\), both given the prescribed imbalance sign. The single-word lemma realizes each split with independent \(00\)-counts ranging over \([0,L-r_1]\) and \([0,L-r_2]\). Their sums fill the entire integer interval \([0,2L-s]\). Thus every allowed \(A\) is realized.

**Sufficiency for \(t=0\).** The case \(s=0\) is handled by the two constant words. For positive even \(s\), if either \(L\) is odd or \(s\le2L-2\), split \(s\) into two positive odd counts at most \(L\), assigning opposite imbalance signs. If \(L\) is even and \(s=2L\), instead take two words with the even count \(L\) and zero imbalance. Every chosen strand has a transition, so the single-word lemma supplies every total \(00\)-count \(A\) from \(0\) through \(2L-s\).

**Sufficiency for \(|t|=1\).** Necessarily \(s\) is odd, \(1\le s\le2L-1\). When \(s\ge3\), write \(s=r_1+r_2\), with a positive odd \(r_1\le L\) and a positive even \(r_2\le L\); such a split exists for every odd \(s\) in this range. Give the odd strand the required signed imbalance, the even strand imbalance zero. Both traverse both symbols, so the single-word lemma fills every \(A\in[0,2L-s]\). For \(s=1\), one word has one transition and hence offers \(a\in[0,L-1]\). The other is constant, adding either \(0\) or \(L\) to the \(00\)-count. Thus the union is exactly the full interval \([0,2L-1]\). The characterization follows.

**Counting.** At \(s=0\) there are three profiles. The \(t=0\) profiles with \(s=2j\), \(1\le j\le L\), contribute
\[
\sum_{j=1}^{L}(2L-2j+1)=L^2.
\]
For each of the two signs \(t=\pm1\), the profiles at \(s=2j+1\), \(0\le j<L\), contribute
\[
\sum_{j=0}^{L-1}(2L-2j)=L(L+1).
\]
For each sign \(t=\pm2\), the same even-sum count is \(L^2\) when \(L\) is odd, or \(L^2-1\) when \(L\) is even, because the final \(s=2L\) case is excluded in the latter parity. Therefore
\[
P(n)=3+L^2+2L(L+1)+2\left(L^2-\mathbf1_{\{L\text{ even}\}}\right)
=5L^2+2L+3-2\mathbf1_{\{L\text{ even}\}}.
\]
Substitution of \(L=n-1\) proves the stated piecewise quadratic formula. A valid zero-error code uses at most one multiset from each pooled profile; selecting one preimage of every realizable profile attains this bound. \(\square\)

## Verification
The accompanying standalone standard-library script `verify.py` implements the literal observation map for each word. It compares the theorem's complete profile *sets* (not merely their counts) with exhaustive enumeration over unordered pairs of words for all lengths \(2\le n\le10\). It then compares the theorem's profile sets with independent Minkowski sums of single-word adjacent-pair vectors for \(11\le n\le17\), and checks the resulting exact count identity for \(18\le n\le127\). Run `python3 verify.py`. The run produces the final marker `THEOREM_BOUNDARY_CHECKS_OK`. These finite computations corroborate, but do not replace, the preceding proof for all \(n\ge2\).

## Relationship to prior work
Yehezkeally, Marcovich, and Yaakobi (2021) define pooled \(\ell\)-profiles of multisets of multiple equal-length strands and reconstruction codes using precisely the observation model considered here. Their results concern read-length lower bounds and asymptotic-rate constructions; the published paper's theorems and appendices do not state the fixed two-strand binary, read-length-two exact profile count or this characterization. The generalized 2022 extension by Yehezkeally, Bar-Lev, Marcovich, and Yaakobi develops asymptotic reconstruction in related models, not the present exact short-read enumeration.

A previously published single-strand binary two-mer classification gives an exact quadratic count for \(k=1\), and its proof classifies individual Markov-type vectors. For the present two-strand problem, attainable vectors are the *Minkowski sum* of two single-strand sets. Their decomposition and the parity-sensitive endpoint constraints are not captured by the scalar one-strand count. Counting **cyclic** Markov types (Jacquet, Knessl, and Szpankowski, 2010) forces cross-transition balance and does not enumerate two independent linear paths with pooled imbalances up to two. A literature and research-index search located no statement implying the displayed two-strand formula; this is a qualified originality assessment, not a claim that all prior literature has been exhausted.

## Limitations
The formula concerns only a fixed binary alphabet, exactly two linear strands of identical length, complete multiplicity-preserving length-two substring reads, and their unordered source multiset. It does not determine the sizes of individual inverse-image fibres, optimal representative encoding algorithms, incomplete/noisy read models, different lengths, larger alphabets, or additional strands. The exact count is elementary enough that an equivalent unpublished or unindexed Markov-type enumeration could exist; independent review of originality has not occurred. No independent audit or external certification is claimed.

## References
1. Y. Yehezkeally, S. Marcovich, and E. Yaakobi, *Multi-strand Reconstruction from Substrings*, arXiv:2108.11725v1, publicly posted 2021-08-26. https://arxiv.org/abs/2108.11725.
2. Y. Yehezkeally, A. Bar-Lev, S. Marcovich, and E. Yaakobi, *Generalized Unique Reconstruction from Substrings*, arXiv:2210.04471v1, publicly posted 2022-10-10. https://arxiv.org/abs/2210.04471.
3. R. Gabrys and O. Milenkovic, *Unique Reconstruction of Coded Strings from Multiset Substring Spectra*, arXiv:1804.04548v1, 2018. https://arxiv.org/abs/1804.04548.
4. P. Jacquet, C. Knessl, and W. Szpankowski, *Counting Markov Types*, DMTCS Proceedings AM (2010), DOI:10.46298/dmtcs.2768.
5. *Exact binary two-multispectrum code size and singleton classification*, publicly posted research record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-binary-two-multispectrum-code-size-and-singleton-classific--13779c08da71.
