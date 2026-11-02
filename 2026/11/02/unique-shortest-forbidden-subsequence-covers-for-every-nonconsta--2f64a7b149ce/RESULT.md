# Unique shortest forbidden-subsequence covers for every nonconstant binary triple

## Finding
Let \(x\preccurlyeq y\) mean that \(x\) is a *scattered subsequence* of \(y\): its letters occur in \(y\) in order, but not necessarily consecutively. For a binary forbidden pattern \(u\) and \(k\ge1\), put
\[
\mathcal A_k(u)=\{x\in\{0,1\}^k:u\not\preccurlyeq x\}.
\]
An *admissible cover* is a finite word \(W\) such that \(u\not\preccurlyeq W\) and every member of \(\mathcal A_k(u)\) is a scattered subsequence of \(W\). The constraint that the *host itself avoids* the forbidden word is essential.

**Theorem.** For each \(k\ge3\) and each of the six nonconstant binary patterns \(u\) of length three, there exists exactly one shortest admissible cover. Its length is
\[
L(u,k)=3k-4+\tau(u),\qquad
\tau(u)=\mathbf1_{u_1\ne u_2}+\mathbf1_{u_2\ne u_3}.
\]
For the four words with one adjacent-letter change, \(L=3k-3\); for the two alternating words, \(L=3k-2\). Representatives and their unique optimizers are
\[
\begin{array}{c|c|c}
 u& W_{u,k}&|W_{u,k}|\\ \hline
001&1^{k-2}\,0\,1^{k-1}\,0^{k-1}&3k-3\\
010&1^{k-1}\,0^k\,1^{k-1}&3k-2.
\end{array}
\]
The remaining four cases follow by reversal and bit complementation, applied simultaneously to the forbidden pattern and the host.

## Assumptions and scope
The alphabet is precisely \(\{0,1\}\), \(k\) is an arbitrary integer at least three, and the forbidden pattern is one of \(001,010,011,100,101,110\). Both the targets and the host avoid the pattern as a scattered subsequence; no contiguous-factor interpretation is intended. The theorem minimizes the length of a **single linear host** (not a cyclic word), and uniqueness is literal, not merely up to symmetry. Unary forbidden patterns and patterns of length other than three are not included in the new theorem.

## Proof
**1. Two symmetry orbits.** Reversal preserves subsequence containment after reversing both words, and exchanging the symbols \(0\) and \(1\) also preserves it. These operations map admissible hosts bijectively, preserving lengths and uniqueness. The six nonconstant triples split into the two orbits \(\{001,100,110,011\}\) and \(\{010,101\}\). It suffices to treat \(001\) and \(010\).

**2. Case \(u=001\): forced run lower bound.** Any admissible host contains \(0^k\), because this target avoids \(001\). Hence it contains at least \(k\ge3\) zeros. A word that avoids \(001\) cannot have a \(1\) after its second zero: those two zeros and the later \(1\) would form a forbidden subsequence. Since the host must also contain the permitted target \(0\,1^{k-1}\), it has a \(1\) after its first zero. Consequently every admissible host has the unique canonical decomposition
\[
W=1^a0\,1^b0^c,\qquad a\ge0,\ b\ge1,\ c\ge1.
\]
The target \(1^{k-2}01\) must use the first zero (there is no \(1\) after the later zeros); therefore \(a\ge k-2\). The target \(01^{k-1}\) forces \(b\ge k-1\), because the first zero is the only zero preceding any ones. The target \(0^k\) forces \(1+c\ge k\), so \(c\ge k-1\). Thus
\[
|W|=a+1+b+c\ge(k-2)+1+(k-1)+(k-1)=3k-3.
\]
Equality forces all three run lengths, so at most one minimum host is possible.

**3. Case \(u=001\): covering all permitted targets.** Put
\[
W_1=1^{k-2}0\,1^{k-1}0^{k-1}.
\]
It avoids \(001\) because no \(1\) lies after the second zero. Let \(x\in\mathcal A_k(001)\).

