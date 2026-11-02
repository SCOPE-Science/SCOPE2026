# One-letter slack rigidity in the Černý reset language

## Finding
Let \(n\ge 2\). On \(Q=\mathbb Z/n\mathbb Z\), let the two-letter deterministic automaton have transitions
\[
 a:i\mapsto i+1\pmod n,\qquad
 b:i\mapsto\begin{cases}0,&i=n-1,\\i,&0\le i\le n-2.\end{cases}
\]
A word is *resetting* if its action maps \(Q\) to a singleton. A word *first resets at its final letter* if it is resetting and its proper prefix obtained by deleting its last letter is not resetting. Put \(L=(n-1)^2\) and
\[
 W=b(a^{n-1}b)^{n-2}.
\]
The only reset word of length \(L\) is \(W\); none is shorter. Exactly \((n-2)^2+1\) words of length \(L+1\) first reset at their last letter. The complete list consists of \(aW\) and, for \(1\le j\le n-2\) and \(0\le t\le n-2\) with \(t\ne j\), the words
\[
 b(a^{n-1}b)^{j-1}a^tba^{n-1-t}b(a^{n-1}b)^{n-2-j}.
\]
These are all distinct. Consequently, counting words that reset at or before their last letter, there are exactly \((n-2)^2+3\) resetting words of length \(L+1\). The empty ranges in the displayed family are understood literally when \(n=2\), leaving only \(aW=ab\) as a first-at-final-letter word.

## Assumptions and scope
The state labels and transition convention are fixed above; input words act from left to right. Counts concern distinct labeled words, not cyclic equivalence classes. A word that first resets at length \(L+1\) need not be minimal under deletion of an arbitrary internal letter. The counting distinction is important: the two additional words \(Wa\) and \(Wb\) of length \(L+1\) already reset after \(L\) letters.

## Proof
**1. Reverse preimages and an interval-growth bound.** For a subset \(S\subseteq Q\), write \(S\ell^{-1}\) for its complete preimage under a letter. One has
\[
 Sa^{-1}=S-1,
 \qquad
 Sb^{-1}=\begin{cases}
 S\cup\{n-1\},&0\in S,\ n-1\notin S,\\
 S\setminus\{n-1\},&0\notin S,\ n-1\in S,\\
 S,&\text{otherwise.}
 \end{cases}
\]
If \(w\) resets to \(q\), applying these preimages in reverse letter order starting from \(\{q\}\) yields \(Q\). Process the reverse word again, *ignoring* each inverse \(b\)-step unless it strictly increases the currently maintained set. At every stage the maintained set contains the true preimage set: this follows by induction from monotonicity of inverse images, since an ignored \(b^{-1}\) either shrinks or fixes the maintained set. The final maintained set is therefore also \(Q\).

Starting from a singleton, all maintained sets are cyclic intervals. Indeed, rotations preserve intervals; an increasing \(b^{-1}\) can occur only on the interval \(\{0,1,\ldots,k-1\}\) and changes it to \(\{n-1,0,\ldots,k-1\}\). For an interval of size strictly between \(1\) and \(n\), this is the *unique orientation* in which \(b^{-1}\) increases its size. Hence, between successive increasing inverse \(b\)-steps, at least \(n-1\) inverse \(a\)-steps are required. Exactly \(n-1\) increases are needed to pass from size one to size \(n\). Thus **every resetting word contains at least** \((n-1)(n-2)\) occurrences of \(a\) and at least \(n-1\) occurrences of \(b\), giving length at least \(L\). This argument allows arbitrary interspersed shrinking or idle inverse steps; pruning them cannot invalidate the lower bound.

If a word first resets at its last letter, that letter must be \(b\), since \(a\) is a permutation. Moreover that last \(b\) must merge \(0\) and \(n-1\), so the final image is \(\{0\}\) and the reverse preimage construction starts at \(\{0\}\). With exactly \((n-1)(n-2)\) inverse \(a\)-steps, the first expansion occurs immediately, each intervening rotation has exactly \(n-1\) steps, and there are none after the final expansion. This follows because the first and inter-expansion rotations are fixed modulo \(n\), while any nonminimal choice adds a whole \(n\) steps. Exactly \(n-1\) occurrences of \(b\) are then all expanding, producing the unique reverse sequence \(b(a^{n-1}b)^{n-2}\). It reads the same forwards, proving uniqueness of \(W\) at length \(L\).

**2. The one-letter budget.** Consider a word that first resets at its last letter at length \(L+1\). The bounds just proved leave only two possibilities for its letter counts:
\[
 (|w|_a,|w|_b)=\bigl((n-1)(n-2)+1,n-1\bigr)
 \quad\text{or}\quad
 \bigl((n-1)(n-2),n\bigr).
\]
In the first case all inverse \(b\)'s increase cardinality, and the extra inverse \(a\) cannot occur before or between increases: there the permitted number of rotations differs from the minimum by a multiple of \(n\), never by one. It must occur after the reverse process has already attained \(Q\). Reading forwards yields exactly \(aW\).

