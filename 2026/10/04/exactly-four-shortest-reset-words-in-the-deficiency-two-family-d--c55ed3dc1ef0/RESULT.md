# Exactly four shortest reset words in the deficiency-two family \(D_n\)
## Finding
For every integer \(n>4\), let \(D_n\) be the synchronizing automaton on \(Q=\{1,\ldots,n\}\) with letters \(a,b,c\) defined by \(a(1)=a(2)=a(3)=1\) and \(a(q)=q\) for \(4\le q\le n\); \(b(1)=b(2)=1\), \(b(3)=2\), and \(b(q)=q\) for \(4\le q\le n\); and \(c(1)=4\), \(c(2)=1\), \(c(3)=4\), \(c(q)=q+1\) for \(4\le q<n\), and \(c(n)=3\). Then the complete set of shortest reset words is
\[
\left\{x c\,(b c^{n-1})^{n-4} b c y : x,y\in\{a,c\}\right\}.
\]
Hence \(D_n\) has exactly four shortest reset words, each of length \((n-2)^2+1\). The two ending in \(a\) reset to state \(1\), and the two ending in \(c\) reset to state \(4\). In particular, the deficiency-two letter \(a\) occurs in a shortest reset word only at the first position, the last position, or both.
## Assumptions and scope
The statement uses exactly the transition convention above. It applies to every integer \(n>4\). It classifies words of minimum reset length only; it makes no claim about longer reset words or about other deficiency-two automata.
## Proof
The defining paper proves that the reset threshold of \(D_n\) is \((n-2)^2+1\) by tracking coins and holes on the main circle \(C=\{3,4,\ldots,n\}\). Its equality argument gives two facts that determine every optimal word.

First, any shortest reset word must begin with either \(ac\) or \(c^2\), and both prefixes map the full state set onto \(C\). After this entry step, each decrease in the number of active states is a proper merge of the adjacent active pair positioned at \(3\) and \(n\). The source's case analysis of proper merging words shows that the only merges of the minimum possible length \(3\) are \(bcc\) and \(bca\).

Second, after a nonfinal merge, the newly merged coin must be returned to state \(3\) before the next hole-growth step. A merge by \(bcc\) ends at state \(4\); the source lower bound requires \(n-3\) occurrences of \(c\) to return it to \(3\). Equality in the total reset-length bound leaves exactly \(n-3\) positions for this transport, so the transport word is forced to be \(c^{n-3}\). Thus every nonfinal merge-and-transport block is
\[
 bcc\,c^{n-3}=bc^{n-1}.
\]
A nonfinal merge by \(bca\) ends at state \(1\). The next \(c\) only moves that coin to state \(4\), after which the same \(n-3\) further occurrences of \(c\) are still required to reach \(3\). Its transport therefore costs at least \(n-2\), one more than equality permits. Consequently all of the first \(n-4\) merges are forced to be \(bcc\), followed by the forced transport \(c^{n-3}\).

There is no transport after the last merge, so its minimum-length choice may be either \(bcc\) or \(bca\). Combining the two possible entry prefixes with the two possible final merges yields exactly
\[
 x c\,(b c^{n-1})^{n-4} b c y,\qquad x,y\in\{a,c\}.
\]
Every such word has length \(2+n(n-4)+3=(n-2)^2+1\), so all four are shortest. Directly on the final pair \(\{3,n\}\), \(bcc\) merges to state \(4\) while \(bca\) merges to state \(1\), proving the target split.
## Verification
The included `verify.py` independently builds the transition maps above and performs exact breadth-first search in the power automaton for every \(5\le n\le16\). In each case it finds reset length \((n-2)^2+1\), exactly four shortest paths to singleton subsets, two ending at state \(1\) and two at state \(4\). It separately generates the four displayed words and replays them directly for every \(5\le n\le100\). These finite checks stress-test the symbolic proof; they are not used to replace its universal argument.
## Relationship to prior work
Ananichev, Volkov, and Zaks define \(D_n\), prove the exact threshold \((n-2)^2+1\), and exhibit one shortest reset word, \(c^2(bc^{n-1})^{n-4}bc^2\). Their lower-bound proof contains the equality constraints used above, but it does not state the complete set or the number of shortest reset words. Later shortest-reset-word algorithms compute an optimum word or its length for a given automaton; the inspected algorithmic work does not supply this all-optimal-word classification for \(D_n\).
## Limitations
The novelty claim is a statement-level comparison with the inspected primary and algorithmic literature, not a claim that every unpublished computation has been excluded. The classification is an equality-case refinement of the original threshold proof rather than a new reset-threshold bound. The finite verifier covers only bounded \(n\); the all-\(n\) result rests on the proof above and the cited structural lemmas.
## References
D. S. Ananichev, M. V. Volkov, and Yu. I. Zaks, “Synchronizing Automata with a Letter of Deficiency 2,” *Developments in Language Theory*, Lecture Notes in Computer Science 4036, 2006, DOI 10.1007/11779148_39.

D. S. Ananichev, M. V. Volkov, and Yu. I. Zaks, “Synchronizing automata with a letter of deficiency 2,” *Theoretical Computer Science* 376 (2007), DOI 10.1016/j.tcs.2007.01.010.

A. Kisielewicz, J. Kowalski, and M. Szykuła, “Computing the shortest reset words of synchronizing automata,” *Journal of Combinatorial Optimization* 29 (2015), DOI 10.1007/s10878-013-9682-0.