If \(x\) contains at least two zeros, all its ones occurring after the first zero must precede the second zero. Thus \(x=1^i0\,1^j0^c\) with \(c\ge1\) and \(i+j+c+1=k\). In particular \(i\le k-2\), \(j\le k-2\), and \(c\le k-1\), so the four blocks embed respectively into the four blocks of \(W_1\). If \(x\) contains exactly one zero, write \(x=1^i0\,1^j\) with \(i+j=k-1\). If \(j\ge1\), then \(i\le k-2\), so it embeds through the first zero, with its trailing ones inside the middle block. If \(j=0\), it embeds by selecting \(k-1\) of the \(2k-3\) ones preceding the last zero. The all-ones target \(1^k\) also embeds, as \(2k-3\ge k\) for \(k\ge3\). Therefore \(W_1\) is admissible; the lower bound and equality conditions prove it is the unique optimum.

**4. Case \(u=010\): forced run lower bound.** In any word avoiding \(010\), all zeros occur contiguously: a zero, then a one, then another zero would otherwise be a forbidden subsequence. Every admissible host must contain \(0^k\), so it has the form
\[
W=1^a0^b1^c,\qquad b\ge k.
\]
The permitted targets \(1^{k-1}0\) and \(01^{k-1}\) impose respectively \(a\ge k-1\) and \(c\ge k-1\), as there is a unique zero run. Consequently \(|W|\ge3k-2\), with equality possible only for
\[
W_2=1^{k-1}0^k1^{k-1}.
\]
Every \(010\)-avoiding target containing a zero has form \(1^i0^j1^\ell\), where \(j\ge1\), \(i+\ell+j=k\). Its three runs embed into the corresponding runs of \(W_2\), since \(i,\ell\le k-1\) and \(j\le k\). The all-ones target embeds because \(2(k-1)\ge k\) for \(k\ge2\). Hence \(W_2\) is admissible and uniquely shortest.

The symmetry reduction completes the proof for all six nonconstant triples. The formula \(L=3k-4+\tau(u)\) simply records the two values by the number of adjacent changes. \(\square\)

## Verification
The self-contained `verify.py` implements literal subsequence matching and an independent breadth-first search over the vector of greedy-progress states for every permitted target. For all eight length-three binary patterns and \(3\le k\le7\), it exhaustively determines the shortest length and number of shortest hosts (40 cases), confirming uniqueness and the displayed formulas, including the already-known unary controls. For \(3\le k\le12\), direct checking of all binary length-\(k\) targets against the proposed hosts performs 65,472 individual tests. Run with `python3 verify.py`; expected final output is `VERIFY_OK coverage_instances 65472 BFS_instances 40`. These finite checks corroborate but do not replace the all-\(k\) proof.

## Relationship to prior work
The main context is the study of missing scattered factors and subsequence universality, including Fleischmann et al., *m-Nearly k-Universal Words – Investigating Simon Congruence* (arXiv:2202.07981, 2022), and Adamson et al., *Tight Bounds for the Number of Absent Subsequences* (arXiv:2407.18599, first public July 26, 2024). The former characterizes near-universality and sets of absent subsequences; the latter optimizes absent-subsequence *counts* at a fixed universality index. Neither of these statements establishes the minimum length and uniqueness of a host which itself avoids one prescribed nonconstant triple yet covers **all** permitted length-\(k\) targets. A general constrained-cover construction gives upper bounds, and the unary forbidden-pattern optimum is known; the present theorem resolves the entire first nonunary binary class. Ordinary shortest-common-supersequence formulations which permit the host to contain the forbidden pattern are not equivalent.

## Limitations
This is an exact result only for nonconstant binary forbidden words of length three. It does not determine the optimum for longer forbidden words, larger alphabets, hosts that may contain the forbidden word, or hosts subject to other constraints. The originality comparison cannot exclude unindexed or unavailable equivalents; no independent mathematical audit has been undertaken. Tests at finite values of \(k\) do not constitute an infinite proof.

## References
1. P. Fleischmann, L. Haschke, A. Huch, A. Mayrock, and D. Nowotka, *m-Nearly k-Universal Words – Investigating Simon Congruence*, arXiv:2202.07981 (first publicly posted February 16, 2022), https://arxiv.org/abs/2202.07981.
2. D. Adamson, P. Fleischmann, A. Huch, F. Manea, P. Sarnighausen-Cahn, and M. Wiedenhöft, *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599 (first publicly posted July 26, 2024), https://arxiv.org/abs/2407.18599.
3. D. Adamson et al., *k-Universality of Regular Languages*, arXiv:2311.10658 (2023), https://arxiv.org/abs/2311.10658.
