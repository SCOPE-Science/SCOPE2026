# Complete quaternary single-tail-deletion optimal-code spectrum and minimum ranking length

## Finding

Let \(\Sigma\) be a fixed labeled alphabet of four symbols. A *partial permutation* is a nonempty word with no repeated symbols, of any length from one through four. Let \(\mathcal P\) be the set of all such words. For a word \(w\), the one-tail-deletion ball is \(B(w)=\{w\}\) if \(|w|=1\), and \(B(w)=\{w,w_{2}\cdots w_{|w|}\}\) otherwise. A code \(C\subseteq\mathcal P\) is correcting when \(B(u)\cap B(v)=\varnothing\) for all distinct \(u,v\in C\).

The maximum code size, already established in the motivating literature, is \(28\). Among *all* labeled maximum codes there are exactly
\[
  54^4=8{,}503{,}056
\]
distinct codebooks. In fact, writing \(n_j(C)=\#\{w\in C:|w|=j\}\), their complete length-composition enumerator is
\[
  \sum_{\substack{C\subseteq\mathcal P\\C\text{ correcting}\\|C|=28}}
  x_1^{n_1(C)}x_2^{n_2(C)}x_3^{n_3(C)}x_4^{n_4(C)}
  =P(x_1,x_2,x_3,x_4)^4,
\]
where
\[
 P=x_1x_4^3(x_4+2x_3)^3+3x_2x_4^4(x_4+2x_3)^2.
\]
Equivalently, the distribution by total word length \(\Lambda(C)=\sum_{w\in C}|w|\) has polynomial
\[
 \sum_{\substack{C\subseteq\mathcal P\\C\text{ correcting}\\|C|=28}} t^{\Lambda(C)}
 =\bigl[t^{22}(t+2)^2(3t^2+t+2)\bigr]^4.
\]
Thus the least possible total ranking length of a maximum code is exactly \(88\), attained by exactly \(4{,}096\) labeled codes. These and only these minimizers have \(4\) words of length one, \(12\) words of length three, and \(12\) words of length four. The maximum total length within maximum codes is \(104\), attained by exactly \(81\) codes.

## Assumptions and scope

The alphabet is labeled: codebooks related by symbol relabeling are counted separately when their actual word sets differ. Words may have any nonzero length at most four but have no repeated letter. An error removes the *first* symbol of a word at most once and never removes the final symbol. The cost \(\Lambda\) is a purely combinatorial total of ranking positions; no experimental synthesis-cost or decoding-performance claim is made.

## Proof

**Confusability lemma.** Every nonempty suffix of a partial permutation has the same last letter. For distinct words \(u,v\), their one-tail-deletion balls intersect exactly when either (i) one word is obtained from the other by deleting its first letter, or (ii) they have equal length at least two and the same suffix after deleting their first letters. The balls otherwise have incompatible output lengths or different output words. Hence the confusability graph has parent–child edges and a clique among the children of each suffix-tree vertex; different terminal-letter components are disjoint.

Fix one terminal letter \(a\). The sixteen partial permutations ending in \(a\) form a rooted suffix tree with one length-one root, three length-two children, six length-three grandchildren, and six length-four leaves. The root together with its three children forms a clique. The six length-three nodes each have exactly one length-four child; these six parent–child pairs are edges. The clique and these six edges partition all sixteen vertices. A correcting code therefore selects at most one word from each of seven disjoint groups, giving a bound of seven words with last letter \(a\). This bound is achieved by the root and all six leaves. There are four last letters, so the global maximum is \(4\cdot7=28\), independently recovering the known cardinality bound.

Equality forces exactly one choice from the four-element short-word clique and exactly one choice from each length-three/length-four pair. Group the six pairs by their three common length-two parent words, two pairs per parent. In a parent group, selecting the two length-three words is forbidden because they are siblings. The three allowed choices are (a) both length-four children, or (b) exactly one length-three word and its opposite length-four child (two labeled choices). Their length weights are \(x_4^2+2x_3x_4=x_4(x_4+2x_3)\).

If the short choice is the root \(a\), all three parent groups make independent choices, yielding weight \(x_1[x_4(x_4+2x_3)]^3\). If the short choice is one of the three length-two words, both of its length-three children are forbidden and their two corresponding length-four children are forced. The other two parent groups remain free, giving weight \(3x_2x_4^2[x_4(x_4+2x_3)]^2\). Adding the two cases gives exactly the stated polynomial \(P\). Since distinct terminal-letter components have disjoint deletion outputs, their choices combine independently, proving the fourth power.

Setting every \(x_j=1\) gives \(P(1,1,1,1)=3^3+3\cdot3^2=54\), hence \(54^4\) codebooks. Setting \(x_j=t^j\) gives \(P(t,t^2,t^3,t^4)=t^{22}(t+2)^2(3t^2+t+2)\). Its smallest monomial is \(8t^{22}\): each terminal-letter component selects its length-one root, exactly one of two length-three siblings in each of three groups, and the other three length-four leaves. Its largest monomial is \(3t^{26}\): each component selects one of the three length-two words and all six length-four leaves. Positivity of coefficients makes both extremes sharp, with global multiplicities \(8^4\) and \(3^4\). This also proves the asserted unique minimum-length composition.

For completeness, a transfer recurrence enumerates every (not just maximum) code for any alphabet size \(q\ge2\). For a node with \(b\) possible one-letter prefixes, let \(U_b\) enumerate correcting selections in its descendant subtree excluding the node, and \(V_b\) those including it; use a variable \(z\) per chosen word and \(x_j\) for its length \(j\). With \(U_0=1\), \(V_0=zx_q\), and \(1\le b\le q-1\),
\[
 U_b=U_{b-1}^{\,b}+bV_{b-1}U_{b-1}^{\,b-1},
 \qquad V_b=zx_{q-b}U_{b-1}^{\,b}.
\]
The generating polynomial over all correcting codes is \((U_{q-1}+V_{q-1})^q\). Here the first term excludes all children; the second selects one of the sibling children; selection of the root excludes all children. This recurrence follows from exactly the same confusability lemma and specializes to the quaternary result above.

## Verification

The standalone program `verify.py` constructs the actual deletion balls and exhaustively checks all subsets of the sixteen vertices in one terminal-letter component for \(q=4\) (all \(65{,}536\) subsets). It compares their full independence polynomial with a separately implemented subtree recurrence. The maximum is seven, achieved by exactly 54 local codes, and the complete optimal length profiles agree term by term with \(P\). The program also independently checks the smaller cases \(q=2,3\), computes additional recurrence examples for \(q=5,6\), and ends with `VERIFY_OK`. The infinite-in-\(q\) recurrence follows from the proof, not from these finite tests. The program output is included as `verify_output.txt`.

## Relationship to prior work

Cohen, Yaakobi, and Yakhini (2026) define this variable-length partial-permutation tail-deletion model and establish the maximum size of one-tail-deletion-correcting codes as a special case of their general theorem; they exhibit optimal constructions. The value \(28\) is therefore **not** claimed as new. The present result instead counts *all* optimal quaternary codebooks, gives every length-composition frequency, and optimizes total ranking length among maximum codes. The earlier rank-modulated composite-encoding paper concerns the general encoding framework and a different ranking-error model. A full-text inspection of the May 2026 tail-deletion paper found no stated enumeration of all optimal codebooks or minimum total ranking-length classification.

## Limitations

The enumeration uses the exact single-prefix-deletion model with at most one deletion and variable-length partial permutations. It does not apply to ordinary subsequence deletion at arbitrary positions, two tail deletions, indel errors, or stochastic decoding. Rank length is a mathematical proxy and not a measured physical cost. Equivalence under alphabet relabeling is not factored out; all numbers count labeled codebooks. Undetected equivalent formulations in general suffix-tree packing or finite-code literature remain possible; absence from searched records is not proof of universal novelty.

## References

1. T. Cohen, E. Yaakobi, and Z. Yakhini, *Correcting Tail Deletions in Rank Modulated Composite Encoding for Data Storage in DNA*, arXiv:2605.19148v1, first submitted 2026-05-18, especially Sections II–IV and Theorem 6. https://arxiv.org/abs/2605.19148
2. T. Cohen, Z. Wang, E. Yaakobi, and Z. Yakhini, *Rank Modulated Composite Encoding for Data Storage in DNA*, ISTC 2025, DOI:10.1109/ISTC65386.2025.11154607. https://doi.org/10.1109/ISTC65386.2025.11154607