In the second case, the inverse process has \(n\) occurrences of \(b\). None can shrink the set: if one decreased size, the other \(n-1\) occurrences could increase it by at most \(n-1\), insufficient for a net gain of \(n-1\). Hence exactly \(n-1\) are expanding and the remaining one fixes the set. Deleting that identity step leaves the unique \(L\)-letter path just established. Equivalently, every such word is obtained by inserting one \(b\) into \(W\), and the insertion must be an inverse-state identity at the point where the redundant letter occurs.

**3. Exact admissible insertion positions.** In the reverse growth path, immediately after the \(r\)-th expansion, the set is \(S_r=\{n-1,0,\ldots,r-1\}\) for \(1\le r\le n-2\). After \(k\) inverse rotations, with \(0\le k\le n-2\), inverse \(b\) fixes the set exactly when \(k=0\) or \(1\le k\le n-2\) and \(k\ne r\). At \(k=r\) it instead deletes \(n-1\); after \(n-1\) rotations, the next canonical \(b^{-1}\) is expanding. An insertion immediately before that expansion can equivalently be assigned immediately after it, so boundary insertions are counted only once. The insertion immediately after the *first* reverse expansion is forbidden, since it creates a final `bb` in the forward word, which would already reset one letter earlier. The insertion after the *last* reverse expansion produces an initial `bb` in the forward word and is allowed for \(n\ge3\).

Reindexing the reverse gaps from right to left gives the displayed forward family: in its \(j\)-th \(a^{n-1}\)-block, put the extra \(b\) after \(t\) copies of \(a\). The boundary value \(t=n-1\) is the same physical insertion as \(t=0\) in the next block (or is an impermissible trailing `bb`), so use \(0\le t\le n-2\). For positive \(t\), the corresponding inverse offset is \(k=n-1-t\), in the reverse gap \(r=n-1-j\); the sole prohibited shrink offset \(k=r\) is exactly \(t=j\). At \(t=0\), the adjacent pair of \(b\)'s has one productive and one idle inverse step, and is permitted. Therefore the admissible positions are precisely \(t\ne j\). They give \(n-2\) choices in each of the \(n-2\) blocks and are different as words. For \(n=2\), a direct one-state-growth check shows no second-case word that first resets at its final letter. Together with \(aW\) this proves \((n-2)^2+1\).

**4. Total number of resets at the next length.** The only word first resetting at length \(L\) is \(W\). A length-\(L+1\) word that was already reset at an earlier prefix must therefore be \(Wa\) or \(Wb\), whereas all other resetting words at this length are precisely those just classified. The total is \((n-2)^2+3\). \(\square\)

## Verification
The standalone `verify.py` independently constructs the full subset transition graph for every \(2\le n\le11\). Integer dynamic programming counts all words according to their *first* synchronizing prefix length without enumerating exponentially many words. It confirms the unique shortest word, the complete explicit candidate list, and the values \(1,2,5,10,17,26,37,50,65,82\) of first-at-next-length counts. Direct simulation also checks that each listed word first resets at its last letter. Run with `python3 verify.py`; success ends with `VERIFY_OK`. These checks are finite corroboration; the argument above is the all-length proof.

## Relationship to prior work
The classical Černý family has minimum reset length \((n-1)^2\) (Černý, 1964). Kisielewicz, Kowalski and Szykuła (first publicly available online 17 November 2013) give algorithms for shortest reset words and analyze reverse subset search for the family, but do not supply the stated count or classification of first-reset words one letter above optimum in the inspected article. Stoner's 2014 manuscript investigates reset thresholds for automata with cyclic permutations and merging arcs; its studied quantity is the shortest length, not near-optimal word multiplicity. Two public results on the same automaton determine early rank-deficiency thresholds and worst-case avoiding thresholds, respectively. Those extremal lengths do not determine how many full-set reset words first synchronize at length \((n-1)^2+1\) or their complete forms. The formula here is derived directly, not inferred from the absence of a matching title or from finite experiments.

## Limitations
The classification is specific to the labeled two-letter Černý family and one letter of slack above the optimum. It makes no claim about general synchronizing automata, further near-optimal lengths, or the open Černý conjecture. Priority is assessed against the located material; exact older formulations outside indexed or accessible sources could remain. The distinction between prefix-first synchronization and arbitrary subsequence-minimality must be retained.

## References
1. J. Černý, “Poznámka k homogénnym experimentom s konečnými automatmi,” *Matematicko-fyzikálny časopis* 14 (1964), 208–216.
2. A. Kisielewicz, J. Kowalski and M. Szykuła, “Computing the shortest reset words of synchronizing automata,” *Journal of Combinatorial Optimization* 29 (2015), 88–124; first published online 17 November 2013. DOI: 10.1007/s10878-013-9682-0. https://link.springer.com/article/10.1007/s10878-013-9682-0
3. D. Stoner, “On the Minimal Reset Words of Synchronizing Automata,” manuscript, 30 July 2014. https://studylib.net/doc/10483209/on-the-minimal-reset-words-of-synchronizing-automata
4. “Exact early deficiency profile of the Černý automata,” public research record (2026). https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-early-deficiency-profile-of-the-ern-automata--766d362d36d3
5. “Exact k-avoiding thresholds of the Černý automata,” public research record (2026). https://github.com/Resultary/2026/tree/main/2026/9/17/SCOPE-cerny-k-avoiding-thresholds--5cdbaf373a0f
